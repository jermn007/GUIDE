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
| Listed in Anthropic's Claude directory | verified | Approved and live since 2026-11-09 (v3.4.1 at `1f4c436`), in Claude Code, Cowork, and the Claude apps. The listing tracks `main`. The plugin icon is still waiting for its own review. |

## Open

| Item | Evidence | Notes |
|---|---|---|
| Edge-case regression runs | open | `archetypes/edge_cases_XX.json` exist for all 10 archetypes, but no script runs them. |
| Printable rubric matches the live framework | open | Brought to parity in v3.4.0, checked by hand. v3.5.0 carries archetype 02's new Bloom's Alignment anchors and corrects the archetype and dimension counts, but the [v3.5.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.5.0.md) found drift: the new 02 guidance on samples, test type, and answer keys, some 01 and 03 anchor text, and an archetype 10 column in the coverage matrix are missing. No automated check compares the two. |
| Continuous integration | open | No CI workflow. Checks are run by hand. |
| Plugin commands run end to end | open | `/guide-review`, `/guide-design`, and `/guide-pipeline` pass `claude plugin validate`, and their instructions were followed by hand in a dry run. No live run in Claude Code yet. How Claude chat treats typed-only skills is not documented. |
| Default judge model | open | The Python runners default to `claude-sonnet-4-20250514`, an older model. Override with `model_name`. |
| Discipline Alignment at 5 | open | Stays at 4 until the standards owners validate the crosswalk. See the [v3.3.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.3.0.md). |

## Next

1. Add a script that runs the edge cases against a live model and reports drift from `expected_overall`.
2. Add a CI workflow that runs the registry check, the output-format check, and the pipeline smoke test.
