"""Generate the skill's handoff references from the canonical archetypes/ handoffs,
then mirror the canonical skill into the plugin.

Single source of truth for handoff rubric content:
- archetypes/handoff_0X_*.md   (the model-agnostic practitioner guides)

Everything downstream is GENERATED — do not hand-edit it:
- skill/guide-instructional-design/references/handoff_0X_*.md   (skill edition + version footer)
- skill/guide-instructional-design-plugin/skills/framework/  (plugin mirror)

The skill-specific files that are NOT handoffs — SKILL.md, package.json,
references/00_archetype_index.md, references/NOTICE.md — are edited directly in
skill/guide-instructional-design/ and only mirrored into the plugin by this script.
SKILL.md, EVALUATE.md and DESIGN.md are edited the same way. The plugin's agents/,
PIPELINE.md, and entry-command skills (skills/evaluate, build,
pipeline) are plugin-only and untouched here.

This script:
1. Writes the skill edition of each archetypes/handoff_*.md into the skill's
   references/: the sections in HARNESS_ONLY_SECTIONS are dropped, the Human Prompt
   Template is replaced by its JSON output shape ("Output JSON"), and the
   "Source: GUIDE ... (vX.Y.Z) ... Archetype NN of 10" version footer is appended.
   The canonical handoffs stay complete for use outside Claude.
2. Mirrors the canonical skill tree into the plugin's skills/framework/
   so the plugin always ships the same content. Only the `name` in SKILL.md differs:
   the plugin's copy is named `framework`.
3. Checks that each specialist agent's output contract uses the same dimension keys
   as its handoff's output JSON, and exits non-zero if not.

Run from the repo root:
    python skill/build_skill.py

Author: Jeremy Terhune
Copyright 2026 Jeremy Terhune
License: Apache-2.0 (see LICENSE and NOTICE in the repository root)
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

GUIDE_VERSION = "3.5.0"
COPYRIGHT_YEAR = "2026"
COPYRIGHT_HOLDER = "Jeremy Terhune"
TOTAL_ARCHETYPES = 10
# Trailing note appended after "of 10" for specific archetypes (10 is the synthesis lens).
FOOTER_SUFFIX = {10: " (the synthesis archetype)"}
DIMENSIONS_PER_ARCHETYPE = 6
# Non-handoff reference authored in archetypes/ and propagated like the handoffs.
CROSSWALK_NAME = "discipline_alignment_crosswalk.md"

# H2 sections of a canonical handoff that only serve the Python LLM-as-a-judge harness
# (or the repo's history). The skill edition drops them: Claude reads the scoring guide
# directly, so the judge system prompt (a compressed restatement of that guide) and the
# harness input/calibration notes only cost context. They stay in archetypes/ for use
# outside Claude.
HARNESS_ONLY_SECTIONS = {
    "System Prompt (Judge Rubric)",
    "Input Format",
    "Calibration & Validation",
    "Integration with GUIDE Pipeline",
    "Version History",
}
# Replaced in the skill edition by just the JSON output shape it contains.
JUDGE_TEMPLATE_SECTION = "Human Prompt Template"
OUTPUT_JSON_HEADING = "Output JSON"

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHETYPES_DIR = REPO_ROOT / "archetypes"
SKILL_DIR = REPO_ROOT / "skill" / "guide-instructional-design"
REFERENCES_DIR = SKILL_DIR / "references"
PLUGIN_DIR = REPO_ROOT / "skill" / "guide-instructional-design-plugin"
# Inside the plugin the skill is named "framework", so it reads as
# guide-instructional-design:framework and not as the plugin name twice.
PLUGIN_SKILL_NAME = "framework"
PLUGIN_SKILL_DIR = PLUGIN_DIR / "skills" / PLUGIN_SKILL_NAME
PLUGIN_AGENTS_DIR = PLUGIN_DIR / "agents"

# Matches a trailing "--- / *Source: GUIDE ... *" footer block so a source file that
# already carries one is not double-stamped.
FOOTER_RE = re.compile(r"\n*-{3,}\n+\*Source: GUIDE\b.*?\*\s*$", re.DOTALL)


def footer_for(n: int, filename: str) -> str:
    suffix = FOOTER_SUFFIX.get(n, "")
    return (
        "\n---\n\n"
        f"*Source: GUIDE - Grounded Universal Instructional Design Evaluator "
        f"(v{GUIDE_VERSION}). Copyright {COPYRIGHT_YEAR} {COPYRIGHT_HOLDER}. "
        f"Licensed under the Apache License, Version 2.0. "
        f"Archetype {n:02d} of {TOTAL_ARCHETYPES}{suffix}. "
        f"Skill edition: the judge prompts and Python-harness notes are omitted; "
        f"the full model-agnostic handoff is `archetypes/{filename}` in the GUIDE repository.*\n"
    )


def split_sections(text: str) -> list[tuple[str | None, str]]:
    """Split markdown into (H2 heading title, chunk) pairs, ignoring headings in code fences.

    The first chunk (everything before the first H2) has a title of None. Each chunk
    keeps its own heading line and any trailing `---` separator.
    """
    sections: list[tuple[str | None, list[str]]] = [(None, [])]
    in_fence = False
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            sections.append((line[3:].strip(), []))
        sections[-1][1].append(line)
    return [(title, "".join(lines)) for title, lines in sections]


def extract_scores_json(chunk: str) -> str | None:
    """Return the JSON object holding the first "scores" key in a chunk, or None."""
    at = chunk.find('"scores"')
    if at == -1:
        return None
    start = chunk.rfind("{", 0, at)
    depth = 0
    for i in range(start, len(chunk)):
        if chunk[i] == "{":
            depth += 1
        elif chunk[i] == "}":
            depth -= 1
            if depth == 0:
                return chunk[start : i + 1]
    return None


def scores_keys(json_text: str) -> list[str]:
    """Return the keys of the "scores" object in a JSON template (placeholders allowed)."""
    m = re.search(r'"scores"\s*:\s*\{(.*?)\}', json_text, re.DOTALL)
    return re.findall(r'"([a-z0-9_]+)"\s*:', m.group(1)) if m else []


def slim_handoff(text: str, name: str) -> tuple[str, list[str]]:
    """Return the skill edition of a handoff and the dimension keys of its output JSON.

    Drops the sections that only serve the Python LLM-as-a-judge harness (see
    HARNESS_ONLY_SECTIONS) and replaces the Human Prompt Template with just the JSON
    output shape the judge returns, under an "Output JSON" heading.
    """
    out: list[str] = []
    keys: list[str] = []
    found_template = False
    for title, chunk in split_sections(text):
        if title == JUDGE_TEMPLATE_SECTION:
            found_template = True
            json_text = extract_scores_json(chunk)
            if json_text is None:
                raise SystemExit(f"{name}: no JSON with a \"scores\" object in the Human Prompt Template")
            keys = [k for k in scores_keys(json_text) if k != "overall"]
            out.append(
                f"## {OUTPUT_JSON_HEADING}\n\n"
                "Return this shape when the user wants machine-readable output "
                "(scores are integers 1-5; `overall` follows the archetype's scoring rule):\n\n"
                f"```json\n{json_text.strip()}\n```\n\n---\n\n"
            )
        elif title in HARNESS_ONLY_SECTIONS:
            continue
        else:
            out.append(chunk)
    if not found_template:
        raise SystemExit(f"{name}: no '## {JUDGE_TEMPLATE_SECTION}' section to slim")
    if len(keys) != DIMENSIONS_PER_ARCHETYPE:
        raise SystemExit(f"{name}: output JSON has {len(keys)} dimensions, expected {DIMENSIONS_PER_ARCHETYPE}")
    body = re.sub(r"(\n---\s*\n)(\s*---\s*\n)+", r"\1", "".join(out))
    return body.rstrip() + "\n", keys


def generate_references() -> dict[int, list[str]]:
    """Write the skill edition of each canonical handoff into references/ with a footer.

    Returns {archetype number: dimension keys} for the consistency checks.
    """
    keys_by_archetype: dict[int, list[str]] = {}
    pattern = re.compile(r"handoff_(\d{2})_.+\.md$")
    for src in sorted(ARCHETYPES_DIR.glob("handoff_*.md")):
        m = pattern.search(src.name)
        if not m:
            continue
        n = int(m.group(1))
        canonical = FOOTER_RE.sub("", src.read_text(encoding="utf-8")).rstrip() + "\n"
        body, keys = slim_handoff(canonical, src.name)
        dst = REFERENCES_DIR / src.name
        dst.write_text(body + footer_for(n, src.name), encoding="utf-8", newline="")
        keys_by_archetype[n] = keys
    if len(keys_by_archetype) != TOTAL_ARCHETYPES:
        raise SystemExit(f"Found {len(keys_by_archetype)} handoffs, expected {TOTAL_ARCHETYPES}")
    return keys_by_archetype


def check_agents(keys_by_archetype: dict[int, list[str]]) -> list[str]:
    """Check each specialist agent's output contract against its handoff's dimensions.

    The agents are hand-maintained, so this catches a renamed or re-ordered dimension
    in a handoff that was never carried into the agent that scores it.
    """
    problems: list[str] = []
    owner = re.compile(r"owning archetype (\d{2})")
    for path in sorted(PLUGIN_AGENTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = owner.search(text)
        if not m:
            continue
        n = int(m.group(1))
        # An agent may show several "scores" objects (e.g. 10's one-dimension fail_fast
        # check); its full scorecard is the one with the most keys.
        candidates = [
            [k for k in scores_keys(s) if k != "overall"]
            for s in re.findall(r'"scores"\s*:\s*\{.*?\}', text, re.DOTALL)
        ]
        agent_keys = max(candidates, key=len, default=[])
        if agent_keys != keys_by_archetype.get(n):
            problems.append(
                f"{path.name}: scores keys {agent_keys} do not match handoff {n:02d} "
                f"{keys_by_archetype.get(n)}"
            )
    owners = {int(m.group(1)) for p in PLUGIN_AGENTS_DIR.glob("*.md")
              if (m := owner.search(p.read_text(encoding="utf-8")))}
    for n in sorted(set(keys_by_archetype) - owners):
        problems.append(f"no agent says it is 'owning archetype {n:02d}'")
    return problems


def generic_footer() -> str:
    """Version footer for non-handoff references (no archetype number)."""
    return (
        "\n---\n\n"
        f"*Source: GUIDE - Grounded Universal Instructional Design Evaluator "
        f"(v{GUIDE_VERSION}). Copyright {COPYRIGHT_YEAR} {COPYRIGHT_HOLDER}. "
        f"Licensed under the Apache License, Version 2.0.*\n"
    )


def copy_crosswalk() -> Path | None:
    """Copy the discipline-alignment crosswalk into references/ with a version footer.

    Authored in archetypes/ (alongside the handoffs) so the per-handoff relative
    links resolve in both archetypes/ and the generated references/ directory.
    """
    src = ARCHETYPES_DIR / CROSSWALK_NAME
    if not src.exists():
        return None
    body = FOOTER_RE.sub("", src.read_text(encoding="utf-8")).rstrip() + "\n"
    dst = REFERENCES_DIR / CROSSWALK_NAME
    dst.write_text(body + generic_footer(), encoding="utf-8", newline="")
    return dst


def mirror_skill_to_plugin() -> None:
    """Copy the canonical skill tree into the plugin, identical except for the skill's name."""
    if PLUGIN_SKILL_DIR.exists():
        shutil.rmtree(PLUGIN_SKILL_DIR)
    shutil.copytree(SKILL_DIR, PLUGIN_SKILL_DIR)
    skill_md = PLUGIN_SKILL_DIR / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    old = f"name: {SKILL_DIR.name}\n"
    if text.count(old) != 1:
        raise SystemExit(f"Expected one '{old.strip()}' line in {skill_md}")
    skill_md.write_text(text.replace(old, f"name: {PLUGIN_SKILL_NAME}\n"), encoding="utf-8", newline="")


def main() -> None:
    if not ARCHETYPES_DIR.is_dir():
        raise SystemExit(f"Cannot find archetypes dir: {ARCHETYPES_DIR}")
    if not REFERENCES_DIR.is_dir():
        raise SystemExit(f"Cannot find references dir: {REFERENCES_DIR}")
    keys_by_archetype = generate_references()
    crosswalk = copy_crosswalk()
    mirror_skill_to_plugin()
    print(f"Generated {len(keys_by_archetype)} skill-edition handoff(s) at GUIDE v{GUIDE_VERSION}.")
    if crosswalk:
        print(f"Copied {crosswalk.name} into references/.")
    print(f"Mirrored {SKILL_DIR.name}/ -> plugin skills/{PLUGIN_SKILL_NAME}/.")
    problems = check_agents(keys_by_archetype)
    if problems:
        for p in problems:
            print(f"  FAIL  {p}")
        raise SystemExit(f"{len(problems)} agent/handoff mismatch(es).")
    print("Agent output contracts match the handoff dimensions.")


if __name__ == "__main__":
    main()
