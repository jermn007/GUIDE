# Archetype 3: Instructional Sequencing & Events
## Handoff Documentation

**Purpose**: Design and evaluate lesson plans, course outlines, module structures, and learning paths for pedagogical coherence, event coverage, and instructional effectiveness. The dimensions below work in both directions: sequence against them, or score an existing sequence.

**Design targets** (using these dimensions forward, in design mode) - the moves that produce a 4-5:
- Walk Gagné's nine events in order; don't skip gain-attention, recall of prior learning, or assessment/retention.
- Match the strategy to the learning domain (intellectual skill vs. attitude vs. motor skill).
- Scaffold with gradual release (I do / we do / you do) and fade support; build in ARCS motivational beats and spaced retrieval for transfer.

Then run an evaluate-mode self-check against the scoring anchors below.

**Use Cases**:
- Peer review of lesson plans before delivery
- Course outline validation
- Online module structure assessment
- Learning pathway design review
- Curriculum mapping against Gagné's Nine Events

---

## Evaluation Dimensions

| Dimension | Scale | Definition | Key Criteria |
|-----------|-------|------------|--------------|
| **Gagné's Nine Events Coverage** | 1-5 | Are all nine events present in the instruction? | (1) Gain attention, (2) State objectives, (3) Recall prior, (4) Present content, (5) Provide guidance, (6) Elicit performance, (7) Provide feedback, (8) Assess performance, (9) Enhance retention/transfer |
| **Learning Domain Alignment** | 1-5 | Are instructional strategies appropriate for the learning domain — and do they leverage learner motivation where data is available? | Gagné's 5 domains; **Keller's ARCS as cross-cutting motivational layer**, especially for Attitudes domain |
| **Sequencing Logic** | 1-5 | Does instruction move from simple to complex, known to unknown, concrete to abstract? | Dick/Carey prerequisite analysis; hierarchical/procedural/combination sequencing |
| **Scaffolding & Gradual Release** | 1-5 | Is support provided early and gradually removed? | Initial support → guided practice → independent practice transition; Merrill's First Principles |
| **Practice & Feedback Integration** | 1-5 | Are there sufficient opportunities for practice with timely, specific feedback? | Multiple practice opportunities; confirmatory/evaluative/remedial/descriptive feedback |
| **Transfer & Retention Design** | 1-5 | Does instruction explicitly support transfer and long-term retention? | Real-world application; spaced practice; varied contexts |

---

## Scoring Guide

### Gagné's Nine Events Coverage
- **5**: All nine events clearly identifiable; logical flow and integration.
- **4**: Eight events present; one event unclear or implied.
- **3**: Six to seven events present; one to two missing or vague.
- **2**: Four to five events present; multiple missing.
- **1**: Fewer than four events; no clear instructional structure.

### Learning Domain Alignment (v3.1.0: ARCS integrated)
- **5**: Learning domain explicitly identified; all strategies match domain. For the Attitudes domain or any motivationally-sensitive content, ARCS is explicitly designed in.
- **4**: Domain clear; most strategies appropriate; one minor mismatch.
- **3**: Domain can be inferred; strategy-domain alignment partial; motivation treated as generic relevance statement.
- **2**: Domain unclear; several strategies misaligned.
- **1**: Domain not identified; strategies inappropriate for domain; learner motivation ignored when data was available.

**Domain-Strategy Matching**:
- **Verbal Information** (facts, names, definitions): Lectures, mnemonics, elaboration, chunking.
- **Intellectual Skills** (procedures, rules, concepts): Practice, feedback, part-to-whole sequencing.
- **Cognitive Strategies** (metacognition): Modeling, explicit strategy instruction, transfer practice.
- **Motor Skills**: Demonstration, practice, feedback on form/timing.
- **Attitudes** (values, beliefs, preferences, motivation): Modeling, persuasive arguments, attitude-building experiences, **and Keller's ARCS** — Attention (curiosity-grabbing entry), Relevance (tie to the learner's personal/professional goals captured in Archetype 07 L4), Confidence (early wins, clear success criteria), Satisfaction (intrinsic reward, recognition, applied outcomes).

**ARCS as a cross-cutting motivational layer (Keller, 1987 / 2010).** While ARCS is canonical for the Attitudes domain, the four conditions strengthen sequencing in any domain. When the learner profile from Archetype 07 L4 captures goals/interests/motivations, this dimension should check that the instruction *uses* them:
- **A**ttention — opening hook ties to a real problem the learner has, not generic relevance.
- **R**elevance — examples and scenarios match the learner's job/career context.
- **C**onfidence — early scaffolded wins build self-efficacy before harder tasks.
- **S**atisfaction — practice connects to outcomes the learner has named as valuable (mastery, recognition, advancement).

**If the upstream needs assessment captured ARCS data and this instruction ignores it, flag a major severity issue under this dimension regardless of domain match.**

### Sequencing Logic
- **5**: Clear progression from simple to complex; prerequisites identified; logical hierarchy.
- **4**: Generally logical sequence; minor prerequisite gaps.
- **3**: Sequence attempts progression but some items out of order; prerequisite analysis partial.
- **2**: Sequence unclear; several items illogically placed.
- **1**: Disorganized; no apparent sequence; major prerequisite violations.

### Scaffolding & Gradual Release
- **5**: Clear three-phase plan: initial support, guided practice, independent practice. Worked examples precede independent problems (Merrill).
- **4**: Scaffolding present; mostly systematic; some fading is clear.
- **3**: Some scaffolding but not systematic; support level inconsistent.
- **2**: Minimal scaffolding; learners may be unsupported in early attempts.
- **1**: No scaffolding; learners expected to work independently immediately.

### Practice & Feedback Integration
- **5**: Multiple practice opportunities (3-5+); feedback is timely, specific, varied in type.
- **4**: Adequate practice; feedback mostly timely and specific.
- **3**: Minimal practice; feedback delayed or generic.
- **2**: Little practice; feedback rare or very delayed.
- **1**: No practice or feedback; assessment only.

**Feedback Types**: Confirmatory (right/wrong), Evaluative (criterion-based), Remedial (corrective), Descriptive (specific guidance with next steps).

### Transfer & Retention Design
- **5**: Transfer explicitly addressed; practice in varied contexts; spaced review built into timeline.
- **4**: Transfer activities present; some context variety; review mentioned.
- **3**: Minimal transfer; single or limited context.
- **2**: No explicit transfer; single context; no retention strategy.
- **1**: No transfer or retention considerations.

---

## System Prompt (Judge Rubric)

```
You are an expert instructional design evaluator specializing in course design and instructional sequencing.

You assess lesson plans, course outlines, module structures, and learning paths using six dimensions:

1. Gagné's Nine Events Coverage (1-5)
   The nine events: gain attention, state objectives, recall prior learning, present content,
   provide guidance, elicit performance, provide feedback, assess performance, enhance retention/transfer.
   Events may be reordered but all should be present.

2. Learning Domain Alignment (1-5) — v3.1.0 includes ARCS as cross-cutting motivational lens.
   Gagné's 5 domains: verbal information, intellectual skills, cognitive strategies, motor skills, attitudes.
   For the Attitudes domain (and as a cross-cutting motivational lens for any domain), apply
   Keller's ARCS: Attention (curiosity hook), Relevance (tie to the learner's personal/professional
   goals from Archetype 07 L4), Confidence (early scaffolded wins, clear success criteria),
   Satisfaction (outcomes the learner has named as valuable - mastery, recognition, advancement).
   If the upstream needs assessment captured learner goals/interests/motivations and this instruction
   ignores them in favor of generic framing, that is a domain-alignment failure, not just polish.

3. Sequencing Logic (1-5)
   Dick/Carey prerequisite analysis; hierarchical/procedural/combination sequencing.

4. Scaffolding & Gradual Release (1-5)
   Initial support → guided practice → independent practice.
   Merrill's First Principles: worked examples before independent tasks.

5. Practice & Feedback Integration (1-5)
   Gagné events 6-7. Multiple practice opportunities; timely, specific, varied feedback
   (confirmatory, evaluative, remedial, descriptive).

6. Transfer & Retention Design (1-5)
   Gagné event 9; spaced practice; varied contexts; real-world application.

Return JSON with overall score (mean of 6 dimensions), individual dimension scores,
rationale per dimension, severity_flags, and improvement_suggestions.
```

---

## Human Prompt Template

```
Evaluate the following instructional artifact.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object.
```

---

## Severity Flags (Red Flags)

1. **Missing Events**: Fewer than six Gagné events; instruction is incomplete.
2. **No Assessment**: Assessment/performance check absent.
3. **No Practice or Feedback**: Instruction moves from content to assessment with no guided practice.
4. **Prerequisite Violations**: Content presented before learners have foundation.
5. **No Scaffolding Plan**: Learners expected to work independently with complex tasks immediately.
6. **Domain-Strategy Mismatch**: Verbal information taught through discovery; motor skill taught through reading only.
7. **No Transfer Plan**: Instruction stops at practice; no real-world application.
8. **ARCS Data Ignored**: Upstream Archetype 07 captured learner goals/motivations and this instruction frames everything generically (v3.1.0 major flag).

---

## Improvement Suggestions

When scoring < 4 on any dimension:

1. **Gagné's Events**: Map existing instruction to the nine events; fill gaps with targeted activities.
2. **Domain Alignment**: Identify the learning domain; select or modify strategies to match. If learner ARCS data is available, design Attention/Relevance/Confidence/Satisfaction beats per segment.
3. **Sequencing**: Conduct prerequisite analysis (Dick/Carey); reorder content simple → complex.
4. **Scaffolding**: Design three-phase scaffolding plan; worked examples early; explicit support fade.
5. **Practice & Feedback**: Add 3-5+ practice opportunities; design timely, specific, varied feedback.
6. **Transfer**: Include spaced review; practice in varied contexts; culminating real-world application.

---

## References

- Dick, W., Carey, L., & Carey, J.O. (2015). *The Systematic Design of Instruction* (8th ed.). Pearson.
- Gagné, R.M., Wager, W.W., Golas, K.C., & Keller, J.M. (2005). *Principles of Instructional Design* (5th ed.). Wadsworth/Thomson Learning.
- Keller, J.M. (1987). Development and Use of the ARCS Model of Instructional Design. *Journal of Instructional Development*, 10(3), 2-10.
- Keller, J.M. (2010). *Motivational Design for Learning and Performance: The ARCS Model Approach*. Springer.
- Merrill, M.D. (2002). First Principles of Instruction. *ETR&D*, 50(3), 43-59.
- Vygotsky, L.S. (1978). *Mind in Society*. Harvard University Press.
