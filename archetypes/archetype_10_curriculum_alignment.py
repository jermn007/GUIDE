"""
Archetype 10: Curriculum Alignment
==================================

Evaluates whether an instructional artifact's internal pieces — objectives,
instructional strategies (content, activities, chunking, sequencing), and
learner assessments — cohere with each other and with broader scopes
(course-level vertical progression and discipline-level competencies).

This archetype operationalizes the **Efficient** quality outcome (Merrill,
2024) - the alignment of objectives <-> strategies <-> assessments mapped
to that outcome by Hirumi (2025). It is the synthesis archetype: it does
NOT evaluate the quality of any individual component (other archetypes do
that) but whether the components, taken together, say the same thing. A course can score 5/5 on archetypes
02, 03, and 07 individually and still fail this archetype if its objectives,
instruction, and assessment teach and test different cognitive levels or
different behaviors.

Dimensions:
1. Objective <-> Strategy Coherence - instruction teaches what objective states (Tyler, 1949;
   Dick & Carey, 2015)
2. Strategy <-> Assessment Coherence - assessment measures what was taught
3. Objective <-> Assessment Coherence - verb-to-task and Bloom-level match between objective
   and assessment (Mager, 1997; Bloom 1956 / Anderson & Krathwohl, 2001; Webb's DoK, 1997)
4. Coverage Completeness - no orphan objectives, no orphan instruction; blueprint derivable
   (Wiggins & McTighe, 2005)
5. Vertical Alignment - lessons/modules build coherently; prerequisites respected (Bruner;
   Reigeluth, 1999; van Merrienboer & Kirschner, 2018)
6. Discipline Alignment - course/program aligns to professional competencies, knowledge
   base, or accrediting examinations (Hirumi, Ratliff & de la Mora, 2021; Hirumi, 2025)

Citations:
- Tyler, R.W. (1949). Basic Principles of Curriculum and Instruction
- Bloom, B.S. (1956); Anderson & Krathwohl (2001). Taxonomy of Educational Objectives
- Webb, N.L. (1997). Depth of Knowledge framework
- Mager, R.F. (1997). Preparing Instructional Objectives (3rd ed.)
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.)
- Wiggins, G., & McTighe, J. (2005). Understanding by Design (Backward Design)
- Reigeluth, C.M. (1999). Elaboration Theory
- van Merrienboer & Kirschner (2018). Ten Steps to Complex Learning (4C/ID)
- Merrill (2002). First Principles of Instruction (effective, efficient, engaging quality outcomes)
- Hirumi, Ratliff & de la Mora (2021); Hirumi (2025). Mapping the quality outcomes to alignments
  of instructional elements (objectives <-> strategies <-> assessments; theory/research alignment;
  personal/professional goal alignment)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype


JUDGE_SYSTEM_PROMPT = """You are an expert in instructional design, curriculum mapping, and Bloom's taxonomy alignment.
Your role is to evaluate whether an instructional artifact's internal pieces — objectives,
instructional strategies (content, activities, chunking, sequencing), and learner assessments —
cohere with each other and with broader scopes.

CRITICAL: You evaluate ONLY internal coherence, not the quality of any individual component.
Other GUIDE archetypes evaluate component quality:
- Archetype 02 evaluates whether the assessment itself is well-constructed.
- Archetype 03 evaluates whether the instruction is well-sequenced.
- Archetype 07 evaluates whether the objectives are well-written.

Your job is different: do the three components, taken together, say the same thing? A course
can score 5/5 on each of 02, 03, and 07 and still fail this archetype if its objectives,
instruction, and assessment teach and test different cognitive levels or different behaviors.

You will score across 6 dimensions, each on a 1-5 scale:

1. **Objective <-> Strategy Coherence** (1-5)
   - Does the instruction actually teach what the objective states?
   - Behavior verb in the objective is practiced in instruction
   - Bloom level taught matches Bloom level stated (Bloom 1956; Anderson & Krathwohl 2001)
   - No instruction exists that doesn't trace to an objective (no extraneous content)
   Score: 1=Instruction and objectives essentially disconnected; 5=Every objective verb practiced; Bloom levels match; no extraneous content

2. **Strategy <-> Assessment Coherence** (1-5)
   - Does the assessment measure what was taught?
   - Assessment tasks reflect the practice activities in format and cognitive demand
   - No surprises for the learner — same Bloom level taught is tested
   - Skills tested were actually practiced, not just mentioned
   Score: 1=Assessment tests different content than was taught; 5=Assessment mirrors practice in format and cognitive demand

3. **Objective <-> Assessment Coherence** (1-5)
   - Does the assessment test what the objective states?
   - Verb-to-task match (Mager 1997): if objective says "analyze," assessment asks for analysis
   - Bloom-level match (Bloom 1956; Anderson & Krathwohl 2001): cognitive demand of objective equals cognitive demand of assessment
   - Webb's Depth of Knowledge (Webb 1997) consistent across objective and assessment
   - The criterion stated in the objective is the criterion in the rubric
   Score: 1=Assessment tests fundamentally different behaviors than objectives state; 5=Verb, Bloom level, DoK, and criterion all match

4. **Coverage Completeness** (1-5)
   - Is every objective addressed in both instruction AND assessment?
   - Is every piece of instruction tied to an objective?
   - No orphan objectives (stated but not taught or not tested)
   - No orphan instruction (taught but not aligned to any objective)
   - A blueprint or table of specifications is present or trivially derivable (Dick & Carey 2015; Wiggins & McTighe 2005)
   Score: 1=Objectives, instruction, and assessment are three independent lists; 5=Complete coverage, no orphans, blueprint derivable

5. **Vertical Alignment** (1-5)
   - Across lessons/modules/courses, do they build coherently?
   - Prerequisites identified and respected
   - Spiral curriculum (Bruner) or elaboration logic (Reigeluth 1999) evident
   - Later content extends, not merely repeats, earlier content
   - For 4C/ID-style designs (van Merrienboer & Kirschner 2018), whole-task progression coherent
   Score: 1=Lesson/module order is arbitrary or reverse-coherent; 5=Clear vertical logic; prerequisites respected; progression builds
   Note: For single-lesson artifacts, score within-lesson sequencing instead and flag the adaptation in rationale.

6. **Discipline Alignment** (1-5)
   - Does the course/program align to professional competencies, knowledge base, or accrediting examinations?
   - Stated linkage to external competency framework
   - Every objective at the unit/lesson level maps upward to a competency at the discipline level (Hirumi, Ratliff & de la Mora 2021; Hirumi 2025, Figure 1)
   Score: 1=No stated discipline-level alignment; 5=Explicit traceable linkage; every objective maps upward
   Note: For artifacts not intended to align with a discipline (one-off workshops, internal training), score on internal coherence with stated purpose and note the adaptation in rationale.

Return JSON with overall score (mean of 6 dimensions; cap at 3.0 if Objective <-> Assessment Coherence scores 1 or 2),
individual dimension scores, rationale per dimension, severity_flags (critical issues),
and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the internal alignment of the following instructional artifact.

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
    "objective_strategy_coherence": <1-5>,
    "strategy_assessment_coherence": <1-5>,
    "objective_assessment_coherence": <1-5>,
    "coverage_completeness": <1-5>,
    "vertical_alignment": <1-5>,
    "discipline_alignment": <1-5>,
    "overall": <mean of all 6, capped at 3.0 if objective_assessment_coherence <= 2>
  }},
  "rationale": {{
    "objective_strategy_coherence": "<brief explanation citing specific evidence>",
    "strategy_assessment_coherence": "<brief explanation>",
    "objective_assessment_coherence": "<brief explanation>",
    "coverage_completeness": "<brief explanation>",
    "vertical_alignment": "<brief explanation>",
    "discipline_alignment": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="curriculum_alignment",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates whether an instructional artifact's objectives, instructional strategies, and learner assessments cohere with each other and with broader scopes (vertical progression, discipline-level competencies). Operationalizes the Efficient quality outcome (Merrill, 2002) per the alignment mapping in Hirumi (2025). Dimensions: Objective<->Strategy Coherence, Strategy<->Assessment Coherence, Objective<->Assessment Coherence, Coverage Completeness, Vertical Alignment, Discipline Alignment.",
    version="1.0.0",
)
