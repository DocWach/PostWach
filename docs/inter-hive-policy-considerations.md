# Inter-Hive Policy Considerations

**Status:** Parking lot for the future inter-hive policy / architecture session.
**Last updated:** 2026-05-21
**Owner:** PostWach (CTO)

This document collects cross-cutting policy and governance topics that span multiple hives and should be addressed when PostWach conducts an inter-hive policy / architecture review session.

---

## Topic 1: Swarm-first default for bulk work

### Problem statement

Observed during TRAK build (2026-04-12): the main Claude session did ~12 of 14 substantial work items directly. Sub-agents spawned to parallelize the work repeatedly returned plans instead of executing. Result: high token burn, serial execution, and context-window growth that would be better served by scoped agents.

The user raised this as a governance concern: we should default to swarms and specialized agents for bulk work rather than having the main LLM do everything.

### Proposed rule (draft R017)

**R017: Swarm-first for bulk work.** Any task that meets ANY of the following should be delegated to a specialized agent:

- Creating or rewriting a file with more than approximately 100 LOC
- Writing a new test suite covering more than 3 cases
- Researching or exploring more than 2 locations in the codebase
- Running an independent review or audit
- Any task that can run in parallel with other independent work

**Carve-outs for main session:**

- Orchestration and coordination (deciding who does what)
- User interaction (questions, debates, summaries)
- Small edits (under approximately 50 LOC, fewer than 3 files)
- Integration across agent outputs (applying results, resolving conflicts)
- Architectural judgment calls where accumulated session context is load-bearing
- Session archives and meta-work

**Agent selection guidance:**

- `coder` for implementation work
- `tester` for test suite generation
- `reviewer` for code review
- `researcher` for exploration
- `Explore` for quick searches
- `Plan` for implementation design
- `general-purpose` only when no specialized fit exists

### Blocker: sub-agent plan-mode inheritance bug

During 2026-04-12, 7+ sub-agents spawned with explicit "execute directly, do not enter plan mode" instructions and `bypassPermissions` mode. All returned plans rather than executing. Root cause appears to be that sub-agents inherit plan-mode state from the main session, overriding spawn-time instructions.

This is a reliability problem that policy cannot fix. R017 adoption should be blocked on either:

- A platform fix to sub-agent plan-mode inheritance, or
- A reliable workaround (for example, spawning agents at session start before plan mode is entered, or using `SendMessage` to resume agents with explicit exit-plan directives)

### Open questions for the inter-hive session

1. Who owns the plan-mode inheritance fix: claude-flow team, or a per-prompt workaround?
2. Should we track tokens spent by main vs. swarm in session archives as a metric?
3. Are specialized agents like `coder` running on a cheaper model by default? If not, cost savings are smaller than projected.
4. When an agent fails or returns a plan, what is the standard recovery path?
5. Should R017 be global or hive-specific?

### Phased rollout proposal

- **Phase A (now):** Track token spend by main vs. swarm in session archives. Two sessions of data.
- **Phase B (after plan-mode fix):** Pilot R017 in one hive (PostWach). Measure token/time/rework deltas.
- **Phase C (after pilot):** Promote to global rule if metrics improve; otherwise iterate.

---

## Topic 2: Cross-hive ticket format and distribution convention

### Problem statement

Raised by GI-JOE in POSTWACH-GIJOE-001 (the closure request ticket for the TRAK ontology, 2026-04-12):

> This is GI-JOE's first outbound ticket to PostWach. PostWach's existing action item to define a global cross-hive sharing policy is relevant here. For now, this ticket mirrors the format PostWach used for the TRAK Ontology Handoff (parent ticket + work breakdown), deposited in a new `01 PostWach/tickets/` directory that mirrors GI-JOE's convention.

GI-JOE suggested folding the following into the global policy when drafted:

- Directory convention (recipient's hive vs. shared location)
- Ticket ID scheme for outbound tickets
- Expected turnaround SLA for infrastructure reviews
- Whether ratification of spec divergences requires a formal spec version bump or can be tracked in amendment blocks (current pattern uses amendment blocks)

### Current observed patterns

- **SEAD handoff pattern:** PostWach to SEAD tickets live at `02 Hives/09 SEAD/tickets/` with ID format `SEAD-{project}-NNN`. Examples: SEAD-PD-001 (PD Workbench handoff), SEAD-TRAK-001 (TRAK Workbench handoff).
- **GI-JOE handoff pattern (PostWach -> GI-JOE):** PostWach created `02 Hives/05 GI-JOE/tickets/` with parent ticket + work breakdown. IDs used: GI-JOE-TRAK-001 with sub-tasks 001.1 through 001.8.
- **GI-JOE reverse ticket (GI-JOE -> PostWach):** GI-JOE created `01 PostWach/tickets/` with ID POSTWACH-GIJOE-001.

### Questions to resolve

1. Is the ticket directory on the recipient's side, the sender's side, or a shared location?
2. Should ticket IDs encode sender-receiver-project-seq, or sender-project-seq, or something else?
3. Is there an SLA scheme per ticket priority (Critical / High / Medium / Low)?
4. Amendment block vs version bump for in-flight spec divergences: what triggers which?

---

## Topic 3: POSTWACH-GIJOE-001 Item 2 (ontology-gate.sh infrastructure refactor)

### Status

Deferred on 2026-04-12 from the NNSA delivery focus. Tracked as task #13 in the TRAK session.

### Summary

GI-JOE refactored `ontology-gate.sh` beyond the strict additive scope in sub-task 001.8. They parameterized the full-mode Python block around an `ONTOLOGY_SET` environment variable and wrapped it in a bash for-loop that accumulates results across registered ontology sets. They also added a mode-only invocation path (`bash ontology-gate.sh full` with no file argument).

Portfolio validation flows through the new parameterized mechanism with no behavior change (20/20 CQs pass).

### Why this belongs in the inter-hive session

- `ontology-gate.sh` is GI-JOE infrastructure consumed by any hive validating ontologies
- Other hives (MACQ, SysMLv2, SEAD) may want to adopt the multi-ontology-set pattern; they should not do so until PostWach confirms the design
- GI-JOE implemented this because sub-task 001.8's shell-level test required the mode-only invocation and the pre-existing script did not support it

### Alternatives considered by GI-JOE

- **Minimal additive patch:** add a single `if [[ $FILE_PATH == *trak* ]]` branch to the existing full-mode logic. Simpler but duplicates code for every additional ontology set.
- **Current implementation:** `ONTOLOGY_SET` env var dispatch + bash for-loop. Cleaner for two-plus ontology sets; required design work to define the env var contract.

### Action for the inter-hive session

Review commit `e6e0ca5` in `02 Hives/05 GI-JOE` and either confirm the dispatch design for portfolio-wide adoption or direct a rollback to the minimal-additive alternative.

---

## Topic 4: Shared infrastructure ownership and change control

### Problem

Multiple hives consume shared infrastructure (ontology-gate.sh, ontology-validation skill, portfolio-governance ontology, Chainguard image guidance, etc.). When one hive extends the infrastructure, the change can affect other hives without their awareness.

### Questions

1. Who is the infrastructure owner of record for each shared asset?
2. What change-control process applies to shared infrastructure (PR with cross-hive review, RFC, unilateral with notification, etc.)?
3. Is there a "shared infrastructure" directory separate from any single hive's namespace?
4. How do backwards-incompatible changes get announced and migrated?

---

## Topic 5: Token and time accounting in session archives

### Problem

We do not currently measure where tokens go (main session vs. swarm vs. reads vs. writes). Without that data, decisions about R017 (swarm-first) and similar governance are uncalibrated.

### Proposal

Add to the scorecard template (`Papers/AI_Swarm_Productivity/scorecard-template.yaml`) new fields:

- `tokens_by_role`: main-session / swarm-agents / tool-overhead
- `wall_clock_parallel_vs_serial`: time if perfectly parallel vs. time actually taken
- `rework_rate`: agent outputs that had to be redone in main session

### Connection to existing research

This would feed directly into the AI Swarm Productivity research line (`Papers/AI_Swarm_Productivity/`). Scorecards are already collected per session. Extending the schema is low-cost and produces the data needed for R017 calibration.

---

## Topic 6: Local review vs Claude-backed sub-agents

### Clarification of a common confusion

Sub-agents spawned via the `Agent` tool (all types: `Explore`, `Plan`, `coder`, `reviewer`, `tester`, specialized researchers) run on Claude's cloud. They share billing and underlying model capacity with the main session. "Spawning an agent" and "sending work to Claude" are the same operation from a token-consumption standpoint. Topic 1 (swarm-first default R017) saves tokens only to the extent that specialized agents route to cheaper models within the Claude ecosystem (Haiku vs Opus). It does not make work "local."

### What actually runs locally

Three paths consume zero Claude tokens at runtime:

1. **Deterministic tooling via Bash.** pytest, ruff, pylint, mypy, pip-audit, bandit, semgrep. Rule-based, not LLM-based. TRAK's CI already runs pytest + pip-audit in this way (SEAD-TRAK-001 D2).

2. **Local LLM via Ollama (or equivalent).** The TRAK tool itself includes `lib/llm_provider.py` with an `OllamaProvider` that hits `OLLAMA_HOST/api/generate`. That is the tool's runtime LLM path for practitioners, not the main-session review path.

3. **Scripted review harness.** A script can combine deterministic checks with an Ollama-backed LLM review over uncommitted diffs. The script executes locally and consumes zero Claude tokens at run time. Writing the script consumes Claude tokens once; every subsequent run is free.

### Proposed local review harness

Proposal: add `scripts/local_review.py` to TRAK (and similar hives over time) with:

- Hard gates: `pytest`, `py_compile`, `pip-audit`, optionally `ruff` or similar linter
- Optional LLM-backed review: read uncommitted diff via `git diff`, send to Ollama with a reviewer prompt, append findings to a Markdown summary
- Output: `docs/local_review_{timestamp}.md` (ignored by git by default)
- Exit code reflects hard-gate failures so the script can be wired to a pre-commit hook

### Questions for the inter-hive session

1. Should every hive adopt a `scripts/local_review.py` pattern, or should the review harness be shared infrastructure (like `ontology-gate.sh`)?
2. Which deterministic gates are mandatory for all hives (pytest + pip-audit) vs recommended (ruff, mypy)?
3. Is there an organization-approved local LLM (Ollama model) for rationale/prose review, or is that researcher choice?
4. How does the local review harness interact with R017 (swarm-first)? Proposed answer: R017 governs Claude-backed work; local review is a separate layer that complements both main-session work and Claude-backed sub-agents.

### Connection to Topic 1

Topic 1 (swarm-first default) and Topic 6 (local review) answer different questions:

- Topic 1: within Claude-backed work, how do we prefer sub-agents over the main session?
- Topic 6: for which work should we not consult Claude at all?

Both should be codified. A reasonable hierarchy: local deterministic gates first (always), then local LLM review second (when configured), then Claude sub-agents third (R017 default), then main session fourth (for judgment/coordination).

---

## Topic 7: External-tool adoption and shared capability hosting

### Problem statement

PostWach periodically adopts external (open-source) tools that become load-bearing for research output. Two instances now exist with the same shape: doc-merge (pandoc + docx report builder, deferred 2026-04-12) and PaperBanana (academic figure generation, demonstrated 2026-05-21). Each raises the same questions: do we fork and own it, where does the code live, and how do other hives consume it without N-times duplication?

### Why it belongs here

PaperBanana currently lives only in PostWach (`.mcp.json` block + 3 skills + capability-index entry). The moment MACQ (NNSA reports), GI-JOE (ontology papers), or the INSIGHT article want figures, the naive path copies the config into each hive. That is the same N-times-N duplication the auto-memory-hook fix (8 commits) and the MCP-registration fix (9 commits) already demonstrated, and which the HOS portability thread exists to eliminate.

### Recommendation (consistent with doc-merge precedent and HOS sub-decisions)

- **Ownership:** PostWach (CTO) curates capability quality; Alpha Empress (COO) governs; consuming hives are clients.
- **Hosting:** standalone portable repo under `DocWach/*`, repo-tracked (HOS portability hard constraint), never user-home-only.
- **Sharing:** one thin MCP server over the canonical install (H1-hybrid), no per-hive copies.
- **Taxonomy:** Output / shared service, not a Hive.

### Questions to resolve

1. Is there a single "shared capability layer" in HOS, distinct from the shared-governance layer? PaperBanana + doc-merge are the evidence for it.
2. Naming and repo location for owned forks (`DocWach/paper-figures`? `DocWach/doc-merge`?).
3. Upstream-drift monitoring: an owned fork needs a staleness sensor (is our fork behind upstream?); folds into the capability-freshness / homeostasis thread.
4. Distinguish this (external OSS adoption) from Topic 4 (internal shared-infra change control); they share a hosting question but differ in origin.

### Related

- PaperBanana ownership analysis: PostWach memory `project_paperbanana_ownership.md`; tool state `project_paperbanana.md`; capability-index entry. Decision process captured in the `cross-project-reviewer` skill (External Tool Adoption Protocol).
- doc-merge: `project_shared_doc_tooling.md`.
- HOS: `project_hos_governance_composition.md` (portability constraint), `project_hos_capability_freshness.md`.

---

## Related references

- `02 Hives/05 GI-JOE/tickets/TRAK_Ontology_Handoff_2026-04-12.md` (original handoff with amendments)
- `02 Hives/05 GI-JOE/tickets/TRAK_Ontology_Work_Breakdown_2026-04-12.md` (sub-task decomposition with amendments)
- `01 PostWach/tickets/TRAK_Ontology_Closure_Request_2026-04-12.md` (POSTWACH-GIJOE-001 from GI-JOE)
- `02 Hives/09 SEAD/tickets/TRAK_Workbench_SEAD_Handoff_2026-04-12.md` (SEAD-TRAK-001 pattern)
- `02 Hives/09 SEAD/tickets/PD_Workbench_SEAD_Handoff_2026-04-10.md` (sibling pattern)
- `01 PostWach/docs/session-archives/SESSION_ARCHIVE_2026-04-12_postwach-01.md` (full-day archive with swarm-use evidence)
- `Papers/AI_Swarm_Productivity/` (productivity research line; scorecards)
