"""
GUIDE judge output-format check.

Every registered archetype must ask its judge for the standard GUIDE output
(the schema GUIDEResult.from_json parses): a "scores" object with six dimension
scores plus "overall", a "rationale" entry per dimension, "severity_flags", and
"improvement_suggestions". An archetype that asks for any other shape returns
empty results through the Python API without raising an error, which is the
bug fixed in v3.4.1 for archetypes 05, 06, and 07.

For each archetype this script formats the human prompt the way the runners do,
finds the JSON template shown to the judge (in the system or human prompt),
fills in its placeholders, and parses the result with
GUIDEResult.from_json. No API calls are made.

Run from the repo root:
    python test_judge_schemas.py

Author: Jeremy Terhune
Copyright 2026 Jeremy Terhune
License: Apache-2.0 (see LICENSE and NOTICE in the repository root)
"""

from __future__ import annotations

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import archetypes  # noqa: F401  (registers all archetypes)
from guide_base import GUIDEResult, _REGISTRY

EXPECTED_ARCHETYPES = 10
DIMENSIONS_PER_ARCHETYPE = 6


def extract_template(text: str) -> str | None:
    """Return the JSON object that contains the first "scores" key, or None."""
    at = text.find('"scores"')
    if at == -1:
        return None
    start = text.rfind("{", 0, at)
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def check(name: str, archetype: dict) -> list[str]:
    """Return a list of problems with one archetype's output format."""
    problems: list[str] = []
    try:
        prompt = archetype["human_prompt"].format(
            input="INPUT", output="OUTPUT", context="N/A", reference="N/A"
        )
    except (KeyError, IndexError, ValueError) as exc:
        return [f"human prompt does not format cleanly: {exc!r}"]

    template = extract_template(archetype["system_prompt"] + "\n" + prompt)
    if template is None:
        return ['no JSON template with a "scores" object in the system or human prompt']
    # Fill unquoted placeholders such as <1-5> or <mean of all 6> with a score.
    filled = re.sub(r'(?<!")<[^>"\n]*>(?!")', "3", template)
    try:
        result = GUIDEResult.from_json(filled, archetype=name)
    except json.JSONDecodeError as exc:
        return [f"JSON template is not valid JSON once filled in: {exc}"]

    dims = [k for k in result.scores if k != "overall"]
    if "overall" not in result.scores:
        problems.append('"scores" has no "overall"')
    if len(dims) != DIMENSIONS_PER_ARCHETYPE:
        problems.append(f'"scores" has {len(dims)} dimensions, expected {DIMENSIONS_PER_ARCHETYPE}')
    if set(result.rationale) - {"overall"} != set(dims):
        problems.append('"rationale" keys do not match the "scores" dimensions')
    data = json.loads(filled)
    for key in ("severity_flags", "improvement_suggestions"):
        if not isinstance(data.get(key), list):
            problems.append(f'"{key}" is missing or not a list')
    return problems


def dimension_keys(name: str, archetype: dict) -> list[str]:
    """Return the judge's six dimension keys, in order, from its JSON template."""
    prompt = archetype["human_prompt"].format(
        input="INPUT", output="OUTPUT", context="N/A", reference="N/A"
    )
    template = extract_template(archetype["system_prompt"] + "\n" + prompt) or ""
    filled = re.sub(r'(?<!")<[^>"\n]*>(?!")', "3", template)
    scores = json.loads(filled).get("scores", {}) if filled else {}
    return [k for k in scores if k != "overall"]


def check_handoffs() -> list[str]:
    """Check each archetypes/handoff_NN_*.md shows the same dimension keys as its judge.

    The handoffs are the model-agnostic edition used outside Claude (and the source of
    the Claude skill), so their output JSON must stay in step with the Python judges.
    """
    problems: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))
    adir = os.path.join(here, "archetypes")
    for fname in sorted(os.listdir(adir)):
        m = re.fullmatch(r"handoff_(\d{2})_(.+)\.md", fname)
        if not m:
            continue
        module = os.path.join(adir, f"archetype_{m.group(1)}_{m.group(2)}.py")
        if not os.path.exists(module):
            problems.append(f"{fname}: no matching {os.path.basename(module)}")
            continue
        with open(module, encoding="utf-8") as fh:
            reg = re.search(r'register_archetype\(\s*name="([^"]+)"', fh.read())
        if not reg or reg.group(1) not in _REGISTRY:
            problems.append(f"{fname}: cannot find the registered archetype name")
            continue
        judge_keys = dimension_keys(reg.group(1), _REGISTRY[reg.group(1)])
        with open(os.path.join(adir, fname), encoding="utf-8") as fh:
            handoff = fh.read()
        template = extract_template(handoff[handoff.find("## Human Prompt Template"):])
        if template is None:
            problems.append(f'{fname}: no JSON template with "scores" in its Human Prompt Template')
            continue
        hm = re.search(r'"scores"\s*:\s*\{(.*?)\}', template, re.DOTALL)
        handoff_keys = [k for k in re.findall(r'"([a-z0-9_]+)"\s*:', hm.group(1)) if k != "overall"]
        if handoff_keys != judge_keys:
            problems.append(f"{fname}: dimension keys {handoff_keys} != judge {judge_keys}")
    return problems


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    print("=" * 65)
    print("  GUIDE judge output-format check")
    print("=" * 65)
    failed = 0
    if len(_REGISTRY) != EXPECTED_ARCHETYPES:
        print(f"  FAIL  registry has {len(_REGISTRY)} archetypes, expected {EXPECTED_ARCHETYPES}")
        failed += 1
    for name, archetype in _REGISTRY.items():
        problems = check(name, archetype)
        if problems:
            failed += 1
            for p in problems:
                print(f"  FAIL  {name}: {p}")
        else:
            print(f"  PASS  {name} (v{archetype.get('version', '?')})")
    handoff_problems = check_handoffs()
    for p in handoff_problems:
        print(f"  FAIL  {p}")
    if not handoff_problems:
        print("  PASS  handoff output JSON matches each judge's dimension keys")
    failed += len(handoff_problems)
    print()
    if failed:
        print(f"{failed} problem(s) found.")
        return 1
    print(f"All {len(_REGISTRY)} archetypes ask for the standard output format, and the handoffs match.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
