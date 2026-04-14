# Archetype 2: Assessment Design Quality
## Handoff Documentation

**Purpose**: Evaluate quiz items, test blueprints, rubrics, and other assessment instruments for pedagogical soundness and measurement validity.

**Use Cases**:
- Peer review of quiz items before deployment
- Validation of unit tests against learning objectives
- Rubric quality assurance
- Assessment blueprint gap analysis
- Item bank audits

---

## Evaluation Dimensions

| Dimension | Scale | Definition | Key Criteria |
|-----------|-------|------------|--------------|
| **Bloom's Alignment** | 1-5 | Are items at the appropriate cognitive level? | Anderson et al. (2001) Revised Taxonomy: Remember → Understand → Apply → Analyze → Evaluate → Create; Knowledge types: Factual, Conceptual, Procedural, Metacognitive |
| **Objective Congruence** | 1-5 | Do items match stated learning objectives? | Mager (1997): behavior + condition + criterion; Dick/Carey (2015) alignment methodology |
| **Item Construction Quality** | 1-5 | Are stems clear, distractors plausible, items unambiguous? | Kubiszyn & Borich (2013) standards: clear stems, homogeneous distractors, single correct answer, no trick questions |
| **Validity Evidence** | 1-5 | Does the assessment show content validity through domain sampling? | Test blueprint existence and adherence; coverage of full domain or key objectives |
| **Reliability Considerations** | 1-5 | Are there enough items, appropriate difficulty, consistent scoring? | Item count (15+ norm-ref., 10-15 criterion-ref.); difficulty spread; clear rubric descriptors |
| **Inclusivity & Fairness** | 1-5 | Are items free from bias, accessible, using inclusive language? | No stereotypes, cultural bias, ableist language, gendered pronouns; accessible for diverse learners |

---

## Scoring Guide

### Bloom's Alignment
- **5**: Mix of cognitive levels aligned to objectives; strong evidence of Analyze/Evaluate/Create items
- **4**: Mostly Understand/Apply with some higher-order thinking
- **3**: Mix of Remember/Understand and Apply; minimal Analyze/Evaluate/Create
- **2**: Primarily Remember/Understand with some Apply
- **1**: All or nearly all items at Remember level (pure recall)

### Objective Congruence
- **5**: Clear, measurable Mager-style objectives; every item maps to a specific objective
- **4**: Well-defined objectives; most items align; 1-2 items tangential
- **3**: Objectives present but somewhat vague; ~70% item alignment
- **2**: Vague objectives; significant alignment gaps
- **1**: Missing or unclear objectives; items don't test stated learning targets

### Item Construction Quality
- **5**: Clear stems; plausible, homogeneous distractors; no ambiguity or trick wording
- **4**: Generally clear; minor stem revision needed; distractors adequate
- **3**: Some stems could be clearer; acceptable distractors; minor ambiguity
- **2**: Confusing stems; weak distractors; one or two trick questions
- **1**: Unclear stems; implausible distractors; pervasive ambiguity

### Validity Evidence
- **5**: Clear test blueprint; balanced coverage of domain; items represent key content
- **4**: Blueprint exists; minor coverage gaps
- **3**: Some blueprint or coverage evidence; skewed toward certain topics
- **2**: Minimal blueprint; gaps in coverage
- **1**: No blueprint; narrow coverage; misses critical content areas

### Reliability Considerations
- **5**: Sufficient items (15+ norm-ref., 10-15 criterion-ref.); varied difficulty; clear scoring rules
- **4**: Adequate items; mostly appropriate difficulty; good rubric clarity
- **3**: Minimal but acceptable item count; uneven difficulty; adequate scoring guidance
- **2**: Too few items or skewed difficulty; vague scoring
- **1**: Insufficient items; all same difficulty; no scoring consistency rules

### Inclusivity & Fairness
- **5**: Accessible language; no bias; considers diverse learners (ELL, neurodivergent, disabilities)
- **4**: Mostly neutral; one item could be more inclusive
- **3**: Generally acceptable; 2-3 items with mild bias or accessibility concerns
- **2**: Several items with cultural bias or inaccessible language
- **1**: Pervasive bias, stereotypes, ableist language, or cultural insensitivity

---

## System Prompt (Judge Rubric)

```
You are an expert instructional design evaluator specializing in assessment design quality.

You assess quiz items, test blueprints, rubrics, and other assessment instruments using six dimensions:

1. **Bloom's Alignment (1-5)**: Are assessment items at the appropriate cognitive level?
   - Use Anderson et al. (2001) Revised Bloom's: Remember → Understand → Apply → Analyze → Evaluate → Create
   - Consider knowledge types: Factual, Conceptual, Procedural, Metacognitive
   - Score 5: Mix of appropriate levels aligned to objectives; evidence of higher-order thinking
   - Score 3: Mostly remember/understand; some apply; minimal analyze/evaluate/create
   - Score 1: All items at recall/factual level; no cognitive depth

2. **Objective Congruence (1-5)**: Do items match stated learning objectives?
   - Apply Mager (1997): objectives should include behavior + condition + criterion
   - Use Dick/Carey (2015) alignment methodology: objective → item → assessment evidence
   - Score 5: Clear, measurable objectives; every item maps directly to an objective
   - Score 3: Objectives present but vague; some items don't align
   - Score 1: No clear objectives or items don't test stated objectives

3. **Item Construction Quality (1-5)**: Are stems clear, distractors plausible, items unambiguous?
   - Kubiszyn & Borich (2013) standards: stem clarity, homogeneous distractors, single correct answer
   - Look for: double negatives, ambiguous wording, trick questions, obviously wrong options
   - Score 5: Clear stems, plausible distractors, no ambiguity or trick wording
   - Score 3: Mostly clear; 1-2 stems could be better; distractors adequate
   - Score 1: Confusing stems, implausible distractors, ambiguous items

4. **Validity Evidence (1-5)**: Does the assessment show content validity through domain sampling?
   - Criterion-referenced assessment: does a test blueprint exist and is it followed?
   - Does coverage represent the full domain or key objectives?
   - Score 5: Clear blueprint; balanced coverage of domain; items represent key content
   - Score 3: Some blueprint or coverage gaps; skewed toward certain topics
   - Score 1: No blueprint; narrow coverage; misses critical content

5. **Reliability Considerations (1-5)**: Are there enough items, appropriate difficulty, consistent scoring?
   - Split-half, internal consistency principles; inter-rater reliability for rubrics
   - Minimum: ~15 items for norm-referenced; ~10-15 for criterion-referenced
   - Difficulty spread: avoid all easy or all hard
   - Rubrics: clear descriptors, consistent criteria
   - Score 5: Sufficient items, varied difficulty, clear scoring rubric or consistency rules
   - Score 3: Minimal items or uneven difficulty; adequate scoring guidance
   - Score 1: Too few items; all same difficulty; vague scoring criteria

6. **Inclusivity & Fairness (1-5)**: Are items free from bias, accessible, using inclusive language?
   - No stereotypes, cultural bias, ableist language, gendered pronouns
   - Consider diverse learners (ELL, neurodivergent, disabilities)
   - Score 5: Accessible language, no bias, considers diverse learners
   - Score 3: Mostly neutral; 1-2 items could be more inclusive
   - Score 1: Biased language, culturally insensitive, inaccessible

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
```

---

## Human Prompt Template

```
Evaluate the following assessment artifact.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object in this format:
{
  "scores": {
    "blooms_alignment": <1-5>,
    "objective_congruence": <1-5>,
    "item_construction_quality": <1-5>,
    "validity_evidence": <1-5>,
    "reliability_considerations": <1-5>,
    "inclusivity_fairness": <1-5>,
    "overall": <mean of all 6>
  },
  "rationale": {
    "blooms_alignment": "<brief explanation>",
    "objective_congruence": "<brief explanation>",
    "item_construction_quality": "<brief explanation>",
    "validity_evidence": "<brief explanation>",
    "reliability_considerations": "<brief explanation>",
    "inclusivity_fairness": "<brief explanation>"
  },
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}
```

---

## Severity Flags (Red Flags)

Look for and flag critical issues:

1. **Assessment-Objective Misalignment**: Items don't match learning objectives
2. **Missing Bloom's Higher Order**: All items at Remember/Understand (if objectives call for Apply+)
3. **Ambiguous Correct Answers**: More than one defensible correct answer
4. **Biased or Offensive Content**: Stereotypes, cultural insensitivity, ableist language
5. **Insufficient Item Count**: Fewer than 10 items for criterion-referenced; fewer than 15 for norm-referenced
6. **No Scoring Rubric**: Subjective assessment with no clear scoring criteria
7. **Coverage Gaps**: Test blueprint shows critical content not assessed

---

## Improvement Suggestions

When scoring < 4 on any dimension, recommend specific next steps:

1. **Bloom's Alignment**: Rewrite X items to target [Analyze/Evaluate/Create]; map remaining items to cognitive taxonomy
2. **Objective Congruence**: Clarify learning objectives using Mager format (behavior, condition, criterion); remove items not aligned
3. **Item Construction**: Revise stems (eliminate double negatives, clarify wording); ensure distractors are plausible and homogeneous
4. **Validity Evidence**: Develop a test blueprint; audit item coverage against domain; rebalance if skewed
5. **Reliability**: Add items to reach minimum count; adjust difficulty for variety; create/refine scoring rubric
6. **Inclusivity**: Review for bias (gender, culture, ability); test with diverse learner groups; use plain, accessible language

---

## Input Format

The archetype expects:

- **Input**: Learning objective(s) or assessment context (e.g., "Quiz for Unit 3: Photosynthesis; students have completed readings")
- **Output**: Quiz items, test blueprint, rubric, or other assessment artifact (ideally formatted with clear item numbers, correct answers, and rubric descriptors)
- **Context** (optional): Domain, learner population, instructional level (e.g., "High school biology, diverse learners including ELL students")
- **Reference** (optional): A "gold standard" rubric, exemplary quiz, or benchmark assessment for comparison

Example:
```
INPUT: "Create a 10-item multiple-choice quiz for Learning Objective: 'Students will analyze photosynthetic processes at the molecular level.'"

OUTPUT:
1. Which of the following best describes the primary function of the Calvin cycle?
   a) Energy production
   b) Carbon fixation and sugar synthesis ← CORRECT
   c) Chlorophyll absorption
   d) Oxygen diffusion

[Items 2-10 follow...]

RUBRIC:
- Item clarity: Stem unambiguous, correct answer defensible
- Distractors: Plausible, derived from common misconceptions
- Bloom's level: Items 1-4 Understand/Apply; Items 5-7 Analyze; Items 8-10 Evaluate
```

---

---

## Calibration & Validation

Before deploying at scale:

1. **Calibrate the Rubric**: Run 5-10 diverse assessment samples through your chosen model. Compare results to your expert judgment. Adjust dimension wording if score distributions are skewed.
2. **Test Edge Cases**: Validate against the 6 edge cases in `edge_cases_02.json`. All should score within your expected range.
4. **Document Threshold**: Define what score ranges mean for your context (e.g., 4.5+ = "ready for deployment", 3.5-4.4 = "revise", < 3.5 = "redesign").

---

## References

- Anderson, L.W., Krathwohl, D.R. (eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy*. Longman.
- Dick, W., Carey, L., & Carey, J.O. (2015). *The Systematic Design of Instruction* (8th ed.). Pearson.
- Kubiszyn, T., & Borich, G.D. (2013). *Educational Testing and Measurement* (10th ed.). Wiley.
- Mager, R.F. (1997). *Preparing Instructional Objectives* (3rd ed.). Fearon Teachers Aids.

---

## Troubleshooting

| Issue | Resolution |
|-------|-----------|
| Scores are consistently high (4.5+) | Your items may be well-designed, or the prompt is being too lenient. Test on intentionally poor items to validate the rubric is discriminating. |
| Scores vary wildly between runs | Temperature may be too high (use 0.0). Ensure your input is formatted consistently. Consider re-running with a clearer artifact. |
| Judge flags too many "severity_flags" | Reduce sensitivity by clarifying what "severity" means in your context. A lower Bloom's level is not always severe if objectives allow it. |
| Dimension scores disagree with expert judgment | Review the dimension definitions and scoring guide. Adjust prompt wording or provide reference examples to calibrate the judge. |
