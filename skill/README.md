# GUIDE — Claude Skill & Plugin

This folder packages [GUIDE](../) as a [Claude skill](https://docs.claude.com/en/docs/claude-code/skills) and an installable Claude Code plugin. The skill exposes GUIDE's 10 archetypes and 60 dimensions as reference-driven workflows for **designing** instructional content and **evaluating** existing artifacts.

Version: **3.1.2** (tracks the GUIDE framework version one-to-one).

## Contents

```
skill/
├── README.md                              # this file
├── sync_skill_from_archetypes.py          # regenerates references/ from ../archetypes/
├── guide-instructional-design/            # canonical skill source
│   ├── SKILL.md                           # router + design/evaluate workflows
│   ├── package.json                       # skill metadata
│   └── references/
│       ├── 00_archetype_index.md          # routing index
│       ├── NOTICE.md                      # Apache-2.0 attribution
│       └── handoff_01..10_*.md            # the 10 archetype rubrics
└── guide-instructional-design-plugin/     # plugin wrapper (mirrors the skill)
    ├── .claude-plugin/plugin.json
    └── skills/guide-instructional-design/ # exact mirror of ../guide-instructional-design/
```

The plugin's `skills/guide-instructional-design/` directory is a generated mirror — do not edit it by hand. Edit `guide-instructional-design/` and run the sync script.

## Install

### Option A — Plugin (recommended for Claude Code users)

Build a `.plugin` zip and install it via Claude Code:

```bash
# from the repo root
cd skill/guide-instructional-design-plugin
zip -r ../guide-instructional-design.plugin .
cd ../..
```

Then in Claude Code:

```
/plugin install ./skill/guide-instructional-design.plugin
```

### Option B — Skill only

If you want just the skill (no plugin wrapper), drop the `guide-instructional-design/` folder into your skills directory:

- **User-level:** `~/.claude/skills/guide-instructional-design/`
- **Project-level:** `.claude/skills/guide-instructional-design/`

```bash
cp -r skill/guide-instructional-design ~/.claude/skills/
```

Or build a `.skill` zip for upload to Claude.ai / API skill stores:

```bash
cd skill
zip -r guide-instructional-design.skill guide-instructional-design
```

## Use

Once installed, the skill self-activates on instructional-design intents. Trigger phrases include: *course*, *training*, *lesson*, *module*, *learning objectives*, *quiz*, *rubric*, *assessment*, *e-learning*, *storyboard*, *needs analysis*, *accessibility (WCAG/UDL)*, or any of the named theorists (Bloom, Gagné, Mayer, Knowles, Sweller, Mager, Keller/ARCS, etc.).

It runs in two modes:

- **Design mode** — "write/build/design X" → author content with the relevant archetype's dimensions as forward-looking criteria, then self-check.
- **Evaluate mode** — "review/score/audit/critique X" → return a structured per-dimension scorecard with rationale, severity flags, and improvement suggestions.

The router in `SKILL.md` picks 1–3 archetypes per artifact. See `references/00_archetype_index.md` for the artifact→archetype map.

## Updating the references

The 9 `references/handoff_0X_*.md` files are derived from the canonical rubrics in [`../archetypes/`](../archetypes/). Whenever those change, regenerate:

```bash
python skill/sync_skill_from_archetypes.py
```

The script (a) copies each archetype handoff into `references/`, (b) normalizes the JSON-snippet placeholders, (c) appends the GUIDE source/version footer, and (d) mirrors the entire canonical skill into the plugin's `skills/` directory so the two stay byte-identical.

`SKILL.md`, `package.json`, `references/00_archetype_index.md`, and `references/NOTICE.md` are skill-specific and edited directly in `guide-instructional-design/`; the sync script will mirror them into the plugin.

## Versioning

Skill and plugin versions track the GUIDE framework version (currently 3.1.2). When bumping GUIDE:

1. Update `GUIDE_VERSION` in `sync_skill_from_archetypes.py`.
2. Update `version` and `claudeSkill.frameworkVersion` in `guide-instructional-design/package.json`.
3. Update `version` in `guide-instructional-design-plugin/.claude-plugin/plugin.json`.
4. Update the version strings in `SKILL.md`, `references/00_archetype_index.md`, and `references/NOTICE.md`.
5. Run `python skill/sync_skill_from_archetypes.py` to regenerate handoff footers and mirror the plugin.

## Build artifacts

`*.skill` and `*.plugin` zip artifacts are gitignored. Attach them to GitHub Releases rather than committing the binaries.

## License & attribution

Apache License 2.0 — see [`../LICENSE`](../LICENSE) and `guide-instructional-design/references/NOTICE.md`. Copyright 2026 Jeremy Terhune.
