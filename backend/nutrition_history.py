from sqlalchemy.orm import Session
from backend.models import NutritionHistory


def save_nutrition(db: Session, user_id, nutrition):

    new_plan = NutritionHistory(
        user_id=user_id,
        nutrition=nutrition,
    )

    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return new_plan


def get_nutritions(db: Session, user_id):

    return (
        db.query(NutritionHistory)
        .filter(NutritionHistory.user_id == user_id)
        .order_by(NutritionHistory.created_at.desc())
        .all()
    )