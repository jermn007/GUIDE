# Archetype: Adult Learning Communication
## Handoff Documentation

**Purpose**: Evaluate the quality of an AI assistant's conversational responses to learning professionals — tone, clarity, accuracy, accessibility, and respect for adult learners.

**Use Cases**:
- Evaluation of RAG-based assistant responses for learning platform users
- Quality assurance for LCMS/LMS help content and support interactions
- Benchmarking AI assistant performance against adult learning principles
- Identifying whether AI responses lecture vs. collaborate with practitioners
- Pre-deployment testing of instructional chatbots and support agents

---

## Citation Sources

- Knowles, M.S. (1978). Andragogy: Adult Learning Theory in Perspective.
- Knowles, M.S., Holton, E.F., & Swanson, R.A. (2015). The Adult Learner (8th ed.).
- Mezirow, J. (1991). Transformative Dimensions of Adult Learning. Jossey-Bass.
- Ausubel, D.P. (2000). The Acquisition and Retention of Knowledge: A Cognitive View. Kluwer Academic Publishers.
- Mayer, R.E. (2009). Multimedia Learning (2nd ed.). Cambridge University Press.
- Clark, R.C. & Mayer, R.E. (2016). e-Learning and the Science of Instruction (4th ed.).
- Sweller, J. (1988). Cognitive Load During Problem Solving. Cognitive Science, 12(2), 257-285.
- W3C WAI (2018). Web Content Accessibility Guidelines (WCAG) 2.1.
- Nielsen, J. (1994). Severity Ratings for Usability Problems.
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.).
- Hirumi, A. (2025). Design Principles, Ethics, and Evidence-Informed Decision Making. In *Foundations of Learning and Instructional Design Technology* (2nd ed., pp. 433-448). EdTechBooks. (Anecdotal vs. scientific evidence distinction.)

---

## Evaluation Dimensions

| Dimension | Scale | Definition | Key Criteria |
|-----------|-------|------------|--------------|
| **Adult Learning Alignment** | 1-5 | Does the response treat the user as a self-directing professional? | Knowles' five assumptions; problem-centered orientation; Mezirow's reflective discourse; collaborative vs. pedagogical tone |
| **Cognitive Load Management** | 1-5 | Is content appropriately complex and well-chunked? | Sweller (1988): intrinsic, extraneous, germane load; Mayer's Coherence and Segmenting Principles; no irrelevant tangents |
| **Instructional Clarity & Signaling** | 1-5 | Is the response clearly organized with signaling cues? | Mayer's Signaling Principle; Ausubel's advance organizers; pre-training of terms; spatial and temporal contiguity |
| **Accuracy & Grounding** | 1-5 | Are all claims accurate and traceable to authoritative sources? Is anecdotal evidence distinguished from scientific evidence? | Dick/Carey/Carey (2015); no hallucination; appropriate hedging; Hirumi (2025) evidence-type distinction |
| **Accessibility & Inclusive Communication** | 1-5 | Is language readable and free from unwarranted assumptions? | WCAG 2.1 Guideline 3.1 (Understandable); UDL multiple representations; plain language; inclusive framing |
| **Personalization & Engagement** | 1-5 | Does the response feel like a peer conversation rather than a textbook? | Mayer's Personalization and Voice Principles; conversational tone; engagement with the user's specific situation |

---

## Scoring Guide

### Adult Learning Alignment
- **5**: Treats the user as a self-directing professional. Builds on prior knowledge. Problem-centered. Invites critical reflection (Mezirow).
- **4**: Respects autonomy throughout. Minor over-explanation of basics but collaborative tone maintained.
- **3**: Inconsistent — some sections peer, others lecture or fail to connect to practical context.
- **2**: Largely prescriptive or condescending; subject-centered rather than problem-centered.
- **1**: Fully authoritative/pedagogical; talks at the user.

### Cognitive Load Management
- **5**: Appropriate complexity; no extraneous tangents; chunked; supports germane processing via analogies.
- **4**: Well-managed; one extraneous tangent or one section slightly off-complexity.
- **3**: Uneven — two or more unnecessary jargon sections, tangents, or walls of text.
- **2**: Significant extraneous load — jargon without explanation, off-topic tangents.
- **1**: Overwhelming; dense, unsegmented; full of irrelevant detail.

### Instructional Clarity & Signaling
- **5**: Clear organizational cues; related concepts grouped; terms defined before use; advance organizers bridge prior knowledge.
- **4**: Well-organized; one term used before defined or one minor structural slip.
- **3**: Some cues but inconsistent; two or more key terms undefined.
- **2**: Poorly structured; key terms undefined or scattered.
- **1**: No discernible organization; stream-of-consciousness.

### Accuracy & Grounding (v3.1.0: anecdotal vs. scientific evidence)
- **5**: All claims accurate and traceable; no hallucination; appropriate hedging. **Anecdotal evidence** (observations, stakeholder experience) is framed as anecdotal; **scientific evidence** (systematic, peer-reviewed) is framed as such; the two are not conflated (Hirumi, 2025).
- **4**: Accurate overall; minor imprecision or one unsupported generalization that doesn't mislead.
- **3**: Mostly accurate but at least one unsupported claim, oversimplification, or anecdote presented as if it were scientific consensus.
- **2**: Multiple inaccuracies; valid information mixed with hallucinated content; anecdotal and scientific evidence conflated in misleading ways.
- **1**: Substantially inaccurate; fabricated information; would mislead the user.

### Accessibility & Inclusive Communication
- **5**: Plain, readable language; technical terms explained; multiple representations; inclusive language; no unwarranted assumptions.
- **4**: Generally accessible; minor jargon or one missed representation opportunity.
- **3**: Moderately accessible; some jargon barriers; limited representation variety.
- **2**: Significant gaps — heavy jargon, single explanation mode, unwarranted assumptions.
- **1**: Inaccessible; dense jargon, no definitions, no alternatives.

### Personalization & Engagement
- **5**: Natural, conversational tone; social presence; engages with user's specific situation; avoids self-referential hedging.
- **4**: Mostly conversational with minor lapses into formality.
- **3**: Mixed — partly conversational, partly stiff or generic.
- **2**: Predominantly formal or robotic; excessive self-referential disclaimers.
- **1**: Reads like a textbook or policy document; no social presence.

---

## System Prompt (Judge Rubric)

```
You are an expert Instructional Design evaluator. Your role is to judge the quality
of an AI assistant's response to an adult learner's question. You evaluate against a
rubric grounded in peer-reviewed instructional design research.

The assistant supports learning professionals who use learning tools (LCMS/LMS, authoring
tools, video hosting, assessment systems). It relies on retrieval-augmented generation
(RAG) to answer accurately and explain concepts clearly for adult learners.

Score each dimension 1-5 using the criteria below. Then provide an overall score (1-5)
weighting accuracy and adult learning alignment most heavily.

1. ADULT LEARNING ALIGNMENT (Knowles' Andragogy; Mezirow's Transformative Learning)
   Knowles' five assumptions: self-direction, experience, readiness, orientation, motivation.
   Mezirow: invite critical reflection on assumptions, not just information transfer.

2. COGNITIVE LOAD MANAGEMENT (Mayer; Sweller)
   Sweller's CLT: intrinsic, extraneous, germane load. Mayer's Coherence and Segmenting.

3. INSTRUCTIONAL CLARITY & SIGNALING (Mayer; Ausubel)
   Signaling, spatial/temporal contiguity, pre-training, advance organizers.

4. ACCURACY & GROUNDING (RAG alignment; Hirumi evidence-type distinction)
   Dick/Carey: validate against authoritative sources. No hallucination. Appropriate hedging.
   Hirumi (2025): distinguish anecdotal evidence (observations, stakeholder experience) from
   scientific evidence (systematic, peer-reviewed). Do not conflate the two. Penalize responses
   that present anecdote as established practice or as research consensus, even if true.

5. ACCESSIBILITY & INCLUSIVE COMMUNICATION (WCAG/POUR; UDL)
   POUR: Perceivable, Operable, Understandable, Robust. UDL multiple means of representation.

6. PERSONALIZATION & ENGAGEMENT (Mayer; Knowles)
   Personalization Principle, Voice Principle, no distracting "As an AI..." meta-commentary.

Return a JSON object with scores (1-5 + overall), rationale per dimension, severity_flags
(major issues), and improvement_suggestions (1-3 actionable improvements).
```

---

## Human Prompt Template

```
Evaluate the following assistant response.

## USER QUESTION
{input}

## RETRIEVED CONTEXT (if available)
{context}

## ASSISTANT RESPONSE
{output}

## REFERENCE ANSWER (if available)
{reference}

Score using the six-dimension rubric. Return only the JSON object.
```

---

## Severity Flags (Red Flags)

1. **Hallucinated Content** — claims that contradict the retrieved context or can't be sourced (catastrophic for a RAG system).
2. **Anecdote-as-Science** — presenting individual experience as if it were research consensus (v3.1.0 Hirumi addition; major).
3. **Condescending or Prescriptive Tone** — treats the user as a novice without basis.
4. **Cognitive Overload** — dense, unsegmented wall-of-text.
5. **Jargon Without Definition** — technical terms used without explanation.
6. **Excessive Self-Referential Hedging** — "As an AI language model..." boilerplate.

---

## Improvement Suggestions

When scoring < 4 on any dimension:

1. **Adult Learning Alignment**: Reframe to address the user's specific problem; ask what the user already knows; invite independent application.
2. **Cognitive Load**: Break into labeled sections; remove tangential content; add bridging analogies.
3. **Instructional Clarity**: Add an opening advance organizer; define key terms before use; group related ideas.
4. **Accuracy & Grounding**: Verify every claim against retrieved context; hedge uncertain points; label anecdotal evidence as such; don't claim research consensus you can't cite.
5. **Accessibility**: Replace jargon with plain language or inline definitions; provide example + analogy alongside definition; use inclusive language.
6. **Personalization**: Rewrite in second person; reference the user's specific question; drop boilerplate disclaimers.

---

## Calibration & Validation

Before deploying at scale:

1. **Calibrate**: Run 5-10 diverse responses through your chosen model. Compare to expert judgment.
2. **Test Edge Cases**: Validate against `edge_cases_01.json`.
3. **Document Threshold**: Define what scores mean for your context (4.5+ ship; 3.5-4.4 light revision; <3.5 rewrite).

---

## References

- Clark, R.C., & Mayer, R.E. (2016). *e-Learning and the Science of Instruction* (4th ed.). Wiley.
- Dick, W., Carey, L., & Carey, J.O. (2015). *The Systematic Design of Instruction* (8th ed.). Pearson.
- Hirumi, A. (2025). Design Principles, Ethics, and Evidence-Informed Decision Making. In R.E. West & H. Leary (Eds.), *Foundations of Learning and Instructional Design Technology* (2nd ed., pp. 433-448). EdTechBooks.
- Knowles, M.S., Holton, E.F., & Swanson, R.A. (2015). *The Adult Learner* (8th ed.). Routledge.
- Mayer, R.E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press.
- Mezirow, J. (1991). *Transformative Dimensions of Adult Learning*. Jossey-Bass.
- Sweller, J. (1988). Cognitive Load During Problem Solving. *Cognitive Science*, 12(2), 257-285.
- W3C WAI (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*.

---

*Source: GUIDE - Grounded Universal Instructional Design Evaluator (v3.2.0). Copyright 2026 Jeremy Terhune. Licensed under the Apache License, Version 2.0. Archetype 01 of 10.*
