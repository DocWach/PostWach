# Session Archive — 2026-05-18 postwach-01

**Hive:** PostWach
**Scope:** Pickup from 2026-05-07 plan. Produce the two NSF 25-540 (TTP) RTSync/Dahlgren proposal artifacts the user originally scoped: NSF COA xlsx and NSF Synergistic Activities pdf. Deadline 2026-05-19, so this is the final pre-submission session for these two artifacts.
**Platform:** Ruflo, claude-opus-4-7 (1M context), Windows 11.
**Outcome:** Both artifacts produced. COA xlsx has 5 tables filled (Tables 3-4 carry 3 flagged advisee names + 6 corrected co-author names). Synergistic Activities PDF is single-page with all five entries sourced from internal records, including entry 5 combining WRT-2406 (delivered) and WRT-2516 (in-progress). Open items for user before May 19 submission listed in § 5.

---

## 1. Entry state

Session opened with the user warming up Ruflo and asking how to help complete documentation referenced "last Thursday" (the 2026-05-07 postwach-01 session). The 2026-05-07 archive had inventoried the NSF Dahlgren folder, surfaced two format mismatches, presented a fill plan, and listed nine gating questions; session ended at plan-confirmation with no drafting performed. This session picked that up.

Key constraints loaded from memory + prior archive:
- Deadline: NSF 25-540 (TTP) on 2026-05-19.
- Two artifacts only: NSF COA xlsx + NSF Synergistic Activities pdf. NSF biosketch and C&PS (DOE format only on file), narrative, budget, and NSWCDD letter-of-collab all out of scope.
- Submitter org RTSync, operational anchor NSWCDD, Bo Zeigler may participate within bandwidth.
- User preferences: discuss before executing; no fabricated identifiers; no em dashes; define abbreviations at first use; auto-spawn background agents for non-critical-path work.

---

## 2. Method

Direct conversational session with three background-spawned researcher agents running in parallel under deadline pressure.

1. **Pickup briefing.** Re-read the 2026-05-07 archive; presented status + plan + four-option drafting-mode question for Synergistic Activities. User selected "Draft 5 candidates from portfolio context."
2. **Wach_Collaborators_List.xlsx extraction.** Dumped the DOE-format xlsx (34 collaborator rows + Senior-Key tab). Mapped to NSF COA five-table structure. Identified Karson Sandman as Table 2 (personal preclusion), Salado + Beling as Table 3 advisors, the 10 "advisee"-tagged entries as Table 3 advisee candidates, the 21 "co-author"-tagged entries as Table 4 candidates.
3. **First-name integrity check.** User pushed back: "many of those first names are made up." Cross-referenced against `cv-2500231.pdf` SciENcv biosketch (10-publication subset). Confirmed last-name + first-initial match on 13 of 34; flagged that biosketch initial-match is NOT sufficient because a fabricator using the right initial would pass. User corrected one example directly: Gregory Jared → Gregory Joe (right initial J, wrong full name). This was the trigger for adopting external-source verification.
4. **Parallel agent fan-out.** Spawned three concurrent background researcher agents:
   - **Agent C — first-name verification** (33 names against CrossRef, ORCiD, faculty pages, conference proceedings).
   - **Agent A — Synergistic Activities** (research WRT-2516, draft 5 entries, render PDF).
   - **Agent B — Wach affiliation fact-check** (VT end month, Aerospace current status, Zeigler UA appointment).
5. **COA structural fill.** Saved template as `Wach_NSF_COA.xlsx`. Filled Table 1 (Wach 4 affiliations from biosketch), Table 5 (None within 24-month window). Tables 2-4 deferred until Agent C returned.
6. **Agent returns + corrections applied.** Agent C delivered 5 new fabrication corrections (Philipbar→Brad M., Jugan→Brady, Sonanis→Atharva, Sherburne→Tim, See Tao→Hoong Yan) plus formal-form upgrades (Madachy→Raymond J., McDermott→Thomas A. Jr.), and flagged 3 UNVERIFIED advisees (Iyer, Anderson, Ashok). Agent B confirmed Zeigler is UA Professor Emeritus, ECE department; VT year confirmed but month not publicly recoverable; Aerospace current status unverified (biosketch self-attests, tertiary profiles lean past tense). Agent A produced the PDF with entry 5 marked [PLACEHOLDER] because WRT-2516 was not publicly indexed.
7. **Table 2-4 fill with corrections.** Inserted rows (4 in Table 3, 15 in Table 4) via openpyxl `insert_rows`; populated all entries with verified names; cleared residual template hyperlink.
8. **Entry 5 internal-records pull.** User directed: "use WRT-2406 along with current knowledge of WRT-2516 projected activities. Use internal records." Grep across `03 Projects` returned: WRT-2516 = "Systems Engineering Beyond the Horizon" (CSER 2026 paper acknowledgment, `scripts/build_cser2026_pptx_v2.py`); TRAK = "Transformation Roadmap Assessment Kit" (TRAK_combined_v16.md, MOCRA white paper); Problem Definition + TRAK Workbenches (SEAD handoff tickets, April 2026); WRT-2406 details (biosketch top10_products.md item 10: 77 pages, Sep 2025, 49/29/5 findings, Statement A). Rewrote entry 5 as a single coherent activity covering both WRTs; regenerated PDF; confirmed single-page.

---

## 3. Deliverables

### Files created in proposal folder (`03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/`)
- `Wach_NSF_COA.xlsx` — NSF COA with 5 tables filled
- `Wach_NSF_Synergistic_Activities.pdf` — single-page NSF PAPPG-format Synergistic Activities
- `Wach_NSF_Synergistic_Activities.md` — markdown source for the PDF
- `_build_synergistic_pdf.py` — reportlab build script (NSF template layout)

### Files NOT modified
- `NSF COA TEMPLATE.xlsx` — original template untouched.
- `NSF Synergistic Activities TEMPLATE.pdf` — original template untouched.
- `cv-2500231.pdf`, `cpos-2501395 (1).pdf` — DOE biosketch + C&PS, read-only.
- `Wach_Collaborators_List.xlsx` — DOE-format collaborator list, read-only (contains fabricated first names per § 2.3).

### Session-management files
- `docs/session-archives/SESSION_ARCHIVE_2026-05-18_postwach-01.md` — this archive.
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-18-postwach-01.yaml` — productivity scorecard.

---

## 4. Decisions (durable)

- **D1 (fabrication pattern in Wach_Collaborators_List.xlsx).** Source xlsx carries ~6 fabricated first names matching the pattern: correct first initial + invented full name. Confirmed cases: Gregory Jared→Joe (user-corrected), Philipbar Brandt→Brad M., Jugan Bryan→Brady, Sonanis Anand→Atharva, Sherburne Tom→Tim, Tao Hao→See Tao Hoong Yan (surname is "See Tao"). The xlsx must not be treated as source of truth for any future deliverable; verify against CrossRef metadata or institutional pages.
- **D2 (verification heuristic for NSF submissions).** When NSF deliverable carries identifying info pulled from an internal-curated list, cross-check at least last-name+first-initial against authoritative publisher metadata. Biosketch initial-match is necessary but NOT sufficient because fabricators preserving initials would pass. Treat agency-public sources (CrossRef DOI metadata, ORCiD, institutional faculty pages) as authoritative; LinkedIn/ZoomInfo as MEDIUM; absence-from-public as UNVERIFIED-not-WRONG.
- **D3 (Synergistic Activities entry 5 framing).** WRT-2406 and WRT-2516 are presented as one continuous translation pipeline (research findings → method → tools), not as two separate activities, because NSF prohibits "multiple examples to further describe the activity." WRT-2406 is the delivered prior task that grounds the entry in evidence (SERC-2025-TR-005, 77 pages); WRT-2516 is the active task that supplies the integration-and-transfer-of-knowledge anchor required by NSF.
- **D4 (Zeigler affiliation form).** Bernard P. Zeigler's UA appointment is "Professor Emeritus, Department of Electrical and Computer Engineering" (ECE, not SIE). Any proposal artifact that places him at UA-SIE should be corrected.
- **D5 (cross-implication: INSIGHT 2026 v3 docx).** The Philipbar correction (Brandt → Brad M.) likely affects the INSIGHT 2026 article currently with co-authors. Memory not updated; flagged for user.
- **D6 (deferred until user confirmation).** PhD-vs-MS filter on the 10 Table 3 advisees, VT end month for Table 1, Aerospace Corp current-status decision, submitter email choice (paulwach@arizona.edu vs DH Kim RTSync admin), WRT-2516 final-form Wach role designation. None blocking single-page Synergistic PDF or COA structural completeness; all blocking final pre-submission cleanup.

---

## 5. Open items the user must address before 2026-05-19 submission

1. **3 advisee first names UNVERIFIED.** Iyer, Anderson, Ashok in Table 3 carry `[VERIFY first name]` in the Optional column. Same fabrication pattern as the corrected six; PI should confirm from his own records (advisee roster, email).
2. **VT end month.** Table 1 has Virginia Tech listed without an end date. Public sources confirm year (2025) only. PI should supply month from his LinkedIn or CV.
3. **Aerospace Corp active?** Biosketch (self-certified 2026-04-28) says "2019–present"; tertiary profiles (ZoomInfo, Google Scholar) describe in past tense. Trust biosketch attestation unless PI says otherwise. If actually ended, remove from Table 1.
4. **PhD-vs-MS filter on Table 3 advisees.** All 10 currently written as "T:" thesis advisees. NSF Table 3 is for PhD-thesis advisees only; any MS-only or non-thesis-supervised should move to Table 4 or be removed.
5. **Submitter email.** Header field in Wach_Collaborators_List.xlsx was `[VERIFY] paulwach@arizona.edu OR DH Kim email`. The NSF COA xlsx does not have a submitter-email field in its template, so this is moot for Wach_NSF_COA.xlsx. It WILL matter for whatever Research.gov uploader account submits the package.
6. **Cross-implication INSIGHT 2026 v3 docx.** `02 My Outreach/INSIGHT 2026 AI History/Wach_Salado_INSIGHT_2026_AI_History_v3.docx` likely contains "Philipbar, Brandt" or similar; the correct form is "Philipbar, Brad M." (Brad Montgomery Philipbar; USAFA IFC). Check before any further INSIGHT review cycle.
7. **NSF biosketch + C&PS conversion.** Folder has DOE format only. NSF submission requires NSF-format from SciENcv. Out of scope this session.

---

## 6. Out-of-scope items not pursued

- NSF biosketch (NSF SciENcv conversion of `cv-2500231.pdf`).
- NSF Current and Pending Support (NSF SciENcv conversion of `cpos-2501395 (1).pdf`).
- Project Summary, Project Description, References Cited, Budget + Budget Justification, Data Management Plan, Mentoring Plan, Facilities/Equipment/Other Resources.
- NSWCDD letter-of-collaboration re-engagement (CRADA dormant per 2026-05-07 archive).
- Zeigler's separate COA xlsx (NSF requires one per senior personnel; only Wach's is in the folder).
- MEMORY.md Open Threads entry for this proposal — deferred since deadline is tomorrow and the archive captures pickup state.

---

## 7. Next session entry hints

- **Pickup file:** this archive. Open items in § 5 are the gating list for final pre-submission cleanup.
- **Source-of-truth files this session created:**
  - For NSF COA: `Wach_NSF_COA.xlsx` (replace the 3 `[VERIFY first name]` flags before submit).
  - For Synergistic Activities: `Wach_NSF_Synergistic_Activities.pdf` + `.md` source + `_build_synergistic_pdf.py`.
- **Verification table reference.** The first-name verification agent's full results (33 entries × Verified Name × Source × Confidence × Status) are inline in this conversation's turn-7 tool output. Not separately archived. If a future session needs the raw table, re-run a verification agent or scroll the conversation.
- **Tooling note.** openpyxl `insert_rows(row, amount)` shifts cells correctly but does NOT clear hyperlink objects on overwritten cells; do a `cell.hyperlink = None` cleanup pass after overwriting template example rows.
- **Tooling note 2.** Inline Bash heredoc with `<< 'PYEOF'` broke on complex Python content (quote escaping). The reliable path is: `Write` script to file, `Edit` for incremental modifications, then `python script.py`.
- **Build script lifecycle.** `_build_synergistic_pdf.py` is in the proposal folder; safe to delete after NSF submission.
