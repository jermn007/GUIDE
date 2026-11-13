---
name: guide-pipeline
description: Run the full GUIDE multi-agent ADDIE pipeline - build a course end to end or audit an existing one, with an alignment gate and revision loop.
disable-model-invocation: true
---

Run the GUIDE agent pipeline described in this plugin's `PIPELINE.md`. You are the
orchestrator: the GUIDE agents only read files and return JSON, so you spawn each one and pass
outputs between them.

## Before you start

The pipeline needs subagents. Where you cannot spawn them (Claude chat, for example), say so in
one line, then run it in this conversation: load the `guide-instructional-design` skill, build
the plan yourself from the phases, skips, and gates in `PIPELINE.md`, and work each step
following the skill's `DESIGN.md` or `EVALUATE.md`.

The agents' instructions name their files relative to this plugin, which they cannot resolve
from the user's project. Put these absolute paths in every agent's prompt, and tell each
specialist to read its rubric before it designs or scores:

- Rubrics: `${CLAUDE_PLUGIN_ROOT}/skills/guide-instructional-design/references/`
- Pipeline design: `${CLAUDE_PLUGIN_ROOT}/PIPELINE.md`

An agent may be able to read the rubrics but not `PIPELINE.md`. So state these rules in the prompt of the gate, the
synthesizer, and the reviser instead of relying on that file:

- Fail-fast: block when `objective_strategy_coherence` is below 4.
- Cap: when `objective_assessment_coherence` is 1 or 2, the composite is capped at 3.0.
- Verdict, exactly one of four values: `ship` at 4.5 and up, `light_revision` from 3.5, `revise` from 2.5,
  `redesign` below 2.5.

The agents keep nothing between calls and the artifacts exist only in this conversation. Whenever
you send an agent back to revise, put its own previous output in the prompt in full, next to the
fix; an agent sent only the fix will invent the rest.

Also ask every specialist to start each severity flag with its tier (catastrophic, major, minor,
or cosmetic), so the synthesizer can rank them.

## Steps

1. **Route.** Spawn the `guide-router` agent with the request and any attached artifacts. It
   returns a JSON `dispatch_plan` and a `mode_detected` of build, review, or partial. If its
   `rationale` says the request is too underspecified, ask the user that question before going on.
2. **Run the plan in order.** Spawn each step's agent with its mode and inputs, passing the JSON
   outputs the step names. Steps in the same phase run in one batch: the Design specialists
   together, the Develop pair together, the Evaluate pair together (the router's
   `downstream_notes` say which).
3. **Stop when training is the wrong fix.** When `guide-needs-analysis` returns
   `is_training_appropriate: false`, stop, report its `alternative_interventions`, and ask the
   user whether to continue.
4. **Honor the fail-fast gate.** In a build or partial run, after the Design phase, run
   `guide-curriculum-alignment` in `fail_fast` mode. When its `decision` is `block`, show the
   user the `block_reason`, re-run the Design agent it names once with that fix, and check
   again. If it still blocks, ask the user. Once it passes, re-run any other Design specialist whose
   scorecard flagged the problem the fix removed, so no archetype goes into the composite stale or
   gets left out of it. A review run has no Design phase, so skip this gate.
5. **Close with the gate and the verdict.** Run `guide-curriculum-alignment` in
   `acceptance_gate` mode over every artifact, then `guide-synthesizer` over all scorecards. Its
   verdict is exactly one of ship, light_revision, revise, or redesign.
6. **Revise when asked for.** Keep a round counter that starts at 1. On light_revision or
   revise, spawn `guide-reviser` with the synthesizer's output, the router's `dispatch_plan`, and
   the counter, then run its `revision_plan` as written (it ends with the gate and the
   synthesizer). Give the synthesizer the previous composite each time. Run at most 3 revision
   rounds. Stop earlier when the composite rises by less than 0.5 from one round to the next
   (`non_progress_flag`) or the reviser returns `halted: true`, and hand the decision to the
   user. On redesign, stop and report.

In Claude Code the agents carry the plugin prefix, for example
`guide-instructional-design:guide-router`.

## Report

Lead with the synthesizer's verdict and composite, then the ranked severity findings and next
actions, then one line per archetype score. Offer the full JSON on request.

Request: $ARGUMENTS
