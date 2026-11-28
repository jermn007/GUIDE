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
  - archetype 11: the measurement plan in the composite, the impact report as a
    separate evidence verdict, the missing-plan finding, and the plan passed as
    the reference when the report is scored

Run from the GUIDE repo root (or any dir with guide_base.py and guide_pipeline.py):
    python smoke_test_pipeline.py

Exit code 0 == all assertions passed. Non-zero == failure (prints which case).

Author: Jeremy Terhune
Copyright 2026 Jeremy Terhune
License: Apache-2.0 (see LICENSE and NOTICE in the repository root)
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

# Register every archetype with placeholder prompts. The judge call is
# monkey-patched below, so the prompt bodies are never used — but
# register_archetype() requires them, so pass empty strings.
for n in ARCHETYPE_NAMES:
    guide_base.register_archetype(n, system_prompt="", human_prompt="")


# ---------------------------------------------------------------------------
# Mock the LLM call
# ---------------------------------------------------------------------------

# A dispatch table: each scenario sets this to control what each archetype returns.
_MOCK_RESPONSES: dict[str, GUIDEResult] = {}
# Every judge call the pipeline makes, in order, so scenarios can check what was sent.
_CALLS: list[dict] = []
# Archetype 11 is called twice with the same name: once for the measurement plan and
# once for the impact report. A response staged under this key answers the second.
IMPACT_REPORT_KEY = "summative_evaluation:impact_report"


def _mock_evaluate_standalone(archetype_name, user_input, assistant_output,
                              context="N/A", reference="N/A",
                              model_name="claude-sonnet-5-5", api_key=None) -> GUIDEResult:
    """Return the pre-loaded mock result for this archetype."""
    _CALLS.append({"archetype": archetype_name, "user_input": user_input,
                   "output": assistant_output, "reference": reference})
    if archetype_name == "summative_evaluation" and "impact_report" in user_input:
        if IMPACT_REPORT_KEY not in _MOCK_RESPONSES:
            raise AssertionError("Smoke test did not stage a response for the impact report.")
        return _MOCK_RESPONSES[IMPACT_REPORT_KEY]
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
    _CALLS.clear()
    for arch, overall in specialist_overalls.items():
        flags = (specialist_flags or {}).get(arch, [])
        _MOCK_RESPONSES[arch] = _make_specialist_result(arch, overall, severity_flags=flags)
    _MOCK_RESPONSES["curriculum_alignment"] = _make_gate_result(gate_scores, severity_flags=gate_flags or [])


def _stage_impact_report(overall: int, *, severity_flags=None):
    """Stage archetype 11's answer for the impact report (call after _stage_mocks)."""
    _MOCK_RESPONSES[IMPACT_REPORT_KEY] = _make_specialist_result(
        "summative_evaluation", overall, severity_flags=severity_flags or [])


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
    "measurement_plan":         "objective-to-evidence table; baseline, 30 and 90 days; thresholds set in advance",
}
ALL_SPECIALISTS_5 = {a: 5 for a in ARCHETYPE_NAMES if a != Archetype.CURRICULUM_ALIGNMENT.value}


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
    assert len(verdict.by_archetype) == 11, f"expected 11 archetypes, got {len(verdict.by_archetype)}"
    _ok(f"by_archetype covers all 11 archetypes")
    assert verdict.evidence is None and verdict.missing_measurement_plan is False
    _ok("no impact report, so no evidence verdict; plan present, so no missing-plan finding")


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
        "evidence", "missing_measurement_plan", "verdict_statements",
    }
    assert expected_keys.issubset(parsed.keys()), f"missing keys: {expected_keys - parsed.keys()}"
    _ok(f"verdict JSON has all expected keys ({len(expected_keys)})")
    assert parsed["threshold_band"] == "light_revision"
    _ok(f"threshold_band = {parsed['threshold_band']} (4.0 falls in 3.5-4.4 band)")


def scenario_h_measurement_plan_in_composite():
    """A measurement plan is scored by archetype 11 and averaged in like any other archetype."""
    print("\n[H] Archetype 11: measurement plan enters the composite when present")
    specs = dict(ALL_SPECIALISTS_5)
    specs[Archetype.SUMMATIVE_EVAL.value] = 1
    _stage_mocks(specs, gate_scores={})
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=ARTIFACT_FULL)
    expected = round((9 * 5 + 1 + 5) / 11, 2)
    assert verdict.composite_score == expected, f"expected {expected}, got {verdict.composite_score}"
    _ok(f"composite_score = {verdict.composite_score} (plan scored 1, averaged with ten 5s)")
    assert verdict.by_archetype["summative_evaluation"]["overall"] == 1
    _ok("by_archetype includes summative_evaluation")
    assert verdict.alignment_cap_triggered is False
    _ok("a weak measurement plan does not cap the composite (archetype 10's cap is the only one)")
    owners = {a.fix_owner_archetype for a in verdict.next_actions}
    assert "summative_evaluation" in owners, "expected revision actions owned by summative_evaluation"
    _ok("revision actions are routed to summative_evaluation")

    # Absent and not expected: skipped, like 08 when there are no scenarios.
    artifact = {k: v for k, v in ARTIFACT_FULL.items() if k != "measurement_plan"}
    _stage_mocks({a: 5 for a in ALL_SPECIALISTS_5 if a != "summative_evaluation"}, gate_scores={})
    verdict = pipeline.run_evaluation(request="Job aid", artifact=artifact, measurement_plan_expected=False)
    assert verdict.composite_score == 5.0 and "summative_evaluation" not in verdict.by_archetype
    _ok("plan absent and optional: archetype 11 skipped, composite 5.0")
    assert verdict.missing_measurement_plan is False
    assert not any("measurement plan" in i["finding"] for i in verdict.ranked_severity)
    _ok("no missing-plan finding when the plan is optional")


def scenario_i_missing_plan_is_a_finding():
    """An expected plan that is absent is a synthesizer finding; the composite does not move."""
    print("\n[I] Archetype 11: missing-but-expected measurement plan is a finding, not a score")
    artifact = {k: v for k, v in ARTIFACT_FULL.items() if k != "measurement_plan"}
    _stage_mocks({a: 5 for a in ALL_SPECIALISTS_5 if a != "summative_evaluation"}, gate_scores={})
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact, measurement_plan_expected=True)
    assert verdict.composite_score == 5.0, f"composite should be unchanged, got {verdict.composite_score}"
    _ok(f"composite_score = {verdict.composite_score} (unchanged)")
    assert verdict.threshold_band == "ship"
    _ok("threshold_band = ship (a finding does not change the band)")
    assert "summative_evaluation" not in verdict.by_archetype
    _ok("no score invented for archetype 11")
    assert verdict.missing_measurement_plan is True
    found = [i for i in verdict.ranked_severity if "No measurement plan" in i["finding"]]
    assert len(found) == 1 and found[0]["raised_by"] == "synthesizer"
    _ok("ranked_severity lists 'No measurement plan', raised by the synthesizer")
    assert "no measurement plan" in verdict.verdict_statements["design"]
    _ok("design verdict statement names the missing plan")
    # Default: a full review set is taken to be a course, so the plan is expected.
    _stage_mocks({a: 5 for a in ALL_SPECIALISTS_5 if a != "summative_evaluation"}, gate_scores={})
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact)
    assert verdict.missing_measurement_plan is True
    _ok("default for a full review set: plan expected")


def scenario_j_impact_report_is_separate():
    """The impact report gets its own evidence verdict and never moves the composite."""
    print("\n[J] Archetype 11: impact report is an evidence verdict, never in the composite")
    artifact = dict(ARTIFACT_FULL, impact_report="96% completion, 4.7 satisfaction, proven impact")
    _stage_mocks(ALL_SPECIALISTS_5, gate_scores={})
    _stage_impact_report(1, severity_flags=["catastrophic: completion presented as effectiveness"])
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact)
    assert verdict.composite_score == 5.0, f"report must not move the composite, got {verdict.composite_score}"
    _ok(f"composite_score = {verdict.composite_score} with an impact report scored 1")
    assert verdict.threshold_band == "ship"
    _ok("design verdict stays ship")
    ev = verdict.evidence
    assert ev is not None and ev["evidence_score"] == 1.0 and ev["evidence_verdict"] == "poor"
    _ok(f"evidence verdict = {ev['evidence_verdict']} ({ev['evidence_score']})")
    assert ev["in_composite"] is False and ev["mode"] == "impact_report"
    _ok("evidence block is marked in_composite = False")
    assert verdict.by_archetype["summative_evaluation"]["overall"] == 5
    _ok("by_archetype holds the measurement plan's score, not the report's")
    assert not any("completion presented" in i["finding"] for i in verdict.ranked_severity)
    _ok("the report's flags stay in the evidence block, out of the design findings")
    assert len(verdict.by_archetype) == 11
    _ok("by_archetype still has 11 entries (the report adds none)")

    # Bands for the evidence verdict
    for overall, band in ((5, "excellent"), (4, "good"), (3, "fair"), (2, "poor")):
        _stage_mocks(ALL_SPECIALISTS_5, gate_scores={})
        _stage_impact_report(overall)
        got = pipeline.run_evaluation(request="Course", artifact=artifact).evidence["evidence_verdict"]
        assert got == band, f"evidence score {overall}: expected {band}, got {got}"
    _ok("evidence bands: 5 excellent, 4 good, 3 fair, 2 poor")


def scenario_k_report_scored_against_plan():
    """The measurement plan is the reference when the report is scored; the gate never sees the report."""
    print("\n[K] Archetype 11: the plan is passed as the reference for the impact report")
    report = "IMPACT REPORT TEXT"
    artifact = dict(ARTIFACT_FULL, impact_report=report)
    _stage_mocks(ALL_SPECIALISTS_5, gate_scores={})
    _stage_impact_report(4)
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact, reference="GOLD STANDARD")
    report_calls = [c for c in _CALLS if c["archetype"] == "summative_evaluation" and c["output"] == report]
    assert len(report_calls) == 1, f"expected one impact-report call, got {len(report_calls)}"
    assert report_calls[0]["reference"] == ARTIFACT_FULL["measurement_plan"]
    _ok("impact report scored once, with the measurement plan as its reference")
    assert verdict.evidence["scored_against_plan"] is True
    _ok("evidence.scored_against_plan = True")
    plan_calls = [c for c in _CALLS if c["archetype"] == "summative_evaluation" and c["output"] != report]
    assert len(plan_calls) == 1 and plan_calls[0]["reference"] == "GOLD STANDARD"
    _ok("measurement plan scored once, as a design artifact, with the caller's reference")
    gate_calls = [c for c in _CALLS if c["archetype"] == "curriculum_alignment"]
    assert gate_calls and all(report not in c["output"] for c in gate_calls)
    _ok("alignment gate input does not include the impact report")

    # No plan: the report is still scored, with no reference.
    artifact = {k: v for k, v in artifact.items() if k != "measurement_plan"}
    _stage_mocks({a: 5 for a in ALL_SPECIALISTS_5 if a != "summative_evaluation"}, gate_scores={})
    _stage_impact_report(3)
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact, measurement_plan_expected=False)
    report_calls = [c for c in _CALLS if c["output"] == report]
    assert len(report_calls) == 1 and report_calls[0]["reference"] == "N/A"
    assert verdict.evidence["scored_against_plan"] is False
    _ok("no plan: report scored with reference N/A, scored_against_plan = False")
    assert "summative_evaluation" not in verdict.by_archetype
    _ok("no plan: archetype 11 is absent from by_archetype even though the report was scored")


def scenario_l_verdicts_do_not_stand_in():
    """A capped design with excellent evidence stays capped, and the two are worded apart."""
    print("\n[L] Archetype 11: one verdict cannot stand in for the other")
    artifact = dict(ARTIFACT_FULL, impact_report="rigorous impact study")
    gate_scores = {"objective_assessment_coherence": 2, "overall": 4}
    _stage_mocks(ALL_SPECIALISTS_5, gate_scores=gate_scores)
    _stage_impact_report(5)
    pipeline = guide_pipeline.ADDIEPipeline()
    verdict = pipeline.run_evaluation(request="Course", artifact=artifact)
    assert verdict.alignment_cap_triggered is True and verdict.composite_score == 3.0
    _ok("composite stays capped at 3.0 with an evidence verdict of excellent")
    assert verdict.threshold_band == "revise" and verdict.evidence["evidence_verdict"] == "excellent"
    _ok("design verdict = revise; evidence verdict = excellent")
    design, evidence = verdict.verdict_statements["design"], verdict.verdict_statements["evidence"]
    assert design.startswith("Design verdict: revise") and "does not lift the cap" in design
    assert "excellent" not in design
    _ok("design statement names the cap and does not quote the evidence verdict")
    assert evidence.startswith("Evidence verdict: excellent") and "not averaged into the design composite" in evidence
    assert "revise" not in evidence
    _ok("evidence statement stands alone and says it is not in the composite")

    # The reverse: a clean design with no report says so, and claims no impact.
    _stage_mocks(ALL_SPECIALISTS_5, gate_scores={})
    verdict = pipeline.run_evaluation(request="Course", artifact=ARTIFACT_FULL)
    assert "not evidence that the course worked" in verdict.verdict_statements["design"]
    assert verdict.verdict_statements["evidence"].startswith("Evidence verdict: none")
    _ok("ship with no impact report: evidence verdict is 'none', and the design verdict claims no impact")


def scenario_m_evidence_only():
    """An impact report on its own gets an evidence verdict and no design composite."""
    print("\n[M] Archetype 11: impact report alone (evidence_only)")
    _MOCK_RESPONSES.clear()
    _CALLS.clear()
    _stage_impact_report(2)
    pipeline = guide_pipeline.ADDIEPipeline()
    artifact = {"impact_report": "renewal case: 4.8 of 5, 97% would recommend"}
    assert pipeline.classify_request("Review this renewal case", artifact) == "evidence_only"
    verdict = pipeline.run_evaluation(request="Review this renewal case", artifact=artifact)
    assert verdict.threshold_band == guide_pipeline.NOT_SCORED and verdict.by_archetype == {}
    _ok(f"threshold_band = {verdict.threshold_band}; no design composite")
    assert verdict.evidence["evidence_verdict"] == "poor" and verdict.evidence["scored_against_plan"] is False
    _ok("evidence verdict = poor, scored without a plan")
    assert [c["archetype"] for c in _CALLS] == ["summative_evaluation"]
    _ok("only archetype 11 was called (no alignment gate on an impact report)")
    assert verdict.missing_measurement_plan is False
    _ok("no missing-plan finding without a design to attach it to")
    json.loads(verdict.to_json())
    _ok("verdict serializes to JSON")


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
    scenario_h_measurement_plan_in_composite()
    scenario_i_missing_plan_is_a_finding()
    scenario_j_impact_report_is_separate()
    scenario_k_report_scored_against_plan()
    scenario_l_verdicts_do_not_stand_in()
    scenario_m_evidence_only()
    print()
    print("All scenarios passed.")
