# Data Management Skill

## Overview

The Data Management skill provides comprehensive workflows for managing research data throughout its lifecycle—from collection through archiving. This skill ensures data is well-organized, documented, secure, and compliant with funder requirements and FAIR principles (Findable, Accessible, Interoperable, Reusable).

## Capabilities

- Data organization and structure
- Documentation and metadata
- Storage and backup
- Security and access control
- Data sharing and publication
- Long-term preservation
- Compliance and governance

---

## Phase 1: Data Management Planning

### Data Management Plan Framework

```
DATA MANAGEMENT PLAN (DMP)

DMP COMPONENTS
─────────────────────────────────────────
1. DATA DESCRIPTION
   - What data will be collected/generated?
   - What formats and standards?
   - Expected volume?
   - Relationship to existing data?

2. DOCUMENTATION AND METADATA
   - What documentation will be created?
   - What metadata standards used?
   - How will data be described?

3. STORAGE AND BACKUP
   - Where will data be stored?
   - What backup procedures?
   - How is access controlled?

4. SECURITY AND PRIVACY
   - What are security measures?
   - How is sensitive data protected?
   - What compliance is required?

5. DATA SHARING
   - Will data be shared? When? How?
   - What repository?
   - What access conditions?
   - Any restrictions?

6. PRESERVATION
   - What data will be preserved long-term?
   - Where will it be archived?
   - For how long?

7. RESPONSIBILITIES
   - Who is responsible for each aspect?
   - What resources are needed?

DMP TEMPLATE
─────────────────────────────────────────
Project Title: ____________________
PI: ____________________
Date: ____________________

1. DATA DESCRIPTION

1.1 Types of data
[List all data types that will be collected or generated]
- Type 1: [Description]
- Type 2: [Description]

1.2 Data formats
| Data Type | Format | Standard | Volume Est. |
|-----------|--------|----------|-------------|
| Type 1    | .csv   | ISO 8601 | ~1GB        |
| Type 2    | .json  | Custom   | ~500MB      |

1.3 Existing data
[Describe any existing data that will be used]

2. DOCUMENTATION AND METADATA

2.1 Documentation
[What documentation will be created]
- README files for each dataset
- Codebook for variables
- Protocol documents
- Analysis scripts

2.2 Metadata standards
[What metadata standards will be used]
- Standard: [name, e.g., Dublin Core, DDI]
- Fields: [list key fields]

3. STORAGE AND BACKUP

3.1 Storage location(s)
| Data Type | Primary Storage | Backup |
|-----------|-----------------|--------|
| Active data | [location] | [location] |
| Archived data | [location] | [location] |

3.2 Backup schedule
- Full backup: [frequency]
- Incremental: [frequency]
- Verification: [frequency]

4. SECURITY AND ACCESS

4.1 Security measures
- Encryption: [Yes/No, type]
- Access control: [description]
- Physical security: [description]

4.2 Sensitive data handling
[Describe protections for any sensitive data]

5. DATA SHARING

5.1 Sharing plan
- What: [data to be shared]
- When: [timeline]
- Where: [repository]
- How: [access mechanism]

5.2 Access conditions
- License: [type]
- Restrictions: [any limitations]
- Embargo: [if applicable]

6. PRESERVATION

6.1 Long-term preservation
- What: [data to be preserved]
- Where: [archive]
- Duration: [timeframe]
- Format: [preservation formats]

7. ROLES AND RESPONSIBILITIES

| Task | Responsible | Resources |
|------|-------------|-----------|
| Data collection | [name] | [resources] |
| Documentation | [name] | [resources] |
| Storage management | [name] | [resources] |
| Sharing | [name] | [resources] |
```

### FAIR Principles Implementation

```
FAIR DATA PRINCIPLES

FINDABLE
─────────────────────────────────────────
F1: Globally unique persistent identifier
□ Assign DOI to datasets
□ Use persistent URLs
□ Register in data registries

F2: Rich metadata
□ Comprehensive descriptive metadata
□ Machine-readable format
□ Indexed and searchable

F3: Metadata includes identifier
□ Dataset ID in metadata record
□ Clear link between metadata and data

F4: Registered in searchable resource
□ Listed in relevant repositories
□ Indexed by search engines
□ Discoverable by others

Implementation checklist:
□ DOI assigned? ____
□ Metadata complete? ____
□ Repository selected? ____
□ Searchable/indexed? ____

ACCESSIBLE
─────────────────────────────────────────
A1: Retrievable by identifier
□ Standard protocol (HTTP, FTP)
□ Open, free protocol
□ Authentication if needed

A1.1: Protocol is open and free
□ No proprietary tools required
□ Freely implementable

A1.2: Authentication when needed
□ Clear access procedure
□ Authentication mechanism documented

A2: Metadata accessible even if data isn't
□ Metadata persists after data removed
□ Landing page maintained

Implementation checklist:
□ Access method documented? ____
□ Authentication clear? ____
□ Metadata persistent? ____

INTEROPERABLE
─────────────────────────────────────────
I1: Formal, shared, applicable language
□ Standard file formats
□ Community-accepted standards
□ Open formats preferred

I2: FAIR vocabularies
□ Standard vocabularies/ontologies
□ Controlled terms where applicable
□ Linked to definitions

I3: Qualified references
□ Links to related data
□ References to methods/software
□ Provenance information

Implementation checklist:
□ Standard formats used? ____
□ Vocabularies identified? ____
□ References included? ____

REUSABLE
─────────────────────────────────────────
R1: Richly described with attributes
□ Provenance documented
□ Collection methods described
□ Processing documented

R1.1: Clear usage license
□ License specified
□ License is standard (CC-BY, etc.)
□ Permissions clear

R1.2: Detailed provenance
□ How data was created
□ What processing applied
□ Who created it

R1.3: Community standards
□ Disciplinary norms followed
□ Best practices applied
□ Quality standards met

Implementation checklist:
□ Provenance documented? ____
□ License assigned? ____
□ Standards followed? ____

FAIR ASSESSMENT SCORECARD
─────────────────────────────────────────
| Principle | Score (1-5) | Notes |
|-----------|-------------|-------|
| Findable  |             |       |
| Accessible|             |       |
| Interoperable |         |       |
| Reusable  |             |       |
| **Overall** |           |       |
```

---

## Phase 2: Data Organization

### File and Folder Structure

```
DATA ORGANIZATION FRAMEWORK

FOLDER STRUCTURE TEMPLATE
─────────────────────────────────────────
project-name/
├── README.md                 # Project overview
├── LICENSE                   # Data license
├── data/
│   ├── raw/                 # Original, unmodified data
│   │   ├── README.md        # Description of raw data
│   │   └── [raw data files]
│   ├── processed/           # Cleaned, transformed data
│   │   ├── README.md        # Processing documentation
│   │   └── [processed files]
│   └── external/            # Data from external sources
│       └── README.md        # Source attribution
├── docs/
│   ├── codebook.md          # Variable descriptions
│   ├── protocol.md          # Data collection protocol
│   └── data_dictionary.xlsx # Detailed variable info
├── scripts/
│   ├── 01_import.R          # Data import scripts
│   ├── 02_clean.R           # Data cleaning scripts
│   └── 03_analyze.R         # Analysis scripts
├── outputs/
│   ├── figures/             # Generated figures
│   ├── tables/              # Generated tables
│   └── reports/             # Generated reports
└── archive/                 # Archived/superseded versions

FILE NAMING CONVENTIONS
─────────────────────────────────────────
Good naming practices:
□ Descriptive but concise
□ No spaces (use underscores or hyphens)
□ No special characters
□ Consistent format
□ Include date if relevant (YYYY-MM-DD)
□ Include version if relevant (v01, v02)

Naming pattern:
[project]_[content]_[date]_[version].[ext]

Examples:
✓ survey_responses_2024-01-15_v01.csv
✓ interview_participant-03_clean.txt
✓ analysis_regression-models_final.R

✗ data (2).xlsx
✗ final FINAL v3 (1).docx
✗ John's analysis.R

VERSION CONTROL
─────────────────────────────────────────
For code and documentation:
- Use Git for version control
- Meaningful commit messages
- Branch for experiments
- Tag releases

For data files:
- Include version in filename
- Maintain changelog
- Archive previous versions
- Document what changed

Version log template:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v01 | 2024-01-01 | JD | Initial version |
| v02 | 2024-01-15 | JD | Fixed coding errors |
| v03 | 2024-02-01 | AB | Added new variables |
```

### Data Documentation

```
DOCUMENTATION STANDARDS

README FILE TEMPLATE
─────────────────────────────────────────
# [Dataset Name]

## Overview
[Brief description of the dataset]

## Contents
[List of files with descriptions]

## Data Collection
- **When**: [Date range]
- **Where**: [Location/context]
- **How**: [Method]
- **Who**: [Collector]

## Variables
[Brief description of key variables;
see codebook for details]

## Usage
[How to use this data]

## Citation
[How to cite this dataset]

## License
[License information]

## Contact
[Contact for questions]

## Changelog
[Version history]

CODEBOOK TEMPLATE
─────────────────────────────────────────
# Codebook: [Dataset Name]

## Dataset Description
- **File**: [filename]
- **Format**: [format]
- **Observations**: [N]
- **Variables**: [number]
- **Date range**: [dates]

## Variable Descriptions

### [Variable Name 1]
- **Label**: [Human-readable label]
- **Type**: [numeric/character/date/factor]
- **Description**: [What this measures]
- **Values**: [Range or categories]
- **Missing**: [How missing coded]
- **Notes**: [Any additional info]

### [Variable Name 2]
[Same structure]

## Coding Schemes

### [Categorical Variable]
| Code | Label | Description |
|------|-------|-------------|
| 1 | Category A | [description] |
| 2 | Category B | [description] |
| 99 | Missing | Not collected |

## Derived Variables
[Variables created from raw data]

### [Derived Variable]
- **Source**: [Original variables]
- **Calculation**: [How derived]

DATA DICTIONARY FORMAT
─────────────────────────────────────────
Spreadsheet format:

| Variable | Label | Type | Values | Missing | Source | Notes |
|----------|-------|------|--------|---------|--------|-------|
| id | Participant ID | char | unique | N/A | assigned | |
| age | Age in years | num | 18-99 | -99 | survey Q1 | |
| gender | Gender | factor | 1=M,2=F,3=NB | -99 | survey Q2 | |
```

---

## Phase 3: Storage and Security

### Storage Strategy

```
DATA STORAGE FRAMEWORK

STORAGE TIERS
─────────────────────────────────────────
Tier 1: Active working data
- Location: Local + cloud sync
- Access: Frequent
- Backup: Daily
- Examples: Current analysis files

Tier 2: Project data (less active)
- Location: Network/cloud storage
- Access: Periodic
- Backup: Weekly
- Examples: Completed datasets

Tier 3: Archived data
- Location: Long-term archive
- Access: Rare
- Backup: Archival (replicated)
- Examples: Published datasets

STORAGE OPTIONS
─────────────────────────────────────────
Local storage:
□ Workstation hard drive
□ Lab server
□ Portable drives (encrypted!)

Network storage:
□ Institutional file server
□ Research computing storage
□ Department NAS

Cloud storage:
□ Institutional cloud (Box, OneDrive, Google)
□ Research-specific (OSF, AWS)
□ Commercial (Dropbox) - check compliance!

Long-term archive:
□ Institutional repository
□ Domain repository
□ General repository (Zenodo, Figshare)

STORAGE DECISION MATRIX
─────────────────────────────────────────
| Factor | Consider |
|--------|----------|
| Sensitivity | Can data go to cloud? |
| Size | Does it fit? Cost? |
| Access needs | Who needs access? |
| Compliance | Funder/IRB requirements? |
| Collaboration | Multi-institution needs? |
| Budget | What's affordable? |

BACKUP STRATEGY
─────────────────────────────────────────
3-2-1 Rule:
- 3 copies of data
- 2 different storage types
- 1 offsite location

Backup schedule:
| Data Type | Frequency | Method | Location |
|-----------|-----------|--------|----------|
| Active work | Daily | Automatic | Cloud |
| Project data | Weekly | Scheduled | Server |
| Critical data | Real-time | Sync | Multiple |

Backup verification:
□ Test restores monthly
□ Check backup logs weekly
□ Verify integrity periodically
```

### Data Security

```
DATA SECURITY FRAMEWORK

SECURITY LEVELS
─────────────────────────────────────────
Level 1: Public
- No restrictions
- Openly available
- Standard protections only

Level 2: Internal
- Institutional access only
- Standard access controls
- Normal security measures

Level 3: Confidential
- Restricted access
- Enhanced security
- Access logging

Level 4: Highly Sensitive
- Strict access control
- Encryption required
- Regulatory compliance
- Special handling

SECURITY MEASURES BY LEVEL
─────────────────────────────────────────
| Measure | L1 | L2 | L3 | L4 |
|---------|----|----|----|----|
| Password protection | ✓ | ✓ | ✓ | ✓ |
| Encryption at rest | | | ✓ | ✓ |
| Encryption in transit | | ✓ | ✓ | ✓ |
| Access control | | ✓ | ✓ | ✓ |
| Access logging | | | ✓ | ✓ |
| Multi-factor auth | | | | ✓ |
| Data use agreement | | | ✓ | ✓ |
| Audit trail | | | ✓ | ✓ |

ENCRYPTION GUIDELINES
─────────────────────────────────────────
At rest:
□ Full disk encryption on devices
□ Encrypted containers for sensitive files
□ Encrypted backups

In transit:
□ HTTPS for web transfers
□ SFTP (not FTP) for file transfers
□ VPN for remote access
□ Encrypted email for sensitive data

Tools:
- VeraCrypt (encrypted containers)
- BitLocker/FileVault (full disk)
- 7-Zip (encrypted archives)

SENSITIVE DATA HANDLING
─────────────────────────────────────────
Personally Identifiable Information (PII):
- Names, addresses, SSN, etc.
- De-identify when possible
- Limit access to identified data
- Secure storage required

Protected Health Information (PHI):
- HIPAA compliance required
- Business Associate Agreements
- Minimum necessary principle
- Audit requirements

Human subjects data:
- IRB protocol compliance
- Consent requirements
- Access limitations
- Retention requirements

ACCESS CONTROL
─────────────────────────────────────────
Principles:
- Least privilege (minimum access needed)
- Role-based access
- Regular access review
- Promptly revoke when no longer needed

Access documentation:
| Person | Role | Data Access | Granted | Review |
|--------|------|-------------|---------|--------|
| Name | PI | All | Date | Date |
| Name | RA | Level 2 | Date | Date |

Access request process:
1. Request submitted
2. Need justified
3. PI approval
4. Access granted
5. Training completed
6. Documented
```

---

## Phase 4: Data Sharing

### Data Sharing Planning

```
DATA SHARING FRAMEWORK

SHARING DECISION TREE
─────────────────────────────────────────
Can data be shared?
│
├── Legal constraints?
│   ├── Yes → Can constraints be addressed?
│   │         ├── Yes → Proceed with modifications
│   │         └── No → Cannot share (document why)
│   └── No → Continue
│
├── Ethical constraints?
│   ├── Yes → Can consent be obtained?
│   │         ├── Yes → Proceed
│   │         └── No → Share de-identified only
│   └── No → Continue
│
├── Proprietary/IP concerns?
│   ├── Yes → Negotiate sharing terms
│   └── No → Continue
│
└── Share openly or with restrictions?
    ├── Open → Select open repository
    └── Restricted → Define access conditions

WHAT TO SHARE
─────────────────────────────────────────
Prioritize sharing:
□ Data underlying published findings
□ Data required for replication
□ Data with broad reuse potential
□ Unique/hard-to-collect data

May not share:
□ Data with legal restrictions
□ Identifiable human subjects data (without consent)
□ Proprietary/licensed data
□ Preliminary/low-quality data

PREPARING DATA FOR SHARING
─────────────────────────────────────────
Cleaning checklist:
□ Remove identifying information
□ Check for embedded metadata
□ Remove file paths revealing structure
□ Clean variable names
□ Standardize formats
□ Remove incomplete/test records

Documentation checklist:
□ README file complete
□ Codebook/data dictionary
□ Collection methodology
□ Any limitations documented
□ Citation information
□ License specified

Quality check:
□ Data loads correctly
□ Documentation matches data
□ Third party can understand
□ Variables as described
```

### Repository Selection

```
DATA REPOSITORY SELECTION

REPOSITORY TYPES
─────────────────────────────────────────
Institutional repositories:
- University data repository
- Library data services
- Local archive

Domain repositories:
- Field-specific archives
- Community standards
- Specialized metadata

General repositories:
- Zenodo (CERN)
- Figshare
- Dryad
- OSF
- Dataverse

Government repositories:
- data.gov
- NIH data repositories
- Agency-specific archives

SELECTION CRITERIA
─────────────────────────────────────────
| Criterion | Questions |
|-----------|-----------|
| Persistence | DOIs? Long-term commitment? |
| Discoverability | Indexed? Searchable? |
| Access | Open? Controlled? Embargoed? |
| Formats | Accepted formats? |
| Size | Size limits? Costs? |
| Metadata | Standards supported? |
| Community | Used in your field? |
| Funder | Meets requirements? |

REPOSITORY COMPARISON
─────────────────────────────────────────
| Repository | DOI | Size Limit | Cost | Access |
|------------|-----|------------|------|--------|
| Zenodo | Yes | 50GB | Free | Open/Restricted |
| Figshare | Yes | 20GB free | Varies | Open/Restricted |
| Dryad | Yes | Varies | $$ | Open |
| OSF | Yes | 5GB private | Free | Open/Restricted |
| Dataverse | Yes | Varies | Free | Open/Restricted |

DATA DEPOSIT CHECKLIST
─────────────────────────────────────────
Before deposit:
□ Data cleaned and de-identified
□ Documentation complete
□ Metadata prepared
□ License selected
□ Co-author/stakeholder approval

During deposit:
□ Files uploaded
□ Metadata entered
□ Access settings configured
□ Embargo set (if applicable)
□ Preview/review

After deposit:
□ DOI reserved/minted
□ Test download
□ Add to publications
□ Update data management records
```

### Data Licensing

```
DATA LICENSE SELECTION

LICENSE OPTIONS
─────────────────────────────────────────
Creative Commons licenses:

CC0 (Public Domain)
- No restrictions
- Maximum reuse
- No attribution required
- Recommended for data

CC BY (Attribution)
- Attribution required
- Otherwise unrestricted
- Common for data

CC BY-SA (Attribution-ShareAlike)
- Attribution required
- Derivatives must use same license
- "Copyleft" approach

CC BY-NC (Attribution-NonCommercial)
- Attribution required
- No commercial use
- May limit reuse

CC BY-ND (Attribution-NoDerivatives)
- Attribution required
- No modifications allowed
- Very restrictive

Other options:
- Open Data Commons licenses (ODC)
- Custom data use agreements
- Institutional licenses

LICENSE SELECTION GUIDE
─────────────────────────────────────────
For maximum reuse:
→ CC0 or CC BY

For attribution:
→ CC BY

For academic use only:
→ CC BY-NC (but consider implications)

For sensitive data:
→ Data Use Agreement (DUA)

Funder requirements:
- Many funders prefer open licenses
- Check specific requirements
- NIH: Generally expects sharing
- NSF: Expects reasonable access

LICENSE STATEMENT TEMPLATE
─────────────────────────────────────────
"This dataset is made available under the
[License Name] license. When using this data,
please cite:

[Full citation]

DOI: [DOI]"
```

---

## Phase 5: Long-Term Preservation

### Preservation Planning

```
PRESERVATION FRAMEWORK

WHAT TO PRESERVE
─────────────────────────────────────────
Priority 1: Essential
- Data underlying publications
- Unique/irreplaceable data
- Data with regulatory requirements
- Data with ongoing value

Priority 2: Important
- Complete datasets (not just published subset)
- Analysis code and scripts
- Documentation and protocols

Priority 3: Consider
- Intermediate/processed versions
- Working files
- Supplementary materials

Do not preserve:
- Duplicate copies
- Temporary files
- Superseded versions (unless historically significant)

PRESERVATION FORMATS
─────────────────────────────────────────
Preferred formats (open, non-proprietary):

Text data:
- CSV, TSV (tabular)
- TXT, XML, JSON (structured)
- PDF/A (documents)

Numeric data:
- CSV with data dictionary
- ASCII text

Images:
- TIFF (uncompressed)
- PNG (lossless)
- JPEG2000

Audio:
- WAV, FLAC (lossless)

Video:
- Motion JPEG 2000
- Uncompressed AVI

Avoid:
- Proprietary formats (.xlsx, .sav, .dta)
- Or convert to open + keep original

FORMAT MIGRATION PLAN
─────────────────────────────────────────
Over time, formats become obsolete.

Migration strategy:
1. Monitor format obsolescence
2. Plan migration before obsolete
3. Migrate to current standards
4. Verify integrity after migration
5. Document migration

Integrity verification:
□ Checksum before migration
□ Checksum after migration
□ Compare checksums
□ Spot-check content
□ Document verification

RETENTION SCHEDULE
─────────────────────────────────────────
| Data Type | Minimum Retention | Rationale |
|-----------|-------------------|-----------|
| Published data | 10+ years | Reproducibility |
| Grant-funded | Per funder (often 3-7 years) | Compliance |
| Human subjects | Per IRB/consent | Ethical |
| Student work | Per institution | Policy |

After retention period:
□ Review for continued value
□ Archive or destroy
□ Document disposition
```

### Archive and Disposal

```
ARCHIVAL PROCESS

ARCHIVE PREPARATION
─────────────────────────────────────────
Before archiving:

Review and select:
□ What should be archived?
□ What can be deleted?
□ Are duplicates removed?
□ Is documentation complete?

Prepare files:
□ Convert to preservation formats
□ Organize logically
□ Generate checksums
□ Create manifest

Create package:
□ Data files
□ Documentation (README, codebook)
□ Metadata record
□ Checksum file
□ License information

ARCHIVE CHECKLIST
─────────────────────────────────────────
□ Files in preservation formats
□ Documentation complete
□ Metadata standards applied
□ Checksums generated
□ Access permissions set
□ Retention period specified
□ Contact information current
□ Citation information complete

SECURE DISPOSAL
─────────────────────────────────────────
When data should be destroyed:

Triggers:
- Retention period expired
- Consent withdrawn
- Legal requirement
- No longer needed

Disposal methods:
| Sensitivity | Method |
|-------------|--------|
| Low | Delete files |
| Medium | Secure delete (overwrite) |
| High | Certified destruction |
| Highest | Physical destruction |

Documentation:
□ What was destroyed
□ When
□ By whom
□ Method used
□ Approval obtained

Destruction record template:
| Dataset | Date | Method | Approved By | Destroyed By |
|---------|------|--------|-------------|--------------|
| [name] | [date] | [method] | [name] | [name] |
```

---

## Integration Patterns

### With Research Agents

- **research-architect**: Integrates data management into study design
- **collaboration-coordinator**: Coordinates multi-site data management
- **methodology-advisor**: Ensures data collection supports analysis

### With Other Skills

- **reproducibility**: Coordinates data sharing with code sharing
- **grant-writing**: Develops data management plans for proposals
- **research-roadmapping**: Integrates data milestones into timeline

---

## Output Artifacts

1. **Data Management Plan**: Comprehensive DMP document
2. **Folder Structure**: Organized project directory
3. **Documentation**: README, codebook, data dictionary
4. **Security Assessment**: Data classification and protections
5. **Sharing Plan**: Repository and access approach
6. **Preservation Package**: Archive-ready data package

---

## Quality Criteria

Data management is successful when:

1. **Organized**: Data is structured logically
2. **Documented**: Others can understand the data
3. **Secure**: Appropriate protections in place
4. **Compliant**: Meets funder and regulatory requirements
5. **FAIR**: Findable, Accessible, Interoperable, Reusable
6. **Sustainable**: Data preserved for appropriate duration

---

## Warnings

- Start data management at project start, not end
- Don't underestimate documentation time
- Test backups regularly
- Be careful with sensitive data
- Check funder and institutional requirements
- Plan for personnel changes
- Consider long-term accessibility of formats

---

## Learn More

- DMPTool: dmptool.org
- FAIR Principles: go-fair.org
- DataONE Best Practices: dataoneorg.github.io/Education
- UK Data Service: ukdataservice.ac.uk
- ICPSR Guide: icpsr.umich.edu/web/pages/deposit
