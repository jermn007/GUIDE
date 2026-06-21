---
name: guide-instructional-design
description: >-
  Design and evaluate instructional content using GUIDE, a learning-science framework of 9
  archetypes and 54 theory-grounded dimensions mapped to the ADDIE lifecycle. Use whenever work
  involves teaching, training, or learning: writing or reviewing a lesson plan, course, syllabus,
  or curriculum; building or critiquing a quiz, test, rubric, or assessment; creating or auditing
  an e-learning module, training video, or slide deck; designing scenario-based or branching
  learning; checking learning content for accessibility (WCAG/UDL); running a needs analysis or
  deciding whether training is even the right solution; planning a formative evaluation, usability
  test, or pilot; or grounding any of these in learning theory (Bloom, Gagné, Mayer, Knowles,
  Sweller, Mager, cognitive neuroscience). Trigger even when the user says course, training,
  lesson, module, learners, objectives, or instructional design without naming GUIDE. Use it both
  to CREATE instructional artifacts and to SCORE existing ones with rubrics.
---

# GUIDE: Instructional Design (Design & Evaluate)

GUIDE (Grounded Universal Instructional Design Evaluator) operationalizes peer-reviewed learning
science into nine **archetypes**, each scoring an instructional artifact on **six dimensions**
(54 total) using a 1–5 scale with concrete behavioral anchors. It was built as an LLM-as-a-judge
framework (Zheng et al., 2023), but the same rubrics are powerful **design guardrails**: the things
the judge looks for are exactly the things good instruction should do.

This skill uses GUIDE two ways:

- **Evaluate mode** — score an existing artifact, return a structured scorecard with rationale,
  severity flags, and improvement suggestions. This is GUIDE used as designed.
- **Design mode** — author new instructional content with the relevant archetype's dimensions held
  in mind as forward-looking design criteria, then self-check against them before delivering.

The rubrics live in `references/`. Treat them as the authoritative source — quote their grounding and
anchors rather than improvising. Each archetype is faithful to the GUIDE repository.

## How to use this skill

1. **Identify the artifact and the intent.** What instructional thing is in front of you (or being
   requested), and does the user want it *created/improved* (design mode) or *scored* (evaluate mode)?
   If genuinely ambiguous, ask once; otherwise infer from the verb ("write/build/design" → design;
   "review/score/audit/critique/is this good" → evaluate).

2. **Route to the right archetype(s).** Open `references/00_archetype_index.md` and match the artifact
   to its archetype using the "artifact → archetype" map. Usually 1–3 archetypes apply. Don't force
   all nine; lead with the one matching the artifact's primary purpose, then add lenses (e.g., a
   narrated e-learning scenario → 04 Multimedia + 08 Story + 05 Accessibility).

3. **Load the full rubric(s).** Read the matching `references/handoff_0X_*.md` file(s). Each contains
   the dimension definitions, the grounding text (the cited theory and *why* it matters), the 1–5
   scoring anchors, the judge system prompt, the JSON output format, severity flags, and improvement
   suggestions. Use these verbatim — don't paraphrase the anchors loosely.

4. **Do the work** in the relevant mode (see below).

5. **Verify before delivering.** In evaluate mode, sanity-check that each score is defensible against
   the anchor and that the overall reflects the parts. In design mode, run a quick self-evaluation pass
   against the dimensions and fix anything that would score below 4.

## The nine archetypes (ADDIE order)

| Archetype | Use it for | ADDIE |
|-----------|-----------|-------|
| 07 Needs Analysis | training requests, performance gaps, goals/objectives, learner analysis | Analyze |
| 03 Instructional Sequencing | lesson plans, course outlines, modules, learning paths | Design |
| 08 Story Design | scenarios, case studies, branching/role-play, narrative lessons | Design |
| 09 Cognitive Neuroscience | brain-based design: memory, attention, emotion, 5E | Design |
| 04 Multimedia Design | e-learning, video, slides, interactive media | Develop |
| 05 Accessibility (WCAG/POUR) | web/LMS content, digital materials, UDL compliance | Develop |
| 01 Adult Learning Communication | chatbot/RAG/help answers to learning professionals | Implement |
| 02 Assessment Design | quizzes, tests, item banks, rubrics, blueprints | Evaluate |
| 06 Formative Evaluation | eval plans, usability tests, expert reviews, pilots | Evaluate |

Full theorist lists, the 54 dimensions, and routing detail are in `references/00_archetype_index.md`.

## Evaluate mode

Goal: a defensible, theory-grounded scorecard the user can act on.

1. Read the relevant `handoff_0X_*.md` rubric(s) in full.
2. For each of the six dimensions, find concrete evidence in the artifact and assign 1–5 strictly
   against that dimension's anchor. Cite the evidence ("the third slide narrates and duplicates the
   same text on-screen" → Extraneous Load Reduction = 2 for a redundancy violation). Be willing to give
   low scores; a rubric that never discriminates is useless.
3. Compute the **overall** (mean of the six, unless the archetype specifies weighting — e.g., 01 weights
   Accuracy and Adult Learning Alignment most heavily).
4. Raise **severity flags** for any critical issue the archetype lists (hallucination, no assessment,
   inaccessible to screen readers, training recommended for an environmental problem, etc.). Use Nielsen
   severity framing (cosmetic / minor / major / catastrophic) where the archetype uses it.
5. Give **improvement suggestions** — 1–3 concrete, actionable next steps for any dimension under 4,
   drawn from the archetype's improvement-suggestions section.
6. Map the overall to the threshold band (4.5+ ship · 3.5–4.4 light revision · 2.5–3.4 revise · <2.5
   redesign) and state the verdict plainly.

**Output format.** Default to the scorecard the user can actually use: a per-dimension table (score +
one- or two-sentence rationale each), the overall + verdict, severity flags, and improvement
suggestions. If the user wants machine-readable output or is wiring this into a pipeline, return the
exact JSON object from the archetype's "Output Format" section instead. If multiple archetypes apply,
produce one scorecard per archetype and a short combined verdict.

When scoring is hard:
- **No source/context for accuracy?** Score Accuracy & Grounding conservatively and say why.
- **Linear artifact under a branching dimension?** Score the embedded decision-making instead (see 08).
- **Two dimensions feel similar?** The handoff doc's troubleshooting table usually explains the distinction
  (e.g., 01: Adult Learning = *who the response assumes the user is*; Personalization = *tone/engagement*).

## Design mode

Goal: produce instructional content that would already score 4–5 on the relevant archetype, because the
dimensions were design inputs, not an afterthought.

1. **Start with analysis (07) unless it's clearly done.** Before designing training, confirm there's a
   real, ideally data-based performance gap and that the cause is a skill/knowledge/attitude gap (training
   helps) rather than an environmental one (tools, incentives, process — training won't fix it). Write
   objectives in Mager format (Behavior + Condition + Criterion; observable verbs). Skipping this is the
   most common and most expensive instructional-design mistake.
2. **Pick the design archetype(s)** for the artifact (03 sequencing, 08 story, 09 neuroscience, 04
   multimedia, 05 accessibility) and read the rubric(s).
3. **Author against the dimensions.** Use them as a checklist of what to include. Examples: cover Gagné's
   nine events (03); keep extraneous load down and segment content (04); embed the learning in the
   narrative tension rather than bolting a lesson on (08); sequence Explore before Explain and build in
   spaced retrieval (09); provide alt text, captions, keyboard access, and multiple representations (05).
4. **Keep alignment tight.** Objectives → instruction → practice → assessment should trace to each other
   (Dick & Carey). If you're also producing assessments, apply 02 (Bloom level matches the objective;
   plausible distractors; coverage).
5. **Self-evaluate before delivering.** Run a quick evaluate-mode pass on your own draft against the same
   archetype. Name any dimension that would score below 4 and fix it. Optionally show the user a short
   "GUIDE self-check" table so the grounding is visible.

Explain the *why* from the grounding when it helps the user (e.g., "segmented into ~15-minute chunks
because sustained attention degrades after 15–20 minutes — Posner & Rothbart"). The point of GUIDE is
that good instruction is defensible, not merely tasteful.

## Producing deliverables

If the output is a document, deck, spreadsheet, or PDF (a course outline as a Word doc, a storyboard
deck, an item bank as a spreadsheet, an evaluation report), first do the GUIDE design/evaluation work
here, then read the matching output-format skill (`docx`, `pptx`, `xlsx`, `pdf`) and build the file from
the GUIDE-grounded content. GUIDE supplies the substance; those skills supply the format.

## Reference files

- `references/00_archetype_index.md` — router: artifact→archetype map, ADDIE table, all 54 dimensions,
  shared 1–5 scale, thresholds, and recurring cross-archetype concepts. **Read this first** to choose
  archetypes.
- `references/handoff_01_adult_learning_communication.md` — conversational/RAG answers to learners.
- `references/handoff_02_assessment_design.md` — quizzes, tests, rubrics, blueprints.
- `references/handoff_03_instructional_sequencing.md` — lesson plans, courses, modules, Gagné's events.
- `references/handoff_04_multimedia_design.md` — e-learning, video, slides (deep Mayer / cognitive load).
- `references/handoff_05_accessibility_technical.md` — WCAG 2.1 / POUR / UDL for digital learning content.
- `references/handoff_06_formative_evaluation.md` — evaluation plans, usability tests, pilots.
- `references/handoff_07_needs_analysis.md` — needs assessment, performance gaps, HPT, Mager objectives.
- `references/handoff_08_story_design.md` — scenario/narrative/branching instruction.
- `references/handoff_09_cognitive_neuroscience.md` — brain-based design (memory, attention, emotion, 5E).

Each handoff doc is long; it opens with Purpose and the dimension table, so you can skim to the dimension
you need. Read the whole doc for the archetype you're actively using.

## Attribution

GUIDE — Grounded Universal Instructional Design Evaluator (v3.2.0).
Repository: github.com/jermn007/GUIDE. Copyright 2026 Jeremy Terhune. Licensed under the Apache License,
Version 2.0. The bundled `references/handoff_*.md` files are the project's model-agnostic handoff
documents, reproduced for use inside this skill; see `references/NOTICE.md`. Keep this attribution intact.
