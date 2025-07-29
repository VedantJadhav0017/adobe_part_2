
# v6 All cases, de-plagiarized version
import re
import json
import pymupdf4llm

def ascii_punctuate(text: str) -> str:
    """
    Replace common unicode punctuation with ASCII equivalents.
    """
    subs = {
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
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

def parse_md_outline(md: str, page_num: int):
    result = []
    for ln in md.splitlines():
        if re.fullmatch(r"^[\.\-\*,=\"']{2,}\s*$", ln.strip()):
            continue
        line = ascii_punctuate(ln.strip())
        lvl = None
        txt = None
        if line.startswith('# '):
            lvl = 'H1'
            txt = clean_bold_and_punct(line[2:].strip())
        elif line.startswith('## '):
            lvl = 'H1'
            txt = clean_bold_and_punct(line[3:].strip())
        elif line.startswith('### '):
            lvl = 'H2'
            txt = clean_bold_and_punct(line[4:].strip())
        elif line.startswith('#### '):
            lvl = 'H3'
            txt = clean_bold_and_punct(line[5:].strip())
        elif re.fullmatch(r'_?\*\*(.*?)\*\*_?', line):
            lvl = 'H3'
            txt = clean_bold_and_punct(line)
        if txt and re.match(r'^[a-z]', txt):
            continue
        if lvl and txt:
            result.append({
                'level': lvl,
                'text': txt,
                'page': page_num + 1
            })
    return result

def get_outline_and_title(md_pages):
    doc_title = 'Untitled'
    for pg in md_pages:
        for ln in pg.get('text', '').splitlines():
            line = ascii_punctuate(ln.strip())
            if line.startswith('# '):
                candidate = clean_bold_and_punct(line[2:].strip())
                if not re.match(r'^[a-z]', candidate):
                    doc_title = candidate
                    break
        if doc_title != 'Untitled':
            break
    output = {'title': doc_title, 'outline': []}
    for idx, pg in enumerate(md_pages):
        items = parse_md_outline(pg.get('text', ''), idx)
        for toc in pg.get('toc_items', []):
            if isinstance(toc, (list, tuple)) and len(toc) >= 2:
                lvl, txt = toc[0], clean_bold_and_punct(toc[1])
                if not re.match(r'^[a-z]', txt) and txt not in {e['text'] for e in items}:
                    level = f"H{lvl if 1 <= lvl <= 3 else 3}"
                    items.append({'level': level, 'text': txt, 'page': idx + 1})
        output['outline'].extend(items)
    return output

def outline_from_pdf(pdf_path):
    md = pymupdf4llm.to_markdown(pdf_path, page_chunks=True)
    return get_outline_and_title(md)

# Example usage:
# print(json.dumps(outline_from_pdf(file_path), indent=2))
