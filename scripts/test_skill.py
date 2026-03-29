#!/usr/bin/env python3
"""
Quick test of fire-door-quote skill
Tests Excel generation with sample door data
"""

import sys
from pathlib import Path

# Add parent dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from firedoor_processor import populate_excel_template

# Sample door data (from Alpha Sights survey)
sample_doors = [
    {
        "door_id": "A01-L2",
        "level": "L2",
        "fire_rating": "FD30",
        "door_config": "S",
        "frame_material": "timber",
        "art_codes": "ART01, ART02, ART07"
    },
    {
        "door_id": "A03-L2",
        "level": "L2",
        "fire_rating": "FD30",
        "door_config": "S",
        "frame_material": "timber",
        "art_codes": "ART01, ART10"
    },
    {
        "door_id": "B01-L3",
        "level": "L3",
        "fire_rating": "FD60",
        "door_config": "D",
        "frame_material": "steel",
        "art_codes": "ART01, ART05, ART09"
    }
]

# Paths
skill_dir = Path(__file__).parent.parent
template_path = skill_dir / "assets" / "WestPark_FireDoor_CostSheet_v3_AlphaSights.xlsx"
output_path = "/tmp/fire_door_test_quote.xlsx"

print("🧪 Testing Fire Door Quote Skill...")
print(f"📂 Template: {template_path}")
print(f"📂 Output: {output_path}")
print(f"🚪 Doors: {len(sample_doors)}")

try:
    # Generate quote
    populate_excel_template(
        doors=sample_doors,
        client_name="Skill Test Client",
        template_path=str(template_path),
        output_path=str(output_path)
    )
    
    print("✅ Quote generated successfully!")
    print(f"📊 File size: {Path(output_path).stat().st_size / 1024:.1f} KB")
    print(f"📎 Output: {output_path}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
