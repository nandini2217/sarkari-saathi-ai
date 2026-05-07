from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routes import health, language, schemes, rag, voice

app = FastAPI(
    title="Sarkari Saathi AI",
    description="Multilingual AI Assistant for Government Schemes with Voice + RAG",
    version="1.0.0"
)

# 🌐 Enable CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📁 Serve static files (for audio)
app.mount("/static", StaticFiles(directory="."), name="static")

# 🔌 Include all routes
app.include_router(health.router)
app.include_router(language.router)
app.include_router(schemes.router)
app.include_router(rag.router)
app.include_router(voice.router)

# 🏠 Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Sarkari Saathi AI 🚀",
        "docs": "http://127.0.0.1:8000/docs",
        "version": "1.0.0"
    }