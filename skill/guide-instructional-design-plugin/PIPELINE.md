# GUIDE Agent Pipeline — Workflow Design (v0.1 draft)

A multi-agent ADDIE workflow that uses each of GUIDE's 10 archetypes as both **design guardrail** (when building) and **acceptance test** (when judging). Archetype 10 (Curriculum Alignment, v3.1.0) operates as a cross-cutting alignment check: it does **not** replace any individual archetype's judgment; it verifies that the components agree with each other.

Tracks GUIDE **v3.4.0** (10 archetypes, 60 dimensions). Adopts Hirumi's Three Alignments (01), ARCS motivational alignment (03/07), and the Merrill (2002) Effective/Efficient/Engaging vocabulary that archetype 10 codifies.

## Goals

- Turn a training request into a coherent, defensible instructional artifact end-to-end.
- Catch alignment drift between objectives, instruction, and assessment **before** publication.
- Produce structured, theory-grounded scorecards for every stage — defensible to accreditors and stakeholders.
- Enable batch audits of existing artifacts via the same agent set (skip build phases; jump straight to evaluation).

## Architecture at a glance

```
                       ┌──────────────────────┐
                       │   guide-router       │  (Phase 0: classify + dispatch)
                       └─────────┬────────────┘
                                 │
   Build path ◀─────────────────┴────────────────▶ Audit path
        │                                                  │
        ▼                                                  │
┌──────────────────┐ Phase A — Analyze (07)                 │
│ guide-needs-     │ Gatekeeper: training? + Mager objs +   │
│ analysis         │ McGoldrick/Tobey levels + ARCS         │
└────────┬─────────┘                                        │
         │                                                  │
         ▼                                                  │
┌──────────────────────────────────────────┐                │
│ Phase D — Design  (parallel)             │                │
│  guide-sequencing (03)                   │                │
│  guide-story-design (08, when scenarios) │                │
│  guide-cognitive-neuro (09)              │                │
└────────┬─────────────────────────────────┘                │
         │                                                  │
         ▼  ◀── Alignment fail-fast (10 against 07 + 03)    │
┌──────────────────────────────────────────┐                │
│ Phase D — Develop (parallel)             │                │
│  guide-multimedia (04)                   │                │
│  guide-accessibility (05)                │                │
└────────┬─────────────────────────────────┘                │
         │                                                  │
         ▼                                                  │
┌──────────────────────┐ Phase I — Implement (01)           │
│ guide-adult-learning │ Hirumi Three Alignments            │
└────────┬─────────────┘                                    │
         │                                                  │
         ▼                                                  │
┌──────────────────────────────────────────┐                │
│ Phase E — Evaluate (parallel)            │                │
│  guide-assessment (02)                   │                │
│  guide-formative-eval (06)               │                │
└────────┬─────────────────────────────────┘                │
         │                                                  │
         ▼                                                  ▼
┌──────────────────────────────────────────────────────────────┐
│ Final Acceptance Gate — guide-curriculum-alignment (10)     │
│ O↔S, S↔A, O↔A, Coverage, Vertical, Discipline               │
│ Cap rule: if O↔A ≤ 2 → overall capped at 3.0                │
└────────┬─────────────────────────────────────────────────────┘
         │
         ▼
┌──────────────────┐         ┌──────────────────┐
│ guide-synthesizer│ ◀─────▶ │ guide-reviser    │
│ rolls up         │  loop   │ applies feedback │
└────────┬─────────┘         └──────────────────┘
         │ ship if composite ≥ threshold
         ▼
     Final verdict
```

## Phase 0 — Intake & Router (`guide-router`)

Receives the user's request and classifies it:

- **build** — a training request ("we need a course on X"). Start at Phase A.
- **review** — an existing artifact to grade. Skip to the evaluator fan-out (audit path).
- **partial** — a draft mid-cycle (e.g., objectives + lesson plan, no assessment yet). Resume at the appropriate phase and run the alignment gate on what's present.

Output is a routing decision plus a *dispatch plan*: ordered list of (agent, mode, inputs).

## Phase A — Analyze (Archetype 07)

`guide-needs-analysis` runs the gatekeeper question first: **is training even the answer?** If the cause is environmental (tools, incentives, process), it returns HPT alternatives and the pipeline halts with a recommendation.

If training is appropriate, it produces:

- **McGoldrick & Tobey levels** — business → performance → learning → learner.
- **Mager objectives** (Behavior + Condition + Criterion).
- **ARCS motivational alignment** notes (Attention, Relevance, Confidence, Satisfaction).
- **Recommended downstream archetypes** (e.g., scenarios needed → invoke 08; web/LMS delivery → invoke 05).

## Phase D — Design (Archetypes 03, 08, 09)

Three specialists in parallel:

- `guide-sequencing` (03) — Gagné's nine events, learning-domain alignment, scaffolding/gradual release, ARCS integration.
- `guide-story-design` (08) — invoked when scenarios/case studies/branching apply. Skipped otherwise.
- `guide-cognitive-neuro` (09) — 5E phase order (Explore before Explain), memory systems, attention segments, synaptic strengthening factors.

Each returns a draft design document + a self-evaluation against its own archetype.

**Alignment fail-fast (10).** `guide-curriculum-alignment` runs a lightweight check on (objectives ← Phase A) vs (proposed strategies ← Phase D Design). If `objective_strategy_coherence < 4`, the router sends design back to revision before any Develop work is spent. This is the most expensive misalignment to catch late; catch it here.

## Phase D — Develop (Archetypes 04, 05)

- `guide-multimedia` (04) — Mayer's principles, intrinsic/extraneous load, segmenting, modality, generative processing, learner control.
- `guide-accessibility` (05) — WCAG 2.1 POUR + CAST UDL + remediation feasibility.

Parallel. Each returns the developed artifact (storyboards, scripts, slides, module structure) + self-eval.

## Phase I — Implement (Archetype 01)

`guide-adult-learning` produces the conversational/RAG/help layer that learners actually interact with — chatbot answers, support content, in-product help. Now grounded in **Hirumi's Three Alignments** (analyze → design → develop) plus Knowles/Mezirow. Returns response patterns + a self-eval scorecard.

## Phase E — Evaluate (Archetypes 02, 06)

- `guide-assessment` (02) — generates assessment items (quizzes, rubrics, blueprints) at the Bloom level each objective requires.
- `guide-formative-eval` (06) — drafts the evaluation plan (Bordonaro phases, evaluator selection, instruments, revision decision framework, usability methods).

Parallel.

## Final Acceptance Gate — Archetype 10

`guide-curriculum-alignment` runs the full 6-dimension check on the **complete** artifact set:

1. Objective ↔ Strategy Coherence
2. Strategy ↔ Assessment Coherence
3. Objective ↔ Assessment Coherence
4. Coverage Completeness
5. Vertical Alignment
6. Discipline Alignment

**Weighting rule (from handoff_10):** if `objective_assessment_coherence ≤ 2`, the overall is capped at **3.0** regardless of how well other dimensions score. The pipeline enforces this in the synthesizer.

**Severity flags** the gate must surface to the synthesizer:

- Bloom-level mismatch ≥ 2 between objective and assessment (major).
- Orphan objective (stated but not taught/tested).
- Orphan instruction (taught but unaligned).
- Assessment-without-instruction (catastrophic).
- Multi-module artifact with no vertical alignment.
- Claimed competency framework with no traceable mapping (accreditation risk).

## Synthesis + Revision Loop

`guide-synthesizer` ingests every archetype's JSON scorecard and produces a **combined verdict**:

- Per-archetype scores + overall composite.
- Honors the 10's cap rule.
- Threshold map: **4.5+** ship; **3.5–4.4** light revision; **2.5–3.4** revise; **< 2.5** redesign.
- Severity-flagged issues ranked.

`guide-reviser` reads the synthesized verdict and routes targeted feedback back to the relevant phase agents (e.g., "objective_assessment_coherence = 2 because verbs drift between Phase A objectives and Phase E items → return to Phase E with these specific edits"). Loop until composite clears the threshold or a max-iteration cap is hit (default 3).

## Handoff contracts

Every agent's output adheres to a stable JSON contract so the orchestrator can compose results without parsing prose.

```json
{
  "agent": "guide-multimedia",
  "archetype": 4,
  "mode": "design" | "evaluate",
  "artifact_ref": "string identifier for the artifact under design/review",
  "produced": { ... agent-specific design artifact, when mode=design ... },
  "scorecard": {
    "scores": { "<dim>": 1-5, ..., "overall": 1-5 },
    "rationale": { "<dim>": "..." },
    "severity_flags": [ "..." ],
    "improvement_suggestions": [ "..." ]
  },
  "downstream_hints": [ "for guide-accessibility: caption all narration", ... ]
}
```

The synthesizer's final output:

```json
{
  "verdict": "ship" | "light_revision" | "revise" | "redesign",
  "composite_overall": 1-5,
  "by_archetype": { "01": {...}, "02": {...}, ..., "10": {...} },
  "alignment_cap_triggered": true | false,
  "ranked_severity": [ {"archetype": 10, "flag": "...", "severity": "major"}, ... ],
  "next_actions": [ "..." ]
}
```

## Orchestration patterns

- **Sequential within phase boundaries** (A → Design → Develop → Implement → Evaluate → Gate → Synth). The phase-internal specialists run **in parallel** where listed.
- **Fail-fast at the Design→Develop seam** via the lightweight 10 check; this is the cheapest place to catch verb/Bloom drift before development resources are committed.
- **Audit path** skips A/D/D/I and runs only E + final 10 + synth on an existing artifact. Useful for batch grading.
- **Partial path** lets the router pick up mid-cycle if some artifacts are already produced.
- **Iteration cap** prevents infinite loops; if composite hasn't moved by ≥ 0.5 across two iterations, escalate to the user.

## Composite scoring & thresholds

| Composite (incl. archetype 10) | Status | Action |
|---|---|---|
| 4.5–5.0 | Excellent | Ship |
| 3.5–4.4 | Good with gaps | Light revision; address flagged dimensions before next cohort |
| 2.5–3.4 | Real misalignment | Revise before delivery |
| < 2.5 | Misaligned | Redesign — objectives/instruction/assessment are effectively different courses |

Cap rule from archetype 10 overrides upward composite when `objective_assessment_coherence ≤ 2`.

## When to skip / adapt

- **Single lesson, not a course.** Archetype 10's Vertical Alignment scores within-lesson sequencing; Discipline Alignment becomes internal-purpose coherence. Note the adaptation in the synthesizer rationale.
- **No scenarios.** Skip 08; route directly through 03 + 09 in the design phase.
- **Non-web delivery.** Skip 05 if there's no digital/web component (rare for modern instruction; usually still applies).
- **No assessment authoring needed** (e.g., evaluating an existing artifact). Skip 02 in design mode; still run 02 in evaluate mode against the existing assessment.
- **Internal one-off training.** Discipline Alignment becomes N/A → score on stated-purpose coherence; flag in rationale.

## How to invoke (Cowork / Claude Code)

From a Cowork chat with this plugin installed:

> "Run the GUIDE pipeline on this course outline." → main Claude reads `agents/guide-router.md`, spawns the router subagent, which dispatches the rest via the Task tool.

For evaluation-only on an existing artifact:

> "Grade this artifact end-to-end against GUIDE." → router classifies as `review`, fans out to all relevant judges in parallel, runs 10 as the gate, synthesizer returns the verdict.

The plugin's skill (`guide-instructional-design`) supplies the rubric content all agents reference; the agents supply the *roles* and the orchestration glue.

## Open design choices

A few decisions worth making before v0.2:

- **Default iteration cap** (currently 3) — make configurable.
- **Whether to commit to a Python orchestrator** (extending `guide_registry.py`) in addition to the Cowork plugin path. The Python route is better for CI/batch; the plugin path is better for interactive design work.
- **Where to store agent output between iterations** — Cowork session scratchpad vs. a structured workspace dir (recommended for the Python orchestrator).
- **How aggressive the fail-fast should be at the Design→Develop seam.** Current draft: block on `objective_strategy_coherence < 4`. Could be tunable.

---

*Tracks GUIDE v3.4.0. Copyright 2026 Jeremy Terhune. Apache-2.0.*
