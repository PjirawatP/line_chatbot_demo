from sqlalchemy import Column, String
from sqlmodel import ForeignKey, Relationship, SQLModel, Field

from typing import Optional

from datetime import datetime


class Users(SQLModel, table=True):
    __tablename__ = "users"

    user_id: str = Field(sa_column=Column(String, primary_key=True, nullable=False))

    conversation: list["Conversations"] = Relationship(back_populates="user")


class Conversations(SQLModel, table=True):
    __tablename__ = "conversations"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(sa_column=Column(String, ForeignKey("users.user_id"), nullable=False))
    query_message: str
    response_message: str
    create_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[Users] = Relationship(back_populates="conversation")
