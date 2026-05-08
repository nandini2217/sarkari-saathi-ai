from fastapi import APIRouter

from app.services.embedding_service import semantic_search

router = APIRouter(
    prefix="/schemes",
    tags=["Schemes"]
)

@router.get("/search")
def search_schemes(query: str):

    results = semantic_search(query)

    return {
        "query": query,
        "results": results
    }