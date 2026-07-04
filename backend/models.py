from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database import Base


# ==========================
# USER TABLE
# ==========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    age = Column(Integer)
    gender = Column(String)

    height = Column(Float)
    weight = Column(Float)

    goal = Column(String)
    activity_level = Column(String)

    experience_level = Column(String)
    medical_conditions = Column(Text)
    available_equipment = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")
    chats = relationship("ChatHistory", back_populates="user", cascade="all, delete-orphan")
    workouts = relationship("WorkoutHistory", back_populates="user", cascade="all, delete-orphan")
    nutritions = relationship("NutritionHistory", back_populates="user", cascade="all, delete-orphan")


# ==========================
# PROGRESS TABLE
# ==========================
class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    weight = Column(Float)
    bmi = Column(Float)
    body_fat = Column(Float)

    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="progress")


# ==========================
# CHAT HISTORY
# ==========================
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    user_message = Column(Text)
    ai_response = Column(Text)

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="chats")


# ==========================
# WORKOUT HISTORY
# ==========================
class WorkoutHistory(Base):
    __tablename__ = "workout_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    workout = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workouts")


# ==========================
# NUTRITION HISTORY
# ==========================
class NutritionHistory(Base):
    __tablename__ = "nutrition_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    nutrition = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="nutritions")