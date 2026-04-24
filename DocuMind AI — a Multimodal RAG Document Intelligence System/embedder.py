import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from ingest import process_file

MODEL_NAME = "all-MiniLM-L6-v2"


def build_vector_store(file_path: str, model, store_path: str = "data/vector_store"):
    """Embed all chunks and save to FAISS index."""

    chunks = process_file(file_path)

    # removed SentenceTransformer loading here — model passed in from outside

    print(f"Embedding {len(chunks)} chunks...")
    embeddings = model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print(f"Vector store built — {index.ntotal} vectors stored")

    os.makedirs(store_path, exist_ok=True)
    faiss.write_index(index, os.path.join(store_path, "index.faiss"))
    with open(os.path.join(store_path, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)
    print(f"Saved to {store_path}/")

    return index, chunks          # ← no longer returns model, it came from outside


def search(query: str, index, chunks, model, top_k=3):
    """Find the most relevant chunks for a question."""
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, top_k)

    results = []
    for rank, idx in enumerate(indices[0]):
        results.append({
            "rank": rank + 1,
            "chunk": chunks[idx],
            "score": round(float(distances[0][rank]), 4)
        })
    return results


if __name__ == "__main__":
    PDF = "data/sample.pdf"
    model = SentenceTransformer(MODEL_NAME)   # load once here for direct testing
    index, chunks = build_vector_store(PDF, model)

    query = "What is this document about?"
    results = search(query, index, chunks, model)
    for r in results:
        print(f"Rank {r['rank']}: {r['chunk'][:200]}")