import speech_recognition as sr
from gtts import gTTS
import tempfile
import os


def speech_to_text(audio_bytes):
    recognizer = sr.Recognizer()

    # Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    try:
        with sr.AudioFile(temp_audio_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language="en-IN")
        return text

    except Exception as e:
        print("STT Error:", e)
        return ""

    finally:
        os.remove(temp_audio_path)


def text_to_speech(text: str):
    tts = gTTS(text=text, lang='en')

    file_path = "response.mp3"
    tts.save(file_path)

    return file_path