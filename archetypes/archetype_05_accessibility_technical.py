"""
ARCHETYPE 5: WCAG/POUR TECHNICAL ACCESSIBILITY

Evaluates web-based learning content, LMS pages, and e-learning modules for WCAG 2.1 compliance.
Dimensions: Perceivable, Operable, Understandable, Robust, UDL Integration, Remediation Feasibility.

References:
- W3C WAI (2018). Web Content Accessibility Guidelines (WCAG) 2.1.
- CAST (2018). Universal Design for Learning Guidelines version 2.2.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guide_base import register_archetype

JUDGE_SYSTEM_PROMPT = """You are an expert in WCAG 2.1 accessibility compliance and Universal Design for Learning (UDL).
Your role is to evaluate web-based learning content against accessibility standards.

You will score across 6 dimensions, each on a 1-5 scale:

1. **Perceivable** (1-5)
   - Text alternatives for non-text content (1.1.1): All images, icons, graphs have alt text
   - Captions for audio (1.2.2): Multimedia includes captions for hearing-impaired users
   - Audio description (1.2.5): Videos have audio descriptions for visual content
   - Color not sole conveyor (1.4.1): Information isn't conveyed by color alone
   - Contrast ratio (1.4.3): Text contrast ≥4.5:1 for normal text
   - Text resizable (1.4.4): Content remains readable when text enlarged to 200%
   Score: 1=No alt text, captions, or descriptions; 5=Full coverage of all above

2. **Operable** (1-5)
   - Keyboard accessibility (2.1.1): All functionality accessible via keyboard
   - No keyboard traps (2.1.2): Users can navigate away from any element
   - Adjustable timing (2.2.1): Users can extend time limits for tasks
   - Skip navigation (2.4.1): Links to skip repetitive content present
   - Descriptive titles (2.4.2): Page/section titles clearly describe content
   - Logical focus order (2.4.3): Tab order follows logical sequence
   - Descriptive link text (2.4.4): Links have meaningful text (not "click here")
   Score: 1=Not keyboard accessible; 5=Full keyboard nav, no traps, clear focus

3. **Understandable** (1-5)
   - Language identified (3.1.1): Page language explicitly set
   - Consistent navigation (3.2.3): Navigation patterns consistent across pages
   - Consistent identification (3.2.4): Components identified consistently
   - Error identification (3.3.1): Errors clearly identified to user
   - Labels and instructions (3.3.2): Form fields have clear labels
   - Error suggestions (3.3.3): Errors provide suggestions for correction
   Score: 1=No language set, inconsistent nav, no error handling; 5=Fully compliant

4. **Robust** (1-5)
   - Valid HTML (4.1.1): Code passes WCAG validation
   - Name/role/value (4.1.2): UI components have accessible names and roles
   - ARIA usage (4.1.2): ARIA correctly applied (not redundantly or incorrectly)
   - Assistive tech compatibility: Content works with screen readers, keyboard nav
   Score: 1=Invalid HTML, broken screen reader support; 5=Valid, ARIA correct, full AT support

5. **Universal Design for Learning Integration** (1-5)
   - Multiple means of representation: Content in text, audio, visual, interactive formats
   - Multiple means of action/expression: Learners can interact via keyboard, mouse, touch, voice
   - Multiple means of engagement: Choices in learning pace, difficulty, content type
   - Alternative formats: PDFs accessible, transcripts provided, captions included
   - Flexible assessment: Not dependent on single modality (vision, hearing, motor control)
   Score: 1=Single format/modality only; 5=Multiple formats, flexible engagement

6. **Remediation Feasibility** (1-5)
   - Surface-level issues (quick fixes): Missing alt text, contrast ratio, missing captions
   - Structural issues (significant effort): No keyboard nav requires code refactor, invalid HTML
   - Architectural barriers (rebuild required): Flash content, unsupported technologies
   Score: 5=Quick fixes only; 1=Requires architectural rebuild

Return only a valid JSON object with keys: perceivable, operable, understandable, robust, udl_integration, remediation_feasibility.
Each key should map to an integer 1-5.
Include a "summary" key with 1-2 sentences explaining the overall accessibility level and priority fixes needed.
"""

JUDGE_HUMAN_PROMPT = """Evaluate the following web-based learning content for WCAG 2.1 compliance.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object."""

register_archetype(
    name="wcag_accessibility",
    system_prompt=JUDGE_SYSTEM_PROMPT,
    human_prompt=JUDGE_HUMAN_PROMPT,
    description="Evaluates web-based learning content, LMS pages, and e-learning modules for WCAG 2.1 compliance and UDL integration. Scores: Perceivable, Operable, Understandable, Robust, UDL Integration, Remediation Feasibility.",
)
