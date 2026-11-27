# Archetype 11: Summative Evaluation & Learning Transfer

> **DRAFT - not part of the released framework.** This file lives in `docs/drafts/` so the build scripts, which read `archetypes/handoff_*.md`, do not pick it up. Dimension names, anchors, and citations are proposals for review. See "Open questions" at the end.

**Purpose**: Design and evaluate the plan, and the report, that answer the question asked after release: did people learn it, do they use it on the job, and did that change anything that matters? The dimensions below work in both directions: draft a summative evaluation or measurement plan against them, or score an existing plan, dashboard specification, or impact report.

**When this is skipped** (an illustrative scenario): A new-manager programme runs for a year. The dashboard shows 94% completion and a 4.6 out of 5 satisfaction rating, and the programme is renewed. Nobody checks whether managers hold the feedback conversations the programme taught. They do not: the practice was never scheduled into their week, and their own managers never ask about it. The numbers were accurate and answered the wrong question. If your evidence that training worked is completion and satisfaction, this archetype is for you.

**Design targets** (using these dimensions forward, in design mode) - the moves that produce a 4-5:
- Plan evidence along the whole chain - reaction, learning, behavior on the job, and results - and say in advance which links you will not measure and why (Kirkpatrick & Kirkpatrick; Thalheimer).
- Map every objective to at least one measure and one data source before launch, so the instruction is built to emit the evidence.
- Measure after a delay as well as at the end, against a baseline or a comparison, and state what else could explain the result (Phillips; Shadish, Cook & Campbell).
- Plan for the conditions that make transfer happen - manager support, opportunity to use, follow-up - and measure them (Baldwin & Ford).
- Write the decision rule before the data arrives: what result means continue, revise, or retire, and which part of the design each finding goes back to.

Then run an evaluate-mode self-check against the scoring anchors below.

**Professional alignment** (the professional standards this archetype *aims* to align with - an independent, aspirational mapping by the author, not reviewed or endorsed by these bodies; see [`discipline_alignment_crosswalk.md`](../../archetypes/discipline_alignment_crosswalk.md) for the full mapping, citations, and licensing notes):
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
- **10 Curriculum Alignment** checks on paper that objectives, strategies, and assessments agree. Archetype 11 checks in practice, with learner data, whether that alignment produced the outcome.

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
2. **Reaction**: what learners thought of it. Weakly related to learning (Alliger et al., 1997).
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
- **Confidence is not competence.** Self-rated confidence and satisfaction do not stand in for performance.
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

### 5. Transfer Conditions (1-5)

Does the plan account for what has to be true at work for the new behavior to appear and last?

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

## System Prompt (Judge Rubric)

```
You are an expert in training evaluation, learning transfer, and learning analytics.
Your role is to assess summative evaluation plans, measurement plans, dashboard specifications,
and impact reports for quality and appropriateness.

You will score across 6 dimensions, each on a 1-5 scale:

1. **Outcome Chain Coverage** (1-5)
- Evidence should follow the chain: participation, reaction, learning, behavior on the job, results
- Not every link must be measured, but omissions should be stated and justified
- Completion and satisfaction alone are not evidence of learning or transfer
Score: 1=Completion or satisfaction treated as success; 5=Whole chain planned with rationale for each link

2. **Objective-Evidence Traceability** (1-5)
- Each objective maps to a measure and a named data source
- Tracking is designed for the questions asked, not left to platform defaults
- Stable identifiers link objectives to activities and items
Score: 1=Course-level totals, no mapping; 5=Explicit objective-to-evidence table built before launch

3. **Measurement Quality** (1-5)
- Timing: baseline, end of instruction, and delayed measures
- Instruments measure performance, not recall or confidence alone
- Sample size and response rate stated; non-response considered
- Behavior measured by observation or work-system evidence, not self-report alone
Score: 1=End-of-course satisfaction only; 5=Baseline plus delayed measures, piloted instruments, multiple agreeing sources

4. **Attribution & Comparison** (1-5)
- Baseline and some form of comparison (comparison group, staggered rollout, trend line, success cases)
- Other explanations for the result listed and addressed
- Claims proportionate to the design; limits stated
Score: 1=Causal claims from after-only data; 5=Designed comparison, alternatives examined, confidence stated

5. **Transfer Conditions** (1-5)
- Manager support, opportunity to use, follow-up, and workplace barriers are planned for
- These conditions are measured and reported beside outcomes
Score: 1=Workplace not considered; 5=Managers equipped, use scheduled, spaced follow-up, barriers tracked

6. **Decision Rules & Feedback Loop** (1-5)
- Thresholds for continue, revise, or retire set before data arrives
- Each finding is routed to a specific part of the design with an owner
- Versions compared on the same measures
- Learner data handled ethically: consent, aggregation, retention, no punitive use
Score: 1=Report is the end product; 5=Advance thresholds, routed findings, version comparison, ethics stated

Severity flags to raise: completion or satisfaction presented as effectiveness; no measure after the end of the course; objectives with no evidence mapped; causal or return-on-investment claims with no baseline or comparison; behavior claimed from self-report alone; individual learner data exposed or used punitively; findings with no route back to the design.

Return JSON with overall score (mean of 6 dimensions), individual dimension scores, rationale per dimension, severity_flags (critical issues), and improvement_suggestions (actionable next steps).
```

---

## Human Prompt Template

```
Evaluate the following summative evaluation plan, measurement plan, or impact report.

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

## Evidence Base by Dimension

What each dimension rests on, and who to cite for it. Full references follow.

| Dimension | Claim the rubric makes | Evidence to cite |
|---|---|---|
| 1. Outcome Chain Coverage | Satisfaction and completion do not show learning or transfer | Alliger et al. (1997) and Sitzmann et al. (2008): meta-analyses finding reactions only weakly related to learning. Kirkpatrick & Kirkpatrick (2016), Kaufman & Keller (1994), Thalheimer (2018) for the chain itself; Holton (1996) for the critique |
| 1. Outcome Chain Coverage | Practitioners rarely evaluate past the end-of-course test | DeVaughn & Stefaniak (2020): the barriers instructional designers report when evaluating |
| 2. Objective-Evidence Traceability | Measures should be derived from objectives, and tracking designed for the question | Dick, Carey & Carey (2015) on criterion-referenced measures and summative evaluation; Kraiger, Ford & Salas (1993) on matching measures to outcome type; Gašević, Dawson & Siemens (2015) on analytics grounded in learning design; IEEE 9274.1.1-2023 for xAPI |
| 3. Measurement Quality | Delayed measures show what was retained; end-of-course tests overstate it | Roediger & Karpicke (2006); Cepeda et al. (2006); Brown, Roediger & McDaniel (2014) |
| 3. Measurement Quality | Instruments need evidence of validity and reliability | Kubiszyn & Borich (2016) |
| 4. Attribution & Comparison | After-only data cannot support causal claims | Shadish, Cook & Campbell (2002); Phillips (2003) on isolating effects; Brinkerhoff (2003) for small programmes; Arthur et al. (2003) on how effect sizes vary by criterion |
| 5. Transfer Conditions | Transfer depends on the learner, the design, and the workplace | Baldwin & Ford (1988); Blume et al. (2010); Ford, Baldwin & Prasad (2018); Grossman & Salas (2011); Salas et al. (2012) on what happens before and after training |
| 5. Transfer Conditions | Follow-up and reinforcement sustain new behavior | Wurth & Wurth (2018); Cepeda et al. (2006) |
| 6. Decision Rules & Feedback Loop | Evaluation exists to inform a decision | Scriven (1967); Dick, Carey & Carey (2015); Kaufman (2003) on value to the organisation and society |
| 6. Decision Rules & Feedback Loop | Learner data carries ethical obligations | Slade & Prinsloo (2013); Giacumo, Villachica & Stepich (2024) on equity in design and evaluation |

---

## Citation & References

Entries marked **[checked]** were confirmed against a publisher, repository, or index record while drafting. All others were written from memory or from course materials and must be verified before release.

**Evaluation Models**
- Kirkpatrick, D.L., & Kirkpatrick, J.D. (2006). Evaluating Training Programs: The Four Levels (3rd ed.). Berrett-Koehler.
- Kirkpatrick, J.D., & Kirkpatrick, W.K. (2016). Kirkpatrick's Four Levels of Training Evaluation. ATD Press.
- Phillips, J.J. (2003). Return on Investment in Training and Performance Improvement Programs (2nd ed.). Butterworth-Heinemann.
- Brinkerhoff, R.O. (2003). The Success Case Method: Find Out Quickly What's Working and What's Not. Berrett-Koehler.
- Thalheimer, W. (2018). The Learning-Transfer Evaluation Model: Sending Messages to Enable Learning Effectiveness. Work-Learning Research. **[checked: title and year]**
- Kaufman, R., & Keller, J.M. (1994). Levels of evaluation: Beyond Kirkpatrick. Human Resource Development Quarterly, 5(4), 371-380.
- Kaufman, R. (2003). Value, value, where is the value? Performance Improvement, 42(2). (Pages to confirm)
- Dick, W., Carey, L., & Carey, J.O. (2015). The Systematic Design of Instruction (8th ed.). Pearson. (Chapter on summative evaluation)
- Scriven, M. (1967). The methodology of evaluation. In R.W. Tyler, R.M. Gagné, & M. Scriven (Eds.), Perspectives of Curriculum Evaluation. Rand McNally. (Formative and summative distinction)

**Critiques and Evidence**
- Holton, E.F. (1996). The flawed four-level evaluation model. Human Resource Development Quarterly, 7(1), 5-21.
- Alliger, G.M., Tannenbaum, S.I., Bennett, W., Traver, H., & Shotland, A. (1997). A meta-analysis of the relations among training criteria. Personnel Psychology, 50(2), 341-358. https://doi.org/10.1111/j.1744-6570.1997.tb00911.x **[checked]**
- Sitzmann, T., Brown, K.G., Casper, W.J., Ely, K., & Zimmerman, R.D. (2008). A review and meta-analysis of the nomological network of trainee reactions. Journal of Applied Psychology, 93(2), 280-295. https://doi.org/10.1037/0021-9010.93.2.280 **[checked]**
- Arthur, W., Bennett, W., Edens, P.S., & Bell, S.T. (2003). Effectiveness of training in organizations: A meta-analysis of design and evaluation features. Journal of Applied Psychology, 88(2), 234-245.
- Salas, E., Tannenbaum, S.I., Kraiger, K., & Smith-Jentsch, K.A. (2012). The science of training and development in organizations: What matters in practice. Psychological Science in the Public Interest, 13(2), 74-101. https://doi.org/10.1177/1529100612436661 **[checked]**
- DeVaughn, P., & Stefaniak, J. (2020). An exploration of the challenges instructional designers encounter while conducting evaluations. Performance Improvement Quarterly, 33(4), 443-470. https://doi.org/10.1002/piq.21332 **[checked: one source lists a different volume; confirm on the journal page]**
- Kraiger, K., Ford, J.K., & Salas, E. (1993). Application of cognitive, skill-based, and affective theories of learning outcomes to new methods of training evaluation. Journal of Applied Psychology, 78(2), 311-328.

**Transfer of Training**
- Baldwin, T.T., & Ford, J.K. (1988). Transfer of training: A review and directions for future research. Personnel Psychology, 41(1), 63-105.
- Blume, B.D., Ford, J.K., Baldwin, T.T., & Huang, J.L. (2010). Transfer of training: A meta-analytic review. Journal of Management, 36(4), 1065-1105.
- Ford, J.K., Baldwin, T.T., & Prasad, J. (2018). Transfer of training: The known and the unknown. Annual Review of Organizational Psychology and Organizational Behavior, 5, 201-225. https://doi.org/10.1146/annurev-orgpsych-032117-104443 **[checked: article and DOI; confirm pages]**
- Grossman, R., & Salas, E. (2011). The transfer of training: What really matters. International Journal of Training and Development, 15(2), 103-120.
- Wurth, A., & Wurth, K. (2018). Training Reinforcement: The 7 Principles to Create Measurable Behavior Change and Make Learning Stick. Wiley.

**Retention and Delayed Measurement**
- Roediger, H.L., & Karpicke, J.D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. Psychological Science, 17(3), 249-255.
- Cepeda, N.J., Pashler, H., Vul, E., Wixted, J.T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354-380.
- Brown, P.C., Roediger, H.L., & McDaniel, M.A. (2014). Make It Stick: The Science of Successful Learning. Harvard University Press.

**Measurement**
- Kubiszyn, T., & Borich, G.D. (2016). Educational Testing and Measurement: Classroom Application and Practice (11th ed.). Wiley.

**Learning Analytics and Data Ethics**
- Gašević, D., Dawson, S., & Siemens, G. (2015). Let's not forget: Learning analytics are about learning. TechTrends, 59(1), 64-71. https://doi.org/10.1007/s11528-014-0822-x **[checked]**
- Slade, S., & Prinsloo, P. (2013). Learning analytics: Ethical issues and dilemmas. American Behavioral Scientist, 57(10), 1510-1529. https://doi.org/10.1177/0002764213479366 **[checked: sources differ by one page on the range]**
- IEEE. (2023). IEEE Standard for Learning Technology - JavaScript Object Notation (JSON) Data Model Format and Representational State Transfer (RESTful) Web Service for Learner Experience Data Tracking and Access (IEEE Std 9274.1.1-2023). (The xAPI standard) **[checked]**
- Giacumo, L.A., Villachica, S.W., & Stepich, D.A. (2024). Instructional Design for Organizational Justice. Routledge.

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

## Open questions (draft only - remove before release)

1. **Count and naming.** Adding this makes 11 archetypes and 66 dimensions. Every "10 archetypes, 60 dimensions" statement, `TOTAL_ARCHETYPES`, the smoke test, the printable rubric, and the plugin's agent list would change. That is a version bump the author decides.
2. **ADDIE placement.** This sits in Evaluate beside 02 and 06, but runs after Implement in time. The pipeline would need a post-launch entry point as well as a pre-launch one (scoring the measurement plan before release).
3. **Composite and cap rule.** Should 11 enter the composite for a pre-launch build, where only the plan exists? One option: score the plan pre-launch, and score the report as a separate post-launch review.
4. **Overlap with 03.** Archetype 03 has a Transfer & Retention dimension for the design of the instruction. Dimension 5 here covers the workplace and the measurement of transfer. The boundary should be stated in both files.
5. **Trademark check.** "Kirkpatrick" and "Four Levels" are used here by citation and paraphrase only. Confirm that wording against the rights holder's guidance before release, as was done for the crosswalk.
6. **Citations.** Nine references are marked [checked] in the reference list. Verify the rest against their sources before release, and read the cited passages to confirm each one supports the claim in the "Evidence Base by Dimension" table.
7. **Still to build if adopted:** the judge module, edge cases, an owning agent, crosswalk entries, and the generated skill and plugin references.
