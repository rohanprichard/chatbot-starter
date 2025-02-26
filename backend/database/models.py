from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    chats = relationship("Chat", back_populates="user")


class Chat(Base):
    __tablename__ = "chat"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    messages = relationship("Message", back_populates="chat")
    user = relationship("User", back_populates="chats")


class Message(Base):
    __tablename__ = "message"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    chat_id = Column(String, ForeignKey("chat.id"), nullable=False)
    type = Column(String, nullable=False)

    content = Column(String, nullable=False)
    is_user = Column(Boolean, nullable=False)

    buttons = Column(String, nullable=True)
    resources = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    chat = relationship("Chat", back_populates="messages")
