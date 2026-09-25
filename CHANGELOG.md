# Changelog

All notable changes to GUIDE are listed here, newest first. Dates are GitHub release dates. Each release also has notes and downloads on the [Releases page](https://github.com/jermn007/GUIDE/releases).

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
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

[Unreleased]: https://github.com/jermn007/GUIDE/compare/v3.4.0...HEAD
[3.4.0]: https://github.com/jermn007/GUIDE/compare/v3.3.0...v3.4.0
[3.3.0]: https://github.com/jermn007/GUIDE/compare/v3.2.2...v3.3.0
[3.2.2]: https://github.com/jermn007/GUIDE/compare/v3.2.1...v3.2.2
[3.2.1]: https://github.com/jermn007/GUIDE/compare/v3.2.0...v3.2.1
[3.2.0]: https://github.com/jermn007/GUIDE/compare/v3.1.2...v3.2.0
[3.1.2]: https://github.com/jermn007/GUIDE/releases/tag/v3.1.2
