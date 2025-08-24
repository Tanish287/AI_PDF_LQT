import faiss
import numpy as np

class VectorDB:
    def __init__(self):
        self.chunks = []
        self.metadatas = []
        self.index = None
        self.embeddings = None

    def add(self, chunks, embeddings, source):
        if self.index is None:
            self.index = faiss.IndexFlatL2(len(embeddings[0]))
            self.embeddings = np.array(embeddings)
        else:
            self.embeddings = np.vstack([self.embeddings, embeddings])
        self.index.add(np.array(embeddings))
        for i, chunk in enumerate(chunks):
            meta = {"source": source, "page": chunk["page"], "text": chunk["text"]}
            self.chunks.append(chunk["text"])
            self.metadatas.append(meta)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        results = []
        for idx in I[0]:
            if idx < len(self.metadatas):
                results.append(self.metadatas[idx])
        return results
