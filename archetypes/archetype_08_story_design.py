"""
Archetype 8: Story & Narrative Design for Instruction
======================================================

Evaluates scenario-based learning, narrative structures in training, case studies,
branching scenarios, and story-driven instruction using six dimensions grounded in
narrative pedagogy and storytelling frameworks.

Dimensions:
1. Narrative Structure - Story Circle/Pixar or Campbell's Hero's Journey framework
2. Learning-Narrative Integration - Are learning objectives embedded naturally?
3. Character & Situation Authenticity - Relatable characters, realistic scenarios
4. Emotional Engagement & Motivation - Productive tension and emotional stakes
5. Decision Points & Branching Quality - Meaningful choices with distinct consequences
6. Transfer & Generalizability - Can learners extract principles for their own contexts?

Citations:
- Pixar Story Circle / Story Spine framework (EME6346 course materials)
- Campbell, J. (1949). The Hero with a Thousand Faces
- EME6346 Module 2: Storytelling Framework Analysis rubric

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype


JUDGE_SYSTEM_PROMPT = """You are an expert instructional design evaluator specializing in narrative and story-based learning design.

You assess scenario-based learning, narrative structures in training, case studies, branching scenarios, and story-driven instruction using six dimensions:

1. **Narrative Structure (1-5)**: Does the story follow a recognized structural framework?
   - Story Circle/Pixar: "Once upon a time → Every day → One day → Because of that → Until finally → Ever since then → Moral"
   - Campbell's Hero's Journey: Ordinary world → Call to adventure → Refusal of the call → Meeting the mentor → Crossing the threshold → Tests and allies → Ordeal → Reward → The road back → Return with the elixir
   - Structure need not be rigid but should be identifiable and coherent
   - Score 5: Clear, recognizable structure; story arc is well-developed; beginning, middle, end are distinct
   - Score 3: Some structural elements present; story is coherent but structure is loose or one phase is underdeveloped
   - Score 1: No recognizable structure; story feels random, fragmentary, or lacks narrative coherence

2. **Learning-Narrative Integration (1-5)**: Are learning objectives embedded naturally within the narrative?
   - Does the story serve the instruction, or does instruction interrupt the story?
   - Best practice: impossible to separate the learning from the narrative
   - Learning objectives should emerge from the story tension, not be imposed as external lessons
   - Score 5: Learning objectives are woven into the story fabric; narrative tension drives learning; no artificial "here's the lesson" moments
   - Score 3: Learning objectives present and mostly integrated; some moments where instruction feels overlaid on the story
   - Score 1: Learning objectives are tacked on; instruction regularly interrupts narrative flow; story and learning feel disconnected

3. **Character & Situation Authenticity (1-5)**: Are characters relatable to target audience? Are scenarios realistic?
   - Characters should face genuine decisions, not obvious right/wrong choices
   - Scenarios should reflect learners' actual work/life contexts
   - Emotional stakes should feel earned and believable
   - Score 5: Characters are vivid, relatable, with realistic motivations; scenarios are grounded in learner reality; decisions involve genuine dilemmas
   - Score 3: Characters are adequate; scenarios are recognizable but somewhat idealized; some decisions feel a bit contrived
   - Score 1: Characters feel generic or unrelatable; scenarios are unrealistic or clichéd; decisions lack authenticity

4. **Emotional Engagement & Motivation (1-5)**: Does the narrative create productive tension that drives engagement?
   - Emotional stakes should amplify learning, not impair it
   - Look for: conflict, mystery, curiosity, meaningful consequences, authentic stakes
   - Productive tension motivates deeper processing; anxiety impairs learning
   - Score 5: Story creates genuine emotional engagement; productive tension throughout; emotional arcs serve learning; no anxiety that blocks processing
   - Score 3: Moderate emotional engagement; some tension; mostly productive but occasional moments that might overwhelm some learners
   - Score 1: Flat affect or overwhelming anxiety; emotional engagement is absent or counterproductive to learning

5. **Decision Points & Branching Quality (1-5)**: Are decision points meaningful with distinct, logical consequences?
   - For interactive/branching scenarios: choices should have real impact
   - Consequences should be instructive, not arbitrary or punitive
   - Wrong paths should teach something, not just say "try again"
   - Branches should represent genuine complexity, not surface variation
   - Score 5: Decision points are abundant and meaningful; each choice has distinct consequences; wrong paths are instructive; branches diverge significantly
   - Score 3: Some meaningful decisions; most choices have consequences but they might feel forced; some branches overlap
   - Score 1: Few or no real decisions; consequences feel random; wrong paths are dismissive; little branching complexity

6. **Transfer & Generalizability (1-5)**: Can learners extract principles that apply to their own situations?
   - Story should be specific enough to be engaging but general enough to be applicable
   - Narrative should explicitly or implicitly support transfer of learning to real contexts
   - Score 5: Clear principles emerge that transfer; story is grounded enough to be engaging but open enough for generalization; metacognitive reflection supported
   - Score 3: Some transferable principles; story is moderately specific; learners can see connections but transfer isn't guaranteed
   - Score 1: Story is too context-specific to generalize; principles are unclear; learners may see no connection to their own situations

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following narrative/story-based learning artifact.

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
    "narrative_structure": <1-5>,
    "learning_narrative_integration": <1-5>,
    "character_situation_authenticity": <1-5>,
    "emotional_engagement_motivation": <1-5>,
    "decision_points_branching_quality": <1-5>,
    "transfer_generalizability": <1-5>,
    "overall": <mean of all 6>
  }},
  "rationale": {{
    "narrative_structure": "<brief explanation>",
    "learning_narrative_integration": "<brief explanation>",
    "character_situation_authenticity": "<brief explanation>",
    "emotional_engagement_motivation": "<brief explanation>",
    "decision_points_branching_quality": "<brief explanation>",
    "transfer_generalizability": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="story_design",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates scenario-based learning, narrative structures in training, case studies, branching scenarios, and story-driven instruction using six dimensions: narrative structure, learning-narrative integration, character & situation authenticity, emotional engagement & motivation, decision points & branching quality, and transfer & generalizability.",
    version="1.0.0",
)
