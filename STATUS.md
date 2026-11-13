# Status

What works, what is open, and what is next. Last checked: 2026-11-12, at v3.5.0.

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
| Printable rubric works with a screen reader | verified | The author read `GUIDE_Rubric_Document.docx` with NVDA on 2026-11-12 and found no problems. No second screen reader has been tried. The figures carry alt text and every table marks its header row. |
| Edge cases scored by a live judge | tested | Run on 2026-11-12 with `python run_edge_cases.py --live --backend cli --model sonnet`: 62 of 68 cases within 0.7 of the expected overall, mean absolute drift 0.43, no errors. The judge scores about 0.3 lower than the expected scores on average and never ranks a bad case above a good one. Results are in [`self-evaluations/edge_case_run_v3.5.0.json`](self-evaluations/edge_case_run_v3.5.0.json). Each case was scored once, by one model. |
| Listed in Anthropic's Claude directory | verified | Approved and live since 2026-11-09 (v3.4.1 at `1f4c436`), in Claude Code, Cowork, and the Claude apps. The listing tracks `main`. The plugin icon is still waiting for its own review. |

## Open

| Item | Evidence | Notes |
|---|---|---|
| Continuous integration | open | No CI workflow. Checks are run by hand. |
| Six edge cases drift from their expected scores | open | `edge_cases_02` good_01 and good_02, `edge_cases_08` good_02 and bad_02, `edge_cases_09` borderline_01, and `edge_cases_10` bad_01 scored 0.8 to 1.8 lower than expected. In at least one (02 good_01) the judge found real flaws the expected scores overlook. Each needs a decision: correct the expected scores or sharpen the anchor. |
| Pipeline build path and revision loop, live | open | The live `/guide-pipeline` run was a review that ended in redesign, so the needs-analysis stop, the fail-fast gate, and the reviser loop have not run live. How Claude chat treats typed-only skills is not documented. |
| Default judge model | open | The Python runners default to `claude-sonnet-4-20250514`, an older model. Override with `model_name`. |
| Discipline Alignment at 5 | open | Stays at 4 until the standards owners validate the crosswalk. See the [v3.3.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.3.0.md). |

## Next

1. Review the six edge cases that drift from their expected scores, and re-run the edge cases with a second model.
2. Add a CI workflow that runs the registry check, the output-format check, the edge-case check, the pipeline smoke test, and `docs/build_rubric_docx.py --check`.
