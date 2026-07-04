from sqlalchemy.orm import Session

from backend.models import Progress



def add_progress(db: Session, user_id, weight, bmi, body_fat=None):
    progress = Progress(
        user_id=user_id,
        weight=weight,
        bmi=bmi,
        body_fat=body_fat
    )

    db.add(progress)
    db.commit()
    db.refresh(progress)

    return progress


def get_progress(db: Session, user_id):
    return (
        db.query(Progress)
        .filter(Progress.user_id == user_id)
        .order_by(Progress.date.asc())
        .all()
    )