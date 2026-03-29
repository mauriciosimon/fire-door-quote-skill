# Fire Door Quote Generator Skill

Generate fire door compliance quotes from building survey data for orc-estra AI agents.

## Description

This skill processes fire door survey PDFs or text, extracts door specifications, maps them to compliance codes, and produces detailed Excel quotes with materials, labor, and pricing.

## Features

- **Survey Processing**: Extract door data from PDF/text surveys
- **Compliance Mapping**: Map ART codes (survey findings) to B-codes (materials/labor)
- **Excel Quote Generation**: Professional multi-sheet Excel reports
- **Rate Card Integration**: Built-in pricing for WestPark Fire Door Services

## Contents

- `SKILL.md` - Complete skill documentation and workflow
- `scripts/firedoor_processor.py` - Core processing logic
- `scripts/generate_quote.py` - CLI entry point for testing
- `assets/WestPark_FireDoor_CostSheet_v3_AlphaSights.xlsx` - Excel template
- `references/FIRE_DOOR_RULES.md` - Business rules and code mappings
- `scripts/reference_files/BMTrada_ART_Codes_RateCard_Mapping.csv` - ART to B-code mapping

## Requirements

- Python 3.9+
- openpyxl
- anthropic SDK (for Claude API)
- User's Anthropic API key (BYOK model)

## Installation

Install this skill via the orc-estra Skills UI using this GitHub repository URL.

## Usage

1. User uploads fire door survey (PDF or text)
2. Agent reads SKILL.md for instructions
3. Agent extracts door data using Claude
4. Agent runs `firedoor_processor.py` to generate Excel quote
5. Agent provides download link to user

## Client

**WestPark Fire Door Services**
- Fire door compliance and remediation
- UK-based specialist contractor

## License

Proprietary - WestPark Fire Door Services
