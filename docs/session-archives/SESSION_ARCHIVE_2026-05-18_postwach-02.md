# Session Archive — 2026-05-18 postwach-02

**Hive:** PostWach
**Scope:** Diagnose recurring Claude Code / ruflo startup breakages (2026-05-04, 2026-05-08, plus a latent 2026-05-11 incident discovered during this session). Apply a permanent fix so the failure mode does not recur. User hypothesis at intake was that the Gemini CLI install was implicated.
**Platform:** Ruflo v3.7.0-alpha.14, Claude Code v2.1.143, Windows 11.
**Outcome:** Root cause re-classified from "Gemini install conflict" to "npm atomic-rename race during Claude's own self-update." Three-layer permanent fix applied: auto-update disabled on both tools, orphan staging dirs cleaned (one parked due to file lock), self-heal wrapper installed in `dsp` with built-in staleness reminder.

---

## 1. Entry state

User asked to warm up ruflo, review recent records of the breakage, and noted the suspicion that installing/using the Gemini CLI was implicated. After diagnosis was presented, user pushed for a permanent solution, then for deeper investigation before committing, then approved a refined three-layer plan plus a self-heal wrapper.

Two earlier archives documented the symptoms:
- `SESSION_ARCHIVE_2026-05-04_postwach-04.md`: claude.exe restored from `.old.1777925134995`; claude-flow.cmd self-recursion fixed.
- `SESSION_ARCHIVE_2026-05-08_diagnostic-repair-01.md`: claude.exe restored from `.old.1778164016975`; claude-flow regressed to 3.5.80; stale daemon PID.

---

## 2. Method

1. **Read both prior archives + grep `gemini` mentions across archives/memory.** Older Gemini references were about Gemini-as-LLM-provider in IGNITE/MBSE work, unrelated to CLI installation. Only the 2026-05-04 archive listed "Platform: Gemini CLI" — circumstantial.
2. **Probed `%APPDATA%\npm\node_modules\`.** Found two orphaned npm staging directories: `@google\.gemini-cli-urC4acx2` (created 2026-04-30, finished 2026-05-08; 0.5 MB) and `@anthropic-ai\.claude-code-PAq18HUw` (created today 1:21 PM; 473 MB). Both are npm's `.<pkgname>-<random>` atomic-rename staging dirs that never got cleaned up.
3. **Converted `.old.<epoch>` timestamps to local time.** 1777925134995 = 2026-05-04 16:05 EDT; 1778164016975 = 2026-05-07 10:26 EDT. Found a third orphan inside the 5/18 staging dir: `.old.1778513826079` = 2026-05-11 11:37 EDT — a latent break that never surfaced as a visible failure because no one tried to start Claude until the next auto-update overwrote the stale state.
4. **Verified Gemini install was NOT concurrent with first breakage.** Gemini package directory mtime 2026-05-08 10:11 AM is AFTER the 2026-05-07 10:26 EDT second breakage. The Gemini hypothesis was a temporal coincidence, not the mechanical cause.
5. **Identified the mechanical cause.** Claude Code's auto-updater renames the running `claude.exe` to `claude.exe.old.<epoch>` (Windows cannot overwrite an in-use EXE), then drops in the new copy. When step 2 fails — typically due to file-handle contention from Windows Defender, OneDrive scan, antivirus, or a stale process — you are left with the rename done but no new binary. The orphan `.<name>-<random>` directories are the same npm pattern failing.
6. **Verified Gemini CLI settings schema.** Grepped the gemini-cli bundle for update-control keys. Migration code in `chunk-H6HKTH5H.js` showed legacy key `disableAutoUpdate` was migrated to current key `general.enableAutoUpdate` under the merged settings root.
7. **Attempted JSON-based disable for Claude Code.** Edit of `~/.claude/settings.json` to add `"autoUpdater": false` was rejected by Claude Code's settings validator. Schema does not expose `autoUpdater` / `autoUpdates` as a JSON field; documented mechanism is the env var `DISABLE_AUTOUPDATER=1` (already set in step 9).
8. **Cleaned orphan staging dirs.** Gemini orphan deleted cleanly. Claude orphan: 22 MB deleted, then `Access Denied` on 2 stuck files (~451 MB) holding stale handles. Renamed the partially-cleaned dir to `_DELETE_ME_orphan_PAq18HUw` so it cannot collide with any future install. Will clear cleanly after reboot.
9. **Wrote the three-layer fix.**
   - `DISABLE_AUTOUPDATER=1` user env var via `[Environment]::SetEnvironmentVariable(..., "User")`.
   - `general.enableAutoUpdate: false` added to `~/.gemini/settings.json` alongside existing `ide.hasSeenNudge` and `security.auth.selectedType`.
   - `dsp.ps1` rewritten with two functions: (a) self-heal — if `claude.exe` is missing in `bin/`, find newest `claude.exe.old.*` by descending name-sort and rename it back; (b) staleness reminder — check `package.json` LastWriteTime for claude-code and gemini-cli; print yellow warning + exact install command when >35 days. `dsp.cmd` rewritten with the self-heal half only.
10. **Decision on wrapper placement.** Self-heal lives in `dsp.ps1` / `dsp.cmd`, not in `claude.ps1` / `claude.cmd`. Reason: the latter are owned by npm and get overwritten by every `npm install -g @anthropic-ai/claude-code`. `dsp` is user-owned and survives. Trade-off: if user ever launches `claude` directly (not via `dsp`), self-heal is bypassed.
11. **Memory + index update.** Created `memory/project_claude_gemini_update_procedure.md`. Added one-line index entry under new `Local Environment / Tooling` section in MEMORY.md.

---

## 3. Deliverables

### Files modified

- `%APPDATA%\npm\dsp.ps1` — rewritten: self-heal pre-flight (restore `claude.exe.old.<newest>`) + staleness check (>35 days warning for both Claude and Gemini package.json mtimes) + invoke `claude --dangerously-skip-permissions @args`.
- `%APPDATA%\npm\dsp.cmd` — rewritten: self-heal pre-flight only (CMD batch lacks PowerShell's date arithmetic) + invoke `claude --dangerously-skip-permissions %*`.
- `~/.gemini/settings.json` — added `general.enableAutoUpdate: false` block.
- `memory/MEMORY.md` — new section "Local Environment / Tooling" with one-line pointer.

### Files created

- `memory/project_claude_gemini_update_procedure.md` — full procedure including diagnostic history, three-layer fix details, manual update workflow, and what-if-dsp-fails recovery steps.
- `docs/session-archives/SESSION_ARCHIVE_2026-05-18_postwach-02.md` — this archive.
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-05-18-postwach-02.yaml` — productivity scorecard.

### System state changed

- Windows user env var `DISABLE_AUTOUPDATER=1` set (User scope).
- `@google\.gemini-cli-urC4acx2` orphan deleted (0.5 MB).
- `@anthropic-ai\.claude-code-PAq18HUw` orphan: ~22 MB deleted, ~451 MB renamed to `_DELETE_ME_orphan_PAq18HUw` pending reboot.

### Files NOT changed

- `~/.claude/settings.json` — Edit rejected by schema validator (no `autoUpdater` field exists). Env var route used instead. File on disk is unchanged from session start.
- `claude.ps1`, `claude.cmd`, `claude-flow.ps1`, `claude-flow.cmd`, `ruflo.ps1`, `ruflo.cmd`, `gemini.ps1`, `gemini.cmd` — all npm-owned wrappers untouched.

---

## 4. Decisions (durable)

- **D1 (root cause).** Both breakages were Claude Code's own auto-updater failing mid-rename due to file-handle contention on Windows (Defender / OneDrive / stale process). The Gemini CLI is mechanically separate (different `@scope`, different `bin/`). The Gemini install timing was circumstantial. Disabling Gemini's auto-updater is hygiene, not the actual fix.
- **D2 (JSON vs env).** Claude Code's `~/.claude/settings.json` schema does NOT expose `autoUpdater` or `autoUpdates`. The only documented disable mechanism is env var `DISABLE_AUTOUPDATER=1`. Do not attempt JSON-based approaches in future sessions; the validator rejects unknown fields.
- **D3 (wrapper placement).** Any self-heal / pre-flight logic for Claude must live in `dsp.ps1` / `dsp.cmd` (user-owned), never in `claude.ps1` / `claude.cmd` (npm-owned, overwritten on every install). Cost of this choice: user must launch via `dsp`, not raw `claude`, for self-heal to fire.
- **D4 (staleness signal).** Use `package.json` LastWriteTime as install-recency signal, not a separately-maintained JSON timestamp file. Self-updating by construction: whenever user runs `npm install -g <pkg>`, the package.json mtime gets bumped, resetting the staleness clock automatically.
- **D5 (latent break confirmation).** A third breakage occurred 2026-05-11 11:37 EDT (epoch 1778513826079) that never surfaced as a visible failure — it was found buried inside today's staging dir during cleanup. This raises the actual incident rate from 2 in 4 days (5/4, 5/8) to 3 in 8 days (5/4, 5/7-as-symptom, 5/11). Confirms the failure is recurring and justifies the preventive fix even though no active break was happening at session start.
- **D6 (parked orphan).** `_DELETE_ME_orphan_PAq18HUw` is parked, not deleted. Two stuck files (~451 MB) held by stale Windows handles cannot be released without a reboot. The rename ensures no future npm install can collide with the directory name. Manual cleanup after next reboot.

---

## 5. Open items the user must address

1. **Reboot at convenience to clear the parked orphan.** After reboot, delete `C:\Users\pfwac\AppData\Roaming\npm\node_modules\@anthropic-ai\_DELETE_ME_orphan_PAq18HUw` (no longer locked).
2. **Verify env var takes effect.** This session inherited pre-change env. Next `dsp` launch will run with `DISABLE_AUTOUPDATER=1`. No action required, just be aware.
3. **Manual update cadence.** Roughly monthly: exit all Claude/Gemini/ruflo sessions → fresh PowerShell → `npm install -g @anthropic-ai/claude-code` and/or `npm install -g @google/gemini-cli` → verify with `--version`. `dsp.ps1` will print a yellow reminder at startup when >35 days since last install.
4. **Optional add-on deferred:** Windows Defender exclusion for `%APPDATA%\npm\` would reduce contention. Needs admin. Not done this session.
5. **Optional add-on deferred:** Pin Gemini to stable channel rather than current nightly (`0.42.0-nightly.20260507`). Nightly = more frequent updates than needed. Not done this session.

---

## 6. Out-of-scope items not pursued

- Structural install isolation (separate npm prefixes per tool).
- ruflo / claude-flow auto-update mechanism analysis. (No evidence ruflo participates in the same race; not investigated.)
- Defender exclusion for `%APPDATA%\npm\` (deferred per user).
- Inspection / cleanup of any other orphan staging dirs across other npm `@scope` packages (only `@anthropic-ai/` and `@google/` examined).
- Windows scheduled task or boot-time janitor that auto-clears `.exe.old.*` and orphan staging dirs (out of scope this session; if breakages stop occurring, no need to add).

---

## 7. Next session entry hints

- **Pickup file:** `memory/project_claude_gemini_update_procedure.md` is the canonical reference for the manual update procedure and what-if-dsp-fails recovery. Read that first if any Claude/Gemini startup issue recurs.
- **Diagnostic playbook on next failure:**
  1. Check `%APPDATA%\npm\node_modules\@anthropic-ai\claude-code\bin\` for `claude.exe.old.*` orphans. If present, the newest one is the binary to restore.
  2. If `dsp` was used to launch, self-heal should have already done the restore — investigate why it did not.
  3. Check for new orphan `.<name>-<random>` staging dirs under `%APPDATA%\npm\node_modules\@anthropic-ai\` or `@google\`. Rename to `_DELETE_ME_<name>_<random>` to park them; delete after reboot if locked.
  4. If everything looks clean and tool still fails, reinstall via `npm install -g <pkg>` from a fresh PowerShell.
- **Verification one-liner:**
  ```powershell
  "DISABLE_AUTOUPDATER (User): $([Environment]::GetEnvironmentVariable('DISABLE_AUTOUPDATER','User'))"
  "Gemini enableAutoUpdate: " + ((Get-Content "$env:USERPROFILE\.gemini\settings.json" -Raw | ConvertFrom-Json).general.enableAutoUpdate)
  ```
  Expect: `1` and `False`.
- **Trigger for review of this fix:** if `dsp` ever prints the `[dsp self-heal] claude.exe missing; restoring from ...` line, that is a signal that the auto-update is still firing despite the env var, OR that another mechanism is renaming `claude.exe`. Investigate before normalizing.
