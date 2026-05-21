# NOTICE — Source and Attribution

This skill packages content from the **GUIDE** project.

**GUIDE — Grounded Universal Instructional Design Evaluator**
Version 3.0.2
Repository: https://github.com/jermn007/GUIDE
Copyright 2026 Jeremy Terhune.
Licensed under the Apache License, Version 2.0 (the "License"). You may not use these files except in
compliance with the License. A copy of the License is available at:
https://www.apache.org/licenses/LICENSE-2.0

GUIDE was developed as a capstone synthesis of the author's work in the University of Central Florida
Master of Arts in Instructional Systems program. It applies the LLM-as-a-judge pattern
(Zheng et al., 2023) to instructional-design evaluation across 9 archetypes and 54 theory-grounded
dimensions.

## What is bundled here

The nine `handoff_0X_*.md` files in this directory are GUIDE's "model-agnostic handoff documents,"
reproduced for use inside this skill so the rubrics, grounding text, scoring anchors, judge prompts,
and output formats are available without depending on the upstream codebase. They correspond to the
files under `archetypes/` in the GUIDE repository.

`00_archetype_index.md` is a condensed routing index created for this skill; it summarizes and points
to the handoff documents, which remain the authoritative source.

## Modifications

Content is reproduced substantively verbatim from the GUIDE handoff documents. The only changes are:
formatting normalization (e.g., code-fence indentation), and an attribution footer appended to each
bundled file. No dimension definitions, scoring anchors, grounding text, or citations were altered.

## Theoretical sources

GUIDE draws on 20+ named sources across instructional design, cognitive science, and narrative theory,
including Knowles (1980), Mezirow (1991), Ausubel (2000), Bloom (1956) / Anderson & Krathwohl (2001),
Gagné (1985), Mayer (2009), Sweller (1988), Mager (1997), Keller (1987, 2010 — ARCS), Campbell (1949),
Snyder (2005), Brown, Roediger & McDaniel (2014), Dick, Carey & Carey (2015), Van Tiem et al. (2000),
WCAG 2.1 (W3C WAI, 2018), CAST UDL (2018), Nielsen (1994), and Zheng et al. (2023). Full citations
appear in the individual handoff documents.
