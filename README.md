
# AntonPDF-1B: PDF Semantic Search & Query Response

AntonPDF-1B is a tool for performing smart semantic search and automated query response on PDF documents. It extracts structured information and answers from PDF files using advanced text processing and search techniques.

## Features
- Extracts outlines and titles from PDFs
- Performs semantic search on document content
- Outputs results in structured JSON format

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/VedantJadhav0017/adobe_part_2.git
cd adobe_part_2
```

### Install Requirements

```bash
pip install -r requirements.txt
```

## Usage

Run semantic search on a challenge input and save the output as JSON:

```bash
python src/semantic_search.py "challenge_pdfs/Collection 1/challenge1b_input.json" "challenge_outputs_json/1stchallenge1b_output_test.json"
python src/semantic_search.py "challenge_pdfs/Collection 2/challenge1b_input.json" "challenge_outputs_json/2ndchallenge1b_output_test.json"
python src/semantic_search.py "challenge_pdfs/Collection 3/challenge1b_input.json" "challenge_outputs_json/3rdchallenge1b_output_test.json"
```

## Project Structure

- `src/` - Source code for semantic search and PDF processing
- `challenge_pdfs/` - Input PDF collections and JSONs
- `challenge_outputs_json/` - Output JSONs for each challenge
- `requirements.txt` - Python dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.


