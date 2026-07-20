---
name: document-qa
description: Pre-signoff QA scan for a Word/PDF deliverable. Catches the "simple things" that get missed by eyeballing — duplicate/missing figure & table labels, captions orphaned in text boxes, figures/tables with no caption or no in-text callout, inconsistent table formatting (header shading, borders, first-column bold, cell font), inconsistent caption style, leftover scaffolding/placeholders, and heading-hierarchy outliers. Run BEFORE calling any docx/pdf "done" or "camera-ready". Complements document-format-fidelity (which matches a reference's LOOK); this checks internal CONSISTENCY and completeness.
metadata:
  type: reference
  integration_status: (b) demonstrated 2026-07-20 on RTSync DLA DTO Technical Volume
---

# /document-qa

The consistency-and-completeness arm of the document-QA SOP. Exists because "is it camera-ready?" kept getting answered "yes" while duplicate Figure-1 captions, an unnumbered table, and two deliverable tables sat in plain sight. Eyeballing misses these; a scan does not. See [[feedback_holistic_formatting_fidelity]], [[feedback_formatting_verify_visually]], [[project_document_qa_procedure]].

## When to use

Run this BEFORE telling the principal a `.docx`/PDF is done, camera-ready, or ready to send. Also run it after ANY multi-edit pass on a deliverable, and after the principal hand-edits a file (to confirm nothing regressed and their style is applied consistently).

Do NOT rely on attribute inspection alone — this scan is necessary but NOT sufficient. It is paired with the render-and-look gate: after the scan is clean, still render to PDF and LOOK at every figure page, table page, and heading ([[feedback_formatting_verify_visually]]).

## The two-part gate (both required)

1. **Automated scan** — run `check.py` (below). Resolve every FAIL and review every WARN.
2. **Render and look** — convert to PDF (LibreOffice headless) and view each figure/table/heading region as an image. Attributes mislead (a shaded-in-XML header can render invisible; a "consistent" table can have a bold first column the scan flags but you must confirm the fix visually).

Signoff is blocked until BOTH pass. "The scan is clean" is not "done"; "I looked at one page" is not "done".

## How to run the scan

```bash
python "C:/Users/pfwac/OneDrive - University of Arizona/Documents/03 Projects/00_Hive_Empire/01 Hives/01 PostWach/.claude/skills/document-qa/check.py" "<path-to.docx>"
```

Stdlib + python-docx only. Copy the file to a local temp path first if it lives on OneDrive (cloud placeholders intermittently fail to open as a zip).

## What it checks (and the misses each one prevents)

| Check | The real miss it prevents |
|---|---|
| **Duplicate labels** — same "Figure N"/"Table N" caption appears >1× | Two "Figure 1" captions (one left in a floating text box) |
| **Caption sequence** — gaps/dupes in Figure/Table numbering | "Table 2" missing because only Table 1 was labeled |
| **Textbox captions** — captions living in `w:txbxContent` | Orphaned old captions the body-paragraph search can't see |
| **Caption presence** — every figure/table has a caption; every caption has a figure/table | Unlabeled table; caption with no object |
| **In-text callouts** — every Figure N / Table N referenced by number in prose | A numbered table nothing points to |
| **Table consistency** — header fill, borders, first-column bold, cell font size across all tables | Table 5's bold "Year" column; Table with different header shade |
| **Caption-style consistency** — "Label N." prefix-bold pattern + size uniform | One caption all-bold, others prefix-bold; 9pt vs 10pt |
| **Duplicate tables** — two tables with near-identical header/purpose | Two deliverable tables |
| **Scaffolding** — `[Define…]`, `[cite…]`, `[PLACEHOLDER]`, `TBD`/`TODO`, `(include Subcontractors…)` | Template prompts and unfilled cite markers shipped |
| **Heading hierarchy** — top-level section header size/bold outliers | "Related Work" 12pt while siblings are 10pt; a section not bold |

## How to read the output

- **FAIL** — a definite defect. Fix before signoff.
- **WARN** — likely a defect or a judgment call (e.g., a table's bold first column may be an intentional row-label; confirm intent, then make it consistent either way).
- **INFO** — inventory (counts of figures/tables/refs) for a sanity check.

## After the scan

For every FAIL/WARN, fix it in the deliverable, re-run the scan to confirm zero FAILs, THEN render and look. Only then report status — and report what the scan verified, not "looks good".

## Related
- `/document-format-fidelity` — match a reference document's rendered LOOK (fonts, margins, booktabs). Different job: that matches an external target; this checks internal consistency/completeness.
- `/refcheck`, `/reflookup`, `/refverify` — the R019 citation gate (deeper reference verification than this scan's scaffolding check).
