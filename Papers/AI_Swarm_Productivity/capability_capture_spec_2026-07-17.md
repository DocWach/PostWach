# Capability-Capture Daemon — Spec / Design Note (2026-07-17)

Purpose: scope the going-forward, machine-sourced capture of **harness capability utilization** per session,
so scorecard section D2b (Capability Utilization, schema v1.3) is populated by an objective daemon rather than
human recall. Written so the build session starts with a plan, not a blank page.

Author: PostWach (Opus 4.8, claude-opus-4-8[1m]), principal-directed, 2026-07-17.
**R016: DESIGN NOTE (a) — nothing built yet.** Promote to (b) after the daemon runs on a real transcript and
emits a verified `capability_engagement` block.

Owner: folded into the **cost-instrumentation thread** (same file `cost-capture.mjs`, same Alpha Empress
governance handoff). Sibling of `cost_instrumentation_spec_2026-07-16.md`.

## Why this exists (the design path that produced it)

The literal ask ("update the scorecard to reflect skills, agents, swarms, tools used") was stress-tested with
an RBW adversarial review (`claim-holds-with-caveat`) and then reformulated via GQM (`problem-framer`). Both
converged on one architectural move: **stop asking a human to attest capability use; extract it from the
transcript with a daemon.** That single move dissolves the RBW defeaters that killed the human-filled
"all-required" design:

| RBW defeater (human-filled design) | Resolved by the daemon because |
|---|---|
| Fabrication pressure on fields unobservable at fill-time | Daemon reads facts from the transcript/logs; unobservable => explicit GAP, never a guess |
| Slash-command-IS-a-skill double-count | De-dup by **which harness tool fired** (deterministic) |
| New fields duplicate `agents_spawned`/`tool_calls`/`swarm_topology` and drift | Daemon writes the **existing authoritative fields**; D2b adds only presence/identity views |
| "Ambient" always-on infra is zero-variance | Measure **engagement** (varies per session), not "installed" (portfolio-level only) |
| No consumer => all-required is pure burden | Human fill shrinks to ~5 subjective flags; the rest is free |

## Grounding facts (verified against source)

- **Precedent to extend:** `.claude/helpers/cost-capture.mjs` (B1) is a working `SessionEnd` hook. Mechanics to
  reuse verbatim:
  - stdin carries `transcript_path` + `session_id` (`cost-capture.mjs:107-111`); falls back to newest
    non-`agent-` `.jsonl` in the project transcript dir (`:89-97`).
  - streams the transcript line-by-line as JSONL, `JSON.parse` per line (`:56-58`).
  - **event-id de-dup** so repeated re-injection of a result does not over-count ~10x: workflow notifications
    keyed by `<task-id>`, Agent results by `agentId`; assistant-authored lines skipped (`:52-74`).
  - idempotent (skips a session id already stamped, `:132-135`); **never throws, always `exit 0`** (`:162`).
- **Authoritative fields the daemon WRITES (never duplicate elsewhere):** `ai_efficiency.agents_spawned`,
  `ai_efficiency.tool_calls`, `ai_efficiency.swarm_topology`, `ai_efficiency.tokens_*`, `ai_efficiency.cost.*`.
  Consumer `analyze_scorecards.py` derives `agent_utilization` from `ai_efficiency.agents_spawned` +
  `process.agent_failures` (`:194`) and CSV-exports `swarm_topology`, `tokens_input/output`, `total_cost_usd`
  (`:510-515`). Drift in these silently corrupts the one derived metric — so the daemon is the single writer.
- **`subagent_tokens` is a PROXY, not verified output** (~16x; see `research_token_ledger.md`). Any dose metric
  sourced from it inherits that caveat.

## Metric catalog (what the daemon emits)

TYPE = presence | count | dose. CHANNEL = transcript (in the JSONL) | hooklog (only an external observer knows)
| config (settings/.mcp.json) | human (subjective, NOT daemon). Reconciliation names the authoritative field.

| # | Category | Metric | TYPE | CHANNEL | Reconciliation / note |
|---|----------|--------|------|---------|-----------------------|
| M1 | Subagents | `agents_spawned` | count | transcript | **authoritative D2 field** — daemon writes it |
| M2 | Subagents | `agent_failures` | count | transcript | **authoritative D4 field** (`process.agent_failures`) |
| M3 | Subagents | `subagent_types` | presence+count | transcript | new D2b; tally `Task` `subagent_type`; does NOT restate M1 |
| M4 | Coordination | `coordination_style` | presence | transcript | new D2 field; objective discriminator (below); distinct from `swarm_topology` |
| M5 | Skills | `skills_engaged` / `skill_invocation_count` | presence/count | transcript | new D2b; scan `Skill` tool calls |
| M6 | Skills | `skills_used` (names) | presence | transcript | daemon becomes source of truth; human list is fallback |
| M7 | Tools | `tool_calls` | count | transcript | **authoritative D2 field** — daemon fills it, stop guessing |
| M8 | MCP/plugins | `plugins_engaged` (identity) + `mcp_tool_call_count` | presence/count | transcript | detect `mcp__<server>__*` prefixes; **subset/partition of M7, never additive** |
| M9 | Workflows | `workflow_invoked` | presence | transcript | detect `Workflow` / `workflow_execute`; feeds M4 |
| M10 | Memory | `memory_engaged` + `stores_written` | presence/count | transcript | detect `memory_store`/`memory_search`/auto-memory writes (INVOKED, per RBW re-bucket) |
| M11 | Hooks | `hooks_fired` | presence | **hooklog** | NOT in transcript (a SessionEnd hook cannot self-report from inside); each hook appends `{hook_id, session_id, ts}` to a shared `hook-firing.log`; daemon folds it in |
| M12 | Config | `capabilities_installed` | presence | config | near-zero-variance => **portfolio-level once, NOT per-session** |

**De-dup rule (deterministic):** classify each tool-use block by the tool that fired — `Skill`→skill,
`Task`→subagent, `Workflow`→workflow, `mcp__claude-flow__swarm_init`/`hive-mind_*`→swarm, other `mcp__*`→plugin,
`Read/Edit/Bash/Grep/...`→routine. A slash command that is also a skill is counted once, as a skill.
M8 ⊆ M7 (report as a breakdown, never a sum).

## coordination_style discriminator (resolves workflow-vs-swarm objectively)

Keyed on which orchestration tool actually fired in the transcript — a machine fact, never an attestation:

| Observed | `coordination_style` |
|---|---|
| `Workflow` tool / `workflow_execute` | `workflow` |
| `mcp__claude-flow__swarm_init` or any `hive-mind_*` | `swarm` |
| both | `hybrid` |
| `Task`/Agent spawns, no workflow/swarm-init | `agent-fanout` |
| no orchestration tool at all | `single-agent` |
| transcript unreadable / not captured | `unknown` (ONLY here; never a stand-in for "none") |

Distinct from `swarm_topology` (hierarchical/mesh/star — the *shape* when a swarm initialized). Style = what
orchestrated the session; topology = how the swarm was wired.

## Build outline (extend cost-capture.mjs; do NOT fork a new hook)

1. In `parseTranscript`, alongside token accounting, tally tool-use blocks by tool name into a
   `caps = {skills:{}, subagent_types:{}, mcp:{}, workflow:false, swarm:false, memory_writes:0, tool_calls:0, ...}`
   accumulator, applying the same event-id de-dup discipline.
2. Derive `coordination_style` from `caps.workflow`/`caps.swarm`/subagent presence.
3. Emit a compact `capability_engagement` YAML block and write the **authoritative** fields
   (`agents_spawned`, `tool_calls`, `swarm_topology`) plus the new presence fields into that session's scorecard
   (locate by session id/date), idempotently (skip if already stamped), never throwing, `exit 0`.
4. Fold `hook-firing.log` in for M11. Read config (M12) once at portfolio level, not per session.
5. Anything not observable => explicit `not_captured` / GAP marker in the block; never a fabricated value.
6. Keep the manual mode (`node cost-capture.mjs <file>`) so a transcript can be parsed to JSON without append —
   the verification path before wiring it to SessionEnd.

## Constraints / risks

- **Quiescence required for the build.** `cost-capture.mjs` is a shared `SessionEnd` hook under a OneDrive-synced
  `.claude/`. Editing it while other sessions run risks a concurrent SessionEnd firing against a half-written
  file, and the concurrent-`.claude`-edit hazard behind INCIDENT-001. **Implement only when no other sessions are
  live; commit promptly.** (This is why the template ships first and the daemon waits.)
- Idempotency + de-dup are load-bearing (the cost hook learned this the hard way); reuse them, do not reinvent.
- `subagent_tokens` proxy caveat carries into any dose metric.
- The moderation questions (does capability-X-use co-vary with quality?) are **not answerable at current N** —
  the daemon's job now is cheap, objective covariate accumulation, not reporting an effect.

## Governance / skills (R020, cross-hive)

- PostWach BUILDS; **Alpha Empress REGISTERS** the v1.3 template + the capability-capture increment for cross-hive
  consistency (same handoff as the B1 cost hook; see `docs/governance_handoff_cost_instrumentation_2026-07-16.md`).
- Skills to use on the build: `hooks-automation` (hook wiring), `update-config` (settings.json if a new hook-log
  path is needed), `red-blue-white` on the final field-set before it ships to co-hives.

## Deliverables checklist (build session)
- [ ] `parseTranscript` extended with the `caps` accumulator + de-dup
- [ ] `coordination_style` derivation
- [ ] `capability_engagement` block written to the scorecard (idempotent, authoritative fields single-sourced)
- [ ] `hook-firing.log` convention + fold-in for M11
- [ ] portfolio-level `capabilities_installed` read (M12)
- [ ] verified on one real transcript via manual mode (R016 -> (b))
- [ ] Alpha Empress governance-registration note
