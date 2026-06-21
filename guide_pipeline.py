"""
GUIDE Pipeline - ADDIE Multi-Archetype Orchestrator
====================================================
GUIDE: Grounded Universal Instructional Design Evaluator (v3.2.0)

Extends guide_registry.py with a multi-archetype evaluation pipeline that maps
to the ADDIE lifecycle, applies archetype 10's curriculum-alignment cap rule,
and produces a structured verdict + targeted revision recommendations.

This module focuses on the *evaluation* side of the pipeline (end-to-end audit
of a complete or partial artifact set). For the *build* side (agents that
actually author content), see the Cowork plugin's agents/ directory.

Place this file at the GUIDE repo root alongside guide_base.py and
guide_registry.py. It imports from both.

Usage:

    from guide_pipeline import ADDIEPipeline

    pipeline = ADDIEPipeline(model_name="claude-sonnet-4-20250514")

    # Full evaluation of a course artifact set
    verdict = pipeline.run_evaluation(
        request="Course on customer retention for service reps",
        artifact={
            "needs_analysis": "...",            # archetype 07
            "objectives": "...",                # input to 10
            "lesson_plan": "...",               # archetype 03
            "scenarios": "...",                 # archetype 08 (optional)
            "neuro_design_notes": "...",        # archetype 09
            "multimedia_storyboard": "...",     # archetype 04
            "accessibility_spec": "...",        # archetype 05
            "conversational_responses": "...",  # archetype 01 (optional)
            "assessment": "...",                # archetype 02
            "formative_eval_plan": "...",       # archetype 06
        },
        context="Optional retrieval context or source material",
        reference="Optional gold-standard artifact for comparison",
    )

    print(verdict.composite_score)
    print(verdict.threshold_band)
    for action in verdict.next_actions:
        print(f"  - {action.fix_owner_archetype}: {action.action}")

Author: Jeremy Terhune
License: Apache-2.0 (matches GUIDE repo)
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional

from guide_base import GUIDEResult, CompositeResult, evaluate_standalone, list_archetypes


# ---------------------------------------------------------------------------
# Constants — archetype identifiers and ADDIE mapping
# ---------------------------------------------------------------------------

class Archetype(str, Enum):
    """Canonical archetype identifiers (must match registry names)."""
    ADULT_LEARNING       = "adult_learning_communication"   # 01 Implement
    ASSESSMENT_DESIGN    = "assessment_design"              # 02 Evaluate
    SEQUENCING           = "instructional_sequencing"       # 03 Design
    MULTIMEDIA           = "multimedia_design"              # 04 Develop
    ACCESSIBILITY        = "wcag_accessibility"             # 05 Develop
    FORMATIVE_EVAL       = "formative_evaluation_protocol"  # 06 Evaluate
    NEEDS_ANALYSIS       = "needs_analysis_front_end"       # 07 Analyze
    STORY_DESIGN         = "story_design"                   # 08 Design (optional)
    COGNITIVE_NEURO      = "cognitive_neuroscience"         # 09 Design
    CURRICULUM_ALIGNMENT = "curriculum_alignment"           # 10 Synthesis gate


# Map each artifact slot in the input dict → archetype that judges it.
# When a slot is absent the corresponding archetype is skipped.
ARTIFACT_TO_ARCHETYPE: dict[str, Archetype] = {
    "needs_analysis":           Archetype.NEEDS_ANALYSIS,
    "lesson_plan":              Archetype.SEQUENCING,
    "scenarios":                Archetype.STORY_DESIGN,
    "neuro_design_notes":       Archetype.COGNITIVE_NEURO,
    "multimedia_storyboard":    Archetype.MULTIMEDIA,
    "accessibility_spec":       Archetype.ACCESSIBILITY,
    "conversational_responses": Archetype.ADULT_LEARNING,
    "assessment":               Archetype.ASSESSMENT_DESIGN,
    "formative_eval_plan":      Archetype.FORMATIVE_EVAL,
}

# Phase ordering — used by the synthesizer when ranking findings by where in
# ADDIE the failure should be fixed (cheapest to fix earliest).
PHASE_ORDER: dict[Archetype, int] = {
    Archetype.NEEDS_ANALYSIS:       1,   # Analyze
    Archetype.SEQUENCING:           2,   # Design
    Archetype.STORY_DESIGN:         2,
    Archetype.COGNITIVE_NEURO:      2,
    Archetype.MULTIMEDIA:           3,   # Develop
    Archetype.ACCESSIBILITY:        3,
    Archetype.ADULT_LEARNING:       4,   # Implement
    Archetype.ASSESSMENT_DESIGN:    5,   # Evaluate
    Archetype.FORMATIVE_EVAL:       5,
    Archetype.CURRICULUM_ALIGNMENT: 6,   # Gate
}

# Archetype 10's cap rule: if Objective↔Assessment Coherence ≤ 2, the composite
# overall is capped at 3.0 no matter what else scores.
CAP_RULE_DIMENSION = "objective_assessment_coherence"
CAP_RULE_THRESHOLD = 2          # score ≤ this triggers the cap
CAP_RULE_CEILING   = 3.0        # composite cannot exceed this when triggered

# Threshold map for the final verdict band.
VERDICT_BANDS: list[tuple[float, str, str]] = [
    (4.5, "ship",           "Excellent — defensible to accreditors and learners; ship."),
    (3.5, "light_revision", "Good with gaps; address flagged dimensions before next cohort."),
    (2.5, "revise",         "Real misalignment; revise before delivery."),
    (0.0, "redesign",       "Misaligned; objectives, instruction, and assessment are effectively three different courses."),
]


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class FailFastResult:
    """Lightweight Design→Develop alignment check (single dimension)."""
    objective_strategy_coherence: int
    decision: str               # "proceed" or "block"
    block_reason: str = ""
    route_back_to: Optional[Archetype] = None

    def to_dict(self) -> dict:
        d = asdict(self)
        if self.route_back_to:
            d["route_back_to"] = self.route_back_to.value
        return d


@dataclass
class RevisionAction:
    """A single targeted revision instruction owned by one archetype's fixer."""
    fix_owner_archetype: str
    dimension: str
    current_score: int
    target_score: int
    action: str
    rationale: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class PipelineVerdict:
    """Final verdict produced by the synthesizer."""
    composite_score: float                       # 0.0-5.0, post-cap
    composite_score_uncapped: float              # what it would be without the cap
    alignment_cap_triggered: bool
    cap_reason: str
    threshold_band: str                          # ship / light_revision / revise / redesign
    band_explanation: str
    by_archetype: dict[str, dict]                # archetype name → {overall, top_finding}
    ranked_severity: list[dict]
    next_actions: list[RevisionAction]
    iteration_number: int = 1
    non_progress_flag: bool = False

    def to_dict(self) -> dict:
        return {
            "composite_score": round(self.composite_score, 2),
            "composite_score_uncapped": round(self.composite_score_uncapped, 2),
            "alignment_cap_triggered": self.alignment_cap_triggered,
            "cap_reason": self.cap_reason,
            "threshold_band": self.threshold_band,
            "band_explanation": self.band_explanation,
            "by_archetype": self.by_archetype,
            "ranked_severity": self.ranked_severity,
            "next_actions": [a.to_dict() for a in self.next_actions],
            "iteration_number": self.iteration_number,
            "non_progress_flag": self.non_progress_flag,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


# ---------------------------------------------------------------------------
# The pipeline
# ---------------------------------------------------------------------------

class ADDIEPipeline:
    """
    Multi-archetype evaluation pipeline mapped to ADDIE.

    Workflow:
      1. classify_request   → mode = build | review | partial
      2. fan_out_specialists → run each applicable archetype as a judge
      3. alignment_gate     → run archetype 10 across the artifact set; apply cap rule
      4. synthesize         → compose verdict (verdict + ranked findings)
      5. plan_revisions     → targeted, rubric-anchored revision actions
    """

    def __init__(
        self,
        model_name: str = "claude-sonnet-4-20250514",
        api_key: Optional[str] = None,
        max_iterations: int = 3,
    ):
        self.model_name = model_name
        self.api_key = api_key
        self.max_iterations = max_iterations
        self._verify_registry()

    # -- registry sanity check ---------------------------------------------

    def _verify_registry(self) -> None:
        """Confirm all 10 archetypes are registered (caller imports guide_registry)."""
        registered = set(list_archetypes())
        expected = {a.value for a in Archetype}
        missing = expected - registered
        if missing:
            raise RuntimeError(
                f"GUIDE pipeline cannot start: archetypes not registered: {sorted(missing)}.\n"
                "Make sure you've imported guide_registry (which auto-registers all archetypes)."
            )

    # -- 1. classify -------------------------------------------------------

    def classify_request(self, request: str, artifact: dict) -> str:
        """
        Decide the pipeline mode based on what's present in the artifact dict.
        - build:   request only, no artifact pieces yet (the orchestrator can't
                   build content itself — it will return a stub asking the user
                   to use the Cowork plugin agents to author the artifacts).
        - review:  full or near-full artifact set; do an end-to-end audit.
        - partial: some pieces present; audit what we have, flag what's missing.
        """
        present = {k for k, v in artifact.items() if v}
        if not present:
            return "build"
        # Define a "near-full" set: needs analysis + at least one design/develop + assessment
        full_signals = {"needs_analysis", "lesson_plan", "assessment"}
        if full_signals.issubset(present):
            return "review"
        return "partial"

    # -- 2. specialist fan-out --------------------------------------------

    def fan_out_specialists(
        self,
        artifact: dict,
        context: str = "N/A",
        reference: str = "N/A",
    ) -> list[GUIDEResult]:
        """
        Run each present artifact slot through its judging archetype.
        Skips archetype 10 here — that's the gate, called separately.
        """
        results: list[GUIDEResult] = []
        for slot, content in artifact.items():
            if not content:
                continue
            archetype = ARTIFACT_TO_ARCHETYPE.get(slot)
            if archetype is None or archetype == Archetype.CURRICULUM_ALIGNMENT:
                continue
            r = evaluate_standalone(
                archetype_name=archetype.value,
                user_input=f"Evaluate the {slot} artifact:",
                assistant_output=str(content),
                context=context,
                reference=reference,
                model_name=self.model_name,
                api_key=self.api_key,
            )
            results.append(r)
        return results

    # -- 2b. Design→Develop fail-fast (lightweight 10 check) ---------------

    def fail_fast_alignment(
        self,
        objectives: str,
        proposed_strategies: str,
        context: str = "N/A",
    ) -> FailFastResult:
        """
        Lightweight check between Design and Develop: run archetype 10 with
        objectives + strategies, look only at objective_strategy_coherence.
        Block when < 4.
        """
        combined_artifact = (
            "OBJECTIVES (from Phase A):\n"
            f"{objectives}\n\n"
            "PROPOSED STRATEGIES (from Phase D Design):\n"
            f"{proposed_strategies}\n"
        )
        r = evaluate_standalone(
            archetype_name=Archetype.CURRICULUM_ALIGNMENT.value,
            user_input="Fail-fast alignment check between objectives and proposed strategies.",
            assistant_output=combined_artifact,
            context=context,
            reference="N/A",
            model_name=self.model_name,
            api_key=self.api_key,
        )
        oss = int(r.scores.get("objective_strategy_coherence", 0))
        if oss >= 4:
            return FailFastResult(
                objective_strategy_coherence=oss,
                decision="proceed",
            )
        # Block; route back to the agent most responsible
        route_back = self._route_back_for_alignment_failure(r)
        return FailFastResult(
            objective_strategy_coherence=oss,
            decision="block",
            block_reason=r.rationale.get("objective_strategy_coherence", "Drift detected."),
            route_back_to=route_back,
        )

    @staticmethod
    def _route_back_for_alignment_failure(r: GUIDEResult) -> Archetype:
        """
        Heuristic: route alignment failures to whichever upstream phase is most
        likely the cause. If the rationale mentions Bloom-level or verb drift,
        send back to Needs Analysis (07); if it mentions sequencing or missing
        practice, send to Sequencing (03); otherwise default to 03.
        """
        text = (r.rationale.get("objective_strategy_coherence", "") + " ".join(r.severity_flags)).lower()
        if any(t in text for t in ("bloom", "verb", "objective", "mager")):
            return Archetype.NEEDS_ANALYSIS
        if any(t in text for t in ("scenario", "branching", "narrative", "story")):
            return Archetype.STORY_DESIGN
        if any(t in text for t in ("memory", "attention", "5e", "spaced")):
            return Archetype.COGNITIVE_NEURO
        return Archetype.SEQUENCING

    # -- 3. alignment gate (full archetype 10) ----------------------------

    def alignment_gate(
        self,
        artifact: dict,
        context: str = "N/A",
        reference: str = "N/A",
    ) -> GUIDEResult:
        """
        Full archetype-10 acceptance gate across the complete artifact set.
        Returns the raw GUIDEResult; the synthesizer applies the cap rule.
        """
        # Compose the full artifact set as one input for the judge.
        composed = "\n\n".join(
            f"### {slot.upper().replace('_', ' ')}\n{content}"
            for slot, content in artifact.items()
            if content
        )
        return evaluate_standalone(
            archetype_name=Archetype.CURRICULUM_ALIGNMENT.value,
            user_input="Acceptance-gate alignment check across the complete artifact set.",
            assistant_output=composed,
            context=context,
            reference=reference,
            model_name=self.model_name,
            api_key=self.api_key,
        )

    # -- 4. synthesize ----------------------------------------------------

    def synthesize(
        self,
        specialist_results: list[GUIDEResult],
        gate_result: GUIDEResult,
        iteration_number: int = 1,
        prior_composite_score: Optional[float] = None,
    ) -> PipelineVerdict:
        """
        Compose all archetype scorecards into a single verdict.
        Applies the archetype-10 cap rule.
        """
        all_results = specialist_results + [gate_result]

        # Per-archetype summary
        by_archetype: dict[str, dict] = {}
        for r in all_results:
            overall = r.overall_score
            top_finding = r.severity_flags[0] if r.severity_flags else (
                next(iter(r.improvement_suggestions), "") if r.improvement_suggestions else ""
            )
            by_archetype[r.archetype] = {
                "overall": overall,
                "top_finding": top_finding,
                "severity_flags": list(r.severity_flags),
            }

        # Uncapped composite = mean of all archetype overall scores
        valid_overalls = [r.overall_score for r in all_results if r.overall_score > 0]
        uncapped = sum(valid_overalls) / len(valid_overalls) if valid_overalls else 0.0

        # Cap rule: if archetype 10's objective_assessment_coherence ≤ threshold, cap composite
        cap_dim = int(gate_result.scores.get(CAP_RULE_DIMENSION, 5))
        cap_triggered = cap_dim <= CAP_RULE_THRESHOLD
        capped = min(uncapped, CAP_RULE_CEILING) if cap_triggered else uncapped
        cap_reason = (
            f"Archetype 10 {CAP_RULE_DIMENSION} = {cap_dim}; composite capped at {CAP_RULE_CEILING}."
            if cap_triggered else ""
        )

        # Verdict band
        band, explanation = self._verdict_for(capped)

        # Ranked severity
        ranked = self._rank_severity(all_results, gate_result)

        # Revision actions
        actions = self._plan_revisions(all_results, gate_result)

        # Non-progress check (only meaningful if a prior score is provided)
        non_progress = (
            prior_composite_score is not None
            and (capped - prior_composite_score) < 0.5
        )

        return PipelineVerdict(
            composite_score=round(capped, 2),
            composite_score_uncapped=round(uncapped, 2),
            alignment_cap_triggered=cap_triggered,
            cap_reason=cap_reason,
            threshold_band=band,
            band_explanation=explanation,
            by_archetype=by_archetype,
            ranked_severity=ranked,
            next_actions=actions,
            iteration_number=iteration_number,
            non_progress_flag=non_progress,
        )

    @staticmethod
    def _verdict_for(score: float) -> tuple[str, str]:
        for threshold, band, explanation in VERDICT_BANDS:
            if score >= threshold:
                return band, explanation
        return "redesign", VERDICT_BANDS[-1][2]

    @staticmethod
    def _rank_severity(all_results: list[GUIDEResult], gate_result: GUIDEResult) -> list[dict]:
        """
        Rank severity findings across all agents. Cross-corroboration boost: if
        multiple archetypes flag related issues, those rank higher.
        """
        flags: list[dict] = []
        for r in all_results:
            for flag in r.severity_flags:
                flags.append({
                    "archetype": r.archetype,
                    "finding": flag,
                    "corroborated_by": [],
                })
        # Simple corroboration heuristic: same keyword appearing in multiple flags
        for i, item in enumerate(flags):
            keywords = {w.lower() for w in item["finding"].split() if len(w) > 4}
            for j, other in enumerate(flags):
                if i == j:
                    continue
                other_kw = {w.lower() for w in other["finding"].split() if len(w) > 4}
                if keywords & other_kw:
                    item["corroborated_by"].append(other["archetype"])

        # Sort: gate findings first, then by corroboration count desc
        def sort_key(item: dict) -> tuple[int, int]:
            from_gate = 0 if item["archetype"] == Archetype.CURRICULUM_ALIGNMENT.value else 1
            return (from_gate, -len(item["corroborated_by"]))

        return sorted(flags, key=sort_key)

    def _plan_revisions(
        self,
        specialist_results: list[GUIDEResult],
        gate_result: GUIDEResult,
    ) -> list[RevisionAction]:
        """
        For each dimension that scored < 4, emit a targeted revision instruction
        owned by the archetype most responsible for the fix.
        """
        actions: list[RevisionAction] = []
        for r in [*specialist_results, gate_result]:
            for dim, score in r.scores.items():
                if dim == "overall":
                    continue
                try:
                    score_int = int(score)
                except (TypeError, ValueError):
                    continue
                if score_int >= 4:
                    continue
                suggestion = next(iter(r.improvement_suggestions), "")
                rationale = r.rationale.get(dim, "")
                actions.append(RevisionAction(
                    fix_owner_archetype=r.archetype,
                    dimension=dim,
                    current_score=score_int,
                    target_score=4,
                    action=suggestion or f"Lift {dim} to ≥ 4 per the rubric's anchors.",
                    rationale=rationale or "Below threshold per archetype scoring guide.",
                ))
        # Sort by ADDIE phase order (cheapest to fix earliest)
        actions.sort(key=lambda a: PHASE_ORDER.get(
            Archetype(a.fix_owner_archetype) if a.fix_owner_archetype in {x.value for x in Archetype} else Archetype.CURRICULUM_ALIGNMENT,
            99,
        ))
        return actions

    # -- 5. top-level convenience runner ----------------------------------

    def run_evaluation(
        self,
        request: str,
        artifact: dict,
        context: str = "N/A",
        reference: str = "N/A",
        iteration_number: int = 1,
        prior_composite_score: Optional[float] = None,
    ) -> PipelineVerdict:
        """
        End-to-end evaluation pipeline. Returns a PipelineVerdict.

        The orchestrator does *not* author content; that's the Cowork plugin's
        job. This function audits whatever is present in `artifact`, runs the
        alignment gate, and produces a structured revision plan the user (or a
        downstream builder agent) can act on.
        """
        mode = self.classify_request(request, artifact)
        if mode == "build":
            # Nothing to evaluate yet — signal upstream to use the build agents.
            return PipelineVerdict(
                composite_score=0.0,
                composite_score_uncapped=0.0,
                alignment_cap_triggered=False,
                cap_reason="",
                threshold_band="redesign",
                band_explanation=(
                    "No artifact pieces present. Use the Cowork plugin's agents to author "
                    "Needs Analysis → Design → Develop → Implement → Evaluate artifacts, "
                    "then re-run this pipeline against the resulting artifact set."
                ),
                by_archetype={},
                ranked_severity=[],
                next_actions=[],
                iteration_number=iteration_number,
            )

        specialist_results = self.fan_out_specialists(artifact, context, reference)
        gate_result = self.alignment_gate(artifact, context, reference)
        return self.synthesize(
            specialist_results,
            gate_result,
            iteration_number=iteration_number,
            prior_composite_score=prior_composite_score,
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="GUIDE ADDIE pipeline — multi-archetype evaluation of an instructional artifact set."
    )
    parser.add_argument("--request", required=True, help="The original training request or course goal.")
    parser.add_argument(
        "--artifact-json",
        required=True,
        help="Path to a JSON file with the artifact slots (see ARTIFACT_TO_ARCHETYPE).",
    )
    parser.add_argument("--context", default="N/A", help="Optional retrieval context or source material.")
    parser.add_argument("--reference", default="N/A", help="Optional gold-standard artifact for comparison.")
    parser.add_argument("--model", default="claude-sonnet-4-20250514", help="Anthropic model name.")
    parser.add_argument("--output", default="-", help="Output path for verdict JSON (- for stdout).")
    args = parser.parse_args()

    with open(args.artifact_json) as f:
        artifact = json.load(f)

    pipeline = ADDIEPipeline(model_name=args.model)
    verdict = pipeline.run_evaluation(
        request=args.request,
        artifact=artifact,
        context=args.context,
        reference=args.reference,
    )

    out = verdict.to_json()
    if args.output == "-":
        print(out)
    else:
        with open(args.output, "w") as f:
            f.write(out)
        print(f"Verdict written to {args.output}")


if __name__ == "__main__":
    # Import the registry so all archetypes auto-register
    import guide_registry  # noqa: F401
    _cli()
