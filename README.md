# 🇮🇳 Sarkari Saathi AI

Sarkari Saathi AI is a full-stack multilingual AI assistant built to simplify access to Indian government schemes through AI-powered text and voice interactions.

The platform enables users to search, understand, and interact with government welfare schemes in multiple Indian languages using Retrieval-Augmented Generation (RAG), semantic search, and voice-enabled AI assistance.

---

# 🚀 Key Features

## 🤖 AI-Powered Government Scheme Assistant
Ask questions about government schemes in natural language.

### Example Queries
- “Help for farmers”
- “Scholarships for girls”
- “Schemes for unemployed youth”
- “Government support for small businesses”

---

## 🌐 Multilingual Language Support
Supports multiple Indian languages including:
- English
- Hindi
- Marathi
- Tamil
- Bengali
- Telugu
- and more

---

## 🎤 Voice Assistant
Integrated voice-based interaction system:
- Speech-to-Text
- AI Response Generation
- Text-to-Speech Output
- Microphone & Audio File Support

---

## 🧠 Retrieval-Augmented Generation (RAG)
Implements RAG architecture to retrieve relevant scheme data before generating AI responses for improved accuracy and contextual understanding.

---

## 🔎 Semantic Search Engine
Uses embeddings and vector similarity search to identify the most relevant government schemes based on user intent.

---

# 🛠️ Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn
- SpeechRecognition
- gTTS
- Sentence Transformers

## Frontend
- React.js
- Axios
- CSS

## AI & NLP
- RAG Pipeline
- Semantic Embeddings
- NLP-based Query Processing

---

# 📂 Project Structure

```bash
sarkari-saathi/
│
├── backend/
│   └── sarkari-saathi-ai/
│       ├── app/
│       │   ├── routes/
│       │   ├── services/
│       │   ├── core/
│       │   └── data/
│       │
│       ├── requirements.txt
│       └── main.py
│
├── frontend/
│   └── sarkari-frontend/
│       ├── public/
│       ├── src/
│       ├── package.json
│       └── package-lock.json
│
├── .gitignore
└── README.md
```

---

# ⚙️ Backend Setup

## 1️⃣ Navigate to Backend

```bash
cd backend/sarkari-saathi-ai
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 3️⃣ Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Backend URL:
```bash
http://127.0.0.1:8000
```

Swagger Documentation:
```bash
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

## 1️⃣ Navigate to Frontend

```bash
cd frontend/sarkari-frontend
```

## 2️⃣ Install Dependencies

```bash
npm install
```

## 3️⃣ Start React Application

```bash
npm start
```

Frontend URL:
```bash
http://localhost:3000
```

---

# 📡 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | Health Check |
| `/language/process` | POST | Language Translation |
| `/schemes/search` | GET | Government Scheme Search |
| `/schemes/semantic-search` | GET | Semantic Search |
| `/api/v1/rag/ask` | GET | AI-powered RAG Query |
| `/api/v1/voice/ask` | POST | Voice Assistant Endpoint |

---

# 🎯 Example API Request

```bash
GET /api/v1/rag/ask?query=help for farmers
```

---

# 📸 Application Modules

- FastAPI Swagger Documentation
- AI Scheme Search Engine
- Semantic Retrieval System
- Voice-enabled Assistant
- React Frontend Dashboard

---

# 🔮 Future Enhancements

- 🔐 User Authentication & Authorization
- ☁️ Cloud Deployment
- 📱 Mobile Application
- 🗣️ Real-time Voice Streaming
- 🤖 Advanced LLM Integration
- 📊 Analytics Dashboard
- 🌍 Expanded Regional Language Support

---

# 🤝 Contributing

Contributions are welcome.

### Steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

Developed by **Nandini** 🚀
