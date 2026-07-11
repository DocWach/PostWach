# Session Archive — 2026-07-10 postwach-04

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m] (main-loop; no subagents, no swarm).
**Focus:** Create a Word version of the P2 dissertation journal manuscript to share the latest draft with co-authors, and add Rao (Hanumanthrao) Kannan as a co-author to both P1 and P2.
> PROVENANCE: run by Claude (Anthropic, Opus 4.8, claude-opus-4-8[1m], Claude Code main-loop) at Paul Wach's direction. P2 LaTeX edited and converted to .docx via pandoc with an aux-based cite/cref resolver; Kannan affiliation web-verified. No agents spawned; no memory-store writes.

## Headline
Delivered the P2 co-author Word draft (**`manuscript_p2/Wach_etal_Necessary_Sufficient_Conditions_Verification_Models_P2_2026-07-10.docx`**, 5.8 MB) with Kannan added, built from `main.tex` (v0.13). P1's identical edit is **staged but not applied** because the P1 `.docx` is open/locked in Word.

## Author change (confirmed with principal + web-verified)
- **Rao Kannan = Hanumanthrao Kannan**, Asst. Prof., **Dept. of Industrial & Systems Engineering and Engineering Management (ISEEM), University of Alabama in Huntsville** (verified via UAH faculty page; NSF CAREER 2025). Frequent Salado co-author (Salado-Kannan 2018; Kannan-Salado 2026).
- **Placement (principal decision):** before Beling. New byline: Wach¹, Salado¹, Zeigler², **Kannan³**, Beling⁴.
- **Affiliations renumbered by first appearance:** ¹ UA SIE, ² RTSync, ³ UAH ISEEM (new), ⁴ UVA Data Science (Beling moved 3→4).

## P2 — done
- Edited `main.tex`: byline, affiliation block (+UAH, Beling→4), `pdfauthor`, header comment.
- Converted LaTeX→Word with pandoc 3.8.3. A naive pass **silently dropped in-text natbib citations** and mishandled cleveref, so the working pipeline is: parse `main.aux` for `\bibcite` (key→number) and `\newlabel{...@cref}` (label→type+number); inline-expand `\input{appendix_proof}`; replace every `\cite/\citep/\citet`→`[n]` (range-compressed) and `\Cref/\cref/\ref/\eqref`→resolved text ("Table 1", "Section 4.2 (Figures 4, 5 and 6)"); splice `main.bbl` with `\bibitem` labels stripped so pandoc auto-numbers 1–36 in citation order.
- **Verified (structural, not visual):** author line correct; 73 numbered `[n]` in-text cites + numbered reference list; 143 equations as native Word math (OMML); 11 embedded figures; 25 tables; 0 raw `[fig:/tab:/sec:]` label leaks.
- Caveat surfaced to principal: verified programmatically, not by opening in Word (COM barred here). Draft-fidelity conversion; canonical typesetting stays in LaTeX/PDF.

## P1 — staged, blocked by open Word
- `01_Dis_Pub_P1_comparison/Wach_etal_Comparing_Approaches_..._P1_2026-07-03.docx` is **locked by a running WINWORD** (confirmed: exclusive-open throws sharing violation; `~$` owner file present). Per standing rule: no force-kill, no Word COM, no overwrite of an open deliverable.
- Prepared **`01_Dis_Pub_P1_comparison/_p1_add_kannan.py`** — a python-docx run-level editor that clones the existing superscript runs to insert ", Hanumanthrao Kannan"³ before Beling and the UAH affiliation line, and renumbers Beling/UVA to 4. Inspected P1's runs from a read-only copy to build it; the script self-aborts with a LOCKED message if the file is still held.
- **To finish:** principal closes Word → run the script → verify. Open question: same first-appearance renumbering as P2 (Beling 3→4) vs. append Kannan as the next superscript without renumbering.

## Files
- Deliverable: `02 My Outreach/2026 - Dis Pub/manuscript_p2/Wach_etal_Necessary_Sufficient_Conditions_Verification_Models_P2_2026-07-10.docx` (created).
- Modified: `manuscript_p2/main.tex` (author block).
- Staged tool: `01_Dis_Pub_P1_comparison/_p1_add_kannan.py` (pending P1 unlock).
- Temp P2 build scripts (`_p2_build.py`, `_p2_word_build.tex`) created then removed after the docx verified.
- Records: this archive; scorecard `2026-07-10-postwach-04.yaml`.

## Method note (why the conversion was not one-shot)
Pandoc's LaTeX reader does not run natbib's numbering: with a spliced compiled `.bbl` it produced a reference list but **no in-text citation markers at all**, and rendered cleveref refs as bare numbers with one multi-label ref leaking raw `[fig:...]`. Resolving from `main.aux` (the source of truth for both citation numbers and cross-ref types) and inlining `\input` files closed both gaps. Also relevant for future sessions: this shell mangles backslashes in inline `python -c`/heredocs, so all regex/preprocessing must live in written `.py` files.

## Hygiene
No agents spawned; no swarm started; no orphaned agents to terminate. No memory-store writes (no R018 store attribution needed beyond this archive's provenance line). No git commit this session (manuscript edits under `02 My Outreach/`, outside the PostWach repo; records here are untracked pending the principal's usual records commit). No `Co-Authored-By: claude-flow` trailer used. **Open item carried forward:** apply `_p1_add_kannan.py` once P1 is closed in Word.
