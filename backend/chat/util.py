import os
from sqlalchemy.orm import Session

from backend.database.tools import get_or_create_chat, get_all_messages_from_chat


def get_prompt(prompt_name: str):
    with open(os.path.join(os.path.dirname(__file__), f"prompts/{prompt_name}.txt"), "r") as file:
        prompt = file.read()
        return prompt

def start_chat(user_id: str, db: Session):
    chat = get_or_create_chat(user_id, db)
    messages = get_all_messages_from_chat(chat.id, db)
    return chat, messages

def get_chat_history(chat_id: str, db: Session):
    messages = get_all_messages_from_chat(chat_id, db)
    return messages