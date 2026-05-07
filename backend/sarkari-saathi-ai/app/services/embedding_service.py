import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(
    "app/vector_store/faiss_index.bin"
)

# Load metadata
with open("app/vector_store/metadata.pkl", "rb") as f:
    schemes = pickle.load(f)

def semantic_search(query: str, top_k=3):

    # Convert query to embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        scheme = schemes[idx]

        results.append({
            "name": scheme["name"],
            "category": scheme["category"],
            "eligibility": scheme["eligibility"],
            "benefits": scheme["benefits"],
            "description": scheme["description"],
            "documents": scheme["documents"]
        })

    return results