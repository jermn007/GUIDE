# Design mode

Goal: instructional content that would already score 4-5 on the relevant archetype, because the
dimensions were design inputs, not an afterthought.

## Steps

1. **Start with needs analysis (07) unless it is clearly done.** This is the **gatekeeper**:
   confirm a real, ideally data-based performance gap, and that its cause is a skill, knowledge,
   or attitude gap (training helps) rather than an environmental one such as tools, incentives,
   or process (training will not fix it). When the request does not say, ask, one question at a
   time, until the gap and its cause are clear. Then write objectives in Mager format (Behavior +
   Condition + Criterion, with observable verbs). Skipping this is the most common and most
   expensive instructional-design mistake.
2. **Pick the design archetype(s)** for the artifact (03 sequencing, 08 story, 09 neuroscience,
   04 multimedia, 05 accessibility) and read each `references/handoff_NN_*.md`, starting with its
   **Design targets**.
3. **Author against the dimensions**, using them as a checklist of what to include: cover Gagné's
   nine events (03); keep extraneous load down and segment content (04); embed the learning in the
   narrative tension rather than bolting a lesson on (08); sequence Explore before Explain and
   build in spaced retrieval (09); provide alt text, captions, keyboard access, and multiple
   representations (05).
4. **Keep alignment tight.** Objectives, instruction, practice, and assessment must trace to each
   other (Dick & Carey). When you also produce assessments, apply 02: the Bloom level matches the
   objective's verb, distractors are plausible, and coverage is balanced.
5. **Self-evaluate before delivering.** Run an evaluate-mode pass (`EVALUATE.md`) on your own
   draft against the same archetype(s), and fix every dimension that would score below 4. Show
   the user a short "GUIDE self-check" table when the grounding helps them trust the design.

Explain the *why* from the grounding when it helps the user ("segmented into ~15-minute chunks
because sustained attention degrades after 15-20 minutes - Posner & Rothbart"). The point of GUIDE
is that good instruction is defensible, not merely tasteful.

## Done when

- The performance gap and its cause are stated, or the user confirmed analysis was already done.
  If the cause turned out to be environmental and the user chose to stop at the non-training
  recommendation, you are done here.
- Every objective is in Mager format with an observable verb.
- Every objective traces to instruction and practice, and to an assessment item where one exists.
- The self-check shows every dimension of every archetype used at 4 or above, or names the
  remaining gap and why it stays.
