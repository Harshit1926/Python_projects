import faiss
import pickle
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from groq import Groq

load_dotenv()

MODEL_NAME = "all-MiniLM-L6-v2"
STORE_PATH = "data/vector_store"

def load_vector_store():
    """Load the saved FAISS index and chunks from disk."""
    print("Loading vector store...")
    index = faiss.read_index(f"{STORE_PATH}/index.faiss")
    with open(f"{STORE_PATH}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    print(f"Loaded {index.ntotal} vectors and {len(chunks)} chunks")
    return index, chunks


def retrieve_chunks(query, index, chunks, model, top_k=3):
    """Find the most relevant chunks for the query."""
    query_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, top_k)

    retrieved = []
    for rank, idx in enumerate(indices[0]):
        retrieved.append({
            "rank": rank + 1,
            "text": chunks[idx],
            "score": round(float(distances[0][rank]), 4)
        })
    return retrieved


def build_prompt(query, retrieved_chunks):
    """Build the prompt that gets sent to the LLM."""

    # combine retrieved chunks into one context block
    context = ""
    for i, chunk in enumerate(retrieved_chunks):
        context += f"\n[Source {i+1}]\n{chunk['text']}\n"

    prompt = f"""You are a helpful assistant. Answer the user's question using ONLY 
the context provided below. If the answer is not in the context, say 
"I couldn't find that in the document."

At the end of your answer, always mention which Source number(s) you used.

Context:
{context}

Question: {query}

Answer:"""
    return prompt


def ask(query, index, chunks, model):
    """Full RAG pipeline — retrieve + generate."""

    # Step 1 — retrieve relevant chunks
    print(f"\nQuestion: {query}")
    print("Retrieving relevant chunks...")
    retrieved = retrieve_chunks(query, index, chunks, model)

    # Step 2 — build prompt with context
    prompt = build_prompt(query, retrieved)

    # Step 3 — send to Groq LLM
    print("Generating answer...\n")
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        # NEW - use this
        model="llama-3.3-70b-versatile",   
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2   
    )

    answer = response.choices[0].message.content
    return answer, retrieved


if __name__ == "__main__":
    # load everything
    index, chunks = load_vector_store()
    model = SentenceTransformer(MODEL_NAME)

    # ask questions in a loop
    print("\nRAG system ready! Type 'quit' to exit.\n")
    while True:
        query = input("Ask a question: ").strip()
        if query.lower() == "quit":
            break
        if query:
            ask(query, index, chunks, model)
            print("\n" + "="*50 + "\n")