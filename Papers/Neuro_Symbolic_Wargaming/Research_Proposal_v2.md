# Neuro-Symbolic AI for Wargaming, Mission Engineering, and Acquisition Integration

## NATO STO Technical Activity Proposal (TAP)

**Version:** 2.0
**Date:** January 2026
**Classification:** UNCLASSIFIED // FOR OFFICIAL USE ONLY
**Proposed Panel:** SAS (System Analysis and Studies)
**Cross-Panel Relevance:** MSG, HFM, IST

---

## Executive Summary

This Technical Activity Proposal establishes a research program to develop, validate, and transition **neuro-symbolic artificial intelligence** for defense wargaming, mission engineering, and acquisition decision support. The program addresses a critical capability gap: current wargaming practices generate valuable insights but lack the analytical rigor, traceability, and scalability required to systematically inform capability development and acquisition decisions.

### The Problem

NATO and Allied nations invest substantial resources in wargaming to explore operational concepts, test capability hypotheses, and inform defense planning. However:

- **Insights are ephemeral**: Knowledge generated in wargames is rarely captured in reusable, structured forms
- **Analysis is inconsistent**: Different games addressing similar questions produce incomparable results
- **Traceability is weak**: Decision-makers cannot verify how wargame insights connect to specific evidence
- **Scale is limited**: Human-intensive facilitation constrains the number and complexity of games
- **Integration is poor**: Wargaming remains disconnected from formal acquisition processes

### The Solution

Neuro-symbolic AI integrates two reasoning paradigms, with the **symbolic layer serving as the foundational constraint system**:

| Paradigm | Strengths | Limitations | Wargaming Application |
|----------|-----------|-------------|----------------------|
| **Symbolic (FOUNDATION)** | Formal guarantees, explainability, traceability, constraint enforcement | Cannot learn from data alone | Doctrinal compliance, audit trails, formal verification |
| **Neural (AUGMENTATION)** | Pattern learning, generalization, handling ambiguity | Opaque, no inherent guarantees | Scenario generation, pattern recognition, prediction |
| **Integrated** | Neural proposes, symbolic disposes | Research maturity, integration complexity | Credible, traceable, formally verifiable decision support |

**Key Principle:** Neural components operate within boundaries defined by symbolic constraints. The symbolic layer provides NATO-grade formal guarantees while neural components augment human analytical capacity. See *Formal_Verification_Framework.md* for detailed specifications.

### Central Research Question

> **How can neuro-symbolic AI be responsibly integrated into wargaming to produce analytically credible, reusable, and decision-relevant insights that measurably improve capability development and acquisition?**

### Operational Definition: Analytical Credibility

For NATO/defense contexts, "analytically credible" is formally defined as:

```
AnalyticallyCredible(insight) ≡
    hasConfidence(insight, c) ∧ c ≥ 0.7 ∧
    hasCompleteProvenance(insight) ∧
    (SMEValidated(insight) ∨ FormallyVerified(insight)) ∧
    hasComprehensibleExplanation(insight) ∧
    ¬hasContradiction(insight)
```

This requires:
1. **Quantified Confidence**: Calibrated probability ≥ 70% with formal bounds
2. **Complete Traceability**: Every insight traces to wargame evidence
3. **Validation**: Either SME review or formal verification
4. **Explainability**: Comprehensible reasoning chain
5. **Consistency**: No contradictions with existing knowledge

### Proposed Program

- **Duration:** 5 years (3 years R&D, 2 years transition)
- **TRL Progression:** 3 → 8
- **Budget:** €12.5M total (€2.5M/year average)
- **Deliverables:** Validated methodology, operational prototype, trained workforce
- **CDTs:** 6 Cooperative Demonstrations across education, exercises, and acquisition

---

## Part 1: Scientific and Technical Foundation

### 1.1 State of the Art

#### Current AI in Defense Analysis

| Approach | Examples | Strengths | Limitations |
|----------|----------|-----------|-------------|
| Machine Learning | DARPA COMPASS, predictive analytics | Pattern recognition, large-scale data | Black box, no explanation, adversarial vulnerability |
| Expert Systems | JWARS adjudication, doctrine encoders | Explainable, rule-based | Brittle, cannot learn, maintenance burden |
| Agent-Based Models | MANA, ISAAC, WISDOM | Emergent behavior, scenario exploration | Validation challenges, parameter sensitivity |
| Large Language Models | ChatGPT, Claude for analysis | Natural language, broad knowledge | Hallucination, no grounding, inconsistency |

#### The Neuro-Symbolic Frontier

Recent advances in neuro-symbolic AI demonstrate the feasibility of integrated systems:

- **Neural Theorem Provers** (DeepMind): Learning to guide symbolic reasoning
- **Knowledge Graph Embeddings** (IBM, Google): Combining structured knowledge with learned representations
- **Neurosymbolic Concept Learners** (MIT): Learning symbolic concepts from perceptual data
- **Constraint-Guided Generation** (Stanford): Neural generation within symbolic bounds

However, **no existing system** addresses the specific requirements of defense wargaming:
- Doctrinal constraint satisfaction
- Multi-classification security handling
- Human-AI teaming for adjudication
- Acquisition-grade traceability

#### Literature Gap Analysis

| Domain | Existing Work | Gap This Proposal Addresses |
|--------|---------------|----------------------------|
| AI Wargaming | Automated red teaming, scenario generation | Integration with acquisition, traceability |
| Mission Engineering | MBSE tools, requirements management | Wargame-derived validation, gap identification |
| Acquisition Analytics | Cost models, risk analysis | Wargame evidence integration, confidence quantification |
| Explainable AI | Post-hoc explanation, attention visualization | Real-time explanation during wargaming |
| Human-AI Teaming | Automation levels, trust calibration | Wargame facilitator teaming, adjudication |

### 1.2 Theoretical Framework

#### Epistemological Position

This research adopts a **pragmatist epistemology**: knowledge claims are validated through their consequences for action. In the wargaming context:

- An insight is **valid** if it improves decision quality
- A capability gap is **confirmed** if interventions based on it succeed
- AI support is **trustworthy** if users calibrate reliance appropriately

This contrasts with purely rationalist approaches (knowledge from rules alone) and purely empiricist approaches (knowledge from data alone). Neuro-symbolic integration operationalizes pragmatist epistemology by combining rule-based reasoning with learned patterns, validated through operational outcomes.

#### Conceptual Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CAPABILITY DEVELOPMENT CYCLE                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐          ┌───────────────┐          ┌───────────────┐
│   MISSION     │          │   WARGAMING   │          │  ACQUISITION  │
│  ENGINEERING  │◄────────►│               │◄────────►│               │
│               │          │               │          │               │
│ Gap Questions │          │ Gap Testing   │          │ Gap Closure   │
│ MoE/MoP       │          │ Evidence Gen  │          │ Investment    │
│ Scenarios     │          │ Insight Ext   │          │ Justification │
└───────┬───────┘          └───────┬───────┘          └───────┬───────┘
        │                           │                           │
        └───────────────────────────┼───────────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │     NEURO-SYMBOLIC CORE       │
                    ├───────────────────────────────┤
                    │  Neural: Learn, Generate,     │
                    │          Predict, Recognize   │
                    │                               │
                    │  Symbolic: Constrain, Trace,  │
                    │            Explain, Validate  │
                    │                               │
                    │  Integration: Ground learning │
                    │               in knowledge,   │
                    │               explain with    │
                    │               evidence        │
                    └───────────────────────────────┘
```

#### Design Principles

1. **Human Accountability**: AI augments human judgment; humans remain accountable for decisions
2. **Traceable Evidence**: Every AI output links to specific inputs, rules, and learned patterns
3. **Graceful Degradation**: System remains useful when AI components fail or are unavailable
4. **Security by Design**: Classification handling built into architecture, not bolted on
5. **Interoperability First**: NATO standards compliance from inception
6. **Continuous Validation**: Ongoing testing against human expert judgment

### 1.3 Research Questions

#### Primary Research Questions

**RQ1: Methodological Foundations**
> What methodological standards ensure that AI-augmented wargaming produces analytically credible insights suitable for acquisition decisions?

- RQ1.1: What wargaming lifecycle elements are amenable to neuro-symbolic augmentation?
- RQ1.2: How are assumptions, limitations, and uncertainty documented and communicated?
- RQ1.3: What validation protocols establish confidence in AI-generated insights?

**RQ2: Human-AI Integration**
> How should humans and AI systems collaborate during wargaming to maximize insight quality while maintaining human accountability?

- RQ2.1: What cognitive roles should AI play (facilitator, challenger, synthesizer, recorder)?
- RQ2.2: How does AI involvement affect cognitive biases (anchoring, groupthink, confirmation)?
- RQ2.3: What training enables appropriate trust calibration?

**RQ3: Knowledge Architecture**
> How should wargaming knowledge be structured to enable cumulative learning across games, contexts, and time?

- RQ3.1: What ontological commitments support cross-game synthesis?
- RQ3.2: How is provenance maintained from raw gameplay to strategic insight?
- RQ3.3: What mechanisms enable AI learning without compromising security?

**RQ4: Acquisition Integration**
> How can wargame-derived insights be formalized to meet acquisition decision-making requirements?

- RQ4.1: What evidence standards satisfy acquisition authorities?
- RQ4.2: How is confidence quantified and communicated?
- RQ4.3: What interfaces connect wargaming to NDPP and national acquisition processes?

**RQ5: Formal Methods for Wargaming AI** *(NEW)*
> What formal verification methods ensure NATO-grade guarantees for AI-augmented wargaming?

- RQ5.1: What safety and liveness properties must the system satisfy?
- RQ5.2: How can model checking verify temporal properties at scale?
- RQ5.3: What theorem proving approach establishes correctness claims?
- RQ5.4: How is the "neural proposes, symbolic disposes" pattern formally specified?
- RQ5.5: What certification pathway aligns with defense acquisition standards?

#### Secondary Research Questions

**RQ5: Scalability and Efficiency**
- How much can AI reduce wargame design and execution time?
- What is the minimum human involvement for credible results?
- How do costs scale with complexity and classification level?

**RQ6: Adversarial Robustness**
- How can AI-supported wargaming resist manipulation by participants?
- What are failure modes of neuro-symbolic systems in adversarial contexts?
- How is system integrity validated?

**RQ7: Cross-Cultural Validity**
- How do neuro-symbolic methods perform across different national doctrines?
- What adaptations are required for multinational coalition wargaming?
- How is linguistic and conceptual interoperability achieved?

**RQ8: Ethical and Legal Compliance**
- What safeguards prevent AI from generating harmful scenarios?
- How is compliance with IHL and ROE ensured?
- What governance frameworks suit multinational AI-enabled analysis?

---

## Part 2: Technical Approach

### 2.1 System Architecture

#### Overview

The neuro-symbolic wargaming system comprises five integrated layers:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                             │
│  Wargame Designer │ Facilitator │ Analyst │ Sponsor │ Acquisition       │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
┌─────────────────────────────────────┴───────────────────────────────────┐
│                      EXPLANATION & TRUST LAYER                           │
│  Natural Language │ Visualization │ Confidence │ Provenance │ Audit     │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
┌─────────────────────────────────────┴───────────────────────────────────┐
│                    NEURO-SYMBOLIC INTEGRATION LAYER                      │
│  Symbol Grounding │ Neural-Symbolic Coupling │ Confidence Calibration   │
└──────────┬──────────────────────────────────────────────┬───────────────┘
           │                                              │
┌──────────┴──────────┐                      ┌────────────┴────────────┐
│    NEURAL LAYER     │                      │    SYMBOLIC LAYER       │
├─────────────────────┤                      ├─────────────────────────┤
│ Scenario Generator  │                      │ Knowledge Graph         │
│ Pattern Learner     │                      │ Reasoning Engine        │
│ Prediction Engine   │                      │ Constraint Manager      │
│ Adversary Modeler   │                      │ Traceability Manager    │
│ Optimization Engine │                      │ Explanation Engine      │
└──────────┬──────────┘                      └────────────┬────────────┘
           │                                              │
┌──────────┴──────────────────────────────────────────────┴───────────────┐
│                         DATA & KNOWLEDGE LAYER                           │
│  Wargame Repository │ Doctrine Base │ Historical Data │ M&S Interfaces  │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Neural Components

| Component | Function | Architecture | Training Data |
|-----------|----------|--------------|---------------|
| **Scenario Generator** | Create diverse, challenging scenarios | Transformer + constraints | Historical scenarios, doctrine, SME feedback |
| **Pattern Learner** | Extract insights from gameplay | Graph neural network | Annotated game transcripts |
| **Prediction Engine** | Forecast outcomes, identify risks | Ensemble models | Wargame outcomes, operational data |
| **Adversary Modeler** | Generate realistic opponent behavior | Reinforcement learning | Red team data, historical adversaries |
| **Optimization Engine** | Explore trade-spaces, optimize COAs | Evolutionary algorithms | Objective functions, constraints |

#### Symbolic Components

| Component | Function | Formalism | Knowledge Sources |
|-----------|----------|-----------|-------------------|
| **Knowledge Graph** | Structure domain knowledge | OWL 2 + SHACL | Doctrine, NDPP, wargame ontology |
| **Reasoning Engine** | Derive conclusions, check consistency | Description logic + rules | Domain axioms, inference rules |
| **Constraint Manager** | Enforce doctrinal and legal bounds | Constraint satisfaction | ROE, IHL, classification rules |
| **Traceability Manager** | Maintain evidence chains | Provenance graphs | All system interactions |
| **Explanation Engine** | Generate human-understandable rationale | Template + neural | Explanation patterns, user models |

#### Integration Mechanisms

**Symbol Grounding**: Neural representations are anchored to symbolic concepts through:
- Embedding alignment with knowledge graph entities
- Attention mechanisms guided by symbolic structure
- Loss functions incorporating symbolic constraints

**Neural-Symbolic Coupling**: Bidirectional information flow:
- Symbolic → Neural: Constraints guide generation, knowledge informs learning
- Neural → Symbolic: Learned patterns suggest new rules, embeddings enrich reasoning

**Confidence Calibration**: Uncertainty quantification through:
- Bayesian neural networks for epistemic uncertainty
- Symbolic consistency checking for logical uncertainty
- Human validation loops for calibration

### 2.2 Knowledge Architecture

#### Ontology Design

The wargaming knowledge graph employs a modular ontology:

**Core Modules:**
- `wargame-core`: Games, turns, moves, outcomes
- `scenario-model`: Situations, forces, objectives, constraints
- `insight-model`: Observations, patterns, hypotheses, conclusions
- `capability-model`: Gaps, requirements, solutions, measures

**Domain Extensions:**
- `nato-doctrine`: NATO operational concepts, command structures
- `acquisition-model`: NDPP alignment, capability targets
- `security-model`: Classification, handling, releasability

**Alignment Mappings:**
- NDPP capability taxonomy
- NATO Architecture Framework (NAF)
- US DoDAF / UK MODAF equivalences

#### Provenance Model

Every knowledge artifact maintains:

```
Artifact
├── Content (the actual insight, scenario, etc.)
├── Derivation
│   ├── Sources (what it came from)
│   ├── Method (how it was derived)
│   └── Agents (who/what performed derivation)
├── Confidence
│   ├── Epistemic (knowledge uncertainty)
│   ├── Aleatory (inherent randomness)
│   └── Calibration (validation status)
├── Validity
│   ├── Temporal (when valid)
│   ├── Contextual (where valid)
│   └── Conditional (under what assumptions)
└── Governance
    ├── Classification
    ├── Releasability
    └── Handling instructions
```

### 2.3 Data Strategy

#### Data Sources

| Category | Sources | Classification | Volume |
|----------|---------|----------------|--------|
| **Historical Wargames** | RAND, CNA, national archives | Varies (mostly UNCLASS) | 500+ games |
| **Doctrine** | NATO STANAGs, national publications | UNCLASS to RESTRICTED | 1000+ documents |
| **Operational Data** | Lessons learned, AARs | RESTRICTED to SECRET | Limited access |
| **Synthetic Data** | AI-generated scenarios | UNCLASS (by design) | Unlimited |
| **Expert Knowledge** | SME elicitation, structured interviews | UNCLASS | 100+ sessions |

#### Synthetic Data Generation

To address data scarcity while maintaining security:

1. **Scenario Synthesis**: Generate doctrinally plausible but fictional scenarios
2. **Gameplay Simulation**: Agent-based models produce realistic game trajectories
3. **Adversarial Augmentation**: Perturb real data to create variations
4. **Expert Validation**: SMEs verify synthetic data quality

#### Data Governance

| Principle | Implementation |
|-----------|----------------|
| **Minimization** | Collect only data necessary for research objectives |
| **Purpose Limitation** | Use data only for specified wargaming research |
| **Security** | Classification-appropriate storage and handling |
| **Retention** | Delete raw data after model training; retain only models and metadata |
| **Auditability** | Log all data access and transformations |

### 2.4 Human-AI Teaming Model

#### Cognitive Role Allocation

| Role | Human Responsibilities | AI Responsibilities |
|------|------------------------|---------------------|
| **Design** | Objectives, scope, key questions | Scenario generation, force balancing, gap coverage |
| **Facilitation** | Player engagement, clarification, atmosphere | Real-time analysis, consistency checking, time management |
| **Adjudication** | Final decisions, edge cases, player disputes | Outcome calculation, precedent retrieval, option generation |
| **Analysis** | Interpretation, contextualization, recommendations | Pattern extraction, cross-game synthesis, confidence estimation |
| **Reporting** | Narrative, strategic framing, stakeholder communication | Evidence compilation, visualization, traceability documentation |

#### Trust Calibration Framework

**Appropriate Trust**: Users should rely on AI when it is likely correct and override when it is likely wrong.

| AI Confidence | AI Accuracy | Appropriate Response |
|---------------|-------------|---------------------|
| High | High | Accept AI recommendation |
| High | Low | **Overtrust risk** - additional validation needed |
| Low | High | **Undertrust risk** - calibration training needed |
| Low | Low | Human judgment with AI as input |

**Calibration Mechanisms:**
- Confidence displays with historical accuracy
- Explanation of reasoning for user verification
- Periodic calibration exercises with known answers
- Feedback loops to improve AI calibration

#### Workload Management

AI should reduce, not increase, cognitive workload:

| Phase | Without AI | With AI | Reduction Target |
|-------|------------|---------|------------------|
| Scenario Development | 40 hours | 16 hours | 60% |
| Game Execution | Real-time | Real-time | 0% (maintain human engagement) |
| Post-Game Analysis | 80 hours | 32 hours | 60% |
| Report Generation | 40 hours | 16 hours | 60% |
| Cross-Game Synthesis | 120 hours | 24 hours | 80% |

### 2.5 Security Architecture

#### Multi-Level Security

The system supports simultaneous operation across classification levels:

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNCLASSIFIED DOMAIN                           │
│  Training, Research, PME, Unclassified Wargames                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Full AI capability, cloud deployment, open research    │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │ One-way data diode
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESTRICTED DOMAIN                             │
│  Exercise Support, Analytical Wargames                          │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  AI with restricted training, on-premise deployment     │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │ One-way data diode
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SECRET DOMAIN                                 │
│  Operational Wargames, Capability Assessment                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Symbolic only (no neural learning), air-gapped         │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

#### Security Principles

1. **Train Low, Deploy High**: Neural models trained on unclassified data, deployed with classified knowledge graphs
2. **Symbolic Security**: Classification rules encoded symbolically, enforced at inference time
3. **Audit Everything**: Complete logging of all AI operations for security review
4. **Human in the Loop**: No AI outputs released without human review at classification boundaries

### 2.6 Interoperability

#### NATO Standards Compliance

| Standard | Relevance | Compliance Approach |
|----------|-----------|---------------------|
| STANAG 4774/4778 | Metadata binding | Native support in knowledge graph |
| FMN Spiral | Federated mission networking | Service interfaces aligned |
| NIEM | Information exchange | Ontology mappings |
| MSDL | Scenario definition | Import/export capability |
| C-BML | Command and control | Interface adapter |

#### M&S Integration

| System Type | Integration Pattern | Data Exchange |
|-------------|---------------------|---------------|
| Constructive (JTLS, JEMM) | Bidirectional API | Scenario injection, outcome extraction |
| Virtual (flight simulators) | Event streaming | Player actions, system states |
| Live (instrumented exercises) | Batch import | Post-exercise data ingest |
| Analytical (spreadsheet models) | File exchange | Scenario parameters, results |

---

## Part 3: Research Program

### 3.1 Work Breakdown Structure

#### Phase 1: Foundation (Year 1)

**WP1.1: Requirements and Architecture** (M1-M6)
- Stakeholder requirements elicitation
- System architecture specification
- Security architecture design
- Interoperability requirements

**WP1.2: Ontology Engineering (FOUNDATIONAL)** (M4-M12)
- Wargaming ontology development using NeOn methodology
- NATO standards alignment (MIP DEM, JC3IEDM, APP-6, STANAG 4774/4778)
- Formal axiomatization of domain concepts
- OWL 2 profile selection with decidability analysis
- Competency question definition and validation
- See **Ontology_Engineering_Strategy.md** for detailed methodology

**WP1.2b: Formal Verification Foundation** (M6-M12)
- Safety/liveness property specification (LTL/MTL)
- Model checking infrastructure (NuSMV/UPPAAL)
- Theorem proving setup (Isabelle/HOL)
- Formal interface contracts
- See **Formal_Verification_Framework.md** for detailed approach

**WP1.3: Baseline Establishment** (M6-M12)
- Current practice documentation
- Performance baseline measurement
- Evaluation framework development
- Ethics review and approval

**Milestone M1**: Architecture Review (M6)
**Milestone M2**: TRL 4 Assessment (M12)

#### Phase 2: Development (Year 2)

**WP2.1: Neural Component Development** (M13-M24)
- Scenario generator implementation
- Pattern learner training
- Prediction engine development
- Adversary modeler prototype

**WP2.2: Symbolic Component Development** (M13-M24)
- Reasoning engine implementation
- Constraint manager development
- Traceability system implementation
- Explanation engine prototype

**WP2.3: Integration Development** (M18-M24)
- Symbol grounding implementation
- Neural-symbolic coupling
- Confidence calibration
- User interface development

**WP2.4: Pilot Preparation** (M18-M24)
- CDT-01 planning with NDC
- Training material development
- Evaluation instrument design
- Security accreditation (UNCLASS)

**Milestone M3**: Integration Demo (M18)
**Milestone M4**: TRL 5 Assessment (M24)

#### Phase 3: Validation (Year 3)

**WP3.1: CDT-01 SCHOLAR Execution** (M25-M30)
- NDC pilot wargames (3 iterations)
- User feedback collection
- Performance measurement
- System refinement

**WP3.2: CDT-02 INSIGHT Execution** (M28-M36)
- JWC analytical wargames (4 iterations)
- M&S integration testing
- Cross-game synthesis demonstration
- Analyst workflow integration

**WP3.3: CDT-02b PARTNER Execution** (M28-M36)
- DoD acquisition wargames (3 iterations)
- JCIDS alignment validation
- Cost-benefit analysis
- US transition planning

**WP3.4: Methodology Development** (M25-M36)
- Handbook drafting
- Training curriculum finalization
- Certification framework
- Best practices documentation

**Milestone M5**: CDT-01 Complete (M30)
**Milestone M6**: TRL 6 Assessment (M36)

#### Phase 4: Demonstration (Year 4)

**WP4.1: CDT-03 CWIX Execution** (M37-M42)
- Multinational exercise integration
- 25-nation participation
- Interoperability validation
- Scale testing

**WP4.2: CDT-03b CMX Execution** (M43-M48)
- Crisis management exercise
- Political-military interface
- Decision support demonstration
- Senior leader feedback

**WP4.3: CDT-04 ACQUIRE Execution** (M37-M48)
- NAAG analytical support
- NDPP integration demonstration
- Capability target analysis
- Investment justification

**WP4.4: System Hardening** (M37-M48)
- Security enhancement
- Reliability improvement
- Performance optimization
- Documentation completion

**Milestone M7**: CWIX Demo Complete (M42)
**Milestone M8**: TRL 7 Assessment (M48)

#### Phase 5: Transition (Year 5)

**WP5.1: Operational Transition** (M49-M60)
- NCIA infrastructure deployment
- Production system configuration
- Operations team training
- Help desk establishment

**WP5.2: Training Deployment** (M49-M60)
- NATO-wide e-learning launch
- Train-the-trainer programs
- Certification examinations
- Continuous education

**WP5.3: Governance Establishment** (M49-M60)
- Policy finalization
- Governance body activation
- Audit procedures
- Continuous improvement process

**WP5.4: Sustainment Handover** (M55-M60)
- NCIA operational acceptance
- Sustainment budget activation
- Research-to-operations transition
- Final reporting

**Milestone M9**: IOC Declaration (M54)
**Milestone M10**: FOC Declaration (M60)

### 3.2 Cooperative Demonstrations of Technology

#### CDT Portfolio Summary

| CDT | Name | Year | Host | TRL | Focus |
|-----|------|------|------|-----|-------|
| 01 | SCHOLAR | 2 | NDC Rome | 4→5 | PME integration |
| 02 | INSIGHT | 2-3 | JWC Stavanger | 5→6 | Analytical wargaming |
| 02b | PARTNER | 2-3 | NPS Monterey | 5→6 | DoD acquisition |
| 03 | CWIX | 3 | JFTC Bydgoszcz | 6→7 | Multinational exercise |
| 03b | CMX | 3 | NATO HQ | 6→7 | Crisis management |
| 04 | ACQUIRE | 4 | NAAG | 7→8 | Capability development |

#### CDT Design Principles

Each CDT follows a common structure:

1. **Preparation** (8 weeks): Requirements, customization, training
2. **Execution** (2-4 weeks): Wargame conduct with AI support
3. **Evaluation** (4 weeks): Data analysis, user feedback, lessons learned
4. **Refinement** (4 weeks): System improvement based on findings

#### Success Criteria (All CDTs)

| Metric | Threshold | Target |
|--------|-----------|--------|
| User acceptance (SUS score) | >68 | >80 |
| Task completion rate | >85% | >95% |
| Insight quality (expert rating) | >3.5/5 | >4.0/5 |
| Time reduction vs. baseline | >20% | >40% |
| System availability | >95% | >99% |
| Security incidents | <2 | 0 |

### 3.3 Evaluation Framework

#### Evaluation Philosophy

The evaluation framework employs **mixed methods**:
- Quantitative metrics for performance and efficiency
- Qualitative methods for understanding user experience
- Expert judgment for assessing insight quality
- Longitudinal tracking for operational impact

#### Evaluation Dimensions

**Dimension 1: Technical Performance**
- Accuracy of AI outputs vs. ground truth
- Response time and throughput
- System reliability and availability
- Security compliance

**Dimension 2: User Experience**
- Usability (System Usability Scale)
- Trust calibration (appropriate reliance)
- Cognitive workload (NASA-TLX)
- Learning curve

**Dimension 3: Analytical Quality**
- Insight relevance (expert rating)
- Insight novelty (comparison to non-AI)
- Traceability completeness
- Explanation comprehensibility

**Dimension 4: Operational Impact**
- Decision quality improvement
- Time and cost savings
- Knowledge reuse rate
- Adoption breadth

#### Baseline Comparison

All evaluations compare against baselines:

| Baseline Type | Description | Measurement |
|---------------|-------------|-------------|
| Historical | Past wargames without AI | Archive analysis |
| Concurrent | Parallel non-AI games | Controlled comparison |
| Expert | Human expert performance | SME benchmark |
| Theoretical | Optimal performance bounds | Analytical calculation |

#### Longitudinal Tracking

Beyond immediate CDT evaluation, long-term tracking includes:

- **2-year follow-up**: Did AI-identified gaps receive investment?
- **5-year follow-up**: Did investments address the gaps?
- **Operational validation**: Did capability improvements manifest in exercises/operations?

### 3.4 Risk Management

#### Technical Risks

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Neural model performance insufficient | M | H | Hybrid approaches, graceful degradation to symbolic-only |
| Knowledge graph incomplete | H | M | Incremental development, SME validation, user feedback |
| Integration complexity exceeds estimates | M | H | Modular architecture, early integration testing |
| Security accreditation delays | M | H | Early engagement with NCIA, conservative classification design |
| Interoperability challenges | M | M | Standards-first design, adapter patterns |

#### Organizational Risks

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Stakeholder resistance | H | H | Early engagement, demonstrated value, change management |
| Funding discontinuity | M | C | Multi-year commitment, contingency planning, partner cost-sharing |
| Key personnel departure | M | H | Knowledge management, documentation, team redundancy |
| Policy/governance delays | M | M | Parallel policy track, interim governance |
| Nation non-adoption | M | M | Flexible deployment, national customization |

#### Operational Risks

| Risk | L | I | Mitigation |
|------|---|---|------------|
| User over-reliance on AI | M | H | Trust calibration training, confidence displays, mandatory review |
| AI manipulation by participants | L | H | Adversarial testing, anomaly detection, human oversight |
| Bias in AI recommendations | M | H | Diverse training data, bias audits, explanation review |
| AI failure during critical wargame | L | H | Graceful degradation, manual fallback procedures |
| Scope creep | H | M | Clear scope definition, change control, governance |

#### Risk Response Strategy

- **Avoid**: Redesign to eliminate risk source
- **Transfer**: Assign risk to party best able to manage (e.g., security to NCIA)
- **Mitigate**: Reduce likelihood or impact through specific actions
- **Accept**: Acknowledge risk and prepare contingency response

### 3.5 Ethical Framework

#### Ethical Principles

1. **Human Dignity**: AI must never generate content that degrades or dehumanizes
2. **Proportionality**: AI capabilities proportional to legitimate defense needs
3. **Accountability**: Clear human accountability for all AI-supported decisions
4. **Transparency**: AI operation understandable to users and oversight bodies
5. **Non-Maleficence**: AI must not facilitate war crimes or IHL violations
6. **Fairness**: AI must not discriminate or amplify bias

#### Ethical Review Process

| Stage | Review Body | Focus |
|-------|-------------|-------|
| Design | Ethics Advisory Board | Architecture, data sources, use cases |
| Development | Continuous ethics review | Training data, model behavior, edge cases |
| CDT | Host institution ethics | Human subjects, informed consent |
| Deployment | Governance Board | Operational use boundaries |
| Operation | Ongoing audit | Actual use patterns, incident review |

#### Red Lines

The system will **never**:
- Generate scenarios depicting war crimes or IHL violations as acceptable
- Recommend actions violating ROE or legal constraints
- Process data about specific individuals for targeting
- Operate without human oversight capability
- Claim certainty when uncertainty exists

#### Ethical Scenario Handling

| Scenario Type | AI Role | Human Role |
|---------------|---------|------------|
| Civilian protection | Generate options, check IHL compliance | Select approach, make decision |
| Escalation dynamics | Model consequences, identify risks | Decide escalation/de-escalation |
| Coalition sensitivities | Flag classification issues, suggest alternatives | Navigate political constraints |
| Adversary depiction | Generate plausible behavior | Ensure balanced, non-stereotyped portrayal |

---

## Part 4: Program Management

### 4.1 Organization Structure

#### Governance

```
┌─────────────────────────────────────────────────────────────────┐
│                    NATO STO OVERSIGHT                            │
│                Science & Technology Committee                    │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │     STEERING COMMITTEE     │
                    │  Nations + Organizations   │
                    └─────────────┬─────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
    ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
    │    TECHNICAL    │ │   OPERATIONAL   │ │   ETHICS &      │
    │  ADVISORY GROUP │ │ ADVISORY GROUP  │ │  GOVERNANCE     │
    │                 │ │                 │ │  BOARD          │
    │ - Architecture  │ │ - User needs    │ │ - Responsible AI│
    │ - Standards     │ │ - CDT design    │ │ - Policy        │
    │ - Evaluation    │ │ - Transition    │ │ - Security      │
    └─────────────────┘ └─────────────────┘ └─────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │      PROJECT TEAM          │
                    │                            │
                    │  Lead Nation: [TBD]        │
                    │  Technical Lead            │
                    │  Project Manager           │
                    │  WP Leaders                │
                    └────────────────────────────┘
```

#### Roles and Responsibilities

| Role | Responsibilities | Commitment |
|------|------------------|------------|
| Project Director | Overall leadership, stakeholder relations | 50% FTE |
| Technical Lead | Architecture, technical decisions | 100% FTE |
| Project Manager | Schedule, budget, reporting | 100% FTE |
| WP Leaders (5) | Work package execution | 50% FTE each |
| Researchers (10) | Technical development | 100% FTE each |
| CDT Coordinators (6) | Demonstration planning and execution | 25% FTE each |

### 4.2 Schedule

#### Master Schedule

| Year | Quarter | Major Activities | Milestones |
|------|---------|------------------|------------|
| 1 | Q1 | Project initiation, requirements | Kickoff |
| 1 | Q2 | Architecture development | M1: Architecture Review |
| 1 | Q3 | Knowledge engineering, baseline | |
| 1 | Q4 | Component prototyping | M2: TRL 4 |
| 2 | Q1 | Neural development | |
| 2 | Q2 | Symbolic development, integration start | M3: Integration Demo |
| 2 | Q3 | CDT-01 preparation, pilot testing | |
| 2 | Q4 | CDT-01 execution start | M4: TRL 5 |
| 3 | Q1 | CDT-01 complete, CDT-02/02b start | M5: CDT-01 |
| 3 | Q2 | CDT-02/02b execution | |
| 3 | Q3 | CDT-03 preparation | |
| 3 | Q4 | Methodology finalization | M6: TRL 6 |
| 4 | Q1 | CDT-03 CWIX execution | |
| 4 | Q2 | CDT-03 complete | M7: CWIX |
| 4 | Q3 | CDT-03b CMX, CDT-04 start | |
| 4 | Q4 | System hardening | M8: TRL 7 |
| 5 | Q1 | Transition preparation | |
| 5 | Q2 | IOC activities | M9: IOC |
| 5 | Q3 | FOC activities | |
| 5 | Q4 | Handover complete | M10: FOC |

#### Critical Path

1. Architecture specification → Component development → Integration
2. Knowledge graph population → Reasoning engine → Constraint checking
3. CDT-01 success → CDT-02/03 approval → CDT-04 execution
4. Security accreditation → Classified deployment → Operational transition

### 4.3 Budget

#### Cost Summary (€ Thousands)

| Category | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Total |
|----------|--------|--------|--------|--------|--------|-------|
| Personnel | 1,200 | 1,400 | 1,400 | 1,200 | 800 | 6,000 |
| Equipment | 200 | 300 | 200 | 200 | 100 | 1,000 |
| Travel | 100 | 150 | 200 | 200 | 150 | 800 |
| CDTs | 0 | 300 | 500 | 500 | 200 | 1,500 |
| Subcontracts | 300 | 400 | 300 | 200 | 100 | 1,300 |
| Infrastructure | 100 | 200 | 300 | 400 | 500 | 1,500 |
| Formal Methods | 100 | 200 | 200 | 150 | 100 | 750 |
| Other | 100 | 100 | 100 | 100 | 100 | 500 |
| **Total** | **2,100** | **3,050** | **3,200** | **2,950** | **2,050** | **13,350** |

**Note:** Budget increased by €750K to include formal methods expertise (2 FTE over 5 years) for ontology engineering, model checking, and theorem proving activities essential for NATO-grade formal guarantees.

#### Cost Sharing Model

| Contributor | Year 1-3 | Year 4-5 | Mechanism |
|-------------|----------|----------|-----------|
| Lead Nation | 40% | 30% | Direct funding |
| Participating Nations (5-10) | 40% | 40% | Cost-share |
| NATO Common Funding | 20% | 30% | STO budget |

### 4.4 Quality Management

#### Quality Principles

1. **Fitness for Purpose**: Deliverables meet stakeholder needs
2. **Technical Excellence**: State-of-the-art methods, rigorous validation
3. **Documentation**: Complete, accurate, accessible records
4. **Continuous Improvement**: Learn from every activity

#### Quality Assurance Activities

| Activity | Frequency | Responsibility |
|----------|-----------|----------------|
| Peer review of technical work | Per deliverable | WP leaders |
| External technical review | Annual | Technical Advisory Group |
| User acceptance testing | Per CDT | CDT coordinators |
| Security audit | Semi-annual | NCIA |
| Ethics review | Quarterly | Ethics Board |
| Progress review | Monthly | Steering Committee |

#### Configuration Management

- Version control for all software and documentation
- Change control board for scope changes
- Baseline management at milestones
- Traceability from requirements to implementation

### 4.5 Communication and Reporting

#### Internal Communication

| Forum | Frequency | Participants | Purpose |
|-------|-----------|--------------|---------|
| Project team meeting | Weekly | Core team | Coordination |
| WP leader sync | Bi-weekly | WP leaders + PM | Integration |
| Technical deep-dive | Monthly | Technical team | Problem-solving |
| Steering Committee | Quarterly | All stakeholders | Governance |

#### External Communication

| Product | Frequency | Audience | Classification |
|---------|-----------|----------|----------------|
| Progress report | Quarterly | STO, nations | UNCLASS |
| Technical report | Per milestone | Technical community | UNCLASS |
| CDT report | Per CDT | All stakeholders | UNCLASS/RESTRICTED |
| Final report | End of project | All | UNCLASS |
| Publications | Ongoing | Academic/defense | UNCLASS |

#### Stakeholder Engagement

| Stakeholder | Engagement Mode | Frequency |
|-------------|-----------------|-----------|
| STO/STC | Formal reporting | Quarterly |
| Participating nations | Working group | Bi-monthly |
| CDT hosts | Direct collaboration | Continuous during CDT |
| User community | Workshops, surveys | Semi-annual |
| Academic community | Conferences, publications | Annual |

---

## Part 5: Expected Outcomes and Impact

### 5.1 Deliverables

#### Technical Deliverables

| Deliverable | Description | TRL | Availability |
|-------------|-------------|-----|--------------|
| Neuro-Symbolic Wargaming System | Operational prototype | 7-8 | NATO nations |
| Knowledge Graph | Populated wargaming ontology | N/A | Open (unclassified core) |
| Neural Models | Trained scenario/pattern/prediction models | N/A | Restricted (security) |
| APIs | Interfaces for M&S integration | N/A | NATO standard |
| Security Package | Accreditation documentation | N/A | Restricted |

#### Methodological Deliverables

| Deliverable | Description | Audience |
|-------------|-------------|----------|
| Methodology Handbook | Practitioner guide for AI-augmented wargaming | Wargame designers, facilitators |
| Training Curriculum | 48-hour certification program | All users |
| Evaluation Framework | Methods for assessing AI wargaming | Analysts, evaluators |
| Governance Framework | Policies for responsible AI use | Leaders, policy makers |
| Integration Guide | How to connect with acquisition processes | Acquisition community |

#### Knowledge Deliverables

| Deliverable | Description | Dissemination |
|-------------|-------------|---------------|
| Research reports | Findings from each phase | STO publication |
| CDT reports | Lessons from demonstrations | STO publication |
| Academic papers | Peer-reviewed publications | Journals, conferences |
| Case studies | Detailed examples of AI-augmented wargaming | Handbook appendices |
| Data sets | Synthetic wargame data for research | Research community |

### 5.2 Impact Metrics

#### Short-Term Impact (Years 1-3)

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| Wargames with AI support | 0 | 15 | Project tracking |
| Trained practitioners | 0 | 100 | Certification records |
| Publications | 0 | 10 | Publication database |
| TRL advancement | 3 | 6 | Assessment reviews |
| Nations engaged | 1 | 10 | Participation records |

#### Medium-Term Impact (Years 4-5)

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| Wargames with AI support | 15 | 50 | Usage tracking |
| Trained practitioners | 100 | 500 | Certification records |
| Capability gaps identified | Manual | 3x baseline | Gap database |
| Analysis cycle time | Baseline | -40% | Process metrics |
| Decision confidence | Baseline | +30% | Stakeholder survey |

#### Long-Term Impact (Years 5-10)

| Metric | Target | Measurement |
|--------|--------|-------------|
| NATO-wide adoption | Standard practice | Policy review |
| Acquisition influence | Documented impact | Case studies |
| Capability improvement | Measurable outcomes | Operational assessment |
| Research community | Self-sustaining | Publication/funding trends |
| Commercial transition | Industry adoption | Market analysis |

### 5.3 Transition Pathway

#### Transition Stages

| Stage | Timeline | Activities | Success Criteria |
|-------|----------|------------|------------------|
| **Research** | Y1-3 | Development, CDT-01/02 | TRL 6, methodology validated |
| **Demonstration** | Y3-4 | CDT-03/04, scale testing | TRL 7, multinational success |
| **Pilot Deployment** | Y4-5 | Limited operational use | IOC declared |
| **Full Deployment** | Y5+ | NATO-wide availability | FOC declared |
| **Sustainment** | Y5+ | Operations, updates | Continuous improvement |

#### Transition Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Technology not ready | Conservative TRL gates, fallback to symbolic-only |
| Users not ready | Comprehensive training, phased rollout |
| Infrastructure not ready | Early NCIA engagement, cloud-first design |
| Policy not ready | Parallel governance track, interim measures |
| Funding not ready | Multi-year commitment, transition budget |

### 5.4 Sustainability

#### Technical Sustainability

- **Open Standards**: Build on NATO standards for long-term compatibility
- **Modular Architecture**: Enable component replacement and upgrade
- **Documentation**: Comprehensive technical documentation for maintenance
- **Test Suites**: Automated testing for regression prevention

#### Organizational Sustainability

- **Training Pipeline**: Self-sustaining train-the-trainer model
- **Community of Practice**: Network of practitioners for knowledge sharing
- **Governance Structure**: Permanent governance body for oversight
- **Feedback Loops**: Continuous improvement based on user input

#### Financial Sustainability

- **Operational Budget**: Transition from R&D to operational funding (Y5+)
- **Cost Recovery**: Potential for service-based cost recovery from heavy users
- **Efficiency Gains**: Demonstrated savings justify continued investment
- **Partner Contributions**: National implementations share development costs

---

## Part 6: Conclusion

### 6.1 Summary of Proposal

This Technical Activity Proposal establishes a comprehensive research program to develop and transition neuro-symbolic AI for defense wargaming. The program addresses a critical capability gap: the need for analytically rigorous, traceable, and scalable methods to connect wargaming insights to capability development and acquisition decisions.

**Key Features:**

- **Neuro-Symbolic Integration**: Combines learning capabilities with explainable reasoning
- **Mission Engineering Alignment**: Maps 42 gap questions to wargame validation
- **Acquisition Integration**: Direct connection to NDPP and national processes
- **Responsible AI**: Built-in governance, ethics, and human accountability
- **NATO Interoperability**: Standards-compliant from inception
- **Validated Approach**: Six CDTs across education, exercises, and acquisition

### 6.2 Why Now?

Several factors make this the right time for this research:

1. **AI Maturity**: Neuro-symbolic methods have reached sufficient maturity for defense application
2. **Strategic Need**: Accelerating threat environment demands faster, more rigorous analysis
3. **Resource Constraints**: Limited budgets require better evidence for investment decisions
4. **NATO Momentum**: AI Strategy provides policy framework for responsible adoption
5. **Talent Availability**: Growing AI expertise in defense research community

### 6.3 Why NATO STO?

NATO STO is uniquely positioned to lead this research:

- **Multinational Reach**: Access to diverse perspectives and requirements
- **Operational Connection**: Direct links to operational commands and exercises
- **Standards Authority**: Ability to establish NATO-wide standards
- **Neutrality**: Trusted broker among nations and organizations
- **Track Record**: Proven ability to deliver complex research programs

### 6.4 Call to Action

We invite NATO nations and partner organizations to:

1. **Participate**: Join the research program as contributing nations
2. **Host CDTs**: Offer venues for cooperative demonstrations
3. **Provide Expertise**: Contribute subject matter experts to advisory groups
4. **Share Data**: Make historical wargame data available (appropriately classified)
5. **Adopt Outcomes**: Commit to using validated methods and tools

### 6.5 Contact Information

| Role | Name | Organization | Email |
|------|------|--------------|-------|
| Proposal Lead | [TBD] | [Lead Institution] | [TBD] |
| Technical Lead | [TBD] | [Technical Institution] | [TBD] |
| NATO Liaison | [TBD] | STO | [TBD] |

---

## Appendices

### Appendix A: Acronyms

| Acronym | Definition |
|---------|------------|
| AAR | After Action Report |
| AI | Artificial Intelligence |
| AoA | Analysis of Alternatives |
| C-BML | Coalition Battle Management Language |
| CDT | Cooperative Demonstration of Technology |
| CMX | Crisis Management Exercise |
| COA | Course of Action |
| CWIX | Coalition Warrior Interoperability eXercise |
| FMN | Federated Mission Networking |
| FOC | Full Operational Capability |
| HFM | Human Factors and Medicine (STO Panel) |
| IHL | International Humanitarian Law |
| IOC | Initial Operational Capability |
| IST | Information Systems Technology (STO Panel) |
| JCIDS | Joint Capabilities Integration and Development System |
| JWC | Joint Warfare Centre |
| KRL | Knowledge Readiness Level |
| M&S | Modeling and Simulation |
| MBSE | Model-Based Systems Engineering |
| ME | Mission Engineering |
| MIP | Multilateral Interoperability Programme |
| MoE | Measure of Effectiveness |
| MoP | Measure of Performance |
| MSG | Modelling and Simulation Group (STO Panel) |
| NAAG | NATO Armaments Group |
| NAF | NATO Architecture Framework |
| NCIA | NATO Communications and Information Agency |
| NDC | NATO Defence College |
| NDPP | NATO Defence Planning Process |
| NPS | Naval Postgraduate School |
| OWL | Web Ontology Language |
| PME | Professional Military Education |
| ROE | Rules of Engagement |
| SAS | System Analysis and Studies (STO Panel) |
| SHACL | Shapes Constraint Language |
| SME | Subject Matter Expert |
| STANAG | Standardization Agreement |
| STC | Science and Technology Committee |
| STO | Science and Technology Organization |
| SUS | System Usability Scale |
| TAP | Technical Activity Proposal |
| TRL | Technology Readiness Level |
| WP | Work Package |

### Appendix B: References

[To be populated with full academic and policy references]

### Appendix C: Supporting Documents

The following documents provide detailed specifications referenced in this proposal:

1. **ME_Wargame_Mapping_Matrix.md**: Complete mapping of 42 ME gap questions to wargame designs
2. **Neuro_Symbolic_Architecture_Specification.md**: Detailed technical architecture with formal foundations
3. **Methodology_Handbook_Outline.md**: Practitioner handbook structure
4. **Pilot_Wargame_Designs.md**: Detailed specifications for 5 pilot wargames
5. **Transition_Roadmap.md**: Comprehensive operationalization pathway
6. **NATO_STO_Research_Topics_Expanded.md**: 80 research questions across 10 topics
7. **Ontology_Engineering_Strategy.md**: NeOn methodology adaptation, NATO standards alignment, formal axiomatization, OWL 2 profile selection
8. **Formal_Verification_Framework.md**: Model checking strategy, theorem proving, safety case structure (GSN), certification pathway

### Appendix D: Letters of Support

[To be populated with letters from participating nations and organizations]

### Appendix E: Team Qualifications

[To be populated with CVs and organizational capabilities]

---

*Document prepared for NATO STO Technical Activity Proposal submission*

*Version 2.0 - January 2026*
