from pydantic import BaseModel
from typing import List
from datetime import datetime


class MessageRequest(BaseModel):
    message: str


class MessageResponse(BaseModel):
    id: str
    message: str
    is_user: bool
    created_at: datetime


class MessageResponseWithResources(MessageResponse):
    resources: List[str]


class MessageResponseWithButtons(MessageResponse):
    buttons: List[str]


class ChatResponse(BaseModel):
    messages: List[MessageResponse]
