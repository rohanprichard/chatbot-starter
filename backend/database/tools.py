
from sqlalchemy.orm import Session
from backend.database.models import User, Chat, Message


# User Utilities

def create_user(email: str, password: str, db: Session) -> User:
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    return user

def get_user_by_email(email: str, db: Session) -> User:
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id: str, db: Session) -> User:
    return User.query.filter_by(id=user_id).first()


# Chat Utilities

def get_all_chats_by_user_id(user_id: str, db: Session) -> list[Chat]:
    return Chat.query.filter_by(user_id=user_id).order_by(Chat.created_at.desc()).all()

def get_chat_by_id(chat_id: str, db: Session) -> Chat:
    return Chat.query.filter_by(id=chat_id).first()

def create_chat(user_id: str, db: Session) -> Chat:
    chat = Chat(user_id=user_id)
    db.add(chat)
    db.commit()
    return chat

def get_or_create_chat(user_id: str, db: Session) -> Chat:
    chats = get_all_chats_by_user_id(user_id, db)
    if len(chats) == 0:  # TODO: Add chat refresh logic
        chat = create_chat(user_id, db)
    else:
        chat = chats[0]
    return chat


# Message Utilities

def save_message(chat_id: str, content: str, db: Session) -> Message:
    message = Message(chat_id=chat_id, content=content)
    db.add(message)
    db.commit()
    return message

def get_all_messages_from_chat(chat_id: str, db: Session) -> list[Message]:
    return Message.query.filter_by(chat_id=chat_id).order_by(Message.created_at.desc()).all()

def get_message_by_id(message_id: str, db: Session) -> Message:
    return Message.query.filter_by(id=message_id).first()