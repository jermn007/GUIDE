"""
GUIDE Archetypes - Evaluation Modules for Instructional Design
===============================================================
GUIDE: Grounded Universal Instructional Design Evaluator

Import this package to register all archetypes with the base registry.

Usage:
    import archetypes  # registers all archetypes
    from guide_base import list_archetypes, evaluate_standalone

    print(list_archetypes())
    result = evaluate_standalone("assessment_design", input, output)
"""

from . import archetype_01_adult_learning_communication
from . import archetype_02_assessment_design
from . import archetype_03_instructional_sequencing
from . import archetype_04_multimedia_design
from . import archetype_05_accessibility_technical
from . import archetype_06_formative_evaluation
from . import archetype_07_needs_analysis
from . import archetype_08_story_design
from . import archetype_09_cognitive_neuroscience
