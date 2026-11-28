# Archetype 11: Summative Evaluation & Learning Transfer

**Purpose**: Design and evaluate the plan, and the report, that answer the question asked after release: did people learn it, do they use it on the job, and did that change anything that matters? The dimensions below work in both directions: draft a summative evaluation or measurement plan against them, or score an existing plan, dashboard specification, or impact report.

**When this is skipped** (an illustrative scenario): A new-manager programme runs for a year. The dashboard shows 94% completion and a 4.6 out of 5 satisfaction rating, and the programme is renewed. Nobody checks whether managers hold the feedback conversations the programme taught. They do not: the practice was never scheduled into their week, and their own managers never ask about it. The numbers were accurate and answered the wrong question. If your evidence that training worked is completion and satisfaction, this archetype is for you.

**Design targets** (using these dimensions forward, in design mode) - the moves that produce a 4-5:
- Plan evidence along the whole chain - reaction, learning, behavior on the job, and results - and say in advance which links you will not measure and why (Kirkpatrick & Kirkpatrick; Thalheimer).
- Map every objective to at least one measure and one data source before launch, so the instruction is built to emit the evidence.
- Measure after a delay as well as at the end, against a baseline or a comparison, and state what else could explain the result (Phillips; Shadish, Cook & Campbell).
- Plan for the conditions that make transfer happen - manager support, opportunity to use, follow-up - and measure them (Baldwin & Ford).
- Write the decision rule before the data arrives: what result means continue, revise, or retire, and which part of the design each finding goes back to.

Then run an evaluate-mode self-check against the scoring anchors below.

**Professional alignment** (the professional standards this archetype *aims* to align with - an independent, aspirational mapping by the author, not reviewed or endorsed by these bodies; see [`discipline_alignment_crosswalk.md`](discipline_alignment_crosswalk.md) for the full mapping, citations, and licensing notes):
- **IBSTPI ID Competencies (2012)** - Evaluation & Implementation: C17 (evaluating interventions), C18 (data-based revision).
- **ATD Capability Model (2020)** - Evaluating Impact; Data & Analytics; Performance Improvement.
- **ISPI/HPT Ten Standards** - S1 Focus on Results; S10 Evaluate Results and Measure Impact.

**Evaluation Context**: Use this archetype when assessing:
- Summative evaluation plans and impact study designs
- Measurement and learning analytics plans written before launch
- Dashboard or report specifications for a course or programme
- Impact reports, post-launch reviews, and programme renewal cases
- xAPI or other tracking designs (which events are recorded, and why)
- Transfer and follow-up plans (manager check-ins, spaced follow-up, on-the-job observation)

**Relationship to other archetypes:**
- **06 Formative Evaluation** is run before release, with a handful of learners, to fix the instruction. Archetype 11 is run after release, with the real population, to judge whether it worked and what the next version should change. Archetype 06 flags "summative claims from formative data"; archetype 11 is where summative claims belong.
- **02 Assessment Design** evaluates whether the test itself is sound. Archetype 11 uses test results as one link in the chain and asks what happens after the test.
- **07 Needs Analysis** defines the performance gap. Archetype 11 checks whether that same gap closed, using the measure 07 named.
- **03 Instructional Sequencing** scores how the instruction itself supports transfer (Transfer & Retention Design). Archetype 11 scores the workplace conditions around it and whether transfer was measured.
- **10 Curriculum Alignment** checks on paper that objectives, strategies, and assessments agree. Archetype 11 checks in practice, with learner data, whether that alignment produced the outcome.

**Two ways to run this archetype:**
- **Measurement plan** (before launch, in the Evaluate phase beside archetype 06): score the plan for how the course will be judged once it is live. Like every other archetype, this score enters the composite when a plan is present and is left out when it is not.
- **Impact report** (after launch): score the report, dashboard, or renewal case that claims the course worked. When a measurement plan exists, pass it as the reference, so dimension 6 can check the result against the thresholds set in advance. This score is reported on its own as an **evidence verdict**, using the bands under "Score Interpretation for Stakeholders" below. It is never averaged into the design composite: a well-designed course is not evidence of impact, and good impact evidence does not repair a design that failed its gate.

---

## Rubric: 6 Dimensions (1-5 Scale)

### 1. Outcome Chain Coverage (1-5)

Does the evidence follow the whole chain from participation to results, or does it stop at the easy end? Not every link must be measured, but omissions should be stated and justified.

| Score | Participation & Reaction | Learning | Behavior on the Job | Results | Rationale |
|-------|-------------------------|----------|--------------------|---------|-----------|
| **1** | Completion or attendance only | Not measured | Not measured | Not measured | Completion treated as success |
| **2** | Completion + satisfaction | End-of-course quiz only | Not measured | Asserted, not measured | No justification for gaps |
| **3** | Measured | Measured against objectives | Self-report only | Named, loosely linked | Some gaps acknowledged |
| **4** | Measured | Measured against objectives | Observed or system evidence | One results measure tied to the original gap | Gaps justified |
| **5** | Measured, kept in proportion | Decision-making and task performance, not recall alone | Multiple sources, including delayed | Results measure agreed with the sponsor before launch | Explicit rationale for every link measured or skipped |

**The chain, in plain terms** (after Kirkpatrick & Kirkpatrick; tiers after Thalheimer's LTEM):
1. **Participation**: who attended, started, finished. Says nothing about learning.
2. **Reaction**: what learners thought of it. A weak guide to learning: liking correlates about zero with learning (Alliger et al., 1997), and where reactions do relate to learning it is to learning measured straight after training, not later (Sitzmann et al., 2008).
3. **Learning**: what they can recall, decide, and do at the end.
4. **Behavior**: what they do on the job, weeks later.
5. **Results**: what changed for the team or organisation because of that behavior.

---

### 2. Objective-Evidence Traceability (1-5)

Can each objective be followed to the data that will show whether it was met?

| Score | Objective Mapping | Data Sources | Instrumentation | Granularity | Gaps |
|-------|------------------|--------------|-----------------|-------------|------|
| **1** | No mapping; course-level totals only | Unnamed | Whatever the platform records by default | Course | Unknown |
| **2** | Some objectives mapped | Named loosely ("LMS data") | Default tracking | Module | Not identified |
| **3** | Most objectives mapped to a measure | Named per measure | Some events added on purpose | Activity | Some identified |
| **4** | Every objective mapped to a measure and source | Named, with owner | Events designed for the questions asked | Item or task | Identified with plan |
| **5** | Explicit objective-to-evidence table, built before launch | Named, with owner and access confirmed | Stable identifiers link each objective to its activities and items | Item or task, rolled up to objective | None, or justified |

**Objective-to-evidence table (template):**
```
Objective: [e.g., "Hold a feedback conversation using the SBI structure"]
Learning evidence: [e.g., "Scenario 3 decisions; role-play checklist score"]
Behavior evidence: [e.g., "Manager observation checklist at 30 days; 1:1 notes sampled"]
Results evidence: [e.g., "Team engagement item 7, next survey cycle"]
Data source and owner: [e.g., "Learning record store - L&D; engagement survey - HR"]
```

**Notes on tracking data:**
- Record events because a question needs them, not because the tool can.
- A nested course often reports its parts as unrelated activities. Record the parent-child structure at build time; it is hard to recover later.
- Some activities record a learner's choice or commitment rather than a right or wrong answer. Report these as frequencies, without correct/incorrect framing.

---

### 3. Measurement Quality (1-5)

Are the measures taken at the right time, with sound instruments, from enough people?

| Score | Timing | Instruments | Sample | Response Quality | Behavior Measures |
|-------|--------|-------------|--------|------------------|-------------------|
| **1** | End of course only | Satisfaction survey only | Whoever replied | Not considered | None |
| **2** | End of course only | Recall quiz + satisfaction | Convenience; size not stated | Low response accepted | Self-rated confidence |
| **3** | One delayed measure | Performance-relevant items | Size stated | Response rate reported | Self-report of use |
| **4** | Baseline, end, and delayed | Scenario or task-based; observation checklist | Adequate and described | Non-response considered | Observation or work-system evidence |
| **5** | Baseline, end, and two or more delayed points | Piloted instruments with stated reliability | Planned size with rationale | Non-response bias examined | Multiple independent sources that agree |

**Guidance:**
- **Delay matters.** A test at the end of the course measures what was just seen. Remeasure after days or weeks to see what was kept.
- **Confidence is not competence.** Self-rated confidence and satisfaction do not stand in for performance (Roediger & Karpicke, 2006).
- **Use more than one source.** Behavior rated by the same person in the same setting as the training looks stronger than it is (Blume et al., 2010).
- **Small groups.** With few learners, report counts and cases rather than percentages, and say so.

---

### 4. Attribution & Comparison (1-5)

When a result changes, is there reason to believe the training caused it?

| Score | Baseline | Comparison | Other Explanations | Claims | Method |
|-------|----------|------------|--------------------|--------|--------|
| **1** | None | None | Ignored | Causal claims from after-only data | None |
| **2** | Informal | None | Not discussed | Overstated | Before/after implied |
| **3** | Measured | Before/after only | Mentioned | Mostly proportionate | Before/after |
| **4** | Measured | Comparison group, staggered rollout, or trend line | Listed and addressed | Proportionate to the design | Quasi-experimental or success-case |
| **5** | Measured on the results measure | Comparison plus trend | Systematically examined | Confidence level stated; limits named | Designed comparison, with success and non-success cases explaining why |

**Practical ways to compare** (choose what the setting allows):
- **Before and after**: the minimum. Weak alone, since anything else that changed is mixed in.
- **Staggered rollout**: teams trained later serve as the comparison for teams trained first.
- **Trend line**: several measures before and after, so an existing trend is not mistaken for an effect.
- **Success Case Method** (Brinkerhoff): find the people for whom it worked best and least, and document why. Suited to small programmes.
- **Isolating the effect** (Phillips): control groups, trend analysis, or structured estimates, used before any return-on-investment figure is quoted.

---

### 5. Workplace Transfer Conditions (1-5)

Does the plan account for what has to be true at work for the new behavior to appear and last? This dimension covers what happens outside the instruction. Practice and spaced review built into the course itself are scored by archetype 03 (Transfer & Retention Design).

| Score | Manager Support | Opportunity to Use | Follow-Up | Environment Barriers | Measured? |
|-------|-----------------|--------------------|-----------|---------------------|-----------|
| **1** | Not considered | Not considered | None | Not considered | No |
| **2** | Mentioned | Assumed | A reminder email | Mentioned | No |
| **3** | Managers informed | Identified | One follow-up activity | Some named | Partly |
| **4** | Managers have a defined role | Planned within weeks | Spaced follow-up | Named, with owner | Yes |
| **5** | Managers briefed, equipped, and asked to report | Scheduled into work | Spaced follow-up plus commitments revisited | Barriers from needs analysis tracked to closure | Yes, and reported beside outcomes |

**Three groups of transfer factors** (Baldwin & Ford, 1988):
- **The learner**: ability, motivation, belief that it will be useful.
- **The design**: practice that resembles the job, varied examples, feedback.
- **The workplace**: support from managers and peers, opportunity to use the skill, time, tools, and consequences.

A plan that measures behavior without measuring these conditions cannot tell a weak course from a workplace that prevented its use.

---

### 6. Decision Rules & Feedback Loop (1-5)

Is it clear what will be done with the findings, and do they reach the next version?

| Score | Decision Rule | Routing | Version Comparison | Data Ethics | Reporting |
|-------|---------------|---------|--------------------|-------------|-----------|
| **1** | None; report is the end product | None | None | Not addressed | Numbers without interpretation |
| **2** | Implied | Informal | None | Minimal | Descriptive |
| **3** | Stated after the data arrives | To the course owner | Informal | Addressed | Findings with some interpretation |
| **4** | Stated in advance | Each finding tied to a part of the design | Cohorts compared across versions | Aggregated reporting; access defined | Findings with recommended actions |
| **5** | Thresholds for continue, revise, and retire set in advance, with a minimum sample | Each finding names the objective, the suspected design dimension, and an owner | Versions compared on the same measures; changes logged | Consent, aggregation, retention, and no punitive use stated | Written for the decision-maker; limits stated |

**Finding template:**
```
Evidence: [e.g., "61% chose option B on Scenario 3, decision 2 (n=140)"]
Objective: [which objective this bears on]
Suspected cause: [e.g., "Distractor B matches the pre-training habit; practice gave no feedback on it"]
Proposed change: [e.g., "Add a worked example contrasting A and B; revise feedback"]
Decision and owner: [revise in next version - course owner]
```

---

## Output JSON

Return this shape when the user wants machine-readable output (scores are integers 1-5; `overall` follows the archetype's scoring rule):

```json
{
  "scores": {
    "outcome_chain_coverage": <1-5>,
    "objective_evidence_traceability": <1-5>,
    "measurement_quality": <1-5>,
    "attribution_comparison": <1-5>,
    "transfer_conditions": <1-5>,
    "decision_feedback_loop": <1-5>,
    "overall": <mean of all 6>
  },
  "rationale": {
    "outcome_chain_coverage": "<brief explanation>",
    "objective_evidence_traceability": "<brief explanation>",
    "measurement_quality": "<brief explanation>",
    "attribution_comparison": "<brief explanation>",
    "transfer_conditions": "<brief explanation>",
    "decision_feedback_loop": "<brief explanation>"
  },
  "severity_flags": ["<critical issue 1>", "<critical issue 2>"],
  "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>"]
}
```

---

## Severity Flags (Red Flags)

Look for and flag critical issues. Each one means the evaluation cannot support the decision it is meant to inform:

1. **Completion or Satisfaction as Effectiveness**: The programme is judged a success on attendance, completion, or ratings alone
2. **Nothing Measured After the Course Ends**: All evidence is collected on the last day, yet lasting learning or behavior change is claimed
3. **Objectives with No Evidence**: One or more objectives have no measure or data source mapped to them
4. **Attribution Without Comparison**: A change in results, or a return-on-investment figure, is credited to training with no baseline, comparison, or account of other causes
5. **Behavior from Self-Report Alone**: On-the-job behavior change is claimed only from learners saying they changed
6. **Learner Data Misuse**: Individual learner records are exposed beyond need, kept without limit, or used to penalise individuals
7. **No Route Back to the Design**: Findings are reported, but nothing says who decides, on what threshold, or which part of the instruction changes

---

## Implementation Notes

### Data Input Format
```json
{
  "document_type": "evaluation_plan | measurement_plan | dashboard_spec | impact_report",
  "project_type": "elearning_module | course | programme | performance_support",
  "stage": "pre_launch | post_launch",
  "population_size": "number",
  "time_since_launch_weeks": "number"
}
```

### Expected Scoring Patterns
- **Rigorous (5-4)**: Whole chain planned; objective-to-evidence table; baseline and delayed measures; a comparison; transfer conditions measured; decision thresholds set in advance.
- **Adequate (3)**: Learning measured against objectives; one delayed or self-report behavior measure; before/after only; managers informed; decisions made after the fact.
- **Weak (2)**: Completion, satisfaction, and a recall quiz; results asserted; no comparison; workplace assumed.
- **Non-starter (1)**: Completion dashboard presented as proof of impact.

### Proportionality
Match the effort to the stakes. A five-minute job aid does not need a comparison group; a year-long leadership programme does. A plan can score well with few measures if it says plainly what it will and will not be able to claim.

---

## Citation & References

Bibliographic details were checked on 2026-11-27: journal articles against Crossref records, books against catalogue records, and a subset against the published text itself. `docs/archetype_11_evidence_and_decisions.md` in the GUIDE repository holds the "Evidence Base by Dimension" table (the claim each dimension makes, the source cited for it, whether the source supports it, and how far the source was read), the verification notes, and the design decisions behind this archetype's place in the pipeline.

**Evaluation Models**
- Kirkpatrick, D.L., & Kirkpatrick, J.D. (2006). Evaluating Training Programs: The Four Levels (3rd ed.). Berrett-Koehler.
- Kirkpatrick, J.D., & Kirkpatrick, W.K. (2016). Kirkpatrick's Four Levels of Training Evaluation. ATD Press.
- Phillips, J.J. (2003). Return on Investment in Training and Performance Improvement Programs (2nd ed.). Butterworth-Heinemann.
- Brinkerhoff, R.O. (2003). The Success Case Method: Find Out Quickly What's Working and What's Not. Berrett-Koehler.
- Thalheimer, W. (2018). The Learning-Transfer Evaluation Model: Sending Messages to Enable Learning Effectiveness. Work-Learning Research.
- Kaufman, R., & Keller, J.M. (1994). Levels of evaluation: Beyond Kirkpatrick. Human Resource Development Quarterly, 5(4), 371-380. https://doi.org/10.1002/hrdq.3920050408
- Kaufman, R. (2003). Value, value: Where is the value? Performance Improvement, 42(2), 36-38. https://doi.org/10.1002/pfi.4930420214
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.). Pearson. (Chapter: Designing and Conducting Summative Evaluations)
- Scriven, M. (1967). The methodology of evaluation. In R.W. Tyler, R.M. Gagné, & M. Scriven (Eds.), Perspectives of Curriculum Evaluation. Rand McNally. (Formative and summative distinction)

**Critiques and Evidence**
- Holton, E.F. (1996). The flawed four-level evaluation model. Human Resource Development Quarterly, 7(1), 5-21. https://doi.org/10.1002/hrdq.3920070103
- Alliger, G.M., Tannenbaum, S.I., Bennett, W., Traver, H., & Shotland, A. (1997). A meta-analysis of the relations among training criteria. Personnel Psychology, 50(2), 341-358. https://doi.org/10.1111/j.1744-6570.1997.tb00911.x
- Sitzmann, T., Brown, K.G., Casper, W.J., Ely, K., & Zimmerman, R.D. (2008). A review and meta-analysis of the nomological network of trainee reactions. Journal of Applied Psychology, 93(2), 280-295. https://doi.org/10.1037/0021-9010.93.2.280
- Arthur, W., Bennett, W., Edens, P.S., & Bell, S.T. (2003). Effectiveness of training in organizations: A meta-analysis of design and evaluation features. Journal of Applied Psychology, 88(2), 234-245. https://doi.org/10.1037/0021-9010.88.2.234
- Salas, E., Tannenbaum, S.I., Kraiger, K., & Smith-Jentsch, K.A. (2012). The science of training and development in organizations: What matters in practice. Psychological Science in the Public Interest, 13(2), 74-101. https://doi.org/10.1177/1529100612436661
- DeVaughn, P., & Stefaniak, J. (2020). An exploration of the challenges instructional designers encounter while conducting evaluations. Performance Improvement Quarterly, 33(4), 443-470. https://doi.org/10.1002/piq.21332
- Clark, R.C. (2020). Evidence-Based Training Methods: A Guide for Training Professionals (3rd ed.). ATD Press.
- Kraiger, K., Ford, J.K., & Salas, E. (1993). Application of cognitive, skill-based, and affective theories of learning outcomes to new methods of training evaluation. Journal of Applied Psychology, 78(2), 311-328. https://doi.org/10.1037/0021-9010.78.2.311

**Transfer of Training**
- Baldwin, T.T., & Ford, J.K. (1988). Transfer of training: A review and directions for future research. Personnel Psychology, 41(1), 63-105. https://doi.org/10.1111/j.1744-6570.1988.tb00632.x
- Blume, B.D., Ford, J.K., Baldwin, T.T., & Huang, J.L. (2010). Transfer of training: A meta-analytic review. Journal of Management, 36(4), 1065-1105. https://doi.org/10.1177/0149206309352880
- Ford, J.K., Baldwin, T.T., & Prasad, J. (2018). Transfer of training: The known and the unknown. Annual Review of Organizational Psychology and Organizational Behavior, 5, 201-225. https://doi.org/10.1146/annurev-orgpsych-032117-104443
- Grossman, R., & Salas, E. (2011). The transfer of training: What really matters. International Journal of Training and Development, 15(2), 103-120. https://doi.org/10.1111/j.1468-2419.2011.00373.x
- Wurth, A., & Wurth, K. (2018). Training Reinforcement. Wiley. (Practitioner guidance)

**Retention and Delayed Measurement**
- Soderstrom, N.C., & Bjork, R.A. (2015). Learning versus performance: An integrative review. Perspectives on Psychological Science, 10(2), 176-199. https://doi.org/10.1177/1745691615569000
- Roediger, H.L., & Karpicke, J.D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249-255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354-380. https://doi.org/10.1037/0033-2909.132.3.354
- Brown, P.C., Roediger, H.L., & McDaniel, M.A. (2014). Make It Stick: The Science of Successful Learning. Belknap Press of Harvard University Press.

**Measurement**
- Kubiszyn, T., & Borich, G.D. (2016). Educational Testing and Measurement: Classroom Application and Practice (11th ed.). Wiley.

**Learning Analytics and Data Ethics**
- Gašević, D., Dawson, S., & Siemens, G. (2015). Let's not forget: Learning analytics are about learning. TechTrends, 59(1), 64-71. https://doi.org/10.1007/s11528-014-0822-x
- Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and dilemmas. American Behavioral Scientist, 57(10), 1510-1529. https://doi.org/10.1177/0002764213479366
- IEEE. (2023). IEEE Standard for Learning Technology - JavaScript Object Notation (JSON) Data Model Format and Representational State Transfer (RESTful) Web Service for Learner Experience Data Tracking and Access (IEEE Std 9274.1.1-2023). (The xAPI standard)
- Giacumo, L.A., Villachica, S.W., & Stepich, D.A. (2025). Instructional Design for Organizational Justice. Routledge. (Chapter 12: implementation, summative evaluation, and continuous improvement)

**Research Design**
- Shadish, W.R., Cook, T.D., & Campbell, D.T. (2002). Experimental and Quasi-Experimental Designs for Generalized Causal Inference. Houghton Mifflin.

The models above are named with attribution and described in the author's own words. GUIDE is independent of, and not endorsed by, their authors or rights holders.

---

## Common Evaluation Scenarios

### Scenario A: Compliance Course, Large Population
- **Chain**: Completion, scenario-based decisions, incident or audit findings as the results measure
- **Traceability**: Each policy objective mapped to scenario decisions
- **Measurement**: Baseline incident rate; delayed scenario check at 90 days
- **Comparison**: Trend line across prior years; staggered rollout by site
- **Transfer**: Job aid at the point of need; supervisors briefed
- **Decision rule**: Any decision point under 70% correct is revised before the next cycle

### Scenario B: New-Manager Programme, Small Cohorts
- **Chain**: Role-play performance, observed feedback conversations, team engagement item
- **Traceability**: Objective-to-evidence table with manager observation checklist
- **Measurement**: Baseline, end, 30 and 90 days; counts and cases, not percentages
- **Comparison**: Success Case Method across two cohorts
- **Transfer**: Senior managers ask about commitments in 1:1s; practice scheduled
- **Decision rule**: Fewer than half of commitments acted on at 30 days triggers a review of workplace barriers before any course change

### Scenario C: Sales Enablement, Fast Turnaround
- **Chain**: Product knowledge check, call observation, conversion on the new product
- **Traceability**: Each talking point mapped to a call-review item
- **Measurement**: Call reviews two and six weeks after launch
- **Comparison**: Teams enabled in week one against teams enabled in week four
- **Transfer**: Battle card in the sales tool; managers coach from call reviews
- **Decision rule**: Talking points used in under 30% of reviewed calls are rewritten or dropped

### Scenario D: Performance Support Only (No Course)
- **Chain**: Use of the job aid, task accuracy, rework rate
- **Traceability**: Each step in the aid mapped to an error type
- **Measurement**: Error log before and after; short observation sample
- **Comparison**: Before/after with trend
- **Transfer**: The aid sits in the workflow; this dimension is about findability and upkeep
- **Decision rule**: Error types that do not fall are examined for a tool or process cause

---

## Validation Checklist

Use this before scoring:

- [ ] The question the evaluation must answer, and the decision it informs, are stated
- [ ] Each link in the chain is either measured or explicitly set aside with a reason
- [ ] Every objective maps to at least one measure and data source
- [ ] At least one measure is taken after a delay
- [ ] A baseline or comparison exists for the behavior or results measure
- [ ] Other explanations for the result are listed
- [ ] Manager support, opportunity to use, and follow-up are planned and measured
- [ ] Thresholds for continue, revise, or retire are set in advance
- [ ] Each finding has a route to a part of the design and an owner
- [ ] Learner data handling is stated: consent, aggregation, retention, permitted use
- [ ] Limits of the evidence are stated in the report

---

## Score Interpretation for Stakeholders

| Overall Range | Status | Action |
|--------------|--------|--------|
| **4.5-5.0** | Excellent | Evidence supports decisions about the programme; act on findings |
| **3.5-4.4** | Good | Sound evidence with named limits; act on findings, close the stated gaps next cycle |
| **2.5-3.4** | Fair | Supports claims about learning, not about behavior or results; do not quote impact |
| **< 2.5** | Poor to inadequate | Reports activity, not effect; redesign the evaluation before renewing or scaling |

---

## Rapid Evaluation Checklist (for quick assessments)

When time is tight, prioritize:
1. **Chain**: Something beyond completion and satisfaction is measured
2. **Traceability**: Each objective has a measure
3. **Delay**: At least one measure after the course ends
4. **Comparison**: A baseline exists
5. **Decision**: A stated rule for what happens next

If these five are met, score ≥3 ("Fair"). Lower scores indicate critical gaps.

---

*Source: GUIDE - Grounded Universal Instructional Design Evaluator (v3.5.0). Copyright 2026 Jeremy Terhune. Licensed under the Apache License, Version 2.0. Archetype 11 of 11. Skill edition: the judge prompts and Python-harness notes are omitted; the full model-agnostic handoff is `archetypes/handoff_11_summative_evaluation.md` in the GUIDE repository.*
