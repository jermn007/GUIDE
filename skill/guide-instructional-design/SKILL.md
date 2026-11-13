---
name: guide-instructional-design
description: >-
  Design and evaluate instructional content using GUIDE, a learning-science framework of 10
  archetypes and 60 theory-grounded dimensions mapped to the ADDIE lifecycle. Use whenever work
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
science into ten **archetypes**, each scoring an instructional artifact on **six dimensions**
(60 total) using a 1-5 scale with concrete behavioral **anchors**. The same rubrics work in two
directions: the things a judge looks for are exactly the things good instruction should do.

- **Evaluate mode**: score an existing artifact and return a scorecard with evidence, severity
  flags, and fixes.
- **Design mode**: author new instructional content with the archetype's dimensions as design
  inputs, then self-check against them before delivering.

The rubrics in `references/` are the authoritative source. Quote their grounding and anchors
rather than improvising.

## How to use this skill

1. **Pick the mode.** "Write / build / design / improve" means design mode; "review / score /
   audit / critique / is this good" means evaluate mode. Ask once only if the request is
   genuinely ambiguous.
2. **Route to the archetype(s).** Read `references/00_archetype_index.md` and match the artifact
   to its archetype(s) with the artifact-to-archetype map. Usually 1-3 apply: lead with the one
   matching the artifact's primary purpose, then add lenses (a narrated e-learning scenario is
   04 Multimedia + 08 Story + 05 Accessibility). Archetype **10 Curriculum Alignment** is the
   synthesis gate: run it last, once objectives, instruction, and assessment exist together.
3. **Read the rubric(s).** Read each matching `references/handoff_NN_*.md` in full. Every handoff
   has its purpose and design targets, the six dimensions with scoring anchors, and an Output
   JSON section; most add severity or red flags, improvement suggestions, and troubleshooting
   or scenario notes.
4. **Run the mode.** Read `EVALUATE.md` for evaluate mode or `DESIGN.md` for design mode, and
   follow it through to its "Done when" checklist.

The ten archetypes, in ADDIE order: 07 Needs Analysis (Analyze); 03 Instructional Sequencing,
08 Story Design, 09 Cognitive Neuroscience (Design); 04 Multimedia Design, 05 Accessibility
(Develop); 01 Adult Learning Communication (Implement); 02 Assessment Design, 06 Formative
Evaluation (Evaluate); 10 Curriculum Alignment (across all phases).

## Producing deliverables

When the output is a document, deck, spreadsheet, or PDF (a course outline as a Word doc, a
storyboard deck, an item bank as a spreadsheet, an evaluation report), do the GUIDE work first,
then load the matching output-format skill (`docx`, `pptx`, `xlsx`, `pdf`; through the Skill tool
where one is available) and build the file from the GUIDE-grounded content. GUIDE supplies the
substance; those skills supply the format.

## Reference files

- `EVALUATE.md`: the evaluate-mode procedure and scorecard format.
- `DESIGN.md`: the design-mode procedure, starting from needs analysis.
- `references/00_archetype_index.md`: router (artifact-to-archetype map, ADDIE table, all 60
  dimensions, the shared 1-5 scale, verdict thresholds, recurring cross-archetype concepts).
  **Read this first** to choose archetypes.
- `references/handoff_01_adult_learning_communication.md`: conversational/RAG answers to learners.
- `references/handoff_02_assessment_design.md`: quizzes, tests, rubrics, blueprints.
- `references/handoff_03_instructional_sequencing.md`: lesson plans, courses, modules, Gagné's events.
- `references/handoff_04_multimedia_design.md`: e-learning, video, slides (deep Mayer / cognitive load).
- `references/handoff_05_accessibility_technical.md`: WCAG 2.1 / POUR / UDL for digital learning content.
- `references/handoff_06_formative_evaluation.md`: evaluation plans, usability tests, pilots.
- `references/handoff_07_needs_analysis.md`: needs assessment, performance gaps, HPT, Mager objectives.
- `references/handoff_08_story_design.md`: scenario/narrative/branching instruction.
- `references/handoff_09_cognitive_neuroscience.md`: brain-based design (memory, attention, emotion, 5E).
- `references/handoff_10_curriculum_alignment.md`: synthesis gate, objective-strategy-assessment coherence.
- `references/discipline_alignment_crosswalk.md`: how each archetype maps to IBSTPI / ATD / ISPI-HPT
  professional standards (the Discipline Alignment reference model).

The handoffs here are the **skill edition**: the Python judge prompts and harness notes are
omitted. The full model-agnostic handoffs, for use with other models and the Python API, live in
the GUIDE repository's `archetypes/` folder.

## Attribution

GUIDE - Grounded Universal Instructional Design Evaluator (v3.5.0).
Repository: github.com/jermn007/GUIDE. Copyright 2026 Jeremy Terhune. Licensed under the Apache License,
Version 2.0. The bundled `references/handoff_*.md` files are generated from the project's model-agnostic
handoff documents for use inside this skill; see `references/NOTICE.md`. Keep this attribution intact.
