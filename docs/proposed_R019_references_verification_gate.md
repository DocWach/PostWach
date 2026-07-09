# Proposed R019: References Verification Gate

> PROVENANCE: claude-opus-4-7[1m] (Anthropic, Claude Code CLI) authored in session 2026-06-02-postwach-04 as a session-close deliverable, on the principal's direction to plan the rule/gate update in a distinct session. Not yet adopted. Pending principal review.

## 1. Goal

Make it structurally impossible for a lab-authored manuscript to include an unverified citation. The behavioral rule (`feedback_references_triple_check`) already exists; it has been violated twice in two months under deadline pressure. This proposal adds the structural backstop: a curated approved-references store, a Byzantine-Bayesian verification protocol that is the only way refs enter the store, a slash command that exposes the protocol to the author at draft time, and a pre-render gate that aborts any render whose bibliography contains entries not in the store.

## 2. Failure modes that motivate the rule

Two confirmed incidents under the existing behavioral rule:

| Date | Manuscript | Error | Caught by |
|---|---|---|---|
| 2026-05-27 | STIDS 2026 MTA "FINAL" | 6 hard ref errors (ISO year wrong, invented OMG doc number, wrong framework attribution to Giles/Giammarco 2019, missing Dachowicz year, orphan Allen 1983, duplicate W3C/SKOS) plus formatting | Post-submission triple-check 2026-06-01 |
| 2026-06-02 | SERC SwarmEng v0.1 | 3 hard ref errors in REF 1 McDermott (title wrong "Artificial Intelligence and Future of Systems Engineering" vs correct "AI4SE and SE4AI: A Research Roadmap"; author Clifford swapped with Bone; pages 47-50 vs correct 8-14); REF 13 ruflo author "R. Cohen" not externally verifiable | Post-draft triple-check by literature-reviewer subagent same session |

Both errors are the same failure mode: **the author drafted a plausible-from-memory citation under flow, without hands-on external verification at draft time**. The behavioral rule reads at the wrong decision point (the "should I run a triple-check?" decision), not the "should I write this citation?" decision. Without structural friction, drafting fluency consistently beats the verification reflex.

## 3. Proposed rule wording

To be added to `~/.claude/CLAUDE.md` global rules block:

> **[R019] No unverified references. Manuscripts MUST cite only references that exist in the approved-references store. A reference becomes approved only by passing the Byzantine-Bayesian verification protocol (Section 5 of the R019 plan): at least three independent agents fetch reference fields from authoritative external sources and reach consensus, with per-field Bayesian posterior probability above the stated threshold. Disagreement triggers a red/blue/white debate round and re-vote; persistent disagreement requires human adjudication. Verification evidence (source URLs, verifying models, posteriors, date) is stored alongside the reference. Manuscripts whose bibliography contains any unapproved entry MUST NOT render. The author MAY use a visible `[PLACEHOLDER]` marker but MUST NOT draft a plausible-from-memory citation. @quality @research [edit] risk:critical**

The existing `feedback_references_triple_check` memory stays as the behavioral explainer of *why*; R019 is the structural *how* and *enforced via*. Both together.

## 4. Data store

Single source of truth for the portfolio. Governance owned by PostWach (CTO role); physical location is the user's OneDrive Resource Library so all hives read it via a stable absolute path. Not in any git repo — OneDrive provides versioning.

```
C:\Users\pfwac\OneDrive - University of Arizona\Documents\04 Resource Library\00 Verified References\
├── approved.bib          # BibTeX, the canonical citation data
├── manifest.yaml         # verification metadata per bibkey + defaults block
├── pending/              # candidate refs awaiting verification
└── quarantine/           # refs that failed verification, with reason
```

**Resolution (2026-06-03 postwach-02):** Location decided. Store stood up empty + skeleton; seeded with 16 single-model-triple-check entries from the SwarmEng SERC abstract pass.

### 4.1 Schema scope (cross-paper consistency)

R019 governs the **bibliography entry** only — the line that appears in a manuscript's References section. It does NOT govern: in-text annotations ("as Smith notes, …"), per-paper commentary attached to a cite ("see Table 2 for our application"), or reading notes kept adjacent to a ref in a notes file. Those stay 100% per-paper, untouched.

Two papers citing the same approved ref must match on **load-bearing fields**: authors, title, year, venue (journal or conference), volume/issue/pages, DOI/URL. Style-only punctuation, abbreviation choices, and template formatting ("Eds." vs "ed.") are house style, not verification.

### 4.2 Manifest schema

Each `manifest.yaml` entry:

```yaml
- bibkey: mcdermott2020ai4se
  verified: true
  verification_mode: byzantine-N3-tau95   # or single-model-triple-check (seed)
  verified_date: 2026-06-02
  verified_by:
    - claude-opus-4-7
    - gpt-5
    - gemini-2.5-pro
  primary_source: "10.1002/inst.12278"
  evidence_urls:
    - "https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/inst.12278"
    - "https://sercuarc.org/news/incose-insight-march-2020-special-feature-ai-and-systems-engineering/"
  per_field_posterior:
    title: 1.00
    authors: 0.99
    year: 1.00
    venue: 1.00
    volume_issue: 1.00
    pages: 0.99
    doi: 1.00
  consensus: 3/3
  confidence: high
  pending_byzantine_verification: false  # true for seed entries pre-Phase-5 backfill
  revalidate_after: null                 # ISO 8601 date; null = no expiry
  notes: ""
```

### 4.3 Software-citation fields

Software refs carry three additional fields to separate the run-of-record from upstream churn:

- `version_used` — what was actually invoked in this work (e.g., `ruflo v3.7.0-alpha.14`). Pinned, never changes after verification. The in-paper citation always renders `version_used`.
- `current_version` — what the upstream repo's latest tag reads when the entry was last checked. Informational.
- `version_checked_date` — when `current_version` was last refreshed.

### 4.4 Staleness defaults

Approved refs are not infinitely valid. URL rot, retractions, venue renames, and software releases all change the truth-content of an entry over time. Default `revalidate_after` durations (manifest top-level `defaults.staleness`, ISO 8601 durations):

| Class | Default window | Rationale |
|---|---|---|
| Peer-reviewed published | `null` (no expiry) | Wymore 1993 does not go stale. |
| Software | P6M (6 months) | Releases and renames; run-of-record may need refresh on re-use. |
| Preprint / in-press | P3M (3 months) | Page numbers, DOIs, in-press status change at publication. |
| URL-only (no DOI/ISBN) | P6M (6 months) | URL rot is the main risk. |

Per-hive optional overlay: a hive may keep a local `references/extra.bib` for refs that are domain-specific (e.g., MACQ acquisition-law cites) and not portfolio-wide. The pre-render gate checks both the portfolio store and the local overlay.

## 5. Verification protocol (Byzantine + Bayesian)

Composes three already-(b)-demonstrated capabilities from the portfolio:

1. **Tri-model review pipeline** (Claude + Codex + Gemini over shared ruflo namespace, demonstrated 2026-05-21, V1+V1.5 PASS). Used as the verification participants.
2. **TRAK Bayesian evidence aggregation pattern.** Used per-field across agent outputs to produce a posterior probability that each field is correct.
3. **Tri-model red/blue/white debate pattern** (same demonstrated capability). Used when initial vote fails consensus.

Protocol per candidate reference:

| Step | Action | Output |
|---|---|---|
| 0 | **DOI dedup pre-check.** If the candidate has a DOI and that DOI is already in `approved.bib`, return `DUPLICATE-OF-APPROVED <bibkey>` without launching verification. If the DOI matches another `pending/` entry, group them as a deduplication-needed set (Step 0a). | Early exit OR dedup-group flag |
| 0a | **Deduplication of same-DOI pending entries.** Verify the DOI's canonical metadata once via Steps 2-5. The pending entry whose fields match the canonical result becomes the survivor; the others move to `quarantine/duplicate-of-<bibkey>.md` with the verification transcript as evidence. | Survivor bibkey + list of quarantined duplicates |
| 1 | Author runs `/refverify <candidate>` (Section 6) or queues candidate via `pending/` | Verification job created |
| 2 | N independent agents (default N=3) each fetch the reference fields from at least one authoritative external source | Per-agent (field, value, source_url, claimed_confidence) tuples |
| 3 | Per-field Bayesian aggregation: prior from source-reputation table, likelihood from each agent's confidence | Per-field posterior probability |
| 4 | Byzantine consensus check: do at least ⌈2N/3⌉ agents agree on each load-bearing field (authors, title, year, venue, vol/issue/pages, DOI/URL)? | consensus vector |
| 5 | If full consensus + all posteriors ≥ τ (default τ = 0.95) | Move to `approved.bib`; commit manifest entry |
| 6 | If partial consensus or any posterior < τ | Trigger Step 7 |
| 7 | Red/blue/white debate round: red argues against candidate, blue argues for, white synthesizes. Re-vote. | New consensus vector |
| 8 | If still no consensus | Route to human adjudication; hold in `pending/` with debate transcript |
| 9 | If human rejects | Move to `quarantine/` with reason |

### 5.1 Human-attested verification path

Some legitimate references have no authoritative external source: lecture recordings, internal seminar videos, personal communications, unpublished drafts shared by colleagues, sponsor-restricted documents that can't leave a controlled environment, ephemeral web content captured pre-rot. For these, the Byzantine protocol above cannot run — there is nothing to triangulate against.

The escape hatch is `verification_mode: human-attested`. Required fields beyond the standard manifest entry:

```yaml
- bibkey: california2004wymorelecture
  verified: true
  verification_mode: human-attested
  attested_by: paulwach@arizona.edu
  attested_date: "2026-06-04"
  attestation_rationale: |
    Lecture by A. Wayne Wymore, recorded 2004 in Los Angeles. No publisher,
    no DOI, no public archive. Source: personal copy from the author's
    estate. External verification is not possible; cite is valid because
    the recording itself is the primary source.
  evidence_local: "Z99 VT Archive/.../Wymore_Lecture_2004.mp4"
  pending_byzantine_verification: false
```

Required to qualify:

- The ref-type plausibly has no external source (video, internal lecture, personal communication, unpublished work, sponsor-restricted, ephemeral web).
- `attestation_rationale` explains *specifically* why external verification is not possible. "I think it's right" is not sufficient. A generic "no DOI available" is not sufficient.
- `attested_by` is a real human, named. The drafting agent CANNOT self-attest.
- `evidence_local` (optional) points at a local copy of the source if one exists, so future sessions can re-validate against the same artifact.

What this mode does NOT permit:

- Bypassing verification for refs that DO have an authoritative external source. If a journal article is paywalled, that's not human-attested grounds — the publisher page still exists.
- Self-citing without attestation: a Wach et al. in-press paper is `single-model-triple-check` + the principal's confirmation that it's in-press; not human-attested.
- Speed-running verification to clear the pending backlog. The mode is for genuinely unverifiable refs; misuse defeats R019.

Human-attested entries are NOT subject to `pending_byzantine_verification: true` because there is nothing to upgrade to. They remain `human-attested` permanently, with their attestation rationale on file.

**Default parameters:** N=3, τ=0.95, ⌈2N/3⌉=2 (so unanimity not required, but supermajority is). Starting values calibrated to "expensive enough that bad refs don't slip through, cheap enough to not block drafting." Revisit after Phase 3 backfill experience.

**Authoritative source allowlist** (initial; extend as needed):

- Publisher pages: Wiley, Springer, IEEE Xplore, ACM Digital Library, MIT Press, Elsevier ScienceDirect, MDPI, IOS Press
- DOI registries: doi.org, CrossRef API
- Standards bodies: W3C TR archive, ISO catalogue, IEC, IEEE Standards, ITU
- Specs/specs-as-code: OMG specs page, OASIS, ETSI
- Community archives: AAAI archive, ACL anthology, CEUR-WS, arXiv (only for venues where arXiv is the published form)
- Code/software: GitHub release pages (for software cites with explicit version tags)

**NOT authoritative:** Google Scholar profile pages, Wikipedia, ResearchGate full-text without publisher cross-check, random PDFs, blog posts, social media.

## 6. New slash command (proposed)

The principal suggested a slash-command interface so the rule is exposed where the author actually works (drafting). Proposed command:

**`/refverify <citation-string-or-bibkey>`**

Behavior:

1. Parses the citation string (e.g., "McDermott et al. 2020 INSIGHT") or looks up the bibkey if already in `pending/`.
2. **DOI dedup pre-check** (Step 0 from §5): if the candidate has a DOI already in `approved.bib`, return `DUPLICATE-OF-APPROVED <bibkey>` immediately without running verification. If the DOI matches another `pending/` entry, run dedup-of-same-DOI (Step 0a) to identify the canonical survivor.
3. Otherwise runs the Byzantine-Bayesian protocol (Section 5) end-to-end with sane defaults.
4. Reports per-field decision, posterior probabilities, source URLs used, consensus vector.
5. On APPROVED: commits to `approved.bib` + `manifest.yaml`, returns the formatted IEEE citation string ready for paste.
6. On DISAGREEMENT: returns the debate transcript and asks the author whether to human-adjudicate or re-run with different sources.
7. On REJECTION: returns the reason and recommended alternative ref if one was identified during search.
8. On NO-EXTERNAL-SOURCE (the ref-type plausibly has no authoritative external source — see §5.1): refuses to mark `verified: true` autonomously and prompts the human author for `verification_mode: human-attested` with the required `attestation_rationale` text. The agent cannot self-attest.

### 6.1 Trigger authority

**Both the human author and the drafting agent (Claude in a session) may trigger `/refverify`.** The autonomous-trigger boundary is "about to write a citation," not "merely encountered a citation in source material":

- When the agent is reading source material that contains citations, do nothing. Reading is not citing.
- When the agent is about to **emit** a citation in a draft manuscript or other deliverable, the path is: prefer `/reflookup` first to reuse an approved entry; if no match, drop a visible `[PLACEHOLDER]` and queue verification, OR trigger `/refverify` inline.
- `[PLACEHOLDER]` is the explicit escape hatch during flow. Batched verification at end-of-section or end-of-draft is fine.

This dual-trigger avoids the cost of the agent firing verification rounds on every citation-shaped string it sees, while preserving the structural guarantee that no plausible-from-memory citation reaches a render.

**Companion commands:**

- **`/reflookup <topic-or-snippet>`** — search `approved.bib` for already-verified references matching a topic, so the author can prefer reuse over re-verification.
- **`/refcheck <manuscript-path>`** — run the pre-render gate against an arbitrary manuscript, return per-cite verdicts. This is the same logic that the structural gate (Section 7) runs at render time, exposed standalone for author convenience.

## 7. Render gate

Implementation is `01 PostWach/scripts/refcheck.py` (Python; portable across Windows / macOS / Linux). Thin shell wrappers `refcheck.sh` (bash) and `refcheck.ps1` (PowerShell) live alongside and forward arguments. Callable from any hive via stable absolute path.

```
refcheck.py <manuscript.md> [--portfolio-store=<path>] [--local-store=<path>] [--strict|--advisory] [--autoverify] [--bibkey-mode]
```

Behavior:

1. Extract every in-text `[Author, Year]` cite key from the manuscript.
2. Extract every numbered bibliography entry.
3. Look up every cite key against `approved.bib` (portfolio store + optional local overlay).
4. On any miss:
   - Default (`--strict` without `--autoverify`): print the offending cite key + the line it appears on; exit non-zero. **Do NOT auto-launch `/refverify`.** Rationale: gate failures are common during drafting, auto-verification on every miss is expensive, and the author often wants to see what's missing and decide (delete the cite? reuse an approved equivalent? add a `[PLACEHOLDER]`?).
   - With `--autoverify`: same as default, then auto-launch `/refverify` on each missing entry. Opt-in for the author who explicitly wants the gate-and-verify combo in one shot.
   - With `--advisory`: exit 0 with warnings only (used at every-save tier).

Wire into the existing `ontology-gate.sh` two-tier pattern (GI-JOE): advisory tier on every save, blocking tier on `pandoc`/`xelatex` invocation. The pandoc wrapper (e.g., a `make-pdf.sh` script) calls `refcheck.sh --strict` before invoking pandoc. Non-zero exit aborts the render with the failing cite keys shown.

## 8. Implementation phases

| Phase | Scope | Deliverable | Effort estimate |
|---|---|---|---|
| 1 | Stand up the data store | `04 Resource Library/00 Verified References/{approved.bib, manifest.yaml, pending/, quarantine/}` seeded with the 16 SwarmEng v0.3 verified refs (single-model-triple-check mode) | ~30 min — **DONE 2026-06-03** |
| 2 | Adopt R019 globally | Edit `~/.claude/CLAUDE.md`; cross-link `feedback_references_triple_check.md` to R019 | ~15 min |
| 3 | Backfill in-flight manuscripts | Run the verification protocol on AICB v0.6 refs, STOIC v0.5 refs, AI4RE_SLR refs, MOACRA refs. Push verified entries into `approved.bib`. Quarantine the rest. | ~2-4 hr (depending on automation) |
| 4 | Build `refcheck.sh` | The gate script + integration with a `make-pdf.sh` pandoc wrapper. Two-tier advisory/blocking. | ~1-2 hr |
| 5 | Build `/refverify` command | Slash command that invokes the tri-model protocol. Initially could be a thin wrapper around the existing tri-model review pipeline. | ~2-4 hr |
| 6 | Build `/reflookup` and `/refcheck` companion commands | Quality-of-life entry points. | ~1 hr each |
| 7 | Cross-portfolio rollout | Run gate against every paper in every hive's repo, surface ref-quarantine reports, prioritize cleanup. | rolling |

Total to operational: roughly half a day for Phases 1-2, then ~1-2 days for Phases 3-5 staged across a week.

## 9. Acceptance criteria

R019 is operational when all of the following hold:

- [x] `approved.bib` + `manifest.yaml` exist and are populated with at least the SwarmEng v0.3 refs (**16 entries seeded 2026-06-03**, single-model-triple-check mode; pending Byzantine N=3 upgrade in Phase 5).
- [x] R019 is in `~/.claude/CLAUDE.md` (**added 2026-06-03**). Per-hive CLAUDE.md cross-references TBD across the 9 V3 hives.
- [x] `refcheck.py` (with `refcheck.sh` / `refcheck.ps1` wrappers) exists, runs against any markdown manuscript, returns correct verdicts, exits non-zero on missed cites (**built 2026-06-03**; tested 16/16 PASS on SwarmEng v0.3 References_Bios.md and 2-MISS + 1-??? on a deliberately-broken fixture).
- [ ] `/refverify`, `/reflookup`, `/refcheck` slash commands exist and produce the documented output (**Phase 5**, pending).
- [x] At least one manuscript has been rendered through the gate end-to-end and the gate rejected an intentional bad-cite test case (**done 2026-06-03**, broken fixture rejected with exit code 1).
- [x] `feedback_references_triple_check.md` is updated to reference R019 as the structural backstop (**done 2026-06-03**).

**Status as of 2026-06-03 postwach-02:** 5 of 6 acceptance criteria met. R019 is enforceable today via `refcheck.py` invoked from a pandoc-wrapper script. The slash-command surface (`/refverify` etc.) is the remaining work to make verification ergonomic for the author during drafting.

**Status as of 2026-06-04 (continuation):** 6 of 6 acceptance criteria met. `/refcheck`, `/reflookup`, `/refverify` slash commands shipped (MVP) under `01 PostWach/.claude/skills/`. End-to-end test: `@wach2022pairing` promoted from `pending/` to `approved.bib` via `refverify.py --promote` (DOI 10.1002/inst.12414 verified against Wiley publisher page, MATCH-WITH-ENRICHMENT verdict, manifest entry written). All 9 V3 hive CLAUDE.md files carry a cross-reference to R019. Matcher refinements landed (multi-author + editor + alias indexing; title-keyword tiebreak; unicode-hyphen + smart-quote normalization), with `refcheck.py` now returning 16/16 on the SwarmEng v0.3 reference list. `--list-stale` and `--refresh` verbs added to `refverify.py` for software-version revalidation. **R019 is operational.**

## 10. Resolutions (2026-06-03 postwach-02)

The seven open questions from the original draft were resolved with the principal in session postwach-02. Resolutions captured below; full discussion in `docs/session-archives/SESSION_ARCHIVE_2026-06-03_postwach-02.md` §2.

| Q | Topic | Resolution |
|---|---|---|
| Q1 | Where does the data store live? | **`04 Resource Library/00 Verified References/`** (OneDrive-direct, NOT in any git repo; OneDrive provides version history; cross-hive access via stable absolute path). Phase 1 standup **DONE 2026-06-03**. |
| Q2 | N and τ defaults | Keep **N=3, τ=0.95** provisionally. Revisit after Phase 3 backfill experience. Rationale (recorded for future tuning): N=3 because ⌈2N/3⌉=2 is the smallest Byzantine supermajority that survives one disagreement. τ=0.95 calibrated to "expensive enough that bad refs don't slip through, cheap enough to not block drafting." |
| Q3 | Trigger authority | **Both** (human and autonomous agent). Autonomous trigger fires only "about to write," not "encountered." `[PLACEHOLDER]` is the escape hatch during flow; batched verification at end-of-section or end-of-draft is fine. See §6.1. |
| Q4 | Software citation versioning | **Three fields**: `version_used` (pinned, never changes), `current_version` (informational, refreshed on revalidation), `version_checked_date`. In-paper cite always uses `version_used`. See §4.3. |
| Q5 | Cross-paper consistency | **Load-bearing fields only.** R019 governs the bibliography entry; in-text annotations, per-paper commentary, and reading notes are untouched. Style-only punctuation/abbreviations are house style, not verification. See §4.1. |
| Q6 | Staleness / `revalidate_after` | **Class-specific defaults**: peer-reviewed = null (no expiry); software = 6 months; preprint/in-press = 3 months; URL-only = 6 months. ISO 8601 durations. See §4.4. |
| Q7 | Render-gate failure default | **Abort + report; do NOT auto-verify.** Reasons: gate failures common during drafting, auto-verify expensive, author often wants to see what's missing and decide. Opt-in via `--autoverify` flag for the explicit gate-and-verify combo. See §7. |

## 11. Future open questions

0. *(Resolved 2026-06-04 postwach-02 cont.) DOI dedup pre-check + human-attested mode.* Folded into §5 (Step 0/0a) and §5.1, and into the `/refverify` behavior in §6. The 13 internal-duplicate DOIs in the EndNote import are now first-class cases the protocol handles. The Wymore lecture and similar source-less refs have an explicit attestation path with human-author requirement and rationale field.

1. **Per-hive overlay store discipline.** When (if ever) should a hive's `references/extra.bib` overlay be elevated into the portfolio `approved.bib`? Initial guess: when a domain-specific ref is cited by 2+ hives. Needs Phase 3 backfill data to calibrate.
2. **Byzantine seed-entry upgrade scheduling.** The 16 seed entries are single-model-triple-check. Phase 5 backfill upgrades them to byzantine-N3-tau95. Should the upgrade run all-at-once or rolling? Cost vs disruption tradeoff.
3. **Out-of-band reference additions.** If the user manually drops a `.bib` entry into `approved.bib` (e.g., from EndNote XML import), does it count as approved? Initial proposal: no — manual drops land in `pending/` first and must pass `/refverify`. The EndNote v2.enl import is the immediate test case.
4. **Slash-command implementation venue.** Thin wrapper around existing tri-model review pipeline? New Claude Code skill? Both? Decide before Phase 5.
5. **What happens when an approved ref is later corrected.** A v2 of an entry replaces v1; what about manuscripts that already cite v1? Initial proposal: every render runs `refcheck.sh` against the current `approved.bib`, so stale-but-still-approved citations get refreshed at next render. Bigger question: should retraction trigger a portfolio-wide scan + warning?
6. **Retraction Watch integration.** Out of scope per Appendix B but flagged for Phase 7+. Worth revisiting once Phase 1-5 are operational.
7. **Sponsor-restricted refs (e.g., WRT-2406 RESTRICTED).** Should refs to restricted material live in the portfolio store at all, or in a separate access-controlled overlay? Defer until first such ref is needed.

---

## Appendix A: Mapping to existing demonstrated capabilities

| Component | Existing capability | R016 status |
|---|---|---|
| Tri-model verification | Tri-model review pipeline (Claude+Codex+Gemini over shared ruflo) | (b) demonstrated 2026-05-21, V1+V1.5 PASS |
| Bayesian aggregation | TRAK evidence + confidence pattern | (b) demonstrated (per memory project_trak.md) |
| Red/blue/white debate | Tri-model red/blue/white pattern | (b) demonstrated 2026-05-21 |
| Two-tier gate | `ontology-gate.sh` (advisory + blocking) in GI-JOE | (b) demonstrated portfolio governance D4 |
| Slash command exposure | Claude Code skills pattern | Standard mechanism |

R019 is a composition of existing demonstrated capabilities, not a new invention. This is the intended cost profile.

## Appendix B: Out-of-scope for this proposal

- The rule for figures (no equivalent failure mode logged yet; not in this proposal).
- The rule for software/data versions beyond the citation case (separate concern).
- Cross-paper editorial-style enforcement (Chicago vs IEEE; not a verification problem).
- Automated retraction-watch (Retraction Watch API integration; future enhancement).
