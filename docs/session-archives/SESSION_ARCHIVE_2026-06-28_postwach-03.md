# Session Archive — 2026-06-28 postwach-03

> NOTE: renumbered from postwach-02 → postwach-03 at session end: a concurrent PostWach session
> (the dissertation-journal R019 work) had independently claimed the postwach-02 slot tonight. That
> concurrent session is the "concurrent writer" flagged in §8 (it promoted the foundational SE refs).

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI) orchestrated this session, the worklists, the
> pilot reference promotions, this archive, and the scorecard. ruflo/claude-flow v3.10.40 was warmed up at
> session start (no claude-flow MCP sub-agents spawned; coordination used the Claude Code Agent tool).
> Background agents spawned via the Agent tool (all claude-opus-4-8): KannanDiscovery (researcher),
> SaladoInventory, HarvestSaladoJournals, HarvestSaladoConf, HarvestKannan (general-purpose). External
> bibliographic sources read: CrossRef API, Unpaywall API, ORCID, DBLP. No external model agents this session.

**Hive:** PostWach. **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m]. **Status:** ACTIVE (Wave-1
local-harvest agents running at time of writing).

**Headline:** Began a portfolio task to locate, download, and add the complete publications of **Alejandro
Salado** and **Hanumanthrao "Rao" Kannan** to their `04 Resource Library` folders, with a final step of
promoting each into the **R019 approved-references store**. Built structured worklists for both authors
(~240 in-scope items), **proved the reference verify→promote pipeline end-to-end** (3 pilot entries promoted
to `approved.bib`), discovered a large **local PDF trove** in the VT archives / EndNote stores, and launched a
**local-harvest swarm** as Wave 1 of the PDF acquisition.

## 1. Task framing (principal direction)
- Two target folders: `04 Resource Library\Salado` and `04 Resource Library\Rao Kannan`.
- Salado's publication list supplied as a PDF in his folder; Kannan's folder was empty (list discovered).
- **Scope (confirmed):** published journal + conference + magazine papers + publicly-released technical
  reports. Out: under-review, books, edited books/standards, book chapters, patents, invention disclosures.
- **Paywall handling (confirmed):** approve metadata + flag PDF for later UA-library retrieval.
- **PDFs are the main deliverable** (principal escalated this): get COMPLETE published versions, automate as
  much as possible. Principal pointed to ResearchGate + the VT archives as likely local/remote sources and
  asked for a **swarm**. Reference promotion authorized to proceed in background batches.

## 2. What was produced
- `04 Resource Library\Salado\_worklist_salado.yaml` — 208 in-scope items (53 journal / 116 conference /
  9 magazine / 30 tech reports), parsed verbatim from his publication-list PDF. IDs S-J##, S-C##, S-M##, S-T##.
- `04 Resource Library\Rao Kannan\_worklist_kannan.yaml` — 13 journal + 21 conference (out-of-scope: 1 book
  chapter, 1 PhD thesis, 1 arXiv preprint). IDs K-J##, K-C##. Kannan = Hanumanthrao "Rao" Kannan, UAH
  (ORCID 0000-0001-5307-7800), disambiguated from CS-theory "R. Kannan".
- **3 pilot references promoted** to `04 Resource Library\00 Verified References\approved.bib` (+ manifest):
  `@kannan2026theory` (Syst. Eng. 29(3) V&V), `@stephen2024formal` (Systems 12(5)), `@kannan2019preference`
  (Systems 7(4)). All single-model-triple-check vs CrossRef, clean 8-field MATCH, `pending_byzantine_verification: true`.
- 1 PDF downloaded so far: the V&V arXiv accepted manuscript (`Kannan_Salado_2026_...arXiv.pdf`) in the Salado folder.

## 3. Pipeline validation (refverify, previously "(a) research artifact, never run end-to-end")
- **Now (b) demonstrated.** `scripts/refverify.py` works: Step 0 DOI dedup correctly returns
  DUPLICATE-OF-APPROVED (e.g. `10.1002/sys.21463` → `@salado2018mathematical`) vs NOT-IN-STORE; field
  comparison is NFKD/hyphen/quote-normalized with substring containment; `--promote` appends to bib + manifest.
- **CrossRef API** (`api.crossref.org/works/{doi}`) is the workhorse for canonical metadata — fast, on the
  R019 allowlist. Set `PYTHONIOENCODING=utf-8` to avoid Windows cp1252 errors on en-dashes in titles.
- **Two gotchas found + solved:**
  1. The pending EndNote store (`pending/imported_from_endnote.bib`, 1562 entries) reuses `authoryearword`
     bibkeys. Passing `--candidate-bibkey` makes refverify verify the STALE abbreviated pending entry
     (e.g. `kannan2019theoretical` collided → author MISMATCH). Fix: **mint a non-colliding key** (checked vs
     both stores) — used `kannan2019preference`.
  2. `--promote` REQUIRES `--candidate-bibkey`; so each new entry needs a collision-checked minted key.
- **Data integrity:** `approved.bib` grew 121→124 real entries; `uniq -d` shows zero duplicate keys; no stray
  `kannan2019theoretical` entry. (`grep "^@"` reads 125 due to one pre-existing indented entry — cosmetic.)
- **Note on K-J7 "Elemental patterns of verification strategies" (`10.1002/sys.21481`):** Step 0 says
  NOT-IN-STORE — it is NOT yet approved despite being a well-known Salado/Kannan paper. Needs promotion.

## 4. PDF acquisition reality (the crux)
- **arXiv** downloads fine headlessly (curl).
- **MDPI is Akamai-bot-blocked** — 403 to curl, .NET, and versioned URLs; Unpaywall confirms mdpi.com is the
  only OA host. Gold-OA but needs **real browser automation** to fetch (the *Systems* journal papers).
- **Wiley Systems Engineering / IEEE Xplore / Springer** = paywalled (the dominant Salado + Kannan venues).
- **Local trove discovered (decisive):** the principal's VT archives + EndNote stores hold a large fraction,
  often as PUBLISHED-version PDFs. Key stores (under `…\OneDrive - University of Arizona\Documents`):
  `04 Resource Library\01 Reading` (575), `…\Math of MBSE` (2198, organized by publisher),
  `00 Verified References\Archive\EndNote_VT` (3337, EndNote .Data\PDF stores),
  `Z99 VT Archive\VT plaptop\02 Articles` (580), `02 My Outreach\00 Master Copies` (53). Salado heavily
  represented; Kannan sparse (mostly remote/paywalled, the hard residual).

## 5. Swarm architecture (PDF acquisition)
- **Wave 1 — local harvest (RUNNING):** 3 background agents copy the best PUBLISHED local copy of each
  worklist item into the target folder (copy-only, never move; reject drafts/abstracts/reviewer copies;
  validate `%PDF` signature). Agents: `HarvestSaladoJournals` (S-J/S-M/S-T, 92 items), `HarvestSaladoConf`
  (S-C, 116), `HarvestKannan` (K-J/K-C, ~31). Each writes a `_harvest_report_*.md` to its target folder.
- **Wave 2 — remote residual (PENDING harvest reports):** per missing item, waterfall Unpaywall OA → arXiv →
  VTechWorks/institutional repo → browser automation (MDPI) → ResearchGate → else flag PDF-unavailable.
- **References (parallel, serialized writes):** drive CrossRef→refverify over the worklists via a
  deterministic script (NOT concurrent --promote calls — appends would race/corrupt the governed store).

## 6. Open threads / next steps
- [ ] Collect Wave-1 harvest reports (3 agents); compute coverage; build the consolidated missing-PDF list.
- [ ] Wave 2 remote downloads; stand up/verify browser automation for MDPI OA PDFs; test ResearchGate +
      VTechWorks yield. Decide browser-tooling path.
- [ ] Reference promotion of the full in-scope set via CrossRef→refverify (serialized). Resolve DOIs for
      conference papers (CrossRef title query); confirm AIAA "inferred" DOIs before promoting (R019/R109).
- [ ] Promote K-J7 Elemental Patterns (known gap).
- [ ] Produce the `PDF-unavailable` manifest (paywalled + bot-blocked items) with direct links for UA-library.
- [ ] R016 status: refverify pipeline now **(b) demonstrated**. Folder population + approved-store backfill
      are the integrated deliverable in progress.

## 7. Key paths
- Worklists: `04 Resource Library\{Salado\_worklist_salado.yaml, Rao Kannan\_worklist_kannan.yaml}`
- Approved store: `04 Resource Library\00 Verified References\{approved.bib, manifest.yaml}`
  (backups `*.bak-pre-wyse-20260628` predate this session's 3 additions)
- Tooling: `01 PostWach\scripts\{refverify.py, reflookup.py, refcheck.py}`; skills `/refverify /reflookup /refcheck`
- Salado source list: `04 Resource Library\Salado\Salado list of publications.pdf`

## 8. Results (working-session end) + concurrency flag
- **References promoted by this session: 141** Salado/Kannan papers (+ 3 pilot + 3 driver-test), via `promote_refs.py` (serialized refverify; gate `title_sim >= 0.92`; CrossRef canonical). Zero MISMATCH. All R019 single-model-triple-check, `pending_byzantine_verification: true`.
- **CONCURRENCY FLAG (no action taken, per principal):** `approved.bib` grew to **320 entries**, ~54 MORE than this session's promotions account for. The extra keys are foundational SE references (`wymore1976sem`, `zeigler2000theory`, `bertalanffy1968general`, `page2021prisma`, `omg2019sysml16`, ISO/IEEE standards) with `publisher/address/isbn` fields and formatting **this session's script never emits** — added by a **concurrent writer** (another session or the `docs/phase3_backfill` effort) around 19:47. Integrity verified clean: **no duplicate keys, no duplicate DOIs, every bib entry has a manifest entry**. The interleaved appends did not corrupt the store this time, but two processes appending to one governed `approved.bib` is a live race-corruption hazard. Pre-bulk backups: `approved.bib.bak-pre-bulk-20260628`, `manifest.yaml.bak-pre-bulk-20260628`.
- **PDFs acquired this session: 47** (Salado 42, Kannan 5): 30 local harvest + 8 OA curl [IEEE OJSE, ASEE PEER] + ~6 green-OA [UA repository.arizona.edu] + 3 VTechWorks (DSpace7) VT-era manuscripts.
  - Download reality solved: MDPI/Wiley/IEEE block headless curl AND Playwright `request.get` (JS challenge / paywall). Green-OA via repository copies is the working lever. **Gotcha:** `repository.arizona.edu` blocks the long realistic Chrome UA but allows short `Mozilla/5.0 Chrome/124.0` (and 403s Python urllib regardless — must shell to curl).
- **Manifests:** `_PDF_status.md` in each author folder. FINAL: Salado HAVE 42 / paywalled 91 / unresolved 75; Kannan HAVE 5 / paywalled 27 / unresolved 2. TOTAL HAVE 47 / paywalled 118 / unresolved 77 of 242.
- **VTechWorks pass (done):** `vt_repo_search.py` searched 198 not-yet-held items; +3 PDFs (S-J49 SLR, S-J29 IoT, K-J8 preference); correctly skipped already-held (morphisms/equivalence harvested locally). Arizona DSpace6 `/rest/discover` is 403-blocked, so green-OA covers UA-repo only.
- **approved.bib continued growing to 327** during the session (concurrent writer still active — flag stands).
- **Reusable tooling (in `%TEMP%\refpilot`):** `resolve_pubs.py` (DOI+OA resolution), `promote_refs.py` (bulk refverify), `download_oa.py`, `green_oa.py` (multi-UA curl), `vt_repo_search.py`, `build_manifest.py`. Result TSVs in the Verified References folder (`_resolution_master.tsv`, `_promotion_results.tsv`, `_download_results.tsv`, `_green_oa_results.tsv`, `_pdf_browser_needed.tsv`, `_vtechworks_results.tsv`).
- **Still open:** ~92 paywalled Salado + 28 Kannan (UA library / ResearchGate); 78 unresolved (manual DOI for tech reports, 2026-INCOSE-not-yet-in-CrossRef, older confs) then promote; Kannan K-C23 (CSER 2019 Bayesian Networks) not located.
