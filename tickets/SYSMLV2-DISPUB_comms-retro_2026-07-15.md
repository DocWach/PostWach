# Cross-hive communication retro: SysMLv2 hive <-> PostWach (dispub, VERIF-002)

**Date:** 2026-07-15 · **Author:** SysMLv2 hive · **For:** PostWach (sysmlv2-slice)
**Provenance (R018):** claude-opus-4-8 (Anthropic, Claude Code CLI), Opus 4.8 [1m].
**Scope:** the process used to coordinate the SysMLv2 hive's VERIF-002 deliverables into the
dissertation-publication paper P1 ("Asserted or Entailed?"), and what worked vs. what did not.

---

## What we were trying to do

Feed the SysMLv2 representational-capacity work (SYSMLV2-VERIF-002 deliverables D1-D8) into P1, while
respecting the lane rule "the hive stages content; PostWach owns the main.tex/paper claim and
integration." Coordination was supposed to happen on a shared "blackboard."

## Channels attempted, in order

1. **Named file-path blackboard** (`02 My Outreach/2026 - Dis Pub/manuscript_v3/BLACKBOARD_dispub.md`,
   per the original ticket). **Did not exist** on disk; the `02 My Outreach` folder is absent; the
   `coordination/` folder in the PostWach repo is empty claude-flow scaffolding. No shared filesystem
   rendezvous existed.
2. **ruflo (claude-flow) MCP memory mirror**, namespace `dispub-blackboard`. Used `memory_store`,
   `memory_search`, `memory_retrieve`. Posted three notes for PostWach:
   - `query/postwach/sysmlv2-integration-target-2026-07-15` (questions + ground-truth corrections)
   - `inbox/postwach/sysmlv2-P1-figure-staged-2026-07-15` (ack + staged figure)
   - `query/postwach/sysmlv2-textual-listing-and-section-labels-2026-07-15` (textual-notation
     decision + request for P1 section labels)
   Read prior entries `inbox/sysmlv2-hive/VERIF-002-complete` and
   `discussion/results-presentation-per-relationship-vs-per-approach`.
3. **Repo-tracked files** as the durable channel: deliverables staged in
   `07 SysMLv2/tickets/SYSMLV2-VERIF-002_deliverables/` (D6 construct-detail + defense, D7 figure
   patch [superseded], D8 textual-notation listing), and the complete model committed into the
   publication repo at `Wach_Dissertation_Journal_Publication/supplementary_materials/12_sysmlv2_descriptive_model/`.
4. **The human principal as relay.** In practice, this is the channel that actually carried information
   between the two hives (see below).

## What worked

- **Repo-tracked files.** Staging deliverables as files in the repo was reliable and durable. This
  reconfirms the prior session's conclusion: files are the canonical cross-hive channel.
- **The ruflo mirror for the SysMLv2 hive's own store.** Store/retrieve/semantic-search all worked
  within this hive's `.swarm/memory.db` (HNSW + embeddings; exact-key retrieve lossless).
- **The human principal relaying** PostWach's decisions (P1/P2 clarification, the correct repo URL,
  the figure-vs-textual-notation decision). Every genuine cross-hive information transfer happened this
  way.
- **Verify-against-disk discipline.** Checking the message's premises against the actual files caught
  several mismatches before they caused bad edits.

## What did NOT work / difficulties

1. **Cross-store split (the core problem).** The ruflo mirror is **per-repo**: each hive has its own
   `.swarm/memory.db`. The SysMLv2 hive's `dispub-blackboard` and PostWach's are **different stores**.
   Result: my posts to `dispub-blackboard` were not visible to PostWach, and PostWach's posts were not
   visible to me. Searching the namespace returned only my own entries. The "blackboard" was not a
   shared surface at all. (This exact caveat was flagged at the end of the 2026-07-01/02 session and
   recurred unchanged.)
2. **No shared rendezvous of any kind.** With no file blackboard and no shared store, there was no
   place both hives could read and write. PostWach's blackboard post (P1/P2 map, section map,
   fig:sysmlv2 defect) was unreachable by the SysMLv2 hive; it arrived only because the principal
   pasted its content into chat.
3. **Divergent views of disk state produced premise mismatches.** The incoming message referenced a
   staged patch `SYSMLV2_SECTION_UPDATE_2026-07-01.md`, a "blackboard section 5" with a notional-case
   artifact list, and a defective `fig:sysmlv2` showing `part def Flashlight` -- **none of which
   existed** in the files the SysMLv2 hive could read (both `manuscript` and `manuscript_v3` have
   SysML v2 only as table columns; no such patch on disk or on the mirror). Time went to reconciling
   the mismatch rather than to the work.
4. **Wrong-repo detour.** "The paper's git repo" was first identified as the PostWach repo
   (`DocWach/PostWach`); the model file was briefly copied and staged there, then the principal
   corrected it to `DocWach/Wach_Dissertation_Journal_Publication`. The mistaken copy was fully
   reverted (PostWach repo left untouched), but the round trip cost a cycle. Root cause: no
   machine-readable pointer to the authoritative paper repo; it lived only in the principal's head.
5. **Tooling friction (execution, not comms, but it slowed delivery).** The long OneDrive path
   exceeded Windows MAX_PATH (260 chars): file copy needed the `\\?\` long-path prefix, and `git add`
   needed `core.longpaths=true`. The Bash->PowerShell wrapper also mangled `$variables` and `\\`
   escapes, which forced routing PowerShell through script files instead of inline commands.

## Recommendations

- **Establish one shared rendezvous both hives can read and write.** Best option: a committed file
  blackboard (e.g., `BLACKBOARD_dispub.md`) inside a repo both hives clone, so it travels through git.
  Alternative: a genuinely shared claude-flow store (federation BBS or a common `.swarm` DB), not the
  per-repo default. If neither is set up, **make the human-relay explicit** as the channel rather than
  assuming the mirror is shared.
- **Record authoritative locations in a file, not in conversation.** A small machine-readable pointer
  (paper repo URL, live manuscript path, P1/P2 map) in the shared blackboard would have prevented the
  wrong-repo detour and the P1/P2 confusion.
- **Treat repo-tracked files as canonical** until a shared store exists (unchanged from the prior
  session's finding).
- **Consider a registered skill** for cross-hive blackboard coordination and paper-integration
  handoffs (currently none exists; noted under R020 this session).

**Integration status (R016):** (a) research artifact -- a process retrospective by the SysMLv2 hive,
not independently reviewed. Placed in PostWach's `tickets/` at the principal's request; not committed.
