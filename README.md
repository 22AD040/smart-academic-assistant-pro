![GitHub stars](https://img.shields.io/github/stars/22AD040/smart-academic-assistant-pro?style=social)
![GitHub forks](https://img.shields.io/github/forks/22AD040/smart-academic-assistant-pro?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/22AD040/smart-academic-assistant-pro)

---

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Gemini](https://img.shields.io/badge/Gemini-AI-brightgreen)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)
![RAG](https://img.shields.io/badge/RAG-Architecture-purple)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

# 🎓 Smart Academic Assistant Pro

> 🧠 AI-Powered Academic Assistant with PDF Intelligence using RAG (Retrieval-Augmented Generation)

---

## 🚀 Live Demo

🌐 **Frontend (Streamlit App):**  
👉 https://your-streamlit-link.streamlit.app/

⚙️ **Backend (FastAPI - Render):**  
👉 https://smart-academic-assistant-pro.onrender.com

---

## 🧠 Overview

**Smart Academic Assistant Pro** is a full-stack AI application that helps students:

- 📄 Learn from PDFs
- 🤖 Get AI-generated structured answers
- 🔍 Perform semantic search using embeddings
- 🧠 Understand concepts via mindmaps & key points

It combines **Generative AI + Vector Search (RAG)** to deliver accurate, context-aware answers.

---

## ✨ Features

### 🔐 Authentication System
- Login / Register
- Per-user session management
- Secure local storage (JSON-based)

### 📄 PDF Intelligence (RAG)
- Upload PDF documents
- Chunking + Embeddings
- FAISS-based semantic retrieval
- Context-aware answering

### 🤖 AI Capabilities
- Powered by **Google Gemini API**
- Structured answers with:
  - Headings
  - Bullet points
  - Examples
  - Key Points
  - Mindmaps (text-based)

### 💬 Chat System
- Persistent chat history per user
- Sidebar history navigation
- “New Chat” feature

### ⚡ Performance
- Fast retrieval using FAISS
- Optimized embeddings (MiniLM)
- Backend deployed on Render

---

## 🧠 Tech Stack

| Technology            | Role                     |
|---------------------|--------------------------|
| Streamlit           | Frontend UI              |
| FastAPI             | Backend API              |
| Google Gemini API   | LLM (Answer generation)  |
| HuggingFace         | Embeddings               |
| FAISS               | Vector Database          |
| PyPDF               | PDF Processing           |
| Python              | Core Logic               |

---

## 🏗️ Architecture (RAG)

```text
User → Upload PDF → Chunking → Embeddings → FAISS Index
                                 ↓
User Query → Retrieve Relevant Chunks → Gemini → Answer

---

## 📁 Project Structure

```
smart-academic-assistant-pro/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── embeddings.py
│   │   ├── retrieval.py
│   │   ├── vector_store.py
│   │
│   ├── services/
│   │   └── llm_service.py
│   │
│   ├── utils/
│   │   └── pdf_utils.py
│   │
│   ├── auth/
│   │   └── auth.py
│   │
│   └── config.py
│
├── scripts/
│   └── build_index.py
│
├── data/
│   ├── users.json
│   └── chats.json
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## 📸 Screenshots

### 🔐 Login Page

*(Add image in /assets folder)*

### 🤖 Chat Interface

*(Add image in /assets folder)*

### 📄 PDF Upload + Q&A

*(Add image in /assets folder)*

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/22AD040/smart-academic-assistant-pro.git
cd smart-academic-assistant-pro
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

### Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🌐 Deployment

### 🔹 Backend (Render)

* Create Web Service
* Add environment variable:

```
GEMINI_API_KEY=your_key
```

* Start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

### 🔹 Frontend (Streamlit Cloud)

Add secrets:

```toml
gemini_api_key = "your_key"
```

---

## 🔒 Security

* 🔐 API keys stored securely (`.env` / Streamlit secrets)
* 🚫 No sensitive data in GitHub
* 👤 User data isolated per session
* 📁 `.gitignore` prevents data leakage

---

## ⚠️ Known Limitations

* ⏳ PDF processing may be slow (free tier hosting)
* 🔁 Backend may sleep after inactivity
* 📄 Large PDFs (>5MB) may timeout

---

## 🚀 Future Improvements

* ⚡ Background PDF processing
* 🔐 Password hashing (bcrypt)
* 📊 Visual mindmaps
* 🌍 Multi-language support
* 📱 Mobile responsive UI

---

## 👩‍💻 Author

**Ratchita B**
🎓 Artificial Intelligence & Data Science

---

## ⭐ Support

If you like this project:

* ⭐ Give it a star on GitHub
* 🔗 Share with others

---

## 📜 License

This project is licensed under the MIT License.
