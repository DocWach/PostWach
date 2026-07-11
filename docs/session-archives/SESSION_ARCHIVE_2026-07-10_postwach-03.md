# Session Archive — 2026-07-10 postwach-03

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m] (main-loop; no subagents, no swarm).
**Focus:** Update the DocWach/Disruption-Swarm-Setup onboarding repo: simplify to match reality, make Claude-subscription auth primary, and add cross-platform (macOS/Windows) install paths.
> PROVENANCE: run by Claude (Anthropic, Opus 4.8, claude-opus-4-8[1m], Claude Code main-loop) at Paul Wach's direction. Repo cloned locally; docs edited; live `claude-flow` CLI help audited for command validity; committed and pushed to `main`. No agents spawned; no memory-store writes.

## Headline
Fact-corrected and cross-platform-ized the Disruption-Swarm-Setup team onboarding docs. Committed `7b72720` and pushed to `origin/main` (11 files, +283/-49). Scope was set by three up-front decisions from the principal: **fix facts only** (no MCP-first restructure), **subscription-primary auth**, and **full macOS/Windows parallel coverage + a new mac-gotchas doc**.

## What changed (11 files)
- **Facts (all guides):** version `v3.1.0-alpha.3` / `v3.1.x` -> `v3.14` (verified against live install: claude-flow 3.14.4, Claude Code 2.1.170); deprecated `hooks session-start` -> `hooks session-restore`; dropped unverified `session-restore --latest`; removed 2 dead links to a nonexistent `docs/claude-flow-reference.md`; linked the existing-but-unlinked FAQ; stale "March 6 meeting" -> "your onboarding session."
- **Auth (subscription-primary):** every auth step now leads with `claude` -> `/login` -> Claude account; API key demoted to a documented fallback for API billing. `cost-guardrails.md` reframed with a new "Managing Subscription Usage" section (flat fee + usage limits) ahead of the per-token tables.
- **Cross-platform:** side-by-side macOS/Windows in README quick-install and the pre-meeting checklist (Node, PATH, login, env vars); new `docs/mac-gotchas.md` (7 sections mirroring windows-gotchas: PATH/zsh, Homebrew vs Intel, EACCES/no-sudo, iCloud spaces, Gatekeeper, Apple Silicon). Both gotchas docs cross-link.

## Method note (why this was not a naive edit pass)
Before editing, audited the actual v3.14 CLI surface (`claude-flow <cmd> --help`) rather than trusting the alpha docs. That both **caught real breakage** (deprecated `session-start`, dead reference link) and **prevented needless churn**: the central `swarm init --topology/--max-agents/--strategy` and `memory store --key/--value/--namespace` commands are still valid, so they were left alone. Post-edit grep sweep confirmed zero remaining stale patterns.

## Files
- Deliverable (working clone): `_workspace/Disruption-Swarm-Setup/` — README.md, docs/{pre-meeting-checklist, claude-flow-getting-started, claude-flow-cheatsheet, claude-flow-user-manual, cost-guardrails, faq, graduated-complexity, permissions-and-safety, windows-gotchas}.md modified; docs/mac-gotchas.md created.
- Pushed: `DocWach/Disruption-Swarm-Setup` commit `7b72720` on `main`.
- Records: this archive; scorecard `2026-07-10-postwach-03.yaml`.

## Still open (deferred, not blocking)
- **MCP-registration step:** the guides still never tell a new user to register the claude-flow MCP server with Claude Code (the thing that makes "just talk to Claude" work). Flagged to the principal; held off because it is a content addition, not a fact fix. Add on request.
- Optional global em-dash purge of the prior author's untouched lines (my added text already avoids them per preference).
- If a separate local checkout of the repo exists elsewhere, `git pull` it to sync.

## Hygiene
Pushed one commit to `main` (principal-approved delivery method). No `Co-Authored-By: claude-flow` trailer (per standing preference); author/committer `Paul Wach <pfwach@gmail.com>`. No agents spawned; no swarm started (ruflo warmed to v3.14.4 for MCP/agent-list status only, confirmed 0 agents, then idle). No orphaned agents to terminate. No memory-store writes, so no R018 store attribution beyond this archive's provenance line. Working clone left in place under `_workspace/`.
