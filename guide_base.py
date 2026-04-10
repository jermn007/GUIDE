"""
GUIDE Base - Shared Infrastructure for All Evaluation Archetypes
=================================================================
GUIDE: Grounded Universal Instructional Design Evaluator

Provides the common data classes, evaluation runners, and LangChain/LangSmith
integration used by all archetype modules. Each archetype defines its own
JUDGE_SYSTEM_PROMPT and JUDGE_HUMAN_PROMPT; this module provides the machinery
to execute them.

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from typing import Optional, Callable


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

@dataclass
class GUIDEResult:
    """Result from a single evaluation run."""

    archetype: str = ""
    scores: dict[str, int] = field(default_factory=dict)
    rationale: dict[str, str] = field(default_factory=dict)
    severity_flags: list[str] = field(default_factory=list)
    improvement_suggestions: list[str] = field(default_factory=list)
    raw_output: str = ""

    @property
    def overall_score(self) -> int:
        return self.scores.get("overall", 0)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_json(cls, text: str, archetype: str = "") -> "GUIDEResult":
        """Parse the judge LLM's JSON output into a result object."""
        cleaned = re.sub(r"```json\s*", "", text)
        cleaned = re.sub(r"```\s*$", "", cleaned)
        data = json.loads(cleaned)
        return cls(
            archetype=archetype,
            scores=data.get("scores", {}),
            rationale=data.get("rationale", {}),
            severity_flags=data.get("severity_flags", []),
            improvement_suggestions=data.get("improvement_suggestions", []),
            raw_output=text,
        )


@dataclass
class CompositeResult:
    """Result from running multiple archetypes against the same input."""

    results: list[GUIDEResult] = field(default_factory=list)

    @property
    def overall_scores(self) -> dict[str, int]:
        return {r.archetype: r.overall_score for r in self.results}

    @property
    def mean_overall(self) -> float:
        scores = [r.overall_score for r in self.results if r.overall_score > 0]
        return sum(scores) / len(scores) if scores else 0.0

    def to_dict(self) -> dict:
        return {
            "composite_mean": round(self.mean_overall, 2),
            "archetype_scores": self.overall_scores,
            "results": [r.to_dict() for r in self.results],
        }


# ---------------------------------------------------------------------------
# Archetype Registry
# ---------------------------------------------------------------------------

_REGISTRY: dict[str, dict] = {}


def register_archetype(
    name: str,
    system_prompt: str,
    human_prompt: str,
    description: str = "",
    version: str = "1.0.0",
):
    """Register an evaluation archetype with the global registry."""
    _REGISTRY[name] = {
        "name": name,
        "system_prompt": system_prompt,
        "human_prompt": human_prompt,
        "description": description,
        "version": version,
    }


def list_archetypes() -> list[str]:
    """Return names of all registered archetypes."""
    return list(_REGISTRY.keys())


def get_archetype(name: str) -> dict:
    """Get a registered archetype by name."""
    if name not in _REGISTRY:
        available = ", ".join(_REGISTRY.keys())
        raise KeyError(f"Archetype '{name}' not found. Available: {available}")
    return _REGISTRY[name]


# ---------------------------------------------------------------------------
# LangChain-Compatible Evaluator Factory
# ---------------------------------------------------------------------------

def make_evaluator(
    archetype_name: str,
    model_name: str = "claude-sonnet-4-20250514",
    temperature: float = 0.0,
) -> Callable:
    """
    Create a LangChain-compatible evaluator for a specific archetype.

    Returns a callable that accepts a dict with keys:
        - input: the user's question / artifact being evaluated
        - output: the assistant's response / artifact content
        - context: (optional) retrieved RAG context or source material
        - reference: (optional) reference/golden answer

    Usage with LangSmith:
        from guide_base import make_evaluator
        import archetypes.archetype_02_assessment_design  # registers itself

        evaluator = make_evaluator("assessment_design")
        client = Client()
        results = client.evaluate(predict_fn, data="ds", evaluators=[evaluator])
    """
    archetype = get_archetype(archetype_name)

    try:
        from langchain_anthropic import ChatAnthropic
        from langchain_core.messages import SystemMessage, HumanMessage
    except ImportError:
        raise ImportError(
            "Install langchain-anthropic: pip install langchain-anthropic langchain-core"
        )

    llm = ChatAnthropic(model=model_name, temperature=temperature, max_tokens=4096)

    def evaluate(run_output: dict) -> dict:
        human_msg = archetype["human_prompt"].format(
            input=run_output.get("input", ""),
            output=run_output.get("output", ""),
            context=run_output.get("context", "N/A"),
            reference=run_output.get("reference", "N/A"),
        )
        response = llm.invoke([
            SystemMessage(content=archetype["system_prompt"]),
            HumanMessage(content=human_msg),
        ])
        result = GUIDEResult.from_json(response.content, archetype=archetype_name)
        return {
            "key": f"guide_{archetype_name}",
            "score": result.overall_score,
            "comment": json.dumps(result.to_dict(), indent=2),
            "details": result.to_dict(),
        }

    return evaluate


# ---------------------------------------------------------------------------
# Standalone Evaluation (Anthropic SDK)
# ---------------------------------------------------------------------------

def evaluate_standalone(
    archetype_name: str,
    user_input: str,
    assistant_output: str,
    context: str = "N/A",
    reference: str = "N/A",
    model_name: str = "claude-sonnet-4-20250514",
    api_key: Optional[str] = None,
) -> GUIDEResult:
    """Evaluate a single response using the Anthropic SDK directly."""
    archetype = get_archetype(archetype_name)

    try:
        import anthropic
    except ImportError:
        raise ImportError("Install anthropic SDK: pip install anthropic")

    client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    human_msg = archetype["human_prompt"].format(
        input=user_input,
        output=assistant_output,
        context=context,
        reference=reference,
    )

    response = client.messages.create(
        model=model_name,
        max_tokens=4096,
        temperature=0.0,
        system=archetype["system_prompt"],
        messages=[{"role": "user", "content": human_msg}],
    )

    return GUIDEResult.from_json(response.content[0].text, archetype=archetype_name)


# ---------------------------------------------------------------------------
# Composite Evaluation (Multiple Archetypes)
# ---------------------------------------------------------------------------

def evaluate_composite(
    archetype_names: list[str],
    user_input: str,
    assistant_output: str,
    context: str = "N/A",
    reference: str = "N/A",
    model_name: str = "claude-sonnet-4-20250514",
    api_key: Optional[str] = None,
) -> CompositeResult:
    """
    Run multiple archetypes against the same input and return a composite result.

    Example:
        result = evaluate_composite(
            ["adult_learning_communication", "assessment_design", "accessibility_technical"],
            user_input="...",
            assistant_output="...",
        )
        print(result.mean_overall)
        print(result.overall_scores)
    """
    composite = CompositeResult()
    for name in archetype_names:
        r = evaluate_standalone(
            archetype_name=name,
            user_input=user_input,
            assistant_output=assistant_output,
            context=context,
            reference=reference,
            model_name=model_name,
            api_key=api_key,
        )
        composite.results.append(r)
    return composite


# ---------------------------------------------------------------------------
# LangSmith Dataset Evaluation
# ---------------------------------------------------------------------------

def run_langsmith_eval(
    archetype_name: str,
    dataset_name: str,
    predict_fn: Callable,
    model_name: str = "claude-sonnet-4-20250514",
    project_name: Optional[str] = None,
):
    """Run an archetype evaluator against a LangSmith dataset."""
    try:
        from langsmith import Client
    except ImportError:
        raise ImportError("Install langsmith: pip install langsmith")

    evaluator = make_evaluator(archetype_name, model_name=model_name)
    client = Client()

    return client.evaluate(
        predict_fn,
        data=dataset_name,
        evaluators=[evaluator],
        experiment_prefix=project_name or f"guide-{archetype_name}",
    )
