from langdetect import detect
from transformers import pipeline

# Load translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")

def detect_language(text: str):
    try:
        return detect(text)
    except:
        return "unknown"


def translate_to_english(text: str):
    lang = detect_language(text)

    if lang == "en":
        return text

    if lang == "hi":
        result = translator(text, max_length=512)
        return result[0]['translation_text']

    # fallback
    return text