from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    chats = relationship("Chat", back_populates="user")


class Chat(Base):
    __tablename__ = "chat"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    summary = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    messages = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = "message"
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    chat_id = Column(String, ForeignKey("chat.id"), nullable=False)

    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    chat = relationship("Chat", back_populates="messages")
