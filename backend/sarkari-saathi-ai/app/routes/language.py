from fastapi import APIRouter
from app.services.language_service import detect_language, translate_to_english

router = APIRouter(prefix="/language", tags=["Language"])

@router.post("/process")
def process_text(text: str):
    lang = detect_language(text)
    translated = translate_to_english(text)

    return {
        "original_text": text,
        "detected_language": lang,
        "translated_text": translated
    }