# Root-cause report: how the §5.1 Results misalignment survived the Methods restructure (2026-07-16)

**Author:** PostWach (CTO). **Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.
**Trigger:** After restructuring Methods (§4) into Setup / Execution Protocol this session, the principal found that Results §5.1 "Structural overview" is out of alignment: some of its content now duplicates the new Methods Setup, and the system-requirements rendering belongs under §5.2 Text-based practice, "as was previously decided." This is the SECOND such report; it is a recurrence of the pattern documented in `P1_review_misses_rootcause_2026-07-15.md`.

## Section 1 — The miss

§5.1 "Structural overview" currently holds five things:
1. Framing: "the text-based approach renders the artifacts, the others formalize them; three verification-model relationships are at issue."
2. The system requirements: `tab:sr` (five SRs as natural-language statements) + its framing.
3. The system design instance (the flashlight, torque switch, at the coupled level).
4. The verification requirements, plus the VRPS and VMMC development.
5. VM-A and VM-B definitions, and a full restatement of the two assessment axes (existence + characterization).

After the Methods restructure, most of this is now misplaced:
- **The two axes** (item 5, para) are a near-verbatim duplicate of the new Methods §4.2.4 "The two assessment axes."
- **The case setup** (SD instance, VM-A/VM-B, the VR activities) belongs in the Methods notional case (§4.2.3), which now fixes the case as SD4/VM8/VM6 but without the concrete descriptions.
- **The SR table and natural-language rendering** (item 2) is the *text-based* approach's output, and we had already decided the renderings "are reported with the results rather than fixed here," meaning under §5.2 Text-based practice, not in a common overview.

So §5.1 is a vestigial "common setup" block that straddles Methods and Text-based practice and no longer has a coherent home.

## Section 2 — How it happened

1. **I restructured Methods as a local §4 edit and never checked the downstream Results.** The Methods Setup now establishes the approaches, the four artifacts, the notional case (SD, VM-A, VM-B), and the two axes. §5.1 establishes the same things. The restructure created a duplication and a boundary shift, but I scoped the change, and my verification, to §4 alone. I verified §4 in isolation (byte-diff of tables, latexmk, refcheck, render of §4) and did not re-read §5 to ask "did this change make anything downstream redundant or misplaced?"

2. **§5.1 was a latent misalignment from the day the by-approach Results was built.** When I converted Results to by-approach earlier this session, I parked the artifact-establishment in a "Structural overview" §5.1. But the by-approach design means artifact-establishment belongs either in Methods (setup) or in §5.2 (the text-based rendering). §5.1 was a "common block" that never fit the by-approach model. In particular, the SR table went into §5.1, not §5.2, contradicting the already-agreed decision that the text-based rendering is reported under text-based. The misplacement was latent; the Methods restructure exposed it.

3. **The Workflow was scoped to §4 and could not see the knock-on effect.** The brief said "Output ONLY the LaTeX for section 4." Neither the Workflow nor I asked whether a two-phase Methods makes §5.1 redundant. The judge raised an INTEGRATOR FLAG about label consistency, but content overlap with §5 was outside its charge.

## Section 3 — Why verification did not catch it

Same structural failure as the 2026-07-15 report: I verify **local correctness** (does §4 compile, do cites resolve, do the tables match), not **global consistency** (does each piece of content live in exactly one place; does Methods set up what Results reports; did a structural change ripple downstream). A green build and a passing refcheck say nothing about whether Methods and Results now overlap. There is still no gate that checks section boundaries, which is precisely the document-QA SOP that both this report and the prior one flag as unbuilt.

## Section 4 — Recurrence

This is the M1-family failure from `P1_review_misses_rootcause_2026-07-15.md`: optimizing for "no error in what is present" rather than "is the structure right across the whole artifact." The new, sharper variant is **failure to propagate a structural change to its downstream consumer.** Methods and Results in a comparison paper are coupled by design (Methods fixes inputs; Results reports what each approach does with them). Changing one without reconciling the other guarantees a boundary defect.

## Section 5 — Preventive measures

1. **Cross-section consistency pass after any structural change.** When a section is restructured, immediately re-read the adjacent and mirroring sections (here Methods and Results) and reconcile: remove duplication, move content to its correct home, fix now-broken cross-references. Make this a required step, not an afterthought.
2. **Explicit content-placement map for the paper.** For this comparison paper: Methods = fixed inputs (the three approaches, the four artifact definitions, the notional case incl. SD/VM-A/VM-B, the two axes); Results = what each approach expresses, one subsection per approach; the natural-language rendering of the artifacts is the text-based approach's output and lives in §5.2. A one-page map of "which content lives where" would have caught both the SR-in-§5.1 misplacement and the post-restructure duplication.
3. **Promote the document-QA SOP from TODO to built.** It must include a section-boundary check: no content duplicated across sections; every structural decision reflected everywhere it touches. This is now flagged in two consecutive root-cause reports.

## Section 6 — Proposed fix (for principal confirmation)

Dissolve §5.1 "Structural overview" and redistribute:
- **To Methods §4.2.3 (the notional case):** the concrete system-design description, the VM-A/VM-B descriptions, and the two verification activities (the VR setup). These are fixed inputs.
- **To §5.2 Text-based practice:** the SR table (`tab:sr`) and its framing, as the text-based approach's natural-language rendering, plus the "text-based renders, others formalize" lead-in.
- **Remove as duplicate:** the two-axes paragraph (now in Methods §4.2.4) and the three-relationships framing (covered by the Results intro and Methods §4.3).
- **Open judgment call:** the VRPS/VMMC development currently in §5.1 is science-based apparatus; it can go to Methods (establishing the VR artifact) or to §5.3 (science-based practice). Recommend §5.3, since it is the science-based machinery the science-based subsection relies on.

Result: Results begins directly with Text-based practice, then SysML v2, then WySE, then Comparison, with no common-overview straddle.
