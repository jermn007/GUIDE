"""Generate the skill's handoff references from the canonical archetypes/ handoffs,
then mirror the canonical skill into the plugin.

Single source of truth for handoff rubric content:
- archetypes/handoff_0X_*.md   (the model-agnostic practitioner guides)

Everything downstream is GENERATED — do not hand-edit it:
- skill/guide-instructional-design/references/handoff_0X_*.md   (skill copy + version footer)
- skill/guide-instructional-design-plugin/skills/.../references/  (plugin mirror)

The skill-specific files that are NOT handoffs — SKILL.md, package.json,
references/00_archetype_index.md, references/NOTICE.md — are edited directly in
skill/guide-instructional-design/ and only mirrored into the plugin by this script.
The plugin's agents/ and PIPELINE.md are plugin-only and untouched here.

This script:
1. Copies each archetypes/handoff_*.md into the skill's references/, appending the
   "Source: GUIDE ... (vX.Y.Z) ... Archetype NN of 10" version footer.
2. Mirrors the entire canonical skill tree into the plugin's skills/ directory so
   the plugin always ships a byte-identical copy.

Run from the repo root:
    python skill/build_skill.py
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

GUIDE_VERSION = "3.2.2"
COPYRIGHT_YEAR = "2026"
COPYRIGHT_HOLDER = "Jeremy Terhune"
TOTAL_ARCHETYPES = 10
# Trailing note appended after "of 10" for specific archetypes (10 is the synthesis lens).
FOOTER_SUFFIX = {10: " (the synthesis archetype)"}

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHETYPES_DIR = REPO_ROOT / "archetypes"
SKILL_DIR = REPO_ROOT / "skill" / "guide-instructional-design"
REFERENCES_DIR = SKILL_DIR / "references"
PLUGIN_SKILL_DIR = (
    REPO_ROOT
    / "skill"
    / "guide-instructional-design-plugin"
    / "skills"
    / "guide-instructional-design"
)

# Matches a trailing "--- / *Source: GUIDE ... *" footer block so a source file that
# already carries one is not double-stamped.
FOOTER_RE = re.compile(r"\n*-{3,}\n+\*Source: GUIDE\b.*?\*\s*$", re.DOTALL)


def footer_for(n: int) -> str:
    suffix = FOOTER_SUFFIX.get(n, "")
    return (
        "\n---\n\n"
        f"*Source: GUIDE - Grounded Universal Instructional Design Evaluator "
        f"(v{GUIDE_VERSION}). Copyright {COPYRIGHT_YEAR} {COPYRIGHT_HOLDER}. "
        f"Licensed under the Apache License, Version 2.0. "
        f"Archetype {n:02d} of {TOTAL_ARCHETYPES}{suffix}.*\n"
    )


def generate_references() -> list[Path]:
    """Copy each canonical handoff into references/ with a fresh version footer."""
    written: list[Path] = []
    pattern = re.compile(r"handoff_(\d{2})_.+\.md$")
    for src in sorted(ARCHETYPES_DIR.glob("handoff_*.md")):
        m = pattern.search(src.name)
        if not m:
            continue
        n = int(m.group(1))
        body = FOOTER_RE.sub("", src.read_text(encoding="utf-8")).rstrip() + "\n"
        dst = REFERENCES_DIR / src.name
        dst.write_text(body + footer_for(n), encoding="utf-8", newline="")
        written.append(dst)
    return written


def mirror_skill_to_plugin() -> None:
    """Copy the canonical skill tree into the plugin so the two stay byte-identical."""
    if PLUGIN_SKILL_DIR.exists():
        shutil.rmtree(PLUGIN_SKILL_DIR)
    shutil.copytree(SKILL_DIR, PLUGIN_SKILL_DIR)


def main() -> None:
    if not ARCHETYPES_DIR.is_dir():
        raise SystemExit(f"Cannot find archetypes dir: {ARCHETYPES_DIR}")
    if not REFERENCES_DIR.is_dir():
        raise SystemExit(f"Cannot find references dir: {REFERENCES_DIR}")
    written = generate_references()
    mirror_skill_to_plugin()
    print(f"Generated {len(written)} handoff reference(s) at GUIDE v{GUIDE_VERSION}.")
    print(f"Mirrored {SKILL_DIR.name}/ -> plugin skills/{SKILL_DIR.name}/.")


if __name__ == "__main__":
    main()
