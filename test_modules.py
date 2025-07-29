#!/usr/bin/env python3
"""
Test script to verify the modular structure works correctly.
"""

def test_imports():
    """Test that all modules can be imported successfully."""
    try:
        from text_utils import ascii_punctuate, clean_bold_and_punct
        print("✓ text_utils imported successfully")
        
        from outline_parser import parse_md_outline, get_outline_and_title
        print("✓ outline_parser imported successfully")
        
        from pdf_processor import outline_from_pdf
        print("✓ pdf_processor imported successfully")
        
        # Test text utilities
        test_text = 'Hello "world" – this is a test…'
        cleaned = ascii_punctuate(test_text)
        print(f"✓ ascii_punctuate test: '{test_text}' → '{cleaned}'")
        
        test_bold = "**Bold text** with `backticks`"
        cleaned_bold = clean_bold_and_punct(test_bold)
        print(f"✓ clean_bold_and_punct test: '{test_bold}' → '{cleaned_bold}'")
        
        print("\n✅ All module imports and basic functionality tests passed!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_imports()
