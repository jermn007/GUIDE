---
name: guide-design
description: Design new instruction with GUIDE, starting from a needs analysis that checks whether training is the right fix.
disable-model-invocation: true
---

Design instructional content with GUIDE in **design mode**, in this conversation.

1. **Load the rubrics.** Load the `guide-instructional-design` skill (through the Skill tool where
   one is available; in Claude Code its full name is
   `guide-instructional-design:guide-instructional-design`) and read its `DESIGN.md` and
   `references/handoff_07_needs_analysis.md`. The archetype index can wait until step 4.
2. **Run the gatekeeper interview** before designing anything. Ask one question at a time. Give
   each one your recommended answer or, for facts only the user has, your working assumption and
   how to check it. Continue until you can state:
   - the performance gap (current versus desired performance, with any data behind it),
   - its cause, and whether training can fix it (a skill, knowledge, or attitude gap) or the fix
     lies elsewhere (tools, incentives, process),
   - the learners and the context the instruction must fit.
   Skip any question the request or attached material already answers. When the cause is wholly
   or mainly environmental, say so plainly, recommend the non-training fix, and ask whether to
   stop there or design training for the remaining skill gap only.
3. **Write the objectives** in Mager format (Behavior + Condition + Criterion) and confirm them
   with the user. When the user already has objectives and wants a rework of an existing
   artifact, confirm the objectives and go straight to step 4.
4. **Design the artifact** by following `DESIGN.md` from step 2 through its "Done when" list,
   including the self-check against every archetype you used.

Request: $ARGUMENTS
