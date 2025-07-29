"""
Text utility functions for cleaning and normalizing text content.
"""
import re


def ascii_punctuate(text: str) -> str:
    """
    Replace common unicode punctuation with ASCII equivalents.
    """
    subs = {
        "'": "'",
        "'": "'",
        """: '"',
        """: '"',
        "–": '-',
        "—": '-',
        "…": '...'
    }
    for u, a in subs.items():
        text = text.replace(u, a)
    return text


def clean_bold_and_punct(text: str) -> str:
    """
    Remove backticks, bold markers, trailing numbers, repeated punctuation, and normalize whitespace.
    """
    text = ascii_punctuate(text)
    text = re.sub(r'`([^`]+)`', r"\1", text)
    text = text.replace('`', '')
    text = re.sub(r'_?\*\*(.*?)\*\*_?', r"\1", text)
    text = re.sub(r'(?:\b)(\d+)$', '', text)
    text = re.sub(r'[\.\-\,\"\=]{2,}', '', text)
    return ' '.join(text.split()).strip()
