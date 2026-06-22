# GUIDE Archetype Index & Router

This is the routing map for the GUIDE framework. Use it to pick the right archetype(s) for any
instructional-design task, then open the matching `handoff_XX_*.md` file for the full grounding text,
scoring anchors, judge prompt, and output format.

GUIDE = **G**rounded **U**niversal **I**nstructional **D**esign **E**valuator. **Ten** archetypes,
**60** dimensions (6 per archetype), each grounded in named learning-science sources and scored 1–5
with behavioral anchors. Built on the LLM-as-a-judge pattern (Zheng et al., 2023). Tracks GUIDE v3.2.1.

**What's new in v3.1.0:** Archetype **10 Curriculum Alignment** (synthesis archetype, evaluates
relationships between objectives ↔ strategies ↔ assessments). Archetypes **03 Sequencing** and
**07 Needs Analysis** integrate **Keller's ARCS** (motivational design). Archetype **01 Adult
Learning Communication** adopts **Hirumi's Three Alignments** framework (Merrill 2002 quality triad).
Across the framework, alignment to *personal/professional goals* is now an evaluable design element.

---

## The 10 archetypes mapped to ADDIE

| # | Archetype | ADDIE phase | Theorists | Reference file |
|---|-----------|-------------|-----------|----------------|
| 7 | Needs Analysis & Front-End Design | **A**nalyze | Van Tiem (HPT), McGoldrick & Tobey, Mager, Keller (ARCS), Hirumi | `handoff_07_needs_analysis.md` |
| 3 | Instructional Sequencing & Events | **D**esign | Gagné, Reigeluth, van Merriënboer, Merrill, Dick & Carey, Keller (ARCS) | `handoff_03_instructional_sequencing.md` |
| 8 | Story & Narrative Design | **D**esign | Campbell, Snyder (Beat Sheet), Story Circle | `handoff_08_story_design.md` |
| 9 | Cognitive Neuroscience & Brain-Based Instruction | **D**esign | BSCS 5E, Ausubel, Brown/Roediger/McDaniel, Posner & Rothbart | `handoff_09_cognitive_neuroscience.md` |
| 4 | Multimedia Content Design (Deep Mayer) | **D**evelop | Mayer, Paivio, Sweller, Clark | `handoff_04_multimedia_design.md` |
| 5 | WCAG/POUR Technical Accessibility | **D**evelop | WCAG 2.1, CAST UDL, Section 508, Nielsen | `handoff_05_accessibility_technical.md` |
| 1 | Adult Learning Communication | **I**mplement | Knowles, Mezirow, Ausubel, Mayer, Hirumi (Three Alignments) | `handoff_01_adult_learning_communication.md` |
| 2 | Assessment Design Quality | **E**valuate | Bloom/Anderson & Krathwohl, Webb, Messick, Mager, Kubiszyn & Borich | `handoff_02_assessment_design.md` |
| 6 | Formative Evaluation Protocol Quality | **E**valuate | Bordonaro, Dick & Carey, Nielsen, Scriven, Kirkpatrick | `handoff_06_formative_evaluation.md` |
| **10** | **Curriculum Alignment (Synthesis)** | **Cross-cutting** | Tyler, Bloom/Anderson & Krathwohl, Webb (DoK), Mager, Wiggins & McTighe, Reigeluth, van Merriënboer & Kirschner, Merrill (2002), Hirumi (2021, 2025) | `handoff_10_curriculum_alignment.md` |

**Archetype 10 is the synthesis archetype.** It evaluates *relationships between* objectives, instructional
strategies, and assessments — not the quality of any individual component (other archetypes do that).
A course can score 5/5 on archetypes 02, 03, and 07 individually and still fail 10. That is exactly
the failure mode 10 is designed to catch.

---

## What each archetype evaluates (artifact → archetype)

Use this to route. Match the artifact in front of you to the archetype whose object of evaluation it is.

- **A request for training, a problem statement, a learner/audience profile, a goal or objectives list, a performance-gap write-up** → **07 Needs Analysis**. Ask first: is training even the right intervention?
- **A lesson plan, course outline, module structure, syllabus, or learning path** → **03 Instructional Sequencing**.
- **A scenario, case study, branching scenario, role-play, or any narrative-driven lesson** → **08 Story Design**.
- **Any instruction you want judged against how the brain actually learns (memory, attention, emotion, 5E)** → **09 Cognitive Neuroscience**.
- **An e-learning module, video, slide deck, animation, or interactive media** → **04 Multimedia Design**.
- **A web page, LMS shell, digital course material, or anything that must meet WCAG/UDL** → **05 Accessibility**.
- **A chatbot/RAG answer, help-desk reply, or any conversational response to a learning professional** → **01 Adult Learning Communication**.
- **A quiz, test, item bank, rubric, or test blueprint** → **02 Assessment Design**.
- **An evaluation plan, usability test, expert-review protocol, or pilot study design** → **06 Formative Evaluation**.
- **A complete artifact set (objectives + instruction + assessment) where you want to verify they actually agree** → **10 Curriculum Alignment**. Always run this as the final gate when you have all three components.

**Multiple archetypes often apply.** A narrated e-learning scenario could be scored by 04 (multimedia),
08 (story), 05 (accessibility), and 09 (neuroscience), then have its full alignment checked by 10.
Pick the 1–3 component archetypes that match primary purpose, then always end with 10 if the artifact
set is complete.

---

## The 60 dimensions at a glance

Each archetype scores six dimensions 1–5. Overall is normally the mean of the six. **Archetype 01**
weights Accuracy and Adult Learning Alignment most heavily. **Archetype 10** caps overall at 3.0 if
`objective_assessment_coherence ≤ 2`.

**01 Adult Learning Communication** — Adult Learning Alignment · Cognitive Load Management ·
Instructional Clarity & Signaling · Accuracy & Grounding · Accessibility & Inclusive Communication
· Personalization & Engagement.

**02 Assessment Design** — Bloom's Alignment · Objective Congruence · Item Construction Quality ·
Validity Evidence · Reliability Considerations · Inclusivity & Fairness.

**03 Instructional Sequencing** — Gagné's Nine Events Coverage · Learning Domain Alignment ·
Sequencing Logic · Scaffolding & Gradual Release · Practice & Feedback Integration · Transfer &
Retention Design. *(ARCS integrated across.)*

**04 Multimedia Design** — Multimedia Principle Compliance · Extraneous Load Reduction · Intrinsic
Load Management · Generative Processing Support · Interactivity & Learner Control · Visual Design &
Information Architecture.

**05 Accessibility (WCAG/POUR)** — Perceivable · Operable · Understandable · Robust · UDL Integration
· Remediation Feasibility.

**06 Formative Evaluation** — Phase Coverage · Evaluator Selection · Data Collection Alignment ·
Revision Decision Framework · Feasibility & Practicality · Usability Engineering Integration.

**07 Needs Analysis** — Performance Gap Identification · Cause Analysis · Needs Assessment Completeness
· Goal & Objective Quality · Stakeholder Alignment · Intervention Appropriateness. *(ARCS at L4
learner profile; Hirumi anecdotal-vs-scientific framing.)*

**08 Story Design** — Narrative Structure · Learning-Narrative Integration · Character & Situation
Authenticity · Emotional Engagement & Motivation · Decision Points & Branching Quality · Transfer &
Generalizability.

**09 Cognitive Neuroscience** — 5E Model Alignment · Memory System Optimization · Attention Management
· Emotional Engagement for Encoding · Synaptic Strengthening Factors · Theory-Practice Grounding.

**10 Curriculum Alignment** — Objective ↔ Strategy Coherence · Strategy ↔ Assessment Coherence ·
Objective ↔ Assessment Coherence · Coverage Completeness · Vertical Alignment · Discipline Alignment.
*(Cap rule: if Objective ↔ Assessment ≤ 2, overall capped at 3.0.)*

---

## The 1–5 scale (shared across all archetypes)

- **5 — Exemplary**: Fully meets the criterion; theory-grounded; nothing to fix.
- **4 — Strong**: Meets the criterion with one minor gap.
- **3 — Adequate / uneven**: Partially meets it; two or more noticeable gaps.
- **2 — Weak**: Significant problems; criterion mostly unmet.
- **1 — Inadequate**: Criterion not met; would mislead, exclude, or fail learners.

**Composite interpretation thresholds** (adapt to context; defaults from the handoff docs):
- **4.5–5.0** — Publish/ship as-is.
- **3.5–4.4** — Light revision; ship with documented gaps.
- **2.5–3.4** — Real concerns; revise before wide rollout.
- **< 2.5** — Redesign; do not ship.

---

## Recurring cross-archetype concepts

Several theories appear in multiple archetypes. When designing or evaluating, these are the load-bearing ideas:

- **Mager-format objectives** (Behavior + Condition + Criterion; observable verbs, never "understand/know") — 02, 07, 10.
- **Cognitive Load Theory** (Sweller: intrinsic / extraneous / germane) — 01, 04, 09.
- **Alignment** (objective → instruction → assessment; Tyler, Dick & Carey, Wiggins & McTighe) — 02, 03, 07, **10 (synthesis)**.
- **Bloom / Webb DoK** (cognitive level + depth of knowledge) — 02, 10.
- **Mayer's multimedia principles** (coherence, signaling, redundancy, contiguity, modality, personalization) — 01, 04.
- **Retrieval practice & spacing** (Brown/Roediger/McDaniel; "Make It Stick") — 03, 09.
- **Advance organizers / meaningful learning** (Ausubel) — 01, 03, 09.
- **UDL — multiple means of representation, action/expression, engagement** (CAST) — 05, plus accessibility threads in 01, 02, 04.
- **Transfer** (application in varied/authentic contexts) — 03, 08, 09, 10 (Vertical).
- **ARCS — Attention, Relevance, Confidence, Satisfaction** (Keller) — 03, 07.
- **Hirumi's Three Alignments** (Merrill 2002 effective/efficient/engaging mapped to alignments) — 01, 07, 10.
- **HPT cause analysis** — the gatekeeper question in 07.
- **Nielsen severity ratings** (cosmetic / minor / major / catastrophic) — used for severity flags in 01, 05, 06, 10.

---

## Source

GUIDE — Grounded Universal Instructional Design Evaluator (v3.2.1).
Repository: github.com/jermn007/GUIDE. Copyright 2026 Jeremy Terhune. Apache-2.0.
This index condenses the ten `handoff_*.md` files in this directory; those files are the authoritative source.
