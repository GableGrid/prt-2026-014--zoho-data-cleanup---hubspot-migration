# PRT-2026-014 -- Zoho Data Cleanup --- HubSpot Migration
### GableGrid Portfolio Project



![Dashboard Preview](screenshots/preview.png)

## Overview
This project is a full contact database migration and data hygiene initiative involving 21,000 records from Zoho CRM and DaySmart. It includes cross-system deduplication, email validation using ZeroBounce, and data governance rules to ensure clean and consistent data.

The final output includes HubSpot and Scheduler-ready CSV files along with a 5-page Power BI dashboard built with 20+ DAX measures for reporting and analysis.


## Features

✅ 21,000 contact records generated with realistic data (Python + Faker)
✅ SQL JOIN + MAX(Appointment_Date) per contact via SQLite
✅ 7-Year Rule: LIVE (2019–2026) vs ARCHIVE (≤2018) classification
✅ Email cross-reference Zoho ↔ DaySmart — 1,193 matched
✅ Rescue Logic: 373 bounced Zoho emails updated from DaySmart
✅ Deduplication — 21,000 → 18,866 unique (DaySmart = Source of Truth)
✅ ZeroBounce simulation — 75.1% valid rate across 18,866 records
✅ Clinical Exception Rule — invalid email + active client → email nulled, name+phone kept
✅ Prospect Rule — invalid email + no DaySmart booking → 1,792 deleted
✅ Unsubscribe Rule — opt-out flag → 3,983 suppressed
✅ Top 1,000 marketing contacts scored (Opens + Clicks + Recency + Revenue + Visits)
✅ 4 import-ready CSV files with field mapping (Zoho Last_Open_Date → HubSpot custom property)
✅ Power BI 5-page dashboard with 20+ DAX measures


## Tech Stack
| Tool | Purpose |
|------|---------|
| Python + Faker | Mock data generation |
| SQLite in-memory | SQL joins & aggregation |
| Pandas | Data transformation |
| OpenPyXL | Excel report generation |
| Power BI | Dashboard & DAX |

## Output Files
| File | Records | Purpose |
|------|---------|---------|
| FileA_HubSpot_Import.csv | 13,091 | HubSpot CRM import |
| FileB_Scheduler_Contacts_LIVE.csv | 16,080 | Scheduler contacts |
| FileC_Scheduler_ApptHistory_LIVE.csv | 23,328 | Appointment history |
| FileD_Archive.csv | 4,578 | Pre-2019 archive |

## Screenshots
### Contact Overview
[![Contact Overview](screenshots/Contact%20Overview.PNG)](screenshots/Contact%20Overview.PNG)

### Revenue & Appointments
[![Revenue & Appointments](screenshots/Revenue%20%26%20Appointments.PNG)](screenshots/Revenue%20%26%20Appointments.PNG)

### Email Health & ZeroBounce
[![Email Health & ZeroBounce](screenshots/Email%20Health%20%26%20ZeroBounce.PNG)](screenshots/Email%20Health%20%26%20ZeroBounce.PNG)

### Top 1k Marketing
[![Top 1k Marketing](screenshots/Top%201k%20Marketing.PNG)](screenshots/Top%201k%20Marketing.PNG)

### Archive & Data Quality
[![Archive & Data Quality](screenshots/Archive%20%26%20Data%20Quality.PNG)](screenshots/Archive%20%26%20Data%20Quality.PNG)

## Live Demo
[Available on request](https://app.powerbi.com/links/0-fVsisZfr?ctid=ad235308-5c52-4c9e-af62-bb621c52a11b&pbi_source=linkShare&bookmarkGuid=ab2a6004-1e99-4c9c-a25f-4e8e019b3ec7)

## Built By
[Murad] — [murad@gablegrid.com]

---
🏢 **GableGrid** — Business Intelligence & 
Automation Agency  
🌐 gablegrid.com | 📧 hello@gablegrid.com  
📍 Dhaka, Bangladesh  
⭐ Top Rated on Upwork | 100% Job Success Score
```

---

**.gitignore**
```
# Credentials
*.env
*.key
credentials.json
secrets.*

# Real data — use dummy data only in portfolio
/data/real/
client_data.*

# Python
__pycache__/
*.pyc
venv/

# Node
node_modules/

# OS
.DS_Store
Thumbs.db
```

---

**Folder structure:**
```
/src/.gitkeep
/docs/.gitkeep
/data/.gitkeep          ← Dummy data only
/screenshots/. gitkeep   ← Portfolio images
/deliverables/.gitkeep
```

---

## How to Create Both — Step by Step

### Step 1 — Create Client Template Repo
```
github.com/GableGrid
→ New repository
→ Name: gablegrid-template-client-job
→ Private ✅
→ Add README ✅
→ Create repository
```

### Step 2 — Add All Files
```
Inside the repo:
→ Edit README.md → paste template above
→ Add file → .gitignore → paste content
→ Add file → src/.gitkeep → empty
→ Add file → docs/.gitkeep → empty
→ Add file → data/.gitkeep → empty
→ Add file → deliverables/.gitkeep → empty
```

### Step 3 — Mark as Template
```
Settings → scroll down
→ ✅ Template repository
→ Save
```

### Step 4 — Repeat for Portfolio Template
```
Name: gablegrid-template-portfolio
→ Public ✅
→ Same process
→ Add screenshots folder too
→ Mark as template ✅
```

---

## How to Use a Template for Every New Job
```
New repository
→ Repository template dropdown
→ Select: gablegrid-template-client-job
→ Name: prj-2025-004-powerbi-sales
→ Private
→ Create ✅

Instantly ready:
✅ README with structure
✅ .gitignore configured
✅ All 4 folders ready
✅ Zero setup time
