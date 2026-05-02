# 🚀 AI Resume Analyzer (Full-Stack AI Agent)

An intelligent **AI-powered Resume Analyzer & Career Assistant** that helps users:

* 📄 Upload and analyze resumes
* 💬 Chat with an AI career assistant
* 🎯 Get job recommendations
* 📊 Improve skills and career direction

---

## 🧠 Features

### 🔹 1. AI Chat Assistant

* Conversational AI (Gemini API)
* Context-aware responses using resume + chat history
* Career guidance, interview prep, skill suggestions

### 🔹 2. Resume Upload & Parsing

* Upload PDF/DOCX resumes
* Extract and analyze text using NLP (spaCy)

### 🔹 3. Job Recommendations

* Suggests relevant job roles
* Matches resume with job profiles

### 🔹 4. User System

* Email-based login
* User-specific chat history & resume storage

### 🔹 5. Modern Chat UI

* ChatGPT-like interface
* Typing animation
* Enter-to-send support

---

## 🏗 Tech Stack

### 🔹 Frontend

* React (Vite)
* Axios
* CSS (custom UI)

### 🔹 Backend

* FastAPI
* Python

### 🔹 AI & NLP

* Google Gemini API
* spaCy (resume parsing)

### 🔹 Database

* MongoDB

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   │   └── resume_routes.py
│   ├── services/
│   │   ├── chat_agent.py
│   │   ├── parser.py
│   │   ├── job_recommender.py
│   │   ├── auth.py
│   ├── utils/
│   │   └── file_handler.py
│   ├── config/
│   │   └── db.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   └── package.json
│
└── README.md
```

---

## ⚙️ Setup Instructions

---

### 🔹 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

### 🔹 2. Backend Setup

```bash
cd backend

# create virtual environment
python -m venv venv

# activate
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# install dependencies
pip install -r requirements.txt
```

---

### 🔹 3. Environment Variables

Create `.env` inside backend:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 🔹 4. Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 🔹 5. Frontend Setup

```bash
cd ../frontend

npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🔌 API Endpoints

### 🔹 Auth

```
POST /login
```

### 🔹 Resume Upload

```
POST /upload-resume
```

### 🔹 Chat AI

```
POST /chat
```

### 🔹 Job Recommendations

```
POST /recommend-jobs
```

---

## 💡 How It Works

1. User logs in with email
2. Uploads resume
3. Resume is parsed using NLP
4. Chat uses:

   * Resume context
   * Chat history
5. AI responds intelligently
6. Job recommendations are generated

---

## 🔥 Future Improvements

* ✅ JWT Authentication
* ✅ Real-time streaming responses
* ✅ Resume scoring system
* ✅ ATS optimization
* ✅ Multi-user dashboard
* ✅ Chat history sidebar
* ✅ Voice-based AI assistant

---

## 📸 Screenshots

*Add your UI screenshots here*

---

## 🤝 Contributing

Contributions are welcome!

```bash
git fork
git clone
git checkout -b feature-name
git commit -m "Added feature"
git push
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Harsh Rajvanshi**

* GitHub: https://github.com/redcoder7417
* LinkedIn: https://www.linkedin.com/in/harsh-rajvanshi-336a2422b/

---

## ⭐ Final Note

This project demonstrates:

* Full-stack development
* AI integration
* Real-world problem solving

👉 A strong **portfolio-ready project for AI/ML + Full Stack roles**

---

**🚀 Built with passion and curiosity**
