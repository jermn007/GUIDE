# GUIDE Archetype Index & Router

This is the routing map for the GUIDE framework. Use it to pick the right archetype(s) for any
instructional-design task, then open the matching `handoff_XX_*.md` file for the full grounding text,
scoring anchors, judge prompt, and output format.

GUIDE = **G**rounded **U**niversal **I**nstructional **D**esign **E**valuator. Ten archetypes,
60 dimensions (6 per archetype), each grounded in named learning-science sources and scored 1–5 with
behavioral anchors. Built on the LLM-as-a-judge pattern (Zheng et al., 2023) and on the grounded-design
premise that key design decisions should be traceable to evidence from research, theory, and documented
best practice (Hannafin, Hannafin, Land, & Oliver, 1997).

Archetypes 01-09 evaluate component quality across the ADDIE lifecycle. Archetype 10 (Curriculum Alignment)
is the synthesis archetype — it evaluates whether the components, taken together, cohere. A course can
score well on 02, 03, and 07 individually and still fail 10 if its objectives, instruction, and assessment
teach and test different cognitive levels or behaviors.

---

## Quality outcomes & the Three Alignments

GUIDE operationalizes the three alignments that produce high-quality instruction (Hirumi, 2025;
Hirumi, Ratliff, & de la Mora, 2021):

- **Effective** — alignment of instructional elements to **theory, research, and documented best practice**
  (Hannafin et al., 1997). The *grounded* in GUIDE's name. Every archetype is theory-grounded; archetypes
  04 and 09 lead with this lens.
- **Efficient** — alignment of **objectives ↔ instructional strategies (chunking, sequencing) ↔ learner
  assessments** (Tyler, 1949; Bloom, 1956; Dick, Carey & Carey, 2015). The internal coherence check.
  Archetypes 02, 03, and 07 carry the load here; a cross-archetype Internal Alignment Check is planned
  for v3.1.
- **Engaging** — alignment of instructional elements to **learners' personal and professional goals,
  interests, and motivations** (Keller, 1987, 2010 — ARCS). Captured at 07 L4 (Learner Needs), applied
  at 03 (Learning Domain Alignment), and surfaced in 01, 08, and 09.

Each archetype below is tagged with the alignment(s) it primarily produces evidence about.

---

## The 10 archetypes mapped to ADDIE and the Three Alignments

| # | Archetype | ADDIE phase | Primary alignment | Theorists | Reference file |
|---|-----------|-------------|-------------------|-----------|----------------|
| 7 | Needs Analysis & Front-End Design | **A**nalyze | Efficient (objectives) + Engaging (L4 ARCS) | Rossett, Kaufman, Gilbert, Van Tiem (HPT), McGoldrick & Tobey, Mager, Keller (ARCS) | `handoff_07_needs_analysis.md` |
| 3 | Instructional Sequencing & Events | **D**esign | Efficient (Obj↔Strategy) + Effective (theory) | Gagné, Reigeluth, van Merriënboer, Merrill, Dick & Carey, Keller (ARCS) | `handoff_03_instructional_sequencing.md` |
| 8 | Story & Narrative Design | **D**esign | Engaging (narrative/emotional) | Campbell, Vogler, Harmon (Story Circle), Snyder (Save the Cat!) | `handoff_08_story_design.md` |
| 9 | Cognitive Neuroscience & Brain-Based Instruction | **D**esign | Effective (theory) + Engaging (relevance) | Kandel, Sousa, Medina, Ausubel, Brown/Roediger/McDaniel, BSCS 5E | `handoff_09_cognitive_neuroscience.md` |
| 4 | Multimedia Content Design (Deep Mayer) | **D**evelop | Effective (Mayer/Sweller) | Mayer, Paivio, Sweller, Clark | `handoff_04_multimedia_design.md` |
| 5 | WCAG/POUR Technical Accessibility | **D**evelop | Cross-cutting (precondition for all three) | WCAG 2.1, CAST UDL, Section 508, Nielsen | `handoff_05_accessibility_technical.md` |
| 1 | Adult Learning Communication | **I**mplement | Engaging (problem-centered, personalized) | Knowles, Mezirow, Sweller, Ausubel, Mayer, WCAG | `handoff_01_adult_learning_communication.md` |
| 2 | Assessment Design Quality | **E**valuate | Efficient (Obj↔Assessment) | Bloom/Anderson & Krathwohl, Webb, Messick, Mager, Kubiszyn & Borich | `handoff_02_assessment_design.md` |
| 6 | Formative Evaluation Protocol Quality | **E**valuate | Cross-cutting (measures whether alignment was achieved) | Scriven, Kirkpatrick, Stufflebeam, Bordonaro, Dick & Carey, Nielsen | `handoff_06_formative_evaluation.md` |
| 10 | Curriculum Alignment (Synthesis) | **Cross-ADDIE** | **Efficient** (synthesis — Obj↔Strategy↔Assessment + vertical + discipline) | Tyler, Bloom/Anderson & Krathwohl, Webb (DoK), Mager, Dick & Carey, Wiggins & McTighe, Reigeluth, van Merriënboer, Hirumi | `handoff_10_curriculum_alignment.md` |

---

## What each archetype evaluates (artifact → archetype)

Use this to route. Match the artifact in front of you to the archetype whose object of evaluation it is.

- **A request for training, a problem statement, a learner/audience profile, a goal or objectives list, a performance-gap write-up** → **07 Needs Analysis**. (Ask first: is training even the right intervention?)
- **A lesson plan, course outline, module structure, syllabus, or learning path** → **03 Instructional Sequencing**.
- **A scenario, case study, branching scenario, role-play, or any narrative-driven lesson** → **08 Story Design**.
- **Any instruction you want judged against how the brain actually learns (memory, attention, emotion, 5E)** → **09 Cognitive Neuroscience**. This is the "deep design" lens; pairs well with 03.
- **An e-learning module, video, slide deck, animation, or interactive media** → **04 Multimedia Design**.
- **A web page, LMS shell, digital course material, or anything that must meet WCAG/UDL** → **05 Accessibility**.
- **A chatbot/RAG answer, help-desk reply, or any conversational response to a learning professional** → **01 Adult Learning Communication**.
- **A quiz, test, item bank, rubric, or test blueprint** → **02 Assessment Design**.
- **An evaluation plan, usability test, expert-review protocol, or pilot study design** → **06 Formative Evaluation**.
- **An end-to-end course (objectives + instruction + assessment together), a course map being audited for coherence, a Bloom-drift check between stated and tested behavior, or any curriculum review against discipline-level competencies / accreditation standards** → **10 Curriculum Alignment**. Run *in addition* to component archetypes when the question is "do these pieces hang together?" rather than "is this piece well-designed?"

**Multiple archetypes often apply.** A narrated e-learning scenario could be scored by 04 (multimedia),
08 (story), 05 (accessibility), and 09 (neuroscience). Pick the 1–3 most relevant rather than forcing all ten.
When in doubt, lead with the archetype that matches the artifact's primary purpose, then add lenses.

**When to add archetype 10.** Archetype 10 is the synthesis lens — it does not evaluate component quality
(other archetypes do that). Include it when the artifact contains objectives + instruction + assessment
together and the question is whether they cohere. Typical pairings: 07 + 03 + 02 + 10 for a full course
review; 02 + 10 to check Bloom-drift between stated objective and assessment item; 03 + 10 to check that
sequencing teaches what objectives state.

---

## The 60 dimensions at a glance

Each archetype scores six dimensions 1–5. Overall is normally the mean of the six (a few archetypes
weight specific dimensions — see the individual handoff doc).

**01 Adult Learning Communication** — Adult Learning Alignment · Cognitive Load Management · Instructional
Clarity & Signaling · Accuracy & Grounding · Accessibility & Inclusive Communication · Personalization &
Engagement. *(Overall weights Accuracy and Adult Learning Alignment most heavily.)*

**02 Assessment Design** — Bloom's Alignment · Objective Congruence · Item Construction Quality · Validity
Evidence · Reliability Considerations · Inclusivity & Fairness.

**03 Instructional Sequencing** — Gagné's Nine Events Coverage · Learning Domain Alignment · Sequencing Logic
· Scaffolding & Gradual Release · Practice & Feedback Integration · Transfer & Retention Design.

**04 Multimedia Design** — Multimedia Principle Compliance · Extraneous Load Reduction · Intrinsic Load
Management · Generative Processing Support · Interactivity & Learner Control · Visual Design & Information
Architecture.

**05 Accessibility (WCAG/POUR)** — Perceivable · Operable · Understandable · Robust · UDL Integration ·
Remediation Feasibility.

**06 Formative Evaluation** — Phase Coverage · Evaluator Selection · Data Collection Alignment · Revision
Decision Framework · Feasibility & Practicality · Usability Engineering Integration.

**07 Needs Analysis** — Performance Gap Identification · Cause Analysis · Needs Assessment Completeness ·
Goal & Objective Quality · Stakeholder Alignment · Intervention Appropriateness.

**08 Story Design** — Narrative Structure · Learning-Narrative Integration · Character & Situation Authenticity
· Emotional Engagement & Motivation · Decision Points & Branching Quality · Transfer & Generalizability.

**09 Cognitive Neuroscience** — 5E Model Alignment · Memory System Optimization · Attention Management ·
Emotional Engagement for Encoding · Synaptic Strengthening Factors · Theory-Practice Grounding.

**10 Curriculum Alignment** — Objective ↔ Strategy Coherence · Strategy ↔ Assessment Coherence · Objective ↔
Assessment Coherence · Coverage Completeness · Vertical Alignment · Discipline Alignment. *(Overall is
capped at 3.0 if Objective ↔ Assessment Coherence scores 1 or 2 — an assessment that measures fundamentally
different behaviors than its objectives state cannot be considered well-aligned regardless of other dimensions.)*

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

- **Mager-format objectives** (Behavior + Condition + Criterion; observable verbs, never "understand/know") — 02, 07.
- **Cognitive Load Theory** (Sweller: intrinsic / extraneous / germane) — 01, 04, 09.
- **Alignment** (objective → instruction → assessment; Dick & Carey) — 02, 03, 07.
- **Mayer's multimedia principles** (coherence, signaling, redundancy, contiguity, modality, personalization) — 01, 04.
- **Retrieval practice & spacing** (Brown/Roediger/McDaniel; "Make It Stick") — 03, 09.
- **Advance organizers / meaningful learning** (Ausubel) — 01, 03, 09.
- **UDL — multiple means of representation, action/expression, engagement** (CAST) — 05, plus accessibility threads in 01, 02, 04.
- **Transfer** (application in varied/authentic contexts) — 03, 08, 09.
- **Nielsen severity ratings** (cosmetic / minor / major / catastrophic) — used for severity flags in 01, 05, 06.
- **Is training even the answer?** (HPT cause analysis; Van Tiem) — the gatekeeper question in 07.
- **ARCS motivational design** (Keller: Attention, Relevance, Confidence, Satisfaction) — capture learner goals/interests/motivations at 07 L4 (Learner Needs), then design against them in 03 Learning Domain Alignment (especially Attitudes domain). Engagement = alignment between instruction and the learner's "why."
- **Three Alignments → Effective / Efficient / Engaging** (Hirumi, 2025; Hirumi, Ratliff, & de la Mora, 2021) — the top-level quality vocabulary GUIDE evaluates against. See *Quality outcomes & the Three Alignments* above.
- **Grounded design** (Hannafin, Hannafin, Land, & Oliver, 1997) — the meta-principle that key design decisions should be traceable to research, theory, and documented best practice. This is the *grounded* in GUIDE's name and the rationale for every archetype's grounding text and citations.
- **Anecdotal vs. scientific evidence** (Hirumi, 2025) — anecdotal evidence comes from observations and stakeholder experience; scientific evidence comes from systematic, peer-reviewed research. Both are usable, but confusing them produces bad design decisions. Surfaces in 01's *Accuracy & Grounding* and 07's *Performance Gap Identification* (which requires data, not anecdote).

---

## Source

GUIDE — Grounded Universal Instructional Design Evaluator (v3.1.0).
Repository: github.com/jermn007/GUIDE. Copyright 2026 Jeremy Terhune. Licensed under the Apache License, Version 2.0.
This index condenses the nine `handoff_*.md` files in this directory; those files are the authoritative source.
