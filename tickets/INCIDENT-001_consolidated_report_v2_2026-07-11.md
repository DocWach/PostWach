# INCIDENT-001 — Consolidated Report v2 (`.claude/` deletion & recovery)

- **Status:** RESOLVED (committed base restored; residual re-apply + commit pending — see §8).
- **Severity:** High (loss of the PostWach hive's `.claude/` working tree — 542 files; fully recovered from git; uncommitted edits recoverable from local file-history).
- **Date:** 2026-07-11.
- **Authoring session:** `fddfa778` (the session that CAUSED the deletion — authored for accountability), consolidating the discovery/recovery work of session `0618d5b0` and the Red/Blue/White (RBW) review.
- **Provenance (R018):** Claude (Anthropic, Opus 4.8, claude-opus-4-8[1m], Claude Code, session `fddfa778`), 2026-07-11.
- **Relationship to prior docs (version control):** consolidates and CORRECTS `PostWach_INCIDENT-001_dotclaude_deletion_2026-07-11.md` (the working ticket) and `INCIDENT-001_PostWach-session-contribution_2026-07-11.md` (the `0618d5b0` contribution). Where this v2 and the earlier docs disagree, **this v2 governs** (it post-dates the RBW fact-check). Distinct filename by design; does not overwrite either prior doc.

---

## 0. Version history (changelog)
| Ver | Date | Session | Change |
|---|---|---|---|
| v0.1 | 2026-07-11 | `0618d5b0` (discovery) | Opened ticket: discovery, git-forensic diagnosis (unstaged `D`, recycle-bin check), blast radius, ordered recovery options. Root cause initially *hypothesized* as the parallel session / bypass-mode agents. |
| v0.2 | 2026-07-11 | `0618d5b0` | Root cause CONFIRMED to `fddfa778`'s recursive delete (from that session's transcript). Recovery findings: snapshots mostly exhausted, but Claude Code `file-history` FOUND → uncommitted edits recoverable. |
| contrib | 2026-07-11 | `0618d5b0` | Separate contribution doc: discovery + recovery-source forensics + recovery method, reproducible. |
| **v2** | **2026-07-11** | **`fddfa778` + RBW** | **This report.** Corrections per RBW: (a) **status → RESOLVED** (recovery performed); (b) the "second unidentified recursive delete" in log `6e87c5db` **identified as unrelated** (old temp cleanup); (c) **proximate-cause honesty** added (7/10 delete proven; 7/11 disappearance mechanism inferred, not logged); (d) recovery-win (file-history) recorded. |

---

## 1. Event log (chronological; each event tagged PROVEN or INFERRED)
| When (UTC / ~MST) | Event | Evidence | Status |
|---|---|---|---|
| 2026-07-11 **01:16:37Z** / 2026-07-10 ~18:16 | Session `fddfa778` ran `Remove-Item -Recurse -Force $bad` (line 119), again `-ErrorAction Stop` (line 132), then `& cmd /c "rd /s /q "$bad""` (line 136), where `$bad = "…\01 PostWach\.claude"`. **Intent: delete ONE misplaced memory file; actual: recursive delete of the whole `.claude`.** | `fddfa778…jsonl` lines 119/132/136 | **PROVEN** |
| 2026-07-10 night → 2026-07-11 morning | `.claude` present again; session `0618d5b0` **read and edited** `.claude/skills` (morphism skills). | `0618d5b0` edits + 18 `file-history` snapshots with edit markers | **PROVEN** (that it was present) |
| ↳ mechanism of re-appearance after the 7/10 delete | OneDrive re-synced the files from cloud, OR the 7/10 delete did not fully land locally. | none direct | **INFERRED** |
| 2026-07-11 ~15:00 | `0618d5b0` **discovered** `.claude` missing: a `Read` of `morphism-research-frontier/SKILL.md` failed; `Test-Path .claude` = False; `git status` = 542 ` D`, 100% under `.claude/`. | `0618d5b0` transcript; git status | **PROVEN** |
| ↳ proximate cause of the 7/11 disappearance | Most likely OneDrive-sync propagation of the 7/10 delete. **No delete command is logged at ~15:00 in any session.** | absence of a logged delete | **INFERRED** |
| 2026-07-11 ~15:0x | Recovery-source forensics (`0618d5b0`): OneDrive cloud recycle bin EMPTY; Windows Recycle Bin absent (88 items, 0 match, newest 6/22); VS Code Local History none; **Claude Code `~/.claude/file-history/` FOUND — 18 snapshots with this-session edit markers.** | `0618d5b0` forensics | **PROVEN** |
| 2026-07-11 ~15:18 | **`git restore .claude`** performed and verified (`0618d5b0` established/verified it; session `fddfa778` also ran it this turn: BEFORE = missing / 542 ` D` → AFTER = 542/542 present, `git status -- .claude` clean). | both sessions' commands; git status | **PROVEN** |
| 2026-07-11 | Working ticket + contribution authored; **RBW review** run; log `6e87c5db` identified as an **unrelated** temp cleanup (`AppData\Local\Temp\deck*_png`, dated **2026-06-22**), NOT a `.claude` delete. | RBW (Red) verification | **PROVEN** |
| 2026-07-11 | This consolidated v2 report authored. | this file | **PROVEN** |

---

## 2. Root cause (confirmed) + proximate-cause honesty
- **Confirmed cause:** session `fddfa778` executed a **recursive force-delete of `01 PostWach\.claude`** (the commands above), intending to remove a single misplaced memory file. `Remove-Item -Recurse` deletes depth-first; it silently removed `agents/`, `skills/`, `helpers/`, `commands/`, `settings.json` and only errored on the OneDrive-locked stray `projects\…` subtree. A `Get-ChildItem` taken *after* that first pass showed "only `projects\…` remaining," which the operator misread as the folder's *original* contents when it was the **aftermath of the delete**. `rd /s /q` then finished it.
- **Proximate-cause honesty (RBW correction):** the 7/10 delete is proven, but `.claude` was demonstrably **present again on 7/11 morning** (edited by `0618d5b0`) and then missing by ~15:00 **with no delete command logged in between**. So the *direct* cause of the state discovered at 7/11 15:00 is **most likely OneDrive-sync propagation of the 7/10 delete, but is not directly logged.** `fddfa778` is the confirmed origin of a recursive `.claude` delete and the primary root cause; the exact 7/11 mechanism is an open forensic item, not a closed fact.
- **Superseded hypotheses:** the earlier "parallel session did it," "bypass-mode agents did it," and "a second unidentified recursive delete (`6e87c5db`)" hypotheses are all **retired** — `6e87c5db` is an unrelated 2026-06-22 temp cleanup; no second `.claude` delete exists in the logs.

## 3. Forensic evidence (RBW-verified, read-only)
Independently checked by both Red and Blue against the actual logs/git:
- Delete commands at `fddfa778` lines 119/132/136 — **SUPPORTED**.
- Executed delete is in `fddfa778` only (the string also appears in `0618d5b0` but **quoted for analysis**, not executed) — **SUPPORTED**.
- `fddfa778` = the Patsy/this session (`Patsy_v1_Build_Runbook`, `Patsy_Decision_Register`) — **SUPPORTED**.
- 542 files, all under `.claude/`, intact in git — **SUPPORTED**.
- `6e87c5db` recursive delete targets `AppData\Local\Temp\deck*_png` (2026-06-22), not `.claude` — **SUPPORTED** (resolves the caveat).

## 4. Blast radius
- **Deleted (recovered):** `.claude/` only — 542 files (skills/agents/helpers/commands/settings).
- **Safe / unaffected:** `Papers/`, `docs/` (scorecards, session archives), `scripts/`, `tickets/`, `_workspace/`; the Fable-planning research artifacts under `00 Planning and Execution/Fable 5 planning/`; and the **user-profile auto-memory** at `C:\Users\pfwac\.claude\…\memory\` (a different location from the project `.claude`).

## 5. Recovery (performed)
- **Committed base:** `git restore .claude` → **542/542 files** restored; `git status -- .claude` **clean**. Verified.
- **Uncommitted edits (recoverable, per `0618d5b0`):** Claude Code's `~/.claude/file-history/` holds 18 snapshots carrying `0618d5b0`'s edit markers (`2026-07-10 currency update`, `wach2024theoretical`, `Integration status [R016]: (a) research artifact`). `fddfa778` edited **no** skill files, so it has no skill edits to recover.
- **Residual (see §8):** re-apply `0618d5b0`'s uncommitted skill edits from file-history + transcript, then **commit `.claude/`**.

## 6. RBW adjudication summary
- **Forensics: airtight** (verified independently by Red and Blue).
- **Thoroughness (combined docs): strong** — discovery, git-forensics, blast radius, exhaustive recovery-source search incl. the file-history win, recovery method, root cause, prevention.
- **Corrections applied in this v2:** status currency (was accurate at authoring, stale after recovery); `6e87c5db` closed as unrelated; proximate-cause over-attribution softened to "inferred."
- **Verdict:** not untruthful; the prior gaps were staleness and one over-attribution, both corrected here.

## 7. Prevention lessons
0. **Never use a recursive force-delete (`Remove-Item -Recurse` / `rd /s /q`) to remove a single file.** Delete only the specific path. Never trust a directory listing taken after a *partially-failed* recursive delete in a OneDrive-synced tree — its aftermath mimics sparse "original" contents. *(This is the direct cause; it is mine.)*
1. **Do not run two Claude Code sessions manipulating the same `.claude/` in a OneDrive-synced directory concurrently** — shared on-disk state + OneDrive sync + multi-process writes is a loss trap (and it corrupts incident-record editing too: a concurrent ticket edit already hit a "modified since read" collision).
2. **Be sparing with bypass-mode external agents** (full disk access = deletion risk).
3. **Commit `.claude/` skill edits promptly** so working-tree loss is fully git-recoverable. Uncommitted edits are the only real exposure.
4. **Claude Code `file-history` is a real local safety net** for uncommitted edits, but it is per-session and not permanent — not a substitute for committing.

## 8. Open items
- [ ] Re-apply `0618d5b0`'s uncommitted skill edits (currency blocks marking bridge/Target A/harmonization CLOSED; R016 `(a)` tags + analyst downgrades; cross-project-reviewer roster; ref-maintenance) from file-history + transcript.
- [ ] **Commit `.claude/`** (it is clean/restored) so this cannot recur silently.
- [ ] (Optional forensic) Confirm whether the 7/11 ~15:00 disappearance was OneDrive-sync propagation vs a distinct event — currently INFERRED.
- [ ] Fold prevention lessons into the post-2026-07-12 repo-cleanup + Alpha Empress governance review; evaluate excluding `.claude/` from OneDrive sync.
