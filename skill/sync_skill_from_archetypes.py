"""Regenerate the skill's reference files from the canonical archetypes/ directory.

Canonical sources of truth:
- archetypes/handoff_0X_*.md         (rubric content)
- skill/guide-instructional-design/  (canonical skill tree: SKILL.md, package.json,
                                      references/00_archetype_index.md, references/NOTICE.md)

This script:
1. Reads each archetypes/handoff_*.md, applies two normalizations
   (quote the <1-5> JSON placeholders so the snippet is parseable; drop the
   stray duplicate closing fence in the example JSON block), then appends a
   Source footer stamped with GUIDE_VERSION.
2. Writes the result to skill/guide-instructional-design/references/.
3. Mirrors the entire canonical skill tree into
   skill/guide-instructional-design-plugin/skills/guide-instructional-design/
   so the plugin always ships an exact copy of the skill.

Run from the repo root:
    python skill/sync_skill_from_archetypes.py
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

GUIDE_VERSION = "3.0.1"
COPYRIGHT_YEAR = "2026"
COPYRIGHT_HOLDER = "Jeremy Terhune"

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHETYPES_DIR = REPO_ROOT / "archetypes"
SKILL_DIR = REPO_ROOT / "skill" / "guide-instructional-design"
PLUGIN_SKILL_DIR = (
    REPO_ROOT
    / "skill"
    / "guide-instructional-design-plugin"
    / "skills"
    / "guide-instructional-design"
)
REFERENCES_DIR = SKILL_DIR / "references"


def transform_handoff(source_text: str, archetype_num: int) -> str:
    text = re.sub(r":\s*<(1-5)>", r': "<\1>"', source_text)
    text = re.sub(r"```\s*\n```\s*\n", "```\n", text)
    text = text.rstrip() + "\n"
    footer = (
        f"\n---\n\n"
        f"*Source: GUIDE — Grounded Universal Instructional Design Evaluator "
        f"(v{GUIDE_VERSION}). Copyright {COPYRIGHT_YEAR} {COPYRIGHT_HOLDER}. "
        f"Licensed under the Apache License, Version 2.0. "
        f"Archetype {archetype_num:02d} of 9.*\n"
    )
    return text + footer


def sync_references() -> list[Path]:
    written: list[Path] = []
    pattern = re.compile(r"handoff_(\d{2})_.+\.md$")
    for src in sorted(ARCHETYPES_DIR.glob("handoff_*.md")):
        m = pattern.search(src.name)
        if not m:
            continue
        n = int(m.group(1))
        dst = REFERENCES_DIR / src.name
        dst.write_text(transform_handoff(src.read_text(encoding="utf-8"), n), encoding="utf-8")
        written.append(dst)
    return written


def mirror_skill_to_plugin() -> None:
    if PLUGIN_SKILL_DIR.exists():
        shutil.rmtree(PLUGIN_SKILL_DIR)
    shutil.copytree(SKILL_DIR, PLUGIN_SKILL_DIR)


def main() -> None:
    if not ARCHETYPES_DIR.is_dir():
        raise SystemExit(f"Cannot find archetypes dir: {ARCHETYPES_DIR}")
    if not REFERENCES_DIR.is_dir():
        raise SystemExit(f"Cannot find references dir: {REFERENCES_DIR}")
    written = sync_references()
    mirror_skill_to_plugin()
    print(f"Synced {len(written)} handoff reference(s) at GUIDE v{GUIDE_VERSION}.")
    print(f"Mirrored {SKILL_DIR.name}/ -> plugin skills/{SKILL_DIR.name}/.")


if __name__ == "__main__":
    main()
