from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.pdf_utils import extract_chunks_from_pdf
from app.embedding_utils import get_embeddings
from app.vector_db import VectorDB
from app.rag import generate_answer
import os

app = FastAPI()
vector_db = VectorDB()

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_path = f"sample_pdfs/{file.filename}"
    with open(pdf_path, "wb") as f:
        f.write(await file.read())
    chunks = extract_chunks_from_pdf(pdf_path)
    embeddings = get_embeddings(chunks)
    vector_db.add(chunks, embeddings, file.filename)
    return {"message": "PDF uploaded and processed", "chunks": len(chunks)}

@app.post("/query/")
async def query_pdf(query: str = Form(...)):
    query_embedding = get_embeddings([query])[0]
    results = vector_db.search(query_embedding)
    answer = generate_answer(query, results)
    return JSONResponse({"answer": answer, "context": results})
