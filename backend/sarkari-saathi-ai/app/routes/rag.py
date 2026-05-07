from fastapi import APIRouter
from app.services.rag_service import generate_response

router = APIRouter(
    prefix="/api/v1/rag",
    tags=["RAG"]
)

@router.get("/ask")
def ask(query: str):
    return generate_response(query)