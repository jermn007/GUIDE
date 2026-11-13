"""
GUIDE edge-case runner
======================

Each archetype has labeled test cases in archetypes/edge_cases_NN.json: an artifact,
the scores an expert would give it, and why. This script uses them two ways.

  python run_edge_cases.py              Check the case files (no model, no API key).
  python run_edge_cases.py --live       Score every case with a live judge and report
                                        drift from the expected overall.
  python run_edge_cases.py --live --backend cli
                                        The same, through the Claude Code CLI you are
                                        signed in to (no API key).

The check confirms that every case names exactly its judge's six dimensions, that
every expected score is a whole number from 1 to 5, and that a stated overall agrees
with its own dimension scores. It exits non-zero on any problem, so it can run in CI.

The live run sends each case's artifact to a judge and prints expected versus actual.
It exits non-zero when any case drifts from its expected overall by more than
--tolerance (one full point for cases that expect only a whole-number overall). There are two ways to reach a model:

  --backend api   (default) the `anthropic` package and ANTHROPIC_API_KEY.
  --backend cli   the `claude` command, with the judge prompt as the system prompt
                  and no tools. It scores --jobs cases at a time (default 4).

--report FILE writes the results as JSON, to keep with a release.

    python run_edge_cases.py --live --archetype 02
    python run_edge_cases.py --live --model claude-sonnet-5-5 --tolerance 0.7
    python run_edge_cases.py --live --backend cli --model sonnet --report drift.json

Author: Jeremy Terhune
Copyright 2026 Jeremy Terhune
License: Apache-2.0 (see LICENSE and NOTICE in the repository root)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import guide_registry  # noqa: E402,F401  (importing registers the archetypes)
from guide_base import GUIDEResult, _REGISTRY, evaluate_standalone, get_archetype  # noqa: E402
from test_judge_schemas import dimension_keys  # noqa: E402

ARCHETYPES_DIR = os.path.join(HERE, "archetypes")
DEFAULT_MODEL = "claude-sonnet-5-5"
# How far a stated overall may sit from the mean of its own dimension scores.
OVERALL_SLACK = 0.25
# Archetype 10 caps the overall at 3.0 when this dimension scores 1 or 2.
CAP_ARCHETYPE = "curriculum_alignment"
CAP_DIMENSION = "objective_assessment_coherence"
CAP_VALUE = 3.0
# Archetype 01's overall is weighted, not a plain mean, so its stated overalls are not checked.
WEIGHTED_ARCHETYPES = {"adult_learning_communication"}
NON_SCORE_KEYS = {"overall", "rationale", "severity_flags"}


def load_cases(path: str) -> tuple[str, list[dict]]:
    """Return (registered archetype name, cases) for one edge-case file."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    cases = data.get("edge_cases") or data.get("examples") or []
    name = data.get("archetype") or data.get("metadata", {}).get("archetype", "")
    if name not in _REGISTRY:
        number = re.search(r"edge_cases_(\d{2})\.json$", path).group(1)
        for fname in os.listdir(ARCHETYPES_DIR):
            if fname.startswith(f"archetype_{number}_") and fname.endswith(".py"):
                with open(os.path.join(ARCHETYPES_DIR, fname), encoding="utf-8") as fh:
                    m = re.search(r'register_archetype\(\s*name="([^"]+)"', fh.read())
                name = m.group(1) if m else name
    return name, cases


def case_id(case: dict) -> str:
    return str(case.get("case_id") or case.get("id") or case.get("title") or "?")


def expected_dimensions(case: dict) -> dict:
    scores = case.get("expected_scores") or {}
    return {k: v for k, v in scores.items() if k not in NON_SCORE_KEYS}


def expected_overall(archetype: str, case: dict) -> float | None:
    """The overall a case expects: stated if present, else derived from its dimensions."""
    if "expected_overall" in case:
        return float(case["expected_overall"])
    scores = case.get("expected_scores") or {}
    if "overall" in scores:
        return float(scores["overall"])
    dims = expected_dimensions(case)
    if not dims:
        return None
    mean = sum(dims.values()) / len(dims)
    if archetype == CAP_ARCHETYPE and dims.get(CAP_DIMENSION, 5) <= 2:
        mean = min(mean, CAP_VALUE)
    return round(mean, 2)


def check_file(path: str) -> list[str]:
    """Return the problems in one edge-case file (empty when it is sound)."""
    problems: list[str] = []
    fname = os.path.basename(path)
    archetype, cases = load_cases(path)
    if archetype not in _REGISTRY:
        return [f"{fname}: archetype '{archetype}' is not registered"]
    if not cases:
        return [f"{fname}: no cases found"]
    judge_keys = dimension_keys(archetype, _REGISTRY[archetype])
    seen: set[str] = set()
    for case in cases:
        cid = case_id(case)
        if cid in seen:
            problems.append(f"{fname} {cid}: duplicate case id")
        seen.add(cid)
        dims = expected_dimensions(case)
        if not dims:
            if "expected_overall" not in case:
                problems.append(f"{fname} {cid}: no expected scores")
            continue
        if sorted(dims) != sorted(judge_keys):
            missing = sorted(set(judge_keys) - set(dims))
            extra = sorted(set(dims) - set(judge_keys))
            problems.append(f"{fname} {cid}: dimension keys differ from the judge (missing {missing}, extra {extra})")
            continue
        bad = {k: v for k, v in dims.items() if not (isinstance(v, int) and 1 <= v <= 5)}
        if bad:
            problems.append(f"{fname} {cid}: scores must be whole numbers 1-5, got {bad}")
            continue
        stated = (case.get("expected_scores") or {}).get("overall")
        if stated is not None and archetype not in WEIGHTED_ARCHETYPES:
            mean = sum(dims.values()) / len(dims)
            if archetype == CAP_ARCHETYPE and dims.get(CAP_DIMENSION, 5) <= 2:
                mean = min(mean, CAP_VALUE)
            if abs(mean - float(stated)) > OVERALL_SLACK:
                problems.append(f"{fname} {cid}: stated overall {stated} is not the mean of its dimensions ({mean:.2f})")
    return problems


def case_text(case: dict) -> tuple[str, str, str, str]:
    """Return (input, output, context, reference) for the judge from any case shape."""
    user_input = case.get("input") or case.get("description") or case.get("title") or ""
    output = case.get("artifact") or case.get("output") or case.get("description") or ""
    context = case.get("context") or "N/A"
    if not isinstance(context, str):
        context = json.dumps(context, ensure_ascii=False)
    reference = case.get("reference") or "N/A"
    return str(user_input), str(output), context, str(reference)


def evaluate_with_cli(archetype: str, user_input: str, output: str, context: str, reference: str, model: str) -> GUIDEResult:
    """Score one case through the Claude Code CLI: judge prompt as system prompt, no tools."""
    spec = get_archetype(archetype)
    human = spec["human_prompt"].format(input=user_input, output=output, context=context, reference=reference)
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as work:
        system_file = os.path.join(work, "judge_system_prompt.txt")
        with open(system_file, "w", encoding="utf-8") as fh:
            fh.write(spec["system_prompt"])
        cmd = ["claude", "-p", "--system-prompt-file", system_file, "--tools", "", "--model", model]
        proc = subprocess.run(cmd, input=human, capture_output=True, text=True, encoding="utf-8",
                              cwd=work, timeout=600, shell=(os.name == "nt"))
    text = (proc.stdout or "").strip()
    if proc.returncode != 0 or not text:
        raise RuntimeError((proc.stderr or text or "no output").strip()[:300])
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise RuntimeError("no JSON object in the judge's reply: " + text[:200])
    return GUIDEResult.from_json(text[start:end + 1], archetype=archetype)


def score_case(archetype: str, case: dict, model: str, backend: str) -> dict:
    """Score one case and return a result row; a failed call is a row with an error, not an exception."""
    want = expected_overall(archetype, case)
    user_input, output, context, reference = case_text(case)
    row = {"archetype": archetype, "case": case_id(case), "expected_overall": want,
           "expected_scores": expected_dimensions(case)}
    try:
        if backend == "cli":
            result = evaluate_with_cli(archetype, user_input, output, context, reference, model)
        else:
            result = evaluate_standalone(archetype, user_input, output, context=context,
                                         reference=reference, model_name=model)
    except Exception as exc:
        row["error"] = str(exc)
        return row
    scores = {k: v for k, v in result.scores.items() if k != "overall" and isinstance(v, (int, float))}
    got = result.scores.get("overall")
    if not isinstance(got, (int, float)):
        got = sum(scores.values()) / max(len(scores), 1)
    row.update(judge_overall=round(float(got), 2), judge_scores=scores, severity_flags=result.severity_flags,
               rationale=result.rationale)
    if want is not None:
        row["drift"] = round(float(got) - want, 2)
        # A case that expects only a whole-number overall (no dimension scores) cannot be matched
        # more closely than one step, so one step counts as agreement.
        row["whole_number_overall"] = not row["expected_scores"] and float(want).is_integer()
    return row


def within(row: dict, tolerance: float) -> bool:
    """True when a scored case agrees with its expected overall."""
    allowed = max(tolerance, 1.0) if row.get("whole_number_overall") else tolerance
    return abs(row["drift"]) <= allowed + 1e-9


def run_live(paths: list[str], model: str, tolerance: float, backend: str, jobs: int, report: str | None) -> int:
    rows: list[dict] = []
    for path in paths:
        archetype, cases = load_cases(path)
        print(f"\n{os.path.basename(path)}  ({archetype}, {backend} backend, model {model})", flush=True)
        workers = jobs if backend == "cli" else 1
        with ThreadPoolExecutor(max_workers=max(workers, 1)) as pool:
            results = list(pool.map(lambda c: score_case(archetype, c, model, backend), cases))
        for row in results:
            rows.append(row)
            cid = row["case"]
            if "error" in row:
                print(f"  ERROR {cid}: {row['error']}")
            elif row["expected_overall"] is None:
                print(f"  ----  {cid}: no expected overall; judge gave {row['judge_overall']:.2f}")
            else:
                verdict = "ok   " if within(row, tolerance) else "DRIFT"
                print(f"  {verdict} {cid}: expected {row['expected_overall']:.2f}, "
                      f"judge {row['judge_overall']:.2f} ({row['drift']:+.2f})")
                for key, exp in row["expected_scores"].items():
                    act = row["judge_scores"].get(key)
                    if isinstance(act, (int, float)) and abs(act - exp) >= 2:
                        print(f"          {key}: expected {exp}, judge {act}")
        sys.stdout.flush()
    scored = [r for r in rows if "drift" in r]
    errors = [r for r in rows if "error" in r]
    drifted = [r for r in scored if not within(r, tolerance)]
    mean_signed = sum(r["drift"] for r in scored) / len(scored) if scored else 0.0
    mean_abs = sum(abs(r["drift"]) for r in scored) / len(scored) if scored else 0.0
    print(f"\n{len(scored) - len(drifted)} of {len(scored)} scored cases within {tolerance} of the expected overall "
          f"(mean absolute drift {mean_abs:.2f}, mean drift {mean_signed:+.2f}); {len(errors)} error(s).")
    if report:
        with open(report, "w", encoding="utf-8") as fh:
            json.dump({"model": model, "backend": backend, "tolerance": tolerance,
                       "cases": len(rows), "within_tolerance": len(scored) - len(drifted), "errors": len(errors),
                       "mean_absolute_drift": round(mean_abs, 3), "mean_drift": round(mean_signed, 3),
                       "results": rows}, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"Report written to {report}")
    return 1 if drifted or errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or run the GUIDE edge cases.")
    parser.add_argument("--live", action="store_true", help="score each case with a live judge (needs ANTHROPIC_API_KEY)")
    parser.add_argument("--archetype", help="two-digit archetype number, e.g. 02 (default: all)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"model for --live (default {DEFAULT_MODEL})")
    parser.add_argument("--tolerance", type=float, default=0.7, help="allowed drift in the overall for --live (default 0.7)")
    parser.add_argument("--backend", choices=("api", "cli"), default="api",
                        help="how --live reaches a model: the Anthropic API (default) or the signed-in claude CLI")
    parser.add_argument("--jobs", type=int, default=4, help="cases scored at once with --backend cli (default 4)")
    parser.add_argument("--report", help="write the --live results to this JSON file")
    args = parser.parse_args()

    paths = sorted(
        os.path.join(ARCHETYPES_DIR, f) for f in os.listdir(ARCHETYPES_DIR)
        if re.fullmatch(r"edge_cases_\d{2}\.json", f) and (not args.archetype or f == f"edge_cases_{args.archetype}.json")
    )
    if not paths:
        print("No edge-case files matched.")
        return 1

    print("=" * 65)
    print("  GUIDE edge cases")
    print("=" * 65)
    problems: list[str] = []
    count = 0
    for path in paths:
        found = check_file(path)
        problems += found
        _, cases = load_cases(path)
        count += len(cases)
        print(f"  {'FAIL' if found else 'PASS'}  {os.path.basename(path)} ({len(cases)} cases)")
    for p in problems:
        print(f"        {p}")
    if problems:
        print(f"\n{len(problems)} problem(s) in the case files.")
        return 1
    print(f"\nAll {count} cases in {len(paths)} file(s) are well-formed.")
    if not args.live:
        return 0
    if args.backend == "api" and not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n--live needs ANTHROPIC_API_KEY in the environment, or use --backend cli.")
        return 1
    return run_live(paths, args.model, args.tolerance, args.backend, args.jobs, args.report)


if __name__ == "__main__":
    sys.exit(main())
