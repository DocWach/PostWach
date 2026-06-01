# Statement of Work: Subcontract to The Value Enablement Group, LLC

**Prime Award:** DARPA-PA-25-07-02 (CLARA), TA1
**Prime Contractor:** University of Arizona
**Subcontractor:** The Value Enablement Group, LLC (VEG)
**Subcontractor PI:** Jeffrey Wallk, Managing Partner
**Period of Performance:** 24 months (Phase 1: 15 months; Phase 2: 9 months)
**Estimated Start Date:** June 22, 2026

---

## Summary

- Design and document the integration architecture connecting AR and ML components into the morphism composition pipeline
- Specify data flow, interface contracts, and trust metrology dashboard architecture
- Design deployment architecture (containerized services, APIs, monitoring)
- Support IV&V interactions, Hackathon preparation, and inter-performer workshops
- Attend program-wide meetings as second essential personnel
- Contribute to progress reports and final report

---

## 1. Background

The University of Arizona (UA) is preparing a proposal to DARPA under the Compositional Learning-And-Reasoning for AI Complex Systems Engineering (CLARA) program, TA1. The project, titled "Morphism-Grounded Compositional Assurance for Autonomous AI Systems," develops a formal framework for composing AI subsystems with verifiable trust guarantees grounded in systems-theoretic morphisms.

VEG provides systems architecture and data architecture expertise to complement UA's theoretical and implementation capabilities.

---

## 2. Scope of Work

VEG shall perform the following tasks under the direction of the UA PI.

### Task 1: Systems Architecture Design (Phase 1, Months 1-6)

- Design the integration architecture connecting AR components (OWL 2 DL ontology, Bayesian Logic Programs) with ML components (Transformer encoders, FAISS) into a unified pipeline
- Specify data flow, interface contracts, and component interaction patterns for the morphism composition chain
- Define the trust metrology dashboard architecture (graduated verdict display, real-time D_h monitoring, SPC chart integration)
- Document architecture decisions in a Systems Architecture Document (SAD)

**Deliverable:** Systems Architecture Document (SAD), v1.0

### Task 2: Trust Metrology Integration Framework (Phase 1, Months 4-12)

- Design the runtime integration layer that connects morphism quality instruments (D_s, D_b, d_cos) to the composition verdict engine
- Specify the interface between the SPC engine and the circuit breaker trigger logic (Normal/Caution/Restrict/Halt/Lockdown graduated response)
- Define data formats and protocols for morphism quality certificates
- Support integration testing of the composed AR-ML pipeline on the ECG testbed

**Deliverable:** Integration Framework Specification; integration test support artifacts

### Task 3: Deployment Architecture and Standards Alignment (Phase 1, Months 9-15)

- Design the deployment architecture for the composed system (containerized services, API specifications, monitoring endpoints)
- Assess alignment with relevant deployment standards for safety-critical AI systems
- Support IV&V team interactions and Hackathon preparation (software packaging, documentation, demonstration materials)
- Contribute to Workshop participation and inter-performer technical discussions

**Deliverable:** Deployment Architecture Document; Hackathon support materials

### Task 4: Phase 2 Extension Support (Phase 2, Months 16-24)

- Update the systems architecture to accommodate the second ML kind (Bayesian neural networks) and AR-constrained training pipeline
- Extend the integration framework for the three-task composed pipeline (arrhythmia classification, guideline compliance, end-to-end patient monitoring)
- Support the domain-transfer cost analysis by documenting architecture portability and domain-specific vs. domain-agnostic components
- Contribute to Hackathon #2 preparation and final software release

**Deliverable:** Updated SAD v2.0; domain-transfer architecture analysis; Hackathon #2 support

### Task 5: Program Participation (Phases 1 and 2)

- Attend program-wide meetings (Phase Kickoff Meetings, Workshops, Hackathons) as the second essential personnel
- Participate in regular coordination meetings with the UA PI (biweekly minimum)
- Contribute to progress reports and the final report

**Deliverable:** Meeting attendance; written contributions to progress and final reports

---

## 3. Cost Allocation

**Overall split:** 75% UA / 25% VEG of total proposed budget ($1.85M)

| | Phase 1 (15 mo) | Phase 2 (9 mo) | Total |
|---|---|---|---|
| **UA** | $825,000 | $562,500 | $1,387,500 |
| **VEG** | $275,000 | $187,500 | $462,500 |
| **Total** | $1,100,000 | $750,000 | $1,850,000 |

### VEG Cost Breakdown (Estimated)

| Category | Phase 1 | Phase 2 | Total |
|---|---|---|---|
| Direct Labor (Jeffrey Wallk) | $200,000 | $130,000 | $330,000 |
| Travel (program meetings) | $20,000 | $12,500 | $32,500 |
| Other Direct Costs (computing, materials) | $10,000 | $10,000 | $20,000 |
| G&A / Overhead | $45,000 | $35,000 | $80,000 |
| **Subtotal** | **$275,000** | **$187,500** | **$462,500** |

*Note: VEG cost categories and rates subject to negotiation and VEG's disclosed rate structure. VEG does not carry university F&A overhead, so a higher proportion of the subcontract flows to direct labor.*

### Milestone Payment Alignment

VEG payments shall align with the DARPA milestone schedule:

| Month | DARPA Milestone | VEG Deliverable | Est. Payment |
|---|---|---|---|
| 1 | Kickoff | Personnel confirmed; SAD outline | $30,000 |
| 3 | Progress report | SAD v1.0 draft | $40,000 |
| 6 | Demo: initial capability | Integration Framework Spec | $50,000 |
| 9 | Demo: composed capability | Deployment Architecture; Hackathon prep | $55,000 |
| 12 | Hackathon #1; progress report | Hackathon participation; integration artifacts | $50,000 |
| 15 | Phase 1 final | Phase 1 closeout deliverables | $50,000 |
| 18 | Demo: extended capability | Updated SAD v2.0 | $50,000 |
| 22 | Hackathon #2 | Hackathon participation; final integration | $50,000 |
| 24 | Phase 2 final | Domain-transfer analysis; final report contributions | $87,500 |
| | | **Total** | **$462,500** |

---

## 4. Reporting

- Biweekly written status to the UA PI (brief, email-format)
- Written contributions to DARPA progress reports at Months 3, 6, 9, 12, 15, 18, 22, 24
- Final report contributions due 30 days before program end

## 5. Data Rights

All work product shall be delivered under Apache 2.0 license, consistent with CLARA program requirements. VEG shall not incorporate proprietary or restricted IP into deliverables without prior written approval from the UA PI.

## 6. Key Personnel

- **Jeffrey Wallk**, Managing Partner, VEG -- Co-PI, systems architecture lead

Substitution of key personnel requires prior written approval from the UA PI and notification to the DARPA Agreements Officer.

---

*This SOW is a draft for UA ERAS routing and DARPA proposal preparation. Final terms subject to subcontract negotiation between UA and VEG.*
