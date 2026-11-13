# Changelog

All notable changes to GUIDE are listed here, newest first. Dates are GitHub release dates. Each release also has notes and downloads on the [Releases page](https://github.com/jermn007/GUIDE/releases).

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [3.5.0] - 2026-11-12

### Added
- Archetype 02 (Assessment Design): guidance for scoring a single item or a short sample. Four dimensions score normally; Validity Evidence and Reliability Considerations are capped at 3 for a sample, and the item-count and coverage flags do not apply. An artifact presented as the complete assessment still meets the full thresholds.
- Archetype 02: a rule for telling criterion-referenced from norm-referenced tests (cut score or mastery criterion versus percentiles, ranks, or a curve), with criterion-referenced as the stated default when the artifact does not say.
- Archetype 02: a "Missing or Wrong Answer Key" severity flag, and a cap of 2 on Reliability Considerations when there is no answer key or scoring guide.
- [v3.5.0 self-evaluation](self-evaluations/GUIDE_Self_Evaluation_v3.5.0.md), scored against the updated rubrics.
- `docs/build_rubric_docx.py` regenerates the ten archetype sections of `GUIDE_Rubric_Document.docx` from the handoffs, so the printable rubric cannot drift from the rubrics. It also rebuilds the table of contents, adds an archetype 10 column to the coverage matrix, marks every table's header row, and gives the figure alt text. `--check` fails when the file is stale.
- `docs/practice.md`: three score-then-compare exercises (a quiz, a slide, a training request) with GUIDE's scores and reasoning, and a review schedule for one day, three days, and one week later. The printable rubric carries it as a closing section.
- Three diagrams, drawn as SVG: the archetypes across ADDIE, the five steps of a review with the four verdict bands, and archetype 10's links and cap rule. They appear in the README and the printable rubric with full alt text. `docs/art/render_diagrams.py` rasterizes them for the docx.
- `run_edge_cases.py` checks every edge-case file without a model, and with `--live` scores each case with a judge and reports drift from the expected overall. `--backend cli` scores through the signed-in Claude Code CLI, so no API key is needed, and `--report` saves the results.
- Live runs of all 68 edge cases on two models, each case scored once per model: [Sonnet](self-evaluations/edge_case_run_v3.5.0.json), 66 within tolerance (mean absolute drift 0.36), and [Opus](self-evaluations/edge_case_run_v3.5.0_opus.json), 62 (0.39). Tolerance is 0.7, or one full point for the ten archetype 01 cases that expect only a whole-number overall. The first Sonnet run had 62; six cases were then corrected. No case drifts on both models.
- Four edge cases for archetype 02's new rules: a single-item sample, a keyless quiz on one objective, a recall quiz for recall objectives, and a short norm-referenced placement test.
- Severity flag lists for archetypes 05 (Accessibility) and 06 (Formative Evaluation), in the handoffs and the Python judges. Every rubric now names the conditions to flag.
- Archetype 02: the item-count minimum applies to an instrument covering a module or unit. A check on one narrow objective is judged on whether its items exhaust the objective.
- Handoff 09: reference entries for Bjork (1994), Craik and Lockhart (1972), Kosslyn et al. (2006), Shepard and Metzler (1971), and Yerkes and Dodson (1908), which were cited in the text without one.
- Every handoff opens with a short "When this is skipped" scenario: an illustrative case of what goes wrong for a learner when the archetype is ignored, and who should care. The skill references and the printable rubric carry them.
- `.github/workflows/checks.yml` runs the offline checks on every pull request and push to `main`: judge and handoff keys, edge-case files, the pipeline smoke test, generated skill references, and the printable rubric's freshness. No model calls and no secrets.
- Three plugin commands: `/guide-review` scores an artifact, `/guide-design` starts with a needs-analysis interview before designing, and `/guide-pipeline` runs the 13-agent pipeline with the main conversation as orchestrator. They are user-invoked skills (`disable-model-invocation: true`), so they add nothing to Claude's context until typed. Before, the pipeline started only from phrasing, and its router agent had no way to spawn the other agents.
- `EVALUATE.md` and `DESIGN.md` in the skill. `SKILL.md` now routes to one of them, so each run reads only the procedure for its mode, and each ends on a checkable "Done when" list (every score cites evidence, every dimension under 4 has a fix).
- `build_skill.py` checks that each specialist agent's output contract uses the same dimension keys as its handoff, and `test_judge_schemas.py` checks that each handoff's output JSON matches its Python judge.
- Plugin README: a Commands section and an "It's working if" section.
- `STATUS.md` records a live run of each command in Claude Code on 2026-11-12, including the pipeline's needs-analysis stop, fail-fast gate, and one revision round, and on 2026-11-13 two full builds, each in a single headless run; the second used all 13 agents.
- Zenodo DOI: a DOI badge and citation in the README, and the concept DOI ([10.5281/zenodo.22949871](https://doi.org/10.5281/zenodo.22949871)) in `CITATION.cff`. v3.4.1 is archived as [10.5281/zenodo.22949872](https://doi.org/10.5281/zenodo.22949872).
- Plugin `README.md`, in preparation for listing GUIDE in Anthropic's Claude directory. The directory requires a README of at least 40 words in the plugin folder and shows it as the listing's description. It says what each archetype is for, which parts load in Claude chat versus Cowork and Claude Code, and that the plugin runs and sends nothing.
- Plugin `displayName` ("GUIDE Instructional Design") in `plugin.json`.
- Plugin icon at `.claude-plugin/icon.png`: the three-alignments mark from the README hero, 1024 by 1024 px. `docs/art/icon.py` draws it in code, so it carries the same Apache-2.0 license as the rest of the repo.
- `PRIVACY.md`: the plugin and skill collect, store, and send nothing, and the Python judges send your content only to the services you choose, with your own key.
- Directory listing links in `plugin.json`: `documentationUrl` (the README), `supportUrl` (GitHub issues), `privacyPolicyUrl` (`PRIVACY.md`), and `termsOfServiceUrl` (the Apache License 2.0).

### Changed
- Archetype 02's Bloom's Alignment anchors now score the match between each item and its objective, not how high the items reach. Before, a recall quiz for a recall objective could not score above 2. The Python judge (`assessment_design`, now v1.1.0), the assessment agent, and the printable rubric carry the same change.
- `/guide-pipeline` gives every agent the absolute path of the rubric folder. The agents name their rubrics relative to the plugin, which they could not resolve from the user's project.
- `EVALUATE.md` says where each handoff keeps its severity list (Severity Flags, Red Flags, or Common Pitfalls to Flag) and what to flag for the two handoffs that have none (05 and 06).
- `GUIDE_Rubric_Document.docx`: the archetype sections are now the handoffs' own text, so they carry every anchor, flag, and note in the rubrics. The document grew from about 60 pages to about 92, including the practice section and figures.
- Archetype 04: the Extraneous Load Reduction and Generative Processing Support anchors no longer overlap between adjacent scores.
- Archetypes 05 and 06 use GUIDE's four score bands in their interpretation tables. Handoffs 01, 02, and 04 quote the same four bands in their calibration notes.
- The "Grounded in" column in the README and the theorist column in the archetype index list only sources each rubric cites. Removed: Rossett, Gilbert, Reigeluth and van Merrienboer (from 03), Vogler, Harmon, Kandel, Sousa, Medina, Paivio, Section 508, Webb and Messick (from 02), Scriven, Kirkpatrick, and Stufflebeam.
- Handoff 09 presents the 10-20 minute attention segment as a design rule of thumb, drops the claim that no other judge covers cognitive neuroscience, and cites Dunlosky et al. (2013) in its example where it cited a source it did not list.
- The three-alignments diagram's source line is darker (it was 2.45:1 against its background; it is now about 7:1), and the PNG is re-rendered from the SVG.
- The archetype index no longer opens with a "What's new in v3.1.0" block.
- Archetype 02: Objective Congruence scores the item mapping when objective quality and mapping disagree, and the Coverage Gaps flag can be judged from the objectives when there is no blueprint.
- Archetype 10: Strategy-Assessment Coherence is scored on its own. When instruction and assessment agree with each other but both miss the objective, that dimension stays high and the miss is scored on the two objective links. Before, a judge lowered all three for one fault. The Python judge is now v1.0.1.
- Archetype 08: a linear case study is not by itself a 1 on Decision Points & Branching Quality. The score-1 anchor said "linear story only" while the note under it said to score the characters' decisions; the anchor now agrees with the note. The Python judge is now v1.1.1.
- Six edge cases that drifted in the first live run are settled. `edge_cases_02` good_01 is rewritten as a quiz that earns its label (it had a keyed answer that needed no calculation on a "calculate" objective, untagged items, and half its stated objective untested), and good_02 loses an overlapping score band. The expected scores of `edge_cases_08` good_02 and bad_02, `edge_cases_09` borderline_01, and `edge_cases_10` bad_01 are corrected against the anchors.
- The discipline alignment crosswalk and handoff 10 say plainly that the crosswalk is GUIDE's own discipline-level mapping. When archetype 10 scores another course, Discipline Alignment looks for that course's own competency framework. The crosswalk's coverage notes are corrected to match its table.
- The Python runners default to `claude-sonnet-5-5`. They defaulted to an older model.
- `/guide-pipeline` tells the orchestrator to put an agent's earlier output in the prompt whenever it sends that agent back to revise. In the first full headless build, an agent sent only the fix invented part of its earlier work; a second build confirmed the fix. It also says to re-run a Design specialist whose flags a fail-fast fix removed, after that build left archetype 09 out of its composite.
- The synthesizer's verdict is held to its four values; in a live run it had returned a fifth. `/guide-pipeline` now states the fail-fast, cap, and verdict rules in the prompts of the gate, synthesizer, and reviser, because an agent could read the rubrics but not `PIPELINE.md`.
- `/guide-pipeline` stops when needs analysis finds training is the wrong fix, passes the reviser and synthesizer the inputs their contracts require, and skips the fail-fast gate in review runs. `PIPELINE.md` and the router and gate agents now name the main conversation as the orchestrator.
- Threshold bands in the archetype index state their lower bounds, so an overall such as 4.47 has a band.
- `STATUS.md`: the Claude directory listing is live (published 2026-11-09).
- The skill's `references/handoff_*.md` are now a **skill edition**, about a fifth smaller. `build_skill.py` drops the sections that serve only the Python judge harness (the judge system prompt, the human prompt template, input-format, calibration, pipeline-integration, and version-history notes) and keeps the JSON output shape as an "Output JSON" section. The complete handoffs in `archetypes/` are unchanged for use with other models and the Python API.
- Scoring guidance that appeared only in a judge prompt is now also in the kept sections of the handoffs: 01's overall weighting and its output JSON, 03's output JSON and "events may be reordered" rule, and small anchor details in 02, 06, 08, 09, and 10.
- Plugin `description` in `plugin.json` uses a colon instead of an em dash.
- `guide-router.md` and `PIPELINE.md` no longer put the agent name guide-formative-eval in inline code, and the pipeline diagram's code block is marked as `text`. The directory's validator read the inline name as a shell `eval` command and warned of a download-and-execute risk. The plugin runs no commands.
- README hero: the title, the three-alignments mark, and the subtitle are about 10% larger.
- README hero: the mark's dots now match the three-alignments diagram (effective in blue at the top, efficient in green at bottom left, engaging in amber at bottom right). Green and amber were swapped.
- README fact badges now open matching content: archetypes goes to the archetype table, dimensions to the list of all 60 dimensions, and the ADDIE pipeline badge to `PIPELINE.md`. Before, they opened the badge image.

### Fixed
- The printable rubric's worked calibration example gave archetype 01 a plain-mean overall of 3.7, against the rubric's own rule. It now shows the weighted 3.6 and says why. Its back-matter reference list gains thirteen works that the archetype sections and the crosswalk cite, and the Dolcos year is corrected there too.
- `GUIDE_Rubric_Document.docx` said "nine archetypes" and "54 evaluation dimensions" in three places. It now says ten and 60.
- Handoff 09 dated Dolcos, LaBar, and Cabeza's *Neuron* paper 2005. It is 2004.
- The agent list in the READMEs and manifests counted the curriculum-alignment gate apart from the 10 specialists, which summed to 14. The gate is one of the 10; there are 13 agents.
- `EVALUATE.md` pointed to a troubleshooting table that handoff 01 does not have.
- Two edge cases stated an overall that was not the mean of their own scores (`edge_cases_02` borderline_01: 3.2, now 3.5; `edge_cases_03` borderline_01: 3.7, now 4.5). The new edge-case check found them.
- The printable rubric's reader objectives promised judge prompts the document does not contain. The objective now points to the repository.

## [3.4.1] - 2026-09-24

### Fixed
- Archetypes 05 (Accessibility), 06 (Formative Evaluation), and 07 (Needs Analysis) asked the judge for a flat JSON object instead of the standard `scores` / `rationale` / `severity_flags` / `improvement_suggestions` format, so their results came back empty through the Python API. Their prompts and handoffs now use the standard format (prompt version 1.1.0). The plugin and skill were not affected.

### Added
- `test_judge_schemas.py`, which checks that every archetype asks for the standard output format.
- `CHANGELOG.md` (this file), backfilled from the GitHub release notes.
- `STATUS.md`: what works, what is open, and what is next, with each item marked verified, tested, or open.
- `CITATION.cff`, which turns on the **Cite this repository** button on GitHub.
- A README hero image in light and dark versions, drawn in code from `docs/art/hero.html`.

### Changed
- Self-evaluation reports moved into `self-evaluations/`. The v3 comparison report is renamed `GUIDE_Self_Evaluation_v3.0.0.md`.
- Every Python file now carries the Apache-2.0 header. Seven modules still had a stale "Proprietary" header from v2.1.0.
- README rewritten for first-time users: badges, numbered install steps, a quick start, and developer material in collapsible sections.

## [3.4.0] - 2026-08-11

### Added
- The three-alignments diagram (Effective, Efficient, Engaging), in the README and the printable rubric.
- A **Design targets** block for each archetype in `GUIDE_Rubric_Document.docx`.

### Changed
- `GUIDE_Rubric_Document.docx` brought back to parity with the live framework: dual-mode note, discipline crosswalk, and an alphabetized References list.
- The professional-standards mapping is now described as aspirational: the standards GUIDE aims to align with, not reviewed or endorsed by IBSTPI, ATD, or ISPI.

No dimension definitions or scoring anchors changed. Self-evaluation composite: 4.0 to 4.4.

## [3.3.0] - 2026-08-09

### Added
- `archetypes/discipline_alignment_crosswalk.md`: maps all 10 archetypes to IBSTPI (2012), the ATD Talent Development Capability Model (2020), and ISPI/HPT's Ten Standards.
- A Professional alignment block in each handoff.

### Changed
- Includes the v3.2.3 changes, which were merged but never released on their own:
  - Every handoff leads with both modes (design and evaluate) and gains a Design targets block.
  - `SKILL.md` and `NOTICE` corrected from "9 archetypes / 54 dimensions" to "10 / 60."
  - Archetype 10's two run modes documented (fail-fast pre-check and full acceptance gate).

Archetype 10 Discipline Alignment rose from 2 to 4 in the self-evaluation.

## [3.2.2] - 2026-06-22

### Fixed
- `plugin.json` declared `repository` as an object, so v3.2.1 failed to install. It is now a string.

## [3.2.1] - 2026-06-22

### Added
- Plugin marketplace (`.claude-plugin/marketplace.json`) so installs receive updates.

## [3.2.0] - 2026-06-21

### Added
- A 13-agent ADDIE pipeline in the plugin: a router, 10 archetype specialists, the curriculum-alignment gate, a synthesizer, and a reviser.
- `guide_pipeline.py` (`ADDIEPipeline`) for batch evaluation, with a mocked end-to-end test in `smoke_test_pipeline.py`.
- `skill/build_skill.py`: `archetypes/handoff_*.md` is now the single source of truth for the skill and plugin.

### Fixed
- Pipeline archetype identifiers now match the registry.
- Smoke test output on Windows (UTF-8).

## [3.1.2] - 2026-05-25

First public release as an installable Claude skill and plugin.

### Added
- Archetype 10, Curriculum Alignment: the synthesis archetype that checks whether objectives, strategies, and assessments agree (introduced in v3.1.0).
- Effective, Efficient, Engaging as the top-level quality outcomes, with Keller's ARCS for engagement (v3.0.2 to v3.0.3).
- Claude skill and plugin packaging (v3.0.1).

### Fixed
- The `SKILL.md` description exceeded the 1024-character limit, which stopped the skill from loading.
- Citations: the three quality outcomes are credited to Merrill (2002), and the alignment mapping to Hirumi, Ratliff and de la Mora (2021) and Hirumi (2025) (v3.1.1).

[Unreleased]: https://github.com/jermn007/GUIDE/compare/v3.5.0...HEAD
[3.5.0]: https://github.com/jermn007/GUIDE/compare/v3.4.1...v3.5.0
[3.4.1]: https://github.com/jermn007/GUIDE/compare/v3.4.0...v3.4.1
[3.4.0]: https://github.com/jermn007/GUIDE/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/jermn007/GUIDE/compare/v3.2.2...v3.3.0
[3.2.2]: https://github.com/jermn007/GUIDE/compare/v3.2.1...v3.2.2
[3.2.1]: https://github.com/jermn007/GUIDE/compare/v3.2.0...v3.2.1
[3.2.0]: https://github.com/jermn007/GUIDE/compare/v3.1.2...v3.2.0
[3.1.2]: https://github.com/jermn007/GUIDE/releases/tag/v3.1.2
