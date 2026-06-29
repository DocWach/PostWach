# Session Archive — 2026-06-03 postwach-02

> PROVENANCE: claude-opus-4-7[1m] (Anthropic, Claude Code CLI). All session artifacts (this archive, the VT archive review handoff doc, the EndNote-format investigation, and ruflo warmup outputs) produced by this model in this access mode. No sub-agents spawned this session; no swarm initialized.

**Hive:** PostWach
**Scope:** Resume the R019 references-verification-gate discussion from session postwach-04 (2026-06-02). The principal answered all 7 open questions from the proposal's Section 10. Side investigation: identify and assess EndNote-library files in the VT archive as the canonical-references seed for the new approved-references store. Side deliverable: a VT archive review handoff document for a separate future session.
**Platform:** ruflo v3.7.0-alpha.14 (warmed at session start; MCP stdio mode healthy 100/100 on 5 monitored components; AgentDB 16 controllers enabled across L1-L5; memory 428 entries at 100% embedding coverage; no live swarm).
**Outcome:** All 7 R019 open questions resolved at the decision-input level (with two parked sub-decisions on EndNote conversion path and on staleness-policy parameter tuning). EndNote investigation surfaced canonical `My EndNote Library v2.enl` (true authoring date 2024-07-24), confirmed it is a ZIP wrapping MyISAM tables (not SQLite), and produced three viable conversion paths. VT archive review handoff doc written at `docs/handoff_VT_archive_review.md` consolidating the 2026-06-03 morning audit + the EndNote findings + the OSP/OSL equivalence finding from postwach-05.

---

## 1. Entry state

Session opened: "warm up ruflo, let's continue the discussion from last night on the rule update."

Recovered state:

- R019 proposal exists at `docs/proposed_R019_references_verification_gate.md` (authored in session postwach-04 on 2026-06-02; not yet adopted). 195 lines. 7 open questions in Section 10.
- ruflo warmup identical to previous session: v3.7.0-alpha.14, MCP stdio PID 14104, system_health 100/100, AgentDB 16 controllers enabled, memory 428 entries 100% embedded, last swarm terminated 2026-06-01.
- No live swarm. Memory `claude-memories` namespace holds 399 entries including `feedback_references_triple_check.md` (the behavioral rule R019 is designed to back structurally).
- A parallel SwarmEng SERC session ran the same morning (logged as postwach-01 by that session); that work is independent and does not affect R019.

---

## 2. R019 open-question resolutions (durable)

The principal answered all 7 questions from the R019 proposal Section 10. Resolutions:

- **Q1 — Data store location:** `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\` (an existing empty subfolder under Resource Library). Sits outside any git repo; OneDrive provides version history. Cross-hive read access via absolute path. Confirmed by principal direct path provision.
- **Q2 — N and τ defaults:** Principal requested explanation rather than a decision. Explained: N=3 = number of independent agents (tri-model pipeline) per verification; supermajority ⌈2N/3⌉ = 2 means one disagreement does not sink verification (smallest viable Byzantine N). τ=0.95 = per-field posterior probability threshold after Bayesian aggregation (source-reputation prior × per-agent confidence likelihood). Defaults remain `N=3, τ=0.95` provisionally; revisit after Phase 3 backfill experience.
- **Q3 — Trigger authority:** **Both** (human author and Claude autonomous). Caveat captured: autonomous trigger fires only when the agent is about to write a citation, not when it merely encounters one in source material. `[PLACEHOLDER]` is the escape hatch during flow; batch verify at end-of-section or end-of-draft.
- **Q4 — Software citation versioning:** Recommendation accepted (3 fields: `version_used`, `current_version`, `version_checked_date`). Citation in-paper always uses `version_used`.
- **Q5 — Cross-paper consistency (impact + notes clarification):** R019 governs the bibliography entry only. In-text annotations, per-paper commentary attached to a cite, and reading notes are not touched. Two papers citing the same approved ref must match on load-bearing fields (authors, title, year, venue, pages, DOI); style-only punctuation/abbreviations are house style, not verification.
- **Q6 — Staleness / `revalidate_after` (intent):** Three real failure modes documented (URL rot, retractions, software-version drift). Recommendation: peer-reviewed published refs — no automatic expiry; software refs — revalidate after 6 months; preprints / in-press — revalidate after 3 months; URL-only refs — revalidate after 6 months.
- **Q7 — Render-gate failure-recovery default:** Recommendation accepted: abort the render and report missing cites; do NOT auto-launch `/refverify`. Add `--autoverify` flag for opt-in combined gate-and-verify.

The 7-question discussion is the substantive R019 design progress for this session. **No code or rule text changes have been made yet** — the proposal is still in `docs/proposed_R019_references_verification_gate.md` unmodified. Implementation phase 1 (data store standup at the agreed location) is the next R019 action when the principal authorizes execution.

---

## 3. EndNote investigation (side thread)

Principal directive: "Based on the parallel session on the VT archives, we should have access to an EndNote file with my previous reference records. Can you convert that. It is the most canonical source that I have."

### Discovery

Six `.enl` files at `Z99 VT Archive\VT plaptop\` plus paired `.Data\` sidecars:

| File | Index size | Data size | True date | Verdict |
|---|---|---|---|---|
| **My EndNote Library v2.enl** | 1414 KB | 110 MB | **2024-07-24 17:02** | Canonical |
| My EndNote Library_2020-06-19.enl | 1026 KB | 47 MB | (older) | Snapshot |
| EndNote_mathOfMBSE_2020_03_30.enl | 982 KB | 42 MB | (older) | Topic-focused |
| My EndNote Library.enl | 224 KB | 4 MB | (older) | Likely v1 |
| EndNote_MathOfMBSE_2019-12-19.enl | 220 KB | 1 MB | (older) | Topic-focused |
| EndNote_Library_2024-02-06.enl | 272 KB | 0 MB | (broken) | Orphan, sidecar empty |

Personal drive (`C:\Users\pfwac\Documents` non-OneDrive) checked: no EndNote files. VT archive is the only EndNote source on this machine.

### Format facts (resolved durable)

- `.enl` files are ZIP archives. PK header confirms. Each `.enl` contains exactly **2 files**: `refs.MYD` and `refs.frm`.
- The 2-file ZIP is a snapshot/index pointer. **The active database lives in the paired `.Data\` folder** with `rdb\` (real database) and `tdb\` (transient database) subfolders containing **MyISAM** tables (`.MYD`, `.MYI`, `.frm`).
- MyISAM is the bundled storage engine from EndNote's embedded MariaDB. Direct `sqlite3` connection returns "file is not a database."
- Text content (titles, authors, venues, abstracts, notes) is plaintext inside `refs.MYD` and can be extracted via simple printable-string scan.
- Numeric content (year, volume, pages, ref-type ID) is stored as binary integers and is NOT recoverable by naive string extraction.
- True authoring date for v2.enl: 2024-07-24 17:02 (read from zip metadata via `file v2.enl`). Filesystem `LastWriteTime` 2026-02-23 17:06 is the OneDrive migration date, not the authoring date. This generalizes: **all VT archive filesystem dates are migration dates; true dates must be read from inside files.**

### Probe results on v2 live refs.MYD

In a probe of `My EndNote Library v2.Data\rdb\refs.MYD` (1437 KB):

- ~22,140 printable strings of length ≥ 6
- ~4,647 author-format strings (`Lastname, F`)
- ~4,281 long strings (40-250 chars; titles + abstracts + research-notes)
- ~528 journal/venue-like strings (samples: "Systems Engineering", "Proceedings of AIAA Space 2016", "INCOSE", "IEEE Transactions on Systems, Man, and Cybernetics: Systems")
- 0 pure 4-digit year strings (years stored as binary integers)

Estimated **~1,500-2,000 reference records** based on author-string count and typical EndNote record structure.

### Existing partial XML exports

`02 My Outreach\Archive\OJSE 2022\References_OJSE.xml` (31 KB) and `References_OJSE_2.xml` (29 KB) are EndNote v18.2 XML exports from v2.enl (per-paper subsets, ~15-30 records each). They confirm the EndNote XML schema is parseable and that DOIs are stored cleanly (samples verified: `10.1002/sys.21241`, `10.1002/sys.21568`, `10.1002/sys.21463`, `10.3390/systems7020019`). If conversion Path (A) is chosen, the converter can mirror this schema.

### Three conversion paths surfaced (none executed)

- **(A)** Manual EndNote XML export by principal on a machine with EndNote installed, then I convert XML → BibTeX. Highest accuracy; needs license.
- **(B)** Local MariaDB install pointed at `v2.Data\rdb`, `SELECT * FROM refs`, dump. High accuracy; ~30-60 min setup; leaves MariaDB installed.
- **(C)** String extraction from raw `refs.MYD`. Partial accuracy (no years, no ref-types). Useful as searchable index, not as canonical BibTeX.

Principal interrupted the AskUserQuestion that would have chosen a path, redirected to "Open the folder that the EndNote file is contained in" (folder opened in Explorer), then to creating the VT archive review handoff document. **Conversion path is therefore PARKED** until the next R019-related session decides.

---

## 4. VT archive review handoff document

Authored at `docs/handoff_VT_archive_review.md`. Designed to be loadable by a fresh session without prior context. Consolidates three sources:

- The 2026-06-03 morning audit (`Z99 VT Archive\_Audit_2026-06-03\AUDIT_SUMMARY.md`) — 2,104 surviving files, 219 root-empty subtrees, data-loss diagnosis (failed bulk copy)
- The EndNote investigation from this session — format facts, file inventory, conversion paths
- The OSP/OSL equivalence finding from session postwach-05 (2026-06-02)

Ten sections: location, top-level structure, audit state with 5-tier re-download priority, EndNote-specific section, OSP/OSL artifacts, what has been touched, what has NOT been touched, open work, constraints, related documents.

Principal's stated intent: transfer this document to a separate future session. The doc is self-contained for that purpose.

---

## 5. Decisions made this session (durable)

- **D1. R019 store location:** `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\` (existing empty folder, OneDrive-direct, no git versioning, cross-hive accessible via absolute path).
- **D2. R019 trigger authority:** both human and autonomous agent, with autonomous trigger gated on "about to write" (not "encountered").
- **D3. R019 software-citation fields:** 3 fields — `version_used` (pinned, never changes), `current_version` (informational), `version_checked_date`. In-paper cite always uses `version_used`.
- **D4. R019 cross-paper consistency:** governs bibliography entry only. In-text annotations, per-paper notes, and reading commentary not regulated. Bibliography entries match on load-bearing fields (authors, title, year, venue, pages, DOI); style is per-paper.
- **D5. R019 staleness policy (proposed defaults):** peer-reviewed = no expiry; software = 6 months; preprints/in-press = 3 months; URL-only = 6 months.
- **D6. R019 render-gate failure default:** abort + report (no auto-verify). Opt-in via `--autoverify` flag.
- **D7. v2.enl is canonical EndNote source.** True authoring date 2024-07-24. Last touched ~18 months ago; Arizona-era references (2024-07 to present) are not in this library.
- **D8. EndNote `.enl` format characterization (durable, future sessions inherit):** ZIP archives wrapping MyISAM tables in the paired `.Data\` folder. Not SQLite. Text fields plaintext-recoverable; numeric fields binary.
- **D9. Conversion path decision PARKED.** Three paths surfaced (A=manual XML export, B=MariaDB mount, C=partial extraction). Choice deferred to next R019-related session.
- **D10. VT archive filesystem-dates-are-migration-dates is a generalized rule** (also applies to OSP/OSL files in `00 VT Backup\Paul - Misc\Publications\2025 - CSER - OSL\` from postwach-05). True authoring dates must be read from inside files.

---

## 6. Artifacts produced this session

- `docs/handoff_VT_archive_review.md` — the VT archive review handoff document, 10 sections
- This archive (`docs/session-archives/SESSION_ARCHIVE_2026-06-03_postwach-02.md`)
- (Scorecard not yet written; will be filled at session end per [R014])
- No file edits to `docs/proposed_R019_references_verification_gate.md` — the proposal is still in its original 195-line form; the 7 resolutions are recorded here in §2 and §5

---

## 7. Open items / next session entry points

| # | Item | State |
|---|---|---|
| 1 | R019 proposal edit: incorporate the 7 resolutions into the proposal document | Pending; the resolutions are in this archive §2/§5 only |
| 2 | R019 Phase 1: stand up the data store at `04 Resource Library\00 Verified References\` | Authorized location but not executed |
| 3 | EndNote v2 → BibTeX conversion path choice (A/B/C) | Parked; user interrupted the AskUserQuestion |
| 4 | EndNote conversion execution once path chosen | Pending Item 3 |
| 5 | Seed `00 Verified References\` with the SwarmEng v0.3 16 verified refs (from postwach-01 today) as the first approved entries | Pending Item 2; refs already verified |
| 6 | VT archive Tier 1-2 re-copy work (audit recommendation) | Out of scope this thread; needs VT access |
| 7 | Promote OSL ↔ OSP equivalence finding to a project-memory file? | Still optional; finding lives in handoff doc + postwach-05 archive |

---

## 8. Process notes

- **Auto-memory loaded** 188 entries at SessionStart. Useful for tone (no em-dashes, no AI-voice), structure (paper-status discipline, R016 integration status), and cross-session continuity (the previous postwach-04 R019 proposal).
- **No swarm, no Task subagents.** Pure single-agent thread.
- **One Explorer launch** (`explorer.exe` on the VT plaptop folder per principal request).
- **AskUserQuestion used twice.** First time (Q-batch on R019 7 questions) answered cleanly. Second time (EndNote source-library + import-status questions) interrupted by principal redirect.
- **R016 integration-status discipline:** R019 components mapped to existing (b) demonstrated capabilities (tri-model review pipeline, TRAK Bayesian aggregation, ontology-gate.sh two-tier pattern). EndNote v2.enl is a research artifact, not a capability. The OSP/OSL file set is a research artifact. The 2026-06-03 morning audit is a research artifact (one-shot inventory; not a reusable tool).
- **R018 foundation-model provenance:** archive carries claude-opus-4-7[1m] PROVENANCE line; handoff doc carries it too.
- **R104 root-folder discipline:** handoff doc in `docs/`, archive in `docs/session-archives/`, no root saves.

---

---

## 9. R019 implementation (Phases 1, 2, 4) — late session

After the interim section above, the principal authorized execution of two of the three pending R019 actions in one batch: edit the proposal to fold in the resolutions + stand up the data store (Phase 1), then adopt R019 globally (Phase 2) and build the render gate (Phase 4).

### 9.1 Proposal edit (resolutions folded in)

`docs/proposed_R019_references_verification_gate.md` updated with surgical edits:

- §4 Data store: path changed to `04 Resource Library/00 Verified References/` (OneDrive-direct, not git-tracked); manifest schema extended with `verification_mode`, `pending_byzantine_verification`, `revalidate_after`, `notes`.
- §4.1 Schema scope: bibliography-entry-only governance; in-text annotations, per-paper notes, reading commentary not regulated.
- §4.3 Software citation: 3-field structure (`version_used` pinned, `current_version` informational, `version_checked_date`).
- §4.4 Staleness defaults: peer-reviewed = null; software = P6M; preprint/in-press = P3M; URL-only = P6M (ISO 8601 durations).
- §5 Parameters: N=3, τ=0.95 marked as starting values; revisit after Phase 3 backfill.
- §6.1 NEW: trigger authority = both human + autonomous, gated on "about to write" not "encountered"; `[PLACEHOLDER]` is the flow escape hatch.
- §7 Render gate: abort + report default; `--autoverify` opt-in flag for combined gate + verify.
- §8 Phase 1: path updated, status marked DONE 2026-06-03.
- §10: original 7 open questions converted to **Resolutions** table with Q1-Q7 answers.
- §11 NEW: 7 forward-looking open questions (overlay discipline, Byzantine seed-entry upgrade scheduling, manual-drop policy, slash-command implementation venue, ref-correction propagation, Retraction Watch, sponsor-restricted refs).

### 9.2 Phase 1 — Data store standup

Created at `C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\`:

- `approved.bib` — 16 BibTeX entries, full IEEE-compatible metadata; header comment notes verification mode and Phase-5 Byzantine-upgrade pending. Entries cover: 6 ontology-engineering methodology refs (McDermott AI4SE, Fernández Methontology, Suárez-Figueroa NeOn, Guarino OntoClean, Duque-Ramos OQuaRE, Arp BFO), 1 CCO (Jensen FOIS 2024), 3 W3C TRs (OWL 2 Profiles, SHACL, SPARQL), OpenCAESAR OML, Wymore 1993, Zeigler 2018, Kamien STIDS MTO, Wach IS 2026 MEO, ruvnet ruflo.
- `manifest.yaml` — schema_version 1.0; `defaults` block with staleness windows; 16 per-entry records carrying `verification_mode: single-model-triple-check`, `pending_byzantine_verification: true`, evidence_urls where available, notes flagging the v0.1 errors that triple-check caught (Wymore "Tricotyledon" not "Tricotyledonous"; ruvnet GitHub byline replacing unverifiable "R. Cohen"; Jensen et al. 2024 FOIS replacing the original Rudnicki placeholder; Mission Thread Ontology not "Mission Theory"). ruvnet entry carries the 3 software-cite fields.
- `pending/` empty (`.keep` placeholder)
- `quarantine/` empty (`.keep` placeholder)

### 9.3 Phase 2 — Global rule adoption

`~/.claude/CLAUDE.md` updated: R019 added after R018 in the Research Context block. Wording references the proposal doc, points at the approved-references store path, names the pre-render gate file, and cross-links the behavioral memory.

`memory/feedback_references_triple_check.md` updated: added a "Structural backstop (R019)" paragraph noting that as of 2026-06-03 the behavioral rule is backed by R019; clarifies that the behavioral memory remains the *why* explainer and R019 is the structural *how*. Wikilink to the proposal doc preserved.

Per-hive CLAUDE.md cross-references are NOT done in this session — 9 V3 hives need a one-line R019 reference each. That's a separate small task.

### 9.4 Phase 4 — Render gate (refcheck.py)

Implementation: `01 PostWach/scripts/refcheck.py` (Python, ~150 lines, no external dependencies; uses stdlib `re`, `unicodedata`, `pathlib`, `argparse`). Thin wrappers `refcheck.sh` (bash) and `refcheck.ps1` (PowerShell) forward arguments.

Behavior matches proposal §7:

- Modes: pandoc-citekey (`@bibkey` extraction) auto-detected when manuscript has `@bibkey` patterns and no References section; otherwise IEEE-numbered bibliography extraction.
- BibTeX parsing: regex-based, handles single-level nested braces (`{AI4SE}`, `{SE4AI}`) and double-brace org-name idiom (`{{ruvnet (rUv)}}`).
- Surname extraction: handles four cases — "F. Lastname" prefix, "Lastname, F." comma form, double-brace org name as atomic surname, and bare lowercase software byline.
- Normalization: `unicodedata.NFKD` + combining-mark strip + LaTeX accent-escape strip + casefold. Handles `Fernández` ↔ `Fern{\'a}ndez` matching; handles `Suárez-Figueroa` ↔ `Su{\'a}rez-Figueroa`.
- Index: `(surname_normalized, year) -> [bibkey]`, with fallback first-word entry for org-style names so manuscript-side `ruvnet` matches bibkey-side full `ruvnet (rUv)`.
- Exit codes: 0 = all match (or advisory mode); 1 = misses in strict mode.

### 9.5 Test results

| Test | Manuscript | Result | Exit |
|---|---|---|---|
| 1 | SwarmEng v0.3 References_Bios.md (real, 16 refs) | **16/16 matched** | 0 |
| 2 | Deliberately broken fixture (1 valid + 1 fabricated + 1 unparseable) | 1/3 matched, 1 MISS, 1 ??? | 1 |
| 3 | Bash wrapper on Test 1 | 16/16 matched | 0 |
| 4 | PowerShell wrapper on Test 1 | 16/16 matched | 0 |

Three iteration rounds were needed to get to clean 16/16. The bugs caught and fixed: (a) parse_bib over-stripped inner braces, losing the double-brace org-name signal; (b) name comparison was case-and-accent sensitive, breaking on Fernández/Suárez and on lowercase byline "ruvnet"; (c) index keyed only on full normalized name, so manuscript-side truncated surname extraction missed multi-word org names. All three fixes documented in the script.

### 9.6 R019 acceptance criteria status

5 of 6 criteria met (per updated proposal §9):

- [x] approved.bib + manifest.yaml exist and are populated
- [x] R019 is in `~/.claude/CLAUDE.md` (per-hive cross-references still TBD)
- [x] refcheck.py runs and exits correctly
- [ ] /refverify, /reflookup, /refcheck slash commands (Phase 5, pending)
- [x] At least one bad-cite test case rejected
- [x] feedback_references_triple_check.md cross-links R019

R019 is **enforceable today** via direct invocation of `refcheck.py` from a pandoc-wrapper script (manual integration step per manuscript). The slash-command surface for in-flow verification is the next implementation step.

### 9.7 Updated open items / next session entry points

| # | Item | State |
|---|---|---|
| 1 | Per-hive CLAUDE.md R019 cross-reference (9 hives) | Pending; small task per hive |
| 2 | EndNote v2.enl XML export → BibTeX import into pending/ | Blocked on principal's other machine action (Path A) |
| 3 | Phase 5 — build `/refverify`, `/reflookup`, `/refcheck` slash commands | Pending; thin wrapper around tri-model review pipeline likely |
| 4 | Phase 3 backfill — verify AICB v0.6 + STOIC v0.5 + STIDS + MOACRA refs against approved store | Pending; sized at ~2-4 hr |
| 5 | Wire refcheck into a pandoc wrapper for the SwarmEng / STOIC / AICB build chains | Pending; per-paper integration |
| 6 | Phase 5 Byzantine N=3 upgrade of the 16 single-model-triple-check seed entries | Pending; tri-model pipeline composes (b) demonstrated capabilities |

---

**End of session 2026-06-03 postwach-02 (interim 2).** R019 reached operational milestone: rule adopted globally, store populated with 16 verified entries, render gate built and tested end-to-end on real and broken manuscripts. Five of six acceptance criteria met. R019 is enforceable today; the slash-command surface (Phase 5) and per-hive cross-references are the remaining work. Phase 3 backfill awaits the EndNote XML import from the principal's external machine.

---

## 10. Continuation 2026-06-04 — full R019 close-out

Session continued into 2026-06-04 with the principal-authorized EndNote XML re-export (full 1,562-entry library), swarm-based parallel execution of three remaining R019 work streams, follow-up matcher refinements, and end-to-end /refverify test on a real reference.

### 10.1 EndNote XML import (Phase 3 backfill seed)

Principal re-exported `My EndNote Library v2.enl` from a machine with EndNote installed; the second export delivered the full 1,562 records (the first attempt had returned only one record because the EndNote export scope defaulted to "selected references" — fix: Edit→Select All before File→Export).

Built `01 PostWach/scripts/endnote_xml_to_bibtex.py` (one-shot converter; handles ref-type mapping, VT ezproxy DOI strip, bibkey generation, duplicate-DOI surfacing). Ran end-to-end: 1,562 records → `pending/imported_from_endnote.bib` (1.5 MB BibTeX) + `pending/imported_from_endnote_manifest.yaml`. Distribution: 662 articles, 407 inproceedings, 285 incollections, 70 books, 49 techreports, 13 phdthesis, plus 76 misc/unpublished. 51% have DOI. 13 internal duplicate DOIs flagged. Cross-store: 3 DOI overlaps with approved.bib (mcdermott2020ai4se, 2 other Wach/SAGE refs); 1 bibkey collision (mcdermott2020ai4se — pending version superseded by approved).

### 10.2 Swarm (3 background agents, hierarchical, swarm-1780591611051-wp0u6p)

Principal directed: spin up a swarm, run remaining R019 actions in parallel. Three Task subagents:

| ID | Role | Outcome |
|---|---|---|
| ac1d4e9... | coder (Phase 3 backfill) | Extended `refcheck.py` with `--include-pending` and `--pending-store` flags; ran against AICB v0.6, STIDS MTO, STOIC v0.5; wrote per-paper reports at `docs/phase3_backfill/`. Surfaced that the pending pool yielded only 1 useful Phase-3 match (`wach2022pairing`) — 1,561 EndNote entries are historical context, not in-flight backfill candidates. |
| ae81fae... | general-purpose (per-hive crossrefs) | Added one-line R019 cross-reference rule to each of 9 V3 hive CLAUDE.md files: Alpha Empress A010, PostWach R109, GI-JOE G009, Fort Wachs X011, MACQ P012, COSYSMO C007, SysMLv2 S008, PLM L009, SEAD D007. Flagged SEAD numbering conflict (memory claimed D007-D009 existed but disk had only D001-D006). |
| a6ee407... | system-architect (Phase 5 slash commands) | Built `01 PostWach/.claude/skills/{refcheck,reflookup,refverify}/SKILL.md` + supporting `scripts/reflookup.py` (~210 LOC) and `scripts/refverify.py` (~410 LOC at first commit). MVP `/refverify`: single-model triple-check + DOI dedup pre-check + human-attested path with anti-self-attest gate. Full Byzantine N=3 explicitly deferred to Phase 5b. |

All three agents returned cleanly. Total subagent token spend ~350k across the three (Agent C heaviest at 146k).

### 10.3 Follow-up refinements (post-swarm)

Four items addressed sequentially:

**SEAD numbering reconciliation.** Read on-disk SEAD CLAUDE.md: confirmed D001-D006 only. Memory's record of D007 (container hardening 2026-03-02, implementing global [R013]) and D008/D009 (Fort Wachs ZT references 2026-03-10) was stale — those rules were planned but never committed. R019 cross-ref correctly placed at D007. Memory should be updated to flag the un-committed rules; deferred to user.

**Matcher refinements in `refcheck.py`.** Started at 13/16 on SwarmEng v0.3 (regression from 16/16 baseline; root cause was external bib edits changing first-author surnames on shacl2017, kamien2026mto, ruvnet2026ruflo). Fixed in five iterations:

1. Title-keyword tiebreak (`pick_best_by_title`) — when multiple bibkeys share `(surname, year)`, score each by title-token overlap with manuscript bib line. Resolves the wach2026meo vs kamien2026mto false-positive (line #15).
2. Multi-author indexing — `all_surnames()` returns every author's surname; index under each `(surname, year)` pair, not just first. Resolves line #14 (manuscript "D. Kamien..." now matches kamien2026mto's reordered authors `Wach, Paul and Kamien, David...`).
3. Editor field indexing — when `author` is a corporate atom (e.g., `{{W3C}}`) AND `editor` is present, index under editor surnames too. Resolves line #9 (manuscript cites SHACL by editors Knublauch + Kontokostas).
4. Aliases field support — bib entries can carry `aliases = {alt1, alt2}` for surname variants; matcher honors them. Added `aliases = {ruvnet, ruvnet (rUv)}` to ruvnet2026ruflo. Resolves line #16.
5. Stale stub message replaced — `[--autoverify]` block now lists missing entries with `/refverify ...` invocation hints, instead of saying "/refverify is not yet implemented."

Final state: **16/16 OK on SwarmEng v0.3.**

**`refverify.py` enhancements.** Added `--list-stale` (scans manifest for entries past their `revalidate_after` date; prints them with the software-cite refresh recipe), `--refresh` (in-place YAML edit of an existing manifest entry's fields; auto-fills `version_checked_date` if omitted), `ENRICH` verdict (claimed-empty + canonical-present = enrichment, not contradiction; doesn't block promotion), unicode hyphen + smart-quote normalization in `normalize_compare` (prevents typography-only DIFFs).

### 10.4 End-to-end /refverify test (Phase 3 cycle close)

Promoted `@wach2022pairing` from `pending/` to `approved.bib`:

1. `/reflookup "wach 2022 pairing"` → found PENDING entry
2. WebSearch → canonical DOI `10.1002/inst.12414` (Wiley INSIGHT vol 25 issue 4 pp 65-70)
3. `refverify.py --candidate-bibkey wach2022pairing --candidate-doi 10.1002/inst.12414 --field doi=... --field title=... --field journal=... [+5 more] --evidence-url https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/inst.12414 --primary-source 10.1002/inst.12414 --verified-by claude-opus-4-7 --promote`
4. Step 0: NOT-IN-STORE (no DOI dedup hit)
5. Field comparison: 6 OK + 1 ENRICH (DOI added)
6. Verdict: MATCH-WITH-ENRICHMENT → promote
7. Appended to approved.bib + manifest.yaml (`verification_mode: single-model-triple-check`, pending_byzantine_verification: true)
8. Re-ran refcheck on AICB v0.6 with new approved.bib: @wach2022pairing now OK (approved) — Phase 3 cycle closed end-to-end.

### 10.5 R019 acceptance criteria — 6 of 6 met

All six acceptance criteria closed (per updated proposal §9):

- [x] `approved.bib` (37 entries: 16 seed + STIDS-MTO 20 external backfill + @wach2022pairing) + `manifest.yaml` populated
- [x] R019 in `~/.claude/CLAUDE.md` + cross-referenced in 9 V3 hive CLAUDE.md files
- [x] `refcheck.py` (with `refcheck.sh` + `refcheck.ps1` wrappers) runs end-to-end; 16/16 OK on SwarmEng v0.3 after matcher refinements
- [x] `/refverify`, `/reflookup`, `/refcheck` slash commands shipped (MVP); full Byzantine N=3 deferred to Phase 5b
- [x] Bad-cite fixture rejected (deliberately-broken file exits non-zero in strict mode)
- [x] `feedback_references_triple_check.md` cross-links R019 as structural backstop

**R019 is operational.**

### 10.6 Open items / forward-looking

| # | Item | State |
|---|---|---|
| 1 | Phase 5b — full Byzantine N=3 protocol via tri-model review pipeline | Pending; deferred. Single-model triple-check MVP serves the current need. |
| 2 | Memory file update — flag SEAD D007-D009 entries as planned-not-committed | Pending principal review. The PostWach MEMORY.md notes those rules existed; disk says otherwise. |
| 3 | Phase 3 backfill on remaining in-flight manuscripts (STOIC v0.5, STIDS MTO, AICB v0.6 remaining MISSes, MOACRA) | Pending; sized in postwach-02 archive Item 4. Each is a separate small backfill session. |
| 4 | Wire `refcheck.py --strict` into the SwarmEng / STOIC / AICB pandoc render wrappers | Pending; one-line addition per render script. |
| 5 | Per-paper bibkey-vs-cite-form reconciliation (line #14 Kamien-cite-form fixed by matcher; STIDS-style cite forms may differ) | Lower priority; revisit if a new paper trips the matcher. |
| 6 | Concurrent-write race on approved.bib (two sessions promoting simultaneously) | No file lock implemented; OneDrive lock is best-effort. Not a real risk at current usage. |

### 10.7 Process notes (continuation)

- **Swarm worked cleanly.** Three subagents in parallel, total wallclock ~7.5 minutes for the longest agent (system-architect). The hierarchical topology meant I orchestrated; subagents didn't talk to each other directly. Agent C's claim about NameError in refcheck.py was incorrect (verified by direct file read + end-to-end test); no fix needed.
- **External bibedits-during-session is a real risk.** The 13/16 regression caught us — the matcher behavior is unchanged but the bib data shifted under it. Future practice: re-run refcheck after any approved.bib edit, and document the change in the bib's header comment.
- **The pending pool is /reflookup infrastructure, not Phase-3 backfill input.** Only 1 of 40 cross-paper citations resolved to a pending entry (`wach2022pairing` for AICB). The remaining 1,561 EndNote entries are historical context — searchable via `/reflookup` but not actively cited.
- **ENRICH verdict was the right call.** Without it, /refverify would have blocked on the wach2022pairing promote because pending was missing the DOI field. ENRICH treats "claimed empty + canonical present" as data enrichment, not contradiction. Six fields matched, one was added; verdict MATCH-WITH-ENRICHMENT.
- **Aliases field handles the single-author software cite case.** ruvnet2026ruflo has `author = {rUv}` (canonical) but manuscripts cite "ruvnet (rUv)"; the `aliases = {ruvnet, ruvnet (rUv)}` field bridges without disturbing the canonical author form.
- **No swarm shutdown required to terminate subagents** — they returned cleanly on their own. MCP swarm state still shows the swarm; explicit shutdown clean-up at session close.

---

**End of session 2026-06-03 postwach-02 (final).** Session spanned 2026-06-03 → 2026-06-04. R019 operationally complete (6 of 6 acceptance criteria). 37 approved entries, 1,561 pending. 9 V3 hives cross-referenced. Render gate working end-to-end on real and broken manuscripts. /refverify MVP shipped + tested end-to-end via @wach2022pairing promotion (Phase 3 cycle close). Phase 5b (Byzantine N=3) and per-manuscript backfills are the remaining work. Swarm shutdown executed at close.
