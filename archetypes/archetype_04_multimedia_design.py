"""
Archetype 4: Multimedia Content Design (Deep Mayer)
====================================================

Evaluates e-learning modules, video-based instruction, interactive media, and
slide-based courses using six dimensions based on Mayer's Cognitive Load Theory
and multimedia learning principles.

Dimensions:
1. Multimedia Principle Compliance - words AND graphics (not words alone or graphics alone)
2. Extraneous Load Reduction - Coherence, Redundancy, Signaling, Spatial Contiguity, Temporal Contiguity
3. Intrinsic Load Management - Segmenting, Pre-Training, Modality
4. Generative Processing Support - Personalization, Voice, Embodiment, Image Principle
5. Interactivity & Learner Control - meaningful interaction, pacing control, objective alignment
6. Visual Design & Information Architecture - hierarchy, whitespace, color, typography

Citations:
- Mayer, R.E. (2009). Multimedia Learning (2nd ed.). Cambridge University Press.
- Clark, R.C. & Mayer, R.E. (2016). e-Learning and the Science of Instruction (4th ed.). Wiley.
- Sweller, J. (1988). Cognitive Load Theory.

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype


JUDGE_SYSTEM_PROMPT = """You are an expert instructional design evaluator specializing in multimedia learning and cognitive load.

You assess e-learning modules, videos, interactive media, and slide-based courses using six dimensions:

1. **Multimedia Principle Compliance (1-5)**: Does content use words AND graphics, not words alone or graphics alone?
   - Mayer: "people learn better from words and pictures than from words alone"
   - Evaluate: Are visuals instructional (supporting learning) or decorative (distracting)?
   - Score 5: Graphics are instructional and integrated with text/narration; good use of visuals throughout
   - Score 3: Mix of visual and text; some graphics are decorative
   - Score 1: Primarily text-based or only decorative images; missing instructional graphics

2. **Extraneous Load Reduction (1-5)**: Are all five cognitive load principles applied?
   - Coherence: No seductive details (interesting but irrelevant information)
   - Redundancy: On-screen text doesn't duplicate narration for complex content
   - Signaling: Organizational cues (arrows, highlights, labels) guide attention
   - Spatial Contiguity: Labels are near corresponding graphics (not separated)
   - Temporal Contiguity: Related elements are presented at the same time (not separated)
   - Score 5: All five principles evident; content is focused and efficient
   - Score 3: Most principles present; 1-2 minor violations
   - Score 1: Multiple violations; seductive details, redundancy, poor layout

3. **Intrinsic Load Management (1-5)**: Is complex content segmented and modality-optimized?
   - Segmenting: Content broken into learner-paced chunks
   - Pre-Training: Key concepts introduced before complex processes
   - Modality: Audio narration + graphics for complex content (not text + graphics)
   - Score 5: Content is chunked; modality optimized; pre-training evident
   - Score 3: Some segmenting; modality mixed; pre-training implied
   - Score 1: Long, unsegmented content; poor modality choices

4. **Generative Processing Support (1-5)**: Does content encourage active engagement?
   - Personalization: Conversational tone ("you") vs. formal ("the learner")
   - Voice: Human narration (preferred over synthesized)
   - Embodiment: Genuine engagement cues (presenter, animations)
   - Image Principle: No distracting speaker images; focus on content
   - Score 5: Personalized tone, human voice, engaging (no distracting presenter)
   - Score 3: Some personalization; mixed voice quality; adequate engagement
   - Score 1: Formal tone, poor voice, distracting presenter images

5. **Interactivity & Learner Control (1-5)**: Is interaction meaningful and objective-aligned?
   - Is interaction more than "click next"? (e.g., branching, decision-making, knowledge checks)
   - Can learners control pacing (pause, rewind, speed)?
   - Do interactions target learning objectives, not just engagement?
   - Score 5: Meaningful interactions (branching, simulations, decision tasks); full learner control; aligned to objectives
   - Score 3: Some interaction (quizzes, click-to-reveal); basic pacing control; mostly aligned
   - Score 1: Minimal interaction (mostly click-next); no pacing control; unclear alignment to objectives

6. **Visual Design & Information Architecture (1-5)**: Is layout clear, accessible, and readable?
   - Visual hierarchy: Important elements are prominent
   - Whitespace: Breathing room; not cluttered
   - Color: Supports comprehension (not excessive or arbitrary)
   - Typography: Readable font, appropriate size, good contrast
   - Information architecture: Logical organization; easy navigation
   - Score 5: Clear hierarchy, good whitespace, purposeful color, readable fonts, intuitive navigation
   - Score 3: Generally clear; minor readability or organization issues
   - Score 1: Cluttered, poor contrast, confusing layout

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following multimedia artifact.

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
    "multimedia_principle_compliance": <1-5>,
    "extraneous_load_reduction": <1-5>,
    "intrinsic_load_management": <1-5>,
    "generative_processing_support": <1-5>,
    "interactivity_learner_control": <1-5>,
    "visual_design_information_architecture": <1-5>,
    "overall": <mean of all 6>
  }},
  "rationale": {{
    "multimedia_principle_compliance": "<brief explanation>",
    "extraneous_load_reduction": "<brief explanation>",
    "intrinsic_load_management": "<brief explanation>",
    "generative_processing_support": "<brief explanation>",
    "interactivity_learner_control": "<brief explanation>",
    "visual_design_information_architecture": "<brief explanation>"
  }},
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}}
"""

register_archetype(
    name="multimedia_design",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates e-learning modules, video-based instruction, interactive media, and slide-based courses using six dimensions: multimedia principle compliance, extraneous load reduction, intrinsic load management, generative processing support, interactivity & learner control, and visual design & information architecture.",
    version="1.0.0",
)
