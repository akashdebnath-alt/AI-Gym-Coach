from sqlalchemy.orm import Session

from backend.models import ChatHistory


def save_chat(db: Session, user_id: int, question: str, answer: str):

    chat = ChatHistory(
        user_id=user_id,
        user_message=question,
        ai_response=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(db: Session, user_id: int):

    return (
        db.query(ChatHistory)
        .filter(ChatHistory.user_id == user_id)
        .order_by(ChatHistory.timestamp.desc())
        .all()
    )