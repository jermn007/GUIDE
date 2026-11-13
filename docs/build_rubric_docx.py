#!/usr/bin/env python3
"""Rebuild the ten archetype sections of GUIDE_Rubric_Document.docx from archetypes/handoff_*.md.

The printable rubric has hand-written front and back matter (executive summary,
introduction, calibration example, severity flagging, coverage matrix, crosswalk,
implementation guide, references). Its ten archetype sections used to be hand-written
too, and drifted from the rubrics. This script regenerates those sections from the
canonical handoffs, so the printable rubric cannot say something the rubrics do not.

What it does, in place, on GUIDE_Rubric_Document.docx:
1. Replaces everything from "Archetype 01" up to "Severity Flagging" with a print
   edition of each handoff: the sections build_skill.py keeps for the skill, minus
   the JSON output shape and data-format notes.
2. Stamps the cover with GUIDE_VERSION and the release month from CITATION.cff.
3. Replaces the table of contents with a Word TOC field (headings 1-2).
4. Recomputes the archetype 10 column of the coverage matrix from handoff 10.
5. Accessibility: marks the first row of every table as a repeating header row, sets
   alt text on the three-alignments figure, and re-embeds assets/three-alignments.png.
6. If Word is installed (Windows, pywin32), opens the file to update the TOC page
   numbers. Without Word the TOC updates the first time the file is opened.

Run from the repo root:
    python docs/build_rubric_docx.py
    python docs/build_rubric_docx.py --pdf out.pdf     (also export a PDF; needs Word)
    python docs/build_rubric_docx.py --check           (fail if the file is out of date)

Needs python-docx. Edit the handoffs or this script, never the generated sections.
"""
from __future__ import annotations

import argparse
import copy
import datetime as _dt
import hashlib
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from docx.table import Table
from docx.text.paragraph import Paragraph

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "skill"))
import build_skill  # noqa: E402  (GUIDE_VERSION, slim_handoff, split_sections)

DOCX = REPO_ROOT / "GUIDE_Rubric_Document.docx"
ARCHETYPES_DIR = REPO_ROOT / "archetypes"
FIGURE_PNG = REPO_ROOT / "assets" / "three-alignments.png"
CITATION = REPO_ROOT / "CITATION.cff"

FIRST_GENERATED = "Archetype 01"          # Heading 1 that opens the generated block
AFTER_GENERATED = "Severity Flagging"     # Heading 1 that follows it
TOC_HEADING = "Table of Contents"
MATRIX_FIRST_CELL = "Theoretical Framework"
# H2 sections of the skill edition that are not useful on paper.
# "Evaluation Rubric Table" restates anchors the dimension sections already give in full.
PRINT_DROP_H2 = {build_skill.OUTPUT_JSON_HEADING, "Output Format", "Evaluation Rubric Table"}
PRINT_DROP_H3 = {"Data Input Format"}
RENAME_H2 = {"Handoff Documentation": None}  # None = drop the heading line, keep its content
FIGURE_ALT = (
    "Triangle diagram of GUIDE's three quality outcomes. Effective: instruction aligns with theory and research. "
    "Efficient: objectives, strategies, and assessments align with each other. Engaging: instruction aligns with "
    "learners' personal and professional goals."
)
# Coverage-matrix rows (by a word in the row label) -> patterns that count as that framework appearing in a handoff.
MATRIX_PATTERNS = [
    ("Knowles", r"Knowles"), ("Mezirow", r"Mezirow"), ("Ausubel", r"Ausubel"), ("Sweller", r"Sweller|cognitive load"),
    ("Mayer", r"Mayer"), ("Bloom", r"Bloom|Anderson"), ("Mager", r"Mager"), ("Dick, Carey", r"Dick,? (&|and)? ?Carey|Dick/Carey"),
    ("Gagne", r"Gagn"), ("Vygotsky", r"Vygotsky"), ("WCAG", r"WCAG"), ("UDL", r"\bUDL\b"), ("Nielsen", r"Nielsen"),
    ("HPT", r"Van Tiem|HPT model|Gilbert"), ("Campbell", r"Campbell|Snyder|Story Circle"), ("Brown", r"Brown|retrieval practice"),
    ("5E", r"\b5E\b"), ("Neuroscience", r"neuroscien"),
]
PRACTICE_MD = REPO_ROOT / "docs" / "practice.md"
PRACTICE_TITLE = "Practice: Score This, Then Compare"
GENERATED_FIGURE_PREFIX = "GUIDE figure: "
# key -> (PNG rendered by docs/art/render_diagrams.py, caption, alt text)
FIGURES = {
    "addie-map": (
        REPO_ROOT / "assets" / "addie-map.png",
        "the ten archetypes on the five ADDIE phases.",
        "Diagram of the five ADDIE phases with GUIDE's archetypes under each. Analyze: 07 Needs Analysis. Design: 03 "
        "Instructional Sequencing, 08 Story Design, 09 Cognitive Neuroscience. Develop: 04 Multimedia Design, 05 "
        "Accessibility. Implement: 01 Adult Learning Communication. Evaluate: 02 Assessment Design, 06 Formative "
        "Evaluation. Archetype 10, Curriculum Alignment, spans all five phases and checks that objectives, instruction, "
        "and assessment agree.",
    ),
    "review-flow": (
        REPO_ROOT / "assets" / "review-flow.png",
        "the five steps of a review and the four verdict bands.",
        "Diagram of a GUIDE review in five steps. 1 Route: match the draft to one to three archetypes. 2 Read: read each "
        "rubric's six dimensions and anchors. 3 Score: give each dimension the score its anchor matches and quote the "
        "evidence. 4 Flag and fix: raise severity flags and give a fix for every dimension under 4. 5 Verdict: average "
        "the six scores. Verdict bands: below 2.5 redesign, 2.5 to 3.4 revise, 3.5 to 4.4 light revision, 4.5 to 5.0 ship.",
    ),
    "alignment-cap": (
        REPO_ROOT / "assets" / "alignment-cap.png",
        "the three links archetype 10 scores, and its cap rule.",
        "Triangle diagram linking objectives, instructional strategies, and assessments. Archetype 10 scores the three "
        "links: objective and strategy coherence, strategy and assessment coherence, and objective and assessment "
        "coherence. The cap rule: when objective and assessment coherence scores 1 or 2, the overall is capped at 3.0. "
        "Example: an objective that says apply, tested by a recall question.",
    ),
}
CODE_FONT = "Consolas"
INLINE_RE = re.compile(r"(\*\*.+?\*\*|`[^`]+`|(?<![\*\w])\*(?!\s)[^*]+?(?<!\s)\*(?!\w)|\[[^\]]+\]\([^)]+\))")


# --------------------------------------------------------------------------- markdown source

def print_edition(path: Path) -> tuple[str, str]:
    """Return (title, markdown body) of a handoff's print edition."""
    canonical = build_skill.FOOTER_RE.sub("", path.read_text(encoding="utf-8")).rstrip() + "\n"
    slim, _ = build_skill.slim_handoff(canonical, path.name)
    chunks = []
    title = ""
    for h2, chunk in build_skill.split_sections(slim):
        if h2 is None:
            m = re.search(r"^# (.+)$", chunk, re.MULTILINE)
            title = m.group(1).strip() if m else path.stem
            chunk = re.sub(r"^# .+\n", "", chunk, count=1, flags=re.MULTILINE)
            # Author / course / version lines belong to the repository file, not the printed section.
            chunk = re.sub(r"^\*\*(Author|Grounding|Domains|Version):\*\*.*\n", "", chunk, flags=re.MULTILINE)
        elif h2 in PRINT_DROP_H2:
            continue
        elif h2 in RENAME_H2 and RENAME_H2[h2] is None:
            chunk = chunk.split("\n", 1)[1] if "\n" in chunk else ""
        chunks.append(chunk)
    body = "".join(chunks)
    body = body.replace("[`discipline_alignment_crosswalk.md`](discipline_alignment_crosswalk.md)",
                        "the Discipline Alignment Crosswalk section")
    body = re.sub(r"\s*—\s*", " - ", body)
    # Drop H3 blocks that only describe harness data formats.
    out, skipping = [], False
    in_fence = False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("#"):
            skipping = line.startswith("### ") and line[4:].strip() in PRINT_DROP_H3
        if not skipping:
            out.append(line)
    return title, "\n".join(out)


def heading_title(number: int, raw_title: str) -> str:
    """'Archetype 2: Assessment Design Quality' -> 'Archetype 02: Assessment Design Quality'."""
    name = re.sub(r"^(Archetype\s*\d*\s*[:\-]\s*)+", "", raw_title).strip()
    return f"Archetype {number:02d}: {name}"


# --------------------------------------------------------------------------- docx writing

class Writer:
    """Appends rendered blocks to the document body just before a marker element."""

    def __init__(self, doc, marker):
        self.doc = doc
        self.marker = marker

    def _place(self, element):
        self.marker.addprevious(element)

    def paragraph(self, text: str = "", style: str | None = None, indent: float = 0.0) -> Paragraph:
        p = self.doc.add_paragraph(style=style)
        self._place(p._p)
        if style == "List Paragraph":
            # Hanging indent, so wrapped lines align with the text and not the bullet.
            p.paragraph_format.left_indent = Pt(22 + indent)
            p.paragraph_format.first_line_indent = Pt(-11)
            p.paragraph_format.space_after = Pt(2)
        else:
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            if indent:
                p.paragraph_format.left_indent = Pt(indent)
        if text:
            add_inline(p, text)
        return p

    def heading(self, text: str, level: int, page_break: bool = False) -> Paragraph:
        p = self.doc.add_paragraph(style=f"Heading {level}")
        self._place(p._p)
        if page_break:
            p.paragraph_format.page_break_before = True
        add_inline(p, text)
        return p

    def code(self, lines: list[str]) -> None:
        for line in lines:
            p = self.doc.add_paragraph()
            self._place(p._p)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.left_indent = Pt(12)
            run = p.add_run(line if line else " ")
            run.font.name = CODE_FONT
            run.font.size = Pt(8.5)

    def table(self, rows: list[list[str]]) -> None:
        cols = max(len(r) for r in rows)
        table = self.doc.add_table(rows=len(rows), cols=cols)
        self._place(table._tbl)
        table.style = "Table Grid"
        size = Pt(8) if cols >= 5 else Pt(9)
        for r, row in enumerate(rows):
            for c in range(cols):
                cell = table.cell(r, c)
                para = cell.paragraphs[0]
                para.paragraph_format.space_after = Pt(2)
                add_inline(para, row[c] if c < len(row) else "", size=size, bold=(r == 0))
                if r == 0:
                    shade(cell, "DCE6F1")
        mark_header_row(table)
        spacer = self.doc.add_paragraph()
        self._place(spacer._p)
        spacer.paragraph_format.space_after = Pt(4)


def add_inline(paragraph: Paragraph, text: str, size=None, bold: bool = False) -> None:
    """Add text with **bold**, *italic*, `code`, and [label](target) markup as runs."""
    for part in INLINE_RE.split(text):
        if not part:
            continue
        run_bold, italic, code = bold, False, False
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            part, run_bold = part[2:-2], True
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            part, code = part[1:-1], True
        elif part.startswith("[") and part.endswith(")") and "](" in part:
            label, target = part[1:-1].split("](", 1)
            label = label.strip("`")
            part = f"{label} ({target})" if target.startswith("http") and target not in label else label
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            part, italic = part[1:-1], True
        # Nested markup inside bold (e.g. **`code`** or **a *b* c**) is flattened to plain text.
        part = part.replace("**", "").replace("`", "") if (run_bold or italic) else part
        run = paragraph.add_run(part)
        run.bold = True if run_bold else None
        run.italic = True if italic else None
        if code:
            run.font.name = CODE_FONT
        if size is not None:
            run.font.size = size


def shade(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    for old in tc_pr.findall(qn("w:shd")):
        tc_pr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def mark_header_row(table: Table) -> None:
    """Mark the first row as a header that repeats and is announced by screen readers."""
    if not table.rows:
        return
    tr_pr = table.rows[0]._tr.get_or_add_trPr()
    if tr_pr.find(qn("w:tblHeader")) is None:
        el = OxmlElement("w:tblHeader")
        el.set(qn("w:val"), "true")
        tr_pr.append(el)


def split_row(line: str) -> list[str]:
    cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    return [c.strip().replace("\\|", "|") for c in cells]


def render_markdown(writer: Writer, md: str, h2_page_break: tuple[str, ...] = ()) -> None:
    lines = md.split("\n")
    i = 0
    buffer: list[str] = []

    def flush():
        if buffer:
            writer.paragraph(" ".join(s.strip() for s in buffer))
            buffer.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i].rstrip())
                i += 1
            writer.code(block)
            i += 1
            continue
        if not stripped or re.fullmatch(r"-{3,}", stripped):
            flush()
            i += 1
            continue
        m = re.match(r"^(#{2,6})\s+(.*)$", stripped)
        if m:
            flush()
            level = len(m.group(1))
            text = m.group(2).strip()
            if level <= 3:
                writer.heading(text, level, page_break=(level == 2 and text.startswith(h2_page_break) if h2_page_break else False))
            else:
                writer.paragraph(f"**{text.replace('**', '')}**")
            i += 1
            continue
        if stripped.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = split_row(lines[i])
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c) or not any(cells):
                    rows.append(cells)
                i += 1
            if rows:
                writer.table(rows)
            continue
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if m:
            flush()
            depth = len(m.group(1).replace("\t", "    ")) // 2
            marker = m.group(2)
            text = m.group(3)
            # A list item may continue on following indented lines.
            while i + 1 < len(lines) and lines[i + 1].startswith("  ") and lines[i + 1].strip() \
                    and not re.match(r"^\s*([-*+]|\d+[.)])\s+", lines[i + 1]) and not lines[i + 1].strip().startswith("|"):
                i += 1
                text += " " + lines[i].strip()
            if marker == "- [ ]" or text.startswith("[ ] "):
                text = "☐ " + text[4:]
                bullet = ""
            else:
                bullet = "•  " if not marker[0].isdigit() else f"{marker} "
            writer.paragraph(bullet + text, style="List Paragraph", indent=18 * depth)
            i += 1
            continue
        if stripped.startswith(">"):
            flush()
            quoted = stripped.lstrip(">").strip()
            if quoted:
                writer.paragraph(quoted, indent=24)
            i += 1
            continue
        buffer.append(line)
        i += 1
    flush()


# --------------------------------------------------------------------------- document surgery

def body_children(doc):
    return list(doc.element.body)


def heading_element(doc, startswith: str, level: int = 1):
    for child in body_children(doc):
        if child.tag == qn("w:p"):
            para = Paragraph(child, doc)
            if para.style is not None and para.style.name == f"Heading {level}" and para.text.strip().startswith(startswith):
                return child
    raise SystemExit(f"Cannot find the 'Heading {level}' paragraph starting with '{startswith}'")


def remove_between(doc, start, end, keep_start: bool) -> None:
    body = doc.element.body
    removing = False
    for child in body_children(doc):
        if child is start:
            removing = True
            if keep_start:
                continue
        if child is end:
            break
        if removing:
            body.remove(child)


def next_heading1(doc, after):
    seen = False
    for child in body_children(doc):
        if child is after:
            seen = True
            continue
        if seen and child.tag == qn("w:p"):
            para = Paragraph(child, doc)
            if para.style is not None and para.style.name == "Heading 1":
                return child
    raise SystemExit("No Heading 1 after the table of contents")


def insert_toc(doc) -> None:
    """Replace the static contents list with a TOC field Word fills in."""
    toc_heading = heading_element(doc, TOC_HEADING)
    following = next_heading1(doc, toc_heading)
    remove_between(doc, toc_heading, following, keep_start=True)
    p = doc.add_paragraph()
    following.addprevious(p._p)

    def fld(kind):
        run = p.add_run()
        el = OxmlElement("w:fldChar")
        el.set(qn("w:fldCharType"), kind)
        if kind == "begin":
            el.set(qn("w:dirty"), "true")
        run._r.append(el)

    fld("begin")
    run = p.add_run()
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = ' TOC \\o "1-2" \\h \\z \\u '
    run._r.append(instr)
    fld("separate")
    p.add_run("Open this file in Word to fill in the table of contents (right-click here, then Update Field).")
    fld("end")
    brk = doc.add_paragraph()
    following.addprevious(brk._p)
    brk.add_run().add_break(WD_BREAK.PAGE)


def release_month() -> str:
    m = re.search(r"^date-released:\s*(\d{4})-(\d{2})-(\d{2})", CITATION.read_text(encoding="utf-8"), re.MULTILINE)
    if not m:
        return ""
    return _dt.date(int(m.group(1)), int(m.group(2)), 1).strftime("%B %Y")


def stamp_cover(doc) -> None:
    for para in doc.paragraphs[:40]:
        if para.text.strip().startswith("Version:"):
            text = f"Version: {build_skill.GUIDE_VERSION} | {release_month()}"
            for run in para.runs[1:]:
                run._r.getparent().remove(run._r)
            if para.runs:
                para.runs[0].text = text
            else:
                para.add_run(text)
            return
    raise SystemExit("Cannot find the cover's 'Version:' line")


FRONT_MATTER_SWAPS = {
    "Configure a LangChain/LangSmith evaluation pipeline using the provided judge prompts":
        "Find the judge prompts and Python runners for each archetype in the GUIDE repository (archetypes/), "
        "for use in an automated evaluation pipeline",
    "Read the introductory paragraph and 'When to use' callout to confirm fit.":
        "Read its Purpose and Use Cases to confirm fit.",
    "Read each theoretical foundation and scoring table":
        "Read each dimension's definition and scoring anchors",
    "Use the source materials as a tiebreaker when you are between two scores.":
        "When you are between two scores, re-read both anchors and take the one the evidence matches more closely.",
    "A composite score above 4.0 indicates strong alignment with research-based practice. Scores below 3.0 suggest "
    "significant redesign may be needed.":
        "A composite of 4.5 or above is ready to ship; 3.5 to 4.4 needs light revision; 2.5 to 3.4 needs revision before "
        "wide rollout; below 2.5 calls for redesign.",
    "'Generally well-organized with good signaling. Minor lapses in definition or grouping.'":
        "'Well-organized; one term used before defined or one minor structural slip.'",
    "Functional and friendly response that answers the question. Key weakness":
        "Archetype 01's overall is not a plain mean (that would be 3.67): Accuracy & Grounding and Adult Learning "
        "Alignment weigh most, and Accuracy at 3 pulls it down. A functional, friendly response that answers the "
        "question. Key weakness",
    "Dolcos, F., LaBar, K.S., & Cabeza, R. (2005).": "Dolcos, F., LaBar, K.S., & Cabeza, R. (2004).",
    "weigh most, and Accuracy at 3 pulls it down. A functional":
        "weigh most, and Accuracy at 3 pulls it down. A judge may report this overall as a whole number; the decimal "
        "is shown here to make the weighting visible. A functional",
}

# The worked calibration example scores archetype 01, whose overall is weighted.
CALIBRATION_OVERALL = ("3.7", "3.6")

# Works the archetype sections cite that the hand-written back-matter list lacked.
EXTRA_REFERENCES = [
    "Bjork, R.A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & "
    "A.P. Shimamura (Eds.), Metacognition: Knowing about Knowing (pp. 185-205). MIT Press.",
    "Craik, F.I.M., & Lockhart, R.S. (1972). Levels of processing: A framework for memory research. Journal of "
    "Verbal Learning and Verbal Behavior, 11(6), 671-684.",
    "Kosslyn, S.M., Thompson, W.L., & Ganis, G. (2006). The Case for Mental Imagery. Oxford University Press.",
    "Shepard, R.N., & Metzler, J. (1971). Mental rotation of three-dimensional objects. Science, 171(3972), 701-703.",
    "Association for Talent Development. (2020). Talent Development Capability Model. ATD.",
    "Baldwin, T.T., & Ford, J.K. (1988). Transfer of training. Personnel Psychology, 41(1), 63-105.",
    "Bloom, B.S. (Ed.). (1956). Taxonomy of Educational Objectives: The Classification of Educational Goals. "
    "Handbook I: Cognitive Domain. David McKay.",
    "Gilbert, T.F. (1978). Human Competence: Engineering Worthy Performance. McGraw-Hill.",
    "Kaufman, R., & Valentine, G. (1999). Operational processes for needs assessment. Training & Development, "
    "53(7), 20-27.",
    "Koszalka, T.A., Russ-Eft, D.F., & Reiser, R. (2013). Instructional Designer Competencies: The Standards "
    "(4th ed.). Information Age Publishing.",
    "Trewin, S. (2020). AI Fairness for People with Disabilities.",
    "Van Tiem, D.M., Moseley, J.L., & Dessinger, J.C. (2012). Fundamentals of Performance Improvement: Optimizing "
    "Results through People, Process, and Organizations (3rd ed.). Pfeiffer / ISPI.",
    "Yerkes, R.M., & Dodson, J.D. (1908). The relation of strength of stimulus to rapidity of habit-formation. "
    "Journal of Comparative Neurology and Psychology, 18(5), 459-482.",
]


def replace_in_paragraph(para: Paragraph, old: str, new: str) -> bool:
    """Replace text that may span several runs, keeping the formatting of the run it starts in."""
    runs = para.runs
    full = "".join(r.text for r in runs)
    at = full.find(old)
    if at == -1:
        return False
    pos = 0
    first = True
    for run in runs:
        start, end = pos, pos + len(run.text)
        pos = end
        if end <= at or start >= at + len(old):
            continue
        keep_before = run.text[: max(at - start, 0)]
        keep_after = run.text[at + len(old) - start:] if end > at + len(old) else ""
        run.text = keep_before + (new if first else "") + keep_after
        first = False
    return True


def fix_front_matter(doc) -> None:
    """Corrections to hand-written text that the generated sections would otherwise contradict.

    Each swap is a no-op once applied, so the script stays safe to re-run.
    """
    for p in doc.element.body.iter(qn("w:p")):
        para = Paragraph(p, doc)
        for old, new in FRONT_MATTER_SWAPS.items():
            replace_in_paragraph(para, old, new)
    fix_calibration_overall(doc)
    add_missing_references(doc)


def fix_calibration_overall(doc) -> None:
    """Show archetype 01's weighted overall in the worked example, not the plain mean."""
    old, new = CALIBRATION_OVERALL
    for table in doc.tables:
        for row in table.rows:
            cells = row.cells
            if len(cells) >= 2 and cells[0].text.strip() == "OVERALL" and cells[1].text.strip() == old:
                for para in cells[1].paragraphs:
                    replace_in_paragraph(para, old, new)


def add_missing_references(doc) -> None:
    """Insert EXTRA_REFERENCES into the back-matter list, in alphabetical order, once."""
    start = heading_element(doc, "References")
    entries = []
    el = start.getnext()
    while el is not None:
        if el.tag == qn("w:p"):
            para = Paragraph(el, doc)
            if para.text.strip():
                entries.append(para)
        el = el.getnext()
    if not entries:
        raise SystemExit("The References section has no entries")
    for ref in EXTRA_REFERENCES:
        key = ref.split(")")[0].strip().lower()
        if any(e.text.strip().lower().startswith(key) for e in entries):
            continue
        after = [e for e in entries if e.text.strip().lower() > ref.lower()]
        new_p = copy.deepcopy(entries[0]._p)
        para = Paragraph(new_p, doc)
        for run in para.runs[1:]:
            run._r.getparent().remove(run._r)
        para.runs[0].text = ref
        if after:
            after[0]._p.addprevious(new_p)
            entries.insert(entries.index(after[0]), para)
        else:
            entries[-1]._p.addnext(new_p)
            entries.append(para)


def update_matrix(doc, handoff_text: dict[int, str]) -> None:
    """Give the coverage matrix an archetype 10 column, computed from handoff 10."""
    table = next((t for t in doc.tables if t.rows and t.rows[0].cells[0].text.strip().startswith(MATRIX_FIRST_CELL)), None)
    if table is None:
        raise SystemExit("Cannot find the coverage matrix")
    header = [c.text.strip() for c in table.rows[0].cells]
    if "10" not in header:
        for row in table.rows:
            cells = row._tr.findall(qn("w:tc"))
            row._tr.append(copy.deepcopy(cells[-1]))
        grid = table._tbl.find(qn("w:tblGrid"))
        if grid is not None:
            cols = grid.findall(qn("w:gridCol"))
            grid.append(copy.deepcopy(cols[-1]))
    col = len(table.rows[0]._tr.findall(qn("w:tc"))) - 1
    text10 = handoff_text[10]

    def set_cell(row, value):
        tc = row._tr.findall(qn("w:tc"))[col]
        texts = tc.findall(".//" + qn("w:t"))
        if texts:
            texts[0].text = value
            for extra in texts[1:]:
                extra.text = ""
        else:
            from docx.table import _Cell
            _Cell(tc, table).paragraphs[0].add_run(value)

    set_cell(table.rows[0], "10")
    for row in table.rows[1:]:
        label = row.cells[0].text
        pattern = next((pat for key, pat in MATRIX_PATTERNS if key.lower() in label.lower()), None)
        hit = bool(pattern and re.search(pattern, text10, re.IGNORECASE))
        set_cell(row, "✓" if hit else " ")


def accessibility_pass(doc) -> None:
    for table in doc.tables:
        mark_header_row(table)
    # The hand-placed three-alignments figure: alt text, and the current rendering of its PNG.
    for drawing in doc.element.body.iter(qn("w:drawing")):
        doc_pr = next(drawing.iter(qn("wp:docPr")), None)
        if doc_pr is None or (doc_pr.get("title") or "").startswith(GENERATED_FIGURE_PREFIX):
            continue
        doc_pr.set("descr", FIGURE_ALT)
        doc_pr.set("title", "GUIDE three alignments diagram")
        blip = next(drawing.iter(qn("a:blip")), None)
        rel_id = blip.get(qn("r:embed")) if blip is not None else None
        if rel_id and FIGURE_PNG.exists():
            doc.part.rels[rel_id].target_part._blob = FIGURE_PNG.read_bytes()


def remove_generated_figures(doc) -> None:
    """Remove figures an earlier run placed in the hand-written sections, so a re-run does not stack them."""
    body = doc.element.body
    for drawing in list(body.iter(qn("w:drawing"))):
        doc_pr = next(drawing.iter(qn("wp:docPr")), None)
        if doc_pr is None or not (doc_pr.get("title") or "").startswith(GENERATED_FIGURE_PREFIX):
            continue
        para = drawing.getparent()
        while para is not None and para.tag != qn("w:p"):
            para = para.getparent()
        if para is None:
            continue
        caption = para.getnext()
        if caption is not None and caption.tag == qn("w:p") and Paragraph(caption, doc).text.startswith("Figure:"):
            caption.getparent().remove(caption)
        para.getparent().remove(para)


def add_figure(doc, after, key: str) -> None:
    """Insert a generated figure and its caption after a body element."""
    png, caption, alt = FIGURES[key]
    if not png.exists():
        raise SystemExit(f"Missing {png}: run python docs/art/render_diagrams.py")
    cap = doc.add_paragraph()
    after.addnext(cap._p)
    run = cap.add_run(f"Figure: {caption}")
    run.italic = True
    run.font.size = Pt(9)
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic = doc.add_paragraph()
    after.addnext(pic._p)
    pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pic.paragraph_format.keep_with_next = True
    pic.add_run().add_picture(str(png), width=Inches(6.0))
    doc_pr = next(pic._p.iter(qn("wp:docPr")))
    doc_pr.set("descr", alt)
    doc_pr.set("title", GENERATED_FIGURE_PREFIX + key)


def practice_markdown() -> str:
    """docs/practice.md as plain markdown: HTML disclosure tags dropped, links reduced to their labels."""
    text = PRACTICE_MD.read_text(encoding="utf-8").replace("\r\n", "\n")
    text = re.sub(r"^# .+\n", "", text, count=1)
    text = re.sub(r"^</?details>\s*\n", "", text, flags=re.MULTILINE)
    text = re.sub(r"^<summary>.*</summary>\s*\n", "", text, flags=re.MULTILINE)
    text = text.replace("[`archetypes/`](../archetypes) holds one `handoff_NN_*.md` file per archetype, and the printable "
                        "rubric has the same text.", "The archetype sections of this document hold the anchors.")
    return re.sub(r"\s*—\s*", " - ", text)


def build() -> None:
    doc = Document(str(DOCX))
    remove_generated_figures(doc)
    start = heading_element(doc, FIRST_GENERATED)
    end = heading_element(doc, AFTER_GENERATED)
    remove_between(doc, start, end, keep_start=False)

    writer = Writer(doc, end)
    handoff_text: dict[int, str] = {}
    paths = sorted(ARCHETYPES_DIR.glob("handoff_*.md"))
    if len(paths) != build_skill.TOTAL_ARCHETYPES:
        raise SystemExit(f"Found {len(paths)} handoffs, expected {build_skill.TOTAL_ARCHETYPES}")
    for path in paths:
        number = int(re.search(r"handoff_(\d{2})_", path.name).group(1))
        title, body = print_edition(path)
        handoff_text[number] = body
        h1 = writer.heading(heading_title(number, title), 1, page_break=True)
        render_markdown(writer, body)
        if number == 10:
            add_figure(doc, h1._p, "alignment-cap")
    # Practice exercises and the spaced-review schedule close the generated block.
    writer.heading(PRACTICE_TITLE, 1, page_break=True)
    render_markdown(writer, practice_markdown(), h2_page_break=("Part 2", "Answers"))
    # The section after the generated block starts on its own page.
    Paragraph(end, doc).paragraph_format.page_break_before = True

    stamp_cover(doc)
    fix_front_matter(doc)
    add_figure(doc, heading_element(doc, "Quick-Reference", level=2), "addie-map")
    add_figure(doc, heading_element(doc, "How to Use This Document", level=2), "review-flow")
    insert_toc(doc)
    update_matrix(doc, handoff_text)
    accessibility_pass(doc)
    props = doc.core_properties
    props.title = "GUIDE: Complete Evaluation Rubric and Citation Guide"
    props.subject = f"GUIDE v{build_skill.GUIDE_VERSION}"
    props.language = "en-US"
    props.comments = "Archetype sections generated from archetypes/handoff_*.md by docs/build_rubric_docx.py. sources=" + sources_digest()
    doc.save(str(DOCX))


def sources_digest() -> str:
    """A fingerprint of everything the generated sections depend on."""
    h = hashlib.sha256()
    for path in sorted(ARCHETYPES_DIR.glob("handoff_*.md")):
        h.update(path.read_bytes().replace(b"\r\n", b"\n"))
    h.update(build_skill.GUIDE_VERSION.encode())
    h.update(Path(__file__).read_bytes().replace(b"\r\n", b"\n"))
    h.update(PRACTICE_MD.read_bytes().replace(b"\r\n", b"\n"))
    for png in [FIGURE_PNG] + [fig[0] for fig in FIGURES.values()]:
        if png.exists():
            h.update(png.read_bytes())
    return h.hexdigest()[:16]


def is_current() -> bool:
    comments = Document(str(DOCX)).core_properties.comments or ""
    return f"sources={sources_digest()}" in comments


def refresh_in_word(pdf: Path | None) -> bool:
    """Update the TOC (and optionally export a PDF) with Word, when Word is available."""
    try:
        import win32com.client  # type: ignore
    except ImportError:
        return False
    word = None
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        document = word.Documents.Open(str(DOCX))
        for toc in document.TablesOfContents:
            toc.Update()
        document.Save()
        if pdf is not None:
            document.SaveAs(str(pdf.resolve()), FileFormat=17)
        document.Close(False)
        return True
    except Exception as exc:  # Word missing or automation blocked: the docx is still valid
        print(f"  Word step skipped: {exc}")
        return False
    finally:
        if word is not None:
            word.Quit()


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild the printable rubric's archetype sections from the handoffs.")
    parser.add_argument("--check", action="store_true", help="exit 1 if the docx is older than its sources; write nothing")
    parser.add_argument("--pdf", type=Path, help="also export a PDF to this path (needs Word)")
    parser.add_argument("--no-word", action="store_true", help="skip the Word step that fills in TOC page numbers")
    args = parser.parse_args()
    if args.check:
        ok = is_current()
        print("Printable rubric is current." if ok else "Printable rubric is out of date: run python docs/build_rubric_docx.py")
        return 0 if ok else 1
    build()
    print(f"Rebuilt {DOCX.name} archetype sections at GUIDE v{build_skill.GUIDE_VERSION}.")
    if not args.no_word:
        if refresh_in_word(args.pdf):
            print("Updated the table of contents in Word." + (f" PDF: {args.pdf}" if args.pdf else ""))
        else:
            print("Word not available: the table of contents fills in when the file is first opened in Word.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
