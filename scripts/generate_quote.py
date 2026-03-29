#!/usr/bin/env python3
"""
Fire Door Quote Generator - CLI Wrapper
Called by Orc-estra API endpoint to generate quotes.

Usage:
    python3 generate_quote.py <input_file> <output_file> <template_file>
    
Arguments:
    input_file: Path to uploaded survey spreadsheet (.xlsx, .xls, .csv)
    output_file: Path where quote Excel should be saved
    template_file: Path to the quote template Excel file
"""

import sys
import os
import logging
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from firedoor_processor import (
    detect_format,
    extract_type1_pdf,
    extract_type2_excel,
    populate_excel_template
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 generate_quote.py <input_file> <output_file> <template_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    template_file = sys.argv[3]
    
    # Validate inputs
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.exists(template_file):
        print(f"Error: Template file not found: {template_file}", file=sys.stderr)
        sys.exit(1)
    
    try:
        logger.info(f"Starting quote generation: {input_file} → {output_file}")
        
        # Detect format and extract door data
        filename = os.path.basename(input_file)
        format_type = detect_format(input_file, filename)
        logger.info(f"Detected format: {format_type}")
        
        doors = []
        if format_type == 'type1_pdf':
            logger.info("Extracting from Type 1 PDF...")
            doors = extract_type1_pdf(input_file)
        elif format_type == 'type2_excel':
            logger.info("Extracting from Type 2 Excel...")
            doors = extract_type2_excel(input_file)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
        
        if not doors:
            raise ValueError("No doors found in survey file")
        
        logger.info(f"Extracted {len(doors)} doors from survey")
        
        # Generate quote Excel
        logger.info("Populating template...")
        client_name = "Westpark Client"  # Default - can be extracted from filename or passed as arg
        
        populate_excel_template(
            doors=doors,
            client_name=client_name,
            template_path=template_file,
            output_path=output_file
        )
        
        logger.info(f"Quote saved successfully: {output_path}")
        print(f"SUCCESS: Quote generated with {len(doors)} doors")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Quote generation failed: {e}", exc_info=True)
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
