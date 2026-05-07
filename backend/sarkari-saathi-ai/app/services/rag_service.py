from transformers import pipeline
from app.services.embedding_service import semantic_search
from app.services.security_service import mask_pii
import re

# Load model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_response(query: str):
    # 🔐 Step 1: Mask sensitive data
    safe_query = mask_pii(query)

    # 🔍 Step 2: Retrieve relevant schemes
    results = semantic_search(safe_query, top_k=1)

    if not results:
        return {
            "answer": "Sorry, I could not find any relevant government scheme for your query.",
            "sources": []
        }

    # 🧠 Step 3: Build structured context
    scheme = results[0]
    # Using labels helps the model identify specific data points better
    context_data = f"Scheme: {scheme['name']}, Benefits: {scheme['benefits']}, Eligibility: {scheme['eligibility']}"

    # ✍️ Step 4: Few-Shot Prompting
    # We provide one example (shot) to teach the model the desired length and tone.
    prompt = f"""Answer the question in two descriptive sentences using the provided context.

Example:
Context: Scheme: Ladli Behna, Benefits: ₹1250 per month, Eligibility: Women in MP
Question: Tell me about the Ladli Behna scheme?
Answer: The Ladli Behna scheme provides ₹1250 per month to eligible women in Madhya Pradesh. This financial assistance aims to improve the health and nutrition status of women in the state.

Actual Task:
Context: {context_data}
Question: {safe_query}
Answer:"""

    # 🤖 Step 5: Optimized Generation Logic
    response = generator(
        prompt,
        max_length=100,
        num_beams=5,             # Higher beams for better quality
        repetition_penalty=1.2,
        length_penalty=1.5,      # Encourages the model to be more descriptive
        early_stopping=True
    )

    # 🧹 Step 6: Clean output
    answer = response[0]['generated_text'].strip()

    # Final cleanup to remove any potential "Answer:" prefix from the model
    answer = re.sub(r"^(Answer|Output|Result):", "", answer, flags=re.IGNORECASE).strip()
    answer = answer.replace("â‚¹", "₹")

    # Ensure it ends with a period
    if not answer.endswith("."):
        answer += "."

    return {
    "answer": answer,
    "sources": results,
    "metadata": {
        "retrieved_schemes": len(results),
        "model": "google/flan-t5-base"
    }
}