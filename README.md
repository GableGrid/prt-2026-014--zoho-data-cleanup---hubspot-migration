# PRT-2026-014 — Zoho CRM ↔ DaySmart Migration
### GableGrid Portfolio Project



![Dashboard Preview](screenshots/Contact_Overview.PNG)

## Overview
[What business problem this solves — 2-3 sentences]

## Features
- ✅ [Feature 1]
- ✅ [Feature 2]
- ✅ [Feature 3]
- ✅ [Feature 4]

## Tech Stack
| Tool | Purpose |
|------|---------|
| [Tool 1] | [What it does] |
| [Tool 2] | [What it does] |

## Setup & Run
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Screenshots
![Contact Overview](screenshots/Contact_Overview.PNG)
![Revenue & Appointments](screenshots/Revenue_%26_Appointments.PNG)
![Email Health & ZeroBounce](screenshots/Email_Health_%26_ZeroBounce.PNG)
![Top 1K Marketing](screenshots/Top_1k_Marketing.PNG)
![Archive & Data Quality](screenshots/Archive_%26_Data_Quality.PNG)

## Live Demo
[Link if available — or "Available on request"]

## Built By
[Developer Name] — [email@gablegrid.com]

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
/screenshots/.gitkeep   ← Portfolio images
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

## How to Use Template for Every New Job
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