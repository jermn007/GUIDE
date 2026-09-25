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
    print()
    if failed:
        print(f"{failed} problem(s) found.")
        return 1
    print(f"All {len(_REGISTRY)} archetypes ask for the standard output format.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
