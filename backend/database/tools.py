from sqlalchemy.orm import Session
from backend.database.models import User, Chat, Message


# User Utilities

def create_user(email: str, password: str, db: Session) -> User:
    user = User(email=email, password=password)
    db.add(user)
    db.commit()
    return user

def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter_by(email=email).first()

def get_user_by_id(user_id: str, db: Session) -> User:
    return db.query(User).filter_by(id=user_id).first()


# Chat Utilities

def get_all_chats_by_user_id(user_id: str, db: Session) -> list[Chat]:
    return db.query(Chat).filter_by(user_id=user_id).order_by(Chat.created_at.desc()).all()

def get_chat_by_id(chat_id: str, db: Session) -> Chat:
    return db.query(Chat).filter_by(id=chat_id).first()

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

def save_message(db: Session, chat_id: str, content: str, is_user: bool, type: str = "text", buttons: list[str] = None, resources: list[str] = None) -> Message:
    message = Message(
        chat_id=chat_id, 
        content=content, 
        is_user=is_user,
        type=type,
        buttons=buttons,
        resources=resources
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_all_messages_from_chat(chat_id: str, db: Session) -> list[Message]:
    return db.query(Message).filter_by(chat_id=chat_id).order_by(Message.created_at.desc()).all()

def get_message_by_id(message_id: str, db: Session) -> Message:
    return db.query(Message).filter_by(id=message_id).first()