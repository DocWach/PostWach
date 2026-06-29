# Session Archive — 2026-06-22 postwach-02

**Hive:** PostWach (CTO). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8.
**Headline:** Stood up a new hive, **Finance Bro** (assistant for a financial manager), narrow-first: scaffold + V3 governance `[F101-F114]` plus a working DOL Form 5500 client-prospecting vertical validated on real 2023 data, then connected and pushed it to `DocWach/Finance-Bro-Hive`.

---

## Context
Principal requested a new hive from a scoping `.docx` in `01 Hives/10 Finance Bro`: an assistant for a financial manager spanning **both** money/risk management and managerial / business-development ("finding new clients"). First concrete task: collect and characterize the DOL Form 5500 filings site (`efast.dol.gov/5500Search/`). The scoping doc pointed to "initial ideas from a real financial manager" that were **not in the file** (no text/image/embed); the principal confirmed those notes are still pending and to push forward.

## Decisions (clarified with principal)
- **Name/location:** "Finance Bro," in the existing `10 Finance Bro` folder (not the empty `03 Lawson`).
- **Build strategy:** narrow-first — scaffold + governance, then one working vertical (Form 5500), grow iteratively.
- **Investing engine:** `Papers/AI_Investing_Platform` (README "Financial-Manager," ~31k-line quant engine; R016 **(a)** research artifact, zero client/CRM/5500 code) is **referenced as the money/risk backend, not folded in**.

## The reuse-vs-new debate (the deliverable the principal asked for)
Two parallel Explore agents characterized (1) the AI_Investing_Platform codebase and (2) reusable cross-hive assets + the lean Fort Wachs scaffold. Conclusion: **~70% of v1 is wiring existing parts.**
- **Reuse:** BP Marketing (BD/prospecting swarm), MACQ (`deliverable-generator`/`document-automation`/`persona-router`), GI-JOE (`browser` + ontology), Fort Wachs (PII/compliance policy), the V3 governance template.
- **Reference, don't fold:** AI_Investing_Platform as the money/risk backend.
- **New:** finance orchestrator (queen), lightweight prospect data model (no CRM exists anywhere in the portfolio), the Form 5500 ingestion+characterization skill, finance-specific rules.

## What was built — `10 Finance Bro`
- **Scaffold + governance:** `CLAUDE.md` (V3 `[F101-F114]`: F110 client/prospect PII = critical, F111 no-investment-advice / non-fiduciary posture, F112 data-source terms, F113 synthetic-vs-real, F114 R016 tagging), `README.md`, `.mcp.json` (global `claude-flow mcp start` per R017), `.gitignore` (data + secrets stay local).
- **Agents** (`.claude/agents/custom/` so they're tracked, not gitignored as boilerplate): `finance-queen` (routes managerial vs money/risk), `prospect-researcher` (adapts BP Marketing's market-researcher), `client-data-steward` (PII/compliance gate).
- **Form 5500 vertical:** `form5500-prospecting` SKILL.md + `scripts/ingest_form5500.py`. **Bulk-first** collection from DOL's published per-year datasets (verified URL `https://www.askebsa.dol.gov/FOIA%20Files/<YEAR>/Latest/F_5500_SF_<YEAR>_Latest.zip`); the `browser` skill is reserved for targeted UI lookups, not record-by-record scraping. Script is **schema-tolerant** (matches the 191 real columns by pattern, not hardcoded names) and stamps a `PROVENANCE:` line (real DOL data, F113). **Validated on real 2023 5500-SF data: 306/500 filings scored**, top prospects exactly the advisory sweet spot (small-employer 401(k) plans, $1-9M, 10-73 participants). Prospect **scoring is a swappable config block** — the pending FM criteria slot in there with no downstream rework.
- **Portfolio bookkeeping:** added Finance Bro to PostWach `docs/project-registry.md` (Tier-1, V3 count 9->10, backend reference, reuse sources) and `docs/capability-index.md` (1 skill, 3 agents, 5 reuse entries).

## GitHub
- Principal created `https://github.com/DocWach/Finance-Bro-Hive` (had a GitHub auto-stub README).
- `git init -b main`; **reviewed staged set before any push** — the 131MB DOL zip and prospect CSV are correctly gitignored; only 14 small files staged (largest 16KB), no secrets/PII.
- Push rejected (remote stub README) -> merged unrelated histories `-X ours` to keep the full hive README -> pushed. **Remote audit confirms NO `.zip` / prospect CSV / `.env` on origin.** Local `main` tracks `origin/main`.

## Tooling notes / environment
- **WebFetch 403** on the DOL datasets page; worked around with a `curl -I` HEAD probe to confirm the real bulk-file URL pattern (note the `www.` host and the literal space in `FOIA Files` -> must be `%20`-encoded for urllib).
- 5500-SF (short form) is the right prospecting source: small plans, total assets on the form itself (`SF_TOT_ASSETS_EOY_AMT`); the full Form 5500 puts assets on Schedule H/I.

## Lessons
- **Run it on real data, don't assert the schema.** The column mapper first grabbed `SF_SPONSOR_DFE_DBA_NAME` (usually blank) over `SF_SPONSOR_NAME`; only visible because the run printed blank top-5 names. Pattern-match + inspect-the-header beats hardcoding. ([[feedback_probe_artifact_not_narrative]] family.)
- **Review the staged set before pushing a brand-new repo.** A 131MB dataset sitting in `data/` would have been a costly first commit; `git check-ignore` + `git ls-files --cached` confirmed the gitignore worked before the push, not after.
- **Cross-hive scope -> recon first.** Two parallel Explore agents up front turned an open-ended "what to reuse" into a concrete decision table; this is the [[feedback_check_memory_on_cross_hive_questions]] pattern applied to capability reuse.

## Memory updates
- `project_finance_bro.md`: new — hive scope, build decisions, Form 5500 vertical, reuse map, open items.
- `MEMORY.md`: index pointer under the CTO role section ("Finance Bro created 2026-06-22"); V3 count 9->10.

## Termination
- 2 Explore subagents (codebase recon, reuse/scaffold recon) completed and returned; none left running.
- `claude-flow agent list` -> no active agents. Found one **stale empty swarm** (`swarm-1776781909882-7ml8wf`, 0 agents / 0 tasks, ~62h... 1490h elapsed = ~62 days old, not from this session) and **stopped it** (`swarm stop`) per the no-orphaned-agents governance.
- Open (non-blocking): real financial manager's prospecting criteria pending (swappable `SCORING` hook ready); `browser`-skill spot-check vs the live 5500Search UI is the documented next verification step; principal may want the repo URL added to the registry entry.
- Scorecard: `Papers/AI_Swarm_Productivity/data/scorecards/2026-06-22-postwach-02.yaml`.
