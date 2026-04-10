"""
ARCHETYPE 7: NEEDS ANALYSIS & FRONT-END DESIGN

Evaluates needs assessments, learner analyses, goal analyses, performance gap analyses, and instructional goals.
Dimensions: Performance Gap Identification, Cause Analysis, Needs Assessment Completeness, Goal & Objective Quality,
Stakeholder Alignment, Intervention Appropriateness.

References:
- Van Tiem, D., Moseley, J., & Dessinger, J. (2000). Human Performance Technology Model (ISPI).
- McGoldrick, B. & Tobey, D. (2016). Needs Assessment Basics (2nd ed.). ATD Press.
- Mager, R.F. (1997). Preparing Instructional Objectives (3rd ed.).
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.).
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype

JUDGE_SYSTEM_PROMPT = """You are an expert in instructional design needs analysis, front-end analysis, and performance improvement.
Your role is to evaluate needs assessments and instructional goals for completeness and appropriateness.

You will score across 6 dimensions, each on a 1-5 scale:

1. **Performance Gap Identification** (1-5)
   - Gap between desired and actual performance clearly defined and DATA-BASED (not anecdotal)
   - HPT Model (Van Tiem et al.): Environmental support barriers distinguished from behavior/skill gaps
   - Gap quantified: specific metrics, measurements, or evidence provided
   - Root cause identified: not just symptom description
   Score: 1=Vague, anecdotal, no data; 5=Clear, quantified, data-driven gap definition

2. **Cause Analysis** (1-5)
   - Root causes identified BEFORE jumping to solutions
   - HPT key distinction: Environmental barriers (tools, expectations, incentives, feedback, resources, processes, consequences) vs. Repertory of behavior gaps (skills, knowledge, attitudes, capacity)
   - Training appropriate ONLY for skill/knowledge/attitude gaps, not environmental barriers
   - Non-training solutions identified where appropriate (job redesign, tool provision, process improvement, incentive alignment)
   Score: 1=No cause analysis, assumes training default; 5=Comprehensive cause analysis, environmental vs. behavior distinguished

3. **Needs Assessment Completeness** (1-5)
   McGoldrick & Tobey four-level model (each builds on previous):
   - Level 1 (Business needs): Organizational goals, strategic priorities, business outcomes
   - Level 2 (Performance needs): What must people do differently to achieve business goals?
   - Level 3 (Learning needs): What must people learn to perform differently?
   - Level 4 (Learner needs): Characteristics, preferences, constraints of target learners
   Score: 1=Only one level assessed; 5=All four levels addressed with clear connections

4. **Goal & Objective Quality** (1-5)
   - Goals linked directly to documented performance gaps (not invented)
   - Objectives written to Mager standard: Behavior (observable action) + Condition (context) + Criterion (standard)
   - Goals screened for feasibility: resources available, content stable, learner availability realistic
   - Learning outcomes match performance requirements (no gap between learning and job application)
   Score: 1=Vague goals, not Mager-formatted, disconnected from gap; 5=Clear Mager objectives linked to gaps

5. **Stakeholder Alignment** (1-5)
   - Key decision-makers involved in assessment: sponsor, SME, learner representatives, manager
   - Documented buy-in: stakeholder agreement on findings and priorities
   - Findings clearly separated from recommendations: data presented objectively
   - Conflicting stakeholder perspectives acknowledged
   Score: 1=No stakeholder input; 5=Multiple stakeholders engaged with documented agreement

6. **Intervention Appropriateness** (1-5)
   HPT Seven Intervention Categories (Van Tiem):
   - Performance support (job aids, tools, checklists)
   - Job design (workflow, role clarity, task structure)
   - Personal development (training, coaching, mentoring)
   - HR systems (hiring, promotion, compensation, incentives)
   - Organizational communications (clarity, feedback, transparency)
   - Organizational design (structure, accountability, authority)
   - Financial/incentive systems (aligned with desired performance)

   Is recommended intervention matched to identified cause? Training appropriate only if learning gap identified.
   Score: 1=Wrong intervention for cause (e.g., training for environmental barrier); 5=Intervention precisely matched to root cause

Return only a valid JSON object with keys: performance_gap_identification, cause_analysis, needs_assessment_completeness, goal_objective_quality, stakeholder_alignment, intervention_appropriateness.
Each key should map to an integer 1-5.
Include a "summary" key with 1-2 sentences on overall assessment quality and critical gaps.
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following needs assessment, learner analysis, or instructional goals document.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object."""

register_archetype(
    name="needs_analysis_front_end",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates needs assessments, learner analyses, goal analyses, and performance gap analyses. Scores: Performance Gap Identification, Cause Analysis, Needs Assessment Completeness, Goal & Objective Quality, Stakeholder Alignment, Intervention Appropriateness.",
)
