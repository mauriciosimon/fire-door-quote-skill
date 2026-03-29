---
name: fire-door-quote
description: Generate fire door compliance quotes from building survey data. Processes survey PDFs/text, extracts door specifications, maps to compliance codes, and produces detailed Excel quotes with materials, labor, and pricing.
---

# Fire Door Quote Generator

Process building fire door surveys and generate detailed compliance quotes in Excel format.

## When to Use

- User uploads a fire door survey (PDF or text)
- User requests a fire door quote or compliance report
- Survey contains door schedules, floor plans, or inspection data

## Overview

This skill transforms fire door survey data into professional Excel quotes with:
- Door schedule with compliance codes
- Quote sheet with materials & labor breakdown
- Material call-off sheet
- Client summary with recommendations
- Rate card with pricing

## Workflow

1. **Receive Survey** - User uploads PDF/text or pastes survey content
2. **Extract Data** - Use Claude to extract door data (requires user's API key for BYOK)
3. **Process Quote** - Run `scripts/firedoor_processor.py` to generate Excel
4. **Return File** - Provide download link to user

## Key Components

### Business Rules
- **Complete rules**: See `references/FIRE_DOOR_RULES.md`
- **ART codes**: Survey codes (ART01-ART13) representing door issues
- **B-codes**: Material/labor codes (B01-B12) for quoting
- **Mapping**: ART codes map to B-codes (e.g., ART01 → B01)

### Processing Script
- **Location**: `scripts/firedoor_processor.py`
- **Function**: `populate_excel_template(doors, client_name, template_path, output_path)`
- **Requires**: Python 3.9+, openpyxl, anthropic SDK

### Excel Template
- **Location**: `assets/WestPark_FireDoor_CostSheet_v3_AlphaSights.xlsx`
- **Sheets**: Door Schedule, Quote Sheet, Material Call-Off, Client Summary, Rate Card

## Step-by-Step

### Step 1: Extract Door Data

Use Claude (with user's API key) to extract from survey text:

```
For each door, extract:
- door_id (e.g., "A01-L2", "B03-L3")
- level (floor number)
- fire_rating ("FD30" or "FD60")
- door_config ("S" single, "D" double, "D+S" double+side)
- frame_material (timber/steel)
- ART codes (comma-separated list of issues found)
```

Example output format:
```json
{
  "doors": [
    {
      "door_id": "A01-L2",
      "level": "L2",
      "fire_rating": "FD30",
      "door_config": "S",
      "frame_material": "timber",
      "art_codes": "ART01, ART02, ART07"
    }
  ]
}
```

### Step 2: Generate Excel Quote

```python
from scripts.firedoor_processor import populate_excel_template

# Prepare data
doors_data = [/* extracted door data */]
client_name = "Client Name"
template = "/path/to/skills/fire-door-quote/assets/WestPark_FireDoor_CostSheet_v3_AlphaSights.xlsx"
output = "/tmp/quote.xlsx"

# Generate quote
populate_excel_template(doors_data, client_name, template, output)
```

### Step 3: Return to User

Provide the generated Excel file for download.

## Important Notes

### BYOK (Bring Your Own Key)
- User must provide their own Claude API key
- Use user's key for all Claude API calls (extraction step)
- Never use a hardcoded or shared API key

### Survey Types
The processor handles two survey formats:
- **Type 1**: Simple text format with ART codes
- **Type 2**: Excel-style format with detailed specifications

Detection is automatic based on content structure.

### Default Mappings
When survey data is unclear:
- Default fire rating: FD30
- Default config: S (single)
- Default ART→B mapping: ART01→B01, ART02→B02, etc.

See `FIRE_DOOR_RULES.md` for complete mapping tables.

### Quality Checks
After generating, verify:
- ✅ All doors from survey are in Door Schedule
- ✅ B-code counts match survey ART codes
- ✅ Quote Sheet totals calculate correctly
- ✅ Material Call-Off has all required items
- ✅ Client name appears in all sheets

## Common Issues

**"Template not found"** → Check template path matches assets location
**"Missing door data"** → Verify extraction captured all required fields
**"Incorrect B-code counts"** → Check ART→B mapping in FIRE_DOOR_RULES.md
**"Excel generation fails"** → Ensure openpyxl installed (`pip install openpyxl`)

## Files Structure

```
fire-door-quote/
├── SKILL.md (this file)
├── scripts/
│   └── firedoor_processor.py (1,956 lines - Excel generation logic)
├── references/
│   └── FIRE_DOOR_RULES.md (business rules, mappings, compliance logic)
└── assets/
    └── WestPark_FireDoor_CostSheet_v3_AlphaSights.xlsx (Excel template)
```

## Quick Example

User: "I have a fire door survey for Alpha Sights office. Can you generate a quote?"

1. Ask user to upload survey PDF or paste text
2. Extract door data using Claude (user's API key)
3. Run firedoor_processor.py to generate Excel
4. Return quote file to user

Done!