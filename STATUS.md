# Status

What works, what is open, and what is next. Last checked: 2026-11-13, at v3.5.0.

Each item is marked by its evidence:

- **verified:** a person checked it by hand.
- **tested:** an automated check passes, but no one has looked by hand.
- **open:** not done, or not confirmed.

## What works

| Item | Evidence | Notes |
|---|---|---|
| 10 archetypes register and load | tested | `python guide_registry.py` lists 10. |
| 60 dimensions (6 per archetype) | tested | Counted from each archetype's scoring schema. |
| ADDIE pipeline orchestrator (`ADDIEPipeline`) | tested | `python smoke_test_pipeline.py` passes all scenarios. It uses a mocked model, not live API calls. |
| All 10 archetypes ask for the standard output format | tested | `python test_judge_schemas.py` parses each archetype's JSON template with `GUIDEResult.from_json`. Fixed for 05, 06, and 07 in v3.4.1. It checks the format, not live judge output. |
| Plugin bundles the GUIDE skill, 3 commands, and 13 agents | tested | 4 folders in `skill/guide-instructional-design-plugin/skills/` and 13 files in `agents/`. `python skill/build_skill.py` fails if an agent's score keys drift from its rubric. |
| Releases are archived on Zenodo with a DOI | verified | Starting with v3.4.1 ([record 22949872](https://zenodo.org/records/22949872)). The concept DOI [10.5281/zenodo.22949871](https://doi.org/10.5281/zenodo.22949871) resolves to the latest version. |
| Plugin and marketplace manifests are well-formed | tested | `claude plugin validate` passes on the plugin folder and the repository root (Claude Code 2.1.226). With `--strict`, 2.1.226 fails on the four directory listing URL fields, which it does not know yet. The manifest docs say v2.1.281 and later accept them. |
| Plugin installs from the marketplace | verified | Confirmed by hand at v3.2.2 (see the release notes). Not re-checked for v3.4.0. |
| Printable rubric matches the rubrics | tested | `python docs/build_rubric_docx.py` regenerates the ten archetype sections of `GUIDE_Rubric_Document.docx` from `archetypes/handoff_*.md`, and `--check` fails when the file is older than its sources. The front and back matter are still written by hand. |
| Edge-case files are well-formed | tested | `python run_edge_cases.py` checks all 68 cases: each names its judge's six dimensions, scores are whole numbers 1 to 5, and a stated overall agrees with its own scores. |
| Plugin commands run in Claude Code | verified | Run live on 2026-11-12 from a local build (Claude Code 2.1.226). `/guide-review` scored a single quiz item with the sample rule. `/guide-design` opened with the cause question instead of a course. `/guide-pipeline` reviewed a micro-lesson: router, five specialists in one batch, the alignment gate, and the synthesizer all returned valid JSON and read their rubrics from the path the command gave them. |
| Pipeline gates and revision loop run live | verified | Run on 2026-11-12. Needs-analysis stop: a course request whose cause was a tool change halted before Design. Fail-fast gate: a lecture proposed for a hands-on objective was blocked at `objective_strategy_coherence` 1, the sequencing agent redesigned it, and the re-check passed. Revision loop: the synthesizer returned `revise` at a capped 3.0, the reviser routed work to the assessment and sequencing agents, and the second round scored 4.89 with the cap released. All 11 agent calls returned valid JSON. |
| Printable rubric works with a screen reader | verified | The author read `GUIDE_Rubric_Document.docx` with NVDA on 2026-11-12 and found no problems. No second screen reader has been tried. The figures carry alt text and every table marks its header row. |
| Edge cases scored by a live judge, on two models | tested | `python run_edge_cases.py --live --backend cli`, each case scored once per model. Sonnet: 66 of 68 within 0.7 of the expected overall, mean absolute drift 0.36 (archetypes 02, 08, 09 and 10 re-scored on 2026-11-13 after the corrections below; the rest from 2026-11-12). Opus, all 68 on 2026-11-13: 62 of 68, mean absolute drift 0.39. The two models' overalls differ by 0.20 on average, and no case drifts on both. Both score about 0.25 below the expected scores on average. Results: [`edge_case_run_v3.5.0.json`](self-evaluations/edge_case_run_v3.5.0.json) and [`edge_case_run_v3.5.0_opus.json`](self-evaluations/edge_case_run_v3.5.0_opus.json). |
| Six drifting edge cases settled | tested | The six cases that drifted in the first run were each decided: two artifacts in `edge_cases_02` were rewritten to earn their "good" label, four expected-score sets were corrected against the anchors, and the anchors for 08 Decision Points and 10 Strategy-Assessment Coherence were sharpened. All six are within tolerance on both models. |
| One full build in a single headless run | verified | Run on 2026-11-13 with `--model sonnet`: a barista micro-lesson built end to end in 20 minutes and 18 agent calls. Route, needs analysis (training confirmed), the Design pair, the fail-fast gate (proceed at 5), the Develop pair in design mode, the Evaluate pair, the acceptance gate, the synthesizer (`light_revision`, 4.16), the reviser, one revision round, and a second gate and synthesizer (`light_revision`, 4.39). Every call returned valid JSON, every agent read its rubric, and the synthesizer's verdict stayed within its four values. The router planned no conversational layer or scenario, so the adult-learning and story agents did not run in design mode. |
| Continuous integration | tested | `.github/workflows/checks.yml` runs the offline checks on pull requests and pushes to `main`. It makes no model calls. |
| Listed in Anthropic's Claude directory | verified | Approved and live since 2026-11-09 (v3.4.1 at `1f4c436`), in Claude Code, Cowork, and the Claude apps. The listing tracks `main`. The plugin icon is still waiting for its own review. |

## Open

| Item | Evidence | Notes |
|---|---|---|
| Revision prompts carry the agent's earlier output | open | In the full build, a revised agent was sent only the fix and invented part of its earlier output. `/guide-pipeline` now tells the orchestrator to include the earlier output in full. Not yet re-run live. How Claude chat treats typed-only skills is not documented. |
| Edge cases near the tolerance line | open | Eight cases drift on one model and not the other, by 0.72 to 1.53 (Sonnet: `08_borderline_02`, 10 `bad_03`; Opus: 02 `borderline_01`, `borderline_02`, `borderline_03`, 06 `good_02`, 07 `bad_01`, `08_good_01`). That is judge variance at one run per case, not a settled disagreement. Scoring each case several times would separate the two. |
| Discipline Alignment at 5 | open | Stays at 4 until the standards owners validate the crosswalk. See the [v3.3.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.3.0.md). |

## Next

1. Score each edge case several times per model, so run-to-run variance can be told apart from a wrong expected score.
2. Run a build that includes a conversational layer and a scenario, so the adult-learning and story agents run in design mode, and confirm the revision-prompt fix.
3. A second screen reader and a keyboard-only pass on the printable rubric.
