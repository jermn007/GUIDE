# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

GUIDE (Grounded Universal Instructional Design Evaluator) is a **LLM-as-a-judge evaluation framework** for assessing AI assistant responses and instructional artifacts against peer-reviewed learning science rubrics. It exposes 9 evaluation archetypes covering 54 dimensions total, each grounded in named research (Knowles, Mayer, Sweller, Gagne, etc.).

## Running the Framework

There is no build step. GUIDE is a pure Python library.

**List all registered archetypes:**
```bash
python guide_registry.py
```

**Quick evaluation smoke test:**
```python
from guide_registry import evaluate
result = evaluate("adult_learning_communication", input="...", output="...")
print(result.overall_score, result.scores, result.improvement_suggestions)
```

**Install dependencies by usage mode:**
```bash
# Standalone (Anthropic SDK only)
pip install anthropic

# LangChain mode
pip install langchain-anthropic langchain-core

# LangSmith evaluation pipelines
pip install langsmith langchain-anthropic
```

## Architecture

### Registration Pattern

Archetypes self-register at import time. Each `archetype_XX_*.py` module calls `register_archetype()` at module level, which writes into `_REGISTRY` in `guide_base.py`. `archetypes/__init__.py` imports all 9 modules, so `import archetypes` is sufficient to populate the registry.

**`guide_registry.py`** is the public API — it imports `archetypes` (triggering all registrations), then re-exports the base functions with cleaner signatures (`input`/`output` vs the base's `user_input`/`assistant_output`).

### Core Files

- **`guide_base.py`** — all shared infrastructure: `GUIDEResult`, `CompositeResult`, `_REGISTRY`, and three evaluation runners:
  - `evaluate_standalone()` — uses the Anthropic SDK directly
  - `make_evaluator()` — returns a LangChain-compatible callable for LangSmith pipelines
  - `run_langsmith_eval()` — runs an archetype evaluator against a LangSmith dataset
- **`guide_registry.py`** — public entry point; thin wrappers + `evaluate_all()` (runs all 9 archetypes)
- **`archetypes/archetype_XX_*.py`** — each defines `JUDGE_SYSTEM_PROMPT` and `JUDGE_HUMAN_PROMPT` and calls `register_archetype()`

### Archetype File Convention

Each archetype module follows this pattern:
1. Module-level docstring with theoretical grounding and citations
2. `JUDGE_SYSTEM_PROMPT` — full rubric with per-dimension scoring tables (1-5 scale), required JSON output schema
3. `JUDGE_HUMAN_PROMPT` — template with `{input}`, `{output}`, `{context}`, `{reference}` placeholders
4. `register_archetype(name=..., system_prompt=..., human_prompt=..., description=..., version=...)`

### Judge Output Schema

Every judge LLM call must return this JSON structure (parsed by `GUIDEResult.from_json()`):
```json
{
  "scores": { "<dimension_name>": 1-5, ..., "overall": 1-5 },
  "rationale": { "<dimension_name>": "2-3 sentence justification", ... },
  "severity_flags": ["Nielsen severity 3-4 issues only"],
  "improvement_suggestions": ["top 1-3 actionable items"]
}
```

### Edge Case Files

`archetypes/edge_cases_XX.json` — labeled test sets (good/bad/borderline) with `expected_overall` scores. Used for regression testing as models evolve. Each entry has `id`, `label`, `expected_overall`, `target_dimensions`, `input`, `context`, `output`, `reference`.

### Handoff Docs

`archetypes/handoff_XX_*.md` — implementation notes for each archetype, not loaded at runtime.

## Adding a New Archetype

1. Create `archetypes/archetype_10_name.py` following the existing pattern
2. Define `JUDGE_SYSTEM_PROMPT` (rubric with JSON output schema), `JUDGE_HUMAN_PROMPT` (4 placeholders)
3. Call `register_archetype()` at module level
4. Add `from . import archetype_10_name` to `archetypes/__init__.py`
5. Create `archetypes/edge_cases_10.json` and `archetypes/handoff_10_name.md`

## Default Model

All evaluation runners default to `claude-sonnet-4-20250514`. Override with the `model_name` parameter.
