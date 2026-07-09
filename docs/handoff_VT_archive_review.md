# VT Archive Review — Handoff Document

> PROVENANCE: claude-opus-4-7[1m] (Anthropic, Claude Code CLI). Authored 2026-06-03 in session postwach-02 (PostWach hive). Consolidates: the 2026-06-03 morning VT archive audit (separate parallel session), the EndNote-library investigation in session postwach-02 (afternoon), and the OSP/OSL equivalence finding from session postwach-05 on 2026-06-02. Designed to be read cold by a fresh session.

> PURPOSE: Brief a new Claude session on the VT archive's location, state, conversion challenges, and remaining work, so the new session can pick up VT-archive review tasks without reconstructing context from scratch.

---

## 1. Location

`C:\Users\pfwac\OneDrive - University of Arizona\Documents\Z99 VT Archive\`

Subroots inside the archive:

- `VT plaptop\` — main archive root (11.9 GB after audit; see §3)
- `_Audit_2026-06-03\` — the 2026-06-03 audit deliverables (CSV inventory, missing-content list, summary)

The archive itself is a one-time OneDrive sync from the Virginia Tech laptop. All filesystem `LastWriteTime` and `CreationTime` values cluster around **2026-02-23** because that is the OneDrive sync date — not the original authoring dates. **True authoring dates must be read from inside files** (zip metadata, file content, EXIF, document properties).

---

## 2. Top-level structure (`VT plaptop\`)

| Subfolder | Size | Notes |
|---|---|---|
| `00 Dissertation` | 939 MB | PhD dissertation source materials. |
| `00 Legal` | 33 MB | Legal/admin records. |
| `00 VT Backup` | 5.8 GB | The largest subtree. Contains `Paul - Misc`, `PhD`, `WRT-2406`, `VT Desktop`, `IDT`. **Heaviest data-loss damage in this subtree.** |
| `01 Administrative` | 127 MB | Admin records, travel. |
| `02 Articles` | 2.4 GB | Literature collection. Many subfolders empty (see §3); journal articles re-acquirable from DOIs. |
| `03_Projects` | 901 MB | Project source materials. Multiple subfolders empty (`Beling_DAU`, `Automated-MBSE`, `LLM\Bulldog`). |
| `04 Course Work` | 230 MB | Courses taken (ENGR 5004, ENGR 5104, STAT 5204G, PHIL 5505). |
| `05 Professional Memberships` | 118 MB | INCOSE, NSI, etc. |
| `06 SERC` | 54 MB | SERC-related materials. |
| `07 Mashable` | <1 MB | Python tutorial, fragmentary. |
| `08 Grant Proposals` | 2 MB | Grant drafts (NSA LAS subfolders empty). |
| `09 Courses Taught` | 21 MB | Teaching materials. |
| `Conferences` | 67 MB | Conference attendance materials. |
| `EndNote_*.Data` (×2) + `My EndNote Library*.Data` (×3) | ~204 MB combined | Five EndNote `.Data` sidecar folders. See §4. |
| `Genesys`, `Machine Learning Workshop`, `Map`, `Matlab`, `MS4 Me`, `Neo4j`, `SysML` | 1 MB to 331 MB | Tool / workshop / model directories. MS4 Me's source folders are mostly empty (Eclipse `.project` survived, `src/` and `bin/` did not). |

Root-level files in `VT plaptop\`:

- `Wach_Paul_VT_Prof_2025-09-25.zip` (31 MB) — professional dossier zip
- `d-TEMP_OneSlide.pptx` (1.9 MB)
- 6 EndNote `.enl` files (see §4)
- A few docx / pptx fragments

---

## 3. Audit state (from `_Audit_2026-06-03\AUDIT_SUMMARY.md`)

A prior session ran a full inventory pass. **Read that file** before starting any subtree work — it contains the actionable priorities. Key numbers:

- **2,104** surviving files, **11.9 GB**, all local-on-disk (no cloud-only placeholders)
- **0** OneDrive cloud-only placeholders (sync complete)
- **30** genuinely zero-byte files (all empty-by-design: 28 EndNote MyISAM index-file placeholders + 1 Windows RDP default + 1 MS4 Me workspace marker)
- **~6,800** directory subtrees scanned; **6,453** contain zero files
- **219** root-empty subtrees (the actionable re-download targets)
- Diagnosis: **failed bulk copy** (folder structure copied but file contents lost in many places). Most likely cause: an interrupted `xcopy` / `robocopy` / Explorer drag-and-drop without retry semantics, or an interrupted OneDrive bulk move. Folder `LastWriteTime` clusters around 2026-02-23.

Audit deliverables (in `_Audit_2026-06-03\`):

- `inventory.csv` — 2,104 rows: path, size, ext, timestamps, OneDrive-local-state, empty-flag
- `missing-content.csv` — 219 rows: each root-empty subtree
- `AUDIT_SUMMARY.md` — full text including 5-tier re-download priority list

**Re-download priority tiers (verbatim from AUDIT_SUMMARY):**

- **Tier 1 — Career-critical, irreplaceable:** Dossier, Draft Proposals, IDA, NAVSEA Dahlgren, Violet Labs, Reviewed Articles, PhD\Manuscript (22 nested subdirs), PhD\Research Proposal, PhD\SysML Files, PhD\Dissertation Publications, Alejandro and Paul Com (advisor correspondence)
- **Tier 2 — Sponsored research / restricted:** `WRT-2406\01 Deliverables` (SERC), `WRT-2406\RESTRICTED Internal VT ONLY` ⚠ **export possibly restricted by sponsor agreement; verify before copying**, `08 Grant Proposals\NSA Laboratory for Analytic Sciences\*`
- **Tier 3 — Active project source:** `Beling_DAU\*` (17+ subtrees), `Beling_TestAgility\*`, `Automated-MBSE\*`, `03_Projects\DAU`, MS4 Me Eclipse projects (source code lost across 18 projects including `PaulThesis`, `DissertationModels`, `CounterHomomorphism`)
- **Tier 4 — Teaching / service / travel:** Course prep (46 nested subdirs), Guest Lectures, INCOSE Assistant Director, NSI Admin, Travel, Courses Taught\DE\Innoslate
- **Tier 5 — Recoverable from elsewhere:** EndNote `*.Data\PDF\` subtrees (3,492 empty per-ref PDF folders, PDFs re-acquirable from DOIs), `02 Articles\*` empty literature subfolders, installer downloads

Recommended re-copy command (from VT-network-connected machine):

```
robocopy <source> <dest> /MIR /R:3 /W:5 /COPY:DAT /DCOPY:T /LOG:robocopy.log
```

---

## 4. EndNote libraries (investigated 2026-06-03 postwach-02)

Six `.enl` files at the root of `VT plaptop\`, each with a paired `.Data\` sidecar:

| Library file | Sidecar | Index size | Live data size | True date* | Notes |
|---|---|---|---|---|---|
| `My EndNote Library v2.enl` | `My EndNote Library v2.Data\` | 1414 KB | 110 MB | **2024-07-24 17:02** | **Canonical.** Largest. "v2" naming. EndNote v18.2. |
| `My EndNote Library_2020-06-19.enl` | `My EndNote Library_2020-06-19.Data\` | 1026 KB | 47 MB | (read inside) | Mid-2020 snapshot. |
| `EndNote_mathOfMBSE_2020_03_30.enl` | `EndNote_mathOfMBSE_2020_03_30.Data\` | 982 KB | 42 MB | (read inside) | Math-of-MBSE focused; dissertation era. |
| `My EndNote Library.enl` | `My EndNote Library.Data\` | 224 KB | 4 MB | (read inside) | Likely v1. |
| `EndNote_MathOfMBSE_2019-12-19.enl` | `EndNote_MathOfMBSE_2019-12-19.Data\` | 220 KB | 1 MB | (read inside) | Older math-of-MBSE. |
| `EndNote_Library_2024-02-06.enl` | (no functional sidecar) | 272 KB | 0 MB | (no data) | **Broken / orphan.** Sidecar is empty. Skip. |

*True date = last-modified timestamp recorded inside the file by EndNote, NOT the filesystem LastWriteTime (which is uniformly 2026-02-23 from migration).

### Format facts

- Each `.enl` file is a **ZIP archive containing 2 files: `refs.MYD` and `refs.frm`** — a snapshot/index pointer, not the active database.
- The active database lives in the paired `.Data\` folder with `rdb\` (real database) and `tdb\` (transient database) subfolders containing **MyISAM** tables (`.MYD`, `.MYI`, `.frm`).
- MyISAM is the bundled storage engine from EndNote's embedded MariaDB. This is NOT SQLite. `python -c "import sqlite3; sqlite3.connect(enl)"` will return "file is not a database."
- Text content (titles, authors, venues, abstracts, notes) IS plaintext inside `refs.MYD` and can be string-extracted.
- Numeric content (year, volume, pages, ref-type ID) is stored as **binary integers** and is NOT recoverable by naive string extraction.

### Conversion paths (none completed yet)

Goal: convert v2.enl to BibTeX format and seed `04 Resource Library\00 Verified References\` (the user-designated portfolio reference store for the R019 governance work).

| Path | Cost | Accuracy | Status |
|---|---|---|---|
| **(A)** EndNote XML export (manual) — user opens v2.enl in EndNote Desktop, File → Export → XML; then I convert XML → BibTeX | ~5 min user + ~5 min me | **High** | **Recommended.** Needs EndNote license on some machine. |
| **(B)** Mount with local MariaDB — install MariaDB, point datadir at v2.Data\rdb, `SELECT * FROM refs`, dump to BibTeX | ~30-60 min setup + ~10 min run | **High** | Viable; leaves MariaDB installed; no EndNote license needed. |
| **(C)** Partial string extraction from raw `refs.MYD` — extract titles + authors + venues only; produces a CSV inventory, not canonical BibTeX | ~10 min | **Partial** (no year, no ref-type, no DOI) | Useful as searchable index, not as canonical source. |

### Observed sample structure (from `refs.MYD` probe)

In a probe of `My EndNote Library v2.Data\rdb\refs.MYD` (1437 KB live file), the extractor found:

- ~22,140 printable strings (len >= 6)
- ~4,647 author-format strings (`Lastname, F` form)
- ~4,281 long strings (40-250 chars, mostly titles + abstracts + research notes)
- ~528 journal/venue-like strings (samples: "Systems Engineering", "Proceedings of AIAA Space 2016", "INCOSE", "IEEE Transactions on Systems, Man, and Cybernetics: Systems")
- **0** pure 4-digit year strings (years are binary integers)

Estimated **~1,500-2,000 reference records** in v2.enl based on the author-string count and typical EndNote record structure.

### Known partial XML export (already on disk)

`02 My Outreach\Archive\OJSE 2022\References_OJSE.xml` (31 KB) and `References_OJSE_2.xml` (29 KB) are EndNote XML exports from v2.enl, generated by EndNote v18.2 for the OJSE 2022 paper. They confirm:

- EndNote XML schema is well-formed: `<xml><records><record>...</record></records></xml>`
- Per-record nodes include database/path provenance, ref-type ID + name, foreign keys, contributors/authors, titles, periodical, pages, volume, number, keywords, dates/year, publisher, abstract, urls/pdf-urls, electronic-resource-num (DOI), access-date, research-notes
- Sample DOIs in evidence (verified parseable): `10.1002/sys.21241` (Bjorkman 2013), `10.1002/sys.21568` (Salado 2021 RA), `10.1002/sys.21463` (Salado/Kannan 2018), `10.3390/systems7020019` (Salado/Wach 2019)
- These two XML files together hold maybe 15-30 records, not the full library — they were per-paper exports

If Path (A) becomes available, the conversion script can mirror this exact schema.

---

## 5. OSP / OSL artifacts in the VT archive (from session postwach-05 on 2026-06-02)

`Z99 VT Archive\VT plaptop\00 VT Backup\Paul - Misc\Publications\2025 - CSER - OSL\`

| File | Size |
|---|---|
| `Sandman_etal_2025_CSER_OSP_Intro.docx` | 399 KB |
| `Sandman_etal_2025_CSER_OSP_Intro (2).docx` | 2.4 MB |
| `outline_2024-10-16.docx` | (outline) |

**Durable finding (do not re-derive):** The folder is named `OSL` but every file inside (and every external reference in the publication register, the dTE mini-tutorial, the lit-review scoping doc) uses **OSP**. Inference: **OSL ("Operation Safe Lego") is the earlier or informal name for the same project as OSP ("Operation Safe Passage").** The Lego link is concrete: the dTE mini-tutorial describes the OSP testbed as using "Lego robots as UGV proxies." The `03 Output Artifacts\Lego-EV3-Mindstorm-Models\` SysML library is the model spine for those proxies, though its own README is framed for PLMr.

A future request mentioning either name should resolve to the same artifact set. See `docs/session-archives/SESSION_ARCHIVE_2026-06-02_postwach-05.md` for full inventory.

---

## 6. What has been touched

- **Audit pass (2026-06-03 morning):** Full file inventory, missing-content list, AUDIT_SUMMARY.md. See `_Audit_2026-06-03\`.
- **OSP/OSL inventory (2026-06-02 postwach-05):** Three-tier inventory of OSP/OSL artifacts; equivalence finding logged.
- **EndNote investigation (2026-06-03 postwach-02):** Format facts confirmed (ZIP wrapping MyISAM); v2 identified as canonical; true date 2024-07-24 extracted from zip metadata; conversion paths surfaced. **No conversion executed yet.**
- **Personal drive (non-OneDrive) check:** `C:\Users\pfwac\Documents` exists but has no EndNote files. The VT archive is the only EndNote source.

## 7. What has NOT been touched

- Tier 1-5 re-download work (depends on VT-side access)
- Full content scan of `00 VT Backup\` subtree (only `Paul - Misc\Publications\2025 - CSER - OSL\` examined)
- The 1.97 GB `Wach Lab General.zip` (contents not inspected)
- `02 Articles\` subtree (only enumerated, not searched)
- `00 Dissertation\` subtree (not inspected)
- `SysML\` subtree (331 MB, not inspected)
- `Genesys\`, `Neo4j\`, `Machine Learning Workshop\` (not inspected)
- The smaller `.enl` libraries (only v2 probed in detail)

## 8. Open work / entry points for next session

In priority order:

1. **EndNote conversion to BibTeX.** Choose path from §4 (A/B/C). Output goes to `04 Resource Library\00 Verified References\` to seed R019 governance work.
2. **Tier 1 data-loss re-copy** while VT access is still active (Dossier, Draft Proposals, PhD Manuscript, advisor correspondence).
3. **Tier 2 — verify WRT-2406 RESTRICTED export rules** before any copy.
4. **`Wach Lab General.zip` (1.97 GB) inspection** — could contain irreplaceable consolidated materials.
5. **`02 Articles\` search for SE Math Foundations / morphism / Wymore literature** that may already exist locally before re-acquiring from DOIs.
6. **`00 Dissertation\` PDF / manuscript inspection** — confirm what's there before treating dissertation publications as a re-download target.

## 9. Constraints and cautions

- **Filesystem dates are migration dates, not authoring dates.** Always read inside files (zip metadata, document properties, file content) for true dates.
- **WRT-2406\RESTRICTED Internal VT ONLY** — sponsor agreement may restrict export. Verify before copying.
- **VT access window may close.** The audit recommends doing Tier 1-2 re-copies while VT-side source is reachable.
- **EndNote v2.enl was last touched 2024-07-24.** Any references added during 2024-07 to 2026-02 (Arizona-era papers) are NOT in this library. The library is canonical for VT-era work only.
- **MyISAM raw extraction loses numeric fields.** Do not rely on a string-extraction-only path for canonical BibTeX.
- **The 30 zero-byte files are NOT data loss** (28 EndNote empty-index placeholders + 2 misc). Don't waste time investigating those.

## 10. Related documents

- `_Audit_2026-06-03\AUDIT_SUMMARY.md` — the 2026-06-03 audit (read this first)
- `docs/session-archives/SESSION_ARCHIVE_2026-06-02_postwach-05.md` — OSP/OSL inventory session
- `docs/session-archives/SESSION_ARCHIVE_2026-06-03_postwach-02.md` — the session that authored this handoff (R019 discussion + EndNote investigation)
- `docs/proposed_R019_references_verification_gate.md` — R019 governance proposal (the EndNote conversion is upstream input to R019 Phase 3 backfill)
- `03 Projects/96 OSP_OSL/` — the consolidated OSP/OSL share folder created 2026-06-02 (dTE mini-tutorial PDF + Sandman OSP intro draft docx)
