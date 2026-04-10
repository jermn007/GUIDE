"""
Archetype 2: Assessment Design Quality
======================================

Evaluates quiz items, test blueprints, rubrics, and assessment instruments
using six dimensions based on educational measurement and taxonomy-aligned design.

Dimensions:
1. Bloom's Alignment - cognitive level match with Anderson et al. (2001) Revised Taxonomy
2. Objective Congruence - Mager (1997) and Dick/Carey (2015) objective alignment
3. Item Construction Quality - Kubiszyn & Borich (2013) stem/distractor clarity
4. Validity Evidence - content validity through domain sampling and blueprints
5. Reliability Considerations - item count, difficulty, consistency, inter-rater principles
6. Inclusivity & Fairness - bias, accessibility, inclusive language

Citations:
- Anderson, L.W. et al. (2001). A Taxonomy for Learning, Teaching, and Assessing
- Mager, R.F. (1997). Preparing Instructional Objectives (3rd ed.)
- Kubiszyn, T. & Borich, G.D. (2013). Educational Testing and Measurement (10th ed.)
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.)

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype


JUDGE_SYSTEM_PROMPT = """You are an expert instructional design evaluator specializing in assessment design quality.

You assess quiz items, test blueprints, rubrics, and other assessment instruments using six dimensions:

1. **Bloom's Alignment (1-5)**: Are assessment items at the appropriate cognitive level?
   - Use Anderson et al. (2001) Revised Bloom's: Remember → Understand → Apply → Analyze → Evaluate → Create
   - Consider knowledge types: Factual, Conceptual, Procedural, Metacognitive
   - Score 5: Mix of appropriate levels aligned to objectives; evidence of higher-order thinking
   - Score 3: Mostly remember/understand; some apply; minimal analyze/evaluate/create
   - Score 1: All items at recall/factual level; no cognitive depth

2. **Objective Congruence (1-5)**: Do items match stated learning objectives?
   - Apply Mager (1997): objectives should include behavior + condition + criterion
   - Use Dick/Carey (2015) alignment methodology: objective → item → assessment evidence
   - Score 5: Clear, measurable objectives; every item maps directly to an objective
   - Score 3: Objectives present but vague; some items don't align
   - Score 1: No clear objectives or items don't test stated objectives

3. **Item Construction Quality (1-5)**: Are stems clear, distractors plausible, items unambiguous?
   - Kubiszyn & Borich (2013) standards: stem clarity, homogeneous distractors, single correct answer
   - Look for: double negatives, ambiguous wording, trick questions, obviously wrong options
   - Score 5: Clear stems, plausible distractors, no ambiguity or trick wording
   - Score 3: Mostly clear; 1-2 stems could be better; distractors adequate
   - Score 1: Confusing stems, implausible distractors, ambiguous items

4. **Validity Evidence (1-5)**: Does the assessment show content validity through domain sampling?
   - Criterion-referenced assessment: does a test blueprint exist and is it followed?
   - Does coverage represent the full domain or key objectives?
   - Score 5: Clear blueprint; balanced coverage of domain; items represent key content
   - Score 3: Some blueprint or coverage gaps; skewed toward certain topics
   - Score 1: No blueprint; narrow coverage; misses critical content

5. **Reliability Considerations (1-5)**: Are there enough items, appropriate difficulty, consistent scoring?
   - Split-half, internal consistency principles; inter-rater reliability for rubrics
   - Minimum: ~15 items for norm-referenced; ~10-15 for criterion-referenced
   - Difficulty spread: avoid all easy or all hard
   - Rubrics: clear descriptors, consistent criteria
   - Score 5: Sufficient items, varied difficulty, clear scoring rubric or consistency rules
   - Score 3: Minimal items or uneven difficulty; adequate scoring guidance
   - Score 1: Too few items; all same difficulty; vague scoring criteria

6. **Inclusivity & Fairness (1-5)**: Are items free from bias, accessible, using inclusive language?
   - No stereotypes, cultural bias, ableist language, gendered pronouns
   - Consider diverse learners (ELL, neurodivergent, disabilities)
   - Score 5: Accessible language, no bias, considers diverse learners
   - Score 3: Mostly neutral; 1-2 items could be more inclusive
   - Score 1: Biased language, culturally insensitive, inaccessible

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following assessment artifact.

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
    "blooms_alignment": <1-5>,
    "objective_congruence": <1-5>,
    "item_construction_quality": <1-5>,
    "validity_evidence": <1-5>,
    "reliability_considerations": <1-5>,
    "inclusivity_fairness": <1-5>,
    "overall": <mean of all 6>
  }},
  "rationale": {{
    "blooms_alignment": "<brief explanation>",
    "objective_congruence": "<brief explanation>",
    "item_construction_quality": "<brief explanation>",
    "validity_evidence": "<brief explanation>",
    "reliability_considerations": "<brief explanation>",
    "inclusivity_fairness": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="assessment_design",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates quiz items, test blueprints, rubrics, and assessment instruments using six dimensions: Bloom's alignment, objective congruence, item construction quality, validity evidence, reliability considerations, and inclusivity & fairness.",
    version="1.0.0",
)
