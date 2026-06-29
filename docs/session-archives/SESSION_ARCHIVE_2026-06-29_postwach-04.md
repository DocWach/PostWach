# Session Archive — 2026-06-29 postwach-04

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI) ran this session: the reuse-vs-create
> analysis, the Lawsun hive build, governance, the citecheck gate (4-gate + Bayesian + eyecite +
> CourtListener client), the two design corrections, the test plan + harness, and all docs. ruflo/
> claude-flow (v3.14.4) warmed up at session start (system_health = healthy, score 100). Three Agent-tool
> Explore subagents (inherited Claude model, read-only, completed) scouted MACQ/BP, GI-JOE/Fort Wachs, and
> PostWach citation assets. The plan was adversarially vetted by a tri-model red/blue/white panel run over
> external CLIs: Gemini 2.5-pro (red), Codex gpt-5.5 (red + blue), Gemini 2.5-flash (blue). No persistent
> ruflo swarm was initialized; swarm_status = terminated, 0 agents. No manuscript citations authored, so
> R019 refcheck not triggered (Lawsun has its own legal-citation gate, LW112).

**Hive:** PostWach (CTO / Chief Scientist), building **Lawsun** (new Tier-1 hive). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m]. **Status:** CLOSED.

**Headline:** Planned and built **Lawsun**, a legal-assistant hive ("bringing light to the law"). Answered
the reuse-vs-create question, vetted the plan via tri-model red/blue/white, scaffolded governance +
the legal-research/citation-verification vertical end-to-end, then hardened it through two
principal-driven design corrections and a plan-driven test harness. Repo `DocWach/Lawsun` pushed.

## 1. Task framing (principal direction)
- "Warm up ruflo. Help create a legal assistant (Lawsun). What skills/agents/hive-mind/swarms to reuse vs create? Enter planning mode."
- Add a curated logic/philosophy layer (debated, agreed). Vet the plan with Gemini + Codex red/blue, ruflo as white. Then: build; commit + push; explain defaults; implement two design changes; add token note + legal-sources doc; build the test harness with a driving test plan; do the quick-win tests.
- Close: archive, scorecard, terminate.

## 2. Reuse-vs-create (the recommendation, delivered)
- **Reuse:** ruflo hive-mind/swarm infra; the portfolio **R019 citation protocol** (refcheck/refverify/reflookup) as the anti-hallucination core; **TRAK Bayesian aggregation** (already in R019 §5); GI-JOE `browser`/ontology; MACQ drafting skills (later); Fort Wachs compliance; a **curated** logic/philosophy subset (NOT wholesale import of PostWach's 100+ math library) incl. ethics agents (`justice-arbiter` etc.).
- **Create:** `legal-research`, `citecheck`, `legal-argumentation` (rescoped to proposition-support) skills; `lawsun-queen`, `legal-researcher`, `cite-checker`, `confidentiality-steward` agents (+ 3 stubs); governance [LW101-LW117]; tools `eyecite` + CourtListener.

## 3. Tri-model red/blue/white (white = ruflo/Claude adjudication)
- Both reds converged independently on: existence ≠ good law (overruled); proposition support (real case / wrong holding); query-leak of privilege; academic BibTeX parser ≠ Bluebook (use `eyecite`); stale-cache TTL; source hierarchy; human-review/liability. Codex red surfaced ABA Model Rule 1.6 + Formal Opinion 512 as the ethics anchor.
- Verdict: architecture CONFIRMED; **citecheck hardened 1-gate → 4-gate** (exists / good-law / jurisdiction / proposition). Contested item (`legal-argumentation` "scope creep") resolved by **rescoping** v1 to proposition-support only. Gemini blue needed flash model + GEMINI_API_KEY to clear a pro-endpoint 503 storm.

## 4. Build (committed to DocWach/Lawsun)
- Scaffold (Finance Bro pattern): `CLAUDE.md` [LW101-LW117], `.mcp.json` (npx-free), legal `.gitignore`, README, 4 agents + 3 stubs, 3 skills, MANIFEST.
- Gate: `scripts/citecheck.py`, `data/authorities/verified_authorities.json` (good-law + known-overruled, 30-day TTL), adversarial + passing fixtures, mock citator. Verified: on-point passes, fabricated/overruled/wrong-jurisdiction/wrong-proposition/bare fail closed; LW116 canary never leaks.

## 5. Two principal-driven design corrections (post-build)
- **(a) Confidence is REPORTED, not a gate.** Decoupled precedential weight/posterior from the four defect gates. Gates fail only on a real defect or genuine uncertainty about that determination; low weight never blocks valid authority. Fixed the false-negative where valid persuasive authority (Tarasoff) was blocked — it now correctly fails only gate 3 (jurisdiction), confidence 0.855 reported. Optional `--min-confidence` soft floor (off by default).
- **(b) eyecite + CourtListener wired as the live default.** `eyecite` replaces the regex extractor (caught `id.` short forms the regex couldn't); CourtListener is the live citator behind a cache-first resolver (`verified_authorities.json` = 30-day TTL cache); `--citator mock` for CI. CourtListener confirms existence only (401 anonymous → needs `COURTLISTENER_TOKEN`); good-law/binding come from curated cache, so novel cites fail gates 2/3 closed (no free citator — honest limit). citecheck/eyecite/CourtListener now R016 **(b) demonstrated**.

## 6. Test plan + harness (plan-driven)
- `docs/test_plan.md` = living checklist (IDs TV/TG/TI/TS/TE/TR/TF) that DRIVES growth.
- `tests/test_citecheck.py` = **20 offline pytest** (mock citator, no network); `.github/workflows/ci.yml` runs on push/PR. Covers 4 gates (pass/defect/fail-closed), the **confidence-reported-not-gated invariant (TR-01 regression for the τ fix)**, TTL/no-token fail-closed, LW116 no-leak + bare-query, eyecite extraction + annotation dedup, **TS-03 fuzz** (never crash, default fail-closed; added a try/except eyecite guard), **TE-03 regex-fallback parity**.
- Backlog (in the plan): TG-3c, TF-01 real citator, TF-02 live CourtListener contract test, TF-03 state/local, TF-04 LW110 UPL classifier, TF-05 LW117 label, TF-06 future verticals.

## 7. Docs + reference
- README "Setup & live verification" (CourtListener token how-to). `docs/legal_sources.md` v0 (federal/state/local × cases/statutes/regs × accessibility tiers A-D; the citator gap that bounds gate 2).

## 8. Governance / portfolio updates (PostWach-resident)
- `project-registry.md`: Lawsun Tier-1 entry; V3 hive count **10 → 11**.
- `capability-index.md`: 3 skills, 4 agents, 6 cross-project reuse rows, review-log entry.
- Memory: `project_lawsun.md` + MEMORY.md pointer.

## 9. Ownership decision
- **The test harness belongs to Lawsun** (ownership follows the capability) and already lives in the Lawsun repo. PostWach holds only the CTO governance/quality records + scorecard. No SEAD handoff ([R108] is PostWach-scoped; this is a research-tool test suite inside another hive).

## 10. Commits (DocWach/Lawsun, branch main)
`6210dd6` scaffold → `982845b` citecheck report-confidence + eyecite/CourtListener → `539bcc3` token note + legal_sources → `2eeb245` test plan + harness + CI → `e085204` fuzz + parity.

## 11. Open / next
- Work the TF backlog (real citator, live CourtListener contract test, UPL classifier, future verticals) — each gated by its plan row.
- CourtListener token for live runs; expand `legal_sources.md` to per-state matrix.
- Review Brad's `bmpwach-lab` legal assistant (90 repos scanned 2026-06-29, none named legal/law — need a repo name/account).
