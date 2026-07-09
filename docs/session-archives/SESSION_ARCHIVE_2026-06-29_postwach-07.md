# Session Archive — 2026-06-29 postwach-07

> PROVENANCE: claude-opus-4-8[1m] (Anthropic, Claude Code CLI) ran this session: root-caused the
> unwanted git co-author, performed the portfolio-wide history rewrite + force-push, installed the
> prevention hook, and authored the records. ruflo/claude-flow (v3.14.4) not used for orchestration this
> session; no swarm, no subagents. Tooling: `git filter-repo` (pip-installed). No manuscript citations
> (R019 n/a). NOTE: per principal direction this session, commits no longer carry the
> `Co-Authored-By: claude-flow <ruv@ruv.net>` trailer.

**Hive:** PostWach (CTO / Chief Scientist). **Researcher:** Paul Wach. **Model:** Claude Opus 4.8 [1m]. **Status:** CLOSED.

**Headline:** Removed the **ruvnet** co-author attribution from the principal's git repos portfolio-wide.
Root-caused it (a commit-message trailer the claude-flow harness appends), rewrote history to strip it
from **12 of 13** in-scope DocWach repos with integrity-checked force-pushes, installed a durable
prevention protocol (behavioral + global hook), and deferred 2 repos that carry collaborator/public risk.

## 1. Root cause
- Author/committer were always correct (`Paul Wach <pfwach@gmail.com>`). The "ruvnet" co-author came ONLY
  from the line `Co-Authored-By: claude-flow <ruv@ruv.net>` that the harness default appends to commits;
  GitHub maps `ruv@ruv.net` → the **ruvnet** account, rendering it as co-author on DocWach repos.

## 2. Scope decided (principal)
- Portfolio-wide, **DocWach only** (exclude Brad's bmpwach-lab repos). Prevention = **behavioral + global hook**.
- 15 repos carried the trailer; 2 were bmpwach-lab (excluded) → 13 in-scope DocWach repos.

## 3. Cleaned (12 repos) — rewrite + force-push, all integrity-verified
Method per repo: back up `git diff HEAD` → `git filter-repo --message-callback` (strip the line) →
re-add remote(s) → re-apply dirty patch → `git push --force` → verify. **Tree hash unchanged on every
repo** (message-only rewrite), commits preserved, trailers → 0 (local + origin), uncommitted work restored.

| Repo | trailers→0 | note |
|---|---|---|
| Lawsun, Fort Wachs, Alpha Empress, GI-JOE, MACQ, COSYSMO, PLM, SEAD, Finance Bro, STOIC | ✅ | straightforward single-remote |
| PostWach (83→0) | ✅ | 22 dirty files preserved; submodule-pointer hunk skipped via `git apply --reject` |
| SysMLv2 main (16→0) | ✅ | `--refs main` only; **batch1/public INCOSE untouched**; both remotes + push guards restored; pushed `main→origin` only |

## 4. Prevention installed (the "update protocol")
- **Behavioral:** memory `feedback_no_ruvnet_coauthor.md` + MEMORY.md pointer — I no longer add the trailer.
- **Global hook:** `~/.githooks/` dispatcher set via `core.hooksPath`. `commit-msg` strips any
  `Co-Authored-By:…ruv@ruv.net` line; ALL hook types chain to each repo's local `.git/hooks/<name>` so
  per-repo hooks (e.g. git-LFS in the MBSE plugin repo) still run. Tested: trailer stripped, 0 remaining.

## 5. Initially deferred — both COMPLETED on resume (2026-06-30, principal-approved)
- **src-repo** (Supplychain VT Senior Design, 24→0): shared repo with a VT student (`jroleaga24R`,
  2 commits). Principal confirmed the project is finished; rewrote + force-pushed. Tree unchanged, all
  three authors preserved (DocWach, jroleaga24R, Paul Wach).
- **INCOSE FuSE output** (`batch1` → public `DocWach/INCOSE_FuSE_Vision2035`, 1→0): rewrote `batch1` only
  (`--refs batch1`), restored remotes/guards, force-pushed `batch1→incose-fuse/main` (the legitimate
  guarded public push). INCOSE FuSE public history verified 0 trailers; the **SysMLv2 hive `main` stayed
  clean and untouched**. Terminology (principal, 2026-06-30): INCOSE FuSE is a research OUTPUT, not
  "SysMLv2" (the hive is `main`→`origin`). See `memory/feedback_incose_fuse_not_sysmlv2.md`.

## 6. Method/safety notes (lessons)
- **`git filter-repo` discards uncommitted *tracked* changes** (internal hard reset). Untracked files
  survive. Mitigation used: back up `git diff HEAD` and re-apply after (caught Fort Wachs + PostWach edits).
- `git apply` is atomic; a submodule-pointer hunk fails the whole patch — use `--reject` to apply the
  real file hunks and skip the submodule (PostWach).
- filter-repo removes remotes; must re-add. For SysMLv2, restored both remotes + all push guards and used
  `--refs main` to keep batch1/public pristine.
- All repo commit SHAs changed (history rewrite). Solo private repos → low risk; any other clones must re-clone.

## 7. Status
- **COMPLETE.** All 13 in-scope DocWach repos + the INCOSE FuSE public output are cleaned (trailers → 0,
  force-pushed, verified). Only the 2 bmpwach-lab repos (Brad's) still carry trailers — excluded by the
  principal's scope choice; notify Brad if desired.
- All repo commit SHAs changed (history rewrite). Solo private repos → low risk; any other clones must re-clone.
