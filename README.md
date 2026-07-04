# 🏋️ AI Gym Coach

An intelligent fitness coaching application powered by **Google Gemini**, **LangGraph**, **RAG (Retrieval-Augmented Generation)**, and **Streamlit**.

The application provides personalized workout plans, AI-powered nutrition plans, fitness calculations, and progress tracking based on each user's profile.

---

# Features

### User Authentication

* User Registration
* Secure Login
* Password Hashing using Passlib

### User Profile

* Personal Information
* Height & Weight
* Fitness Goal
* Activity Level
* Experience Level
* Medical Conditions
* Available Equipment

### AI Coach

* Conversational AI powered by Google Gemini
* LangGraph ReAct Agent
* Tool Calling
* RAG-based Fitness Knowledge
* Personalized Responses

### Workout Generator

* AI-generated workout plans
* Personalized based on user profile
* Workout History

### Nutrition Planner

* AI-generated nutrition plans
* Personalized meal recommendations
* Nutrition History

### Progress Tracking

* Weight Tracking
* BMI Tracking
* Body Fat Tracking
* Progress Visualization

---

# Technologies Used

## Frontend

* Streamlit

## Backend

* Python
* SQLAlchemy
* SQLite

## Artificial Intelligence

* Google Gemini
* LangGraph
* LangChain
* FAISS
* HuggingFace Embeddings

## Other Libraries

* Pandas
* Plotly
* NumPy
* Passlib
* Bcrypt

---

# Project Structure

```
gym_coach_pro/

├── app.py
├── requirements.txt
├── backend/
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── graph.py
│   ├── tools.py
│   ├── workout_generator.py
│   ├── diet_generator.py
│   ├── workout_history.py
│   ├── nutrition_history.py
│   ├── progress.py
│   └── rag/
│
├── knowledge/
│
├── faiss_index/
│
└── README.md
```

---

# Installation

Clone the repository.

Install the required packages.

Run the application.

```
pip install -r requirements.txt

streamlit run app.py
```

---

# Future Improvements

* Exercise Video Recommendations
* Cloud Database
* Mobile Application
* Wearable Device Integration
* Weekly Fitness Reports
* Voice Assistant

---

# Developer

**Akash Debnath**

Second Year CSE Project

---

# License

This project is created for educational purposes.
