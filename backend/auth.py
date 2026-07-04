from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.models import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# -------------------------
# Hash Password
# -------------------------
def hash_password(password: str):
    return pwd_context.hash(password)


# -------------------------
# Verify Password
# -------------------------
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# -------------------------
# Register User
# -------------------------
def register_user(db: Session, name, email, password):

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        return False, "Email already registered."

    hashed_password = hash_password(password)

    new_user = User(
    name=name,
    email=email,
    password=hashed_password
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return True, "Registration Successful."


# -------------------------
# Login User
# -------------------------
def login_user(db: Session, email, password):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return False, "User not found."

    if not verify_password(password, user.password):
        return False, "Incorrect password."

    return True, user

# -------------------------
# Update User Profile
# -------------------------
def update_profile(
    db: Session,
    user_id,
    age,
    gender,
    height,
    weight,
    goal,
    activity_level,
    experience_level,
    medical_conditions,
    available_equipment
):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return False, "User not found."

    user.age = age
    user.gender = gender
    user.height = height
    user.weight = weight
    user.goal = goal
    user.activity_level = activity_level
    user.experience_level = experience_level
    user.medical_conditions = medical_conditions
    user.available_equipment = available_equipment

    db.commit()
    db.refresh(user)

    return True, user