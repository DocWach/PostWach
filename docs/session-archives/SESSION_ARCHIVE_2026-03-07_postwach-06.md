# Session Archive — 2026-03-07 PostWach-06

## Session Metadata
- **Date:** 2026-03-07
- **Hive:** PostWach
- **Researcher:** Paul F. Wach
- **Duration:** ~2.5 hours (continuation session)
- **Scorecard:** `2026-03-07-postwach-06.yaml`

## Task: Publication Portfolio Catalog and PDF Consolidation

### Objective
Create a comprehensive publication catalog (Excel) and consolidate all publication PDFs into `02 My Outreach/00 Master Copies/`.

### Deliverables

1. **`02 My Outreach/build_publication_catalog.py`** — Reusable Python script (openpyxl) that generates the catalog from hardcoded publication data. Auto-detects PDFs in Master Copies and Archive. Two-sheet Excel output with color-coded rows, auto-filter, and summary statistics.

2. **`02 My Outreach/Wach_Publication_Catalog.xlsx`** — 57-publication catalog with 14 columns (ID, Year, Type, Venue, Title, Authors, First Author, Status, DOI, Master Copies PDF, PDF in Master?, Archive Folder, Archive PDF Available?, Notes). Summary sheet with counts by type, first-author breakdown, and PDF coverage.

3. **PDF consolidation** — Master Copies folder grew from 28 to 51 PDFs (45/57 cataloged publications covered, 79%).

### Sources Scanned for PDFs
- `02 My Outreach/Archive/` — 19 PDFs copied
- `02 My Outreach/00 Master Copies/` — 28 pre-existing
- VT OneDrive backup (`OneDrive/Documents/VT/00 My Publications/`) — 2 PDFs found (CSER 2018, IEEE SysCon 2023)
- VT laptop backup (`OneDrive/Documents/VT/00 VT Backup/`) — 1 PDF found (CSER 2024 Best Paper)
- ITEA journal website — 1 PDF downloaded directly
- Other publisher sites (Wiley, Springer, IEEE, PMC) — blocked by paywalls/bot protection

### Publication Counts
| Type | Total | First Author |
|------|-------|-------------|
| Journal | 10 | 5 |
| Conference | 30 | 18 |
| Book Chapter | 1 | 0 |
| Magazine | 1 | 1 |
| Dissertation | 1 | 1 |
| Report | 2 | 2 |
| Presentation | 8 | 7 |
| White Paper | 4 | 4 |
| **TOTAL** | **57** | **38** |

### 12 Publications Still Missing PDFs
1. "Cost of Expertise" (IS 2025) — Wiley
2. "Operation Safe Passage" (IS 2025) — Wiley
3. "Operation Safe Passage" (CSER 2025) — Springer, not yet indexed
4. "DT in Acquisition" (IS 2022 DAU) — Wiley
5. "DE Roadmap" (SysCon 2022) — IEEE Xplore
6. "Acquisition Requirements" (ARS 2019) — NPS DAIR
7. "High salt / ETB" (Physiol Reports 2015) — Wiley OA (open access, needs browser)
8. "SOD in renal I/R" (Kidney Int 2010) — PMC free
9. "Sex difference AngII" (AJP 2010) — PubMed
10. "Rat tail AVF" (Kidney Int 2009) — not found online
11. "Renal vasoconstrictor" (FASEB 2007) — not found (likely abstract only)
12. SERC AI4SE 2024 presentation — internal, not published

### Technical Notes
- Script uses `effective_master_pdf` logic to auto-detect archive PDFs that were copied to Master Copies
- Fixed 5 tuples with missing `archive_folder` field (biomedical journal entries)
- curl downloads blocked by most publisher bot protection; only ITEA.org allowed direct download
- VT backup `00 My Publications/` folder is the richest source of older publication PDFs
- VT laptop backup `Publications/` folder had folder structure but mostly empty files (OneDrive sync incomplete)

### CV as Source of Truth
- Primary: `01 Admin/01 CVs and Bios/Paul_Wach_CV_20250721_wPII.pdf` (July 2025, 9 pages)
- CV missing 2026 submissions (CSER 2026, IS 2026, IW 2026) — added manually from working directories
