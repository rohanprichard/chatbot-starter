import os
from sqlalchemy.orm import Session
import logging

from backend.database.db import SessionLocal
from backend.chat.model import MessageTypes, MessageResponse
from backend.database.tools import (
    get_or_create_chat,
    get_all_messages_from_chat,
    get_message_by_id,
)

logger = logging.getLogger(__name__)


def get_prompt(prompt_name: str):
    with open(
        os.path.join(os.path.dirname(__file__), f"prompts/{prompt_name}.txt"), "r"
    ) as file:
        prompt = file.read()
        return prompt


def start_chat(user_id: str, db: Session):
    chat = get_or_create_chat(user_id, db)
    messages = get_all_messages_from_chat(chat.id, db)
    return chat, messages


def get_chat_history(chat_id: str, db: Session):
    messages = get_all_messages_from_chat(chat_id, db)
    return messages


def update_ai_message(ai_message_id: str, content: str):
    db = SessionLocal()
    try:
        message = get_message_by_id(ai_message_id, db)
        if message:
            message.content = content
            db.commit()
            db.refresh(message)
            return message
        else:
            logger.warning(f"Message with ID {ai_message_id} not found")
            return None
    finally:
        db.close()

def get_messages_for_chat_prediction(chat_id: str, db: Session):
    """
    Get messages for chat prediction.
    """
    messages = get_all_messages_from_chat(chat_id, db)
    serialized_messages = []

    for message in messages:
        if message.type == MessageTypes.TEXT:
            serialized_messages.append({
                "content": message.content,
                "role": "user" if message.is_user else "assistant",
            })
        elif message.type == MessageTypes.RESOURCE:
            serialized_messages.append({
                "content": message.content + "\nResources: " + "\n".join(message.resources),
                "role": "user" if message.is_user else "assistant",
            })
        elif message.type == MessageTypes.BUTTON:
            serialized_messages.append({
                "content": message.content + "\nResponse options: " + "\n".join(message.buttons),
                "role": "user" if message.is_user else "assistant",
            })
        elif message.type == MessageTypes.BUTTON_PRESS:
            serialized_messages.append({
                "content": message.content,
                "role": "user" if message.is_user else "assistant",
            })
            
    return serialized_messages


def get_messages_for_chat_initiation(chat_id: str, db: Session):
    """
    Get messages for chat initiation.
    """
    messages = get_all_messages_from_chat(chat_id, db)
    final_messages = []
    for message in messages:
        logger.info(f"Message: {message}")
        final_message = MessageResponse(
            id=message.id,
            message=message.content,
            is_user=message.is_user,
            created_at=message.created_at,
            message_type=message.type,
            resources=message.resources if message.resources else [],
            buttons=message.buttons if message.buttons else [],
        )
        if message.type == MessageTypes.TEXT:
            final_message.resources = []
            final_message.buttons = []
        elif message.type == MessageTypes.RESOURCE:
            final_message.buttons = []
        elif message.type == MessageTypes.BUTTON:
            final_message.resources = []
        final_messages.append(final_message)

    return final_messages
