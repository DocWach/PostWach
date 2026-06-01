# Session Archive — 2026-05-07 postwach-01

**Hive:** PostWach
**Scope:** Begin assembling NSF 25-540 (TTP) proposal artifacts with RTSync. User asked specifically for help completing the NSF COA xlsx and the NSF Synergistic Activities pdf. Session ended at the plan-confirmation point; no drafting performed.
**Platform:** Ruflo, claude-opus-4-7 (1M context), Windows 11.
**Outcome:** Folder inventoried, two format mismatches flagged, plan presented for both artifacts. Session terminated by user before drafting; pickup state is "awaiting user answers to open questions before fill."

---

## 1. Entry state

User opened the session asking to "warm up ruflo" and assemble info for an NSF proposal. Folder under work: `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/`. Solicitation: NSF 25-540 (NSF TTP — Translation to Practice), deadline May 19, 2026 (12 days from today). Submission would be through RTSync. NSWCDD (Naval Surface Warfare Center Dahlgren Division) is the operational anchor; their OSM and MAST programs use DEVS, which is RTSync's stack. Bo Zeigler is the natural co-PI but cannot meet the deadline due to schedule; user is exploring whether to submit anyway with RTSync, possibly with Bo participating where his bandwidth allows. Prior CRADA conversation with the OSM team lapsed several years back. User flagged a NAVSEA news article (2592281) about NSWC Dahlgren wargaming and simulation as flavor context.

User-named scope was strictly the COA xlsx and the Synergistic Activities pdf. Other proposal artifacts (project summary, project description, biosketch, C&PS, budget, FOA-required attachments) were out of scope for this session.

---

## 2. Method

Direct conversational session, no swarm. Single discovery+plan iteration; the user terminated before any fill work.

1. **Warm-up + folder inventory.** `claude-flow --version` -> v3.5.80. MCP `system_status` reported "unhealthy" (swarm health 0.4); flagged but not blocking. Listed the folder; 5 files: `cpos-2501395 (1).pdf`, `cv-2500231.pdf`, `NSF COA TEMPLATE.xlsx`, `NSF Synergistic Activities TEMPLATE.pdf`, `Wach_Collaborators_List.xlsx`.
2. **File reads.** Read the two NSF templates (both empty boilerplate), the DOE biosketch, the DOE C&PS, and dumped both xlsx files via openpyxl. The xlsx dump exceeded the 30KB output cap and was persisted to a tool-results file; re-read from there.
3. **Cross-reference against memory.** Searched ruflo memory for "RTSync Bo Zeigler DEVS NSWCDD Dahlgren OSM MAST CRADA" and "synergistic activities Paul Wach service editorial mentoring" — both returned 0 hits. No prior thread on this proposal in memory.
4. **Plan presentation.** Returned a structured status: folder inventory table, two pre-fill flags, table-by-table coverage matrix for the COA, and five candidate themes for Synergistic Activities with explicit "I do not have enough to draft these without your steer" framing. Asked the user the open questions per table and asked whether to draft 5 candidates or tighten user-provided bullets.
5. **Termination.** User replied "do other things" and asked for archive + scorecard + termination.

---

## 3. Deliverables

### Files read (no modifications)
- `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/NSF COA TEMPLATE.xlsx`
- `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/NSF Synergistic Activities TEMPLATE.pdf`
- `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/cv-2500231.pdf`
- `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/cpos-2501395 (1).pdf`
- `03 Projects/98 Proposal Phase/06 NSF_Dahlgren_RTSync/Wach_Collaborators_List.xlsx`

### New files
- `docs/session-archives/SESSION_ARCHIVE_2026-05-07_postwach-01.md` — this archive.
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-07-postwach-01.yaml` — productivity scorecard.

### Files NOT produced (deferred to next session)
- The two artifacts the user asked for (COA xlsx fill, Synergistic Activities pdf) — both blocked on user input per § 5.

---

## 4. Decisions (durable)

- **D1 (proposal context).** NSF 25-540 with RTSync as submitting org, NSWCDD as operational anchor (DEVS stack alignment via OSM and MAST programs). Wach is the lead point. Bo Zeigler may be senior personnel but has bandwidth constraints. CRADA history with NSWCDD OSM team is dormant, not closed; this proposal would re-open the channel.
- **D2 (existing folder data is DOE-format, not NSF).** `cv-2500231.pdf` is a SciENcv DOE biosketch. `cpos-2501395 (1).pdf` is a SciENcv DOE C&PS. `Wach_Collaborators_List.xlsx` is the DOE-format collaborators template (Senior-Key Personnel + Collaborators tabs; not the 5-table NSF COA structure). The NSF submission will need NSF-format equivalents from SciENcv. Flagged to user; user did not direct action this session.
- **D3 (Wach_Collaborators_List.xlsx is excellent source data for NSF COA Tables 3 and 4).** It already carries 33 collaborator entries dated 2022-2026 with relationship tags (advisor, advisee, co-author, collaborator, personal). The NSF 48-month window (since 2022-05-07) maps cleanly. Karson Sandman is tagged "co-author, personal" — a direct NSF Table 2 candidate.
- **D4 (Synergistic Activities will not be drafted blind).** NSF rules disallow lists and require specific examples of integration and transfer of knowledge. Five candidate themes were surfaced from portfolio context (INSIGHT 2026 article; SERC AI4SE/SE4AI Workshop; PhD/student mentoring; SE Math Foundations / Isomorphism Library public artifacts; DEVS / WySE community engagement). User has not yet confirmed which to use or whether they want Claude to draft from raw user bullets.
- **D5 (ruflo MCP health degraded).** `system_status` returned "unhealthy" with swarm health 0.4. CLI is fine. Not blocking for proposal-fill work, which does not need a swarm. Worth checking if a future cross-hive session needs MCP swarm tools.

---

## 5. Open questions to user (blocking next session's fill work)

These were sent in the plan presentation; user terminated before answering. Resolve these first when picking back up.

**For NSF COA xlsx:**

1. **Table 1 (affiliations last 12 months, since 2025-05-07).** Confirm: which of {RTSync (2026–), University of Arizona (2025–), The Aerospace Corp (2019–), Virginia Tech (ended 2025)} are still active. Especially: confirm Virginia Tech end month and whether Aerospace Corp is still on the roster.
2. **Table 2 (personal/family/business preclusions).** Confirm K. Sandman is a Table 2 entry (he's tagged "personal" in the DOE list). Anyone else?
3. **Table 3 (PhD advisors + PhD thesis advisees).** Advisors are confirmed: Salado, Beling. Of the 10 "advisee" entries in the DOE list (Sandman, Iyer, Husain, Ofsa, Jugan, Anderson, Shanmugam, Curran, Ashok, Sonanis), which are **PhD thesis** advisees vs MS-only or other supervised students?
4. **Table 4 (co-authors + project collaborators last 48 months).** Approve using the DOE list as the source of truth for Table 4 (minus anyone already in Table 3).
5. **Table 5 (editorial board / co-editors last 24 months, since 2024-05-07).** List any editorial roles you've held in window. None on file in the DOE artifacts.
6. **Senior-personnel roster.** DOE list shows Wach + Zeigler. Confirm: is anyone else senior personnel on this proposal?
7. **Submitter email field** in `Wach_Collaborators_List.xlsx` is currently `[VERIFY] paulwach@arizona.edu OR DH Kim email`. Confirm which email goes here. (Side note: per memory, `paulwach@arizona.edu` is preferred for portfolio deliverables; `DH Kim` is presumably an RTSync admin contact.)

**For NSF Synergistic Activities pdf:**

8. **Drafting mode.** Want Claude to draft 5 candidates from the surfaced themes for you to edit, or do you want to paste raw bullets and have Claude tighten them?
9. **Theme selection.** Of the five surfaced candidates (INSIGHT 2026 article; SERC AI4SE/SE4AI Workshop; mentoring thread; SE Math Foundations / Isomorphism Library; DEVS / WySE community engagement), which to use; which to drop; what to add. Possibles not on the list because no evidence in folder: courses taught, INCOSE/IEEE WG service in editorial-or-organizing role, public software releases, K-12 / outreach.

---

## 6. Out-of-scope items flagged but not pursued

- **NSF biosketch and NSF C&PS.** Folder has DOE versions only; NSF submission will need NSF-format from SciENcv. User did not direct action.
- **Proposal narrative (project summary, project description, broader impacts, references).** Not in folder. Not in scope this session.
- **Budget and budget justification.** Not in scope.
- **NSWCDD contact re-engagement.** Old CRADA channel is dormant. Not actioned this session; might be relevant for the proposal's "translation partner" letter of collaboration.
- **Bo's level of participation.** User is open to Bo participating "if he is interested in the topic" and within his bandwidth. Decision deferred.

---

## 7. Next session entry hints

- **Pickup file:** this archive. Open questions in § 5 are the gating list.
- **Source-of-truth files:**
  - For Tables 3 and 4 of the COA: `Wach_Collaborators_List.xlsx` (DOE format already populated).
  - For Synergistic Activities theme content: search PostWach memory + INSIGHT article folder + SERC AI4SE/SE4AI 2026 workshop report + SE Math Foundations / Isomorphism Library paper folder.
- **Deadline reality check:** May 19, 2026. As of 2026-05-07, 12 days. The two artifacts requested are low-effort once user answers § 5 questions. The bigger risk is the unscoped narrative + budget + NSF biosketch/C&PS conversion, which the user has not yet asked about.
- **Tooling note:** `python -c "import openpyxl..."` reads the NSF COA template fine but the dump exceeds 30KB and gets persisted to a tool-results file; read from there. PowerShell ZIP-API pattern from prior MOACRA session may be useful if any docx files enter the proposal folder.
- **Format reminder:** NSF COA xlsx must NOT be uploaded as PDF; it must be `.xlsx` and uploaded under Senior Personnel Documents in Research.gov. Per template instructions: do not alter columns, can insert rows.
- **No memory write yet for this proposal thread.** Decision: wait until either the user confirms submission intent or the artifacts are produced. If deferred again, add an Open Threads entry to `MEMORY.md` titled "NSF 25-540 (TTP) RTSync proposal" pointing to a `project_nsf_25540_rtsync_dahlgren.md` memory file.
