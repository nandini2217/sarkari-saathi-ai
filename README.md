# 🇮🇳 Sarkari Saathi AI

Sarkari Saathi AI is a full-stack multilingual AI assistant designed to help citizens easily understand and access Indian government schemes using text and voice interactions.

The project combines:
- ⚡ FastAPI Backend
- 🎨 React Frontend
- 🧠 AI-powered RAG System
- 🎤 Voice Input & Output
- 🌐 Multilingual Support

---

# 🚀 Features

## ✅ AI Scheme Assistant
Ask questions about government schemes in natural language.

Example:
- "Help for farmers"
- "Scholarships for girls"
- "Schemes for unemployed youth"

---

## 🌐 Multilingual Support
Supports multiple Indian languages:
- Hindi
- English
- Marathi
- Tamil
- Bengali
- and more...

---

## 🎤 Voice Assistant
Users can:
- Speak queries using microphone
- Get AI-generated answers
- Hear responses using text-to-speech

---

## 🧠 RAG (Retrieval-Augmented Generation)
The AI retrieves relevant government scheme information before generating answers for better accuracy.

---

## 🔎 Semantic Search
Uses embeddings and semantic similarity to find the most relevant schemes.

---

# 🛠️ Tech Stack

## Backend
- Python
- FastAPI
- SpeechRecognition
- gTTS
- Sentence Transformers
- Uvicorn

## Frontend
- React.js
- Axios
- CSS

---

# 📂 Project Structure

```bash
sarkari-saathi/
│
├── backend/
│   └── sarkari-saathi-ai/
│       ├── app/
│       ├── requirements.txt
│       └── main.py
│
├── frontend/
│   └── sarkari-frontend/
│       ├── src/
│       ├── public/
│       └── package.json
│
└── README.md


⚙️ Backend Setup

1️⃣ Navigate to backend

cd backend/sarkari-saathi-ai

2️⃣ Create virtual environment

python -m venv venv

3️⃣ Activate virtual environment

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Run FastAPI server

uvicorn app.main:app --reload

Backend runs on:
http://127.0.0.1:8000


💻 Frontend Setup


1️⃣ Navigate to frontend

cd frontend/sarkari-frontend

2️⃣ Install dependencies

npm install

3️⃣ Start React app

npm start

Frontend runs on:
http://localhost:3000


📡 API Endpoints

Health Check

GET /

Language Processing

POST /language/process

Scheme Search

GET /schemes/search

Semantic Search

GET /schemes/semantic-search

RAG Query

GET /api/v1/rag/ask


Example:

/api/v1/rag/ask?query=help for farmers
Voice Assistant
POST /api/v1/voice/ask


Supports:

Voice file upload

Microphone interaction

AI voice response

📸 Screenshots

Swagger API Docs

FastAPI interactive documentation

React Frontend

AI chat interface with voice support


🔮 Future Improvements

🔐 User Authentication

📱 Mobile App

☁️ Cloud Deployment

🗣️ Real-time Streaming Voice

🤖 LLM Integration

📊 Admin Dashboard

🌍 Regional Language Expansion



🤝 Contributing

Contributions are welcome.

Fork the repository
Create a new branch
Commit changes
Push to branch
Open Pull Request


📜 License

This project is licensed under the MIT License.


👩‍💻 Author

Developed by Nandini 🚀