from pydantic import BaseModel
from typing import List
from datetime import datetime
from enum import Enum

class MessageTypes(str, Enum):
    TEXT = "text"
    BUTTON = "button"
    RESOURCE = "resource"
    BUTTON_PRESS = "button_press"


class MessageRequest(BaseModel):
    message: str
    message_type: MessageTypes


class MessageResponse(BaseModel):
    id: str
    message: str
    is_user: bool
    created_at: datetime
    message_type: MessageTypes
    resources: List[str]
    buttons: List[str]


class ChatResponse(BaseModel):
    messages: List[MessageResponse]
