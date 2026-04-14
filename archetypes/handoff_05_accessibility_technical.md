# Archetype 5: WCAG/POUR Technical Accessibility

**Purpose**: Evaluate web-based learning content, LMS pages, and e-learning modules for compliance with WCAG 2.1 standards and Universal Design for Learning (UDL) principles.

**Evaluation Context**: Use this archetype when assessing:
- Learning management system (LMS) pages and course shells
- E-learning modules and interactive tutorials
- Web-based assessments and quizzes
- Learning videos with captions and descriptions
- Accessible digital course materials and content libraries
- Responsive learning experiences across devices
- Synchronous and asynchronous online learning platforms

---

## Rubric: 6 Dimensions (1-5 Scale)

### 1. Perceivable (1-5)

Content must be perceivable to all users regardless of sensory ability.

| Score | Alt Text / Captions | Audio Description | Color Conveyal | Contrast (≥4.5:1) | Resizable to 200% |
|-------|---------------------|-------------------|-----------------|------------------|------------------|
| **1** | No alt text; images unlabeled | No audio descriptions | Color only method | <4.5:1 contrast | Text fails at 200% |
| **2** | Some alt text, inconsistent | Minimal descriptions | Mixed approaches | Borderline contrast | Some zoom failure |
| **3** | Most images have alt text | Some key videos described | Mostly alternative cues | Most at 4.5:1 | Mostly resizable |
| **4** | Nearly all alt text; minor gaps | Key media has descriptions | Alternative cues throughout | 4.5:1+ except decorative | Fully resizable with minor issues |
| **5** | All non-text content alt text; graphs detailed | All video/audio has descriptions | Never color-sole conveyor | All text 4.5:1+, enhanced for graphics | 200% resize fully functional |

**Key WCAG Criteria**: 1.1.1 (Non-text Content), 1.2.2 (Captions), 1.2.5 (Audio Description), 1.4.1 (Color Use), 1.4.3 (Contrast), 1.4.4 (Resize Text)

---

### 2. Operable (1-5)

All functionality must be accessible via keyboard and interfaces must be navigable.

| Score | Keyboard Access | No Keyboard Traps | Timing Control | Skip Links | Focus Order | Link Text |
|-------|-----------------|-------------------|-----------------|-----------|------------|-----------|
| **1** | Mouse-only; not keyboard accessible | Keyboard trapped on elements | No time extension | None | Random order | Generic ("click here") |
| **2** | Some keyboard access; gaps remain | Trap on one or two elements | Limited time control | Present but unclear | Mostly logical | Some generic text |
| **3** | Most features keyboard accessible | Rare traps | Adjustable timing | Skip link present | Mostly logical order | Mostly descriptive |
| **4** | Nearly all keyboard accessible | No traps; minor nav issue | Timing adjustable; rarely needed | Clear skip links | Logical focus order | Nearly all descriptive |
| **5** | All functionality keyboard accessible | No traps anywhere | All timing adjustable | Clear, well-positioned | Perfect logical order | All links descriptive and meaningful |

**Key WCAG Criteria**: 2.1.1 (Keyboard), 2.1.2 (No Keyboard Trap), 2.2.1 (Timing), 2.4.1 (Skip), 2.4.2 (Page Titled), 2.4.3 (Focus Order), 2.4.4 (Link Purpose)

---

### 3. Understandable (1-5)

Content and interaction must be clear and predictable.

| Score | Language Set | Consistent Navigation | Error Messages | Form Labels | Error Recovery | Readable Text |
|-------|-------------|----------------------|-----------------|------------|-----------------|--------|
| **1** | No language; scripts broken | Inconsistent nav patterns | No error messages | Missing labels | No suggestions | Jargon-heavy, unclear |
| **2** | Language set but wrong | Some inconsistency | Vague error messages | Some labels missing | Minimal suggestions | Some unclear passages |
| **3** | Language set correctly | Mostly consistent | Errors identified clearly | Most fields labeled | Basic suggestions | Generally clear |
| **4** | Language set; minor issues | Consistent except minor | Errors identified with context | Nearly all labeled | Good suggestions | Clear language, minimal jargon |
| **5** | Language explicit and correct | Perfectly consistent | Errors with context and solutions | All clearly labeled | Specific recovery steps | Simple, clear language throughout |

**Key WCAG Criteria**: 3.1.1 (Language), 3.2.3 (Consistent Navigation), 3.2.4 (Consistent Identification), 3.3.1 (Error Identification), 3.3.2 (Labels or Instructions), 3.3.3 (Error Suggestion)

---

### 4. Robust (1-5)

Code must be valid and compatible with assistive technologies.

| Score | HTML Validity | Name/Role/Value | ARIA Usage | Screen Reader Support | AT Compatibility |
|-------|-------------|-----------------|-----------|----------------------|------------------|
| **1** | Major validation errors | Missing components | Missing or incorrect | Broken; key content inaccessible | Not tested |
| **2** | Several validation errors | Incomplete implementation | Some ARIA errors | Partial support; gaps | Limited testing |
| **3** | Minor HTML issues | Mostly implemented | Mostly correct ARIA | Mostly functional | Tested once |
| **4** | Valid HTML; edge cases | Nearly all proper | Correct, minimal redundancy | Fully functional | Tested with multiple AT |
| **5** | Valid HTML throughout | All proper | Correct, no redundancy | Full support, context clear | Fully compatible, tested |

**Key WCAG Criteria**: 4.1.1 (Parsing), 4.1.2 (Name, Role, Value); WAI-ARIA Best Practices

---

### 5. Universal Design for Learning Integration (1-5)

Content provides multiple means of representation, action/expression, and engagement (CAST 2018 UDL Guidelines 2.2).

| Score | Multiple Representations | Flexible Action/Expression | Engagement Flexibility | Alternative Formats | Assessment Modality |
|-------|-------------------------|--------------------------|----------------------|-------------------|-------------------|
| **1** | Single format only (text or video) | Single modality (click, type, drag) | No flexibility in pace/difficulty | Single format; no alternatives | Single modality (test, essay, project) |
| **2** | Two formats present | Two modalities available | Limited options | PDF accessible but limited | Some assessment flexibility |
| **3** | Text + one other format | Keyboard + mouse + touch | Moderate pace/difficulty options | Multiple formats (text, audio, video) | Two assessment options |
| **4** | Text + audio + visual | Multiple modalities (keyboard, mouse, touch, voice) | Good pace, difficulty, content options | Transcripts, captions, descriptions | Multiple assessment methods |
| **5** | Multiple formats (text, audio, visual, interactive) | Multiple accessible modalities | Full flexibility in pace, difficulty, interest | All formats with alternatives | Flexible assessment (multiple means) |

**References**: CAST (2018). Universal Design for Learning Guidelines version 2.2.

---

### 6. Remediation Feasibility (1-5)

How easily can identified accessibility issues be fixed? 5 = quick fixes only; 1 = major rebuild required.

| Score | Issue Type | Timeline | Effort | Cost | Priority |
|-------|-----------|----------|--------|------|----------|
| **5** | Surface-level: Missing alt text, captions, labels | Days | Single contributor | Low | Medium-High (Quick wins) |
| **4** | Minor structural: Contrast fixes, focus order, simple ARIA | Days-weeks | 1-2 contributors | Low-Medium | High |
| **3** | Moderate: Form restructuring, navigation redesign, UDL addition | Weeks | 2-3 contributors | Medium | High |
| **2** | Significant: Keyboard nav rebuild, JavaScript accessibility refactor | Weeks-months | 3+ contributors | Medium-High | Critical |
| **1** | Architectural: Rebuild required, Flash/plugin removal, major rewrite | Months+ | Full team | High | Critical (Block release) |

**Guidance**: 
- **Score 5-4**: Can be addressed in current sprint or patch cycle
- **Score 3**: Plan for next major release; include in roadmap
- **Score 2-1**: Block release; plan comprehensive accessibility overhaul; consider new framework or rebuild

---

## System Prompt (Judge Rubric)

```
You are an expert in WCAG 2.1 accessibility compliance and Universal Design for Learning (UDL).
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
```

---

## Human Prompt Template

```
Evaluate the following web-based learning content for WCAG 2.1 compliance.

## INPUT / ARTIFACT
{input}

## CONTEXT (if available)
{context}

## OUTPUT / RESPONSE TO EVALUATE
{output}

## REFERENCE (if available)
{reference}

Score using the rubric above. Return only the JSON object.
```

---

## Implementation Notes

### Data Input Format
```json
{
  "artifact_type": "lms_page | elearning_module | video | assessment | course_material",
  "url_or_description": "...",
  "learning_modality": "synchronous | asynchronous | blended",
  "target_audience": "...",
  "device_context": "desktop | mobile | tablet | responsive"
}
```

### Expected Scoring Patterns
- **Accessible content (5-4)**: Typically scores high on Perceivable, Operable, Understandable, Robust; moderate-high on UDL; 5 on Remediation (nothing to fix).
- **Compliance-challenged (3-2)**: Missing captions, low contrast, keyboard issues; lower scores on Operable/Understandable; moderate Remediation.
- **Non-compliant (1)**: No alt text, not keyboard accessible, broken screen reader; high remediation cost; critical priority.

---

## Citation & References

**WCAG 2.1**
- W3C WAI (2018). Web Content Accessibility Guidelines (WCAG) 2.1. https://www.w3.org/WAI/WCAG21/quickref/
- W3C WAI. Introduction to Web Accessibility. https://www.w3.org/WAI/fundamentals/
- W3C WAI. How People with Disabilities Use the Web. https://www.w3.org/WAI/people-use-web/

**UDL**
- CAST (2018). Universal Design for Learning Guidelines version 2.2. http://udlguidelines.cast.org

**Accessibility Best Practices**
- Chrome DevSummit 2015. Accessibility presentation: focus, keyboard, semantics, ARIA, contrast.
- Nielsen, J. (1994). Severity Ratings for Usability Problems (adapted for remediation prioritization).
- Trewin, S. (2020). AI Fairness for People with Disabilities (accessibility and AI intersection).

---

## Common Evaluation Scenarios

### Scenario A: LMS Course Page (Blackboard/Canvas/Moodle)
- Assess: Page template accessibility, navigation, learning materials
- Focus dimensions: Operable (focus order in course nav), Robust (LMS code validity)
- Common issues: Poor contrast, missing form labels, slow keyboard navigation
- Remediation approach: Vendor settings (contrast themes), institutional template fixes

### Scenario B: Interactive E-Learning Module (Articulate, Adobe Captivate)
- Assess: Keyboard nav for interactions, alt text for objects, captions for video
- Focus dimensions: Perceivable (captions, audio description), Operable (interaction keyboard accessibility)
- Common issues: Drag-and-drop without keyboard alternative, video without captions
- Remediation approach: Module rebuild or vendor plugin; caption service needed

### Scenario C: Learning Video (YouTube, Vimeo)
- Assess: Captions, audio description, transcript, player keyboard accessibility
- Focus dimensions: Perceivable (captions, description), Operable (player controls)
- Common issues: Auto-generated captions (often inaccurate), no audio description for visual content
- Remediation approach: Professional captioning/description service, upload to accessible player

### Scenario D: Web-Based Assessment
- Assess: Form accessibility, timer adjustment, error messages, instructions clarity
- Focus dimensions: Operable (timed tests), Understandable (clear instructions), Robust (screen reader support)
- Common issues: Time limits with no extension, unclear error messages, inaccessible question types
- Remediation approach: Backend changes (timer logic), form label fixes, test format redesign

---

## Validation Checklist

Use this before scoring:

- [ ] Content accessible via keyboard alone (navigate entire page without mouse)
- [ ] Screen reader tested (NVDA on Windows, JAWS if available, Safari VoiceOver on Mac)
- [ ] Images have descriptive alt text; decorative images marked (alt="")
- [ ] Videos have captions (SDH: Speaker: dialogue format)
- [ ] Text contrast tested (WebAIM Contrast Checker, DevTools)
- [ ] Text resizable to 200% without overflow
- [ ] Form fields have associated labels (not placeholder-only)
- [ ] Page language set in HTML lang attribute
- [ ] Focus visible and logical throughout
- [ ] No timing traps; adjustable timers where used
- [ ] ARIA used correctly (aria-labels, aria-hidden, landmarks)
- [ ] Tested on mobile/tablet for touch accessibility

---

## Score Interpretation for Stakeholders

| Overall Range | Status | Action |
|--------------|--------|--------|
| **4.5-5.0** | Excellent | Ship as-is; exemplary accessibility |
| **3.5-4.4** | Good | Minor issues; can ship; document known gaps |
| **2.5-3.4** | Fair | Accessibility concerns; plan fixes before wide rollout |
| **1.5-2.4** | Poor | Significant barriers; remediation required; legal risk |
| **<1.5** | Inaccessible | Cannot ship; critical remediation or redesign needed |
