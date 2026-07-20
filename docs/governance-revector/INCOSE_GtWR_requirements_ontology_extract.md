# INCOSE Guide for Writing Requirements (GtWR) — Ontology and Rules Extract

**Prepared for:** governance-revector work stream (PostWach hive)
**Prepared by:** PostWach research agent
**Date:** 2026-07-14
**Source status:** See REFERENCES section

---

## 1. Source Location

**LOCAL — found in the NNSA project portfolio.**

Primary source files (read-only, all under the NNSA WRT-2516 project):

- `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\incose_rules.json` — flat JSON rule set (A-criterion scheme used by the RE_Assistant tool)
- `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\ontology\incose-req.ttl` — BFO 2020-aligned TBox (class hierarchy + properties)
- `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\ontology\incose-req-rules.ttl` — ABox with all 42 rules, 15 quality characteristics, 14 categories
- `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\ontology\incose-req.shapes.ttl` — SHACL validation shapes
- `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\INCOSE_Requirements_Ontology_Plan_2026-03-26.md` — design rationale document

The ontology is a **formalization** of the INCOSE Guide to Writing Requirements; it is a research artifact (a) derived from that guide. It does not replace the authoritative guide text.

---

## 2. Requirement Ontology / Information Model

### 2.1 Entity Types (Classes)

The ontology (incose-req.ttl) defines nine entity types, BFO 2020-aligned:

| Class | BFO Category | Definition |
|---|---|---|
| `Requirement` | Generically Dependent Continuant (GDC) | A textual information entity specifying a capability, characteristic, constraint, or quality factor that a system must possess |
| `RequirementSet` | GDC | A structured collection of individual needs and/or requirement statements organized as an information artifact (e.g., specification document, DOORS module) |
| `QualityCharacteristic` | GDC | A published definition of a desirable property of a requirement or requirement set |
| `IndividualQualityCharacteristic` | GDC (subclass of QualityCharacteristic) | Applies to individual need and requirement statements (Section 2, C1-C9) |
| `SetQualityCharacteristic` | GDC (subclass of QualityCharacteristic) | Applies to sets of needs and requirements (Section 3, C10-C15) |
| `Rule` | GDC | A published assessment criterion from Section 4, with definition, elaboration, examples, exceptions, and characteristic linkages (42 rules in V4) |
| `RuleCategory` | GDC | A named grouping of related rules (14 categories in V4) |
| `Violation` | Specifically Dependent Continuant (SDC) | A finding that a specific requirement fails to satisfy a specific rule; inheres in the requirement instance |
| `Assessment` | BFO Process | A temporal act of evaluating a requirement or requirement set against rules |
| `AssessmentResult` | GDC | An information artifact produced by an Assessment process |
| `SeverityRating` | GDC | An ordinal position on a severity scale (Low / Medium / High / Critical) |
| `RuleApplicability` | GDC | Level of applicability of a rule (CNCR / RNCR / CR) |

### 2.2 Object Properties (Relationships)

| Property | Domain | Range | Constraint |
|---|---|---|---|
| `testsCharacteristic` | Rule | QualityCharacteristic | Many-to-many |
| `belongsToCategory` | Rule | RuleCategory | Functional (exactly 1) |
| `hasApplicability` | Rule | RuleApplicability | Functional (exactly 1) |
| `violatesRule` | Violation | Rule | Functional (exactly 1) |
| `inheresInRequirement` | Violation | Requirement | Functional (exactly 1); subproperty of BFO `inheres_in` |
| `hasSeverityRating` | Violation | SeverityRating | Functional (exactly 1) |
| `memberOfSet` | Requirement | RequirementSet | Many-to-many |
| `assessesSet` | Assessment | RequirementSet | Many-to-many |
| `hasResult` | Assessment | AssessmentResult | Functional (exactly 1) |
| `includesViolation` | AssessmentResult | Violation | Many-to-many |

### 2.3 Data Properties

| Property | Domain | Type | Notes |
|---|---|---|---|
| `hasRuleId` | Rule | xsd:string | Pattern `^R[0-9]{1,2}$`; R1-R42 |
| `hasCharacteristicId` | QualityCharacteristic | xsd:string | Pattern `^C[0-9]{1,2}$`; C1-C15 |
| `hasShortDescription` | (all) | xsd:string | Brief description |
| `hasOrdinalRank` | SeverityRating | xsd:integer | 1=Low, 2=Medium, 3=High, 4=Critical |
| `requiresProjectDictionary` | Rule | xsd:boolean | Whether assessment requires a project data dictionary/glossary |
| `hasAffectedText` | Violation | xsd:string | Verbatim substring that triggered the violation |
| `hasAssessmentDate` | Assessment | xsd:dateTime | Date/time of assessment |
| `hasAssessor` | Assessment | xsd:string | Human or AI tool identifier |
| `hasRequirementId` | Requirement | xsd:string | Identifier within source document |
| `hasStatementText` | Requirement | xsd:string | Full text of the requirement statement |

### 2.4 Rule Applicability Levels (Appendix D)

Three levels govern whether a rule applies to needs, requirements, or both:

- **CNCR** — Compulsory for Needs and Compulsory for Requirements
- **RNCR** — Recommended for Needs, Compulsory for Requirements
- **CR** — Compulsory for Requirements only (optional for needs)

---

## 3. Needs-vs-Requirements Distinction

The ontology distinguishes two document-level entity types — needs and requirements — but does not define them as separate classes; both are instances of `Requirement`. The distinction is encoded via:

1. **Rule applicability** (Appendix D): rules tagged CNCR apply to needs and requirements; rules tagged CR apply only to requirements. This operationalizes the need/requirement split at the rule level without duplicating the class hierarchy.

2. **RequirementSet-level characteristics** (C10-C15) govern the collection as a whole, applying regardless of whether individual statements are needs or requirements.

**Note on source:** The GtWR ontology plan (§1) characterizes the distinction as arising from the "life cycle concept, need, source, or parent requirement" to which a statement traces (C1, Necessary). The ontology does not encode a formal Needs class separate from Requirements. If a separate `Need` subclass is required for the governance spec rewrite, it would need to be added as a design extension.

---

## 4. Quality Characteristics — Individual (C1-C9)

Defined in GtWR Section 2. Applied to individual need and requirement statements.

| ID | Name | Definition (from ontology ABox) |
|---|---|---|
| C1 | Necessary | The requirement defines an essential capability, characteristic, constraint, or quality factor |
| C2 | Appropriate | The specific intent and amount of detail is appropriate to the level of the entity to which it refers |
| C3 | Unambiguous | The requirement is stated such that it can be interpreted in only one way |
| C4 | Complete | The requirement sufficiently describes the necessary capability, characteristic, constraint, or quality factor to meet the entity need |
| C5 | Singular | The requirement states a single capability, characteristic, constraint, or quality factor |
| C6 | Feasible | The requirement can be realized within entity constraints with acceptable risk |
| C7 | Verifiable/Validatable | The requirement is structured and worded such that its realization can be proven to the stakeholders' satisfaction |
| C8 | Correct | The requirement is an accurate representation of the entity need from which it was transformed |
| C9 | Conforming | The individual requirement conforms to an approved style guide or similar standard |

---

## 5. Quality Characteristics — Set Level (C10-C15)

Defined in GtWR Section 3. Applied to requirement sets as a whole.

| ID | Name | Definition (from ontology ABox) |
|---|---|---|
| C10 | Complete (Set) | The requirement set stands alone such that it sufficiently describes the necessary capabilities, characteristics, constraints, and/or quality factors |
| C11 | Consistent | The set contains individual requirements that are unique, do not conflict, and are not duplicated |
| C12 | Feasible (Set) | The requirement set can be realized within entity constraints with acceptable risk |
| C13 | Comprehensible | The requirement set is written such that it is clear, structured, and readable |
| C14 | Able to be Validated | The requirement set can be proven to satisfy its intended use in the operational environment |
| C15 | Correct (Set) | The requirement set accurately represents the entity needs from which it was transformed |

---

## 6. Requirement Boilerplate / Grammar Pattern

The GtWR prescribes structured statement patterns. From Rule R1 ("Structured Statements") and R2 ("Active Voice") and the RE_Assistant tool prompt (A10.1):

**Canonical form:**
```
The [subject/system-of-interest] shall [imperative verb] [object/complement] [condition/constraint].
```

**Elements of the pattern:**

1. **Subject** — The system of interest (named entity; use definite article "the" per R5; not a subsystem, user, or external system per R3/C2)
2. **Modal verb** — `shall` for compulsory requirements; `should` for recommendations; `may` for permissive
3. **Imperative verb** — Action verb in active voice (R2); avoid superfluous infinitives such as "be designed to," "be able to," "enable" (R10)
4. **Object/complement** — What the system must do or have; use explicit terms defined in glossary (R4)
5. **Condition** (optional) — Explicit operational condition or mode (R27: "when X," "in state Y"); expressed propositionally (R28)
6. **Constraint/qualifier** — Performance parameter with units and range/tolerance (R6, R33, R34); temporal dependencies explicit (R35)

**Anti-patterns explicitly prohibited:**
- Passive voice (R2 violation)
- Superfluous infinitives: "shall be able to," "shall be designed to," "shall enable" (R10)
- Combinators joining two thoughts: "and," "or," "then," "unless," "but," "as well as" (R19)
- Vague terms: "user-friendly," "flexible," "robust," "as appropriate," "if necessary" (R7)
- Escape clauses: "where possible," "if practicable," "to the extent possible" (R8)
- Open-ended clauses: "including but not limited to," "etc.," "and so on" (R9)
- Negative constructions: "shall not" where avoidable (R16)
- Oblique symbol "/" except in units or fractions (R17)
- Pronouns: "it," "they," "its," "this" (R24)
- Reliance on headings for meaning (R25)
- Unachievable absolutes: "100%," "always," "never" (R26)
- Parenthetical subordinate text (R21)
- Purpose phrases: "in order to," "purpose of" (R20)
- Universal quantifiers "all," "any," "both" — use "each" instead (R32)

---

## 7. Numbered Rules (R1-R42)

42 rules in GtWR V4, organized across 14 categories. IDs are from the source (incose-req-rules.ttl, derived from GtWR V4 Section 4 + Appendices D and E).

### Category: Accuracy (R1-R9)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R1 | Structured Statements | CNCR | Conform to agreed statement patterns producing a well-structured complete statement |
| R2 | Active Voice | RNCR | Use active voice with responsible entity clearly identified as subject |
| R3 | Appropriate Subject-Verb | CNCR | Ensure subject and verb are appropriate to the entity to which the statement refers |
| R4 | Defined Terms | CNCR | Define all terms in an associated glossary and/or data dictionary |
| R5 | Definite Articles | RNCR | Use definite article "the" rather than indefinite "a" |
| R6 | Common Units of Measure | CNCR | State quantities using appropriate, consistent, explicitly stated units conforming to a common measurement system |
| R7 | Vague Terms | CNCR | Avoid vague terms |
| R8 | Escape Clauses | RNCR | Avoid escape clauses stating vague conditions or possibilities |
| R9 | Open-Ended Clauses | CNCR | Avoid open-ended non-specific clauses such as "including but not limited to," "etc." |

### Category: Concision (R10-R11)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R10 | Superfluous Infinitives | CR | Avoid superfluous infinitives such as "to be designed to," "to be able to," "to enable" |
| R11 | Separate Clauses | CNCR | Use a separate clause for each condition or qualification |

### Category: Non-Ambiguity (R12-R17)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R12 | Correct Grammar | CNCR | Use correct grammar |
| R13 | Correct Spelling | CNCR | Use correct spelling |
| R14 | Correct Punctuation | CNCR | Use correct punctuation |
| R15 | Logical Expressions | CNCR | Use defined convention to express logical expressions: [X AND Y], [X OR Y], [X XOR Y], NOT [X OR Y] |
| R16 | Use of "Not" | RNCR | Avoid the word "not" |
| R17 | Use of Oblique Symbol | CNCR | Avoid the "/" symbol except in units or fractions |

### Category: Singularity (R18-R23)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R18 | Single Thought Sentence | CNCR | Write a single sentence containing a single thought conditioned and qualified by relevant sub-clauses |
| R19 | Combinators | CNCR | Avoid combinators joining clauses: "and," "or," "then," "unless," "but," "as well as," "however," "whether," "whereas" |
| R20 | Purpose Phrases | CNCR | Avoid phrases indicating purpose: "purpose of," "intent of," "reason for" |
| R21 | Parentheses | CNCR | Avoid parentheses and brackets containing subordinate text |
| R22 | Enumeration | RNCR | Enumerate sets explicitly instead of using a group noun |
| R23 | Supporting Diagram/Model/ICD | RNCR | When requirement relates to complex behavior, reference the supporting diagram, model, or ICD |

### Category: Completeness (R24-R25)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R24 | Pronouns | CNCR | Avoid personal and indefinite pronouns |
| R25 | Headings | CNCR | Avoid relying on headings to support explanation or understanding |

### Category: Realism (R26)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R26 | Absolutes | CNCR | Avoid unachievable absolutes |

### Category: Conditions (R27-R28)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R27 | Explicit Conditions | RNCR | State conditions' applicability explicitly instead of leaving applicability to be inferred from context |
| R28 | Multiple Conditions | CR | Express propositional nature of a condition explicitly for a single action instead of giving lists of actions for a specific condition |

### Category: Uniqueness (R29-R30)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R29 | Classification | CNCR | Classify needs and requirements according to the aspects of the problem or system addressed |
| R30 | Unique Expression | CNCR | Express each need and requirement once and only once |

### Category: Abstraction (R31)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R31 | Solution Free | CNCR | Avoid stating implementation in a need or requirement statement unless there is rationale for constraining the design |

### Category: Quantifiers (R32)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R32 | Universal Qualification | RNCR | Use "each" instead of "all," "any," or "both" when universal quantification is intended |

### Category: Tolerance (R33)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R33 | Range of Values | CR | Define each quantity with a range of values appropriate to the entity and against which it will be verified or validated |

### Category: Quantification (R34-R35)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R34 | Measurable Performance | RNCR | Provide specific measurable performance targets appropriate to the entity |
| R35 | Temporal Dependencies | RNCR | Define temporal dependencies explicitly instead of using indefinite temporal keywords |

### Category: Uniformity of Language (R36-R40)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R36 | Consistent Terms and Units | CNCR | Ensure each term and unit of measure is used consistently throughout the requirement set and associated models |
| R37 | Acronyms | CNCR | Acronyms must be consistent throughout the requirement set and associated models |
| R38 | Abbreviations | CNCR | Avoid abbreviations in need and requirement statements and associated models |
| R39 | Style Guide | CNCR | Use a project-wide style guide for individual need and requirement statements |
| R40 | Decimal Format | CNCR | Use consistent format and number of significant digits for decimal numbers |

### Category: Modularity (R41-R42)

| ID | Name | Applicability | Short Description |
|---|---|---|---|
| R41 | Related Needs and Requirements | CNCR | Group related needs and requirements together |
| R42 | Structured Sets | CNCR | Conform to a defined structure or template for organizing sets of needs and requirements |

---

## 8. Rule-to-Characteristic Cross-Reference Summary

Derived from GtWR V4 Appendix E. Each rule maps to one or more quality characteristics.

| Rule | Characteristics tested |
|---|---|
| R1 | C3, C4, C7, C8, C9 |
| R2 | C3, C4, C7 |
| R3 | C3, C7, C8, C14 |
| R4 | C3, C7, C9, C11, C12, C13, C14 |
| R5 | C3, C7 |
| R6 | C3, C4, C7, C8 |
| R7 | C3, C4, C7 |
| R8 | C3, C7 |
| R9 | C3, C4, C5, C7 |
| R10 | C3, C7 |
| R11 | C3, C4, C7, C8 |
| R12 | C3, C7, C8, C9 |
| R13 | C3, C7 |
| R14 | C3, C8 |
| R15 | C3, C7 |
| R16 | C3, C7, C8 |
| R17 | C3, C7 |
| R18 | C3, C4, C7, C8, C14 |
| R19 | C3, C5 |
| R20 | C1, C5 |
| R21 | C5 |
| R22 | C3, C5 |
| R23 | C3, C4 |
| R24 | C3, C4, C7 |
| R25 | C3, C7 |
| R26 | C6, C7, C8, C14 |
| R27 | C4, C7, C8 |
| R28 | C3, C7 |
| R29 | C10, C11 |
| R30 | C1, C8, C11 |
| R31 | C2 |
| R32 | C4, C7, C8 |
| R33 | C3, C4, C6, C7, C8, C14 |
| R34 | C3, C4, C7, C14 |
| R35 | C3, C4, C7 |
| R36 | C4, C7, C8, C10, C12, C13, C14, C15 |
| R37 | C3, C7, C10, C12, C13, C14 |
| R38 | C7, C10, C12, C13, C14 |
| R39 | C3, C4, C5, C7, C10, C12, C13, C14 |
| R40 | C1, C3, C7, C10 |
| R41 | C4, C7, C8, C9, C10, C14 |
| R42 | C7, C8, C10, C11, C12, C13, C14 |

---

## 9. Applicability Counts Summary

- **CNCR** (compulsory for both needs and requirements): R1, R3, R4, R6, R7, R9, R11, R12, R13, R14, R15, R17, R18, R19, R20, R21, R24, R25, R26, R29, R30, R31, R36, R37, R38, R39, R40, R41, R42 — **29 rules**
- **RNCR** (recommended for needs, compulsory for requirements): R2, R5, R8, R22, R23, R27, R32, R34, R35 — **9 rules**
- **CR** (compulsory for requirements only): R10, R28, R33 — **3 rules**
- Total: **41 rules counted**; the ABox instantiates 42 (R1-R42 as labeled in the source)

---

## 10. Notes on Verification Status

The following items are verified against locally held artifacts:

- Rule IDs R1-R42 and their descriptions: **VERIFIED** against `incose-req-rules.ttl` (committed artifact in WRT-2516 NNSA project)
- Characteristic IDs C1-C9 and C10-C15 and their definitions: **VERIFIED** against `incose-req-rules.ttl`
- Category names and rule-to-category assignments: **VERIFIED** against `incose-req-rules.ttl`
- Applicability levels (CNCR/RNCR/CR): **VERIFIED** against `incose-req-rules.ttl`
- Rule-to-characteristic cross-reference matrix: **VERIFIED** against `incose-req-rules.ttl` (derived from GtWR V4 Appendix E per ontology comments)
- Boilerplate grammar pattern (canonical "The system shall..."): **VERIFIED** against `incose_rules.json` (A10.1) and `ai_analyzer.py` prompt text

The following items are **NOT independently verified against the GtWR document text** (the GtWR PDF itself is not held in this portfolio):

- That the ontology accurately captures all rules without omission or misstatement
- That the Appendix E cross-reference matrix was transcribed without error
- That rule elaborations and examples from GtWR Sections 4.1-4.14 are fully captured (the ontology stores short descriptions only)
- Formal distinction between "needs" and "requirements" as entity types in GtWR Section 1

---

## REFERENCES

| Field | Value |
|---|---|
| Author(s) | Ryan, M. and Wheatcraft, L. (principal authors, per ontology header comment) [UNVERIFIED — name appears in code comment, not independently confirmed] |
| Organization | INCOSE (International Council on Systems Engineering) Requirements Working Group |
| Title | Guide to Writing Requirements |
| Version/Edition | Version/Revision 4 (V4) |
| Date | 1 July 2023 |
| Document number | INCOSE-TP-2010-006-04 |
| ISBN | 978-1-93707-05-4 [UNVERIFIED — appears in ontology header comment] |
| URL/DOI | [UNVERIFIED — not held locally; available via INCOSE store at incose.org] |
| Verification status | **PRIMARY SOURCE NOT HELD LOCALLY.** All content above is extracted from derivative artifacts (ontology, JSON rules file) created by P. Wach (UA) for WRT-2516 project. The derivative artifacts claim to formalize GtWR V4 (1 Jul 2023). The GtWR document itself has not been independently verified by this extraction process. |

**Derivative source (verified as locally present):**

- `incose-req.ttl`, `incose-req-rules.ttl`, `incose-req.shapes.ttl` — P. Wach, University of Arizona, WRT-2516, 2026-03-26, version 0.1.0. Located at `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\ontology\`
- `incose_rules.json` — P. Wach / VT team, WRT-2516. Located at `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\RE_Assistant_VT\backend\`
- `INCOSE_Requirements_Ontology_Plan_2026-03-26.md` — P. Wach, University of Arizona, 2026-03-26. Located at `C:\Users\pfwac\OneDrive - University of Arizona\Documents\03 Projects\01 NNSA\01 Deliverables\`
