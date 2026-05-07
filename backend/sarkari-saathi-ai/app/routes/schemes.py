from fastapi import APIRouter
from app.services.scheme_service import search_schemes
from app.services.embedding_service import semantic_search

router = APIRouter(prefix="/schemes", tags=["Schemes"])


@router.get("/search")
def search(query: str):
    results = search_schemes(query)

    return {
        "query": query,
        "results": results
    }


@router.get("/semantic-search")
def semantic(query: str):
    results = semantic_search(query)

    return {
        "query": query,
        "results": results
    }