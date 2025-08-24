import fitz  # PyMuPDF

def extract_chunks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        for para in paragraphs:
            chunks.append({
                "text": para,
                "page": page_num + 1
            })
    return chunks
