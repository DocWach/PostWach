# ORCiD Workflow — PostWach

**Status:** scope locked 2026-04-29. P1 (auth + read smoke test) PASS 2026-04-29. Push capability (P3-P5) blocked at the Public API tier; awaiting UA Member API decision (see §12).
**Owner:** PostWach (CTO / research intelligence).
**ORCiD ID under management:** `0000-0002-3085-2883` (Paul Wach).
**ORCiD application name:** `DocWach_ORCiD` (Public API client).
**Baseline at scope-lock:** 4 works on ORCiD record; 0 employments, 0 education, 0 distinctions.

## 1. Purpose

Push-only synchronization from canonical CV/RIS sources to the public ORCiD record. Eliminates the recurring rebuild of biosketch product lists that surfaced during the 2026-04-28 Genesis race-the-clock submission, where ORCiD held only 4 works and could not serve as a biosketch input.

## 2. Scope decisions (locked 2026-04-29)

| # | Dimension | Decision |
|---|---|---|
| 1 | Direction | Push-only (CV/local → ORCiD). |
| 2 | Record types | Works + employments + education-and-qualifications + distinctions. |
| 3 | API tier | Public API for read; **push not feasible at Public API tier** (see §12). Membership question pending with UA Libraries. |
| 4 | Source-of-truth | CV is canonical. Push-only obviates a full conflict policy in v1. |
| 5 | Identity / dedup | Persist `put-code ↔ local-id` mapping. Local id = DOI when present, else `(year, first-author-lastname, title-hash)`. |
| 6 | Trigger | Manual command, dry-run preview required before real push. |
| 7 | Operating hive | PostWach. |
| 8 | Credential storage | `~/.config/postwach/orcid.env`. Never committed. |
| 9 | Source feed | RIS as canonical machine-readable format. CV→RIS converter built once. |
| 10 | PostWach output integration | Generative (RIS export for next biosketch) + validation (ORCiD ↔ CV drift). Generative first. |

## 3. Path layout

```
01 PostWach/
├── scripts/orcid/
│   ├── auth.py                   # OAuth helper, token cache
│   ├── cv_to_ris.py              # CV → RIS converter
│   ├── sync.py                   # main sync command (dry-run + push)
│   ├── pull.py                   # ORCiD → biosketch RIS export
│   ├── validate.py               # drift report (P7)
│   └── state/                    # gitignored
│       ├── put_code_map.json     # local-id ↔ ORCiD put-code
│       └── token_cache.json      # access token, refresh token, expiry
└── docs/
    └── orcid-workflow.md         # this document
```

## 4. Credential schema (`~/.config/postwach/orcid.env`)

```
ORCID_CLIENT_ID=APP-XXXXXXXXXXXXXXXX
ORCID_CLIENT_SECRET=<secret>
ORCID_REDIRECT_URI=<as registered>
ORCID_ENVIRONMENT=production       # or 'sandbox'
ORCID_RECORD_HOLDER=0000-0002-3085-2883
```

Loader reads this file only; nothing is committed. State directory is in `.gitignore` for the PostWach repo.

## 5. Phased plan

| Phase | Goal | Status |
|---|---|---|
| P1 | Auth-and-read smoke test. OAuth flow end-to-end, token cache, read public record. | **PASS 2026-04-29.** Token cached, ~20-year lifetime, scope `/authenticate`. Confirmed 4 works on record. |
| P2 | CV → RIS converter. Diff RIS-derived works against existing ORCiD record. | Not started. Read side; not blocked. |
| P3 | Push Top 10 (existing `wach_top10_products.ris` from Genesis). | **BLOCKED.** Public API cannot write. Pending Path B answer. |
| P4 | Expand push to full CV back catalog. | **BLOCKED.** Same reason as P3. |
| P5 | Push employments, education, distinctions. | **BLOCKED.** Same reason as P3. |
| P6 | Generative pull. Export ORCiD record as RIS for next biosketch cycle. | Not started. Read side; not blocked. |
| P7 | Drift report. Compare ORCiD record to CV; flag missing, inconsistent, or auto-imported records. | Not started. Read side; not blocked. |

Each phase ends with a one-line status update and a go/no-go on the next.

## 6. Out-of-scope for v1

| Item | Rationale | Revisit when |
|---|---|---|
| Co-author ORCiD lookup (collaborators-list automation) | Different problem domain (graph traversal, not push-sync). | Next federal proposal cycle. |
| Funding records | NDA/sensitivity questions for active grants. | Once per-grant disclosure policy is documented. |
| Peer-review claims | Low ROI for biosketches; ORCiD's peer-review model is awkward. | If a venue starts requiring it. |
| Trusted-individual / trusted-organization permissions | Single-user v1; no delegation needed. | If/when an institutional admin needs proxy access. |
| Bidirectional sync | Would require a real conflict policy. | After v1 is in production for one full biosketch cycle. |
| On-publish hooks, scheduled syncs | Manual command first; automate after manual is reliable. | After P3-P6 stabilize. |

## 7. Future ontology task

`portfolio-governance.ttl` (GI-JOE) could grow ORCiD-conformant predicates so portfolio-shacl validates publication-record completeness:

- `po:Publication` class with `po:doi`, `po:orcidPutCode`, `po:venue`, `po:year`, `po:authors`.
- `po:Researcher` class with `po:orcidId`, `po:hasAuthored` predicate.
- New CQs: "list all publications missing from ORCiD", "list ORCiD records not linked to a `po:Publication`".

Defer until v1 is operating. Filed under HOS Capability Freshness sub-thread as a candidate for ontology-backed staleness detection (publications missing from ORCiD = stale capability).

## 8. Failure-mode design notes

- **Auto-imported records.** ORCiD's Search-and-Link wizards (Crossref, DataCite, Scopus) may add records we did not push. Policy v1: detect via missing put-code in our local map, log them in dry-run output, leave them alone. Reconciliation deferred to v2.
- **Token expiry.** Public API `/authenticate` tokens are long-lived (~20 years observed; `expires_in` ≈ 631M seconds). Token cache records expiry. Token-renewal logic deferred since it won't be needed for years.
- **Rate limits.** Public API allows 24 req/sec, 100k/day. Top 10 push is well inside. Full CV (~30-50 entries) still trivial. Add per-request sleep only if 429 observed.
- **Partial-write failures.** Each work pushed individually with try/except. On HTTP error, log put-code state, continue, summarize at end. No transactional rollback.

## 9. Operations

```bash
# P1
python scripts/orcid/auth.py --smoke-test

# P2
python scripts/orcid/cv_to_ris.py --cv "<path-to-CV.docx>" --out "<path-to-output.ris>"
python scripts/orcid/sync.py --source <ris> --dry-run

# P3
python scripts/orcid/sync.py --source "04 Genesis/Biosketch_Materials/wach_top10_products.ris" --dry-run
python scripts/orcid/sync.py --source "04 Genesis/Biosketch_Materials/wach_top10_products.ris" --commit

# P6
python scripts/orcid/pull.py --out <path-for-next-biosketch.ris>

# P7
python scripts/orcid/validate.py --cv "<path-to-CV>" --report <path-for-drift-report>
```

Exact paths and CLI flags finalized in implementation.

## 10. Open items

- **Path B answer pending** from Ellen Dubinsky (UA Libraries Scholarly Communication Librarian, `edubinsky@arizona.edu`). Email sent 2026-04-29 asking whether UA has a write-direction Member API integration researchers can use to push works/employments/education to their own ORCiD records.
- Decision on which CV file is canonical for P2 (full CV vs 1-page CV vs both — full CV is the working assumption).
- Capability-index entry to be added when push capability is unblocked.

## 11. Cross-references

- Genesis session archive: `docs/session-archives/SESSION_ARCHIVE_2026-04-28_postwach-01.md`, §7 next-session hint (c).
- This session's archive: `docs/session-archives/SESSION_ARCHIVE_2026-04-29_postwach-03.md`.
- Source RIS for P3: `03 Projects/98 Proposal Phase/04 Genesis/Biosketch_Materials/wach_top10_products.ris`.
- Top 10 rationale and CV/Crossref discrepancies: `03 Projects/98 Proposal Phase/04 Genesis/Biosketch_Materials/top10_products.md`.

## 12. Reality check 2026-04-29 — Public API tier limit + path forward

**Scoping error caught during P1 OAuth flow.** The ORCiD Public API tier (which is what the `DocWach_ORCiD` client registered against) supports only the `/authenticate` and OpenID-related scopes. The `/read-limited`, `/activities/update`, and `/person/update` scopes used for writing to a record are gated behind the Member API tier, which requires institutional or paid membership. Individual record-holder consent does not unlock write scopes for a Public API client. This contradicts §2 row 3 as originally written; that row is now corrected.

**Three paths to back-populate the ORCiD record:**

| Path | Mechanism | Coverage | Effort | Status |
|---|---|---|---|---|
| A | ORCiD's Search & Link wizards (Crossref, DataCite, etc.) on orcid.org. Each wizard is a Member integration the user authorizes; user select-claims their works. | DOI-bearing publications; reaches 7-8 of Top 10. | Manual click-through, ~30 min one-time per wizard. | Available on demand. |
| B | UA Member API integration (write-direction). | Whatever UA's integration supports; potentially full CV. | Email exchange + UA Library tooling cycle. | Pending Ellen Dubinsky reply. |
| C | Manual web entry on orcid.org/account. | Anything Search & Link misses (in-press papers, technical reports without DOIs, employments, education, distinctions). | One entry per item, hand-entered. | Available on demand. |

**Pragmatic order if Path B comes back negative:** A first (catches DOI'd publications in one pass), then C for the residual.

**UA membership facts:**
- UA has been an ORCiD member since 2016 via Greater Western Library Alliance (GWLA), administered through the ORCID US Community / LYRASIS.
- Existing UA integrations are pull-only: `orcid.arizona.edu` (trusted-org connector), `kmap.arizona.edu` (Knowledge Map ingest), Faculty Portfolio (formerly UA Vitae).
- No write-direction integration is publicly documented. Whether one exists internally or could be deployed is the question for Ellen.

**What the read side (P1, P2, P6, P7) can still do at Public API tier:**
- P1 (PASS): authenticate, read public record summary.
- P2: parse CV into RIS, diff against ORCiD's read-only view, produce preview.
- P6: pull ORCiD works as RIS for biosketch generation.
- P7: drift report between ORCiD and CV.

These four phases are independent of the push question and can proceed.
