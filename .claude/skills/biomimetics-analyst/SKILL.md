---
name: Biomimetics Analyst
description: Discover and validate formal morphisms between biological and engineered systems, extending the isomorphism catalog to bio-eng domain pairs
---

# Biomimetics Analyst

A cross-domain morphism discovery capability for biological and engineering systems. It does not model the biology itself (that is the `biophysics-modeler` agent) — it provides the methodology for finding, classifying, validating, and cataloging structural correspondences between biological and engineering domains.

## When to Use This Skill

- Investigating Idea 8 (Formal Morphisms Between Biological and Engineered Systems)
- Investigating Idea 12 (Immune/Cyber Morphisms) — a special case of Idea 8
- Extending the isomorphism catalog (`catalog.json`) to biological source domains
- Formalizing an informal bio-eng analogy into a catalog-ready morphism entry
- Evaluating whether a suspected bio-eng correspondence is exact, partial, or speculative

---

## Quick Start

```bash
# Investigate a single bio-eng domain pair
claude-flow hive-mind spawn "Investigate morphism between [biological system] and [engineering system]. Follow the 7-step morphism discovery protocol." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,control-theorist

# Run Idea 12 (immune/cyber) analysis
claude-flow hive-mind spawn "Investigate Idea 12: formal morphism between adaptive immune response and cybersecurity incident response. Classify morphism type, identify variable mapping, assess catalog readiness." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,control-theorist

# Batch evaluate all known domain pairs
claude-flow hive-mind spawn "Evaluate all 10 known bio-eng domain pairs (B-1 through B-10). For each: classify morphism type, assess catalog readiness, flag pairs needing further investigation." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,numerical-analyst,control-theorist
```

---

## Core Methodology

### Morphism Discovery Protocol

A 7-step procedure for converting an informal bio-eng analogy into a formal, catalog-ready morphism entry.

#### Step 1: Biological System Formalization

Invoke `biophysics-modeler` to produce a mathematical representation of the biological system.

**Required output:** State-space form (states, inputs, outputs, governing ODEs), or effort/flow variables if the system admits a bond-graph decomposition.

**Key decision:** Does this biological system decompose naturally into effort/flow pairs?
- **Yes** (cardiovascular, respiratory, pharmacokinetic): Use `effort_variable` and `flow_variable` fields in catalog entry, consistent with bond-graph formalism
- **No** (immune dynamics, neural circuits with voltage-gated conductances): Use `state_space` representation in catalog entry; document why effort/flow decomposition does not apply

#### Step 2: Candidate Engineering Domain Identification

Check the Known Domain Pairs catalog (below). If the biological system is already listed, use the paired engineering domain. Otherwise:

1. Invoke `pattern-detector` to search existing catalog entries for structural similarity
2. Identify engineering domains with matching state dimension, coupling topology, or conservation laws
3. Propose 1-3 candidate engineering domains ranked by structural similarity

#### Step 3: Variable Mapping Construction

Build an explicit mapping between biological and engineering variables.

**Requirements:**
- Each biological state variable maps to exactly one engineering variable (injection)
- Each biological parameter maps to an engineering parameter with matching physical dimensions or role
- Document unmapped variables on either side (indicates partial morphism)

**Format:** Populate the `variable_mapping` field per `schema.json`:
```json
{
  "variable_mapping": {
    "pressure": "voltage",
    "flow_rate": "current",
    "compliance": "capacitance"
  }
}
```

#### Step 4: Morphism Type Classification

Classify using `schema.json` `isomorphism_type` values:

| Type | Criterion |
|---|---|
| `exact` | Governing equations are identical under variable substitution; all terms map |
| `partial` | Most terms map but some biological terms have no engineering counterpart (or vice versa) |
| `to_investigate` | Structural similarity suspected but not yet formally verified |

Assign `tier` per `schema.json`:

| Tier | Criterion |
|---|---|
| 1 | Fully characterized: governing equations, variable mapping, degradation analysis complete |
| 2 | Partially characterized: equations and mapping exist but degradation not yet analyzed |
| 3 | Conjectured: structural similarity argued but formal mapping incomplete |

#### Step 5: Morphism Validation

For pairs classified as `exact` or `partial`, apply quantitative validation:

1. **Eigenvalue correspondence:** Compare eigenvalues of linearized biological and engineering systems — identical eigenvalues (under variable mapping) confirm structural equivalence
2. **Trajectory correlation:** Simulate both systems from corresponding initial conditions; measure trajectory correlation (Pearson r > 0.95 for exact morphisms)
3. **Bifurcation analysis:** If either system exhibits bifurcations, verify that corresponding parameter changes produce corresponding bifurcations in the other system

For `to_investigate` pairs, define the minimum analysis needed to upgrade to `partial` or `exact`.

#### Step 6: Degradation Analysis

Populate the `degradation_analysis` fields from `schema.json`:

| Field | Question |
|---|---|
| `euler_discretization` | Does the morphism survive Euler discretization? What time step degrades it? |
| `rk4_discretization` | Does RK4 preserve the morphism better? |
| `exact_discretization` | Can an exact discretization preserve the morphism? |
| `nonlinear_extension` | If the morphism is proven for linear case, does it extend to the nonlinear regime? |
| `stochastic_extension` | Does the morphism survive addition of noise/stochastic terms? |

For biological systems, stochastic extension is especially relevant (biological noise, population-level stochasticity).

#### Step 7: Catalog Entry Creation

Format the results as a `catalog.json` entry conforming to `schema.json`. Use ID format `I-N` (next available ID in the catalog).

**Required fields:** `id`, `name`, `tier`, `status`, `isomorphism_type`, `domain_a`, `domain_b`, `variable_mapping`

**Biological-specific guidance:**
- `domain_a`: the biological system; `domain_b`: the engineering system
- For effort/flow systems: populate `effort_variable`, `flow_variable`, `energy_storage_potential`, `energy_storage_kinetic`, `dissipation`
- For non-effort/flow systems: populate `state_space` (states, inputs, outputs, next_state, readout) and leave effort/flow fields empty
- Always populate `governing_equation_continuous`

---

### Catalog Schema Alignment

The isomorphism library uses effort/flow variable formalism from bond-graph theory. Biological systems vary in their compatibility with this formalism:

**Effort/flow compatible** (use full bond-graph fields):
- Cardiovascular: pressure = effort, volumetric flow = flow
- Respiratory: airway pressure = effort, airflow = flow
- Pharmacokinetics: concentration gradient = effort, mass transfer rate = flow

**State-space only** (use `state_space` field, not effort/flow):
- Immune dynamics: antigen, effector cells, memory cells are state variables with no natural effort/flow decomposition
- Neural circuits: membrane voltage is both a state variable and acts like an effort variable, but voltage-gated conductances break the bond-graph linearity assumptions
- Endocrine axes: hormone concentrations are states; the feedback loops do not have a power-conjugate (effort × flow) structure

This is not a limitation — `schema.json` supports both representations. The skill's job is to choose the correct representation for each pair.

---

### Known Domain Pairs

Ten biological-engineering pairs identified from Ideas 8 and 12, ordered by expected morphism strength:

| ID | Biological System | Engineering System | Suspected Type | Schema Representation |
|---|---|---|---|---|
| B-1 | Neural membrane (Hodgkin-Huxley) | RLC circuit | Partial | State-space (voltage-gated nonlinearity) |
| B-2 | SIR/immune compartments | RC/reaction networks | Partial | State-space |
| B-3 | Cardiovascular (3-element Windkessel) | RRC electrical circuit | Exact (linear) | Effort/flow |
| B-4 | Respiratory mechanics | Series RLC circuit | Exact (linear) | Effort/flow |
| B-5 | 2-compartment pharmacokinetics | Multi-loop RC network | Exact (linear) | Effort/flow |
| B-6 | Adaptive immune defense | Cybersecurity incident response | To investigate | State-space |
| B-7 | Musculoskeletal dynamics | Robotic manipulator | Partial | State-space |
| B-8 | Endocrine (HPA axis) | Multi-loop control system | Partial | State-space |
| B-9 | Bacterial chemotaxis | Gradient-following control | Partial | State-space |
| B-10 | Neural field (Wilson-Cowan) | Coupled oscillator network | To investigate | State-space |

**Catalog readiness:**
- B-3, B-4, B-5: Tier 1 candidates (well-established correspondences with full equation forms)
- B-1, B-2, B-7, B-8, B-9: Tier 2 candidates (equations exist, morphism is partial)
- B-6, B-10: Tier 3 candidates (structural similarity suspected, formal mapping needed)

---

### Idea 12 Detail: Immune/Cyber Morphisms

Idea 12 (Immune/Cyber Morphisms) is a special case of Idea 8 investigating the structural correspondence between adaptive immune response and cybersecurity incident response.

#### Proposed Variable Mapping

| Immune System | Cybersecurity System | Mapping Confidence |
|---|---|---|
| Antigen | Threat signature / IoC | Medium |
| Effector cells (T/B cells) | Active defense mechanisms (IDS rules, quarantine) | Medium |
| Immune memory (memory B/T cells) | Threat intelligence database / YARA rules | Medium |
| Clonal expansion | Defense scaling / auto-scaling response | Low |
| Innate immunity (barriers, phagocytes) | Perimeter defenses (firewall, WAF) | Medium |
| Adaptive immunity | Adaptive response (ML-based detection, dynamic rules) | Low |
| Cytokine signaling | Alert propagation / SIEM correlation | Low |

#### Research Questions

1. Can the adaptive immune ODE system (Step 1) and a formal cybersecurity IR model be shown to share eigenvalue structure?
2. Does the immune primary/secondary response dynamics have a quantitative analog in threat detection improvement after first encounter?
3. What biological terms have no cybersecurity counterpart (and vice versa) — where does the morphism break?

#### Honest Assessment

This pair is classified as `to_investigate` (Tier 3). The analogy is widely cited in cybersecurity literature but has not been formalized as a mathematical morphism. The contribution of Idea 12 would be to either:
- **Upgrade** B-6 to `partial` or `exact` with formal evidence, or
- **Downgrade** it to a documented non-morphism (useful negative result: the analogy is informal only)

Either outcome is publishable.

---

## Domain Pair Investigation Template

Use this template when investigating any bio-eng domain pair:

```
DOMAIN PAIR INVESTIGATION: [B-N] — [Bio System] ↔ [Eng System]
Date: [YYYY-MM-DD]
Investigator: [Name]

STEP 1 — BIOLOGICAL FORMALIZATION
  State variables: ___
  Parameters: ___
  Governing ODEs: ___
  Effort/flow decomposition: [Yes → list] / [No → use state_space]

STEP 2 — ENGINEERING DOMAIN
  Source: [Known pair B-N] / [Pattern-detector match] / [Manual identification]
  Engineering state variables: ___
  Engineering governing equations: ___

STEP 3 — VARIABLE MAPPING
  | Biological | Engineering | Notes |
  |---|---|---|
  | | | |
  Unmapped biological variables: ___
  Unmapped engineering variables: ___

STEP 4 — CLASSIFICATION
  Isomorphism type: [exact / partial / to_investigate]
  Tier: [1 / 2 / 3]
  Justification: ___

STEP 5 — VALIDATION (if exact or partial)
  Eigenvalue correspondence: [Confirmed / Failed / Not yet tested]
  Trajectory correlation (r): ___
  Bifurcation correspondence: [Confirmed / Failed / Not yet tested / N/A]

STEP 6 — DEGRADATION ANALYSIS (if Tier 1 or 2)
  Euler discretization: ___
  RK4 discretization: ___
  Exact discretization: ___
  Nonlinear extension: ___
  Stochastic extension: ___

STEP 7 — CATALOG READINESS
  Ready for catalog entry: [Yes / Needs: ___]
  Proposed catalog ID: I-[N]
  Blocking issues: ___
```

---

## Integration with Claude Flow

### Spawn Commands

```bash
# Single-pair investigation
claude-flow hive-mind spawn "Investigate domain pair B-[N]: [bio system] ↔ [eng system]. Execute full 7-step morphism discovery protocol. Produce completed investigation template and draft catalog entry if Tier 1 or 2." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,control-theorist

# Idea 12 focused analysis
claude-flow hive-mind spawn "Investigate Idea 12 (B-6): adaptive immune response ↔ cybersecurity IR. Formalize immune ODE system, identify formal cybersecurity IR model, construct variable mapping, classify morphism. Determine if the widely-cited analogy survives formalization." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,control-theorist

# Batch evaluation of all pairs
claude-flow hive-mind spawn "Evaluate all 10 known bio-eng domain pairs (B-1 through B-10). For each pair: classify morphism type, assign tier, assess catalog readiness. Produce summary matrix and identify the 3 strongest candidates for immediate catalog entry." \
  --queen research-strategic \
  --workers biophysics-modeler,ode-dynamicist,pattern-detector,numerical-analyst,control-theorist
```

### Memory Storage

```bash
# Store domain pair investigation result
claude-flow memory store \
  --key "biomimetics/pair/B-[N]/investigation/$(date +%Y-%m-%d)" \
  --value '{"bio_system": "...", "eng_system": "...", "morphism_type": "...", "tier": N, "catalog_ready": true/false}' \
  --namespace isomorphism-library

# Store batch evaluation summary
claude-flow memory store \
  --key "biomimetics/batch-evaluation/$(date +%Y-%m-%d)" \
  --value '{"pairs_evaluated": 10, "tier1_candidates": [...], "tier2_candidates": [...], "tier3_candidates": [...]}' \
  --namespace isomorphism-library
```

---

## Output Templates

### Morphism Discovery Report

```
MORPHISM DISCOVERY REPORT
Date: [YYYY-MM-DD]
Domain Pair: B-[N] — [Bio System] ↔ [Eng System]
Idea: [8 / 12 / both]

SUMMARY
  Morphism type: [exact / partial / to_investigate]
  Tier: [1 / 2 / 3]
  Catalog ready: [Yes / No]

VARIABLE MAPPING (key correspondences)
  [bio_var_1] ↔ [eng_var_1]
  [bio_var_2] ↔ [eng_var_2]
  ...

STRUCTURAL COMPARISON
  Governing equations match: [Yes / Partially / No]
  Eigenvalue correspondence: [Confirmed / Not confirmed / Not tested]
  Key structural difference: ___

DEGRADATION SUMMARY
  Most robust discretization: ___
  Nonlinear extension: [Preserves / Breaks / Unknown]
  Stochastic extension: [Preserves / Breaks / Unknown]

IMPLICATIONS FOR ISOMORPHISM CATALOG
  Extends catalog by: ___
  Novel contribution: ___

NEXT STEPS
  1. ___
  2. ___
```

### Engineering Transfer Feasibility Assessment

```
ENGINEERING TRANSFER ASSESSMENT
Date: [YYYY-MM-DD]
Source: [Biological system]
Target: [Engineering application]

MORPHISM BASIS
  Domain pair: B-[N]
  Morphism type: [exact / partial]
  Tier: [1 / 2]

TRANSFERABLE INSIGHTS
  1. [Biological mechanism] → [Engineering design principle]
  2. ___

NON-TRANSFERABLE ASPECTS
  1. [Biological feature with no engineering counterpart]
  2. ___

FEASIBILITY: [High / Medium / Low]
CONFIDENCE: [Supported by formal morphism / Suggested by partial morphism / Speculative]
```
