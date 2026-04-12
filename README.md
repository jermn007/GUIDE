# GUIDE - Grounded Universal Instructional Design Evaluator

A modular LLM-as-a-judge evaluation framework for assessing AI assistants and instructional artifacts, grounded in peer-reviewed learning science.

## What is GUIDE?

GUIDE provides **54 evaluation dimensions** organized across **9 archetypes**, each targeting a distinct instructional design domain. Every dimension is scored on a 1-5 scale with explicit criteria anchored to named research. The framework is designed for use in automated evaluation pipelines (LLM-as-a-judge) but the rubrics are useful for human evaluation as well.

Developed as a capstone synthesis of my experience in the University of Central Florida's MA in Instructional Systems and Technology program, GUIDE translates foundational ID research - Knowles, Mayer, Sweller, Gagne, Dick & Carey, Bloom, Vygotsky, Campbell, and others - into structured, repeatable evaluation rubrics.

## Archetypes

| # | Archetype | What It Evaluates |
|---|-----------|-------------------|
| 01 | Adult Learning Communication | AI responses to adult professionals - tone, cognitive load, accuracy, accessibility |
| 02 | Assessment Design | Quizzes, tests, rubrics - Bloom's alignment, item quality, validity, fairness |
| 03 | Instructional Sequencing | Lesson plans, course outlines - Gagne's events, scaffolding, transfer design |
| 04 | Multimedia Design | E-learning modules, videos - Mayer's principles, cognitive load, interactivity |
| 05 | WCAG Accessibility | Web-based learning content - WCAG 2.1 POUR compliance, UDL integration |
| 06 | Formative Evaluation | Evaluation plans - phase coverage, data collection, decision frameworks |
| 07 | Needs Analysis | Needs assessments - performance gaps, cause analysis, HPT intervention matching |
| 08 | Story Design | Narrative instruction - story structure, authenticity, branching, transfer |
| 09 | Cognitive Neuroscience | Brain-aligned instruction - 5E model, memory systems, attention, encoding |

## Repository Structure

```
GUIDE/
├── guide_base.py              # Shared infrastructure (GUIDEResult, evaluator factory, composite eval)
├── guide_registry.py          # Entry point and convenience functions
├── archetypes/
│   ├── __init__.py            # Auto-imports all archetypes on load
│   ├── archetype_01_*.py      # Judge prompts for each archetype (01-09)
│   ├── ...
│   ├── handoff_01_*.md        # Implementation handoff docs for each archetype
│   ├── ...
│   ├── edge_cases_01.json     # Edge case test sets for each archetype
│   └── ...
├── GUIDE_Rubric_Document.docx # Complete rubric with all 54 dimensions, citations, and scoring tables
├── LICENSE                    # Apache 2.0
└── README.md
```

## Usage

### Quick Start

```python
from guide_registry import evaluate, evaluate_composite, evaluate_all

# Evaluate a single response against one archetype
result = evaluate(
    archetype="adult_learning_communication",
    user_input="How do I set up spaced retrieval in my LMS?",
    assistant_output="Here's how to configure spaced retrieval...",
    context="LMS admin documentation"
)
print(result.score, result.explanation)

# Run multiple archetypes against the same input
composite = evaluate_composite(
    archetypes=["adult_learning_communication", "multimedia_design"],
    user_input="...",
    assistant_output="...",
    context="..."
)
for name, result in composite.results.items():
    print(f"{name}: {result.score}/5")

# Run all 9 archetypes
full = evaluate_all(user_input="...", assistant_output="...", context="...")
```

### LangChain/LangSmith Integration

```python
from guide_base import make_evaluator, run_langsmith_eval

# Create a LangSmith-compatible evaluator
evaluator = make_evaluator("assessment_design")

# Run against a LangSmith dataset
run_langsmith_eval(
    archetype="assessment_design",
    dataset_name="my-assessment-dataset",
    predict_fn=my_chain.invoke
)
```

### Standalone (No LangChain)

```python
from guide_base import evaluate_standalone

result = evaluate_standalone(
    archetype="instructional_sequencing",
    user_input="Review my lesson plan...",
    assistant_output="Your lesson plan covers...",
    context="Lesson plan document text"
)
```

## Dependencies

The judge prompts and rubrics are **model-agnostic** - they work with any LLM capable of following structured evaluation instructions.

The Python implementation supports three modes:

- **LangChain mode:** `pip install langchain-anthropic langchain-core`
- **Standalone mode:** `pip install anthropic`
- **LangSmith mode:** `pip install langsmith langchain-anthropic`

## Theoretical Foundations

Each archetype's dimensions are grounded in named, peer-reviewed research. Key sources include:

- **Knowles, M.S.** (1978, 2015) - Andragogy and adult learning theory
- **Mayer, R.E.** (2009, 2014) - Cognitive Theory of Multimedia Learning
- **Sweller, J.** (1988) - Cognitive Load Theory
- **Dick, W., Carey, L., & Carey, J.O.** (2015) - Systematic Design of Instruction
- **Anderson, L.W. & Krathwohl, D.R.** (2001) - Revised Bloom's Taxonomy
- **Gagne, R.M. et al.** (2005) - Principles of Instructional Design
- **Vygotsky, L.S.** (1978) - Zone of Proximal Development
- **Campbell, J.** (1949) - The Hero's Journey / narrative structure
- **BSCS** (2006) - 5E Instructional Model
- **W3C WAI** (2018) - WCAG 2.1 / POUR principles
- **Van Tiem, D. et al.** (2000) - Human Performance Technology
- **Nielsen, J.** (1994) - Severity ratings and usability heuristics
- **Zheng, L. et al.** (2023) - Judging LLM-as-a-Judge with MT-Bench (NeurIPS 2023)

Complete citations with page-level references are available in `GUIDE_Rubric_Document.docx`.

## The Rubric Document

`GUIDE_Rubric_Document.docx` is the comprehensive reference containing all 54 dimensions with their theoretical foundations, source materials, and 1-5 scoring criteria tables. It also includes:

- A quick-reference table mapping all archetypes to their dimensions
- A glossary of key terms
- "When to use this archetype" guidance for each archetype
- A cross-archetype coverage matrix showing which theories appear where
- An implementation guide with usage modes and dependencies
- A full references section with 35+ entries

## Edge Cases

Each archetype includes a JSON file of edge case test inputs designed to exercise specific failure modes. These are useful for regression testing as AI assistants evolve. Edge cases cover scenarios like:

- Responses that sound confident but contain hallucinated information
- Technically correct content that overwhelms with cognitive load
- Assessment items that test at the wrong Bloom's level
- Multimedia designs that violate Mayer's principles in subtle ways
- Narratives that use story as decoration rather than as the learning vehicle

## Author

**Jeremy Terhune**
University of Central Florida, MA in Instructional Systems
[GitHub](https://github.com/jermn007)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this framework. Attribution is required.
