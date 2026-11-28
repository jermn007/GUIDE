"""
ARCHETYPE 11: SUMMATIVE EVALUATION & LEARNING TRANSFER

Evaluates the plan, and the report, that answer the question asked after release: did people
learn it, do they use it on the job, and did that change anything that matters?
Dimensions: Outcome Chain Coverage, Objective-Evidence Traceability, Measurement Quality,
Attribution & Comparison, Workplace Transfer Conditions, Decision Rules & Feedback Loop.

Two modes, one rubric (see guide_pipeline.py for how each is used):
- measurement_plan: scored before launch, in the Evaluate phase beside archetype 06. Enters the
  design composite when present.
- impact_report: scored after launch, with the measurement plan as the reference when one
  exists. Reported as a separate evidence verdict; never averaged into the design composite.

References (full list and evidence notes in archetypes/handoff_11_summative_evaluation.md and
docs/archetype_11_evidence_and_decisions.md):
- Kirkpatrick, D.L., & Kirkpatrick, J.D. (2006). Evaluating Training Programs: The Four Levels.
- Thalheimer, W. (2018). The Learning-Transfer Evaluation Model.
- Baldwin, T.T., & Ford, J.K. (1988). Transfer of training: A review and directions for future research.
- Shadish, W.R., Cook, T.D., & Campbell, D.T. (2002). Experimental and Quasi-Experimental Designs
  for Generalized Causal Inference.
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction.

Author: Jeremy Terhune
Copyright 2026 Jeremy Terhune
License: Apache-2.0 (see LICENSE and NOTICE in the repository root)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype

# The two ways this archetype is run. The rubric and the output keys are the same for both;
# the pipeline decides what each score counts toward.
MODE_MEASUREMENT_PLAN = "measurement_plan"
MODE_IMPACT_REPORT = "impact_report"
MODES = (MODE_MEASUREMENT_PLAN, MODE_IMPACT_REPORT)

JUDGE_SYSTEM_PROMPT = """You are an expert in training evaluation, learning transfer, and learning analytics.
Your role is to assess summative evaluation plans, measurement plans, dashboard specifications,
and impact reports for quality and appropriateness.

You will score across 6 dimensions, each on a 1-5 scale:

1. **Outcome Chain Coverage** (1-5)
   - Evidence should follow the chain: participation, reaction, learning, behavior on the job, results
   - Not every link must be measured, but omissions should be stated and justified
   - Completion and satisfaction alone are not evidence of learning or transfer
   Score: 1=Completion or satisfaction treated as success; 5=Whole chain planned with rationale for each link

2. **Objective-Evidence Traceability** (1-5)
   - Each objective maps to a measure and a named data source
   - Tracking is designed for the questions asked, not left to platform defaults
   - Stable identifiers link objectives to activities and items
   Score: 1=Course-level totals, no mapping; 5=Explicit objective-to-evidence table built before launch

3. **Measurement Quality** (1-5)
   - Timing: baseline, end of instruction, and delayed measures
   - The delayed measure tests decisions or tasks; a delayed recall quiz alone is not enough
   - Instruments measure performance, not recall or confidence alone
   - Sample size and response rate stated; non-response considered
   - Behavior measured by observation or work-system evidence, not self-report alone
   Score: 1=End-of-course satisfaction only; 5=Baseline plus delayed measures, piloted instruments, multiple agreeing sources

4. **Attribution & Comparison** (1-5)
   - Baseline and some form of comparison (comparison group, staggered rollout, trend line)
   - Success cases show that it worked for some people and why; they are not a comparison and do not support an average effect
   - No impact or return-on-investment figure without a step that isolates the training's effect
   - Other explanations for the result listed and addressed
   - Claims proportionate to the design; limits stated
   Score: 1=Causal claims from after-only data; 5=Designed comparison, alternatives examined, confidence stated

5. **Workplace Transfer Conditions** (1-5)
   - Manager support, opportunity to use, follow-up after the course ends, and workplace barriers are planned for
   - Score only what happens outside the instruction; in-course practice and review belong to archetype 03
   - These conditions are measured and reported beside outcomes
   Score: 1=Workplace not considered; 5=Managers equipped, use scheduled, spaced follow-up, barriers tracked

6. **Decision Rules & Feedback Loop** (1-5)
   - Thresholds for continue, revise, or retire set before data arrives
   - Each finding is routed to a specific part of the design with an owner
   - Versions compared on the same measures
   - Learner data handled ethically: consent, aggregation, retention, no punitive use
   Score: 1=Report is the end product; 5=Advance thresholds, routed findings, version comparison, ethics stated

Severity flags to raise: completion or satisfaction presented as effectiveness; no measure after the end of the course; objectives with no evidence mapped; causal or return-on-investment claims with no baseline or comparison; behavior claimed from self-report alone; individual learner data exposed or used punitively; findings with no route back to the design.

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following summative evaluation plan, measurement plan, or impact report.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object in this format:
{{
  "scores": {{
    "outcome_chain_coverage": <1-5>,
    "objective_evidence_traceability": <1-5>,
    "measurement_quality": <1-5>,
    "attribution_comparison": <1-5>,
    "transfer_conditions": <1-5>,
    "decision_feedback_loop": <1-5>,
    "overall": <mean of all 6>
  }},
  "rationale": {{
    "outcome_chain_coverage": "<brief explanation>",
    "objective_evidence_traceability": "<brief explanation>",
    "measurement_quality": "<brief explanation>",
    "attribution_comparison": "<brief explanation>",
    "transfer_conditions": "<brief explanation>",
    "decision_feedback_loop": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="summative_evaluation",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates summative evaluation and measurement plans (before launch) and impact reports (after launch). Scores: Outcome Chain Coverage, Objective-Evidence Traceability, Measurement Quality, Attribution & Comparison, Workplace Transfer Conditions, Decision Rules & Feedback Loop.",
    version="1.0.0",
)
