from transformers import pipeline
from app.services.security_service import mask_pii
from app.services.rag_context_service import build_context
from app.services.faiss_service import search_faiss
import re

# =========================
# LOAD MODEL
# =========================
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

# =========================
# MAIN RAG FUNCTION
# =========================
def generate_response(query: str):

    # 🔐 STEP 1 — MASK SENSITIVE DATA
    safe_query = mask_pii(query)

    # =========================
    # STEP 2 — FAISS RETRIEVAL
    # =========================
    results = search_faiss(safe_query, top_k=3)

    if not results:
        return {
            "answer": "Sorry, I could not find accurate information for your query.",
            "sources": [],
            "metadata": {
                "retrieved_schemes": 0
            }
        }

    # =========================
    # STEP 3 — BUILD CONTEXT
    # =========================
    context = build_context(results)

    # =========================
    # STEP 4 — BETTER PROMPT
    # =========================
    prompt = f"""
You are Sarkari Saathi AI.

You help Indian farmers understand agriculture schemes.

Rules:
- Only answer using the provided context.
- Keep answers simple and helpful.
- Mention scheme names clearly.
- If information is missing, say:
  'Sorry, I could not find accurate information.'

Context:
{context}

User Question:
{safe_query}

Answer:
"""

    # =========================
    # STEP 5 — GENERATE RESPONSE
    # =========================
    response = generator(
        prompt,
        max_length=180,
        num_beams=5,
        repetition_penalty=1.2,
        length_penalty=1.0,
        early_stopping=True
    )

    # =========================
    # STEP 6 — CLEAN OUTPUT
    # =========================
    answer = response[0]["generated_text"].strip()

    # Remove unwanted prefixes
    answer = re.sub(
        r"^(Answer|Output|Result):",
        "",
        answer,
        flags=re.IGNORECASE
    ).strip()

    # Fix encoding issue
    answer = answer.replace("â‚¹", "₹")

    # Ensure proper punctuation
    if not answer.endswith("."):
        answer += "."

    # =========================
    # FINAL RESPONSE
    # =========================
    return {
        "answer": answer,
        "sources": results,
        "metadata": {
            "retrieved_schemes": len(results),
            "model": "google/flan-t5-base",
            "search_type": "FAISS Semantic Search"
        }
    }