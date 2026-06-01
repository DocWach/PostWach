# Session Archive — 2026-04-29 postwach-03

**Hive:** PostWach
**Scope:** Resume the ORCiD-and-PostWach workflow follow-on flagged as next-session hint (c) in the 2026-04-28 Genesis archive. Scope a push-only sync workflow, register an ORCiD developer client, run a P1 OAuth + read smoke test. Recover from scoping error when the Public API tier turned out not to support write scopes.
**Platform:** Ruflo v3.5.80, claude-opus-4-7 (1M context), Windows 11 Home (ARM64), Python 3.12.10, requests 2.32.5, Microsoft Edge.
**Outcome:** Scope locked and recorded in `docs/orcid-workflow.md`. Auth helper at `scripts/orcid/auth.py` written and exercised end-to-end. P1 PASS: token cached for ~20 years, ORCiD record summary read (4 works, 0 employments, 0 education, 0 distinctions). Push phases (P3-P5) blocked at the Public API tier; user has emailed Ellen Dubinsky (UA Libraries) to determine whether a UA Member API write integration is available. Read-side phases (P2, P6, P7) remain unblocked.

---

## 1. Entry state

User: "warm up ruflo and resume conversation on the Genesis submission. Specifically, I want to set up the workflow between my ORCiD account work and PostWach." Session-start AutoMemory imported 168 entries; ruflo MCP stdio running. Genesis archive (2026-04-28) flagged ORCiD bulk-population workflow as a next-session hint, including a note that developer credentials had been configured but not used. The 2026-04-28 archive captured the bullet but not any in-conversation discussion of workflow direction. User clarified mid-session that this is the ORCiD-workflow task, not a Genesis task.

---

## 2. Method

Single-stream conversational session; no swarm, no Task subagents. Tools used: Read (PDF + scope docs + memory + session archive + script outputs), Glob/Grep (locate Genesis assets, find ORCiD references), Bash (Python invocation, gitignore inspection, port + listener checks, file timestamps, kill stale listener via PowerShell), Write/Edit (scope doc, auth.py with multiple iterative patches, env file, gitignore, session archive, scorecard, memory entry), WebSearch + WebFetch (UA ORCiD member status; UA Libraries integrations).

Phases:

1. **Memory + archive context recovery.** Loaded yesterday's Genesis session archive and confirmed it was scope-thin on the workflow direction. Asked user which read of "ORCiD-PostWach workflow" they wanted; user requested I review what's needed before scoping. Surveyed Genesis Top 10 RIS and discovered Paul's ORCiD ID `0000-0002-3085-2883` referenced in the SciENcv paste blocks.
2. **Scope dimensions and lock.** Presented 12 scoping dimensions ranked by impact. User locked all 12; declined detail on three that were design-only (failure modes) or future-deferred (out-of-scope items list and ontology task).
3. **Scope doc + memory.** Wrote `docs/orcid-workflow.md` covering decisions, path layout, credential schema, phased plan, out-of-scope deferrals, future ontology task, failure-mode design notes, operations CLI, open items, cross-references. Added project memory entry pointing to it; one-line index entry in `MEMORY.md`.
4. **Credentials and redirect URI.** User shared `01 Admin/01 CVs and Bios/ORCiD/ORDiD_worklfow_info.pdf` containing Client ID, Client Secret, registered URIs. Caught that the registered redirect URI was the user's public profile page (`https://orcid.org/0000-0002-3085-2883/DocWach_ORCiD`), which cannot serve as an OAuth callback for a CLI tool. Walked the user through OAuth's redirect URI semantics (teaching moment, two rounds), distinguishing it from the Application URL field. User added `http://127.0.0.1:8765/callback` as a second redirect URI.
5. **Auth helper implementation.** Wrote `scripts/orcid/auth.py` with: env-file loader, token cache, callback HTTP handler, token-exchange call, public-record summary reader. Added state directory to `.gitignore`. Wrote env file at `~/.config/postwach/orcid.env` containing the four credential values (off-repo).
6. **Three patch cycles to get the smoke test working.**
   - **Patch 1: Edge launch.** First run used `subprocess.Popen(["cmd", "/c", "start", "", "msedge", url])`. The `cmd` shell interprets `&` as command separator, so Edge received only the URL up to the first `&`. ORCiD returned `invalid_request: missing parameter response_type`. Replaced with direct `subprocess.Popen([edge_exe, url])` bypassing cmd entirely.
   - **Patch 2: Output buffering.** Initial background runs showed empty stdout because Python buffers when not attached to a terminal. Added `print = functools.partial(print, flush=True)` shim. Also switched invocation to `python -u`.
   - **Patch 3: API tier scoping error.** Requested `/authenticate /read-limited /activities/update /person/update`. ORCiD returned `invalid_request: one of the provided scopes is not allowed for this member`. Investigation: Public API tier supports only `/authenticate` and OpenID-related scopes; write scopes require Member API. Reduced SCOPES to `/authenticate` and reran.
   - **Patch 4: HTTP response hygiene.** First run with `/authenticate` got the user to click Authorize but the browser appeared to loop. Diagnosis: my callback handler omitted `Content-Length` and explicit `Connection: close`, plus log_message was silenced so I had no visibility into incoming requests. Re-enabled diagnostic logging and made responses well-formed.
7. **Smoke test PASS.** Final run completed cleanly: callback hit logged (`GET /callback?code=...`), token exchange succeeded, record read returned `Paul Wach / 4 works / 0 employments / 0 education / 0 distinctions`, token cached for ~7305 days.
8. **UA Member API research.** While the user authorized in Edge, used WebSearch + WebFetch to determine UA's ORCiD membership status. Confirmed: UA has been a Member since 2016 via GWLA / ORCID US Community / LYRASIS. Existing UA integrations (`orcid.arizona.edu`, `kmap.arizona.edu`, Faculty Portfolio) are read-only INTO UA from ORCiD. No documented write-direction integration. Identified Ellen Dubinsky (`edubinsky@arizona.edu`) as the right contact.
9. **Path A/B/C decision tree.** Documented three back-population paths in scope doc §12. User opted to email Ellen for Path B; Path A (Search & Link wizards) and Path C (manual web entry) reserved as fallbacks.
10. **Session close.** Updated scope doc to reflect P1 PASS, push blocked, Path B pending. Wrote this archive and the scorecard. No agents to terminate (none were spawned).

---

## 3. Deliverables

### New files
- `docs/orcid-workflow.md` — scope doc; 12 sections covering decisions, path layout, credential schema, phases, out-of-scope, future ontology task, failure modes, operations, open items, cross-references, reality check / Path A-B-C.
- `scripts/orcid/auth.py` — OAuth + read smoke-test helper. ~190 lines. Loads env, runs 3-legged OAuth flow with localhost callback, caches token, reads `/v3.0/{orcid-id}/record`, prints summary.
- `scripts/orcid/state/token_cache.json` — gitignored; access token + expiry. Created during smoke test.
- `~/.config/postwach/orcid.env` — gitignored; off-repo. Contains `ORCID_CLIENT_ID`, `ORCID_CLIENT_SECRET`, `ORCID_REDIRECT_URI`, `ORCID_ENVIRONMENT`, `ORCID_RECORD_HOLDER`.
- `~/.claude/projects/.../memory/project_orcid_workflow.md` — PostWach project memory entry. Records hive ownership, managed ORCiD ID, app name, scope-doc location, credential PDF path (no secret values), v1 scope summary.
- `docs/session-archives/SESSION_ARCHIVE_2026-04-29_postwach-03.md` — this archive.
- `Papers/AI_Swarm_Productivity/data/scorecards/2026-04-29-postwach-03.yaml` — productivity scorecard.

### Modified files
- `.gitignore` — added `scripts/orcid/state/` to gitignore list.
- `~/.claude/projects/.../memory/MEMORY.md` — added Open Threads entry pointing to ORCiD workflow memory file.

### ORCiD-side configuration changes (user-side)
- Added `http://127.0.0.1:8765/callback` as a second registered redirect URI for the `DocWach_ORCiD` Public API client. Existing public-page redirect URI left in place.

---

## 4. Decisions (durable)

- **D1 (operating hive).** PostWach owns the ORCiD push-only sync workflow. Capability-quality scope, biosketch generation as a future PostWach output. Not a separate hive, not user-level outside any hive.
- **D2 (direction).** Push-only for v1. CV is canonical. RIS is the canonical machine-readable feed. Bidirectional sync deferred to v2 after one full biosketch cycle.
- **D3 (record types in scope).** Works + employments + education-and-qualifications + distinctions. Funding records, peer-review claims, trusted-individual permissions out-of-scope for v1.
- **D4 (credentials).** `~/.config/postwach/orcid.env` (off-repo, gitignored, user-home). State directory at `scripts/orcid/state/` (gitignored). No secret values in committed files or memory entries.
- **D5 (corrected after scoping error).** Public API tier supports only `/authenticate` (and OpenID variants). Write scopes are gated behind Member API. Push capability cannot be delivered via the `DocWach_ORCiD` Public API client; an alternative push mechanism is required.
- **D6 (Path B as preferred push mechanism, pending).** UA is an ORCiD member; the question is whether UA has a write-direction integration researchers can use. Email sent to Ellen Dubinsky 2026-04-29. If Path B is positive, the original push-only plan resumes with UA Member credentials authorizing the push. If negative, fall back to Path A (Search & Link wizards) for DOI-bearing publications and Path C (manual web entry) for residuals.
- **D7 (read side proceeds independently).** P1 (PASS), P2, P6, P7 are read-only and can proceed at the Public API tier without waiting for Path B. P3-P5 (push) wait.
- **D8 (token longevity).** Public API `/authenticate` tokens have ~20-year lifetime. Token-renewal logic deferred since it won't be needed for years.

---

## 5. Open threads touched / opened

**Opened:**
- ORCiD Workflow (PostWach-owned). New Open Threads entry in MEMORY.md. Status: scope locked, P1 PASS, push blocked pending Path B answer.

**Touched:**
- Genesis (2026-04-28 archive). Used Top 10 RIS file and `top10_products.md` as the v1 input corpus references; scope doc cross-references both. No Genesis content modified.
- Future ontology task (HOS Capability Freshness sub-thread). ORCiD-conformant predicates noted in scope doc §7 as candidates for `portfolio-governance.ttl`. Deferred until v1 is operating.

**Not touched this session:**
- HOS + Governance Composition, HOS Capability Freshness Subsystem (parent threads, planning mode pending)
- DoD/DoW Policy Stack
- NSA ZT Alignment, Chainguard, Fort Wachs validation, INSIGHT article, NNSA Capability Transition, PD Workbench, IGNITE
- `.claude` vs `.claude-flow` Q1/Q2

---

## 6. Out-of-scope items user flagged

- Funding records, peer-review claims, trusted-individual permissions: out for v1 by user direction.
- Co-author ORCiD lookup (collaborators-list automation): different problem domain; revisit at next federal proposal cycle.
- On-publish hooks and scheduled syncs: manual command first; automation after manual is reliable.
- Future ontology task in `portfolio-governance.ttl` (GI-JOE): defer until v1 is operating.

---

## 7. Next session entry hints

- **If Ellen replies positive (Path B yes):** resume push-side phases. P3 first (Genesis Top 10), then P4 (full CV back catalog), then P5 (employments, education, distinctions). Recheck UA's required OAuth flow; UA's Member integration likely uses its own OAuth client and trusted-org delegation rather than `DocWach_ORCiD`.
- **If Ellen replies negative or non-committal (Path B no):** drive Path A (Search & Link wizards) on `orcid.org/{orcid-id}` directly. Crossref Metadata Search will find ~7 of Top 10 by author + DOI; user select-claims them. Then Path C (manual entry) for residuals: IS 2026 accepted papers (no DOI yet), SERC technical report, employments, education, distinctions including CSER 2024 Best Paper.
- **Read-side phases (independent of Path B answer):** P2 (CV → RIS converter and diff), P6 (generative pull for next biosketch RIS), P7 (drift report). All read-only at Public API tier; can proceed any time.
- **Capability-index entry.** Once push mechanism is operational, add ORCiD sync as a PostWach capability in `docs/capability-index.md`.
- **Capability-freshness link.** Once Path B/A/C is settled, the "publications missing from ORCiD" CQ candidate (scope doc §7) becomes more concrete; revisit when HOS Capability Freshness sub-thread enters build.

---

## 8. Honest session retrospective

One real scoping error that the user paid for in elapsed time: I claimed in the scope doc and in the credentials walkthrough that "ORCiD Public API + 3-legged OAuth lets you push to your own record without institutional membership." That was wrong. The Public API tier supports only `/authenticate` (and OpenID variants); write scopes require Member API. ORCiD's authorize endpoint caught the error directly with `invalid_request: one of the provided scopes is not allowed for this member`. I owned the error in-session and pivoted to the Path A/B/C decision tree, which is the right structure. The cost: the scope doc had to be partially rewritten, the auth.py SCOPES constant patched, and one bonus authorize round-trip burned. Net delay maybe 15 minutes plus credibility.

Three smaller failures, each costing ~5-10 minutes:
1. Edge launcher: shell-quoting bug (`cmd /c start ... &URL` truncated at first `&`). Should have caught this on review of the launch line; it's a textbook `cmd` gotcha.
2. Buffered stdout in background-mode Python: should have used `print(..., flush=True)` or `python -u` from the start. Caught after one wasted run.
3. Callback handler missing `Content-Length` and explicit `Connection: close`, plus diagnostic logs silenced. The user reported "continual loop"; I had no visibility into what Edge was actually requesting until I re-enabled logging.

Two procedural notes that worked: insisting on `discuss before executing` before writing the scope doc kept the user in control of decisions; the credential PDF read into context once, with the secret not echoed to chat or memory, kept handling clean. Memory hygiene held: the project memory entry references the PDF path, not the values.

Net for the user: the workflow now has a clear forward path. P1 plumbing works. The push question is parked at UA Libraries pending Ellen's reply, with Path A/C in the wings. Read-side phases are ready to advance independently. The biggest remaining risk is that Ellen's reply takes weeks; if so, the user should just pull the trigger on Path A and let UA Path B catch up later.

Lessons for next ORCiD-domain sessions:
- (a) Verify API tier permissions before writing them into a scope doc. ORCiD's docs explicitly state which scopes are gated behind Member API; should have read that before claiming Public API + OAuth allowed write.
- (b) For browser-launching subprocess calls on Windows, prefer direct executable invocation over `cmd /c start`; URL `&` and `^` characters are CMD command separators.
- (c) For Python scripts that run as background tasks, always force unbuffered stdout (`-u` flag or per-call flush) and make HTTP handlers verbose by default during initial development.
- (d) For OAuth callback HTTP handlers, always send `Content-Length` and `Connection: close` to ensure clients exit the request cleanly.
