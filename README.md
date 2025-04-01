# MetaBeeAI PDF to Text

A pipeline for processing PDF documents with AI-powered text extraction. This tool splits PDFs into manageable overlapping segments and uses Vision Agentic Document Analysis to extract structured text and image descriptions.

## Features
- Split large PDFs into overlapping 2-page segments
- Extract text and image content with Vision Agentic Document Analysis
- Organize extraction results with unique chunk IDs
- Verify chunk ID uniqueness across document segments

## Installation
### Prerequisites
Python 3.7+
pip

### Setup
Clone the repository:
```
bash
git clone https://github.com/yourusername/metabeeai-pdf.git
cd metabeeai-pdf
```
### Install dependencies:
```
bash
pip install -r requirements.txt
```

### Create a .env file with your API keys:
```
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
LANDINGAI_API_KEY=your_landingai_api_key
```

### Install the package:
```
pip install .
```

## Directory Structure
The pipeline expects PDFs to be organized in a specific structure:
```
data/papers/
├── 001/
│   ├── 001_main.pdf
├── 002/
│   ├── 002_main.pdf
└── ...
```
After processing, it will generate:
```
data/papers/
├── 001/
│   ├── 001_main.pdf
│   └── pages/
│       ├── main_p01-02.pdf
│       ├── main_p01-02.pdf.json
│       ├── main_p02-03.pdf
│       ├── main_p02-03.pdf.json
│       └── ...
├── 002/
...
```

## Usage
### 1. Split PDFs into overlapping segments
```
python -m metabeeai-pdf.split_pdf data/papers
```

This script:
- Looks for subfolders in the specified directory
- For each subfolder, finds a PDF named {subfolder}_main.pdf
- Creates a "pages" subdirectory
- Splits the PDF into overlapping 2-page PDFs (main_p01-02.pdf, main_p02-03.pdf, etc.)

### 2. Process PDFs with Vision Agentic Document Analysis

# Process all papers
```
python -m metabeeai_pdf.va_process_papers
```
# Specify a different directory
```
python -m metabeeai_pdf.va_process_papers --dir path/to/papers
```
# Start from a specific folder
```
python -m metabeeai_pdf.va_process_papers --start 059
```

This script:

- Processes PDF files in each paper's "pages" subdirectory
- Uses the Landing AI Vision Agentic Document Analysis API
- Saves results as JSON files alongside the PDFs
- Creates a timestamped log file in the papers directory

### 3. Verify Chunk ID Uniqueness
Check all papers
```
python -m metabeeai_pdf.unique_chunk_id
```

Specify a different directory
```
python -m metabeeai_pdf.unique_chunk_id --dir path/to/papers
```

This script:
- Checks if each chunk_id in JSON files is unique
- Reports any duplicates found
- Saves results to a JSON log file

## API Keys
The pipeline requires three API keys:
LANDING_AI_API_KEY: For Vision Agentic Document Analysis
OPENAI_API_KEY: For additional AI-powered processing
ANTHROPIC_API_KEY: For additional AI-powered processing

## License
This project is licensed under the MIT License. 

## Contributors
This project is developed by MetaBeeAI

## Contact
For questions or support, please contact us at rachel.parkinson@biology.ox.ac.uk

## Acknowledgments
Special thanks to the following libraries and tools that made this project possible:

- Landing AI for the Vision Agentic Document Analysis API