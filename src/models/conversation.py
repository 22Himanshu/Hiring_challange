from sqlalchemy import (JSON, Column, DateTime, ForeignKey, Integer, String,
                        func)

from .user import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    state = Column(String, nullable=False)
    context = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
