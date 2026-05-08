import json
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from app.services.chunking_service import chunk_text

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load agriculture dataset
with open("app/data/agriculture_schemes.json", "r", encoding="utf-8") as f:
    schemes = json.load(f)

documents = []
metadata = []

# Create chunks
for scheme in schemes:

    full_text = f"""
    Scheme Name: {scheme['name']}

    Category: {scheme['category']}

    Eligibility:
    {scheme['eligibility']}

    Benefits:
    {scheme['benefits']}

    Description:
    {scheme['description']}
    """

    chunks = chunk_text(full_text)

    for chunk in chunks:
        documents.append(chunk)
        metadata.append(scheme)

# Generate embeddings
embeddings = model.encode(documents)

# Convert to numpy float32
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, "app/vector_store/faiss_index.bin")

# Save metadata
with open("app/vector_store/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print(f"✅ FAISS index created with {len(documents)} chunks")


def search_faiss(query, top_k=3):

    # Load FAISS index
    index = faiss.read_index("app/vector_store/faiss_index.bin")

    # Load metadata
    with open("app/vector_store/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    # Query embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []

    seen = set()

    for idx in indices[0]:

        scheme = metadata[idx]

        scheme_name = scheme["name"]

        if scheme_name not in seen:
            results.append(scheme)
            seen.add(scheme_name)

    return results