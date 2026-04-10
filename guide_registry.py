"""
GUIDE Registry - Entry Point for All Evaluation Archetypes
============================================================
GUIDE: Grounded Universal Instructional Design Evaluator

Import this module to register all archetypes and access the full evaluation suite.

Usage:
    from guide_registry import (
        list_archetypes,
        evaluate,
        evaluate_composite,
        evaluate_all,
    )

    # List available archetypes
    print(list_archetypes())

    # Evaluate with a single archetype
    result = evaluate("assessment_design", input="...", output="...")

    # Evaluate with multiple archetypes
    composite = evaluate_composite(
        ["assessment_design", "instructional_sequencing"],
        input="...", output="...",
    )
    print(composite.mean_overall)

    # Evaluate with ALL archetypes
    full = evaluate_all(input="...", output="...")

Author: Jeremy Terhune
License: Proprietary - organizational use by permission
"""

# Register all archetypes by importing the package
import archetypes  # noqa: F401

from guide_base import (
    list_archetypes,
    get_archetype,
    make_evaluator,
    evaluate_standalone,
    evaluate_composite as _evaluate_composite,
    run_langsmith_eval,
    GUIDEResult,
    CompositeResult,
)


def evaluate(
    archetype_name: str,
    input: str,
    output: str,
    context: str = "N/A",
    reference: str = "N/A",
    model_name: str = "claude-sonnet-4-20250514",
    api_key: str | None = None,
) -> GUIDEResult:
    """Evaluate a single input/output pair with one archetype."""
    return evaluate_standalone(
        archetype_name=archetype_name,
        user_input=input,
        assistant_output=output,
        context=context,
        reference=reference,
        model_name=model_name,
        api_key=api_key,
    )


def evaluate_composite(
    archetype_names: list[str],
    input: str,
    output: str,
    context: str = "N/A",
    reference: str = "N/A",
    model_name: str = "claude-sonnet-4-20250514",
    api_key: str | None = None,
) -> CompositeResult:
    """Evaluate a single input/output pair with multiple archetypes."""
    return _evaluate_composite(
        archetype_names=archetype_names,
        user_input=input,
        assistant_output=output,
        context=context,
        reference=reference,
        model_name=model_name,
        api_key=api_key,
    )


def evaluate_all(
    input: str,
    output: str,
    context: str = "N/A",
    reference: str = "N/A",
    model_name: str = "claude-sonnet-4-20250514",
    api_key: str | None = None,
) -> CompositeResult:
    """Evaluate a single input/output pair with ALL registered archetypes."""
    return _evaluate_composite(
        archetype_names=list_archetypes(),
        user_input=input,
        assistant_output=output,
        context=context,
        reference=reference,
        model_name=model_name,
        api_key=api_key,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 65)
    print("  GUIDE - Grounded Universal Instructional Design Evaluator")
    print("=" * 65)
    print()
    print(f"  Registered archetypes: {len(list_archetypes())}")
    print()
    for name in list_archetypes():
        arch = get_archetype(name)
        desc = arch.get("description", "")
        print(f"    - {name}")
        if desc:
            print(f"      {desc}")
        print()
    print("  Usage:")
    print("    from guide_registry import evaluate, evaluate_composite")
    print()
    print('    result = evaluate("assessment_design", input="...", output="...")')
    print()
    print("    composite = evaluate_composite(")
    print('        ["assessment_design", "multimedia_design"],')
    print('        input="...", output="..."')
    print("    )")
    print(f"    print(composite.mean_overall)")
