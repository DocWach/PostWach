# DARPA CLARA Proposal Diagrams
# Morphism-Grounded Compositional Assurance for Autonomous AI Systems

All diagrams are valid Mermaid syntax. Render with any Mermaid-compatible tool
(VS Code preview, mermaid.live, GitHub markdown, etc.).

---

## Diagram 1: The Big Picture -- What Is the Circuit Breaker?

A high-level overview accessible to any audience. The AI Circuit Breaker
continuously measures how well an AI's internal model matches reality,
then triggers a graduated response when quality degrades.

```mermaid
%% Diagram 1: The Big Picture
%% Audience: anyone, no prior technical knowledge needed

flowchart LR
    A["AI System<br/>makes a prediction"] --> B["Circuit Breaker<br/>measures prediction<br/>quality against reality"]
    B --> C{"How good<br/>is the match?"}

    C -->|"Excellent"| D["NORMAL<br/>Full autonomy"]
    C -->|"Slightly off"| E["CAUTION<br/>Flag for review"]
    C -->|"Degraded"| F["RESTRICT<br/>Limit AI actions"]
    C -->|"Poor"| G["HALT<br/>Suspend AI decisions"]
    C -->|"Dangerous"| H["LOCKDOWN<br/>Human takes over"]

    style A fill:#4a90d9,stroke:#2c5f8a,color:#fff
    style B fill:#f5a623,stroke:#c17d15,color:#fff
    style D fill:#7ed321,stroke:#5a9a18,color:#fff
    style E fill:#f8e71c,stroke:#c4b916,color:#333
    style F fill:#f5a623,stroke:#c17d15,color:#fff
    style G fill:#d0021b,stroke:#9a0114,color:#fff
    style H fill:#4a0011,stroke:#2a000a,color:#fff
```

---

## Diagram 2: The Morphism Chain (ECG Domain)

Shows how information flows from the patient's heart to a clinical
classification, passing through five transformation stages (h1 through h5).
Each link has its own morphism quality D_h = (D_s, D_b). The composition
theorem says the weakest structural link bounds the whole chain.

```mermaid
%% Diagram 2: The Morphism Chain (ECG Domain)
%% Each arrow is a morphism h_i with its own quality measure D_h

flowchart LR
    subgraph Chain["Morphism Chain: Heart to Classification"]
        direction LR
        Z1["Heart<br/>(physical system)"]
        Z2["Electrode Signal<br/>(sensor observation)"]
        Z3["Digital Signal<br/>(ADC output)"]
        Z4["Filtered Signal<br/>(processed)"]
        Z5["Features<br/>(extracted)"]
        Z6["Classification<br/>(diagnosis)"]

        Z1 -->|"h1<br/>D_h1 = (D_s1, D_b1)"| Z2
        Z2 -->|"h2<br/>D_h2 = (D_s2, D_b2)"| Z3
        Z3 -->|"h3<br/>D_h3 = (D_s3, D_b3)"| Z4
        Z4 -->|"h4<br/>D_h4 = (D_s4, D_b4)"| Z5
        Z5 -->|"h5<br/>D_h5 = (D_s5, D_b5)"| Z6
    end

    subgraph Theorem["Composition Theorem"]
        T1["D_s total >= max of all D_s_i<br/>(weakest structural link dominates)"]
        T2["D_b total <= sum of all D_b_i<br/>(behavioral errors accumulate)"]
    end

    Chain -.->|"bounds"| Theorem

    style Z1 fill:#e74c3c,stroke:#c0392b,color:#fff
    style Z6 fill:#2ecc71,stroke:#27ae60,color:#fff
    style T1 fill:#ecf0f1,stroke:#95a5a6,color:#333
    style T2 fill:#ecf0f1,stroke:#95a5a6,color:#333
```

---

## Diagram 3: Two-Axis Morphism Quality

Shows D_s (structural distance) and D_b (behavioral distance) as two
independent axes. Four quadrants characterize different failure modes.
The ideal is the bottom-left corner: D_h = (0, 0).

```mermaid
%% Diagram 3: Two-Axis Morphism Quality
%% D_s = structural distance (0 = bijective, 1 = fully collapsed)
%% D_b = behavioral distance (0 = perfect output match)
%% Quadrants show what each combination means

quadrantChart
    title Two-Axis Morphism Quality (D_s vs D_b)
    x-axis "Low D_s (precise model)" --> "High D_s (coarse model)"
    y-axis "Low D_b (correct outputs)" --> "High D_b (wrong outputs)"

    quadrant-1 "COARSE BUT CORRECT: Model lumps states together but outputs are still accurate. Safe with monitoring."
    quadrant-2 "BAD: Coarse model AND wrong outputs. Circuit breaker should HALT or LOCKDOWN."
    quadrant-3 "GOOD: Structurally faithful AND behaviorally accurate. The isomorphic ideal."
    quadrant-4 "PRECISE BUT WRONG: Model distinguishes states correctly but produces wrong outputs. Dangerous -- looks good internally."

    "Isomorphic ideal": [0.1, 0.1]
    "Typical deployed AI": [0.35, 0.25]
    "Coarse but safe": [0.75, 0.15]
    "Looks good, is not": [0.15, 0.75]
    "Degraded system": [0.7, 0.7]
```

---

## Diagram 4: Five-Layer Architecture

The circuit breaker's five layers, stacked from foundational (Layer 1,
Reference Standards) to human-facing (Layer 5, Underwriting Interface).
Shows where AR and ML components sit, and data flow between layers.

```mermaid
%% Diagram 4: Five-Layer Architecture
%% Bottom-up: foundational to human-facing

flowchart TB
    subgraph L5["Layer 5: Human Underwriting Interface"]
        L5a["SPC dashboards<br/>(D_s and D_b charts)"]
        L5b["MTBH reliability panel"]
        L5c["Audit trail<br/>(PROV-O, queryable)"]
    end

    subgraph L4["Layer 4: Closed-Loop Morphism Maintenance"]
        L4a["Positive/negative<br/>learning pipelines"]
        L4b["Ontology Enhancement Gate<br/>(SHACL + SPARQL checks)"]
        L4c["Bounded control dynamics<br/>(gain scheduling)"]
    end

    subgraph L3["Layer 3: Statistical Process Control"]
        L3a["Control charts<br/>(Western Electric + CUSUM)"]
        L3b["Data-derived thresholds<br/>(min 25 subgroups)"]
        L3c["Graduated response engine<br/>(Normal to Lockdown)"]
    end

    subgraph L2["Layer 2: Morphism Instruments"]
        L2a["D_s instrument<br/>(structural fidelity)<br/>AR: OWL ontology<br/>ML: embedding distance"]
        L2b["D_b instrument<br/>(behavioral distance)<br/>sensor ground truth"]
        L2c["d_cos monitor<br/>(runtime sentinel)<br/>ML: cosine alignment"]
        L2d["MTBH tracker<br/>(longitudinal reliability)"]
    end

    subgraph L1["Layer 1: Reference Standards"]
        L1a["Domain ontologies<br/>(cardiac electrophysiology)<br/>AR: OWL 2 DL"]
        L1b["Sensor calibration<br/>standards"]
        L1c["Clinical guidelines<br/>(AHA/ACC, AAMI)"]
        L1d["Staged references<br/>for each chain link"]
    end

    L1 -->|"reference values"| L2
    L2 -->|"D_h measurements"| L3
    L3 -->|"verdicts + trends"| L4
    L3 -->|"status + alerts"| L5
    L4 -->|"updated thresholds"| L3
    L4 -->|"ontology updates"| L1

    style L5 fill:#3498db,stroke:#2980b9,color:#fff
    style L4 fill:#9b59b6,stroke:#8e44ad,color:#fff
    style L3 fill:#f39c12,stroke:#d68910,color:#fff
    style L2 fill:#e74c3c,stroke:#c0392b,color:#fff
    style L1 fill:#2ecc71,stroke:#27ae60,color:#fff
```

---

## Diagram 5: AR-ML Tight Coupling

Shows the bidirectional relationship between Automated Reasoning (AR) and
Machine Learning (ML). This is NOT "AR bolted on" as a post-hoc filter.
AR shapes ML training through the loss function, and ML provides runtime
evidence that AR reasons over.

```mermaid
%% Diagram 5: AR-ML Tight Coupling
%% Key point: AR is IN the loss function, not just an output filter

flowchart TB
    subgraph AR["Automated Reasoning (AR)"]
        AR1["OWL 2 DL Ontology<br/>(domain structure,<br/>morphism types)"]
        AR2["Bayesian Logic Programs<br/>(ProbLog2: probabilistic<br/>morphism inference)"]
        AR3["SHACL Shapes<br/>(composition<br/>preconditions)"]
    end

    subgraph ML["Machine Learning (ML)"]
        ML1["Transformer Encoder<br/>(ECG signal to<br/>diagnostic embeddings)"]
        ML2["Embedding Space<br/>(AR-defined: respects<br/>ontology state distinctions)"]
        ML3["Training Loss Function<br/>(includes morphism<br/>quality penalties)"]
    end

    subgraph coupling["Tight Coupling (not bolt-on)"]
        direction TB
        C1["AR shapes ML training:<br/>loss = task_loss + structural_penalty<br/>+ behavioral_penalty + composition_penalty"]
        C2["AR constrains ML inference:<br/>every output gets a morphism<br/>quality certificate (proof tree)"]
        C3["ML informs AR reasoning:<br/>embedding distances and sensor<br/>comparisons as Bayesian evidence"]
    end

    AR1 -->|"defines valid<br/>state distinctions"| ML2
    AR3 -->|"composition<br/>constraints"| ML3
    AR1 -->|"structural<br/>penalty terms"| ML3
    ML1 -->|"embedding<br/>distances"| AR2
    ML1 -->|"runtime<br/>evidence"| AR2
    AR2 -->|"composition<br/>verdicts"| ML1

    style AR fill:#2980b9,stroke:#1a5276,color:#fff
    style ML fill:#c0392b,stroke:#7b241c,color:#fff
    style coupling fill:#f9e79f,stroke:#b7950b,color:#333
```

---

## Diagram 6: Terminology Hierarchy

Shows how all the morphism quality terms relate to each other.
D_h is the master vector. D_s and D_b are its two axes (design-time
and runtime). d_cos is a fast runtime proxy. MTBH is longitudinal.

```mermaid
%% Diagram 6: Terminology Hierarchy
%% Clarifies which metrics are design-time, runtime, or both

mindmap
    root(("D_h = (D_s, D_b)<br/>Homomorphic Distance<br/>[design-time + runtime]"))
        D_s["D_s: Structural Distance<br/>= 1 minus sigma<br/>How far from bijective?<br/>[design-time, composable]"]
            sigma["sigma: Degree of Homomorphism<br/>Average reciprocal mapping<br/>cardinality across states<br/>[design-time]"]
        D_b["D_b: Behavioral Distance<br/>= max output deviation<br/>How far are outputs?<br/>[runtime, accumulates]"]
        d_cos["d_cos: Cosine Alignment<br/>= 1 minus cos(I, N_o)<br/>Fast per-inference sentinel<br/>[runtime only]<br/>Correlates with D_h<br/>but does NOT decompose"]
        MTBH["MTBH: Mean Time Between<br/>Morphism Quality Exceedances<br/>Longitudinal reliability<br/>[runtime, trailing indicator]"]
```

---

## Diagram 7: Phase 1 / Phase 2 Workflow

24-month program timeline. Phase 1 (months 1-15) proves the composition
theorem on a single ECG task. Phase 2 (months 16-24) deepens with a
second ML kind, full pipeline, and domain-transfer analysis.

```mermaid
%% Diagram 7: Phase 1 / Phase 2 Workflow (24 months)
%% Key milestones, demos, and hackathons marked

gantt
    title CLARA Program Timeline (24 Months)
    dateFormat YYYY-MM
    axisFormat %b %Y

    section Phase 1: Prove Composition (15 mo, $1.1M)
    Kickoff + data access               :milestone, m1, 2027-01, 0d
    Theory + ECG ontology                :t1, 2027-01, 4M
    Progress report + SOA baselines      :milestone, m3, 2027-03, 0d
    Single-task AR+ML prototype          :t2, 2027-04, 5M
    Demo: initial AR-ML capability       :milestone, m6, 2027-06, 0d
    Composition experiments              :t3, 2027-08, 5M
    Demo: composed AR-ML capability      :milestone, m9, 2027-09, 0d
    Hackathon prep + inter-performer     :t4, 2027-09, 4M
    Hackathon 1                          :milestone, m12, 2027-12, 0d
    Progress report                      :milestone, m12b, 2027-12, 0d
    Phase 1 closeout                     :t5, 2027-12, 3M
    Phase 1 final deliverable            :milestone, m15, 2028-03, 0d

    section Phase 2: Deepen and Scale (9 mo, $0.75M)
    Second ML kind + AR-constrained training :t6, 2028-04, 3M
    Demo: extended AR-ML (3 kinds)       :milestone, m18, 2028-06, 0d
    Full ECG pipeline + generalization   :t7, 2028-07, 3M
    Demo: three-task composition         :milestone, m21, 2028-09, 0d
    Hackathon 2                          :milestone, m22, 2028-10, 0d
    Domain-transfer analysis + closeout  :t8, 2028-10, 3M
    Phase 2 final deliverable            :milestone, m24, 2028-12, 0d

    section Key Decision Points
    Phase 1/2 transition gate            :milestone, gate, 2028-03, 0d
```

---

## Diagram 8: Composition Theorem Visual

Shows two component tasks (Classification and Guideline Compliance),
each with their own morphism quality D_h, composing into an end-to-end
monitoring system. The composition bounds are shown explicitly.

```mermaid
%% Diagram 8: Composition Theorem Visual
%% Two tasks compose into a third, with formal bounds on total quality

flowchart TB
    subgraph Task1["Task 1: Arrhythmia Classification"]
        T1_desc["ML: Transformer classifies ECG rhythm<br/>AR: Verifies electrophysiology constraints"]
        T1_metric["D_s1 = structural distance<br/>D_b1 = behavioral distance"]
    end

    subgraph Task2["Task 2: Guideline Compliance"]
        T2_desc["ML: Predicts alert priority<br/>AR: Validates against AHA/ACC protocols"]
        T2_metric["D_s2 = structural distance<br/>D_b2 = behavioral distance"]
    end

    subgraph Compose["Composition Theorem"]
        direction TB
        C_struct["Structural bound:<br/>D_s_total >= max(D_s1, D_s2)<br/>The weakest link dominates"]
        C_behav["Behavioral bound:<br/>D_b_total <= D_b1 + D_b2<br/>Errors accumulate additively"]
    end

    subgraph Task3["Task 3: End-to-End Patient Monitoring"]
        T3_desc["Composed pipeline: Classification feeds<br/>Guideline Compliance feeds Graduated Response"]
        T3_metric["D_s_total: formally bounded below<br/>D_b_total: formally bounded above<br/>If either subsystem degrades,<br/>total assurance degrades within bounds"]
    end

    Task1 -->|"output: classified rhythm<br/>+ morphism certificate"| Task2
    Task1 --> Compose
    Task2 --> Compose
    Compose -->|"formal guarantees"| Task3

    subgraph Example["Concrete Example"]
        Ex1["If D_s1 = 0.05 and D_s2 = 0.12<br/>then D_s_total >= 0.12<br/>(guideline compliance is the bottleneck)"]
        Ex2["If D_b1 = 0.03 and D_b2 = 0.04<br/>then D_b_total <= 0.07<br/>(errors add up, still within tolerance)"]
    end

    Task3 -.-> Example

    style Task1 fill:#3498db,stroke:#2471a3,color:#fff
    style Task2 fill:#2ecc71,stroke:#229954,color:#fff
    style Compose fill:#f9e79f,stroke:#b7950b,color:#333
    style Task3 fill:#8e44ad,stroke:#6c3483,color:#fff
    style Example fill:#ecf0f1,stroke:#95a5a6,color:#333
```
