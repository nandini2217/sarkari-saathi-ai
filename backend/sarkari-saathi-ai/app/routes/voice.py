from fastapi import APIRouter, UploadFile, File
from app.services.voice_service import speech_to_text, text_to_speech
from app.services.rag_service import generate_response

router = APIRouter(prefix="/api/v1/voice", tags=["Voice"])


@router.post("/ask")
async def voice_ask(file: UploadFile = File(...)):
    try:
        # 🎤 Step 1: Read uploaded audio file
        audio_bytes = await file.read()

        # 🎤 Step 2: Convert speech → text
        query = speech_to_text(audio_bytes)

        if not query or query.strip() == "":
            return {
                "query": "Error",
                "answer": "Sorry, could not understand audio."
            }

        # 🤖 Step 3: Get AI answer
        result = generate_response(query)

        # 🔊 Step 4: Convert answer → speech
        audio_file = text_to_speech(result["answer"])

        return {
            "query": query,
            "answer": result["answer"],
            "audio_file": audio_file
        }

    except Exception as e:
        return {
            "query": "Error",
            "answer": "Something went wrong while processing audio."
        }