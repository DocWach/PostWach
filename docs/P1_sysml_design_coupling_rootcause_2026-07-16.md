# Root-cause report: the SysML v2 listing is not design-agnostic (2026-07-16)

**Author:** PostWach (CTO). **Provenance (R018):** claude-opus-4-8[1m], Anthropic, Claude Code CLI, principal-directed.
**Trigger:** The principal identified that the SysML v2 listing (Figure 3) assumes a flashlight design upfront: the requirements are stated in terms of `FlashlightDesign`, so they are not blind to the system design. This contradicts the paper's premise that requirements bound a set of acceptable designs rather than naming one. This is the FOURTH consecutive root-cause report; it is the same meta-pattern as the three before it.

## Section 1 — The defect

The verification artifacts must be design-agnostic where the paper says they are. The text-based SR table states each requirement against a named interface with the command and interface parameters left undefined, "so the requirements bound a set of acceptable designs rather than naming one" (e.g., SR4: yellow light through IF-2). The SysML v2 listing does the opposite. Every requirement is coupled to the specific `FlashlightDesign`:

```
requirement def ProvideYellowLightReq { subject design : FlashlightDesign;
    require constraint { design.led.emittedFlux == requiredFlux } }        // SR
requirement def VerifyYellowLightReq  { subject article : FlashlightDesign;
    require constraint { article.led.emittedFlux == requiredFlux } }       // VR
requirement def AcceptableVerificationModel { subject vm : FlashlightDesign;
    require constraint { vm.led.emittedFlux >= 500 [lm] and vm.led.offFlux < 0.5 [lm] } }
```

Each `subject` is `FlashlightDesign` and each constraint reaches into `design.led`, a specific design's internal part. The requirement therefore presupposes the flashlight, its light-emitting element, and its structure. A design-agnostic requirement would take a general system or interface as subject and constrain the behavior at the interface (luminous flux and wavelength at IF-2), not the internals of one chosen design. The listing bakes the answer (a flashlight) into the requirements, which is exactly what the comparison is supposed to hold open.

The inconsistency is threefold: within the paper (text-based SR is interface-based and design-open, SysML SR is design-coupled); against the stated premise (requirements bound acceptable designs); and across the three renderings (text-based and WySE keep the design open, SysML does not).

## Section 2 — When and how it entered

- The listing came from the SysMLv2 hive deliverable **D8** (`07 SysMLv2/tickets/SYSMLV2-VERIF-002_deliverables/D8_fig_sysmlv2_textual_listing_2026-07-15.md`, dated 2026-07-15 16:47). I ported it into `main.tex` in the postwach-03 session (2026-07-15), replacing the earlier `part def Flashlight` product model.
- The flashlight assumption is older than D8: the original figure was a flashlight PRODUCT model, which had already been flagged. D8's job was to stop showing a product model and show the SE artifacts instead. It did that at the surface (requirements as `requirement def`s, the design and models as `part def`s), but it kept the flashlight coupling inside the requirement subjects and constraints.
- The manuscript directory is not a git repository, so there is no commit trail; the D8 file timestamp plus the postwach-03 session archive pin the introduction to the 2026-07-15 D8 port.

## Section 3 — Why it was not caught

- **I treated the D8 port as fully resolving the flashlight issue when it resolved only the surface.** The prior defect was "this is a product model." D8 removed the product model, and I checked exactly that: does it replace `part def Flashlight`, does it render, later does it fit and left-justify. All structural and formatting. I never checked whether the requirements are design-agnostic, which is the deeper form of the same flashlight problem.
- **I trusted the hive's deliverable and its defense.** The hive's D6 defense argued "these are SE artifacts, not a product model." That defense is about the product-model axis, not the design-agnostic axis; I did not independently test the design-agnostic axis.
- **No cross-representation consistency check.** The text-based SR is interface-based and design-open; the SysML SR should be too. Comparing the three renderings of the same artifact against the design-agnostic principle would have exposed the coupling immediately. That comparison was never run.

## Section 4 — Root cause and recurrence

Fourth report, one meta-pattern: my verification is structural and formatting-level (does it compile, render, fit, replace the old thing), never semantic-consistency-level (is each element consistent with the paper's premises and with its counterparts elsewhere). The specific failure here is trusting a subordinate deliverable and porting it without checking it against the paper's own stated principle (design-agnostic requirements), and without comparing the three artifact renderings for consistency.

- 2026-07-15: wrong Results structure survived because I checked correctness, not design-conformance.
- 2026-07-16 (misalignment): a Methods restructure duplicated §5.1 because I did not check downstream.
- 2026-07-16 (text-based artifacts): a content move erased a semantic role because I moved by location, not role.
- 2026-07-16 (this): a ported deliverable violates a premise because I checked surface, not semantic consistency, and did not cross-check the three renderings.

The document-QA SOP, unbuilt and flagged in every one of these reports, is the missing control.

## Section 5 — Preventive measures

1. **Premise-conformance check for every artifact rendering.** The paper states principles (requirements are design-agnostic; the text-based rendering feeds the others; only WySE entails). Every concrete artifact, in every representation, must be checked against those principles before it ships.
2. **Cross-representation consistency check.** The same artifact rendered three ways (text, SysML, WySE) must agree on the invariants (here, design-agnosticism). Diff the three.
3. **Never port a subordinate deliverable on trust.** A hive/agent deliverable is verified against the paper's premises and cross-checked, not accepted because it replaced the prior defect or because its own defense sounds right.
4. **Stop the whack-a-mole: build and run the document-QA SOP as one comprehensive audit** rather than fixing one principal-found defect per turn.

## Section 6 — Proposed fix (for principal confirmation)

Revise the SysML v2 listing so the requirements are design-agnostic, matching the SR table:
- Requirement `subject`s become a general system or its interface, not `FlashlightDesign`; constraints reference interface behavior (luminous flux and wavelength at IF-2, off-flux at IF-2), not `design.led`.
- `FlashlightDesign` remains as the one `part def` that is the fixed system design (a specific design is legitimately specific); the verification models remain `part def`s; but no requirement reaches into a design's internals.
- Re-verify the revised listing parses against the OMG SysML v2 spec, and cross-check it against the text-based SR and the WySE problem-space rendering for design-agnostic consistency.

Because this is SysML-specific correctness, the revision can be done here or routed back to the SysMLv2 hive; given the hive introduced the coupling, a corrected D9 from the hive (with the design-agnostic requirement recast) is the cleaner path, but I can draft the corrected listing directly if you prefer speed.
