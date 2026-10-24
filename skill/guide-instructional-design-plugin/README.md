# GUIDE: Instructional Design

GUIDE (Grounded Universal Instructional Design Evaluator) scores instructional content against published learning-science research. Use it to **evaluate** a lesson plan, quiz, e-learning module, or needs analysis you already have, or to **design** a new one that meets the same criteria from the start. You ask in plain language and get back a scorecard with reasons and next steps.

GUIDE has 10 archetypes. Each one is a full rubric for one kind of instructional work, and each scores six dimensions on a 1 to 5 scale, for 60 dimensions in all. The archetypes map to the ADDIE lifecycle:

| # | Archetype | Use it for | ADDIE phase |
|---|-----------|-----------|-------------|
| 07 | Needs Analysis | training requests, performance gaps, objectives | Analyze |
| 03 | Instructional Sequencing | lesson plans, course outlines, learning paths | Design |
| 08 | Story Design | scenarios, case studies, branching, role-play | Design |
| 09 | Cognitive Neuroscience | memory, attention, emotion, the 5E model | Design |
| 04 | Multimedia Design | e-learning, video, slides, interactive media | Develop |
| 05 | Accessibility | web and LMS content, digital materials (WCAG, UDL) | Develop |
| 01 | Adult Learning Communication | chatbot and help answers for learning professionals | Implement |
| 02 | Assessment Design | quizzes, tests, item banks, rubrics | Evaluate |
| 06 | Formative Evaluation | evaluation plans, usability tests, pilots | Evaluate |
| 10 | Curriculum Alignment | do objectives, instruction, and assessment agree? | Across all phases |

Archetype 10 checks that the pieces fit together, so a course can score well on every other archetype and still fail it.

## How to use it

You don't need a special command. GUIDE turns on when you talk about courses, lessons, quizzes, training, or learners. Paste a draft and ask for a review:

```text
Review this quiz item with GUIDE.

Objective: Given a customer complaint, the agent will choose the
de-escalation response that follows the company's LEAP model.

Item: What does the "A" in LEAP stand for?
  a) Acknowledge   b) Apologize   c) Assist   d) Assess
```

GUIDE returns a 1 to 5 score on each dimension with the evidence behind it, an overall verdict (ship, light revision, revise, or redesign), flags for serious problems, and one to three concrete fixes. Here it catches that the objective asks learners to *apply* a model, but the item only asks them to *recall* it.

To design instead, ask for what you want built: *"Write a three-item scenario quiz for that objective, using GUIDE."*

## What's included

- **The GUIDE skill:** the rubrics and scoring guidance. It works in Claude chat, Cowork, and Claude Code.
- **13 agents:** a router, 10 archetype specialists, a curriculum-alignment gate, a synthesizer, and a reviser that together run a full ADDIE design or audit. Agents run in Cowork and Claude Code. Claude chat uses the skill only.

## What this plugin runs and sends

Nothing. The plugin contains only Markdown and JSON files. It has no hooks, scripts, MCP servers, or executable code, and it does not fetch or send data anywhere.

## About

GUIDE is built and maintained by Jeremy Terhune. It started as the capstone synthesis for the University of Central Florida Master of Arts in Instructional Systems program.

## Source, license, and citation

GUIDE is open source under the Apache License 2.0. The full framework, a Python API for running the judges outside Claude, the research sources behind each dimension, and the changelog are at [github.com/jermn007/GUIDE](https://github.com/jermn007/GUIDE). To report a problem, open an issue there.

To cite GUIDE, use the concept DOI [10.5281/zenodo.22949871](https://doi.org/10.5281/zenodo.22949871).
