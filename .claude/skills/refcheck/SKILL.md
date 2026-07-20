---
name: refcheck
description: Run the R019 pre-render reference gate against a manuscript before pandoc/xelatex. Fails the render if any cite is not in the approved-references store.
---

# /refcheck

Thin wrapper around `01 PostWach/scripts/refcheck.py`. This skill exposes the R019 render gate to the drafting agent and enforces the "no unverified citations leave the lab" rule at the structural decision point (immediately before render).

**Integration status (R016):** (b) demonstrated. The underlying `refcheck.py` is tested and was used 2026-06-03 to catch real misses on the SwarmEng v0.3 fixture. The wrapping skill itself is new but adds no logic.

---

## When to Use This Skill

Invoke `/refcheck` BEFORE any of the following:

- Running `pandoc` on a manuscript that has a `## References` section or `@bibkey` cites.
- Running `xelatex` / `latexmk` on a `.tex` produced from such a manuscript.
- Producing a `.pdf` / `.docx` deliverable that will leave the lab (submission, sharing, sponsor handoff).
- Calling any wrapper script that ends in `make-pdf.sh`, `build-pdf.ps1`, or similar.

Do NOT invoke `/refcheck` on:

- Reading source material (reading is not citing — see R019 §6.1).
- Manuscripts that have no References section yet (drafting phase before citations are added).
- Internal scratch markdown (notes, session logs) that will not be rendered.

---

## How to Invoke

The script lives at an absolute path under the PostWach hive. Invoke it directly via `Bash`:

```bash
python "C:/Users/pfwac/OneDrive - University of Arizona/Documents/03 Projects/00_Hive_Empire/01 Hives/01 PostWach/scripts/refcheck.py" \
  "<absolute-path-to-manuscript.md>" \
  --strict
```

The default `--portfolio-store` points at the OneDrive `00 Verified References/approved.bib` — no need to pass it explicitly unless you're testing against a fixture.

### Flags the agent should know about

| Flag | When to pass |
|---|---|
| `--strict` (default) | Production. Exits non-zero on any MISS. Use before render. |
| `--advisory` | Drafting-time spot check. Exits 0; prints warnings only. |
| `--local-store <path>` | When a hive carries a domain-specific `extra.bib` overlay (per R019 §4.4). |
| `--include-pending` | Surfaces pending entries (PENDING status) so the author can see what's verifiable-but-not-yet-promoted. Pending matches do NOT cause a non-zero exit even under `--strict`. Probe the script's `--help` before assuming this flag exists — see below. |
| `--bibkey-mode` | Force pandoc `@bibkey` extraction (rather than IEEE numbered bibliography). Usually auto-detected. |
| `--latex` | Force LaTeX `\cite` + BibTeX mode. **Auto-detected for `.tex` manuscripts.** |
| `--refs-bib <path>` | Path to the manuscript's local `.bib` for LaTeX mode. Auto-detected from `\bibliography{}` / `\addbibresource{}` if omitted. |

**LaTeX mode (added 2026-07-15).** For a `.tex` manuscript, refcheck extracts every `\cite`-family key, resolves each through the local `references.bib` (located via `\bibliography{}`), and matches author/year against the approved store. Verdicts: **OK** (approved), **MISS** (cited but not in the approved store, route via `/refverify`), **UNDEF** (key not in the local `.bib` at all, an undefined citation that will break the LaTeX build, add the approved entry to `references.bib`). This is the correct gate for the LaTeX+BibTeX manuscripts under `02 My Outreach/2026 - Dis Pub/`; do NOT run the markdown/numbered modes on them (they find no bibliography and exit 0 vacuously, a false pass).

**Word (`.docx`) and PDF (`.pdf`) modes (added 2026-07-15).** Auto-detected by extension. Both extract the *rendered* reference list (docx via stdlib zip/XML, one paragraph per entry, with a fallback for heading-less pandoc bibliographies; PDF best-effort via `pypdf` / `pdfminer` / poppler `pdftotext`) and match author-year against the approved store, trying every capitalized name-token per entry so both `Wach, P.` and `Paul Wach` resolve. **Word is a real gate** for source-less Word deliverables (SBIR volumes, INSIGHT articles). **PDF is always advisory (never blocks), even under `--strict`.** Caveat: rendered-bibliography matching is fuzzier than the source gate, institutional authors with punctuation (`ISO/IEC/IEEE`, `U.S. Department of Defense`), year-format differences, and PDF line-wrap produce occasional spurious `MISS`/`???` lines that need a human eyeball. **When a `.tex`/`.md` source exists, gate the source, not the rendered artifact.**
| `--autoverify` | Stub. Would auto-launch `/refverify` on each miss; currently prints a notice only. |

### Flag-existence probe

A concurrent agent may be modifying `refcheck.py` to add or change flags. Before relying on `--include-pending` or any other recent flag, probe with `--help`:

```bash
python ".../scripts/refcheck.py" --help
```

If `--include-pending` is absent, fall back to plain `--strict` and report that pending-surfacing is not yet available in the current refcheck build. Do not edit `refcheck.py` to add the flag yourself.

---

## How to Read the Result

`refcheck.py` exits with one of two codes:

- **Exit 0:** All bibliography entries matched. Render may proceed.
- **Exit non-zero (with `--strict`):** One or more entries are MISSING from `approved.bib`. The render MUST NOT proceed.

Stdout contains per-entry verdicts:

```
  OK   # 1  -> mcdermott2020ai4se               (McDermott, 2020)
  MISS # 7  ?? Smith 2024 | Smith J. et al. A new framework for...
  ???  #13  cannot extract surname/year | (some malformed entry)
```

- **OK** — entry has a matching `(surname, year)` pair in `approved.bib`. Safe.
- **MISS** — surname+year extracted but no match in the store. **Must be resolved via `/refverify` before render.**
- **???** — surname/year could not be extracted from the bib line. Manuscript formatting issue; the agent should inspect and fix the bib line itself, then re-run `/refcheck`.
- **PENDING** (only with `--include-pending`) — entry matched to a `pending/` bib. Still cannot ship; route via `/refverify` to promote.

---

## What the Agent MUST Do on a Failed Gate

When `/refcheck` returns non-zero in `--strict` mode:

1. **Do NOT proceed to render.** No pandoc, no xelatex, no PDF, no shareable artifact.
2. **Do NOT autonomously emit additional citations** to "fix" the gap. New citations need verification before they can replace missing ones.
3. **Do NOT silence the gate** with `--advisory` to get the render through. The structural rule (R019, risk:critical) explicitly forbids this.
4. **Route each MISS through `/refverify`.** For each missing bib entry, invoke `/refverify <author-year-or-doi>` to either:
   - Find a duplicate-of-approved (DOI dedup short-circuit),
   - Run the single-model triple-check workflow against authoritative sources, or
   - Route to human-attested path if the ref has no external source.
5. **For ??? entries**, fix the manuscript formatting first (the bib line is malformed). Then re-run `/refcheck`.
6. **Acceptable fallback:** Replace the unresolvable cite with a visible `[PLACEHOLDER]` per R019 §6.1 and surface the gap to the principal. Do not silently delete the cite.

---

## Examples

### Pre-render gate check (production)

```bash
python ".../scripts/refcheck.py" \
  "/path/to/manuscript.md" \
  --strict
# exit 0 -> proceed to pandoc
# exit 1 -> stop; route missing entries through /refverify
```

### Drafting-time spot check (advisory)

```bash
python ".../scripts/refcheck.py" \
  "/path/to/draft.md" \
  --advisory
# always exit 0; warnings on stdout
```

### With pending surfacing

```bash
python ".../scripts/refcheck.py" --help | grep -q 'include-pending' && \
python ".../scripts/refcheck.py" \
  "/path/to/manuscript.md" \
  --strict \
  --include-pending
```

### With a hive-local overlay

```bash
python ".../scripts/refcheck.py" \
  "/path/to/MACQ/paper.md" \
  --strict \
  --local-store "/path/to/MACQ/references/extra.bib"
```

---

## Related Skills

- `/reflookup` — Search approved + pending stores BEFORE drafting a citation. Prefer reuse over verification.
- `/refverify` — Run the single-model triple-check workflow on a MISS to promote it (or quarantine it).

## References

- `docs/proposed_R019_references_verification_gate.md` §7 (render gate)
- `~/.claude/CLAUDE.md` [R019]
- `memory/feedback_references_triple_check.md`
