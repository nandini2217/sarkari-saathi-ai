import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

from app.services.dataset_service import load_schemes

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load schemes
schemes = load_schemes()

# Prepare scheme texts
scheme_texts = [
    f"""
    {scheme['name']}
    {scheme['category']}
    {scheme['eligibility']}
    {scheme['benefits']}
    {scheme['description']}
    """
    for scheme in schemes
]

# Convert to embeddings
embeddings = model.encode(scheme_texts)

# Convert to numpy array
embedding_matrix = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embedding_matrix.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(embedding_matrix)

# Save index
faiss.write_index(index, "app/vector_store/faiss_index.bin")

# Save metadata
with open("app/vector_store/metadata.pkl", "wb") as f:
    pickle.dump(schemes, f)

print("✅ FAISS index created successfully")