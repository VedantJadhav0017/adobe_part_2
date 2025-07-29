#!/usr/bin/env python3
"""
PDF Outline Extractor - Main Entry Point

A modular tool for extracting structured outlines and titles from PDF documents.
"""

import json
import argparse
import sys
from pathlib import Path
from pdf_processor import outline_from_pdf
from text_utils import ascii_punctuate, clean_bold_and_punct
from outline_parser import parse_md_outline, get_outline_and_title


def main():
    """Main entry point for the PDF outline extractor."""
    parser = argparse.ArgumentParser(
        description="Extract structured outlines and titles from PDF documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py document.pdf                    # Print outline to stdout
  python main.py document.pdf --pretty          # Pretty print with indentation
  python main.py document.pdf -o outline.json   # Save to file
        """
    )
    parser.add_argument(
        "pdf_path", 
        help="Path to the PDF file to process"
    )
    parser.add_argument(
        "-o", "--output", 
        help="Output JSON file path (optional, prints to stdout if not specified)"
    )
    parser.add_argument(
        "--pretty", 
        action="store_true", 
        help="Pretty print JSON output with indentation"
    )
    
    args = parser.parse_args()
    
    # Check if PDF file exists
    if not Path(args.pdf_path).exists():
        print(f"Error: PDF file '{args.pdf_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Extract outline from PDF
        result = outline_from_pdf(args.pdf_path)
        
        # Format JSON output
        indent = 2 if args.pretty else None
        json_output = json.dumps(result, indent=indent)
        
        # Write to file or stdout
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Outline extracted and saved to: {args.output}")
        else:
            print(json_output)
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()


# Legacy usage for backward compatibility:
# from main import outline_from_pdf
# result = outline_from_pdf("path/to/document.pdf")
# print(json.dumps(result, indent=2))
