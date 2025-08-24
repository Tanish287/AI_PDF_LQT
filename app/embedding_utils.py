from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(chunks):
    texts = [chunk["text"] if isinstance(chunk, dict) else chunk for chunk in chunks]
    return model.encode(texts, show_progress_bar=False)
