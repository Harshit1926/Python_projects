# DocuMind AI  
### Multimodal RAG Document Intelligence System  

Turn documents into conversations — ask questions and get context-aware answers.

---

## Overview

DocuMind AI is an end-to-end Retrieval-Augmented Generation (RAG) system that allows users to upload documents and query them using natural language.

The system extracts content, converts it into embeddings, retrieves relevant context, and generates answers using a large language model.

---

## Features

- Upload documents (PDF, image, TXT)
- OCR support for scanned documents
- Text chunking for efficient retrieval
- Semantic search using FAISS
- Context-aware answers using LLM (Groq - LLaMA 3)
- Source-based responses

---

## Architecture

Upload → Extract → Chunk → Embed → Store → Retrieve → Generate Answer


---

## Tech Stack

| Layer | Technology |
|------|----------|
| Backend | Flask |
| Embeddings | SentenceTransformers |
| Vector DB | FAISS |
| OCR | Tesseract |
| LLM | Groq (LLaMA 3) |
| Text Splitting | LangChain |

---

## Project Structure

DocuMind-AI/
│
├── app.py
├── embedder.py
├── ingest.py
├── RAG.py
│
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── templates/
│ ├── index.html
│ ├── chat.html
│ └── result.html
│
├── static/
│
└── data/
│ ├── uploads/
│ └── vector_store/

---

## Setup Instructions

## Clone the repository
bash'''
git clone https://github.com/your-username/documind-ai.git
cd documind-ai

## Install dependencies

pip install -r requirements.txt

## Configure environment variables

Create a .env file:

FLASK_SECRET_KEY=your_secret_key
GROQ_API_KEY=your_api_key

## To enable OCR for scanned PDFs and images, install Tesseract OCR.

Download:
https://github.com/tesseract-ocr/tesseract

After installation, update the path in ingest.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Verify installation:

tesseract --version


## Run the Application

python app.py

Open in browser:

http://127.0.0.1:5000/


## Example Usage

i. Upload a document
ii. Ask a question
iii. Get an answer with source references
iv. Limitations
v. OCR depends on local Tesseract installation
vi. Not optimized for very large documents
vii. In-memory vector store (resets on restart)


## Future Enhancements

1. Replace Tesseract with a scalable OCR solution (Google Vision / AWS Textract)
2. Multi-document querying
3. Chat history support
4. Vector database upgrade (Pinecone / Chroma)
5. Docker-based deployment
6. Improved frontend (React)