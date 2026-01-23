# Pilot Wargame Designs for Neuro-Symbolic AI Validation

**Document Version:** 1.0
**Date:** 2026-01-22
**Author:** University of Arizona PostDoc Research
**Status:** TAP-Ready Draft
**Purpose:** Detailed designs for 5 pilot wargames to validate neuro-symbolic AI integration

---

## Executive Summary

This document provides detailed designs for **five pilot wargames** that will validate the neuro-symbolic AI architecture for mission engineering and acquisition decision support. Each pilot targets specific ME gap questions and demonstrates different AI capabilities.

### Pilot Portfolio Overview

| Priority | Pilot Wargame | Gap Questions | Duration | AI Focus | TRL Target |
|----------|---------------|---------------|----------|----------|------------|
| 1 | Coalition Operations Matrix Game | COALITION-Q01, Q03, Q04 | 2.5 days | Constraint reasoning, scenario generation | TRL 4 |
| 2 | Human-Machine Teaming Simulation | HMT-Q01, Q03, Q04 | 2 days | Workload prediction, trust calibration | TRL 4 |
| 3 | Communications-Denied Operations | COMMS-Q01, Q02, Q04 | 2 days | Degradation modeling, threshold detection | TRL 4 |
| 4 | Ethics & Authority Boundaries | ETHICS-Q01, Q02, Q03, Q05 | 2 days | ROE encoding, explanation generation | TRL 4 |
| 5 | Failure Mode Analysis | FAILURE-Q01, Q02 | 1.5 days | Cascade prediction, dependency tracing | TRL 4 |

---

# Pilot 1: Coalition Operations Matrix Game

## 1.1 Overview

| Attribute | Specification |
|-----------|---------------|
| **Wargame Type** | Matrix Game with Classification Layers |
| **Duration** | 2.5 days (20 hours of play) |
| **Participants** | 20-25 |
| **Primary Gap Area** | Coalition & Allied Operations |
| **AI Demonstration** | Symbolic constraint reasoning + Neural scenario generation |

### ME Gap Questions Addressed

| ID | Question | Priority |
|----|----------|----------|
| COALITION-Q01 | Data classification constraints affecting coalition information sharing | HIGH |
| COALITION-Q03 | Planning cycle synchronization across coalition partners | HIGH |
| COALITION-Q04 | Capability and doctrine differences affecting force employment | HIGH |

---

## 1.2 Objectives

### Wargame Objectives
1. Identify critical information sharing friction points in coalition operations
2. Test coordination mechanisms for asynchronous planning cycles
3. Explore force employment options under varying national constraints
4. Generate insights for C4ISR system requirements

### AI Validation Objectives
1. Demonstrate symbolic constraint enforcement for classification rules
2. Validate neural scenario generation with doctrinal grounding
3. Test explanation generation for policy-constrained decisions
4. Assess cross-game pattern learning from coalition scenarios

---

## 1.3 Scenario: OPERATION NORTHERN SHIELD

### Strategic Context

```
CLASSIFICATION: NATO UNCLASSIFIED // FOR EXERCISE PURPOSES ONLY

SITUATION: A near-peer adversary has initiated hybrid operations against
a NATO member state, combining cyber attacks, disinformation, and
conventional force posturing. NATO has invoked Article 5 and is
assembling a multinational response force.

COALITION COMPOSITION:
- Framework Nation: United States
- Major Contributors: United Kingdom, France, Germany
- Regional Contributors: Poland, Norway, Baltic States
- Specialized Contributors: Netherlands (cyber), Canada (SOF)

OPERATIONAL CHALLENGE: The coalition must plan and execute a deterrence
operation while managing:
- Varying national classification systems and release authorities
- Asynchronous planning cycles (US 72-hour vs. German 96-hour)
- Different ROE interpretations and national caveats
- Capability gaps requiring multinational task organization
```

### Scenario Phases

| Phase | Duration | Focus | Key Decisions |
|-------|----------|-------|---------------|
| **Phase 1: Assembly** | 4 hours | Force generation, C2 establishment | National contribution levels, C2 architecture |
| **Phase 2: Planning** | 6 hours | Operational planning, targeting | Information sharing, synchronization |
| **Phase 3: Deployment** | 4 hours | Movement, positioning | Capability integration, logistics |
| **Phase 4: Execution** | 4 hours | Deterrence operations | ROE application, escalation management |
| **Phase 5: Transition** | 2 hours | Handover, lessons learned | Sustainment, future posture |

---

## 1.4 Participant Structure

### Cell Organization

```
┌─────────────────────────────────────────────────────────────────┐
│                        WHITE CELL                                │
│  (Control, Adjudication, AI Operations)                         │
│  - Lead Facilitator (1)                                         │
│  - Assistant Facilitators (2)                                   │
│  - AI Operator (1)                                              │
│  - Data Capture (2)                                             │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   BLUE CELL   │    │   GREEN CELL  │    │   RED CELL    │
│   (Coalition) │    │  (Neutrals)   │    │  (Adversary)  │
│               │    │               │    │               │
│ - US Team (3) │    │ - Host Nation │    │ - Red Team    │
│ - UK Team (2) │    │   (2)         │    │   Lead (1)    │
│ - FR Team (2) │    │ - Media (1)   │    │ - Operators   │
│ - DE Team (2) │    │ - NGOs (1)    │    │   (2)         │
│ - PL Team (1) │    │               │    │               │
│ - NO Team (1) │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
```

### Participant Requirements

| Role | Count | Background Required |
|------|-------|---------------------|
| Coalition Nation Leads | 6 | Military planning experience, NATO familiarity |
| Coalition Staff | 6 | C2/Intel/Ops experience |
| Red Team | 3 | Adversary doctrine knowledge |
| Green Cell | 4 | Political-military experience |
| White Cell | 6 | Facilitation, AI operation |
| **Total** | **25** | |

---

## 1.5 AI Integration

### Neural Components Active

| Component | Application | Configuration |
|-----------|-------------|---------------|
| **Scenario Generator** | Generate information sharing scenarios, inject events | Constrained by STANAG 4774 classification rules |
| **Pattern Learner** | Identify recurring coordination friction patterns | Trained on NATO exercise AARs |
| **Prediction Engine** | Forecast planning cycle conflicts | Configured for 6-nation planning models |

### Symbolic Components Active

| Component | Application | Configuration |
|-----------|-------------|---------------|
| **Knowledge Graph** | Store classification rules, national caveats, doctrine | Populated with STANAG 4774, national policies |
| **Reasoning Engine** | Enforce classification constraints, validate decisions | ROE rules, release authority chains |
| **Constraint Manager** | Check information release validity | Real-time constraint checking |
| **Explanation Engine** | Explain why information cannot be shared | Policy-based explanation templates |

### AI Touchpoints by Phase

| Phase | AI Support | Human Decision |
|-------|------------|----------------|
| **Assembly** | Generate national contribution scenarios | Select contribution levels |
| **Planning** | Flag classification conflicts, predict sync issues | Resolve information sharing |
| **Deployment** | Identify capability integration gaps | Approve task organization |
| **Execution** | Explain ROE constraint violations | Make tactical decisions |
| **Transition** | Synthesize cross-phase patterns | Validate insights |

---

## 1.6 Game Mechanics

### Matrix Game Argument Structure

Each turn, players propose actions using the matrix game format:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MATRIX GAME ARGUMENT                          │
├─────────────────────────────────────────────────────────────────┤
│ ACTOR: [Nation/Cell]                                            │
│ ACTION: [Proposed action]                                       │
│ RESULT IF SUCCESSFUL: [Intended outcome]                        │
│                                                                  │
│ ARGUMENTS FOR (Player provides):                                │
│   1. [Reason this should succeed]                               │
│   2. [Supporting factor]                                        │
│   3. [Historical precedent or doctrinal basis]                  │
│                                                                  │
│ ARGUMENTS AGAINST (Other players/AI provide):                   │
│   1. [Counter-argument]                                         │
│   2. [Complicating factor]                                      │
│                                                                  │
│ AI CONSTRAINT CHECK:                                            │
│   [ ] Classification: [PASS/FAIL with explanation]              │
│   [ ] ROE: [PASS/FAIL with explanation]                         │
│   [ ] Doctrine: [PASS/FAIL with explanation]                    │
│                                                                  │
│ BASE PROBABILITY: [Calculated from arguments]                   │
│ ADJUSTED PROBABILITY: [After constraint modifiers]              │
│ DIE ROLL REQUIRED: [Target number]                              │
└─────────────────────────────────────────────────────────────────┘
```

### Adjudication Rules

1. **Argument Strength**: Each valid argument adds +1 to success probability (max +3)
2. **Counter-Arguments**: Each valid counter subtracts -1 (max -3)
3. **Constraint Violations**: Automatic failure if AI flags critical violation
4. **Base Probability**: 50% + arguments - counters - constraint penalties
5. **Resolution**: Roll d10; success if roll ≤ probability × 10

### Classification Mechanics

| Classification Level | Sharing Restriction | AI Check |
|---------------------|---------------------|----------|
| NATO UNCLASSIFIED | Open sharing | None |
| NATO RESTRICTED | Coalition members only | Verify membership |
| NATO CONFIDENTIAL | Need-to-know validation | Check authorization |
| NATO SECRET | Formal release required | Full release chain |
| COSMIC TOP SECRET | Special handling | Multi-level approval |

---

## 1.7 Inject Schedule

### Pre-Planned Injects

| ID | Phase | Inject | AI Role | Target Question |
|----|-------|--------|---------|-----------------|
| INJ-01 | 1 | Intelligence report requires cross-classification sharing | Constraint check | Q01 |
| INJ-02 | 2 | German planning cycle delays US timeline | Sync prediction | Q03 |
| INJ-03 | 2 | French national caveat prevents targeting option | ROE reasoning | Q04 |
| INJ-04 | 3 | Cyber attack compromises SECRET network | Scenario generation | Q01 |
| INJ-05 | 3 | Polish capability gap requires UK substitution | Capability matching | Q04 |
| INJ-06 | 4 | Time-sensitive target requires rapid coalition approval | Prediction | Q03 |
| INJ-07 | 4 | Collateral damage estimate conflicts with German ROE | Constraint explanation | Q04 |
| INJ-08 | 5 | After-action intelligence reveals classification friction cost | Pattern synthesis | Q01 |

### AI-Generated Dynamic Injects

The Scenario Generator will create additional injects based on gameplay:

- **Trigger Conditions**: Player actions that create new information sharing requirements
- **Generation Parameters**: Constrained by scenario bounds, classification rules
- **Human Approval**: All AI-generated injects reviewed by White Cell before delivery

---

## 1.8 Data Collection Plan

### Automated Capture

| Data Type | Capture Method | Storage |
|-----------|----------------|---------|
| Arguments submitted | Digital argument forms | Knowledge Graph |
| AI constraint checks | Automatic logging | Provenance records |
| Die roll results | Adjudication system | Outcome database |
| Turn timestamps | System clock | Timeline database |

### Manual Capture

| Data Type | Capture Method | Responsibility |
|-----------|----------------|----------------|
| Discussion themes | Observer notes | Data Capture team |
| Participant reasoning | Post-turn debrief | Facilitators |
| Non-verbal dynamics | Observation log | Observers |
| Hot wash insights | Structured capture | Lead Facilitator |

### Traceability Requirements

Every insight must trace to:
```
Gap Question → Scenario Phase → Specific Inject → Player Action →
Outcome → Discussion → Insight → Validation
```

---

## 1.9 Measures of Effectiveness and Performance

### MoEs (Mission-Level)

| MoE | Definition | Target |
|-----|------------|--------|
| Joint Mission Effectiveness | % of coalition objectives achieved | ≥70% |
| Information Availability | % of required information successfully shared | ≥60% |
| Planning Synchronization | % of planning milestones met on time | ≥75% |

### MoPs (Process-Level)

| MoP | Definition | Measurement |
|-----|------------|-------------|
| Data Release Latency | Time from request to release | Hours |
| Classification Overhead | % of time spent on classification issues | % of phase time |
| Constraint Violations | Number of AI-flagged violations | Count per phase |
| Sync Conflicts | Number of planning cycle conflicts | Count per phase |

### AI Validation Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Constraint Accuracy | % of AI constraints validated by SMEs | ≥90% |
| Explanation Clarity | SME rating of AI explanations (1-5) | ≥4.0 |
| Scenario Plausibility | SME rating of AI scenarios (1-5) | ≥4.0 |
| Pattern Relevance | % of AI patterns rated useful | ≥70% |

---

## 1.10 Resource Requirements

### Personnel

| Role | Days | Total Person-Days |
|------|------|-------------------|
| Lead Facilitator | 3.5 | 3.5 |
| Assistant Facilitators | 3.5 | 7 |
| AI Operator | 3.5 | 3.5 |
| Data Capture | 3.5 | 7 |
| Participants | 2.5 | 62.5 |
| **Total** | | **83.5** |

### Technology

| System | Requirement |
|--------|-------------|
| AI Platform | Neuro-symbolic system with coalition scenario config |
| Network | Isolated network for classification exercise |
| Displays | Main display + cell displays (4) |
| Recording | Audio/video capture for all cells |
| Digital Tools | Matrix game argument system, die roller |

### Facilities

| Space | Requirement |
|-------|-------------|
| Main Room | Plenary space for 30 |
| Blue Cell | Breakout for 12 |
| Red Cell | Breakout for 3 |
| Green Cell | Breakout for 4 |
| White Cell | Control room for 6 |

### Budget Estimate

| Category | Estimate |
|----------|----------|
| Participant travel/lodging | $40,000 |
| Facility rental | $5,000 |
| Technology/equipment | $10,000 |
| Materials/supplies | $2,000 |
| Contingency (15%) | $8,550 |
| **Total** | **$65,550** |

---

## 1.11 Schedule

### Day 0: Setup (Evening)

| Time | Activity |
|------|----------|
| 1400-1700 | Facility setup, technology check |
| 1700-1900 | AI system configuration and testing |
| 1900-2000 | White Cell rehearsal |

### Day 1: Opening and Phases 1-2

| Time | Activity |
|------|----------|
| 0800-0900 | Registration, welcome |
| 0900-1000 | Scenario brief, AI capability demo |
| 1000-1030 | Rules and mechanics brief |
| 1030-1045 | Break |
| 1045-1245 | Phase 1: Assembly (4 turns) |
| 1245-1345 | Lunch |
| 1345-1645 | Phase 2: Planning (6 turns) |
| 1645-1730 | Day 1 hot wash |
| 1800 | Social event (optional) |

### Day 2: Phases 3-5 and Closing

| Time | Activity |
|------|----------|
| 0800-0830 | Day 2 orientation |
| 0830-1030 | Phase 3: Deployment (4 turns) |
| 1030-1045 | Break |
| 1045-1245 | Phase 4: Execution (4 turns) |
| 1245-1345 | Lunch |
| 1345-1445 | Phase 5: Transition (2 turns) |
| 1445-1530 | AI pattern presentation |
| 1530-1545 | Break |
| 1545-1700 | Structured debrief and insight capture |
| 1700-1730 | Closing remarks, feedback collection |

### Day 3: Analysis (White Cell Only)

| Time | Activity |
|------|----------|
| 0800-1200 | Data consolidation, initial analysis |
| 1200-1300 | Lunch |
| 1300-1700 | Pattern analysis, insight validation |

---

## 1.12 Expected Outputs

### Immediate Outputs

1. **Wargame Execution Log**: Complete record of all turns, arguments, outcomes
2. **AI Constraint Log**: All constraint checks with explanations
3. **Pattern Report**: AI-identified patterns from gameplay
4. **Hot Wash Notes**: Participant insights from debrief

### Analysis Outputs (Within 2 Weeks)

1. **Draft Insights Document**: Validated insights with traceability
2. **Classification Friction Analysis**: Quantified impact of classification on effectiveness
3. **Synchronization Gap Assessment**: Planning cycle friction points
4. **Capability Integration Findings**: Multinational force employment insights

### Final Outputs (Within 4 Weeks)

1. **Pilot Wargame Report**: Complete analysis with recommendations
2. **AI Validation Assessment**: Performance of AI components
3. **Methodology Lessons Learned**: Process improvements for future pilots
4. **Requirement Implications**: Draft capability requirements supported by wargame

---

# Pilot 2: Human-Machine Teaming Simulation

## 2.1 Overview

| Attribute | Specification |
|-----------|---------------|
| **Wargame Type** | Human-in-the-Loop Simulation |
| **Duration** | 2 days (16 hours of play) |
| **Participants** | 25-30 |
| **Primary Gap Area** | Human-Machine Teaming |
| **AI Demonstration** | Workload prediction + Trust calibration + Adaptive automation |

### ME Gap Questions Addressed

| ID | Question | Priority |
|----|----------|----------|
| HMT-Q01 | Adaptive automation levels based on operator workload | HIGH |
| HMT-Q03 | Interface designs for trust calibration | HIGH |
| HMT-Q04 | System transparency and explanation for oversight | HIGH |

---

## 2.2 Objectives

### Wargame Objectives
1. Identify optimal automation level transitions based on workload
2. Test interface designs for appropriate trust calibration
3. Evaluate explanation approaches for human oversight
4. Generate insights for adaptive automation requirements

### AI Validation Objectives
1. Demonstrate neural workload prediction accuracy
2. Validate symbolic constraint enforcement for authority bounds
3. Test real-time explanation generation quality
4. Assess human-AI team performance metrics

---

## 2.3 Scenario: AUTONOMOUS CONVOY ESCORT

### Operational Context

```
CLASSIFICATION: UNCLASSIFIED // FOR EXERCISE PURPOSES ONLY

SITUATION: A logistics convoy must traverse contested territory with
mixed autonomous and manned escort vehicles. Operators must manage
multiple autonomous systems while maintaining situational awareness
and decision authority over lethal actions.

SYSTEM COMPOSITION:
- 4 Autonomous Ground Vehicles (AGVs) with sensors and weapons
- 2 Unmanned Aerial Vehicles (UAVs) for reconnaissance
- 1 Manned Command Vehicle with 3 operators
- 8 Logistics vehicles (protected)

OPERATIONAL CHALLENGE: Operators must:
- Monitor autonomous system status and recommendations
- Make engagement decisions for weapons release
- Adjust automation levels based on threat environment
- Maintain convoy progress despite disruptions
```

### Scenario Phases

| Phase | Duration | Focus | Workload Level |
|-------|----------|-------|----------------|
| **Phase 1: Route Planning** | 2 hours | Mission preparation, automation config | Low |
| **Phase 2: Movement to Contact** | 4 hours | Monitoring, minor threats | Medium |
| **Phase 3: Contested Transit** | 4 hours | Active threats, engagement decisions | High |
| **Phase 4: Casualty Response** | 3 hours | System degradation, recovery | Very High |
| **Phase 5: Extraction** | 3 hours | Mission completion, handover | Medium→Low |

---

## 2.4 Participant Structure

### Operator Positions (Rotated)

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMMAND VEHICLE CREW                          │
│                                                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ VEHICLE         │  │ SENSOR          │  │ MISSION         │ │
│  │ COMMANDER       │  │ OPERATOR        │  │ COMMANDER       │ │
│  │                 │  │                 │  │                 │ │
│  │ - AGV control   │  │ - UAV control   │  │ - Overall C2    │ │
│  │ - Engagement    │  │ - Threat detect │  │ - ROE authority │ │
│  │   authority     │  │ - Route recon   │  │ - Escalation    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Full Participant Structure

| Role | Count | Rotation |
|------|-------|----------|
| Operators (3 positions × 3 shifts) | 9 | Every 2 phases |
| Observers/Analysts | 6 | Continuous |
| White Cell/Facilitators | 5 | Continuous |
| AI Operators | 2 | Continuous |
| SME Advisors | 4 | On-call |
| Physiological Monitors | 2 | Continuous |
| **Total** | **28** | |

---

## 2.5 AI Integration

### Neural Components Active

| Component | Application | Real-Time |
|-----------|-------------|-----------|
| **Prediction Engine** | Predict operator workload state | Yes |
| **Pattern Learner** | Learn workload-performance relationships | Batch |
| **Optimization Engine** | Recommend automation level adjustments | Yes |

### Symbolic Components Active

| Component | Application | Real-Time |
|-----------|-------------|-----------|
| **Reasoning Engine** | Enforce authority boundaries | Yes |
| **Constraint Manager** | Validate automation transitions | Yes |
| **Explanation Engine** | Explain system recommendations | Yes |
| **Traceability Manager** | Log all human-AI interactions | Yes |

### Automation Levels

| Level | AI Authority | Human Role | Transition Trigger |
|-------|--------------|------------|-------------------|
| **Level 1: Manual** | Advisory only | Full control | Operator request |
| **Level 2: Assisted** | Recommendations | Approval required | Low workload |
| **Level 3: Supervised** | Execution with veto | Oversight | Medium workload |
| **Level 4: Autonomous** | Full execution (non-lethal) | Exception handling | High workload |

### AI-Recommended Transitions

The AI will recommend automation level changes based on:
- Physiological workload indicators (heart rate, eye tracking)
- Task performance metrics (response time, accuracy)
- Threat environment assessment
- Historical patterns from similar operators

**Human always retains authority to accept or override AI recommendations.**

---

## 2.6 Interface Configurations (A/B Testing)

### Interface A: Minimal Explanation

- System status display only
- Automation level indicator
- Simple recommendation ("Recommend Level 3")
- No reasoning provided

### Interface B: Full Explanation

- System status with confidence levels
- Automation recommendation with reasoning
- Workload assessment display
- "What-if" exploration capability
- Uncertainty visualization

### Interface C: Adaptive Explanation

- Explanation detail adjusts to workload
- Low workload: Full explanation available
- High workload: Critical information only
- Operator can request more detail

### Measurement

Each operator rotates through all three interfaces. Measures:
- Decision quality
- Decision speed
- Trust calibration accuracy
- Workload impact
- Preference rating

---

## 2.7 Simulation Environment

### Simulation Fidelity

| Aspect | Fidelity Level |
|--------|----------------|
| Vehicle dynamics | Medium (simplified physics) |
| Sensor representation | High (realistic detection) |
| Threat behavior | High (doctrinal adversary AI) |
| Communications | Medium (degradation effects) |
| Terrain | Medium (representative not actual) |

### Threat Injections

| Threat Type | Frequency | Decision Requirement |
|-------------|-----------|---------------------|
| Suspicious vehicle | Every 15 min | Monitor/track |
| Confirmed hostile | Every 30 min | Engagement decision |
| IED indication | Every 45 min | Route change |
| Ambush | 2-3 per scenario | Full engagement |
| System malfunction | Variable | Automation adjustment |

---

## 2.8 Physiological Measurement

### Workload Indicators

| Measure | Collection Method | Indicator |
|---------|-------------------|-----------|
| Heart Rate Variability | Chest strap | Cognitive load |
| Eye Tracking | Glasses-mounted | Attention allocation |
| Galvanic Skin Response | Wrist sensor | Stress response |
| Pupil Dilation | Eye tracker | Mental effort |

### Performance Indicators

| Measure | Collection Method | Indicator |
|---------|-------------------|-----------|
| Response Time | System logs | Workload impact |
| Decision Accuracy | SME assessment | Performance quality |
| Situation Awareness | SAGAT probes | Awareness maintenance |
| Automation Interaction | System logs | Trust behavior |

---

## 2.9 Measures of Effectiveness and Performance

### MoEs

| MoE | Definition | Target |
|-----|------------|--------|
| Team Performance | Combined human-AI mission success | ≥80% |
| Workload Optimization | Workload within optimal range | ≥70% of time |
| Trust Calibration | Trust matches AI reliability | Correlation ≥0.7 |

### MoPs

| MoP | Definition | Measurement |
|-----|------------|-------------|
| Automation Adaptation Time | Time from recommendation to transition | Seconds |
| Override Rate | % of AI recommendations overridden | % |
| Explanation Request Rate | Frequency of detail requests | Per hour |
| Intervention Accuracy | Correct human interventions | % |

### AI Validation Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Workload Prediction Accuracy | Correlation with ground truth | ≥0.8 |
| Transition Recommendation Quality | SME agreement rate | ≥75% |
| Explanation Helpfulness | Operator rating (1-5) | ≥4.0 |
| Authority Constraint Compliance | Violations prevented | 100% |

---

## 2.10 Schedule

### Day 1: Setup, Training, Phases 1-2

| Time | Activity |
|------|----------|
| 0800-0900 | Participant arrival, sensor fitting |
| 0900-1030 | System training, interface familiarization |
| 1030-1045 | Break |
| 1045-1145 | Practice scenarios (each interface) |
| 1145-1245 | Lunch |
| 1245-1445 | Phase 1: Route Planning (Interface A) |
| 1445-1500 | Break, rotation |
| 1500-1700 | Phase 2: Movement to Contact (Interface B) |
| 1700-1800 | Day 1 debrief, sensor data review |

### Day 2: Phases 3-5, Analysis

| Time | Activity |
|------|----------|
| 0800-0830 | Day 2 setup, sensor check |
| 0830-1030 | Phase 3: Contested Transit (Interface C) |
| 1030-1045 | Break, rotation |
| 1045-1245 | Phase 4: Casualty Response (Interface rotation) |
| 1245-1345 | Lunch |
| 1345-1445 | Phase 5: Extraction (Interface rotation) |
| 1445-1600 | Structured debrief, trust assessment |
| 1600-1700 | AI pattern review, insight capture |

---

## 2.11 Expected Outputs

1. **Workload-Performance Curves**: Empirical relationship by task type
2. **Trust Calibration Findings**: Interface design recommendations
3. **Automation Transition Guidelines**: Trigger conditions and thresholds
4. **Explanation Requirements**: Content and timing specifications
5. **Authority Boundary Validation**: Constraint enforcement effectiveness

---

# Pilot 3: Communications-Denied Operations

## 3.1 Overview

| Attribute | Specification |
|-----------|---------------|
| **Wargame Type** | Computational Wargame with Degradation Injection |
| **Duration** | 2 days (16 hours of play) |
| **Participants** | 15-20 |
| **Primary Gap Area** | Communications-Denied Environments |
| **AI Demonstration** | Degradation modeling + Threshold detection + Autonomous authority |

### ME Gap Questions Addressed

| ID | Question | Priority |
|----|----------|----------|
| COMMS-Q01 | Mission effectiveness degradation vs. communications constraints | HIGH |
| COMMS-Q02 | Autonomous behaviors for extended communications denial | HIGH |
| COMMS-Q04 | C2 adaptation for intermittent communications | HIGH |

---

## 3.2 Scenario: OPERATION SILENT THUNDER

### Operational Context

```
CLASSIFICATION: UNCLASSIFIED // FOR EXERCISE PURPOSES ONLY

SITUATION: A distributed maritime task force must execute a
time-sensitive strike mission in a heavily contested electromagnetic
environment. Adversary jamming progressively degrades communications.

TASK FORCE COMPOSITION:
- 1 Cruiser (Force Commander)
- 2 Destroyers
- 2 Submarines
- 4 Unmanned Surface Vessels (USVs)
- Multiple UAVs

CHALLENGE: Maintain coordinated operations as communications degrade
from full connectivity to near-complete denial.
```

### Communications Degradation Profile

| Phase | Bandwidth | Latency | Availability | Condition |
|-------|-----------|---------|--------------|-----------|
| Phase 1 | 100% | Normal | 100% | Full comms |
| Phase 2 | 50% | 2× | 90% | Contested |
| Phase 3 | 20% | 5× | 70% | Degraded |
| Phase 4 | 5% | 10× | 30% | Denied |
| Phase 5 | Variable | Variable | Variable | Recovery |

---

## 3.3 AI Integration

### Neural Components

| Component | Application |
|-----------|-------------|
| **Prediction Engine** | Model effectiveness degradation curves; predict failure thresholds |
| **Pattern Learner** | Identify effective autonomous behaviors from gameplay |
| **Optimization Engine** | Recommend pre-delegated authority configurations |

### Symbolic Components

| Component | Application |
|-----------|-------------|
| **Reasoning Engine** | Enforce pre-delegated authority bounds |
| **Constraint Manager** | Validate autonomous actions against delegated limits |
| **Traceability Manager** | Track all autonomous decisions for post-mission audit |

### Pre-Delegated Authority Framework

The wargame tests a framework of pre-delegated authorities:

| Authority Level | Commander Approval | Scope |
|-----------------|-------------------|-------|
| **Alpha** | None (standing) | Self-defense, position reporting |
| **Bravo** | Pre-mission | Engagement of designated targets |
| **Charlie** | Last contact | Expanded engagement criteria |
| **Delta** | Emergency | Mission abort/continuation decision |

---

## 3.4 Game Mechanics

### Turn Structure Under Degradation

| Comms Level | Turn Duration | Information Available | C2 Model |
|-------------|---------------|----------------------|----------|
| Full | 15 min | Complete COP | Centralized |
| Contested | 20 min | 80% COP, delayed | Distributed |
| Degraded | 30 min | 50% COP, very delayed | Mission command |
| Denied | 45 min | Local only | Autonomous |

### Autonomous Decision Points

At each phase, players must:
1. Define pre-delegated authorities for subordinate units
2. Specify autonomous behavior rules
3. Set information priority lists for limited bandwidth
4. Establish rally points and synchronization triggers

AI validates that autonomous behaviors stay within delegated bounds.

---

## 3.5 Measures

### MoEs

| MoE | Definition | Target |
|-----|------------|--------|
| Mission Success | Strike objectives achieved | ≥70% |
| Force Coordination | Units remain synchronized | ≥60% at Phase 4 |
| Authority Compliance | Autonomous actions within bounds | 100% |

### MoPs

| MoP | Definition |
|-----|------------|
| Effectiveness vs. Bandwidth | Degradation curve shape |
| Critical Threshold | Bandwidth where effectiveness drops <50% |
| Recovery Time | Time to restore coordination after comms return |

---

## 3.6 Expected Outputs

1. **Degradation Curves**: Empirical effectiveness vs. bandwidth/latency
2. **Critical Thresholds**: Identified failure points by mission type
3. **Autonomous Behavior Catalog**: Effective pre-delegated behaviors
4. **C2 Adaptation Guidelines**: Structure recommendations for degraded ops
5. **Information Priority Framework**: What to transmit when bandwidth limited

---

# Pilot 4: Ethics & Authority Boundaries

## 4.1 Overview

| Attribute | Specification |
|-----------|---------------|
| **Wargame Type** | Ethical Dilemma Seminar with AI Support |
| **Duration** | 2 days (14 hours of play) |
| **Participants** | 20-25 |
| **Primary Gap Area** | Ethics & Legal Compliance |
| **AI Demonstration** | ROE encoding + Authority reasoning + Explanation generation |

### ME Gap Questions Addressed

| ID | Question | Priority |
|----|----------|----------|
| ETHICS-Q01 | ROE constraints encoded in autonomous systems | HIGH |
| ETHICS-Q02 | Human oversight structure for autonomous systems | HIGH |
| ETHICS-Q03 | Human-in-the-loop vs. human-on-the-loop boundaries | HIGH |
| ETHICS-Q05 | Mission-constraint conflict resolution | HIGH |

---

## 4.2 Scenario: OPERATION MORAL COMPASS

### Scenario Design

A series of **15 ethical vignettes** presenting progressively complex situations:

| Vignette Set | Focus | AI Role |
|--------------|-------|---------|
| Set A (1-3) | Clear ROE cases | Demonstrate correct constraint application |
| Set B (4-7) | Boundary cases | Test AI uncertainty communication |
| Set C (8-11) | Conflict cases | Test conflict resolution reasoning |
| Set D (12-15) | Novel cases | Test generalization and explanation |

### Sample Vignette

```
VIGNETTE 7: THE MARKET SQUARE

SITUATION: An autonomous weapon system has identified a high-value
target (confirmed hostile commander) entering a crowded market square.
The system's engagement window is 45 seconds before the target enters
a building.

COMPLICATING FACTORS:
- Civilian density: ~200 people within 50m
- Collateral damage estimate: 15-25 civilian casualties (medium confidence)
- Target value: Responsible for 3 previous attacks killing 45 soldiers
- Alternative: Ground team 10 minutes away (60% intercept probability)
- ROE: Proportionality required; commander approval for >10 civilian CDE

SYSTEM RECOMMENDATION: Request commander approval for engagement

QUESTIONS FOR DISCUSSION:
1. Should the autonomous system have flagged this for human decision?
2. What information should the system provide to the commander?
3. How should uncertainty in the CDE be communicated?
4. What is the appropriate timeline for human decision?
```

---

## 4.3 AI Integration

### Symbolic Components (Primary)

| Component | Application |
|-----------|-------------|
| **Knowledge Graph** | Encode ROE rules, legal frameworks, precedents |
| **Reasoning Engine** | Apply ROE constraints to vignettes |
| **Explanation Engine** | Generate reasoning for AI determinations |
| **Constraint Manager** | Identify constraint conflicts |

### Neural Components (Supporting)

| Component | Application |
|-----------|-------------|
| **Pattern Learner** | Identify patterns in expert judgments |
| **Scenario Generator** | Generate additional boundary cases |

### AI Outputs for Each Vignette

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI ETHICS ANALYSIS                            │
├─────────────────────────────────────────────────────────────────┤
│ VIGNETTE: 7 - The Market Square                                 │
│                                                                  │
│ ROE CONSTRAINT ANALYSIS:                                        │
│   □ Self-defense: Not applicable                                │
│   □ Positive identification: SATISFIED (high confidence)        │
│   □ Proportionality: REQUIRES REVIEW (CDE >10)                  │
│   □ Discrimination: UNCERTAIN (civilian density)                │
│   □ Military necessity: SATISFIED                               │
│   □ Commander approval: REQUIRED (per ROE 4.3.2)                │
│                                                                  │
│ AUTHORITY DETERMINATION:                                        │
│   Recommended: HUMAN-IN-THE-LOOP                                │
│   Reason: CDE threshold exceeded; proportionality judgment      │
│           required; time available for human decision           │
│                                                                  │
│ CONFIDENCE: 85%                                                 │
│ UNCERTAINTY SOURCES:                                            │
│   - CDE estimate has medium confidence (±10 casualties)         │
│   - Target identification high but not certain                  │
│                                                                  │
│ COUNTERFACTUAL:                                                 │
│   If CDE <10: System could engage under ROE 4.2.1               │
│   If no civilians: Clear engagement authorization               │
│                                                                  │
│ PRECEDENT CASES: [3 similar cases from training data]           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.4 Discussion Structure

### For Each Vignette

| Phase | Duration | Activity |
|-------|----------|----------|
| Presentation | 5 min | Read vignette, view AI analysis |
| Individual Reflection | 5 min | Personal assessment |
| Small Group Discussion | 15 min | 4-5 person groups |
| AI Interrogation | 10 min | Query AI for additional reasoning |
| Plenary Discussion | 15 min | Full group synthesis |
| AI Learning | 5 min | AI captures consensus/disagreement |

### Expert Panel

A panel of 4-5 experts (legal, ethics, operations, AI) provides authoritative perspective after each vignette set.

---

## 4.5 Measures

### MoEs

| MoE | Definition | Target |
|-----|------------|--------|
| ROE Coverage | % of ROE correctly encoded | ≥95% |
| Authority Clarity | % of cases with clear determination | ≥80% |
| Conflict Resolution | Satisfactory resolution of conflicts | ≥75% |

### MoPs

| MoP | Definition |
|-----|------------|
| AI-Expert Agreement | % alignment on determinations |
| Explanation Sufficiency | Expert rating of AI explanations |
| Boundary Identification | AI identification of edge cases |

---

## 4.6 Expected Outputs

1. **ROE Encoding Validation**: Verified constraint representations
2. **Authority Boundary Framework**: Human-in vs. on-the-loop criteria
3. **Explanation Requirements**: Content standards for AI ethics reasoning
4. **Conflict Resolution Protocol**: Process for mission-constraint conflicts
5. **Training Requirements**: Preparation for ethical AI oversight

---

# Pilot 5: Failure Mode Analysis

## 5.1 Overview

| Attribute | Specification |
|-----------|---------------|
| **Wargame Type** | Fault Injection Tabletop |
| **Duration** | 1.5 days (12 hours of play) |
| **Participants** | 15-18 |
| **Primary Gap Area** | Failure Modes & Graceful Degradation |
| **AI Demonstration** | Cascade prediction + Dependency tracing + MVP identification |

### ME Gap Questions Addressed

| ID | Question | Priority |
|----|----------|----------|
| FAILURE-Q01 | Single points of failure with no operational workaround | HIGH |
| FAILURE-Q02 | Mission effectiveness degradation and minimum viable configuration | HIGH |

---

## 5.2 Scenario: SYSTEM STRESS TEST

### Architecture Under Test

A representative mission system architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MISSION SYSTEM ARCHITECTURE                   │
│                                                                  │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │ Sensors │───►│ Fusion  │───►│ Decision│───►│ Effectors│     │
│  │         │    │ Engine  │    │ Support │    │         │     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │            │
│       └──────────────┼──────────────┼──────────────┘            │
│                      ▼                                          │
│               ┌─────────────┐                                   │
│               │ Communications│                                  │
│               │    Network    │                                  │
│               └─────────────┘                                   │
│                      │                                          │
│       ┌──────────────┼──────────────┐                          │
│       ▼              ▼              ▼                          │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐                      │
│  │ Platform│   │ Platform│   │ Platform│                      │
│  │    A    │   │    B    │   │    C    │                      │
│  └─────────┘   └─────────┘   └─────────┘                      │
└─────────────────────────────────────────────────────────────────┘
```

### Failure Injection Schedule

| Phase | Failures Injected | Severity |
|-------|-------------------|----------|
| Phase 1 | Single component failures | Low |
| Phase 2 | Multiple independent failures | Medium |
| Phase 3 | Cascading failure scenarios | High |
| Phase 4 | Near-total system degradation | Critical |

---

## 5.3 AI Integration

### Neural Components

| Component | Application |
|-----------|-------------|
| **Prediction Engine** | Predict cascade effects from failures |
| **Pattern Learner** | Identify failure combination patterns |

### Symbolic Components

| Component | Application |
|-----------|-------------|
| **Knowledge Graph** | Model system dependencies |
| **Reasoning Engine** | Trace failure propagation paths |
| **Explanation Engine** | Explain cascade mechanisms |

### AI Analysis for Each Failure

```
┌─────────────────────────────────────────────────────────────────┐
│                    FAILURE ANALYSIS                              │
├─────────────────────────────────────────────────────────────────┤
│ FAILURE INJECTED: Fusion Engine offline                         │
│                                                                  │
│ DIRECT IMPACTS:                                                 │
│   - Sensor data not correlated                                  │
│   - Decision support degraded                                   │
│                                                                  │
│ CASCADE PREDICTION (Neural):                                    │
│   - 85% probability: Targeting accuracy drops to <50%           │
│   - 70% probability: Engagement timeline extends 3×             │
│   - 45% probability: Platform coordination fails                │
│                                                                  │
│ DEPENDENCY TRACE (Symbolic):                                    │
│   Fusion Engine → Decision Support → Targeting → Effectors      │
│   Fusion Engine → Situation Awareness → Commander Decision      │
│                                                                  │
│ WORKAROUND AVAILABLE: Manual fusion (degraded performance)      │
│ WORKAROUND EFFECTIVENESS: 60% of normal                         │
│                                                                  │
│ SINGLE POINT OF FAILURE: YES                                    │
│ CRITICALITY: HIGH                                               │
│                                                                  │
│ MINIMUM VIABLE CONFIGURATION:                                   │
│   Without fusion: Can achieve 40% mission effectiveness         │
│   Threshold for mission abort: 30%                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.4 Game Mechanics

### Failure Response Process

For each injected failure:

1. **AI Prediction** (2 min): AI predicts cascade effects
2. **Player Response** (10 min): Teams develop workarounds
3. **Adjudication** (5 min): Assess workaround effectiveness
4. **Cascade Resolution** (5 min): Apply actual cascade effects
5. **AI Comparison** (3 min): Compare prediction to actual

### MVP Identification Exercise

Participants work to identify the minimum viable configuration:

| Mission Objective | Required Components | Acceptable Degradation |
|-------------------|---------------------|------------------------|
| Primary objective | TBD by participants | TBD |
| Secondary objective | TBD | TBD |
| Essential objective | TBD | TBD |

---

## 5.5 Expected Outputs

1. **SPOF Catalog**: Identified single points of failure
2. **Cascade Model Validation**: AI prediction accuracy assessment
3. **MVP Configurations**: Minimum viable system configurations
4. **Workaround Effectiveness**: Quantified degradation by failure type
5. **Resilience Requirements**: Architecture recommendations

---

# Cross-Pilot Integration

## Synthesis Plan

| Integration Activity | Timing | Purpose |
|---------------------|--------|---------|
| Pattern Cross-Reference | After each pilot | Identify common patterns |
| Knowledge Graph Merge | After pilots 1-3 | Build cumulative knowledge |
| Methodology Refinement | After each pilot | Improve for next pilot |
| Final Synthesis | After pilot 5 | Comprehensive findings |

## Cumulative Knowledge Building

```
Pilot 1 → Knowledge about coalition constraints
    ↓
Pilot 2 → Add human-AI teaming patterns
    ↓
Pilot 3 → Add degradation/autonomy insights
    ↓
Pilot 4 → Add ethics/authority framework
    ↓
Pilot 5 → Add resilience/failure insights
    ↓
INTEGRATED KNOWLEDGE BASE
```

## Success Criteria for Pilot Portfolio

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| ME Questions Addressed | 14 of 18 HIGH priority | Count |
| AI TRL Advancement | TRL 3 → 4 for all components | Assessment |
| Methodology Validation | 80% process steps validated | Checklist |
| Insight Generation | ≥50 validated insights | Count |
| Cross-Pilot Learning | Demonstrated knowledge transfer | Qualitative |

---

*Document prepared for NATO STO TAP development.*
*Version 1.0 - 2026-01-22*
