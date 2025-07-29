"""
PDF processing functionality for extracting outlines and titles.
"""
import json
import pymupdf4llm
from outline_parser import get_outline_and_title


def outline_from_pdf(pdf_path):
    """
    Extract outline and title from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        dict: Dictionary containing title and outline information
    """
    md = pymupdf4llm.to_markdown(pdf_path, page_chunks=True)
    return get_outline_and_title(md)


# Example usage:
# print(json.dumps(outline_from_pdf(file_path), indent=2))
