**PDF Outline Extractor**

A lightweight, modular tool for extracting structured outlines (titles, headings, subheadings) from PDF documents and performing semantic search on their content.

---

## Repository

```bash
# Clone the repository
git clone https://github.com/VedantJadhav0017/adobe_part_2.git
```

---

## Features

* **Outline Extraction**
  Parse PDF files to generate a hierarchical outline (H1/H2/H3) and document title.

* **Semantic Search**
  Search across PDF content using advanced text embeddings and similarity search.

* **Modular Design**
  Separate utilities for text cleaning, outline parsing, and PDF processing for easy maintenance.

---

## Getting Started

### Prerequisites

* Python 3.8+
* [docker](https://www.docker.com/) (optional, for containerized usage)

### Installation

```bash
pip install -r requirements.txt
```

---

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Extract outline from a PDF:**
   ```bash
   python main.py "your_document.pdf" --pretty
   ```

3. **Save outline to file:**
   ```bash
   python main.py "your_document.pdf" -o "outline.json" --pretty
   ```

---

## Usage

### 1. Extract Outline

#### Command Line Usage (Recommended)

```bash
# Extract outline and print to stdout
python main.py "path/to/document.pdf"

# Extract outline with pretty formatting
python main.py "path/to/document.pdf" --pretty

# Save outline to JSON file
python main.py "path/to/document.pdf" -o "output/outline.json" --pretty
```

#### Programmatic Usage

```python
from pdf_processor import outline_from_pdf
import json

result = outline_from_pdf("path/to/document.pdf")
print(json.dumps(result, indent=2))
```

### 2. Semantic Search

```bash
python src/semantic_search.py \
  "challenge_pdfs/Collection 1/challenge1b_input.json" \
  "challenge_outputs_json/1stchallenge1b_output.json"
```

---

## Docker Usage

> **Note:** Docker commands are unchanged.

```bash
docker build -t pdf-outline-extractor .
```

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-outline-extractor
```

---

## Project Structure

```
├── src/
│   ├── semantic_search.py       # Semantic search logic
│   └── chroma/                  # ChromaDB storage
├── main.py                      # Main CLI entry point for PDF outline extraction
├── text_utils.py                # Text cleaning utilities
├── outline_parser.py            # Markdown outline parsing
├── pdf_processor.py             # PDF-to-outline functionality
├── pdf_outline_extractor_legacy.py  # Legacy monolithic version (for reference)
├── requirements.txt             # Python dependencies
└── Dockerfile                   # Container setup
```

### Module Descriptions

- **`main.py`** - Command-line interface and main entry point for PDF outline extraction
- **`text_utils.py`** - Text processing utilities for cleaning and normalizing content
- **`outline_parser.py`** - Markdown parsing and hierarchical outline generation
- **`pdf_processor.py`** - Core PDF processing functionality
- **`pdf_outline_extractor_legacy.py`** - Original monolithic implementation (kept for reference)

---

## Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add YourFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.
