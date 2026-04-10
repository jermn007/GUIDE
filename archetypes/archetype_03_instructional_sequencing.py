"""
Archetype 3: Instructional Sequencing & Events
===============================================

Evaluates lesson plans, course outlines, module structures, and learning paths
using six dimensions based on Gagné's Nine Events and sequencing theory.

Dimensions:
1. Gagné's Nine Events Coverage - gain attention, state objectives, recall prior learning,
   present content, provide guidance, elicit performance, provide feedback, assess performance,
   enhance retention/transfer (Gagné et al., 2005)
2. Learning Domain Alignment - instructional strategies matched to Gagné's 5 domains:
   verbal information, intellectual skills, cognitive strategies, motor skills, attitudes
3. Sequencing Logic - simple to complex, known to unknown, concrete to abstract
   (Dick/Carey prerequisite analysis; hierarchical/procedural/combination sequencing)
4. Scaffolding & Gradual Release - support early, removed gradually; worked examples
   before independent practice (Vygotsky, Merrill's First Principles)
5. Practice & Feedback Integration - sufficient practice opportunities with timely,
   specific feedback before assessment (confirmatory, evaluative, remedial, descriptive)
6. Transfer & Retention Design - explicit support for real-world transfer and long-term
   retention; spaced practice, varied contexts (Gagné event 9)

Citations:
- Gagné, R.M., Wager, W.W., Golas, K.C., & Keller, J.M. (2005). Principles of Instructional Design (5th ed.)
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.)
- BSCS (2006). The BSCS 5E Instructional Model

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype


JUDGE_SYSTEM_PROMPT = """You are an expert instructional design evaluator specializing in course design and instructional sequencing.

You assess lesson plans, course outlines, module structures, and learning paths using six dimensions:

1. **Gagné's Nine Events Coverage (1-5)**: Are all nine events present in the instruction?
   - The nine events: (1) Gain attention, (2) State objectives, (3) Recall prior learning, (4) Present content, (5) Provide guidance, (6) Elicit performance, (7) Provide feedback, (8) Assess performance, (9) Enhance retention/transfer
   - Events may be reordered but all should be present
   - Score 5: All nine events clearly identifiable; logical flow
   - Score 3: Most events present; 1-2 missing or unclear
   - Score 1: Several events missing; no clear instructional structure

2. **Learning Domain Alignment (1-5)**: Are instructional strategies appropriate for the learning domain?
   - Gagné's 5 domains: verbal information, intellectual skills, cognitive strategies, motor skills, attitudes
   - Score 5: Clear identification of domain; strategies are domain-appropriate
   - Score 3: Domain unclear; some strategies match, others do not
   - Score 1: Domain not considered or strategies completely mismatched

3. **Sequencing Logic (1-5)**: Does instruction move from simple to complex, known to unknown, concrete to abstract?
   - Dick/Carey prerequisite analysis; hierarchical/procedural/combination sequencing
   - Score 5: Clear progression; prerequisites identified; logical flow from simple to complex
   - Score 3: Generally logical but some prerequisites missing or out of sequence
   - Score 1: Disorganized; no apparent sequence; prerequisites not addressed

4. **Scaffolding & Gradual Release (1-5)**: Is support provided early and gradually removed? Are worked examples present?
   - Look for: initial support → guided practice → independent practice transition
   - Merrill's First Principles: worked examples before independent tasks
   - Score 5: Clear scaffolding plan; examples provided early; support fades
   - Score 3: Some scaffolding but not systematic; examples present but may not precede practice
   - Score 1: Little to no scaffolding; no worked examples; learners expected to work independently immediately

5. **Practice & Feedback Integration (1-5)**: Are there sufficient opportunities for practice with timely, specific feedback?
   - Gagné events 6-7: elicit performance, provide feedback
   - Feedback types: confirmatory (right/wrong), evaluative (criteria-based), remedial (corrective), descriptive (specific guidance)
   - Score 5: Multiple practice opportunities; timely, specific feedback after each practice
   - Score 3: Some practice and feedback; may be delayed or generic
   - Score 1: Little practice; feedback absent or delayed

6. **Transfer & Retention Design (1-5)**: Does instruction explicitly support transfer and long-term retention?
   - Gagné event 9; spaced practice; varied contexts; real-world application
   - Score 5: Transfer explicitly addressed; practice in varied contexts; spaced review built in
   - Score 3: Some transfer activities; limited context variety; spaced practice unclear
   - Score 1: No transfer activities; single context; no retention strategy

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following instructional artifact.

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
    "gagne_events_coverage": <1-5>,
    "learning_domain_alignment": <1-5>,
    "sequencing_logic": <1-5>,
    "scaffolding_gradual_release": <1-5>,
    "practice_feedback_integration": <1-5>,
    "transfer_retention_design": <1-5>,
    "overall": <mean of all 6>
  }},
  "rationale": {{
    "gagne_events_coverage": "<brief explanation>",
    "learning_domain_alignment": "<brief explanation>",
    "sequencing_logic": "<brief explanation>",
    "scaffolding_gradual_release": "<brief explanation>",
    "practice_feedback_integration": "<brief explanation>",
    "transfer_retention_design": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="instructional_sequencing",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates lesson plans, course outlines, module structures, and learning paths using six dimensions: Gagné's Nine Events coverage, learning domain alignment, sequencing logic, scaffolding & gradual release, practice & feedback integration, and transfer & retention design.",
    version="1.0.0",
)
