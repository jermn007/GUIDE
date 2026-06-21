"""
GUIDE Pipeline Smoke Test
=========================
Exercises the ADDIEPipeline class end-to-end with mocked archetype evaluations
(no Anthropic API call required). Catches regressions in:

  - registry sanity check
  - artifact → archetype routing
  - composite math
  - archetype-10 cap rule (the most opinionated piece)
  - fail-fast Design→Develop check
  - verdict banding
  - revision-action generation
  - build / review / partial mode classification

Run from the GUIDE repo root (or any dir with guide_base.py and guide_pipeline.py):
    python smoke_test_pipeline.py

Exit code 0 == all assertions passed. Non-zero == failure (prints which case).
"""
from __future__ import annotations

import json
import sys
from dataclasses import replace

# The scenario output uses arrows/inequality glyphs (O↔A, ≤, →). Force UTF-8 on
# stdout so the test runs on a default Windows console (cp1252) too.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# Path setup (so the smoke test runs from the same dir as guide_base.py + guide_pipeline.py)
import os
sys.path.insert(0, os.path.dirname(__file__))

import guide_base
from guide_base import GUIDEResult
import guide_pipeline
from guide_pipeline import Archetype

# Derive the archetype names from the pipeline's own enum so the smoke test can
# never silently drift from the names the pipeline actually verifies against.
ARCHETYPE_NAMES = [a.value for a in Archetype]

# Register all 10 archetypes with placeholder prompts. The judge call is
# monkey-patched below, so the prompt bodies are never used — but
# register_archetype() requires them, so pass empty strings.
for n in ARCHETYPE_NAMES:
    guide_base.register_archetype(n, system_prompt="", human_prompt="")


# ---------------------------------------------------------------------------
# Mock the LLM call
# ---------------------------------------------------------------------------

# A dispatch table: each scenario sets this to control what each archetype returns.
_MOCK_RESPONSES: dict[str, GUIDEResult] = {}


def _mock_evaluate_standalone(archetype_name, user_input, assistant_output,
                              context="N/A", reference="N/A",
                              model_name="claude-sonnet-4-20250514", api_key=None) -> GUIDEResult:
    """Return the pre-loaded mock result for this archetype."""
    if archetype_name not in _MOCK_RESPONSES:
        raise AssertionError(
            f"Smoke test did not stage a response for archetype '{archetype_name}'. "
            f"Available: {sorted(_MOCK_RESPONSES.keys())}"
        )
    return _MOCK_RESPONSES[archetype_name]


# Monkey-patch into guide_base and (importantly) into guide_pipeline's namespace,
# since guide_pipeline imported it by name at module load time.
guide_base.evaluate_standalone = _mock_evaluate_standalone
guide_pipeline.evaluate_standalone = _mock_evaluate_standalone


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def _make_specialist_result(archetype_name: str, overall: int, *,
                            severity_flags=None, suggestion="generic fix",
                            dim_overrides: dict | None = None) -> GUIDEResult:
    """A generic specialist scorecard with 6 dims + overall."""
    base = {f"dim_{i}": overall for i in range(1, 7)}
    if dim_overrides:
        base.update(dim_overrides)
    base["overall"] = overall
    return GUIDEResult(
        archetype=archetype_name,
        scores=base,
        rationale={k: f"{k} rationale" for k in base},
        severity_flags=severity_flags or [],
        improvement_suggestions=[suggestion],
    )


def _make_gate_result(scores: dict, *, severity_flags=None) -> GUIDEResult:
    """Archetype-10 gate result. Caller specifies the 6 alignment dims + overall."""
    base = {
        "objective_strategy_coherence": 5,
        "strategy_assessment_coherence": 5,
        "objective_assessment_coherence": 5,
        "coverage_completeness": 5,
        "vertical_alignment": 5,
        "discipline_alignment": 5,
        "overall": 5,
    }
    base.update(scores)
    return GUIDEResult(
        archetype="curriculum_alignment",
        scores=base,
        rationale={k: f"{k} rationale" for k in base},
        severity_flags=severity_flags or [],
        improvement_suggestions=["lift alignment per archetype 10 anchors"],
    )


def _stage_mocks(specialist_overalls: dict[str, int], gate_scores: dict, *,
                 specialist_flags: dict | None = None, gate_flags=None):
    """Load _MOCK_RESPONSES so any subsequent pipeline call returns canned data."""
    _MOCK_RESPONSES.clear()
    for arch, overall in specialist_overalls.items():
        flags = (specialist_flags or {}).get(arch, [])
        _MOCK_RESPONSES[arch] = _make_specialist_result(arch, overall, severity_flags=flags)
    _MOCK_RESPONSES["curriculum_alignment"] = _make_gate_result(gate_scores, severity_flags=gate_flags or [])


def _ok(msg):  print(f"  PASS  {msg}")
def _fail(msg): print(f"  FAIL  {msg}"); sys.exit(1)


# ---------------------------------------------------------------------------
# Scenarios
# ---------------------------------------------------------------------------

ARTIFACT_FULL = {
    "needs_analysis":           "L1-L4 with Mager objectives and ARCS profile",
    "lesson_plan":              "3-week module with Gagné events",
    "scenarios":                "branching scenario for de-escalation",
    "neuro_design_notes":       "15-min segments; spaced retrieval; Explore-before-Explain",
    "multimedia_storyboard":    "narrated animations with signaling",
    "accessibility_spec":       "captions, AD, keyboard nav, WCAG AA",
    "conversational_responses": "RAG help responses",
    "assessment":               "blueprint + items + rubric",
    "formative_eval_plan":      "expert + 1:1 + small group",
}


def scenario_a_clean_ship():
    """All archetypes score 5, gate scores 5 → composite 5.0 → ship."""
    print("\n[A] Clean artifact set, all archetypes score 5")
    specs = {a: 5 for a in ARCHETYPE_NAMES if a != Archetype.CURRICULUM_ALIGNMENT.value}
    _stage_mocks(specs, gate_scores={})  # gate stays all-5
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course on X", artifact=ARTIFACT_FULL)
    assert verdict.composite_score == 5.0, f"expected 5.0, got {verdict.composite_score}"
    _ok(f"composite_score = {verdict.composite_score}")
    assert verdict.alignment_cap_triggered is False
    _ok("alignment_cap_triggered = False")
    assert verdict.threshold_band == "ship", f"expected ship, got {verdict.threshold_band}"
    _ok(f"threshold_band = {verdict.threshold_band}")
    assert verdict.next_actions == [], "expected no revision actions"
    _ok("next_actions empty (nothing < 4)")
    assert len(verdict.by_archetype) == 10, f"expected 10 archetypes, got {len(verdict.by_archetype)}"
    _ok(f"by_archetype covers all 10 archetypes")


def scenario_b_cap_rule_triggered():
    """All specialists score 5 but archetype-10 O↔A coherence = 1 → cap at 3.0 → revise."""
    print("\n[B] Cap rule scenario: O↔A coherence = 1 should cap composite at 3.0")
    specs = {a: 5 for a in ARCHETYPE_NAMES if a != "curriculum_alignment"}
    gate_scores = {
        "objective_assessment_coherence": 1,
        "objective_strategy_coherence": 4,
        "strategy_assessment_coherence": 4,
        "coverage_completeness": 4,
        "vertical_alignment": 4,
        "discipline_alignment": 4,
        "overall": 4,  # gate's own overall
    }
    _stage_mocks(specs, gate_scores=gate_scores, gate_flags=["Bloom-level mismatch between objective and assessment"])
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course on Y", artifact=ARTIFACT_FULL)
    assert verdict.alignment_cap_triggered is True
    _ok("alignment_cap_triggered = True")
    assert verdict.composite_score == 3.0, f"expected cap at 3.0, got {verdict.composite_score}"
    _ok(f"composite_score capped at {verdict.composite_score}")
    assert verdict.composite_score_uncapped > 3.0, "uncapped should be > 3.0"
    _ok(f"composite_score_uncapped (pre-cap) = {verdict.composite_score_uncapped}")
    assert verdict.threshold_band == "revise", f"expected revise, got {verdict.threshold_band}"
    _ok(f"threshold_band = {verdict.threshold_band}")
    # The gate's dim < 4 should produce a revision action
    cap_actions = [a for a in verdict.next_actions if a.dimension == "objective_assessment_coherence"]
    assert cap_actions, "expected a revision action for objective_assessment_coherence"
    _ok(f"revision action present for objective_assessment_coherence (target=4, current={cap_actions[0].current_score})")
    # Severity should include the gate's flag
    gate_flag_in_ranked = any(
        item["finding"] == "Bloom-level mismatch between objective and assessment"
        for item in verdict.ranked_severity
    )
    assert gate_flag_in_ranked, "expected gate's Bloom-mismatch flag in ranked_severity"
    _ok("ranked_severity includes gate's Bloom-mismatch flag")


def scenario_c_build_mode():
    """Empty artifact → build mode → orchestrator returns a stub asking for Cowork agents."""
    print("\n[C] Build mode: empty artifact")
    _MOCK_RESPONSES.clear()  # nothing should be called
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="We need training on incident response", artifact={})
    assert verdict.composite_score == 0.0
    _ok("composite_score = 0.0 (nothing evaluated yet)")
    assert verdict.threshold_band == "redesign"
    _ok("threshold_band = redesign (placeholder for build mode)")
    assert "Cowork plugin" in verdict.band_explanation, "expected build-mode hand-off message"
    _ok("band_explanation correctly defers to Cowork plugin agents")
    assert verdict.by_archetype == {}
    _ok("by_archetype empty (no specialists ran)")


def scenario_d_partial_with_low_specialist():
    """Partial artifact; one specialist scores 2 → revision action targeted at that owner."""
    print("\n[D] Partial artifact: low specialist score generates targeted revision")
    artifact = {
        "needs_analysis": "NA",
        "lesson_plan":    "LP",
        "assessment":     "ASMT",
    }
    specs = {
        Archetype.NEEDS_ANALYSIS.value: 5,
        Archetype.SEQUENCING.value: 2,   # low → produces revision action
        Archetype.ASSESSMENT_DESIGN.value: 4,
    }
    _stage_mocks(specs, gate_scores={})  # gate scores all 5
    # The gate also gets called even with partial artifact; keep its overall at 5
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course on Z", artifact=artifact)
    seq_actions = [a for a in verdict.next_actions if a.fix_owner_archetype == "instructional_sequencing"]
    assert seq_actions, "expected revision action owned by instructional_sequencing"
    _ok(f"revision action owned by instructional_sequencing (current_score={seq_actions[0].current_score})")
    # Verify ordering: lower phase-order archetypes come first
    phase_indices = [
        guide_pipeline.PHASE_ORDER[guide_pipeline.Archetype(a.fix_owner_archetype)]
        for a in verdict.next_actions
    ]
    assert phase_indices == sorted(phase_indices), "revision actions should be ordered by ADDIE phase"
    _ok(f"revision actions ordered by ADDIE phase: {phase_indices}")


def scenario_e_fail_fast():
    """Fail-fast Design→Develop check: O↔S coherence = 2 should block."""
    print("\n[E] Fail-fast alignment check")
    _MOCK_RESPONSES.clear()
    _MOCK_RESPONSES["curriculum_alignment"] = GUIDEResult(
        archetype="curriculum_alignment",
        scores={"objective_strategy_coherence": 2, "overall": 2},
        rationale={"objective_strategy_coherence": "Bloom level taught (describe) is below objective level (analyze)."},
        severity_flags=["Verb-to-practice mismatch on objectives 2 and 3"],
        improvement_suggestions=["Rewrite practice activities to invoke analysis"],
    )
    pipeline = guide_pipeline.ADDIEPipeline()
    ff = pipeline.fail_fast_alignment(
        objectives="learners will analyze incident reports",
        proposed_strategies="learners will describe incident reports",
    )
    assert ff.decision == "block", f"expected block, got {ff.decision}"
    _ok(f"decision = {ff.decision} (O↔S coherence = {ff.objective_strategy_coherence})")
    # Should route back to needs_analysis because rationale mentions Bloom/verb
    assert ff.route_back_to is not None
    _ok(f"route_back_to = {ff.route_back_to.value}")
    assert ff.route_back_to == guide_pipeline.Archetype.NEEDS_ANALYSIS, \
        f"expected NEEDS_ANALYSIS, got {ff.route_back_to}"
    _ok("Bloom/verb keywords correctly routed to needs_analysis")


def scenario_f_non_progress():
    """When prior_composite_score is set and composite hasn't improved by ≥ 0.5 → non_progress_flag."""
    print("\n[F] Non-progress detection across iterations")
    specs = {a: 3 for a in ARCHETYPE_NAMES if a != "curriculum_alignment"}
    _stage_mocks(specs, gate_scores={"overall": 3})
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(
        request="Course",
        artifact=ARTIFACT_FULL,
        iteration_number=2,
        prior_composite_score=2.9,
    )
    assert verdict.non_progress_flag is True, "expected non_progress_flag=True (moved < 0.5)"
    _ok(f"non_progress_flag = True (composite {verdict.composite_score} vs prior 2.9, delta < 0.5)")


def scenario_g_verdict_to_json():
    """Round-trip the verdict through JSON to confirm it's serializable."""
    print("\n[G] JSON round-trip of verdict")
    specs = {a: 4 for a in ARCHETYPE_NAMES if a != "curriculum_alignment"}
    _stage_mocks(specs, gate_scores={"overall": 4})
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=ARTIFACT_FULL)
    payload = verdict.to_json()
    parsed = json.loads(payload)
    expected_keys = {
        "composite_score", "composite_score_uncapped", "alignment_cap_triggered",
        "cap_reason", "threshold_band", "band_explanation", "by_archetype",
        "ranked_severity", "next_actions", "iteration_number", "non_progress_flag",
    }
    assert expected_keys.issubset(parsed.keys()), f"missing keys: {expected_keys - parsed.keys()}"
    _ok(f"verdict JSON has all expected keys ({len(expected_keys)})")
    assert parsed["threshold_band"] == "light_revision"
    _ok(f"threshold_band = {parsed['threshold_band']} (4.0 falls in 3.5-4.4 band)")


# ---------------------------------------------------------------------------
# Run all scenarios
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 65)
    print("  GUIDE Pipeline Smoke Test")
    print("=" * 65)
    scenario_a_clean_ship()
    scenario_b_cap_rule_triggered()
    scenario_c_build_mode()
    scenario_d_partial_with_low_specialist()
    scenario_e_fail_fast()
    scenario_f_non_progress()
    scenario_g_verdict_to_json()
    print()
    print("All scenarios passed.")
