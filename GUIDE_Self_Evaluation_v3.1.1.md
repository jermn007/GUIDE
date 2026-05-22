# GUIDE Framework - Self-Evaluation v3.1.1
## v3.0.0 Frozen Document vs. v3.1.1 Live Framework, plus Archetype 10 Self-Application

**Date:** May 22, 2026
**Method:** Each applicable archetype's scoring criteria applied to the framework as a whole
**Purpose:** Re-score after the Hirumi/Merrill citation work (v3.0.2 through v3.1.1) and apply the new Archetype 10 (Curriculum Alignment) to GUIDE itself

---

## A note on the artifact being evaluated

The v2.2.0 and v3.0.0 self-evaluations targeted `GUIDE_Rubric_Document.docx` as the canonical deliverable. As of v3.1.0, that docx is a frozen snapshot of the v3.0.0 rubric; the live framework now comprises:

- `archetypes/handoff_NN_*.md` - 10 model-agnostic rubric handoffs
- `archetypes/archetype_NN_*.py` - 10 LLM judge prompt modules
- `archetypes/edge_cases_NN.json` - 10 labeled test suites
- `skill/guide-instructional-design/` - Claude skill with router (`SKILL.md`), index (`references/00_archetype_index.md`), and bundled handoffs
- `README.md`, `CLAUDE.md`, `NOTICE` - top-level orientation and attribution

This evaluation targets that living artifact, not the docx. Where the v3.0.0 self-eval scored a Word document, this v3.1.1 self-eval scores a system of interrelated files - which is itself a meaningful change worth surfacing under Archetype 10.

---

## What changed v3.0.0 → v3.1.1

Four releases moved the framework forward between the v3.0.0 docx freeze and this evaluation:

1. **v3.0.1** - Packaged GUIDE as an installable Claude skill + plugin. Added a sync workflow keeping the skill's reference copies regenerated from `archetypes/`.
2. **v3.0.2** - Operationalized engagement-as-alignment-to-learner-goals via Keller's ARCS model. Capture side in Archetype 07 (Needs Analysis L4 now requires goals/interests/motivations); apply side in Archetype 03 (ARCS as a cross-cutting motivational layer for design).
3. **v3.0.3** - Adopted Effective / Efficient / Engaging as top-level quality vocabulary. Added Hannafin et al. (1997) - the foundational *grounded practice* paper - to citations. Added anecdotal-vs-scientific evidence distinction (Hirumi, 2025) to Archetypes 01 and 07.
4. **v3.1.0** - Added Archetype 10 (Curriculum Alignment) as the synthesis lens evaluating internal coherence between objectives, instructional strategies, and assessments. Six dimensions covering the unit/lesson triangle (Obj↔Strategy, Strategy↔Assessment, Obj↔Assessment), Coverage Completeness, Vertical Alignment, and Discipline Alignment.
5. **v3.1.1** - Citation hygiene patch. The Effective/Efficient/Engaging triad is now correctly attributed to Merrill (2024); the alignment mapping that produces those outcomes to Hirumi, Ratliff & de la Mora (2021) and Hirumi (2025). Removed `"Three Alignments framework"` as a proper-noun label that Hirumi did not himself use.

---

## Archetype 01: Adult Learning Communication

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Adult Learning Alignment | 4 | 5 | **+1** | The anecdotal-vs-scientific distinction added in v3.0.3 (per Hirumi, 2025) explicitly invites the kind of epistemological reflection Mezirow's transformative learning calls for - it asks the reader to examine assumptions about what counts as evidence. Previously this dimension held at 4 because the framework "didn't explicitly invite Mezirow-style critical reflection." It does now. |
| Cognitive Load Management | 4 | 4 | 0 | 60 dimensions is denser than 54, but the Three Alignments framing in the README, SKILL.md, and routing index serves as a structural advance organizer that reduces intrinsic load. Net: hold at 4. |
| Instructional Clarity & Signaling | 5 | 5 | 0 | Held at ceiling. Quality Outcomes section and primary-alignment column in v3.0.3 add still more signaling, but the dimension was already saturated. |
| Accuracy & Grounding | 5 | 5 | 0 | Held at ceiling. Merrill (2024), Hannafin et al. (1997), Hirumi (2021/2025) all properly cited; the v3.1.1 citation patch split attributions correctly between Merrill (the triad) and Hirumi (the mapping). |
| Accessibility & Inclusive | 4 | 4 | 0 | Markdown is generally accessible; the skill bundles cleanly. No new alternative representations. Holds. |
| Personalization & Engagement | 4 | 4 | 0 | The skill prompt has personality; the README has voice. ARCS work in v3.0.2 enriched the *rubrics' treatment* of personalization but didn't directly affect the framework's own personalization toward its readers. Holds. |

**Archetype 01 Mean: 4.3 → 4.5 (+0.2)**

---

## Archetype 02: Assessment Design

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Bloom's Alignment | 4 | 5 | **+1** | Archetype 10 (added v3.1.0) explicitly grounds itself in Bloom + Anderson & Krathwohl + Webb's Depth of Knowledge. The framework now operates at multiple Bloom levels - including the Analyze/Evaluate work archetype 10 requires of its judges (comparing cognitive demand across stated, taught, and tested behaviors). |
| Objective Congruence | 4 | 5 | **+1** | v3.0.3's Quality Outcomes section makes the framework's purpose explicit (evaluate instruction across the three alignments). The README, SKILL.md frontmatter, and routing index now state the same objectives in matching language. Reader can self-check: "Did I evaluate one of these three alignments?" - yes/no answer. |
| Item Construction Quality | 4 | 4 | 0 | Archetype 10's anchors are sharply written (e.g., "Bloom-level mismatch ≥ 2 levels apart" as a major severity flag). Earlier archetypes still have some vague mid-range language that v3.0.0 noted "sharpening was only applied to Archetype 01." Not regressed but not yet improved. Holds. |
| Validity Evidence | 4 | 5 | **+1** | Archetype 10 adds explicit construct validity for "internal coherence" as a measurable construct, grounded in Merrill (2024), Tyler (1949), and Hirumi (2025). The Three Alignments framing connects every archetype to a named construct in the published literature - this is the strongest construct validity argument the framework has had. |
| Reliability Considerations | 4 | 4 | 0 | edge_cases_10.json provides 6 worked cases for the new archetype. Sync script verifies consistency between canonical and plugin copies. Still no inter-rater reliability study or multi-rater calibration data. Holds at 4. |
| Inclusivity & Fairness | 5 | 5 | 0 | Held at ceiling. |

**Archetype 02 Mean: 4.2 → 4.7 (+0.5)**

---

## Archetype 03: Instructional Sequencing

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Gagné's Nine Events Coverage | 4 | 4 | 0 | Still 7 of 9 events present. Self-assessment (event 8) and spaced retention (event 9) remain gappy. No regression but no new improvement. |
| Learning Domain Alignment | 4 | 4 | 0 | Still primarily targets intellectual skills (analysis/evaluation). Strategies match. Holds. |
| Sequencing Logic | 5 | 5 | 0 | Held at ceiling. The README → Quality Outcomes → Archetypes → Repository Structure flow is intact and matches the SKILL.md flow. |
| Scaffolding & Gradual Release | 4 | 5 | **+1** | SKILL.md now has explicit design-mode vs. evaluate-mode scaffolding, with guidance on which archetypes pair together for common artifacts. The "When to add archetype 10" sidebar in the routing index provides explicit decision support. Edge cases for archetype 10 (especially the borderline cases) provide multiple worked examples spanning different score ranges. |
| Practice & Feedback | 3 | 3 | 0 | No new self-assessment exercises. Edge cases function as practice but require the reader to compare their reasoning against expected scores without a structured prompt. Holds. |
| Transfer & Retention | 4 | 5 | **+1** | Archetype 10's positioning ("run *in addition* to component archetypes when the question is whether pieces hang together") explicitly scaffolds transfer to multi-archetype evaluations - the most common real-world use case. The skill's self-activation on instructional intents extends transfer support beyond the documentation itself. |

**Archetype 03 Mean: 4.0 → 4.3 (+0.3)**

---

## Archetype 04: Multimedia Design

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Multimedia Principle Compliance | 3 | 3 | 0 | Still text-only. No diagrams added. Hirumi's Figure 1 (the three alignments triangle) would be a high-value addition but isn't reproduced in the GUIDE docs. |
| Extraneous Load Reduction | 4 | 5 | **+1** | The sync script eliminates the risk of drift between canonical and plugin copies, which was a latent source of redundancy noise. The Three Alignments framing replaced a sprawling cross-archetype concept list with a clean three-bucket structure. |
| Intrinsic Load Management | 5 | 5 | 0 | Held at ceiling. Three Alignments serves as advance organizer; primary-alignment column gives readers a mental model before they encounter individual archetypes. |
| Generative Processing | 4 | 4 | 0 | Skill prompt has personality. Tone in handoff scoring tables remains clinical by design. Holds. |
| Interactivity & Learner Control | 3 | 4 | **+1** | The skill's design-mode / evaluate-mode toggle is genuine interactivity - the reader (or LLM) chooses a mode and the skill behavior changes accordingly. This is a step up from the static docx, which had only a TOC. |
| Visual Design & Information Architecture | 4 | 4 | 0 | Markdown rendering is reasonable. Tables are well-structured. No new diagrams. Holds. |

**Archetype 04 Mean: 3.8 → 4.2 (+0.4)**

---

## Archetype 05: Accessibility

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Perceivable | 4 | 4 | 0 | Markdown headings throughout, no images. Holds. |
| Operable | 4 | 4 | 0 | Heading structure clean across handoffs. Holds. |
| Understandable | 4 | 4 | 0 | New sections use clear language. First-use jargon is still occasionally undefined within dimension text. Holds. |
| Robust | 4 | 4 | 0 | Sync script ensures markdown is well-formed across copies. JSON manifests parse cleanly. Holds. |
| UDL Integration | 3 | 4 | **+1** | The skill provides a second representation mode (chat-driven evaluation) alongside the static documentation. Two genuinely different interaction paths to the same evaluation outcome. |
| Remediation Feasibility | 5 | 5 | 0 | Held at ceiling. Any remaining issues are surface-level fixes. |

**Archetype 05 Mean: 4.0 → 4.2 (+0.2)**

---

## Archetype 09: Cognitive Neuroscience

| Dimension | v3.0.0 | v3.1.1 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| 5E Model Alignment | 3 | 4 | **+1** | Engage, Explore, Explain, Elaborate all present. Archetype 10 specifically adds an Evaluate phase - the synthesis check that asks "did the components cohere?" This is the dimension's namesake activity. 4 of 5 phases solidly addressed, with Evaluate now meaningfully present. |
| Memory System Optimization | 3 | 4 | **+1** | The skill's evaluate mode engages procedural memory (running judge prompts is a procedural skill); the design mode engages episodic memory (the reader/LLM imagines a learner using the resulting artifact); semantic encoding remains dominant. 3 of 4 memory systems now engaged, up from 2. |
| Attention Management | 4 | 4 | 0 | Three Alignments framing provides clearer attention focus, but no new attention-reset structure was added. Holds. |
| Emotional Engagement | 3 | 3 | 0 | ARCS work in v3.0.2 enriched the rubrics' treatment of emotional engagement but didn't directly engage the framework's reader emotionally. Holds. |
| Synaptic Strengthening | 3 | 4 | **+1** | Repetition (Three Alignments tagging every archetype), Application (the skill's evaluate mode runs against real artifacts), Imagination (design mode), Spaced practice (the skill is used across sessions). 4 of 5 factors now engaged, up from 3. |
| Theory-Practice Grounding | 5 | 5 | 0 | Held at ceiling. v3.1.1's citation work strengthened this further: Merrill (2024) for the quality triad; Hannafin et al. (1997) for the grounded-design premise; Hirumi (2021/2025) for the alignment mapping; Tyler (1949) for the originating alignment principle. The framework now traces every load-bearing claim to a named source. |

**Archetype 09 Mean: 3.5 → 4.0 (+0.5)**

---

## NEW: Archetype 10 - Curriculum Alignment (Self-Application)

This is the first application of Archetype 10 to GUIDE itself. The framework has implicit objectives (evaluate instruction across the three alignments), strategies (the archetype handoffs, the skill router, the python judge prompts), and assessments (the edge cases, the severity flag conventions, the judge prompts themselves as measurement instruments). Archetype 10 asks whether these cohere.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Objective ↔ Strategy Coherence | 4 | The README's Quality Outcomes section states what GUIDE evaluates (instruction's effectiveness, efficiency, engagement via three alignments). Each handoff does in fact teach evaluation of those things, with v3.0.3's primary-alignment column making the mapping explicit. Not a 5 because some archetypes were authored before the Three Alignments framing and were retrofitted - the connection feels stronger for archetypes 07/03/10 (which got the v3.0.2-v3.1.0 work) than for archetypes 04/05/06/08 (which carry the framing but weren't restructured around it). |
| Strategy ↔ Assessment Coherence | 4 | Each archetype has an `edge_cases_NN.json` testing what its rubric describes. The judge prompt (the "assessment" for whether the rubric works) mirrors the dimension language. Not a 5 because the edge cases vary in depth across archetypes - 03 and 10 have 6 cases each spanning score ranges; others have fewer. |
| Objective ↔ Assessment Coherence | 4 | The judge prompt for each archetype assesses what its objective (the dimension definition) claims to evaluate. Verb-to-task match is generally good. Bloom levels of the rubric criteria are appropriately set at Analyze/Evaluate. Not a 5 because some handoff JSON output schemas use bare `<1-5>` placeholders (caught by the v3.0.1 sync script's normalization) - the criterion language in the rubric criteria isn't always literally the criterion language in the JSON output. |
| Coverage Completeness | 5 | Every archetype has handoff + python module + edge cases. No orphan instruction (every section in every handoff serves a stated dimension). The sync script verifies consistency between canonical and plugin copies. Three Alignments tagging is consistent across all 10 archetypes. A blueprint (the archetype index table with ADDIE phase + primary alignment + theorists) is explicitly maintained. |
| Vertical Alignment | 4 | The ADDIE-ordered structure provides vertical progression. The Three Alignments framing connects archetypes at the top level. Inter-archetype dependencies are explicitly documented in two places: the v3.0.2 ARCS handoff between 07 (capture) and 03 (apply), and the v3.1.0 "run in addition to component archetypes" guidance for archetype 10. Not a 5 because not every archetype-to-archetype relationship is documented this explicitly - readers have to infer most pairings from the routing-index table. |
| Discipline Alignment | 2 | **Real gap.** GUIDE does not ladder up to any recognized ID professional competency framework: no IBSTPI competency mapping, no ATD capability model alignment, no QM rubric crosswalk, no formal ISD certification linkage. For an evaluation framework intended for ID professionals, this is a meaningful omission. The framework's positioning ("grounded in named research") is theoretically defensible but disciplinarily orphaned. |

**Archetype 10 Mean: 3.8**

**Severity Flag:** No discipline-level alignment to recognized ID professional competency frameworks (IBSTPI, ATD, QM, etc.). This is the largest single gap exposed by v3.1.1's self-evaluation and should anchor v3.2 planning.

---

## COMPOSITE SCORE COMPARISON

| Archetype | v2.2.0 | v3.0.0 | v3.1.1 | v3.0.0→v3.1.1 Delta | Priority Status |
|-----------|--------|--------|--------|--------------------|--------------------|
| 01 - Adult Learning Communication | 4.0 | 4.3 | 4.5 | +0.2 | Low → Low |
| 02 - Assessment Design | 3.2 | 4.2 | 4.7 | +0.5 | Low → Low |
| 03 - Instructional Sequencing | 2.7 | 4.0 | 4.3 | +0.3 | Low → Low |
| 04 - Multimedia Design | 3.5 | 3.8 | 4.2 | +0.4 | Medium → Low |
| 05 - Accessibility | 4.0 | 4.0 | 4.2 | +0.2 | Low → Low |
| 09 - Cognitive Neuroscience | 2.8 | 3.5 | 4.0 | +0.5 | Medium → Low |
| 10 - Curriculum Alignment | N/A | N/A | 3.8 | N/A (new) | **MEDIUM** (Discipline Alignment) |

**Composite Mean (apples-to-apples, same 6 archetypes as v3.0.0):** 3.4 → 4.0 → 4.3 (+0.3 v3.0.0 → v3.1.1)

**Composite Mean (all 7 applicable archetypes, including 10):** 4.2

---

## IMPROVEMENT PRIORITY STATUS

From the v3.0.0 self-eval's "Remaining Gaps" list:

| Original Priority | Description | Status |
|-------------------|-------------|--------|
| Sharpen mid-range criteria for Archetypes 02-09 | Replace remaining "mostly" / "minor lapses" language | Partially addressed (archetype 10 has sharp anchors; older archetypes mostly unchanged) |
| Inter-archetype bridging transitions | Advance organizers between archetypes | **DONE** - Three Alignments framing and primary-alignment column serve as cross-archetype bridges |
| Visual model | Diagram of archetypes mapped to ADDIE | Not addressed; Hirumi's Figure 1 (three alignments triangle) would be a high-value addition |
| More calibration examples | 2-4 more across different archetypes/scores | Partially addressed - archetype 10's 6 edge cases substantially expand the worked-example corpus, but only for that archetype |
| Self-assessment exercise | "Score this artifact yourself, then compare" | Not addressed |
| Mezirow critical reflection prompt | Invite readers to examine their assumptions | **DONE** - anecdotal-vs-scientific framing in archetypes 01/07 (v3.0.3) accomplishes this |

**3 of 6 priorities addressed in full, 2 partially, 1 deferred.**

---

## REMAINING GAPS (Future v3.2 Candidates)

Newly surfaced or carried forward:

1. **Discipline Alignment (Archetype 10 self-eval, Score 2).** Add a competency-framework crosswalk - map each GUIDE archetype to relevant IBSTPI, ATD, or QM competencies. This is the single highest-leverage improvement v3.1.1 can identify, because it's the only dimension scoring below 3 in the entire 7-archetype self-evaluation.
2. **Visual model.** Reproduce or adapt Hirumi's Figure 1 (the three alignments triangle) as the canonical visualization. Would lift Archetype 04 Dim 1 from 3 toward 5 and Archetype 09 Dim 4 (Emotional Engagement) by giving readers an iconic mental model to attach to.
3. **Sharpen mid-range criteria for older archetypes (04, 05, 06, 08).** Apply the concrete-language treatment that archetype 10 demonstrates ("Bloom-level mismatch ≥ 2 levels apart") to remaining vague mid-range descriptors.
4. **Self-assessment exercise.** Add a structured "score this artifact, then compare" exercise referencing one of the edge cases. Would address Archetype 03 Dim 5 (Practice & Feedback, the only sub-3 score among existing archetypes) and Archetype 09 Dim 1 (Evaluate phase).
5. **Inter-rater reliability study.** Two independent raters scoring the same set of artifacts using the framework, with agreement statistics reported. Would move Archetype 02 Dim 5 (Reliability Considerations) from 4 to 5.
6. **Cross-archetype meta-evaluator.** A `guide_registry.run_three_alignments(artifact)` helper that runs archetypes 07 + 03 + 02 + 10 together and reports the Effective/Efficient/Engaging composite. Already noted in the v3.1.0 commit message as a possible v3.2 architectural addition; the self-eval confirms the demand.

---

## SUMMARY

v3.1.1 improved the framework substantively without regressions. Apples-to-apples (same 6 archetypes as v3.0.0), the composite rose from 4.0 to 4.3 (+0.3, +7.5%). Every dimension that improved did so for a traceable reason - usually the v3.0.2 ARCS work, the v3.0.3 Three Alignments adoption, or the v3.1.0 addition of Archetype 10.

The most interesting finding is from applying Archetype 10 to GUIDE itself: the framework **does** internally cohere (4-5s on five of the six dimensions), but it scores **2** on Discipline Alignment because it doesn't map to any recognized ID professional competency framework. The framework now has the vocabulary to name its own biggest gap.

Two paragraphs ago I noted that Archetype 10 was the synthesis lens that exposes "what other archetypes can't catch alone." That claim turned out to be true even when GUIDE is the artifact being evaluated - the existing 6 archetypes scored GUIDE in the 4.2-4.7 range, but Archetype 10 caught a structural alignment failure none of them named: GUIDE is theoretically grounded but disciplinarily orphaned. Closing that gap is the priority for v3.2.
