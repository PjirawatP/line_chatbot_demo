from src.config.database import engine
from src.models.models import Users

from sqlmodel import Session, select


def get_user_by_id(user_id: str):
    with Session(engine) as session:
        return session.exec(
            select(Users).where(Users.user_id == user_id)
        ).first()


def create_user(user_id: str):
    new_user = Users(user_id=user_id, create_at="now")  # ปรับ create_at ตามจริง
    with Session(engine) as session:
        session.add(new_user)
        session.commit()
    