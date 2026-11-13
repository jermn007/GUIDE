---
name: evaluate
description: Score an instructional artifact against GUIDE and get a scorecard with evidence, a verdict, and fixes.
disable-model-invocation: true
---

Review an instructional artifact against GUIDE in **evaluate mode**, in this conversation.

1. **Get the artifact.** It is in the request below, attached, or at a file path the request
   names. If there is none, ask the user to paste, attach, or point to it, and wait.
2. **Load the rubrics.** Load this plugin's `framework` skill (through the Skill tool where
   one is available; its full name is `guide-instructional-design:framework`) and follow its "How to use this
   skill" steps in evaluate mode: route to the archetype(s), read each rubric, then run
   `EVALUATE.md` through its "Done when" list. When a rubric tells you to ask something you
   cannot infer (whether a lone quiz item is a sample or the whole test, for example), ask
   once. If the user wants the score now, use the rubric's stated default and say so.
3. **Add the alignment gate when it fits.** When the artifact holds objectives, instruction, and
   assessment together (a full lesson or course), score archetype 10 Curriculum Alignment as well,
   and let its cap rule bound the combined verdict.
4. **Return the scorecard**, one per archetype. When more than one archetype applies, add a short
   combined verdict that leads with the highest-severity findings. Close by offering to rework
   the weakest dimensions (`/build`, which goes straight to the rework when the
   objectives are already set).

For a full multi-agent audit with a revision loop, the user can run `/pipeline` instead.

Artifact or request: $ARGUMENTS
