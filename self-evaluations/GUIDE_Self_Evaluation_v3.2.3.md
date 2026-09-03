# GUIDE Framework - Self-Evaluation v3.2.3

## v3.1.1 Living Framework vs. v3.2.3, after the dual-mode reframe and the archetype-count correction

**Date:** August 8, 2026
**Method:** Each applicable archetype's scoring criteria applied to the framework as a whole, scored as a delta from v3.1.1
**Purpose:** Re-score after (a) the dual-mode "design and evaluate" reframe reached the rubric layer and (b) the SKILL.md / NOTICE.md archetype-count correction (9 archetypes / 54 dimensions -> 10 / 60)

---

## A note on the artifact being evaluated

This evaluation targets the same living artifact the v3.1.1 self-eval scored, not the frozen `GUIDE_Rubric_Document.docx`:

- `archetypes/handoff_NN_*.md` - 10 model-agnostic rubric handoffs (the single source of truth)
- `archetypes/archetype_NN_*.py` - 10 LLM judge prompt modules
- `archetypes/edge_cases_NN.json` - 10 labeled test suites
- `skill/guide-instructional-design/` - Claude skill (`SKILL.md`, `references/00_archetype_index.md`, bundled handoffs) and its plugin mirror
- `README.md`, `CLAUDE.md`, `NOTICE` - top-level orientation and attribution

---

## What changed v3.1.1 -> v3.2.3

Four releases moved the framework between the v3.1.1 self-eval and this one. Only the last changed rubric-layer content, which is why this is the first self-eval since v3.1.1:

1. **v3.2.0** - Packaged GUIDE for the plugin marketplace (auto-updating installs). Packaging only.
2. **v3.2.1** - Fixed `plugin.json` (`repository` must be a string). Packaging only.
3. **v3.2.2** - Reframed the root and skill READMEs (and the portfolio/profile surfaces) to lead with GUIDE's dual nature - design *and* evaluate - rather than evaluation alone. Documentation only; no dimension, anchor, or judge-prompt content changed, so no self-eval was run.
4. **v3.2.3** - Carried the dual-mode framing into the rubric layer and corrected a scope-count defect:
   - Each handoff's `Purpose` / `Overview` opening now leads "Design and evaluate ..." and states explicitly that its dimensions work in both directions (author against them, or score against them). No dimension definition, scoring anchor, citation, or judge prompt was altered.
   - **`SKILL.md` and `NOTICE.md` corrected from "9 archetypes / 54 dimensions" to "10 / 60."** The skill has bundled `handoff_10` (Curriculum Alignment) and routed to it via `00_archetype_index.md` since v3.1.0, but the skill's own frontmatter, intro, archetype table, and reference list still advertised the pre-v3.1.0 count. `SKILL.md` now lists archetype 10 and describes it as the synthesis gate.

---

## Key finding: v3.2.3 closes a coherence gap v3.1.1 could not see in itself

The v3.1.1 self-eval awarded **Objective Congruence (Archetype 02) a 5** and **Objective <-> Strategy Coherence (Archetype 10) a 4**, both partly on the claim that "the README, SKILL.md frontmatter, and routing index now state the same objectives in matching language."

That claim was not actually true. `SKILL.md` said *9 archetypes / 54 dimensions* while `00_archetype_index.md` (shipped in the same skill) said *10 / 60*. The skill's stated scope disagreed with its delivered assets - precisely the objective-to-strategy incoherence Archetype 10 exists to catch. v3.1.1 scored the coherence dimensions as if the surfaces agreed; they did not.

This is a clean piece of dogfooding: **run against GUIDE, Archetype 10's own criteria would have flagged the mismatch that the component archetypes missed.** v3.2.3 resolves it. The scores below are therefore not "inflation from new features" - several are corrections that make a previously over-credited score genuinely earned.

---

## Archetype 01: Adult Learning Communication

| Dimension | v3.1.1 | v3.2.3 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Adult Learning Alignment | 5 | 5 | 0 | Held at ceiling. |
| Cognitive Load Management | 4 | 4 | 0 | The dual-mode `Purpose` lines add one clause per handoff; the design/evaluate split is now an explicit advance organizer rather than an inference. Net neutral on load. |
| Instructional Clarity & Signaling | 5 | 5 | 0 | Held at ceiling. Each handoff now signals its two modes up front. |
| Accuracy & Grounding | 5 | 5 | 0 | Held, but now genuinely earned: the "9 archetypes" claim in `SKILL.md`/`NOTICE.md` was an internal inaccuracy against the 10 bundled handoffs. That inaccuracy is corrected. |
| Accessibility & Inclusive | 4 | 4 | 0 | No change to representation modes. |
| Personalization & Engagement | 4 | 4 | 0 | Holds. |

**Archetype 01 Mean: 4.5 -> 4.5 (0)**

---

## Archetype 02: Assessment Design

| Dimension | v3.1.1 | v3.2.3 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Bloom's Alignment | 5 | 5 | 0 | Held at ceiling. |
| Objective Congruence | 5 | 5 | 0 | **Correction, not inflation.** v3.1.1 credited matching scope language across README, SKILL, and index; the SKILL/index counts actually disagreed (9/54 vs 10/60). v3.2.3 makes every surface state 10/60, so the 5 is now real. |
| Item Construction Quality | 4 | 4 | 0 | Older archetypes still carry some vague mid-range descriptors. Holds. |
| Validity Evidence | 5 | 5 | 0 | Held at ceiling. |
| Reliability Considerations | 4 | 4 | 0 | Still no inter-rater study. Holds. |
| Inclusivity & Fairness | 5 | 5 | 0 | Held at ceiling. |

**Archetype 02 Mean: 4.7 -> 4.7 (0)**

---

## Archetype 04: Multimedia Design

| Dimension | v3.1.1 | v3.2.3 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Multimedia Principle Compliance | 3 | 3 | 0 | Still text-only. The three-alignments triangle / ADDIE diagram remains unbuilt - carried to v3.3. |
| Extraneous Load Reduction | 5 | 5 | 0 | Held. Build script still guarantees no canonical/plugin drift (re-verified this release). |
| Intrinsic Load Management | 5 | 5 | 0 | Held at ceiling. |
| Generative Processing | 4 | 4 | 0 | Holds. |
| Interactivity & Learner Control | 4 | 4 | 0 | The design/evaluate toggle is now stated in every handoff, not just `SKILL.md`, but it is the same mechanism made explicit - not new interactivity. Holds at 4. |
| Visual Design & Information Architecture | 4 | 4 | 0 | Holds. |

**Archetype 04 Mean: 4.2 -> 4.2 (0)**

---

## Archetypes 03, 05, 09: held, no regression

No dimension in Instructional Sequencing (4.3), Accessibility (4.2), or Cognitive Neuroscience (4.0) is moved by this release. The dual-mode `Purpose` reframe reinforces the design/evaluate duality these archetypes' v3.1.1 gains already credited (e.g., 03 Scaffolding, 09 Memory Systems), but adds no new structure, so each holds at its v3.1.1 value. The visual-model and self-assessment-exercise gaps that cap 04 Dim 1, 09 Dim 4, and 03 Dim 5 are unchanged.

---

## Archetype 10: Curriculum Alignment (Self-Application)

| Dimension | v3.1.1 | v3.2.3 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Objective <-> Strategy Coherence | 4 | 4 | 0 | The concrete count-incoherence (stated 9 vs delivered 10) is resolved, and the design/evaluate objective is now represented in every strategy artifact (each handoff), not just the router. Held at 4 rather than raised because the deeper retrofit unevenness remains: archetypes 07/03/10 were restructured around the Three Alignments, while 04/05/06/08 carry the framing without being rebuilt around it. |
| Strategy <-> Assessment Coherence | 4 | 4 | 0 | Edge-case depth still varies across archetypes. Holds. |
| Objective <-> Assessment Coherence | 4 | 4 | 0 | Holds. |
| Coverage Completeness | 5 | 5 | 0 | Held at ceiling. Every archetype has handoff + module + edge cases; the count correction removes the one place the skill under-represented its own coverage. |
| Vertical Alignment | 4 | 4 | 0 | Holds. |
| Discipline Alignment | 2 | 2 | 0 | **Unchanged real gap.** GUIDE still maps to no recognized ID competency framework (IBSTPI, ATD, QM). This remains the framework's lowest score and is slated for v3.3. |

**Archetype 10 Mean: 3.8 -> 3.8 (0)**

**Severity Flag (carried forward):** No discipline-level alignment to recognized ID professional competency frameworks. This is the largest single gap and anchors v3.3 planning.

---

## COMPOSITE SCORE COMPARISON

| Archetype | v3.0.0 | v3.1.1 | v3.2.3 | v3.1.1 -> v3.2.3 | Priority Status |
|-----------|--------|--------|--------|------------------|-----------------|
| 01 - Adult Learning Communication | 4.3 | 4.5 | 4.5 | 0 | Low |
| 02 - Assessment Design | 4.2 | 4.7 | 4.7 | 0 | Low |
| 03 - Instructional Sequencing | 4.0 | 4.3 | 4.3 | 0 | Low |
| 04 - Multimedia Design | 3.8 | 4.2 | 4.2 | 0 | Low |
| 05 - Accessibility | 4.0 | 4.2 | 4.2 | 0 | Low |
| 09 - Cognitive Neuroscience | 3.5 | 4.0 | 4.0 | 0 | Low |
| 10 - Curriculum Alignment | N/A | 3.8 | 3.8 | 0 | **Medium** (Discipline Alignment) |

**Composite Mean (same 6 archetypes as v3.0.0):** 4.0 -> 4.3 -> **4.3** (0)
**Composite Mean (all 7 applicable archetypes, including 10):** **4.2** (0)

Scores are stable by design: v3.2.3 changed framing and corrected a count, not dimension content. The value of the release is a resolved internal-coherence defect and honest scope representation, neither of which the composite is sensitive to - which is itself the correct outcome for a framing/consistency release.

---

## REMAINING GAPS (v3.3 candidates)

Carried forward from v3.1.1, unchanged by v3.2.3:

1. **Discipline Alignment (Archetype 10, score 2).** Map each GUIDE archetype to relevant IBSTPI, ATD, or QM competencies. Still the single highest-leverage improvement available - the only dimension scoring below 3 in the entire 7-archetype self-eval.
2. **Visual model.** A three-alignments triangle / archetype-to-ADDIE diagram would lift Archetype 04 Dim 1 (Multimedia Principle Compliance) and Archetype 09 Dim 4 (Emotional Engagement).
3. **Sharpen mid-range criteria for older archetypes (04, 05, 06, 08).** Apply archetype 10's concrete-anchor treatment to remaining vague mid-range descriptors.
4. **Self-assessment exercise.** A structured "score this artifact, then compare" exercise against an edge case, for Archetype 03 Dim 5 and Archetype 09 Dim 1.
5. **Inter-rater reliability study.** Two raters, agreement statistics, to move Archetype 02 Dim 5 from 4 to 5.

---

## SUMMARY

v3.2.3 improved the framework without regressions and without inflating scores. Its two changes were a framing pass (each handoff now leads "Design and evaluate" and states its dimensions work in both directions) and a correction (`SKILL.md` / `NOTICE.md` now say 10 archetypes / 60 dimensions, matching the assets the skill has bundled since v3.1.0).

The most useful finding is again from Archetype 10 applied to GUIDE itself. v3.1.1 had scored two coherence dimensions partly on the belief that the skill's scope language matched across surfaces; it did not (9/54 vs 10/60). v3.2.3 makes that belief true. The framework's own synthesis lens would have caught the mismatch its component lenses missed - the same claim v3.1.1 made about Archetype 10's value, confirmed once more with GUIDE as the artifact.

The standing priority is unchanged: Discipline Alignment (2/5) is the only sub-3 dimension in the self-evaluation, and closing it - a competency-framework crosswalk - is the anchor for v3.3.
