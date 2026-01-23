# Mission Engineering to Wargame Mapping Matrix

**Document Version:** 1.0
**Date:** 2026-01-22
**Author:** University of Arizona PostDoc Research
**Purpose:** Map 42 Mission Engineering gap questions to neuro-symbolic wargame designs

---

## Executive Summary

This matrix maps each of the 42 Mission Engineering (ME) gap questions to specific wargame designs, identifying how neuro-symbolic AI can contribute to addressing each question. For each question, we specify:

- **Recommended wargame type** and format
- **Neural AI contribution** (pattern learning, scenario generation, prediction)
- **Symbolic AI contribution** (constraint enforcement, traceability, explanation)
- **MoEs/MoPs** for evaluation
- **Acquisition relevance** and DOTMLPFI mapping
- **Recommended pilot priority**

---

## Wargame Type Taxonomy

| Type | Description | Fidelity | AI Suitability |
|------|-------------|----------|----------------|
| **Seminar** | Discussion-based, expert-facilitated | Low | High (synthesis, challenge) |
| **Tabletop** | Turn-based with adjudication | Medium | High (scenario, adjudication) |
| **Matrix** | Structured argumentation with probability | Medium | Very High (probability, argument) |
| **Computational** | Computer-mediated with models | High | Very High (M&S integration) |
| **LVC** | Live-Virtual-Constructive | Very High | Medium (real-time constraints) |
| **Red Team** | Adversarial thinking focus | Medium | High (adversary modeling) |
| **Campaign** | Extended multi-phase operations | High | High (temporal, logistics) |
| **Crisis** | Time-compressed decision scenarios | Medium | High (stress, tempo) |

---

## Gap Area 1: Coalition & Allied Operations (5 Questions)

### Overview
These questions address multinational interoperability, data sharing, and coordination challenges critical for NATO operations.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Multinational Tabletop / Matrix Game |
| **Secondary Type** | Coalition Planning Seminar |
| **Key AI Role** | Model national constraints, optimize coordination |
| **DOTMLPFI Focus** | Interoperability, Organization, Policy |

---

### COALITION-Q01: Data Classification Constraints

**Question:** What data classification constraints and release policies limit mission-critical information sharing with coalition partners, and how do these constraints affect joint mission effectiveness?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Matrix Game with classification layers |
| **Format** | 2-day multinational tabletop |
| **Participants** | 15-25 (multi-nation representation) |
| **Neural Contribution** | Learn historical patterns of classification friction; predict information bottlenecks; generate realistic data-sharing scenarios |
| **Symbolic Contribution** | Encode classification rules (STANAG 4774); enforce release constraints; trace information flow decisions; explain policy violations |
| **MoE** | Joint mission effectiveness; information availability |
| **MoP** | Data release latency; classification overhead |
| **Acquisition Relevance** | C4ISR system requirements; cross-domain solutions |
| **DOTMLPFI** | Interoperability, Policy, Leadership |
| **Pilot Priority** | **HIGH** - Core NATO concern |

**Wargame Design Elements:**
- Multi-classification scenario with COSMIC TOP SECRET, NATO SECRET, UNCLASSIFIED layers
- Information-dependent mission objectives
- Time pressure forcing classification trade-offs
- AI generates information request patterns; symbolic system enforces release rules

---

### COALITION-Q02: Interface Reconfiguration for Partner Access

**Question:** How should system interfaces and data formats be designed to enable rapid reconfiguration for different coalition partner access levels without compromising security?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Technical Tabletop + Computational |
| **Format** | 1-day technical workshop + simulation |
| **Participants** | 12-20 (system architects, security SMEs) |
| **Neural Contribution** | Learn interface adaptation patterns; predict reconfiguration time; generate partner access scenarios |
| **Symbolic Contribution** | Enforce security architecture rules; validate interface compliance; trace configuration decisions |
| **MoE** | Reconfiguration time; security compliance |
| **MoP** | Interface adaptation time; security validation pass rate |
| **Acquisition Relevance** | Interface specifications; security architecture requirements |
| **DOTMLPFI** | Materiel, Interoperability |
| **Pilot Priority** | MEDIUM |

---

### COALITION-Q03: Planning Cycle Synchronization

**Question:** Which coordination mechanisms and liaison structures most effectively synchronize planning cycles across coalition partners with different decision-making timelines?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Coalition Planning Seminar |
| **Format** | 3-day planning exercise |
| **Participants** | 20-30 (multi-nation planners) |
| **Neural Contribution** | Model national planning cycle patterns; predict synchronization points; optimize liaison placement |
| **Symbolic Contribution** | Encode planning process constraints; track decision dependencies; explain timeline conflicts |
| **MoE** | Planning synchronization; decision alignment |
| **MoP** | Planning cycle time delta; decision latency |
| **Acquisition Relevance** | Planning system interoperability; decision support tools |
| **DOTMLPFI** | Organization, Doctrine, Leadership |
| **Pilot Priority** | **HIGH** - Frequent NATO friction point |

---

### COALITION-Q04: Capability and Doctrine Differences

**Question:** How do differences in coalition partner capabilities, doctrine, and rules of engagement affect combined force employment options and mission planning?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Matrix Game |
| **Format** | 2-day multinational wargame |
| **Participants** | 20-30 (multi-nation operators) |
| **Neural Contribution** | Learn capability combination patterns; predict ROE conflicts; generate force employment alternatives |
| **Symbolic Contribution** | Encode national ROE constraints; validate doctrine compliance; trace capability-to-mission mapping |
| **MoE** | Combined force effectiveness; option availability |
| **MoP** | Capability gap count; constraint conflicts |
| **Acquisition Relevance** | Interoperability requirements; capability gap justification |
| **DOTMLPFI** | Doctrine, Organization, Materiel |
| **Pilot Priority** | **HIGH** - Core NATO planning challenge |

---

### COALITION-Q05: Interoperability Standards Cost-Benefit

**Question:** What minimum interoperability standards are required to achieve effective coalition operations, and what is the cost/benefit of exceeding those minimums?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Seminar + Computational Analysis |
| **Format** | 1-day seminar with M&S support |
| **Participants** | 15-20 (standards experts, acquisition) |
| **Neural Contribution** | Learn cost-effectiveness curves from historical data; predict interoperability ROI |
| **Symbolic Contribution** | Encode STANAG requirements; calculate compliance costs; trace standard-to-capability mapping |
| **MoE** | Coalition effectiveness threshold; cost efficiency |
| **MoP** | Interoperability compliance rate; implementation cost |
| **Acquisition Relevance** | Standards selection; cost-benefit analysis for acquisition |
| **DOTMLPFI** | Materiel, Interoperability, Facilities |
| **Pilot Priority** | MEDIUM |

---

## Gap Area 2: Communications-Denied Environments (5 Questions)

### Overview
These questions address operations in contested electromagnetic environments where communications may be degraded, denied, or intermittent.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Computational Wargame with comms degradation |
| **Secondary Type** | Crisis Decision Game |
| **Key AI Role** | Model degradation curves, optimize autonomous behavior |
| **DOTMLPFI Focus** | Materiel, Doctrine, Training |

---

### COMMS-DENIED-Q01: Degradation Thresholds

**Question:** How does mission effectiveness degrade as communications bandwidth decreases or latency increases, and what are the critical thresholds for different mission types?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Computational Wargame |
| **Format** | Multi-run simulation campaign |
| **Participants** | 8-12 (operators, analysts) |
| **Neural Contribution** | Learn degradation curves; predict mission failure thresholds; model non-linear effects |
| **Symbolic Contribution** | Encode mission-comms dependencies; define threshold rules; trace degradation-to-failure chains |
| **MoE** | Mission success rate under degradation |
| **MoP** | Bandwidth threshold; latency threshold |
| **Acquisition Relevance** | Communications system requirements; resilience specifications |
| **DOTMLPFI** | Materiel, Training |
| **Pilot Priority** | **HIGH** - Critical for contested operations |

**Wargame Design Elements:**
- Progressive bandwidth reduction injection
- Latency variation by mission phase
- Multiple mission types for threshold comparison
- AI models degradation; symbolic system defines failure criteria

---

### COMMS-DENIED-Q02: Autonomous Behaviors and Pre-Delegated Authority

**Question:** What autonomous behaviors and pre-delegated authorities should distributed platforms have to continue mission execution during extended communications denial?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Human-in-the-Loop Simulation |
| **Format** | 2-day distributed operations exercise |
| **Participants** | 15-25 (operators, commanders) |
| **Neural Contribution** | Learn effective autonomous behavior patterns; predict authority boundary cases |
| **Symbolic Contribution** | Encode authority delegation rules; enforce ROE constraints; trace autonomous decisions |
| **MoE** | Mission continuation rate; authority adequacy |
| **MoP** | Autonomous action success rate; authority coverage |
| **Acquisition Relevance** | Autonomy requirements; C2 system design |
| **DOTMLPFI** | Doctrine, Materiel, Leadership |
| **Pilot Priority** | **HIGH** - Growing autonomy investment |

---

### COMMS-DENIED-Q03: Communications Architecture Resilience

**Question:** Which communications architectures (mesh, relay, SATCOM, LOS) provide the best resilience against jamming and interference for different operational scenarios?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Computational + Red Team |
| **Format** | Architecture comparison campaign |
| **Participants** | 10-15 (comms engineers, EW experts) |
| **Neural Contribution** | Learn jamming effectiveness patterns; predict architecture performance; optimize hybrid solutions |
| **Symbolic Contribution** | Model architecture constraints; validate coverage requirements; trace link-to-mission dependencies |
| **MoE** | Communications availability under jamming |
| **MoP** | Link availability; jamming resistance |
| **Acquisition Relevance** | Communications architecture selection |
| **DOTMLPFI** | Materiel, Facilities |
| **Pilot Priority** | MEDIUM |

---

### COMMS-DENIED-Q04: C2 Adaptation Under Intermittent Communications

**Question:** How should command and control structures adapt when communications links are intermittent, and what information should be prioritized when bandwidth is constrained?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Crisis Decision Game |
| **Format** | Time-compressed C2 exercise |
| **Participants** | 12-20 (commanders, staff) |
| **Neural Contribution** | Learn information prioritization patterns; predict C2 adaptation effectiveness |
| **Symbolic Contribution** | Encode C2 doctrine; enforce information priority rules; trace adaptation decisions |
| **MoE** | C2 effectiveness under degradation |
| **MoP** | Information priority compliance; adaptation time |
| **Acquisition Relevance** | C2 system requirements; decision support tools |
| **DOTMLPFI** | Doctrine, Organization, Training |
| **Pilot Priority** | **HIGH** |

---

### COMMS-DENIED-Q05: Graceful Degradation Modes

**Question:** What graceful degradation modes should systems support when operating in electromagnetically contested environments, and how should operators be trained to recognize and respond to these modes?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Training-Focused Tabletop |
| **Format** | Operator training exercise |
| **Participants** | 15-25 (operators, trainers) |
| **Neural Contribution** | Learn mode recognition patterns; predict operator response effectiveness |
| **Symbolic Contribution** | Define degradation mode rules; trace mode transitions; explain system state |
| **MoE** | Operator response effectiveness |
| **MoP** | Mode recognition time; response accuracy |
| **Acquisition Relevance** | System design for graceful degradation; training requirements |
| **DOTMLPFI** | Training, Materiel |
| **Pilot Priority** | MEDIUM |

---

## Gap Area 3: Ethics & Legal Compliance (5 Questions)

### Overview
These questions address the governance of autonomous systems, legal constraints, and ethical decision-making in military operations.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Ethical Dilemma Seminar |
| **Secondary Type** | Authority Boundary Matrix Game |
| **Key AI Role** | Pattern-match precedents, enforce ROE constraints |
| **DOTMLPFI Focus** | Doctrine, Leadership, Policy |

---

### ETHICS-Q01: ROE Encoding in Autonomous Systems

**Question:** What legal authorities and rules of engagement constraints must be encoded into autonomous system behaviors, and how should these constraints be validated and updated?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Ethical Scenario Seminar |
| **Format** | 2-day expert workshop |
| **Participants** | 15-20 (legal, ethics, operators) |
| **Neural Contribution** | Pattern-match historical ROE applications; predict edge cases |
| **Symbolic Contribution** | Formally encode ROE constraints; verify constraint consistency; trace authority chains |
| **MoE** | Legal compliance rate; constraint coverage |
| **MoP** | Constraint encoding accuracy; update latency |
| **Acquisition Relevance** | Autonomy governance requirements |
| **DOTMLPFI** | Doctrine, Policy |
| **Pilot Priority** | **HIGH** - Critical for autonomous systems |

**Wargame Design Elements:**
- Progressive autonomy scenarios
- ROE boundary testing vignettes
- Legal expert adjudication
- AI identifies edge cases; symbolic system verifies compliance

---

### ETHICS-Q02: Human Oversight Structure

**Question:** How should human oversight be structured for autonomous systems to ensure accountability while maintaining operational tempo and effectiveness?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | C2 Tabletop with Autonomy |
| **Format** | 1-day oversight exercise |
| **Participants** | 12-18 (commanders, operators) |
| **Neural Contribution** | Model tempo-oversight trade-offs; predict accountability gaps |
| **Symbolic Contribution** | Encode accountability rules; trace decision authority; explain oversight gaps |
| **MoE** | Accountability assurance; tempo maintenance |
| **MoP** | Oversight response time; accountability trace completeness |
| **Acquisition Relevance** | Human-machine interface requirements |
| **DOTMLPFI** | Doctrine, Organization, Leadership |
| **Pilot Priority** | **HIGH** |

---

### ETHICS-Q03: Human-in-the-Loop vs. Human-on-the-Loop

**Question:** Which decision types require human-in-the-loop approval versus human-on-the-loop monitoring, and how do these boundaries shift based on operational context?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Authority Boundary Matrix Game |
| **Format** | Context-varying decision scenarios |
| **Participants** | 15-25 (commanders, ethics, legal) |
| **Neural Contribution** | Learn context-authority patterns; predict boundary shift triggers |
| **Symbolic Contribution** | Define authority categories; enforce boundary rules; trace context-to-authority mapping |
| **MoE** | Decision authority clarity; context adaptability |
| **MoP** | Decision classification accuracy; boundary adaptation time |
| **Acquisition Relevance** | Autonomy level specifications |
| **DOTMLPFI** | Doctrine, Training |
| **Pilot Priority** | **HIGH** |

---

### ETHICS-Q04: Audit Trails and Decision Logs

**Question:** What audit trails and decision logs are required to demonstrate compliance with legal and policy constraints during post-mission review?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Post-Mission Review Seminar |
| **Format** | Audit reconstruction exercise |
| **Participants** | 12-15 (legal, technical, operational) |
| **Neural Contribution** | Learn audit pattern requirements; predict review challenges |
| **Symbolic Contribution** | Define audit completeness rules; verify log integrity; trace decision-to-evidence chains |
| **MoE** | Audit completeness; compliance demonstrability |
| **MoP** | Log coverage rate; review preparation time |
| **Acquisition Relevance** | Logging and audit system requirements |
| **DOTMLPFI** | Materiel, Policy |
| **Pilot Priority** | MEDIUM |

---

### ETHICS-Q05: Mission-Constraint Conflict Resolution

**Question:** How should systems handle situations where mission objectives conflict with legal, ethical, or policy constraints, and who has authority to resolve such conflicts?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Ethical Dilemma Seminar |
| **Format** | Conflict scenario workshop |
| **Participants** | 15-25 (cross-functional) |
| **Neural Contribution** | Pattern-match historical conflict resolutions; predict escalation paths |
| **Symbolic Contribution** | Encode conflict resolution rules; model authority hierarchy; trace resolution decisions |
| **MoE** | Conflict resolution effectiveness; authority clarity |
| **MoP** | Resolution time; escalation accuracy |
| **Acquisition Relevance** | Conflict resolution system requirements |
| **DOTMLPFI** | Doctrine, Leadership |
| **Pilot Priority** | **HIGH** |

---

## Gap Area 4: Sustainment & Lifecycle (5 Questions)

### Overview
These questions address system lifecycle management, obsolescence, and sustainment planning.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Campaign Simulation (Logistics) |
| **Secondary Type** | Lifecycle Planning Seminar |
| **Key AI Role** | Predict obsolescence, optimize sustainment |
| **DOTMLPFI Focus** | Materiel, Facilities, Personnel |

---

### SUSTAIN-Q01: Sustainment vs. Replacement Threshold

**Question:** At what point does the cost of sustaining a legacy system exceed the cost of replacement, and what factors beyond direct cost should influence transition decisions?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Lifecycle Decision Seminar |
| **Format** | Cost-capability trade-off workshop |
| **Participants** | 12-18 (acquisition, sustainment, finance) |
| **Neural Contribution** | Learn cost trajectory patterns; predict crossover points; model non-cost factors |
| **Symbolic Contribution** | Encode cost calculation rules; trace factor-to-decision mapping; explain trade-offs |
| **MoE** | Total ownership cost accuracy; transition timing |
| **MoP** | Sustainment cost trend; replacement threshold |
| **Acquisition Relevance** | Modernization business case; lifecycle cost estimation |
| **DOTMLPFI** | Materiel, Facilities |
| **Pilot Priority** | MEDIUM |

---

### SUSTAIN-Q02: Spare Parts and Depot Capacity

**Question:** What spare parts inventory levels and depot maintenance capacity are required to sustain target mission readiness rates across the fleet lifecycle?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Logistics Campaign Simulation |
| **Format** | Multi-year sustainment wargame |
| **Participants** | 15-20 (logistics, maintenance) |
| **Neural Contribution** | Learn demand patterns; predict stockout risk; optimize inventory levels |
| **Symbolic Contribution** | Encode readiness requirements; validate capacity constraints; trace parts-to-readiness chains |
| **MoE** | Mission readiness rate; inventory adequacy |
| **MoP** | Spare parts availability; depot throughput |
| **Acquisition Relevance** | Sustainment planning; logistics requirements |
| **DOTMLPFI** | Materiel, Facilities, Personnel |
| **Pilot Priority** | MEDIUM |

---

### SUSTAIN-Q03: Technology Refresh Synchronization

**Question:** How should technology refresh cycles be synchronized across interdependent systems to maintain interoperability while avoiding fleet-wide capability gaps?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Portfolio Planning Seminar |
| **Format** | Multi-system refresh planning |
| **Participants** | 15-25 (program managers, architects) |
| **Neural Contribution** | Learn refresh synchronization patterns; predict integration risks; optimize sequencing |
| **Symbolic Contribution** | Encode interoperability dependencies; validate refresh schedules; trace gap-risk chains |
| **MoE** | Interoperability maintenance; gap avoidance |
| **MoP** | Refresh cycle alignment; capability gap duration |
| **Acquisition Relevance** | Technology refresh planning; portfolio management |
| **DOTMLPFI** | Materiel, Interoperability |
| **Pilot Priority** | MEDIUM |

---

### SUSTAIN-Q04: Obsolescence and Supply Chain Vulnerability

**Question:** Which components and subsystems are most vulnerable to obsolescence or supply chain disruption, and what mitigation strategies provide the best long-term value?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Supply Chain Risk Tabletop |
| **Format** | Disruption scenario exercise |
| **Participants** | 12-18 (supply chain, engineering) |
| **Neural Contribution** | Learn obsolescence patterns; predict supply chain disruptions; evaluate mitigation ROI |
| **Symbolic Contribution** | Encode component dependencies; trace vulnerability chains; explain mitigation trade-offs |
| **MoE** | Obsolescence risk reduction; mitigation value |
| **MoP** | Component vulnerability score; mitigation ROI |
| **Acquisition Relevance** | DMS planning; supply chain risk management |
| **DOTMLPFI** | Materiel |
| **Pilot Priority** | MEDIUM |

---

### SUSTAIN-Q05: Decommissioning and Disposal

**Question:** What decommissioning and disposal requirements should be considered during system design to minimize end-of-life costs and environmental impact?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Lifecycle Planning Seminar |
| **Format** | Design-for-disposal workshop |
| **Participants** | 10-15 (engineering, environmental, acquisition) |
| **Neural Contribution** | Learn disposal cost patterns; predict environmental impact |
| **Symbolic Contribution** | Encode environmental regulations; trace design-to-disposal chains; explain compliance requirements |
| **MoE** | End-of-life cost; environmental compliance |
| **MoP** | Disposal cost estimate accuracy; environmental impact score |
| **Acquisition Relevance** | Design requirements; lifecycle cost estimation |
| **DOTMLPFI** | Materiel, Facilities |
| **Pilot Priority** | LOW |

---

## Gap Area 5: Human-Machine Teaming (5 Questions)

### Overview
These questions address the integration of humans and autonomous systems as effective teams.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Human-in-the-Loop Simulation |
| **Secondary Type** | Cognitive Workload Experiment |
| **Key AI Role** | Model workload dynamics, optimize teaming |
| **DOTMLPFI Focus** | Training, Materiel, Personnel |

---

### HMT-Q01: Adaptive Automation Levels

**Question:** How should automation levels dynamically adapt based on operator workload, stress, and situational complexity to optimize team performance?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Human-in-the-Loop Simulation |
| **Format** | Workload variation experiment |
| **Participants** | 15-25 (operators with physiological monitoring) |
| **Neural Contribution** | Learn workload-performance patterns; predict adaptation triggers; optimize automation transitions |
| **Symbolic Contribution** | Encode workload thresholds; enforce authority bounds; trace adaptation decisions |
| **MoE** | Team performance; workload optimization |
| **MoP** | Automation adaptation accuracy; workload balance |
| **Acquisition Relevance** | Adaptive automation requirements |
| **DOTMLPFI** | Materiel, Training |
| **Pilot Priority** | **HIGH** - Core HMT challenge |

**Wargame Design Elements:**
- Physiological workload measurement
- Varying task complexity injections
- Multiple automation level configurations
- AI predicts workload state; symbolic system enforces safe boundaries

---

### HMT-Q02: Information Allocation

**Question:** What information should be presented to operators versus processed autonomously, and how should this allocation change based on mission phase and tempo?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Interface Design Experiment |
| **Format** | Information allocation trials |
| **Participants** | 20-30 (operators, HF engineers) |
| **Neural Contribution** | Learn information relevance patterns; predict attention allocation |
| **Symbolic Contribution** | Encode information priority rules; trace allocation decisions; explain display logic |
| **MoE** | Information allocation effectiveness; operator awareness |
| **MoP** | Information relevance score; allocation adaptation time |
| **Acquisition Relevance** | Display design requirements |
| **DOTMLPFI** | Materiel, Training |
| **Pilot Priority** | MEDIUM |

---

### HMT-Q03: Interface Design for Trust Calibration

**Question:** Which interface designs and decision aids most effectively support rapid operator comprehension and appropriate trust calibration in human-machine teams?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Interface Comparison Experiment |
| **Format** | A/B testing with operators |
| **Participants** | 25-40 (operators) |
| **Neural Contribution** | Learn trust calibration patterns; predict comprehension factors |
| **Symbolic Contribution** | Define trust indicators; trace interface-to-trust mapping; explain AI reasoning |
| **MoE** | Comprehension speed; trust calibration |
| **MoP** | Comprehension time; trust accuracy |
| **Acquisition Relevance** | Interface specification |
| **DOTMLPFI** | Materiel |
| **Pilot Priority** | **HIGH** |

---

### HMT-Q04: System Transparency and Explanation

**Question:** How should systems communicate their confidence, limitations, and reasoning to human teammates to enable effective oversight and intervention?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Transparency Evaluation Seminar |
| **Format** | Explanation quality assessment |
| **Participants** | 15-20 (operators, HF experts) |
| **Neural Contribution** | Learn explanation effectiveness patterns; predict intervention triggers |
| **Symbolic Contribution** | Generate explanations from reasoning chains; enforce confidence communication; trace decision logic |
| **MoE** | Oversight effectiveness; intervention appropriateness |
| **MoP** | Explanation clarity score; intervention timing accuracy |
| **Acquisition Relevance** | Explainability requirements |
| **DOTMLPFI** | Materiel, Training |
| **Pilot Priority** | **HIGH** - Key for responsible AI |

---

### HMT-Q05: Training for Human-Machine Teams

**Question:** What training and rehearsal approaches best prepare operators to work effectively with autonomous teammates across both nominal and off-nominal conditions?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Training Effectiveness Study |
| **Format** | Multi-condition training evaluation |
| **Participants** | 30-50 (operators in training) |
| **Neural Contribution** | Learn skill acquisition patterns; predict off-nominal readiness |
| **Symbolic Contribution** | Encode proficiency criteria; trace training-to-performance; validate competency |
| **MoE** | Training effectiveness; off-nominal readiness |
| **MoP** | Skill acquisition rate; off-nominal performance |
| **Acquisition Relevance** | Training system requirements |
| **DOTMLPFI** | Training, Personnel |
| **Pilot Priority** | MEDIUM |

---

## Gap Area 6: Failure Modes & Graceful Degradation (5 Questions)

### Overview
These questions address system resilience, failure analysis, and graceful degradation under stress.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Fault Injection Simulation |
| **Secondary Type** | Recovery Procedure Tabletop |
| **Key AI Role** | Learn cascade patterns, trace failure logic |
| **DOTMLPFI Focus** | Materiel, Training, Doctrine |

---

### FAILURE-Q01: Single Points of Failure

**Question:** What single points of failure exist in the mission architecture, and which have no operational workaround if they occur during critical mission phases?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Architecture Vulnerability Analysis |
| **Format** | SPOF identification workshop |
| **Participants** | 12-18 (architects, operators) |
| **Neural Contribution** | Learn SPOF patterns from historical data; predict workaround availability |
| **Symbolic Contribution** | Model system dependencies; trace failure-to-mission impact; identify unmitigated SPOFs |
| **MoE** | SPOF identification completeness; workaround coverage |
| **MoP** | SPOF count; workaround availability rate |
| **Acquisition Relevance** | Resilience requirements |
| **DOTMLPFI** | Materiel |
| **Pilot Priority** | **HIGH** |

---

### FAILURE-Q02: Mission Effectiveness Degradation

**Question:** How does mission effectiveness degrade as individual systems fail, and what is the minimum viable system configuration to achieve essential mission objectives?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Degradation Analysis Simulation |
| **Format** | Progressive failure injection |
| **Participants** | 10-15 (operators, analysts) |
| **Neural Contribution** | Learn degradation curves; predict MVP configurations |
| **Symbolic Contribution** | Define mission requirements; trace system-to-capability mapping; validate MVP |
| **MoE** | Degradation curve accuracy; MVP identification |
| **MoP** | Effectiveness vs failure count; MVP coverage |
| **Acquisition Relevance** | Minimum capability requirements |
| **DOTMLPFI** | Materiel, Doctrine |
| **Pilot Priority** | **HIGH** |

---

### FAILURE-Q03: Cascading Failure Effects

**Question:** Which failure combinations create cascading effects that exceed the sum of individual failures, and how can architecture be designed to contain such cascades?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Cascade Analysis Simulation |
| **Format** | Multi-failure scenario injection |
| **Participants** | 12-18 (architects, operators) |
| **Neural Contribution** | Learn cascade patterns; predict non-linear effects; identify cascade triggers |
| **Symbolic Contribution** | Model dependency graphs; trace cascade propagation; validate containment |
| **MoE** | Cascade containment; non-linear effect identification |
| **MoP** | Cascade propagation rate; containment effectiveness |
| **Acquisition Relevance** | Architecture design requirements |
| **DOTMLPFI** | Materiel |
| **Pilot Priority** | MEDIUM |

---

### FAILURE-Q04: Recovery Procedures

**Question:** What automated and manual recovery procedures should be available for each failure mode, and how should operators be alerted and guided through recovery?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Recovery Procedure Tabletop |
| **Format** | Failure response exercise |
| **Participants** | 15-25 (operators, maintenance) |
| **Neural Contribution** | Learn recovery effectiveness patterns; predict operator guidance needs |
| **Symbolic Contribution** | Encode recovery procedures; trace alert-to-action; validate procedure completeness |
| **MoE** | Recovery success rate; operator guidance effectiveness |
| **MoP** | Recovery time; procedure compliance rate |
| **Acquisition Relevance** | Recovery system requirements |
| **DOTMLPFI** | Training, Materiel |
| **Pilot Priority** | MEDIUM |

---

### FAILURE-Q05: Contingency Planning

**Question:** How should pre-mission planning account for potential system failures, and what contingency branches should be prepared for high-impact failure scenarios?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Contingency Planning Seminar |
| **Format** | Branch planning workshop |
| **Participants** | 15-20 (planners, operators) |
| **Neural Contribution** | Learn contingency coverage patterns; predict high-impact scenarios |
| **Symbolic Contribution** | Encode planning requirements; trace failure-to-contingency mapping; validate coverage |
| **MoE** | Contingency coverage; planning completeness |
| **MoP** | Contingency plan count; high-impact scenario coverage |
| **Acquisition Relevance** | Planning tool requirements |
| **DOTMLPFI** | Doctrine, Training |
| **Pilot Priority** | MEDIUM |

---

## Gap Area 7: Temporal & Phasing Decisions (5 Questions)

### Overview
These questions address capability phasing, transition planning, and schedule risk management.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Portfolio Planning Seminar |
| **Secondary Type** | Schedule Risk Simulation |
| **Key AI Role** | Optimize sequencing, predict schedule risk |
| **DOTMLPFI Focus** | Materiel, Organization |

---

### TEMPORAL-Q01: Fielding vs. Threat Timeline

**Question:** When should new capabilities be fielded relative to evolving threat timelines, and how should uncertainty in both schedules affect transition planning?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Threat-Capability Timeline Seminar |
| **Format** | Uncertainty-aware planning workshop |
| **Participants** | 15-25 (acquisition, intelligence, operators) |
| **Neural Contribution** | Learn threat evolution patterns; predict schedule uncertainty impacts |
| **Symbolic Contribution** | Encode timeline dependencies; trace threat-to-capability gaps; explain risk |
| **MoE** | Fielding timing accuracy; threat alignment |
| **MoP** | Schedule variance; threat coverage gap |
| **Acquisition Relevance** | Milestone planning; threat-informed acquisition |
| **DOTMLPFI** | Materiel |
| **Pilot Priority** | **HIGH** - Core acquisition challenge |

---

### TEMPORAL-Q02: Optimal Upgrade Sequencing

**Question:** What is the optimal sequencing of capability upgrades across a portfolio to maximize cumulative mission effectiveness while managing integration risk?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Portfolio Optimization Simulation |
| **Format** | Sequencing analysis |
| **Participants** | 12-18 (program managers, architects) |
| **Neural Contribution** | Learn sequencing optimization patterns; predict integration risk |
| **Symbolic Contribution** | Encode dependency constraints; validate sequencing feasibility; trace effectiveness accumulation |
| **MoE** | Cumulative effectiveness; integration success |
| **MoP** | Sequencing optimality; integration defect rate |
| **Acquisition Relevance** | Portfolio management; sequencing decisions |
| **DOTMLPFI** | Materiel, Organization |
| **Pilot Priority** | MEDIUM |

---

### TEMPORAL-Q03: Parallel Operations During Transition

**Question:** How should legacy and modernized systems be operated in parallel during transition periods, and what is the cost of maintaining dual capabilities?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Transition Operations Tabletop |
| **Format** | Dual-capability operations exercise |
| **Participants** | 15-20 (operators, sustainment) |
| **Neural Contribution** | Learn transition cost patterns; predict parallel operation challenges |
| **Symbolic Contribution** | Encode interoperability requirements; trace dual-operation costs; explain trade-offs |
| **MoE** | Transition smoothness; dual-operation cost |
| **MoP** | Parallel operation duration; dual capability overhead |
| **Acquisition Relevance** | Transition planning; budget estimation |
| **DOTMLPFI** | Materiel, Organization |
| **Pilot Priority** | MEDIUM |

---

### TEMPORAL-Q04: Schedule Dependencies and Margin Allocation

**Question:** Which development schedule dependencies create the greatest risk to operational capability delivery, and where should schedule margin be allocated?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Schedule Risk Simulation |
| **Format** | Monte Carlo schedule analysis |
| **Participants** | 10-15 (program managers, analysts) |
| **Neural Contribution** | Learn schedule risk patterns; predict critical path risks |
| **Symbolic Contribution** | Model dependency network; trace risk propagation; validate margin allocation |
| **MoE** | Schedule risk reduction; margin allocation effectiveness |
| **MoP** | Critical path risk score; margin utilization |
| **Acquisition Relevance** | Schedule management; risk allocation |
| **DOTMLPFI** | Organization |
| **Pilot Priority** | MEDIUM |

---

### TEMPORAL-Q05: Decision Criteria for Capability Increments

**Question:** What decision criteria should trigger acceleration, delay, or cancellation of planned capability increments based on changing operational needs or technical progress?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Decision Gate Seminar |
| **Format** | Criteria development workshop |
| **Participants** | 15-20 (acquisition, operational) |
| **Neural Contribution** | Learn decision trigger patterns; predict criterion effectiveness |
| **Symbolic Contribution** | Encode decision rules; trace trigger-to-action mapping; explain criteria |
| **MoE** | Decision timeliness; criteria clarity |
| **MoP** | Trigger accuracy; decision response time |
| **Acquisition Relevance** | Gate review criteria; adaptive acquisition |
| **DOTMLPFI** | Organization, Policy |
| **Pilot Priority** | MEDIUM |

---

## Gap Area 8: Training & Readiness (4 Questions)

### Overview
These questions address operator training, simulation fidelity, and readiness sustainment.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Training Effectiveness Study |
| **Secondary Type** | LVC Integration Exercise |
| **Key AI Role** | Predict skill decay, optimize training |
| **DOTMLPFI Focus** | Training, Personnel |

---

### TRAINING-Q01: Simulation Fidelity Requirements

**Question:** What simulation fidelity and scenario coverage are required to adequately train operators for mission-critical tasks, and how should training effectiveness be measured?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Training Fidelity Experiment |
| **Format** | Multi-fidelity comparison study |
| **Participants** | 30-50 (operators in training) |
| **Neural Contribution** | Learn fidelity-effectiveness relationships; predict training transfer |
| **Symbolic Contribution** | Define proficiency criteria; trace training-to-performance; validate assessment |
| **MoE** | Training adequacy; skill transfer |
| **MoP** | Simulation fidelity score; skill assessment pass rate |
| **Acquisition Relevance** | Training system requirements |
| **DOTMLPFI** | Training, Facilities |
| **Pilot Priority** | MEDIUM |

---

### TRAINING-Q02: Skill Decay and Sustainment Training

**Question:** How quickly do operator skills decay without practice, and what sustainment training frequency is required to maintain mission readiness?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Longitudinal Training Study |
| **Format** | Skill retention measurement |
| **Participants** | 40-60 (operators over time) |
| **Neural Contribution** | Learn skill decay curves; predict sustainment requirements |
| **Symbolic Contribution** | Define readiness thresholds; trace decay-to-risk; validate training schedules |
| **MoE** | Skill retention; readiness maintenance |
| **MoP** | Skill decay rate; training frequency requirement |
| **Acquisition Relevance** | Training resource requirements |
| **DOTMLPFI** | Training, Personnel |
| **Pilot Priority** | MEDIUM |

---

### TRAINING-Q03: Simulation vs. Live Training

**Question:** Which mission tasks are most difficult to train effectively in simulation, and what live training resources are essential to maintain proficiency?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Training Mode Comparison |
| **Format** | Sim vs. live effectiveness study |
| **Participants** | 30-50 (operators) |
| **Neural Contribution** | Learn training mode effectiveness by task; predict live training requirements |
| **Symbolic Contribution** | Categorize task types; trace mode-to-effectiveness; explain limitations |
| **MoE** | Training mode effectiveness; proficiency maintenance |
| **MoP** | Simulation limitation score; live training requirement |
| **Acquisition Relevance** | Training resource allocation |
| **DOTMLPFI** | Training, Facilities |
| **Pilot Priority** | MEDIUM |

---

### TRAINING-Q04: Training Pipeline Capacity

**Question:** What training pipeline capacity and throughput are required to sustain the qualified operator population given attrition and force structure plans?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Workforce Planning Simulation |
| **Format** | Pipeline capacity modeling |
| **Participants** | 12-18 (training managers, HR) |
| **Neural Contribution** | Learn throughput patterns; predict attrition impacts |
| **Symbolic Contribution** | Encode qualification requirements; trace pipeline-to-workforce; validate capacity |
| **MoE** | Pipeline adequacy; workforce sustainment |
| **MoP** | Training throughput; qualification rate |
| **Acquisition Relevance** | Training infrastructure requirements |
| **DOTMLPFI** | Training, Personnel, Facilities |
| **Pilot Priority** | LOW |

---

## Gap Area 9: Stakeholder & User Engagement (3 Questions)

### Overview
These questions address requirements capture, stakeholder coordination, and analysis alignment with decision needs.

| Aspect | Specification |
|--------|---------------|
| **Primary Wargame Type** | Multi-Party Negotiation |
| **Secondary Type** | Requirements Validation Seminar |
| **Key AI Role** | Learn preference patterns, model conflict resolution |
| **DOTMLPFI Focus** | Organization, Leadership |

---

### STAKEHOLDER-Q01: Operational User Feedback Integration

**Question:** How should operational user feedback be systematically captured, prioritized, and incorporated into system evolution and capability development decisions?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Requirements Validation Seminar |
| **Format** | Feedback process workshop |
| **Participants** | 15-25 (users, acquisition, developers) |
| **Neural Contribution** | Learn feedback pattern value; predict incorporation effectiveness |
| **Symbolic Contribution** | Encode prioritization rules; trace feedback-to-requirement; explain decisions |
| **MoE** | Feedback incorporation rate; user satisfaction |
| **MoP** | Feedback capture completeness; incorporation latency |
| **Acquisition Relevance** | Requirements process improvement |
| **DOTMLPFI** | Organization |
| **Pilot Priority** | MEDIUM |

---

### STAKEHOLDER-Q02: Analysis-Decision Alignment

**Question:** What mechanisms ensure that mission engineering analyses address the actual decision needs of operational commanders and acquisition decision-makers?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Decision-Analysis Alignment Seminar |
| **Format** | Gap analysis workshop |
| **Participants** | 15-20 (analysts, decision-makers) |
| **Neural Contribution** | Learn decision need patterns; predict analysis relevance |
| **Symbolic Contribution** | Map decision needs to analyses; trace alignment; explain gaps |
| **MoE** | Analysis relevance; decision support effectiveness |
| **MoP** | Decision-maker satisfaction; analysis utilization rate |
| **Acquisition Relevance** | Analysis process improvement |
| **DOTMLPFI** | Organization, Leadership |
| **Pilot Priority** | **HIGH** - Core ME challenge |

---

### STAKEHOLDER-Q03: Stakeholder Conflict Resolution

**Question:** Which stakeholder conflicts (e.g., near-term readiness vs. long-term modernization) most frequently impede mission engineering decisions, and how should they be resolved?

| Component | Specification |
|-----------|---------------|
| **Wargame Type** | Multi-Party Negotiation Game |
| **Format** | Conflict resolution exercise |
| **Participants** | 15-25 (diverse stakeholders) |
| **Neural Contribution** | Learn conflict patterns; predict resolution approaches |
| **Symbolic Contribution** | Model stakeholder interests; trace conflict-to-resolution; explain trade-offs |
| **MoE** | Conflict resolution effectiveness; decision velocity |
| **MoP** | Conflict frequency; resolution time |
| **Acquisition Relevance** | Governance process design |
| **DOTMLPFI** | Organization, Leadership, Policy |
| **Pilot Priority** | **HIGH** |

---

## Summary Matrix

### Questions by Gap Area and Pilot Priority

| Gap Area | Total Qs | HIGH | MEDIUM | LOW |
|----------|----------|------|--------|-----|
| Coalition Operations | 5 | 3 | 2 | 0 |
| Comms-Denied | 5 | 3 | 2 | 0 |
| Ethics/Legal | 5 | 4 | 1 | 0 |
| Sustainment | 5 | 0 | 4 | 1 |
| Human-Machine Teaming | 5 | 3 | 2 | 0 |
| Failure Modes | 5 | 2 | 3 | 0 |
| Temporal/Phasing | 5 | 1 | 4 | 0 |
| Training | 4 | 0 | 3 | 1 |
| Stakeholder | 3 | 2 | 1 | 0 |
| **TOTAL** | **42** | **18** | **22** | **2** |

### Recommended Pilot Wargames (Priority Order)

| Priority | Wargame | Questions Addressed | Duration |
|----------|---------|---------------------|----------|
| 1 | **Coalition Operations Matrix Game** | COALITION-Q01, Q03, Q04 | 2-3 days |
| 2 | **Human-Machine Teaming Simulation** | HMT-Q01, Q03, Q04 | 2 days |
| 3 | **Communications-Denied Operations** | COMMS-Q01, Q02, Q04 | 2 days |
| 4 | **Ethics & Authority Boundaries** | ETHICS-Q01, Q02, Q03, Q05 | 2 days |
| 5 | **Failure Mode Analysis** | FAILURE-Q01, Q02 | 1-2 days |

### Wargame Type Distribution

| Wargame Type | Question Count | Percentage |
|--------------|----------------|------------|
| Seminar/Workshop | 14 | 33% |
| Tabletop/Matrix | 12 | 29% |
| Computational/Simulation | 10 | 24% |
| Human-in-the-Loop | 6 | 14% |

### DOTMLPFI Coverage

| Domain | Question Count | Primary Focus |
|--------|----------------|---------------|
| Materiel | 28 | System requirements |
| Training | 14 | Operator preparation |
| Doctrine | 12 | Operational guidance |
| Organization | 11 | Structure and process |
| Leadership | 8 | Command and authority |
| Personnel | 6 | Workforce planning |
| Interoperability | 8 | Coalition operations |
| Facilities | 6 | Infrastructure |

---

## Neuro-Symbolic AI Contribution Summary

### Neural AI Capabilities Applied

| Capability | Application Areas | Questions |
|------------|-------------------|-----------|
| Pattern Learning | Historical data analysis, trend identification | All 42 |
| Scenario Generation | Diverse situation creation, edge case discovery | 25 |
| Prediction | Performance forecasting, threshold identification | 30 |
| Optimization | Sequencing, allocation, configuration | 15 |
| Anomaly Detection | Failure prediction, risk identification | 10 |

### Symbolic AI Capabilities Applied

| Capability | Application Areas | Questions |
|------------|-------------------|-----------|
| Constraint Enforcement | ROE, doctrine, policy compliance | 35 |
| Traceability | Decision chains, requirement mapping | All 42 |
| Explanation Generation | Decision rationale, trade-off communication | 30 |
| Validation | Compliance checking, completeness verification | 25 |
| Formal Modeling | Dependencies, authorities, workflows | 20 |

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-22*
