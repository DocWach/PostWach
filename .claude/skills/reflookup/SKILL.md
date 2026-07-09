---
name: reflookup
description: Search the portfolio approved + pending reference stores before drafting any citation. Prefer reuse of an existing approved entry over running /refverify on something new.
---

# /reflookup

The "look before you draft" companion to R019. Invoked BEFORE writing a citation, so the agent doesn't draft a plausible-from-memory cite (the failure mode R019 exists to prevent).

**Integration status (R016):** (a) research artifact. Built 2026-06-04; not yet used end-to-end on a real drafting session. Promote to (b) demonstrated after first use.

---

## When to Use This Skill

Invoke `/reflookup` whenever the drafting agent is **about to emit** a citation in a manuscript or other deliverable, and at least one of these is true:

- You have an author surname and an approximate year in mind ("McDermott et al. 2020").
- You have a topic in your head ("the AI4SE/SE4AI roadmap paper").
- You have a DOI from external context (a URL, a paper you just fetched).
- You have a partial title.

Per R019 §6.1, the trigger is "about to write a citation." Do NOT trigger on:

- Reading source material that contains citations (reading is not citing).
- Internal scratch notes that will not be rendered.

---

## How to Invoke

The script lives at:

```
01 PostWach/scripts/reflookup.py
```

Invoke via `Bash` (Python stdlib only, no install step):

```bash
python "C:/Users/pfwac/OneDrive - University of Arizona/Documents/03 Projects/00_Hive_Empire/01 Hives/01 PostWach/scripts/reflookup.py" \
  <query terms...>
```

### Search modalities

| Modality | Example | Notes |
|---|---|---|
| Free text | `python reflookup.py mission engineering ontology` | Substring search across title + author + journal + keywords + abstract + bibkey. |
| Author + year | `python reflookup.py --author McDermott --year 2020` | High-precision exact-match scoring boost. |
| DOI exact | `python reflookup.py --doi 10.1002/inst.12278` | Short-circuits to top of results if matched. |
| Keyword (exact field) | `python reflookup.py --keyword "BFO"` | Matches against the `keywords =` bib field. |
| Bare year in query | `python reflookup.py Maier 1998 sos` | Year auto-detected from query terms. |
| Bare DOI in query | `python reflookup.py 10.1145/182.358434` | DOI auto-detected from query terms. |
| Approved-only | `python reflookup.py --approved-only mission engineering` | Skip the 1500+ pending pool when only verified entries are useful. |

### Flags

- `--max-results N` — Cap results (default 10).
- `--approved-store <path>` / `--pending-store <path>` — Override default OneDrive store paths (rarely needed).

---

## How to Read the Result

Output is a ranked list of candidates. Each candidate has:

```
  [APPROVED] @mcdermott2020ai4se
             McDermott 2020 | "AI4SE and SE4AI: A Research Roadmap" | [INSIGHT]
             score=575 hits=author+year,title~ai4se,bibkey~mcdermott...

  [PENDING ] @endnote_imported_smith2021
             Smith 2021 | "Some related title" | [Some Journal]
             score=45 hits=title~mission...
```

Status:

- **APPROVED** — In `approved.bib`. **Use this bibkey directly in your draft. No further action needed.**
- **PENDING** — In `pending/imported_from_endnote.bib`. **Cannot be used as-is.** Run `/refverify <bibkey>` to promote it to approved first.

Exit codes:

- **0** — At least one match found.
- **2** — No matches. The ref is new. Next step is `/refverify` (which will first run the DOI dedup pre-check, then the single-model triple-check workflow).

---

## What the Agent MUST Do With the Result

1. **APPROVED match exists with high confidence** (clear author+year hit, or DOI exact): **Reuse it.** Drop the `@bibkey` into the manuscript. Done. Do NOT re-verify.
2. **APPROVED match exists but ambiguous** (multiple candidates, none obviously dominant): Surface the candidates to the principal or inspect each via the bib record. Pick one or escalate. Do NOT autonomously pick a low-confidence match.
3. **Only PENDING matches**: Surface them, flag that `/refverify` is needed to promote, do NOT cite them yet. Either route through `/refverify` now or drop a `[PLACEHOLDER]` and batch verification at end-of-section.
4. **No matches**: The ref is new. Either invoke `/refverify` inline, or drop a `[PLACEHOLDER]` with enough author/year/topic detail to make verification feasible later.
5. **Never** invent a citation because `/reflookup` returned nothing. That is exactly the failure mode R019 exists to prevent.

---

## Examples

### Topic search

```bash
python ".../scripts/reflookup.py" mission engineering ontology
# Returns approved + pending matches ranked by token-overlap score
```

### Verify a memory-based cite

```bash
python ".../scripts/reflookup.py" --author Maier --year 1998
# Returns maier1998sos if approved
```

### DOI lookup before citing

```bash
python ".../scripts/reflookup.py" --doi 10.1002/sys.21477
# Returns @giles2019swarm if approved; otherwise no match -> /refverify
```

### Reuse-or-verify decision

```bash
# Step 1: lookup
python ".../scripts/reflookup.py" --author Wymore --year 1993
# -> [APPROVED] @wymore1993mbse: reuse this bibkey, do NOT cite from memory.

# Step 1 (no-match case):
python ".../scripts/reflookup.py" --author Brand-New-Author --year 2025
# -> No matches.
# Step 2: /refverify Brand-New-Author 2025 "title fragment"
```

---

## Related Skills

- `/refverify` — Run the single-model triple-check workflow on a candidate that `/reflookup` did not find (or that returned only PENDING entries).
- `/refcheck` — Pre-render gate; checks an entire manuscript at once, not individual cites.

## References

- `docs/proposed_R019_references_verification_gate.md` §6 (companion commands)
- `~/.claude/CLAUDE.md` [R019]
