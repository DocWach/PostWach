# Session Archive: 2026-05-21 PostWach-05

**Date:** Thursday, 2026-05-21
**Hive:** PostWach (CTO)
**Branch:** `main`
**Theme:** Multi-FM ecosystem, Codex CLI + ruflo, tri-model review pipeline (V1/V1.5), FM-provenance governance.

## Context
Started with "warm up ruflo," moved through getting ChatGPT working in the VS Code CLI, and ended building and running a three-model adversarial review pipeline on shared ruflo memory plus the governance scaffolding to account for non-Claude foundation models.

## Accomplishments

### ruflo warm-up
- `ruflo v3.7.0-alpha.14` healthy; MCP bridge live; memory 207 entries, 100% embedding coverage (sql.js + HNSW).

### Codex CLI installed + integrated with ruflo (see `memory/project_codex_cli_ruflo.md`)
- Decision path: user wanted ChatGPT mainly *with* ruflo, no API spend. Resolved to Codex (ChatGPT-subscription auth) as a client of ruflo, not GPT-as-provider.
- Installed standalone **ARM64** binary `codex-aarch64-pc-windows-msvc.exe` (`rust-v0.133.0`) to `%LOCALAPPDATA%\Programs\codex`, on PATH. **No npm** (resolves the user's npm-fragility concern at the root). Auth = Sign in with ChatGPT (no key, no spend), model gpt-5.5.
- Registered claude-flow MCP in `~/.codex/config.toml` via the **`.cmd` absolute path** (bare `claude-flow` = `.ps1`, unspawnable). [R017]/[R106] compliant.
- Validated: Codex called `mcp__claude-flow__system_status` and got real data. Quirk: headless `codex exec` cancels MCP calls unless `--dangerously-bypass-approvals-and-sandbox`; interactive `codex` is the everyday path. Stdin-EOF hang fixed with `'' |`.

### Architecture Q&A
- Codex+ruflo reaches the hive-of-hives more broadly than Claude Code (Codex config is user-global vs per-hive `.mcp.json`). Gemini parity untested at the time. Startup: Codex spawns its own ruflo lazily (no separate warm-up); `dsp`+warm-ruflo is the Claude path. **Concurrency (two CLIs writing ruflo at once) untested = open Q3.**

### Tri-model review pipeline V1 + V1.5 (see `memory/project_tri_model_review.md`)
- **Home:** `02 My Outreach/Tri_model_review/`. Design approved (capability test = gate; methods paper = prize; reusable throughput pipeline). Sequential hand-off; each model does full red/blue/white; synthetic injected-flaw fixture (F1-F6 + decoy D1); pilot-data instrumentation.
- **V1:** Claude (non-blind, authored fixture, excluded from signal), Codex + Gemini blind. **Cross-CLI shared memory verified** (Codex wrote `review-v1/codex/*`, Claude read it back). Codex empirically falsified the fake citation via a CrossRef 404. Detection: Codex 5/6, Gemini 4/6; both missed F6. Codex's R9 exposed that decoy D1 had a real causal-claim weakness -> recall-vs-planted-flaws inadequate.
- **V1.5:** registered claude-flow in Gemini (`gemini mcp add ... .cmd ... mcp start` -> Connected first try; `--approval-mode yolo`, prompt via STDIN). Gemini wrote `review-v1/gemini-direct/*` directly. **Full 3-way cross-CLI shared memory verified** (all three FMs read/write one ruflo store). Findings: run-to-run nondeterminism (Gemini's two runs differed), blue-team confabulation ("47 was an earlier-draft error").

### FM-provenance governance (4 items, all done)
- **Investigation:** ruflo memory has NO producer field; each CLI spawns its own stdio MCP server on a shared DB; provenance today is just key-prefix (self-declared). Three levels: key-prefix (weak), self-tag (spoofable), infra-stamped (trustworthy, ZT Pillar 7, not available). See `governance/fm_provenance_findings.md`.
- **Fix now (PostWach scope):** orchestrator-stamped `provenance_manifest.md` + ruflo `review-v1/_provenance`; self-tagging baked into codex + gemini-direct prompts.
- **Ontology proposal (for GI-JOE):** `governance/ontology_extension_proposal.md` — `fm:FoundationModel ⊑ :SoftwareAgent, prov:SoftwareAgent`, `po:poweredBy`, PROV-O attribution (incl. mediated-write delegation), SHACL completeness shape, CQ C-FM-01/02. Extends existing PROV-O backbone.
- **Rule proposal (for triad):** `governance/rule_proposal_fm_provenance.md` — draft [R0xx] FM-provenance, framed as HOS L1 candidate; Fort Wachs owns the ZT attribution clause; ties to unresolved HOS L1-authorship decision.

## State at Session End
- Codex CLI: (b) demonstrated, integrated with ruflo. Gemini: (b) direct ruflo write demonstrated.
- Tri-model pipeline: (b) demonstrated, full 3-way; V1+V1.5 PASS; pilot data captured.
- FM-provenance: immediate fix applied (PostWach scope); ontology + rule are proposals pending GI-JOE and the triad.

## Resume Steps / Open
1. **V2:** independently-authored fixture (removes author-as-reviewer bias) + expert-adjudicated finding validity; then a real rough-stage manuscript for article pilot data.
2. **Cross-review layer** (user request): each model audits the others' findings (Gemini checks Codex+Claude). Motivated by the confabulation finding.
3. **Concurrency probe:** test simultaneous ruflo writes (Q3) before any workflow assumes it.
4. **Multi-run:** nondeterminism means single-pass review is unreliable; aggregate over runs.
5. **Provenance durable target:** local thin MCP proxy for infrastructure-stamped attribution.
6. **Hand-offs:** ontology proposal -> GI-JOE; rule proposal -> triad (gated on HOS L1 decision).
7. Methods paper needs a name + target venue (agentic-systems / AI-for-SE / swarm-productivity line).

## Governance / Notes
- [R016]: every capability tagged (Codex (b), Gemini direct (b), tri-model (b) 3-way; ontology/rule = proposals, not enacted).
- [R104]: tri-model artifacts confined to the `02 My Outreach/Tri_model_review/` tree, not repo root.
- [R105]: no keys printed/committed. `gemini mcp add` wrote a PROJECT-scoped `.gemini/settings.json` in the PostWach repo (no secrets) — flagged; relocate to user scope or gitignore.
- [R017]/[R106]: all three CLIs use the global `claude-flow` (`.cmd` abs path), never npx.
- Cross-hive discipline honored: ontology/rule changes drafted as proposals, not unilateral edits (GI-JOE owns ontology; L1 rule = triad/HOS).

---

## Continuation (after initial archive) — Cross-review layer + FM-provenance governance

### Cross-review layer (Resume item 2) — (b) demonstrated
Each blind model audited the OTHER models' findings (not its own), run sequentially to avoid concurrent ruflo writes. Audits stored to `review-v1/{codex,gemini-direct}/audit`; results in `metrics/cross_review_results.md`.
- **Codex caught Gemini's confabulation** ("47 was an earlier-draft error") + 5 more invented justifications -> peer audit removes confabulated content.
- **Gemini's audit ADDED a flaw nobody caught:** paired-t-test carry-over bias on the 28% claim (same experts, no counterbalancing) -> auditing also generates findings.
- Confabulator can't self-correct (validates *cross*, not self). Codex more rigorous in the audit role too.
- Provenance lesson: agents reliably write a `PROVENANCE:` line into the value but ignore the `tags` field -> attribution belongs in the payload.

### FM-provenance governance — ENACTED + handed off
- **Investigation:** ruflo memory has no producer field; each CLI runs its own stdio MCP server on a shared DB; no central broker. Trustworthy attribution needs infra-stamping (not available); near-term = orchestrator-stamped manifest + in-payload provenance. `governance/fm_provenance_findings.md`.
- **PostWach-scope fix applied:** `provenance_manifest.md` + ruflo `review-v1/_provenance`; self-tagging baked into prompts.
- **Rule [R018] ENACTED** in `~/.claude/CLAUDE.md` (global, all projects) by **principal approval, overriding the pending HOS L1 process.** Caveat: user-home location violates the HOS portability constraint; migrate to canonical governance locus when HOS exists.
- **Handoffs (committed locally, NOT pushed; user to push):**
  - GI-JOE ontology ticket `GI-JOE-FMPROV-001` (master `e1d30b5`) — fm:FoundationModel + PROV-O attribution + SHACL + CQs; Tier 2 enforcement now permitted since [R018] ratified.
  - Fort Wachs notification `FW-FMPROV-NOTIFY-001` (main `7a0031a`) — CISO to own the ZT Pillar 7 attribution clause + assess infra-stamping.
  - Alpha Empress `docs/adoption-tracker.md` Global Rules section (main `fcc6b03`) — COO tracks cross-hive compliance.

### Updated State at Session End
- Resume items **2 (cross-review)** and **6 (ontology handoff)** are DONE. Rule is enacted (not just proposed).
- **Pending user push:** three repos (GI-JOE, Fort Wachs, Alpha Empress) have local commits.
- Still open: V2 (independent fixture + expert adjudication), concurrency probe (Q3), multi-run aggregation, infra-stamp proxy, HOS L1 process (now with a principal-override precedent to reconcile), methods-paper venue.

### Governance flags (continuation)
- **Process precedent:** [R018] skipped HOS L1 + triad co-sign by principal override; CISO/COO informed after the fact. Reconcile in HOS planning.
- [R016]: cross-review layer (b); [R018] enacted (not proposal).
- [R105]: no secrets in any commit.
