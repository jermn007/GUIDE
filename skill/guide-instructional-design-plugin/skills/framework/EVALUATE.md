# Evaluate mode

Goal: a defensible, theory-grounded scorecard the user can act on. A rubric that never
discriminates is useless, so give low scores where the evidence calls for them.

## Steps

1. **Read the rubric(s)** for every archetype that applies (`references/handoff_NN_*.md`), in full.
2. **Score each dimension against its anchor.** For each of the six dimensions, find concrete
   evidence in the artifact, quote or point to it, and assign the 1-5 score whose anchor that
   evidence matches ("the third slide narrates and duplicates the same text on-screen" means
   Extraneous Load Reduction = 2, a redundancy violation).
3. **Compute the overall** with the archetype's own rule: the mean of the six unless the handoff
   says otherwise (01 weights Accuracy & Grounding and Adult Learning Alignment most heavily; 10
   caps the overall at 3.0 when Objective-Assessment Coherence is 1 or 2).
4. **Raise severity flags** for every critical issue the handoff names (hallucination, no
   assessment, inaccessible to screen readers, training recommended for an environmental problem,
   and so on). The list sits under "Severity Flags", "Red Flags", or "Common Pitfalls to Flag",
   depending on the handoff. Also flag anything outside the list that scores a dimension at 1
   or would exclude, mislead, or fail learners. Use Nielsen severity framing
   (cosmetic / minor / major / catastrophic) for the archetypes the index lists under Nielsen
   severity ratings.
5. **Give improvement suggestions**: 1-3 concrete next steps for each dimension under 4, drawn
   from the handoff's Improvement Suggestions section where it has one, otherwise from what
   the next anchor up describes.
6. **State the verdict** by mapping the overall to the threshold bands in
   `references/00_archetype_index.md` (ship / light revision / revise / redesign).

## Output

Default to the scorecard a person can use: a per-dimension table (score plus a one- or
two-sentence rationale citing the evidence), the overall and verdict, severity flags, and
improvement suggestions. When the user wants machine-readable output or is wiring GUIDE into a
pipeline, return the exact object from the handoff's **Output JSON** section instead. When
several archetypes apply, give one scorecard per archetype and a short combined verdict.

## When scoring is hard

- **No source or context to check accuracy against?** Score Accuracy & Grounding conservatively
  and say why.
- **Linear artifact under a branching dimension?** Score the embedded decision-making instead
  (see 08).
- **One quiz item or a short excerpt instead of a whole test?** Follow "Scoring a single item or
  a short sample" in 02: the instrument-level dimensions are capped, not failed.
- **Two dimensions feel alike?** Re-read both definitions in the handoff's dimension table and
  score each piece of evidence under the dimension whose anchor names it. Handoffs 02, 04, and
  10 also have a troubleshooting table for the common mix-ups.

## Done when

- Every dimension has a score, and every score cites specific evidence from the artifact, or names
  what the artifact is missing (no blueprint, no answer key, no objectives).
- Every dimension under 4 has at least one concrete fix.
- Every severity condition the handoff lists was checked, and each one present is flagged, as is
  every dimension scored 1.
- The overall follows the archetype's own rule, and the verdict matches the threshold band.
