# Status

What works, what is open, and what is next. Last checked: 2026-09-24, against `main` at v3.4.0 plus unreleased docs changes.

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
| Plugin bundles 1 skill and 13 agents | tested | 13 files in `skill/guide-instructional-design-plugin/agents/`. |
| Plugin installs from the marketplace | verified | Confirmed by hand at v3.2.2 (see the release notes). Not re-checked for v3.4.0. |
| Printable rubric matches the live framework | verified | Brought to parity and re-scored in the [v3.4.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.4.0.md). |

## Open

| Item | Evidence | Notes |
|---|---|---|
| Archetypes 05, 06, and 07 from Python | open | Their judge prompts ask for a flat JSON object, but `GUIDEResult.from_json` reads a `scores` key. Through `evaluate()`, their scores come back empty. The plugin and skill are not affected. |
| Edge-case regression runs | open | `archetypes/edge_cases_XX.json` exist for all 10 archetypes, but no script runs them. |
| Continuous integration | open | No CI workflow. Checks are run by hand. |
| Default judge model | open | The Python runners default to `claude-sonnet-4-20250514`, an older model. Override with `model_name`. |
| Discipline Alignment at 5 | open | Stays at 4 until the standards owners validate the crosswalk. See the [v3.3.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.3.0.md). |

## Next

1. Fix the JSON output format for archetypes 05, 06, and 07, and add a check that every archetype asks for the standard format.
2. Add a script that runs the edge cases against a live model and reports drift from `expected_overall`.
3. Add a CI workflow that runs the registry check and the pipeline smoke test.
