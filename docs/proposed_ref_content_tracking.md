# Proposed: Reference Content Tracking (full-text linkage for the R019 store)

**Status [R016]: (a) research artifact / design proposal.** Not yet implemented.
**PROVENANCE [R018]:** drafted by Opus 4.8 (claude-opus-4-8[1m]), Claude Code, at the principal's direction, 2026-07-11.
**Owner:** PostWach (CTO) designs; Alpha Empress (COO) registers for governance. Governed by [R019] / [R109].

## 1. Problem

The portfolio reference store (`04 Resource Library/00 Verified References/approved.bib`) records that a reference is *verified* (bibliographic metadata plus the R019 approval status) but not *where its full text lives*. A verification system that cannot locate the artifact it verified is only half a system.

This failed concretely on 2026-07-11. Zeigler's *Theory of Modeling and Simulation* existed on disk as extracted Markdown at `04 Resource Library/DEVS Corpus/Zeigler_TMS_2018_MDfiles/`, but nothing in the reference store pointed there. The "check the foundations before claiming novelty" pass, which then found that TMS chapter 22 already contains the +probability morphism, could not start until the principal supplied the path by hand. The behavioral rule ([[feedback_references_triple_check]]) and the structural gate ([R019]) both assume the source is reachable; today it is not.

## 2. Goal

Attach the full-text content (PDF, and where available an agent-readable Markdown extraction) to each approved reference, EndNote/Zotero-style, so that any researcher or agent can locate and read the source that a citation stands on. Additive to the existing store, not a rebuild.

## 3. Design

### 3.1 The `file` field (EndNote-equivalent)

Use the standard BibTeX content-attachment convention already understood by JabRef, Zotero, and BibDesk: a `file` field on each entry.

```bibtex
@book{zeigler2018tms,
  author = {Zeigler, Bernard P. and Muzy, Alexandre and Kofman, Ernesto},
  title  = {Theory of Modeling and Simulation},
  edition = {3rd}, publisher = {Academic Press}, year = {2018},
  file   = {DEVS Corpus/Zeigler_TMS_2018.pdf;DEVS Corpus/Zeigler_TMS_2018_MDfiles/}
}
```

- Paths are **relative to a declared content root** (`04 Resource Library/`), so the store is portable and does not hard-code machine paths.
- Multiple attachments are `;`-separated (the JabRef convention): the source PDF and the extracted-MD directory or file.
- A missing/empty `file` field is legal but flagged as content-debt (a reference approved-but-unlinked).

### 3.2 Content-store layout

Full text lives under `04 Resource Library/` in one of two accepted shapes:
- **By corpus** (preferred for multi-part sources): a named subdirectory, e.g. `DEVS Corpus/Zeigler_TMS_2018_MDfiles/ch*.md`, as already exists.
- **By citation key** (for single-file sources): `<content-root>/<bibkey>.pdf` and `<bibkey>.md`.

Prefer **an extracted Markdown alongside the PDF**. The TMS pass was only possible because MD chapters existed and were agent-readable; a bare PDF is far less consultable by an agent. A conversion helper (e.g. the `convert_tms.py` already present in the DEVS Corpus folder) is the model.

### 3.3 Skill integration (the ref* chain)

- **`refcheck`** gains a content gate: for every cited key, confirm the `file` path(s) resolve on disk. A verified-but-unlinked or dangling-path reference is a reported defect, parallel to an unapproved-citation defect.
- **`reflookup`** returns the resolved content location(s) so an agent can open and read the source, not just confirm it exists.
- **`refverify`** may cite the local full text as corroborating evidence during the Byzantine-Bayesian check, and records the content path in the approval record.

### 3.4 Backfill and pilot

- **Pilot on the DEVS Corpus:** populate `file` for `zeigler2018tms` (PDF + the MD chapter directory) and the other Zeigler entries, since that content already exists. This immediately unblocks the WySE foundations passes.
- **Backfill the rest** opportunistically: when a reference is next consulted, link its content; report the unlinked remainder as standing content-debt in the reference-debt line ([[project_postwach_sweep_backlog]]).

## 4. Governance and scope

The store is portfolio-level and R019 is global, so this is a cross-hive change. PostWach (CTO) owns the design; Alpha Empress (COO) registers it and any rule text; Fort Wachs is consulted only if content storage raises a confidentiality question (unpublished full text is IP-sensitive, so the content root inherits the same handling as the rest of the Resource Library). The change is additive and tool-compatible (the `file` field is ignored by any tool that does not use it), so it carries no render-time risk to existing manuscripts.

## 5. Open decisions

- Content root: confirm `04 Resource Library/` as the declared root, or a dedicated `04 Resource Library/00 Content/`.
- Whether extracted-MD is required or recommended for approval (recommend: required for any reference intended to support a foundations/novelty pass; optional otherwise).
- Whether to add a `contentSha` for integrity (defer; not needed for v1).
