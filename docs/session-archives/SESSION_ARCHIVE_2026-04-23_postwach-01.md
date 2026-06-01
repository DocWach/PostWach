# Session Archive — 2026-04-23 postwach-01

**Hive:** PostWach
**Scope:** Warm up ruflo, diagnose the Auto Memory Bridge "Package: Not found" banner, design a permanent MCP-based replacement, and propagate across 7 Tier-1 V3 hives with commits and pushes.
**Platform:** Ruflo v3.5.80, claude-opus-4-7 (1M context), Windows 11 Home
**Outcome:** Auto-memory bridge live across all 8 Tier-1 hives (was silent no-op for ~62 days). Option A-trim MCP-only design implemented. Two root-cause bugs fixed: (1) missing `@claude-flow/memory` package in claude-flow v3.5.80, (2) `process.argv[2]` dispatch bug that routed `node -e "..." import/sync` to the default `status` branch. 8 commits pushed to 8 repos. HOS leakage inventory gains Motivating Example #2. 10 orphaned idle agents cleaned (5 PostWach + 5 SysMLv2).

---

## 1. Entry state

User request: "warm up ruflo". Pinged MCP surface in parallel (`mcp_status`, `system_status`, `swarm_status`, `memory_stats`, `agent_list`). Bridge live (pid 19716, stdio, v3.0.0-alpha.102). `claude-flow doctor` reported 10 pass / 4 benign warnings (stale daemon PID, no API keys, no local TypeScript, no agentic-flow).

Session-start hook banner flagged `Auto Memory Bridge / Package: Not found`. User asked to investigate. Spawned `test-long-runner` agent for deep diagnostic (~2min). Agent found two overlapping bugs and a downstream leakage pattern.

---

## 2. Method

Direct tool use with one test-long-runner agent for initial diagnostic. Staged rollout with user confirmation between every phase (per "discuss before executing" rule).

1. **Diagnostic (agent).** `test-long-runner` probed MCP health, read `.claude/helpers/{auto-memory-hook.mjs,hook-handler.cjs,intelligence.cjs}` and `.claude/settings.json`, walked `npm` package tree. Root cause: `@claude-flow/memory` absent in claude-flow v3.5.80 (only `cli` and `shared` ship in `v3/@claude-flow/`). Hook silently no-ops via `catch(...non-critical)`. Also confirmed [R017]/[R106] compliance clean for claude-flow (`npx` remained only on ruv-swarm / flow-nexus, out of scope).
2. **Cosmetic fix.** `auto-memory-hook.mjs:329` banner `"Not found"` → `"Not installed (fallback active)"`.
3. **Option framing.** Pushed back on "vendor the package" as false-permanent. Laid out three options — A (MCP-only), B (fallback-only), C (vendoring) — with tradeoffs. User chose A, asked about idle-agent hygiene.
4. **Idle-agent cleanup.** Terminated 5 orphan agents from 2026-03-05 (coordinator, 2 researchers, 2 analysts). Clarified these were DB rows, not live processes. Session termination kills processes, not AgentDB state — data-hygiene gap, not resource leak.
5. **Option A caveat.** Discovered MCP surface exposes `memory_import_claude` (import direction) but NOT reverse sync / `curateIndex` (AgentDB → MEMORY.md PageRank reorder). Reframed as Option A-trim: import only, explicit no-op for sync. User approved.
6. **Helper implementation (PostWach pilot).**
   - `.claude/helpers/mcp-client.mjs` (new, 132 lines): minimal stdio JSON-RPC MCP client, spawns `claude-flow mcp start` via `cmd.exe /c` on Windows to avoid DEP0190.
   - `.claude/helpers/auto-memory-hook.mjs` (rewrite, 364→158 lines): Option A-trim. `doImport` calls `memory_import_claude` with `allProjects: true`. `doSync` is logged no-op. `doStatus` pulls `memory_bridge_status`. Argv dispatch accepts command at any position.
   - `.claude/helpers/terminate-idle-agents.mjs` (new, 46 lines): calls `agent_list`, filters `status==='idle' && taskCount===0`, `Promise.allSettled` parallel terminate.
   - `.claude/settings.json`: SessionStart import timeout 6000→20000, SessionEnd sync timeout 8000→5000, add terminate-idle hook with 30000 timeout.
7. **Pilot validation.** End-to-end test succeeded: bridge flipped from `not-synced` → `connected`, AgentDB populated with 20 entries (up from 10 stale Feb-2026 entries), 144 fragments imported from 53 MEMORY.md files across 7 projects.
8. **Surprise argv bug.** During pilot testing, discovered `node -e SCRIPT ARG` puts ARG at `argv[1]`, not `argv[2]`. The original hook's `process.argv[2]` was ALWAYS undefined, defaulting to `status`. Root reason the bridge looked dead — missing-package bug just hid the argv bug. Both fixed by new `argv.slice(1).find((a) => VALID.has(a))` dispatch.
9. **Hive-of-hives discovery.** Before committing PostWach, asked: is this a hive-of-hives issue? Portfolio scan found **11 copies** of `auto-memory-hook.mjs` (MD5 `dce695d...`, all byte-identical except PostWach). Fort Wachs escaped — no `.claude/helpers/` at all (newer hive, different template). Framed as Option X/Y/Z and surfaced link to HOS portability thread.
10. **Option Z selection.** User chose: fix 7 Tier-1 hives + log as HOS evidence. Deferred BP Marketing, Claude_code_test_setup, Roadmapping Hive.
11. **HOS evidence logged.** Appended "Motivating Example #2 (2026-04-23) — auto-memory hook" to `memory/project_hos_governance_composition.md` with per-hive table, Shape 1/2 distinction, parallel [R106] `npx` violation as additional evidence.
12. **Propagation.** Read all 7 hives' existing files. Discovered two distinct settings.json shapes:
    - **Shape 1** (simple SessionStart+SessionEnd, no splice): PostWach, MACQ, GI-JOE, COSYSMO, SysMLv2, PLM
    - **Shape 2** (hook-handler.cjs-based, SessionStart+Stop, `process.argv.splice(1,0,f)` workaround): Alpha Empress, SEAD
    Initially misassigned SEAD and GI-JOE — caught on first edit pass (4 edits failed with "string not found"), re-read, corrected.
13. **Commit+push loop.** User proposed 8 parallel test-agents; pushed back on concurrency risk with shared sql.js AgentDB, substituted sequential bash sweep. All 8 passed (8/8). Sequential commit+push: explicit 4-file staging, HEREDOC commit message with `Co-Authored-By: claude-flow <ruv@ruv.net>`, `git push origin HEAD` per repo. SysMLv2 push guard verified before push — `branch.main.pushRemote=origin` and `remote.incose-fuse.push=batch1→main`.
14. **Side benefit.** SysMLv2 test run caught 5 orphaned idle agents since 2026-03-05, cleaned automatically by new hook. First real-world exercise of the cleanup behavior.

---

## 3. Deliverables

### New files (3 files × 8 hives = 24 new files)

- `.claude/helpers/mcp-client.mjs` — stdio JSON-RPC MCP client (PostWach + 7 hives)
- `.claude/helpers/terminate-idle-agents.mjs` — SessionEnd agent cleanup (PostWach + 7 hives)
- In Alpha Empress only: `.claude/settings.json` was entirely untracked prior (committed as new file)

### Modified files

- 8 × `.claude/helpers/auto-memory-hook.mjs` — rewritten MCP-only Option A-trim
- 8 × `.claude/settings.json` — timeout bumps + terminate-idle hook wiring
- `memory/project_hos_governance_composition.md` — appended Motivating Example #2 section with per-hive Shape 1/2 table and [R106] parallel-issue note
- `docs/session-archives/SESSION_ARCHIVE_2026-04-23_postwach-01.md` (this file)
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-04-23-postwach-01.yaml`

### Code/repo changes — 8 commits, all pushed to origin

| Hive | Repo | Branch | Commit |
|---|---|---|---|
| PostWach | DocWach/PostWach | main | `b2b5450` |
| Alpha Empress | DocWach/Alpha_Empress | main | `ca73ffb` |
| MACQ | DocWach/MACQ | main | `73d7bf0` |
| GI-JOE | DocWach/JOE-G | master | `5307fb8` |
| COSYSMO | DocWach/COSYSMO-Hive | master | `ce6c69f` |
| SysMLv2 | DocWach/SysMLv2-Hive | main | `637c913` |
| PLM | DocWach/PLMr | main | `5d51916` |
| SEAD | DocWach/SEAD | main | `74df8fa` |

---

## 4. Open threads touched

- **HOS + Governance Composition (thread #2 open for planning):** gained Motivating Example #2 with concrete metrics — 8 commits across 8 repos for a 4-file logical change, plus parallel npx-hook leakage as additional duplication-pattern evidence. N×N commit pattern formally logged twice now (2026-04-22 MCP fix = 9 commits; 2026-04-23 hook fix = 8 commits).
- **Hive-of-Hives / Skill catalog governance:** `.claude/helpers/*` is the same duplication disease as skill catalog but even worse — byte-identical copies with no single canonical source, no template mechanism. Fort Wachs escaped because its template differed.
- **Paper status discipline:** N/A this session.

---

## 5. Parallel issue explicitly scoped out

Every Tier-1 hive's `settings.json` still uses `npx @claude-flow/cli@latest ...` (or `npx claude-flow@alpha ...` in PLM) for PreToolUse, PostToolUse, UserPromptSubmit, Notification, statusLine hooks. Same class of Windows-npx brittleness as the 2026-04-22 MCP fix. Violates [R106] (shell usage MUST use globally installed `claude-flow`). Logged as additional HOS evidence, not fixed this pass.

---

## 6. Tier-2 / unregistered hives — deferred state

Still carry the broken hook (argv bug + missing package):
- BP Marketing (Tier 2)
- Claude_code_test_setup (Tier 2)
- Roadmapping Hive (not in project-registry)

Impact is silent no-op, which has been the state for ~62 days. User chose Option Z scope explicitly.

---

## 7. Next session entry hints

- **Auto-memory is now live.** `memory_search_unified` with 144 fragments × embeddings across 7 projects should produce meaningful semantic results; worth exercising in future coordination-heavy sessions.
- **If [R106] npx-settings cleanup becomes desired:** same propagation pattern (Shape 1 vs Shape 2), ~8 commits, log as Motivating Example #3. Consider whether to wait for HOS planning to resolve canonical-locus question first.
- **HOS planning resumption:** the leakage inventory + two concrete motivating examples is probably sufficient evidence that portability has to be a first-class constraint in the design.
- **If editing `auto-memory-hook.mjs` or `mcp-client.mjs`:** remember 8 copies exist across 8 repos. Every change needs 8-way propagation until HOS resolves the duplication. Current MD5 after this session: per-hive identical; reverify after any change.
- **Shape 1 vs Shape 2 mismatch:** if the settings.json Edit pattern fails on a hive, re-read — the hive's settings.json structure may differ from the sibling hive you cribbed the edit from. Shape 2 hives (Alpha Empress, SEAD) put auto-memory on `Stop` not `SessionEnd`, and use the `process.argv.splice(1,0,f)` form.

---

## 8. Artifact integration status per [R016]

- `mcp-client.mjs`, `auto-memory-hook.mjs`, `terminate-idle-agents.mjs`: **(c) integrated deliverable** — wired into SessionStart/SessionEnd/Stop hooks across 8 repos, exercised end-to-end, committed to origin.
- Motivating Example #2 section in HOS memory: **(a) research artifact** — captured evidence, not yet acted on architecturally; belongs to the HOS planning thread.
