from sqlalchemy import TIMESTAMP, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Session(Base):
    __tablename__ = "session"
    id = Column(Integer, primary_key=True, nullable=False)
    expires_at = Column(TIMESTAMP(timezone=True), nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
