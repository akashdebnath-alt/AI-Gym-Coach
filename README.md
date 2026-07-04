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
---

# 📸 Application Screenshots

> Screenshots will be added in future updates.

## Login

![Login](assets/login.png)

---

## Dashboard

![Dashboard](assets/dashboard.png)

---

## AI Coach

![AI Coach](assets/aicoach.png)

---

## Workout Generator

![Workout](assets/workout.png)

---

## Nutrition Planner

![Nutrition](assets/nutrition.png)

---

## Progress Tracking

![Progress](assets/progress.png)

---

# 🏗️ System Architecture

```text
                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
          LangGraph AI Agent
          ┌────────┼────────┐
          │        │        │
          ▼        ▼        ▼
      Gemini    AI Tools   RAG
                            │
                            ▼
                    FAISS Knowledge Base
                            │
                            ▼
                     SQLite Database
```

---

# 🚀 Future Improvements

This project will continue to evolve with new AI capabilities.

### Version 2.0

* 🎤 Voice AI Coach
* 📅 Workout Calendar
* 📊 Advanced Analytics
* 🍎 Smart Nutrition Recommendations

### Version 3.0

* 📷 Exercise Pose Detection
* 🤖 Computer Vision Workout Tracking
* ⌚ Smartwatch Integration

### Version 4.0

* ☁️ Cloud Deployment
* 📱 Mobile Application
* 👨‍🏫 AI Personal Trainer

---

# 👨‍💻 Developer

**Akash Debnath**

Computer Science Engineering Student

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Generative AI
* Large Language Models

GitHub:

https://github.com/akashdebnath-alt

LinkedIn:

https://www.linkedin.com/in/akash-debnath

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.

It motivates me to continue improving the project.
