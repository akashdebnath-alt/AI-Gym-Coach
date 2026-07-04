from sqlalchemy.orm import Session

from backend.models import WorkoutHistory


def save_workout(db: Session, user_id, workout):

    new_workout = WorkoutHistory(
        user_id=user_id,
        workout=workout,
    )

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    return new_workout


def get_workouts(db: Session, user_id):

    return (
        db.query(WorkoutHistory)
        .filter(WorkoutHistory.user_id == user_id)
        .order_by(WorkoutHistory.created_at.desc())
        .all()
    )