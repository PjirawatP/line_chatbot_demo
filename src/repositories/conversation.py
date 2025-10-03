from sqlmodel import select, Session

from src.config.database import engine
from src.models.models import Conversations


def get_recent_conversation_by_user_id(user_id: str):
    with Session(engine) as session:
        statement = select(Conversations).where(Conversations.user_id == user_id)
        return session.exec(statement).all()


def save_conversation_by_user_id(user_id: str, query_message: str, response_message: str):
    conversation = Conversations(
        user_id=user_id,
        query_message=query_message,
        response_message=response_message
    )

    with Session(engine) as session:
        session.add(conversation)
        session.commit()
        session.refresh(conversation)

    return conversation
    