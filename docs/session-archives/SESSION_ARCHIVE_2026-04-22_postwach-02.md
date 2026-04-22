# Session Archive — 2026-04-22 postwach-02

**Hive:** PostWach
**Scope:** Warm up ruflo, diagnose silent MCP bridge failure, roll a permanent portfolio-wide fix across all 9 V3 hives, neutralize SysMLv2 incose-fuse contamination threat, and capture architectural findings in memory.
**Platform:** Ruflo v3.5.80, claude-opus-4-7 (1M context), Windows 11 ARM64
**Outcome:** `mcp__claude-flow__*` tool surface reachable from Claude Code for the first time. Global rule [R017] added; 9 hive-local rules strengthened; 12 `.mcp.json` files normalized (2 new, 10 corrected); 5 `.gitignore` files un-ignored `.mcp.json`; SysMLv2 two-remotes near-miss averted and mechanically guarded. 9 commits pushed to 9 hive repos. HOS thread gains portability principle; new SysMLv2 near-miss memory.

---

## 1. Entry state

User request: "warm up ruflo and initiate claude doctor". Ran `claude-flow --version` (ruflo v3.5.80) and `claude-flow doctor` (11 passed, 3 warnings — no API keys, no local TypeScript, no agentic-flow; all optional). `claude doctor` (Claude Code's own TUI) errored in non-interactive stdin; flagged `! claude doctor` as the invocation path for the user.

Daemon start via `claude-flow start --daemon` reported healthy but `status` immediately showed STOPPED. Flagged the Windows daemon-persistence quirk. User asked why daemon matters; explained the two-daemon model (worker vs orchestration) and the MCP tool surface dependency.

User flagged suspicion: "something may be blocking use of ruflo and forcing use of Claude Code". Investigation confirmed: `.mcp.json` in PostWach (and across hives) registered ruflo via `cmd /c npx @claude-flow/cli@latest mcp start`, which `claude mcp list` reported as "✗ Failed to connect". The local ruflo MCP server itself (PID 4744) was running; Claude Code just couldn't reach it because its registration pointed at an npx-invoked parallel server instead of the local one.

---

## 2. Method

Direct tool use; no Task agents spawned. Staged rollout with proof-of-life gate between each phase. User approved each phase before execution (per "discuss before executing" rule).

1. **Proof of life.** Fixed PostWach `.mcp.json` (command → `claude-flow`, drop `cmd /c npx`). Verified `claude mcp list` now shows `✓ Connected`.
2. **Portfolio inventory.** Enumerated all `.mcp.json` files under `00 My Research/` (10 files, 3 dialects: standard npx, npx+quiet, older `claude-flow@alpha`). Identified Fort Wachs and Alpha Empress as V3 hives without `.mcp.json`.
3. **Fix rollout (12 files).** Batch-edited 6 files (Dialect 1/2), wrote 3 (Dialect 3 — preserved `ruv-swarm` + `flow-nexus` entries), created 2 new (Fort Wachs + Alpha Empress). All 12 pass JSON validation.
4. **Rule governance.** Added global [R017] to `~/.claude/CLAUDE.md` enforcing the pattern. Strengthened 9 hive-local rules ([R106], [P006], [G006], [C006], [S006], [L006], [D006], [X006], [A006]) from `[bash]` scope to `[bash,edit]` scope covering both shell and `.mcp.json` usage, referencing [R017].
5. **Structural discovery.** Inspection revealed `.mcp.json` is gitignored in 5 of 9 V3 hives (PostWach, GI-JOE, COSYSMO, SysMLv2, SEAD). Fix was local-machine-only until gitignore was removed. User approved Option A (un-ignore + track).
6. **SysMLv2 contamination audit.** User escalated concern about INCOSE_FuSE_Vision2035 being a public repo; asked for permanent fix and asked why it keeps coming up. Audit found:
   - `incose-fuse/main` clean — only `LICENSE`, `README.md`, `docs`, `models`.
   - Histories disjoint (`git merge-base` empty).
   - But local `batch1` carried stray hive commit `9e444b0` (`[S001-S006]`) one push away from public leak.
   - Root cause: two remotes in one working directory with no mechanical guard.
7. **SysMLv2 guards installed.** Reset batch1 to `incose-fuse/main` (content preserved on origin/main as `81ed171`). Set `branch.main.pushRemote=origin`, `branch.batch1.pushRemote=incose-fuse`, `remote.incose-fuse.push=refs/heads/batch1:refs/heads/main`, `push.default=current`. Added [S007] to SysMLv2 CLAUDE.md.
8. **Gitignore cleanup.** Removed `.mcp.json` line from 5 hive .gitignores.
9. **Per-hive commits.** Sequential, surgical stage (only `.gitignore`, `.mcp.json`, `CLAUDE.md`). 9 V3 hives committed and pushed to `origin` only. SysMLv2 push-guard verified mid-commit (`branch.main.pushRemote=origin` read back before push). PostWach push bundled two prior unpushed session-archive commits (`198c91c`, `fccfffd`) — flagged to user.
10. **User-level cleanup.** `~/.claude.json` stale `npx claude-flow@alpha` entries normalized via `replace_all` Edit (7 occurrences). Deleted `.claude/scheduled_tasks.lock` (orphan, PID 6360, held since 2026-04-13).
11. **Memory capture.** User asked what to commit to memory given the portability concern. Proposed three priority items; user approved all. Appended portability principle to HOS thread; created SysMLv2 near-miss memory; updated MEMORY.md index (`.claude vs .claude-flow` Q3 partially resolved; HOS portability bullet; SysMLv2 Git Remotes push-guards note).

---

## 3. Deliverables

### New files

- 2 new `.mcp.json`: Fort Wachs, Alpha Empress
- `memory/project_sysmlv2_two_remotes_nearmiss.md` — incident report, audit findings, guards applied, deferred structural fix
- `docs/session-archives/SESSION_ARCHIVE_2026-04-22_postwach-02.md` (this file)
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-04-22-postwach-02.yaml`

### Modified files

- 10 `.mcp.json`: PostWach, MACQ, GI-JOE, Roadmapping Hive, COSYSMO, SysMLv2, PLM, SEAD, BP Marketing, Claude_code_test_setup (all normalized to `claude-flow mcp start`)
- 9 hive `CLAUDE.md`: PostWach [R106], MACQ [P006], GI-JOE [G006], COSYSMO [C006], SysMLv2 [S006]+[S007], PLM [L006], SEAD [D006], Fort Wachs [X006], Alpha Empress [A006] — rule strengthening + [R017] references
- 5 `.gitignore`: PostWach, GI-JOE, COSYSMO, SysMLv2, SEAD — removed `.mcp.json` line
- `~/.claude/CLAUDE.md` — added [R017] MCP registration rule; cleaned up line-12 duplicate guidance
- `~/.claude.json` — 7 per-project MCP scopes normalized from `npx claude-flow@alpha` to `claude-flow mcp start`
- `memory/project_hos_governance_composition.md` — appended "Portability principle" section (hard constraint, leakage inventory, motivating example, 6 open design questions)
- `memory/MEMORY.md` — 3 surgical updates (`.claude vs .claude-flow` Q3 partial resolution; HOS portability bullet; SysMLv2 Git Remotes push-guards note)

### Deleted

- `.claude/scheduled_tasks.lock` (orphan)

### Code/repo changes

9 hive commits, all pushed to `origin` only:

| Hive | Repo | Branch | Commit |
|---|---|---|---|
| PostWach | DocWach/PostWach | main | `931fad0` |
| Alpha Empress | DocWach/Alpha_Empress | main | `2117303` |
| Fort Wachs | DocWach/Fort-Wachs | main | `8af8bc0` |
| MACQ | DocWach/MACQ | main | `a18b6cf` |
| GI-JOE | DocWach/JOE-G | master | `51cd0c0` |
| COSYSMO | DocWach/COSYSMO-Hive | master | `151ae43` |
| SysMLv2 | DocWach/SysMLv2-Hive | main | `1306f48` |
| PLM | DocWach/PLMr | main | `bceadc2` |
| SEAD | DocWach/SEAD | main | `1ca0d8b` |

SysMLv2 commit includes [S007] push-guard rule. `incose-fuse` remote untouched. `batch1` rewritten locally only (was unpushed).

---

## 4. Open threads touched

- **HOS + Governance Composition:** portability constraint added as hard design requirement for future planning sessions. N×N commit cost of today's fix is the motivating empirical evidence.
- **.claude vs .claude-flow Directory Structure:** Q3 (rebrand accounting) partially resolved. Q1 (directory separation) and Q2 (structure consistency) still open.
- **SysMLv2 Git Remotes:** near-miss documented, guards installed, structural fix deferred.

---

## 5. Non-V3 hives — partial state

`.mcp.json` fixed locally but not committed in 3 hives (user flagged these as archival candidates, experimental work):
- Roadmapping Hive
- BP Marketing
- Claude_code_test_setup

If activated later, their `.mcp.json` is already correct on this machine; a commit pass can propagate it when needed.

---

## 6. Out-of-scope items user flagged

1. **Folder move:** Alpha Empress (`01_Alpha_Impress_Disruptor/`) and PostWach → `02 Hives/`. Deferred to separate session (touches project-registry, MEMORY.md paths, per-project scopes in `~/.claude.json`).
2. **Archival decision:** COSYSMO, BP Marketing, Claude_code_test_setup flagged as experimental; archival review deferred.
3. **Pre-push hook for SysMLv2:** Layer 2 guard (Item 3) deferred. Config guards + [S007] rule are belt; hook would be suspenders.
4. **Separate working dir for INCOSE_FuSE_Vision2035:** Layer 2 structural fix (Item 5) deferred. The only "never comes up again" answer to the two-remotes-in-one-dir problem.
5. **HOS planning mode resumption:** gated on user decision. Portability now a first-class requirement when session resumes.

---

## 7. Next session entry hints

- If resuming HOS planning: read `memory/project_hos_governance_composition.md` in full; the portability section at the end sets the new frame.
- If working in SysMLv2: `git branch -vv` and `git remote -v` before any push. [S007] documents the guards; `memory/project_sysmlv2_two_remotes_nearmiss.md` documents why.
- If observing drift in any hive's `.mcp.json` back to an `npx` pattern: ruflo/claude-flow init may be regenerating the broken default. File upstream if so.
- MCP bridge is live. `mcp__claude-flow__*` tools are now usable from Claude Code — consider exercising `mcp__claude-flow__swarm_init` etc. in the next coordination-heavy session.
