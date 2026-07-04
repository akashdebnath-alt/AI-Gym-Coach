# 🏋️ AI Gym Coach

An **AI-powered fitness coaching platform** built using **Streamlit, LangGraph, Google Gemini, and Retrieval-Augmented Generation (RAG)**.

The application acts as an intelligent fitness assistant that generates personalized workout plans, nutrition plans, answers fitness-related questions using an AI agent, and tracks user progress.

---

## ✨ Features

* 🔐 Secure User Authentication
* 🤖 AI Fitness Coach (Google Gemini)
* 🏋️ Personalized Workout Generator
* 🥗 AI Nutrition Planner
* 📚 RAG-based Knowledge Retrieval
* 💬 AI Chat Assistant
* 📈 Progress Tracking Dashboard
* 📝 Workout History
* 🍽️ Nutrition History
* 🗄️ SQLite Database
* ⚡ LangGraph Agent Architecture
* 🎨 Interactive Streamlit Interface

---

## 🛠 Tech Stack

**Frontend**

* Streamlit

**Backend**

* Python
* SQLAlchemy

**AI**

* Google Gemini
* LangGraph
* LangChain

**Database**

* SQLite

**RAG**

* FAISS
* PyPDF
* Sentence Transformers

**Other Libraries**

* Pandas
* NumPy
* Plotly
* Pydantic
* bcrypt

---
## 📂 Project Structure

```text
AI-Gym-Coach/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│
├── backend/
│   ├── auth.py
│   ├── database.py
│   ├── graph.py
│   ├── llm.py
│   ├── models.py
│   ├── prompts.py
│   ├── tools.py
│   ├── workout_generator.py
│   ├── diet_generator.py
│   ├── progress.py
│   ├── chat_history.py
│   ├── workout_history.py
│   ├── nutrition_history.py
│   └── rag/
│
├── knowledge/
│
└── faiss_index/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/akashdebnath-alt/AI-Gym-Coach.git
```

Move into the project directory

```bash
cd AI-Gym-Coach
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```
