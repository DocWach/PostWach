---
title: "LEGO Mindstorms EV3 Model Validation: Student Brief"
subtitle: "Inductive and deductive validation of the EV3 SysML v2 parts library"
author: "Prepared by PostWach for student tasking"
date: "2026-04-29"
geometry: margin=1in
fontsize: 11pt
mainfont: "Calibri"
papersize: letter
toc: false
numbersections: true
header-includes:
  - \usepackage{xcolor}
  - \usepackage{enumitem}
  - \setlist[itemize]{topsep=2pt,itemsep=2pt}
  - \setlist[enumerate]{topsep=2pt,itemsep=2pt}
---

# Purpose

Validate that the LEGO Mindstorms EV3 reusable parts library models real parts and kits correctly. The library is a research artifact at <https://github.com/DocWach/Lego-EV3-Mindstorm-Models>. It carries 172 parts, three kit Bill of Materials (BOM) files, and roughly 37 SysML v2 (Systems Modeling Language version 2) files covering parts, interfaces, behaviors, and requirements. The parser accepts every file with zero errors, but parser-clean is not the same as correct. Your job is to apply human judgment and physical-world checks to the model.

PostWach reviews your final report and decides next steps for the artifact (extend, refactor, or rebuild).

# Time budget

Target 25 hours of effort over two weeks. Hard cap 30 hours. If you hit the cap before finishing, stop and write what you have. A partial report with strong findings beats a complete report with thin findings.

# Deliverables

Two files, submitted together.

1. **Word report.** File name `EV3_Model_Validation_Report_<lastname>_<YYYY-MM-DD>.docx`. Carries prose, the verdict, the verdict justification, and references to finding IDs from the workbook. Sections listed in section 8 of this brief.
2. **Findings workbook.** Use the supplied template `EV3_Model_Validation_Findings_Template_2026-04-29.xlsx`. Save as `EV3_Model_Validation_Findings_<lastname>_<YYYY-MM-DD>.xlsx`. Carries all structured data: BOM tables, findings log, three Phase 3 study tables, verdict summary.

The Word report is for prose and judgment; the workbook is for the data behind every claim. Cite finding IDs (F-NN) from the workbook anywhere you reference a finding in the Word report.

Append a one-line verdict at the top of the Word report: **extend, refactor,** or **rebuild**.

# Working assumptions about you

- SysML v2 fluency: low but aware. You have heard of it, you have not modeled in it.
- LEGO Mindstorms EV3 access: physical kit, no Computer-Aided Design (CAD) tools required.
- This brief is sequenced to build SysML v2 reading fluency before asking you to judge structural choices.

# Workflow

All structured data goes into the findings workbook as you work. The Word report is written last, drawing on what is in the workbook.

## Phase 1: Orientation and deductive anchor (8 hours)

### Step 1.1: Hands-on orientation (2 hours)

1. Open the physical kit. Pick 15 parts of varied types: a beam, a pin, an axle, a gear, a wheel, the brick, a motor, a sensor, a cable, a connector, a panel, a bushing, a frame, a bracket, a specialty piece.
2. For each, find the matching record in `data/parts.json` (search by name or category).
3. For each, open the matching `.sysml` file under `sysml/` (the README explains the directory layout).
4. Note any part you cannot find. Note any record that surprises you.

This step is orientation, not analysis. Do not start logging findings yet.

### Step 1.2: Kit BOM piece-count validation (6 hours)

Three kit files exist:

- `sysml/kits/EV3Kit31313.sysml` claims 601 pieces (Home Edition).
- `sysml/kits/EV3Kit45544.sysml` claims 541 pieces (Education Core).
- `sysml/kits/EV3Kit45560.sysml` claims 853 pieces (Expansion).

For each kit, do **two** checks:

1. **Internal consistency.** Sum the line-item quantities inside the SysML file. Does the sum equal the claimed total? Where it does not, list the discrepancy.
2. **External consistency.** Compare the line-item list against the published inventory for that set on BrickLink or Brickset. Are any parts missing? Are any parts in the SysML kit BOM not in the published inventory?

You may use any approach: hand count, scripted parser, or formulas in the workbook. Document your method.

Record line items on the **Phase 1 BOM** sheet of the findings workbook. The summary panel auto-sums via named ranges and flags internal and external matches per kit. Use the **Notes** column to flag rows where the three values do not agree.

This is the **deductive anchor.** Even if everything else is subjective, this step produces an objective result.

## Phase 2: Inductive walk-through (5 hours)

Read every file under `sysml/` in this order: `domain/` first, then `electronics/`, `hardware/`, `structural/`, `connectors/`, `axles/`, `gears/`, `wheels/`, `other/`, `kits/`, `behavior/`, `requirements/`. Top-level files (`EV3Library.sysml`, `EV3System.sysml`) last.

As you read, log every smell on the **Findings Log** sheet. A smell is anything that makes you pause: an odd name, a duplicated definition, a missing attribute, an inconsistency with the physical part you held in Phase 1, a structural choice that seems wrong.

Aim for at least 12 substantive findings. The workbook pre-numbers IDs F-01 through F-61 with dropdowns for Phase, Severity, and Status. Format details are in section 8.

One free smell is pre-seeded as F-01 in the workbook: both `electronics/` and `hardware/` contain files named `EV3Brick.sysml`, `EV3Motors.sysml`, and `EV3Sensors.sysml`. Determine whether these are intentional layering or unresolved duplication, and complete the F-01 entry with your conclusion.

## Phase 3: Three structural studies (10 hours)

Each study is a focused investigation. Capture structured data on the matching workbook sheet, then write each as a short subsection in the Word report (one to two pages each).

Sheet pointers: Study A on **Phase 3A Multiplicity**, Study B on **Phase 3B Interfaces** (5 scenarios pre-seeded), Study C on **Phase 3C Attributes** (8 attribute checks pre-seeded with measurement methods).

### Study A: Multiplicity and roll-up (2 hours)

**Question.** When a kit has two large servo motors, where does the "two" live? On a port multiplicity? On a kit-level usage instance? On the part definition itself?

Pick 5 parts that appear in multiple kits at varied quantities (a friction pin, a bushing, an axle, a beam, the brick if it appears in more than one). For each, document **how multiplicity is currently captured** and **where you think it should be captured**. State the rule you would propose for the library.

### Study B: Interface capture (4 hours)

**Question.** LEGO Technic has a small, well-defined set of mechanical interfaces: cross-axle hole, technic round hole, friction pin, frictionless pin, stud, anti-stud, gear-tooth mesh, electric port. The model uses SysML v2 ports somewhere. Are these mechanical interfaces typed correctly? Do mating rules hold? For example, friction pins should be allowed to enter technic holes but not cross-axle holes (without forcing).

Use the physical kit to verify mating. Pick 5 connection scenarios (pin-into-beam, axle-into-gear, gear-into-gear, motor-shaft-into-coupler, cable-into-port). For each, document what the model says, what the physical part does, and whether the model represents the constraint.

### Study C: Attribute correctness with physical measurement (4 hours)

**Question.** Are the attributes captured on parts correct?

Pick 8 parts where attributes are measurable from the physical kit. Examples:

- A beam: attribute `length` in modules. Count holes, multiply by 8 mm. Compare.
- A bracket: attribute `angle`. Use a protractor or visually compare to a known reference angle (45°, 53.13°, 90°). Compare.
- An axle: attribute `length`. Count studs. Compare.
- A gear: attribute for tooth count. Count teeth. Compare.
- A cable: attribute `length`. Measure with ruler. Compare.
- A motor or sensor: attribute for cable port type, voltage, or rated speed. Compare to LEGO datasheet.

For each, record the model attribute, the measured value, and whether they agree. Flag any attribute that is missing where a real-world specification exists.

## Phase 4: Verdict and write-up (2 hours)

Complete the **Verdict Summary** sheet in the workbook (verdict dropdown, top 5 findings ranked, open questions). Then write the Word report drawing on the structured data already in the workbook. Choose the verdict.

- **Extend** if the model is roughly correct: minor smells, BOM counts close, attributes mostly right. The next student adds robot configurations or behaviors.
- **Refactor** if the structure is sound but has systematic issues: e.g., duplicate definitions, multiplicity captured inconsistently, interfaces not typed. The next student redesigns specific subsystems.
- **Rebuild** if the modeling foundation is wrong: e.g., parts redefined per kit instead of composed, no real interface model, attributes invented rather than measured. The next student starts over with lessons learned.

Justify the verdict with three to five strongest findings.

# Report structure

Word report sections. Reference the workbook for the underlying data; cite finding IDs (F-NN) where you draw on a finding.

1. **Verdict** (one line at top): extend, refactor, or rebuild.
2. **Summary** (half page): what you did, top three findings, your verdict reasoning.
3. **Phase 1: Kit BOM validation.** Summarize the three kit results in prose; the full tables live in the workbook.
4. **Phase 2: Walk-through findings.** Reference the Findings Log sheet by F-NN; in the prose, narrate the most significant findings (do not duplicate every entry from the workbook).
5. **Phase 3 Study A: Multiplicity.** One to two pages of prose interpreting the workbook table.
6. **Phase 3 Study B: Interface capture.** One to two pages.
7. **Phase 3 Study C: Attribute correctness.** One to two pages.
8. **Verdict justification.** Three to five strongest findings ordered by severity, cited by F-NN.
9. **Open questions.** Anything you could not resolve and want PostWach to weigh in on.
10. **Method notes.** What tools you used, any scripts you wrote, total hours spent.

## Findings log entry format

The workbook **Findings Log** sheet enforces this format. Each row carries:

- ID (pre-numbered F-NN)
- Phase (1, 2, 3A, 3B, 3C, ad-hoc; dropdown)
- Title (short)
- File (`sysml/<path>`)
- Severity (critical, major, minor; dropdown)
- Observation (what you saw)
- Why it matters (one sentence)
- Proposed fix or question
- Status (open, needs-review, resolved, wont-fix; dropdown)
- PostWach Notes (leave blank; for review)

# Out of scope

Do not do these:

- Do not modify the model. Findings only.
- Do not validate against the SysML v2 standard line by line. The parser already passed.
- Do not extend the model with new parts, kits, or behaviors.
- Do not validate the geometry files. The `geometry/` directory is a separate concern.
- Do not run the LDraw to STEP (Standard for the Exchange of Product Data) conversion script in PLMr. That is a separate task for a different student.

# Reference material

- Repository: <https://github.com/DocWach/Lego-EV3-Mindstorm-Models>
- Repository README explains directory layout, data sources, and integration intent.
- BrickLink set inventories: search the set number on <https://www.bricklink.com>.
- Brickset set page: search the set number on <https://brickset.com>.
- LDraw part library: <https://www.ldraw.org> (for verifying part numbers).
- SysML v2 reference: instructor will provide a link to a current quick-reference. You do not need to learn the full standard for this task.

# Glossary

- **Bill of Materials (BOM):** A structured list of parts and quantities that make up a product or kit.
- **CAD:** Computer-Aided Design.
- **EV3:** LEGO Mindstorms EV3, the third-generation educational robotics platform.
- **LDraw:** A community-maintained parts library and file format for LEGO computer-aided drawing.
- **PLMr:** Product Lifecycle Manager, a separate research artifact in the same portfolio that consumes this parts library.
- **SysML v2:** Systems Modeling Language version 2, the modeling language used in the `sysml/` directory.

# What PostWach will do with your report

PostWach reviews your verdict and findings, then advises Paul on whether to extend, refactor, or rebuild this artifact in the next research cycle. Strong, specific findings carry the most weight. A finding with a file path, a line number, and a measurement beats a general impression.

If you find something that does not fit any category in this brief, log it anyway. Surprise findings are sometimes the most valuable.
