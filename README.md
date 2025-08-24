# AI PDF Q&A System

## Overview
This project is an AI-powered system that reads and understands PDF documents, allowing users to upload PDFs and ask questions about their content. It uses FastAPI for the backend, FAISS for vector search, and sentence-transformers for embeddings.

## Features
- Upload multiple PDF files
- Extract and chunk text from PDFs
- Store embeddings in FAISS vector DB
- Query answering using RAG (Retrieval-Augmented Generation)
- Source context and page numbers
- Streamlit UI (optional)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. (Optional) Run Streamlit UI:
   ```bash
   streamlit run app/ui.py
   ```

## Sample PDF
Place sample PDFs in the `sample_pdfs/` folder.

## Tech Stack
- Python
- FastAPI
- FAISS
- sentence-transformers
- PyMuPDF
- Streamlit (optional)

## Known Issues
- Large PDFs may take time to process
- OpenAI API key required for GPT-based answers
