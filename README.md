# GUIDE - Grounded Universal Instructional Design Evaluator

**Version 3.1.1** | Apache License 2.0

GUIDE is an LLM-as-a-judge evaluation framework that operationalizes peer-reviewed instructional design research into structured rubrics. It was developed as a capstone synthesis of my experience in the University of Central Florida Master of Arts in Instructional Systems program.

The framework evaluates instructional content across **10 archetypes** and **60 dimensions**, each grounded in named theoretical sources and scored on a 1-5 scale with concrete behavioral anchors.

## How It Works

GUIDE applies the LLM-as-a-judge pattern (Zheng et al., 2023) to instructional design evaluation. Each archetype is a standalone judge prompt that can be loaded into any LLM capable of following structured evaluation instructions. The judge reads instructional content, scores it against 6 theory-grounded dimensions, and returns a structured scorecard with rationale.

## Quality Outcomes: Effective, Efficient, Engaging

High-quality instruction is effective, efficient, and engaging (Merrill, 2024). Hirumi (2025), building on Hirumi, Ratliff & de la Mora (2021), maps each of those quality outcomes to an alignment of instructional elements. GUIDE operationalizes each:

- **Effective** - instructional elements aligned with **theory, research, and documented best practice** (Hannafin, Hannafin, Land, & Oliver, 1997). Whether the artifact reflects what learning science actually says works. This is the *grounded* in Grounded Universal Instructional Design Evaluator.
- **Efficient** - **objectives, instructional strategies (chunking and sequencing), and learner assessments aligned with each other** (Tyler, 1949; Bloom, 1956; Dick, Carey & Carey, 2015). Whether the artifact's internal pieces cohere so learners aren't doing wasted work.
- **Engaging** - instructional elements aligned with **learners' personal and professional goals, interests, and motivations** (Keller, 1987, 2010 - ARCS). Whether the artifact connects to who the learner is and what they're trying to become.

Each archetype below evaluates one or more of these alignments. The "Primary alignment" column tags the alignment(s) the archetype primarily produces evidence about.

## The Ten Archetypes

Each archetype maps to a phase of the ADDIE instructional design lifecycle:

| Archetype | Focus | ADDIE Phase | Primary alignment |
|-----------|-------|-------------|-------------------|
| Needs Analysis | Rossett, Kaufman, Gilbert, Keller (ARCS) | Analyze | Efficient (objectives) + Engaging (L4 ARCS) |
| Instructional Sequencing | Gagne, Reigeluth, van Merrienboer, Keller (ARCS) | Design | Efficient (Obj↔Strategy) + Effective (theory) |
| Story Design | Campbell, Vogler, Harmon, Snyder | Design | Engaging (narrative/emotional) |
| Cognitive Neuroscience | Kandel, Sousa, Medina, Ausubel, Brown | Design | Effective (theory) + Engaging (relevance) |
| Multimedia Design | Mayer, Paivio, Sweller | Develop | Effective (Mayer/Sweller) |
| Accessibility & Technical | WCAG, CAST UDL, Section 508 | Develop | Cross-cutting (precondition for all three) |
| Adult Learning Communication | Knowles, Mezirow, Sweller, Ausubel | Implement | Engaging (problem-centered, personalized) |
| Assessment Design | Bloom, Webb, Messick | Evaluate | Efficient (Obj↔Assessment) |
| Formative Evaluation | Scriven, Kirkpatrick, Stufflebeam | Evaluate | Cross-cutting (measures whether alignment was achieved) |
| Curriculum Alignment | Tyler, Bloom/Anderson & Krathwohl, Webb (DoK), Mager, Dick & Carey, Wiggins & McTighe, Reigeluth, Hirumi | Cross-ADDIE | **Efficient** (synthesis archetype - Obj↔Strategy↔Assessment + vertical + discipline) |

## Repository Structure

```
GUIDE/
├── README.md                              # This file
├── NOTICE                                 # Copyright and attribution
├── GUIDE_Rubric_Document.docx             # Full rubric document (v3.0.0 snapshot)
├── GUIDE_Self_Evaluation.md               # Self-evaluation baseline (v2.2.0)
├── GUIDE_Self_Evaluation_v3_Comparison.md # Before/after comparison (v2.2.0 -> v3.0.0)
├── guide_base.py                          # Base evaluator class
├── guide_registry.py                      # Archetype registry and runner
├── archetypes/
│   ├── archetype_XX_*.py                  # Judge prompt modules (one per archetype, 01-10)
│   ├── handoff_XX_*.md                    # Model-agnostic handoff docs (one per archetype)
│   └── edge_cases_XX.json                 # Edge case test suites (one per archetype)
└── skill/                                 # Claude skill + plugin packaging
    ├── README.md                          # install/usage for the skill and plugin
    ├── sync_skill_from_archetypes.py      # regenerates references from archetypes/
    ├── guide-instructional-design/        # canonical skill source
    └── guide-instructional-design-plugin/ # installable plugin (mirrors the skill)
```

## Claude Skill / Plugin

GUIDE is also packaged as a Claude skill and plugin under [`skill/`](skill/). Install via:

```
/plugin install ./skill/guide-instructional-design.plugin
```

…and the skill self-activates on instructional-design intents (course, training, lesson, quiz, rubric, e-learning, accessibility, needs analysis, etc.), running in either **design** or **evaluate** mode against the 10 archetypes. See [`skill/README.md`](skill/README.md) for build instructions, skill-only install, and the sync workflow that keeps the skill aligned with `archetypes/`.

## Key Files

**GUIDE_Rubric_Document.docx** is a static snapshot of the v3.0.0 rubric - a comprehensive document containing the original 9 archetypes, 54 dimensions, scoring criteria, a cross-archetype coverage matrix, calibration example, and glossary. The live framework is now v3.1.1 (10 archetypes, 60 dimensions) and lives in `archetypes/` and the skill; the docx will be regenerated on the next major release.

**Archetype Python modules** (`archetype_*.py`) are standalone judge prompts that can be loaded into any LLM. Each contains the full grounding text, scoring criteria, and evaluation instructions for its 6 dimensions.

**Handoff documents** (`handoff_*.md`) are model-agnostic implementation guides. They contain everything a practitioner needs to recreate each judge prompt in any LLM platform without depending on this codebase.

**Edge case files** (`edge_cases_*.json`) provide test scenarios for validating judge behavior at scoring boundaries.

## Theoretical Foundation

The framework draws on 20+ named sources across instructional design, cognitive science, and narrative theory. Key citations include:

- Tyler (1949) - Original alignment principle (objectives → instruction → assessment)
- Knowles (1980) - Andragogy and self-directed learning
- Mezirow (1991) - Transformative learning and critical reflection
- Ausubel (2000) - Meaningful reception learning and advance organizers
- Bloom (1956) / Anderson & Krathwohl (2001) - Taxonomy of educational objectives
- Gagne (1985) - Conditions of learning and nine events of instruction
- Mayer (2009) - Cognitive theory of multimedia learning
- Sweller (1988) - Cognitive load theory
- Campbell (1949) / Snyder (2005) - Narrative structure frameworks
- Hannafin, Hannafin, Land & Oliver (1997) - Grounded practice in instructional design (the *grounded* premise of GUIDE)
- Brown, Roediger & McDaniel (2014) - Retrieval practice and desirable difficulties
- Keller (1987, 2010) - ARCS motivational design (Attention, Relevance, Confidence, Satisfaction)
- Merrill (2024) - Effective, efficient, and engaging learning experiences as the criterion for high-quality instruction
- Hirumi, Ratliff & de la Mora (2021); Hirumi (2025) - Mapping the three quality outcomes to alignments of instructional elements (objectives ↔ strategies ↔ assessments; alignment to theory/research; alignment to personal/professional goals)
- Zheng et al. (2023) - LLM-as-a-judge methodology

## Self-Evaluation

The framework has been evaluated against its own rubrics. The v3.0.x rubric document scores a composite **4.0/5.0** across the 6 applicable archetypes, up from 3.4/5.0 in v2.2.0. See `GUIDE_Self_Evaluation_v3_Comparison.md` for the full before/after analysis.

## License

Copyright 2026 Jeremy Terhune. Licensed under the Apache License, Version 2.0.
