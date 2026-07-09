---
name: refverify
description: Single-model triple-check workflow that verifies a candidate citation against authoritative external sources and promotes it from pending/ to approved.bib. MVP scope; full Byzantine N=3 is Phase 5b future work.
---

# /refverify

The R019 verification entry point. Given a candidate citation, this skill runs Step 0 (DOI dedup), then drives the single-model triple-check workflow: the agent fetches canonical fields from authoritative external sources via WebSearch + WebFetch, the supporting script compares them to the claimed fields, and on MATCH the candidate is promoted.

**Integration status (R016):** (a) research artifact. Built 2026-06-04; not yet used end-to-end on a real new citation. Promote to (b) demonstrated after first end-to-end verify of a non-trivial ref.

---

## MVP vs Full Byzantine Boundary

The R019 proposal (§5) specifies a full Byzantine N=3 protocol: three independent foundation models (Claude + Codex + Gemini), per-field Bayesian aggregation, ⌈2N/3⌉ supermajority consensus, and red/blue/white debate on disagreement. That orchestration requires the tri-model review pipeline ("Tri_model_review", (b) demonstrated 2026-05-21) wired into this skill.

**This skill is the MVP only.** It implements:

1. Step 0 / 0a — DOI dedup pre-check against approved + pending stores.
2. Single-model triple-check — one foundation model (the agent running this session) fetches canonical fields and the script compares them.
3. Human-attested path — for refs with no external source (lectures, personal communications, sponsor-restricted), gated on a real human in `--attested-by`.

**The full Byzantine N=3 protocol is Phase 5b.** It needs:

- Orchestration of two additional independent agents (Codex + Gemini) through the shared ruflo namespace.
- Per-field Bayesian aggregation logic (TRAK pattern reuse).
- Red/blue/white debate round on disagreement.
- Storage of per-field posteriors in the manifest entry.

Until Phase 5b is built, all entries promoted via this skill carry `verification_mode: single-model-triple-check` and `pending_byzantine_verification: true` per the R019 manifest schema.

---

## When to Use This Skill

Invoke `/refverify` when:

- `/reflookup` returned no APPROVED matches, only PENDING matches, or no matches at all.
- `/refcheck` failed with a MISS and the agent needs to verify the missing entry before re-running the gate.
- A human ratification is required for a ref with no external source (lecture, personal communication, in-press paper).

Do NOT invoke `/refverify`:

- On a reference that `/reflookup` already returned as APPROVED. Reuse the bibkey instead.
- Speculatively, before any drafting need. Verification is expensive.
- For refs you have no plan to cite. The verification queue is not a bookmark folder.

---

## What the Agent Does vs What the Script Does

### Agent responsibilities (in-session, before invoking the script)

1. **Identify the candidate.** Either a bibkey already in `pending/imported_from_endnote.bib`, or a fresh candidate (author + year + title + ideally DOI).
2. **Fetch canonical fields from authoritative external sources.** Use WebSearch + WebFetch against the R019 allowlist (§5):
   - Publisher pages: Wiley, Springer, IEEE Xplore, ACM Digital Library, MIT Press, Elsevier ScienceDirect, MDPI, IOS Press.
   - DOI registries: doi.org, CrossRef.
   - Standards bodies: W3C TR, ISO catalogue, IEEE Standards, IEC, ITU.
   - Specs: OMG specs page, OASIS, ETSI.
   - Community archives: AAAI, ACL anthology, CEUR-WS, arXiv (only where arXiv is the published form).
   - Software: GitHub release pages (for software cites with version tags).
   - **NOT authoritative:** Google Scholar profile pages, Wikipedia, ResearchGate full-text without publisher cross-check, blog posts, social media.
3. **Triangulate.** "Triple-check" means three independent reads of the same canonical source (or three corroborating authoritative sources). The agent is responsible for this discipline; the script trusts what it is fed.
4. **Pass results to the script** via `--field key=value` flags (repeatable) or `--evidence-json <path>` for a JSON file with `{"fields": {...}, "evidence_urls": [...]}`.

### Script responsibilities (`01 PostWach/scripts/refverify.py`)

1. **Step 0 / 0a — DOI dedup pre-check.** If the candidate DOI is already in `approved.bib`, return `DUPLICATE-OF-APPROVED` and exit 0. If the DOI matches multiple pending entries, flag `DEDUP-NEEDED-IN-PENDING` and require `--candidate-bibkey` (the prospective survivor).
2. **Field comparison.** Compare the agent-supplied canonical fields against the candidate's claimed fields for each load-bearing field (author, title, year, journal/booktitle, volume, number, pages, doi, url).
3. **Verdict.**
   - **MATCH** — all compared fields agree.
   - **MISMATCH** — at least one field differs; promote blocked (exit 9).
   - **NO-EXTERNAL-SOURCE** — when invoked with `--no-external-source`, prints the human-attested invocation pattern and exits 6.
4. **On MATCH + `--promote`** — append the candidate's bib entry to `approved.bib`, append a manifest entry with `verification_mode: single-model-triple-check`, evidence URLs, and `pending_byzantine_verification: true`.
5. **On dedup-survivor + `--promote`** — quarantine the loser pending entries into `quarantine/duplicate-of-<bibkey>--<loser>.md`.

The script does NOT fetch from the web. The script does NOT decide which sources are authoritative. Those are the agent's job.

---

## Step 0 Always Runs First and May Short-Circuit Everything

This is load-bearing. The DOI dedup pre-check runs before any field comparison. If the candidate DOI is already approved, the right answer is "reuse the existing bibkey," not "run a new verification." Most candidate refs encountered during a typical drafting session are duplicates of something already in the store; Step 0 cheaply catches that case and avoids burning verification effort.

The agent should:

- Always pass `--candidate-doi <doi>` if a DOI is known (or set it as a `doi` field in the candidate bib).
- Treat the Step 0 short-circuit as final. Do not re-run with `--no-external-source` to bypass it.

---

## How to Invoke

The script is at `01 PostWach/scripts/refverify.py`. Python stdlib only.

### Pattern 1: DOI dedup pre-check (cheapest, run first)

```bash
python ".../scripts/refverify.py" --candidate-doi 10.1002/inst.12278
# Exit 0 + "DUPLICATE-OF-APPROVED @mcdermott2020ai4se" -> reuse the approved bibkey.
```

### Pattern 2: Verify a pending entry (the common case for backfill)

```bash
# Step A: agent fetches canonical fields via WebSearch + WebFetch.
# Step B: dry-run comparison.
python ".../scripts/refverify.py" \
  --candidate-bibkey tzafestas1993expert \
  --field title="Expert Systems in Engineering Applications" \
  --field year=1993 \
  --field publisher="Springer" \
  --evidence-url "https://link.springer.com/book/10.1007/978-3-642-84048-7"

# Step C: if MATCH, re-run with --promote.
python ".../scripts/refverify.py" \
  --candidate-bibkey tzafestas1993expert \
  --field title="Expert Systems in Engineering Applications" \
  --field year=1993 \
  --evidence-url "https://link.springer.com/book/10.1007/978-3-642-84048-7" \
  --primary-source "10.1007/978-3-642-84048-7" \
  --confidence high \
  --notes "Verified via Springer book page. WebFetch returned canonical title with title-case." \
  --promote
```

### Pattern 3: Verify a brand-new candidate (not yet in pending/)

```bash
# Agent constructs a small one-entry .bib file at /tmp/cand.bib and passes it in.
python ".../scripts/refverify.py" \
  --candidate-bibkey newauthor2026paper \
  --candidate-bib /tmp/cand.bib \
  --field title="..." --field year=2026 --field journal="..." \
  --evidence-url "https://..." \
  --promote
```

### Pattern 4: Same-DOI dedup in pending

```bash
# When two pending entries share a DOI, designate the survivor with --candidate-bibkey.
python ".../scripts/refverify.py" \
  --candidate-doi 10.1002/sys.21477 \
  --candidate-bibkey giles2019swarm \
  --field title="A Mission-Based Architecture for Swarm Unmanned Systems" \
  --field year=2019 \
  --evidence-url "https://incose.onlinelibrary.wiley.com/doi/10.1002/sys.21477" \
  --promote
# Losers in the same-DOI set go to quarantine/duplicate-of-giles2019swarm--<loser>.md
```

### Pattern 5: Human-attested (refs with no external source)

```bash
# Agent surfaces the candidate and recommends attestation:
python ".../scripts/refverify.py" \
  --candidate-bibkey california2004wymorelecture \
  --no-external-source
# Exit 6 + instructions for the --attest path.

# Then a HUMAN runs (not the agent):
python ".../scripts/refverify.py" \
  --candidate-bibkey california2004wymorelecture \
  --candidate-bib /path/to/cand.bib \
  --attest \
  --attested-by paulwach@arizona.edu \
  --attestation-rationale "Lecture by A. Wayne Wymore recorded 2004 in Los Angeles. No publisher, no DOI, no public archive. Source: personal copy from the author's estate. External verification is not possible." \
  --attestation-evidence-local "Z99 VT Archive/.../Wymore_Lecture_2004.mp4" \
  --promote
```

The script rejects `--attested-by` values that look like agent identifiers (`claude`, `gpt`, `gemini`, `codex`, `agent`, `bot`, `sonnet`, `opus`). Agents cannot self-attest. Per R019 §5.1, attestation requires a real, named human.

---

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success (DUPLICATE-OF-APPROVED, dry-run MATCH, or promoted). |
| 3 | Candidate bibkey not found in any store. |
| 4 | `--attest` invoked without `--attested-by`/`--attestation-rationale`, or with an agent-shaped attester. |
| 5 | `DEDUP-NEEDED-IN-PENDING` but no valid `--candidate-bibkey` provided. |
| 6 | `--no-external-source` set; agent must route to attestation path. |
| 7 | No canonical fields supplied; agent must fetch externally first. |
| 8 | INDETERMINATE — no overlapping fields between candidate and canonical. |
| 9 | MISMATCH — at least one load-bearing field differs. |
| 10 | `--promote` requested without `--candidate-bibkey`. |

---

## What the Agent MUST NOT Do

1. **Never self-attest.** The script blocks this, but the agent should not even attempt to pass its own model name as `--attested-by`.
2. **Never bypass Step 0.** If a DOI is known, pass it. Step 0 is cheap and authoritative.
3. **Never `--promote` without first running a dry-run.** Promotion writes to the canonical store. Confirm MATCH first, then promote.
4. **Never invent canonical fields.** If WebFetch fails or paywalls block access, document the gap in `--notes`, drop confidence to `medium`, and surface to the principal — do not paper over with plausible-from-memory values.
5. **Never use a non-allowlist source as `--evidence-url`.** Google Scholar profile pages, Wikipedia, ResearchGate (without publisher cross-check), blogs, and social media are not authoritative per R019 §5.

---

## Open Design Questions (Punted to Phase 5b)

1. **Byzantine N=3 orchestration.** How is the tri-model review pipeline invoked from inside this skill? Likely a subprocess that talks to the shared ruflo namespace.
2. **Bayesian per-field posterior storage.** Manifest schema already has the `per_field_posterior` field but this MVP doesn't populate it. Phase 5b fills it from the aggregation step.
3. **Red/blue/white debate transcript.** Where does the transcript live when consensus fails? Initial guess: `pending/<bibkey>--debate.md`.
4. **Allowlist enforcement.** The script currently trusts `--evidence-url` values. Phase 5b should validate against an allowlist parsed from the R019 proposal or a config file.
5. **Concurrent-modification of approved.bib.** If two sessions promote simultaneously, the naive `read + append + write` in this script races. OneDrive's lock is best-effort. Phase 5b should adopt a file lock or sentinel pattern.
6. **Software version refresh.** R019 §4.3 introduces `version_used` / `current_version` / `version_checked_date`. The current `--field` mechanism can carry these, but there is no logic for "refresh `current_version` on a stale entry." Phase 5b adds a `--refresh-software` mode.

---

## Related Skills

- `/reflookup` — Search BEFORE invoking `/refverify`. If `/reflookup` finds an APPROVED match, no verification is needed.
- `/refcheck` — Pre-render gate; uses the store that `/refverify` populates.

## References

- `docs/proposed_R019_references_verification_gate.md` §5 (protocol), §5.1 (human-attested), §6 (slash command spec), §6.1 (trigger authority)
- `~/.claude/CLAUDE.md` [R019]
- `memory/feedback_references_triple_check.md`
- `memory/project_tri_model_review.md` (the (b)-demonstrated tri-model pipeline that Phase 5b will integrate)
