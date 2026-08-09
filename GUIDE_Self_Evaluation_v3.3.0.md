# GUIDE Framework - Self-Evaluation v3.3.0

## v3.2.3 Living Framework vs. v3.3.0, after the Discipline Alignment crosswalk

**Date:** August 9, 2026
**Method:** Each applicable archetype's scoring criteria applied to the framework as a whole, scored as a delta from v3.2.3
**Purpose:** Re-score after adding the IBSTPI / ATD / ISPI-HPT competency crosswalk and per-handoff Professional Alignment blocks - the first change aimed squarely at Archetype 10's Discipline Alignment dimension, which has been the framework's only sub-3 score across every prior self-evaluation

---

## A note on the artifact being evaluated

Same living artifact as prior self-evals, now with one addition:

- `archetypes/handoff_NN_*.md` - 10 model-agnostic rubric handoffs (single source of truth), each now carrying a **Professional alignment** block
- `archetypes/discipline_alignment_crosswalk.md` - **new**: maps all 10 archetypes to IBSTPI (2012), ATD (2020), and ISPI/HPT standards
- `archetypes/archetype_NN_*.py`, `archetypes/edge_cases_NN.json` - judge modules and test suites (unchanged)
- `skill/guide-instructional-design/` - Claude skill + plugin mirror (crosswalk now a registered reference)
- `README.md`, `CLAUDE.md`, `NOTICE` - orientation and attribution

---

## What changed v3.2.3 -> v3.3.0

One themed change, additive only:

1. **Discipline Alignment crosswalk.** A new `discipline_alignment_crosswalk.md` maps each archetype to recognized professional standards - IBSTPI Instructional Designer Competencies (2012), the ATD Talent Development Capability Model (2020), and ISPI/HPT's Ten Standards (with Gilbert's BEM) - at their natural altitudes (IBSTPI for artifact/process fit, ATD for practitioner capability, ISPI/HPT for the front-end and evaluation ends). It is built in a **reference-safe form**: framework names and competency numbers as pointers, GUIDE's own paraphrase, full citations, an independence/licensing notice, and no reproduced verbatim competency text or proprietary figures. It also states GUIDE's **intentional scope boundary** (it does not cover IBSTPI Management, most ATD Domains 1/3, or the design of HPT non-instructional interventions).
2. **Per-handoff Professional Alignment blocks.** Each of the 10 handoffs now carries a compact block naming its IBSTPI/ATD/ISPI-HPT pointers and linking to the crosswalk.

**No dimension definitions, scoring anchors, citations, or judge prompts changed.** The 60 dimensions score artifacts exactly as before. This release adds a discipline-alignment *reference layer*; it does not alter the rubric.

---

## Key finding: the first movement on Discipline Alignment in six self-evaluations

Every prior self-eval (v2.2.0 through v3.2.3) named the same standing gap: Archetype 10 applied to GUIDE scored **2 on Discipline Alignment** because GUIDE mapped to no recognized ID professional competency framework. It was the only sub-3 dimension anywhere in the evaluation and was explicitly deferred to v3.3.

v3.3.0 closes it. GUIDE now publishes an explicit, cited crosswalk to three recognized standards, with per-archetype tags. Discipline Alignment moves **2 -> 4**. It stops at 4, not 5, for honest reasons stated below.

---

## Archetype 10: Curriculum Alignment (Self-Application)

| Dimension | v3.2.3 | v3.3.0 | Delta | Rationale |
|-----------|--------|--------|-------|-----------|
| Objective <-> Strategy Coherence | 4 | 4 | 0 | Additive change; the retrofit unevenness noted in v3.2.3 (07/03/10 restructured around the Three Alignments; 04/05/06/08 carry the framing without being rebuilt around it) is unchanged. Holds. |
| Strategy <-> Assessment Coherence | 4 | 4 | 0 | Edge-case depth still varies across archetypes. Holds. |
| Objective <-> Assessment Coherence | 4 | 4 | 0 | Holds. |
| Coverage Completeness | 5 | 5 | 0 | Held at ceiling; the crosswalk adds the discipline axis without leaving orphans. |
| Vertical Alignment | 4 | 4 | 0 | The crosswalk ladders archetypes to discipline-level competencies (the Discipline dimension), not course-level vertical progression. Holds. |
| Discipline Alignment | **2** | **4** | **+2** | **The gap closes.** GUIDE now maps every archetype to IBSTPI (2012), ATD (2020), and ISPI/HPT standards in a cited, structured crosswalk, and each handoff carries a Professional Alignment tag. Not a 5 because: (a) it is a **self-published** mapping, not accreditation or endorsement by the standards bodies; (b) the reference-safe version uses pointers + paraphrase rather than owner-validated verbatim mappings; (c) it rests on the IBSTPI 2012 edition (a revision is pending) with no permission yet sought. Those are the path from 4 to 5. |

**Archetype 10 Mean: 3.8 -> 4.2 (+0.4)**

---

## Other archetypes: held, no regression

The crosswalk's impact is concentrated in Archetype 10's Discipline Alignment. The other six applicable archetypes score GUIDE-as-artifact on their own dimensions (adult-learning communication quality, assessment quality, multimedia design, etc.), which this additive reference layer does not change:

- **01 Adult Learning (4.5), 02 Assessment (4.7), 03 Sequencing (4.3), 05 Accessibility (4.2), 09 Cognitive Neuroscience (4.0):** held. The Professional Alignment blocks add well-cited pointers (reinforcing Accuracy/Validity, already at or near ceiling) but introduce no new structure that moves a dimension.
- **04 Multimedia (4.2):** held. Multimedia Principle Compliance remains 3 - the framework is still text-only, and the crosswalk adds more prose (cleanly tabled, so no load regression). The visual-model gap persists.

No dimension in any archetype regressed.

---

## COMPOSITE SCORE COMPARISON

| Archetype | v3.1.1 | v3.2.3 | v3.3.0 | v3.2.3 -> v3.3.0 | Priority Status |
|-----------|--------|--------|--------|------------------|-----------------|
| 01 - Adult Learning Communication | 4.5 | 4.5 | 4.5 | 0 | Low |
| 02 - Assessment Design | 4.7 | 4.7 | 4.7 | 0 | Low |
| 03 - Instructional Sequencing | 4.3 | 4.3 | 4.3 | 0 | Low |
| 04 - Multimedia Design | 4.2 | 4.2 | 4.2 | 0 | Low (visual model) |
| 05 - Accessibility | 4.2 | 4.2 | 4.2 | 0 | Low |
| 09 - Cognitive Neuroscience | 4.0 | 4.0 | 4.0 | 0 | Low |
| 10 - Curriculum Alignment | 3.8 | 3.8 | **4.2** | **+0.4** | Low (was Medium) |

**Composite Mean (same 6 archetypes as v3.0.0):** 4.3 -> 4.3 -> **4.3** (0)
**Composite Mean (all 7 applicable archetypes, including 10):** 4.2 -> 4.2 -> **4.3** (+0.1)

The 6-archetype composite is unchanged (the crosswalk doesn't touch those archetypes' dimensions); the 7-archetype composite ticks up as Archetype 10 rises. The meaningful result is not the 0.1 composite move but the **retirement of the only sub-3 dimension in the framework's history**.

---

## REMAINING GAPS (future candidates)

1. **Discipline Alignment 4 -> 5.** Seek written permission from IBSTPI (and, as needed, ATD/ISPI) to publish owner-validated, verbatim mappings; pursue external review/endorsement; refresh to the IBSTPI ID revision when published. This is what separates a self-published crosswalk from an accredited one.
2. **Visual model.** A three-alignments triangle / archetype-to-ADDIE diagram would lift Archetype 04 Dim 1 (Multimedia Principle Compliance, still 3) and Archetype 09 Dim 4 (Emotional Engagement).
3. **Sharpen mid-range criteria for older archetypes (04, 05, 06, 08)** and restructure them around the Three Alignments, to lift Archetype 10's Objective <-> Strategy Coherence from 4 to 5.
4. **Self-assessment exercise** for Archetype 03 Dim 5 and Archetype 09 Dim 1.
5. **Inter-rater reliability study** to move Archetype 02 Dim 5 from 4 to 5.

---

## SUMMARY

v3.3.0 is an additive, themed release: a cited crosswalk from all ten archetypes to IBSTPI (2012), ATD (2020), and ISPI/HPT, plus per-handoff Professional Alignment tags, built in a reference-safe form that references frameworks by name and number without reproducing their proprietary text.

The result is the first movement on **Discipline Alignment** since the framework began scoring itself - **2 -> 4** - which raises Archetype 10's mean from 3.8 to 4.2 and the full 7-archetype composite from 4.2 to 4.3. No other dimension moved and none regressed, because the change is a reference layer around the rubric, not an edit to it.

The dimension stops at 4 by design: a self-published crosswalk is a real, defensible discipline anchor, but it is not accreditation. Reaching 5 means securing the standards owners' permission for validated, verbatim mappings and, ideally, external endorsement. For the first time, the framework's lowest score is a 4, and the path to close the remaining point is concrete.
