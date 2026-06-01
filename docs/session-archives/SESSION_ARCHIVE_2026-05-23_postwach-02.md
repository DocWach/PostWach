# Session Archive — 2026-05-23 postwach-02

**Hive:** PostWach
**Scope:** SDA SBIR Direct-to-Phase-II proposal, topic OSW26BZ02-DV004 (Game-Theoretic AI for Robust COA Generation and Wargaming). Warm up ruflo, review Brad Philipbar's Tuesday repo work, then draft Technical Volume 2 as a capability-first, team-holistic, Wach-independent draft into the OneDrive folder, and share it to the proposal-team repo.
**Platform:** ruflo v3.7.0-alpha.14, claude-opus-4-7 (1M context), Windows 11. Pandoc + pdflatex for Word/PDF.
**Outcome:** Vol. 2 Part 1 (Phase I Feasibility) and Part 2 (Phase II Technical) drafted in MD and rendered to Word; a clean combined volume produced in MD/Word/PDF (internal notes stripped) and contributed to `bmpwach-lab/SBIR_D2P2_OSW26BZ02-DV004` as PR #12.

---

## 1. Entry state

User: "Proposal drafting. warm up ruflo. Working folder: 02 SDA/OSW26BZ02-DV004. Check bmpwach-lab git repo for work that Brad added on Tuesday." ruflo confirmed live (MCP stdio, pid 37952; 195 memories imported at session start). No prior DV004 entries in ruflo memory. Local SDA folder held the BAA template `OSW26BZ02-DV004_TechVolum_V1.docx`, a Go/No-Go memo (CONDITIONAL GO, 2026-05-19), and the SCO topic PDF.

## 2. Brad's Tuesday work (located)

`bmpwach-lab/SBIR_D2P2_OSW26BZ02-DV004`, created Tue 2026-05-19 20:56Z (`7a2b5e0`) and driven through Wed. Contains a full LaTeX shred of Vols 1/2/3/5/7, a research/strategy swarm output, V&V lock-down (Option ZOmega, CI gate, SHA-256 manifest), the HIGH MESA TRIAL scenario, locked decisions (brand=ZynWorld; solver=Stackelberg+PSRO Phase I / MCCFR Phase II), SAM.gov SUBMITTED. Prime=RTSync, sub=Philipbar Analytics LLC (PA-LLC). Close 2026-06-23 (DSIP), $2M, 12-mo PoP. Blocked items: Gmail OAuth re-grant + RTSync data package. Repo is the live source of truth; not cloned locally (read via GitHub API).

## 3. Method

1. Confirmed proposal scope against the parsed BAA: Vol. 2 = 15pp (Part 1 Phase I Feasibility 5pp + Part 2 Phase II 10pp, subsections 2.1-2.7). Consistent with a standard DoW D2P2.
2. **Flagged template contamination:** the OneDrive docx Phase I bullets ("secure LLM," "fine-tuning LLMs," "TS/SCI," "air-gapped," "classification, security planning") are lifted from a separate SCO topic. Drafted to the real DV004 ATTR-1..5 / FEAS-1..5 from `SCO_SBIR_26BZ_D2P2_R2.pdf` instead.
3. Established the holistic capability inventory and the corrected provenance chain: IS 2026 papers 427 (math-based data structures, Wymorian morphism foundations) and 490 (DEVS/SES "Queen" orchestration) are precursors; ZynWorld is the engine built from them; ZynWorld debuted publicly at IGNITE 2026 (Berserker SEAD); Brad then used it in a USAFA exercise (likely CULEX, unconfirmed). All three papers confirmed "to appear."
4. Read source artifacts: Brad's FEAS-1..5 + Part 2 sections, STIDS MTO paper, IS 427 + 490 reviewer catalogs, IGNITE `wymore-metrics.json` (real computed degree-of-homomorphism / behavioral-distance values, 7 subsystems, 2026-03-19), CSER 2025 citation.
5. Drafted **Part 1** (FEAS-1..5): ZynWorld measured results as spine; added RTSync DEVS pillar, IGNITE morphic-fidelity bound, STIDS MTO interpretability layer (third-party openCAESAR/OML SEAD validation), maturation timeline. Two-layer fence (CPU-only runtime vs. agentic build/verify). External anchors against circularity.
6. Drafted **Part 2** (Objectives + Tasks 1-5 + 2.2-2.7): aligned to Brad's Task 3/5/Commercialization, filled his stubs; SES "Queen" V&V-complexity-reduction + safety-case theorems de-risk Tasks 1/3/4; Wach placed in Key Personnel under RTSync; 5 commercialization questions answered.
7. Page-budget check: Part 1 ~5pp (on budget); Part 2 ~4.5pp of 10pp (deliberate headroom pending RTSync inputs).
8. Produced a clean combined volume (internal notes stripped, leak-check 0) in MD/Word/PDF; contributed to the team repo as PR #12 under `docs/sbir/contrib/wach-vol2-capability-first/` with a README documenting basis + provenance.

## 4. Deliverables

In `03 Projects/02 SDA/OSW26BZ02-DV004/`:
- `OSW26BZ02-DV004_TechVolume_Part1_Feasibility_draft_2026-05-23.{md,docx}` — Part 1, with internal [R016] note (local only).
- `OSW26BZ02-DV004_TechVolume_Part2_PhaseII_draft_2026-05-23.{md,docx}` — Part 2, with internal note (local only).
- `OSW26BZ02-DV004_TechVolume2_draft_2026-05-23.{md,docx,pdf}` — clean combined volume (shareable).
- Working extracts: `_bradvol2/` (Brad repo files), `_techvol_v1_extract.md` (template). Not for sharing.

On `bmpwach-lab/SBIR_D2P2_OSW26BZ02-DV004`: **PR #12**, branch `contrib/wach-vol2-capability-first-2026-05-23`, clean combined volume (MD/Word/PDF) + README under `docs/sbir/contrib/wach-vol2-capability-first/`.

## 5. Decisions (durable)

- **D1.** Work surface = OneDrive docx (not a clone of Brad's repo); merge target for the final deliverable = Brad's repo. The capability-first draft is additive and reconcilable, not a replacement for the shred.
- **D2.** Vol. 2 framed as team-holistic and Wach-independent: feasibility rests on existing demonstrated artifacts, not Wach's future labor. Wach is named Key Personnel under RTSync.
- **D3.** Draft to the SCO topic PDF (ATTR/FEAS), not the contaminated OneDrive docx template.
- **D4.** All three papers cited as published/to-appear; no fabricated page numbers/DOIs/author orders ([PLACEHOLDER] where unknown). CSER 2025 = Wach, Iyer, Shanmugam, Curran, Ashok, CSER Long Beach 2025.
- **D5.** Degree of homomorphism written spelled-out (not sigma) per standing preference, even though the published paper and IGNITE code use sigma.
- **D6.** Internal "NOT FOR SUBMISSION" notes (candid [R016] maturity ledger, "1000x is RTSync marketing," CULEX/OCI caveat) kept local; only the clean combined volume pushed to the shared repo.
- **D7.** Pushed via PR (not direct to main) to respect Brad's CI gates; contributor path + provenance README.

## 6. Open threads / next steps

- **PR #12** awaits Brad/team review and CI gate.
- **Open confirmations before submission:** PI name + resume (GoNoGo Decision #2 unresolved); B. P. Zeigler participation; RTSync facilities + market-size/funding figures; AFSIM access or teaming partner; USAFA exercise name (CULEX = A5 government-owned, demo reference only); author lists for IS 427/490 + CSER 2026.
- **Part 2 headroom:** ~5.5pp unused in Phase II; invest in work-plan task detail, a risk register (eval analysis flags robustness as heavily read), commercialization specifics, and Key Personnel resumes once RTSync inputs return.
- **Page-budget truth:** final pagination requires the formatted template (Brad's repo page gate).

## 7. Next session entry hints

- MD is the source of record; Word/PDF are pandoc-generated (pdflatex for PDF). Combined clean file built by stripping from `## INTERNAL NOTE` and appending Part 1 references.
- Brad's live draft + parsed BAA analysis are in `bmpwach-lab/SBIR_D2P2_OSW26BZ02-DV004` `docs/sbir/`; read via GitHub API or the local `_bradvol2/` extracts.
- Triggered by team feedback on PR #12, RTSync inputs (PI, AFSIM, market figures), or a decision to expand Part 2 into its headroom.
