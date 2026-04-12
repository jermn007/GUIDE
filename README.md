# GUIDE - Grounded Universal Instructional Design Evaluator

**Version 3.0.0** | Apache License 2.0

GUIDE is an LLM-as-a-judge evaluation framework that operationalizes peer-reviewed instructional design research into structured rubrics. It was developed as a capstone synthesis of the University of Central Florida Master of Arts in Instructional Systems program.

The framework evaluates instructional content across **9 archetypes** and **54 dimensions**, each grounded in named theoretical sources and scored on a 1-5 scale with concrete behavioral anchors.

## How It Works

GUIDE applies the LLM-as-a-judge pattern (Zheng et al., 2023) to instructional design evaluation. Each archetype is a standalone judge prompt that can be loaded into any LLM capable of following structured evaluation instructions. The judge reads instructional content, scores it against 6 theory-grounded dimensions, and returns a structured scorecard with rationale.

## The Nine Archetypes

Each archetype maps to a phase of the ADDIE instructional design lifecycle:

| Archetype | Focus | ADDIE Phase |
|-----------|-------|-------------|
| 01 - Adult Learning Communication | Knowles, Mezirow, Sweller, Ausubel | Implement |
| 02 - Assessment Design | Bloom, Webb, Messick | Evaluate |
| 03 - Instructional Sequencing | Gagne, Reigeluth, van Merrienboer | Design |
| 04 - Multimedia Design | Mayer, Paivio, Sweller | Develop |
| 05 - Accessibility & Technical | WCAG, CAST UDL, Section 508 | Develop |
| 06 - Formative Evaluation | Scriven, Kirkpatrick, Stufflebeam | Evaluate |
| 07 - Needs Analysis | Rossett, Kaufman, Gilbert | Analyze |
| 08 - Story Design | Campbell, Vogler, Harmon, Snyder | Design |
| 09 - Cognitive Neuroscience | Kandel, Sousa, Medina, Ausubel, Brown | Design |

## Repository Structure

```
GUIDE/
├── README.md                              # This file
├── NOTICE                                 # Copyright and attribution
├── GUIDE_Rubric_Document.docx             # Full rubric document (v3.0.0)
├── GUIDE_Self_Evaluation.md               # Self-evaluation baseline (v2.2.0)
├── GUIDE_Self_Evaluation_v3_Comparison.md # Before/after comparison (v2.2.0 -> v3.0.0)
├── guide_base.py                          # Base evaluator class
├── guide_registry.py                      # Archetype registry and runner
└── archetypes/
    ├── archetype_01_*.py through 09_*.py  # Judge prompt modules
    ├── handoff_01_*.md through 09_*.md    # Model-agnostic handoff docs
    └── edge_cases_01_*.json through 09    # Edge case test suites (58 total)
```

## Key Files

**GUIDE_Rubric_Document.docx** is the primary deliverable - a comprehensive rubric document containing all 9 archetypes, 54 dimensions, scoring criteria, a cross-archetype coverage matrix, calibration example, and glossary.

**Archetype Python modules** (`archetype_*.py`) are standalone judge prompts that can be loaded into any LLM. Each contains the full grounding text, scoring criteria, and evaluation instructions for its 6 dimensions.

**Handoff documents** (`handoff_*.md`) are model-agnostic implementation guides. They contain everything a practitioner needs to recreate each judge prompt in any LLM platform without depending on this codebase.

**Edge case files** (`edge_cases_*.json`) provide test scenarios for validating judge behavior at scoring boundaries.

## Theoretical Foundation

The framework draws on 20+ named sources across instructional design, cognitive science, and narrative theory. Key citations include:

- Knowles (1980) - Andragogy and self-directed learning
- Mezirow (1991) - Transformative learning and critical reflection
- Ausubel (2000) - Meaningful reception learning and advance organizers
- Bloom (1956) / Anderson & Krathwohl (2001) - Taxonomy of educational objectives
- Gagne (1985) - Conditions of learning and nine events of instruction
- Mayer (2009) - Cognitive theory of multimedia learning
- Sweller (1988) - Cognitive load theory
- Campbell (1949) / Snyder (2005) - Narrative structure frameworks
- Brown, Roediger & McDaniel (2014) - Retrieval practice and desirable difficulties
- Zheng et al. (2023) - LLM-as-a-judge methodology

## Self-Evaluation

The framework has been evaluated against its own rubrics ("eating our own cooking"). The v3.0.0 rubric document scores a composite **4.0/5.0** across the 6 applicable archetypes, up from 3.4/5.0 in v2.2.0. See `GUIDE_Self_Evaluation_v3_Comparison.md` for the full before/after analysis.

## License

Copyright 2026 Jeremy Terhune. Licensed under the Apache License, Version 2.0.
