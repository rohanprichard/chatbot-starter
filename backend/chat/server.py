import logging
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from typing import Union
from datetime import datetime
import json
from fastapi import Depends
from sqlalchemy.orm import Session

from .llm import generate_response
from .util import get_prompt
from .model import MessageRequest
from backend.database.models import User
from backend.database.tools import get_or_create_chat, save_message
from backend.database.db import get_db
from backend.auth.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/")
async def chat(request: MessageRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    logger.info(f"Chat request received: {request.message}")
    
    # Get or create a chat for this user
    chat = get_or_create_chat(current_user.id, db)
    
    # Save the user message first
    user_message = save_message(
        chat_id=chat.id, 
        content=request.message, 
        is_user=True,
        type="text",
        db=db
    )
    
    # Prepare to generate AI response
    prompt = get_prompt("chat-prompt")
    messages = [{"role": "user", "content": request.message}]
    
    # Create a placeholder for the AI message (we'll update content later)
    ai_message = save_message(
        chat_id=chat.id,
        content="",  # Empty placeholder
        is_user=False,
        type="text",
        db=db
    )
    
    async def stream_with_ids():
        yield f"data: {json.dumps({'user_message_id': user_message.id, 'ai_message_id': ai_message.id})}\n\n"
        
        full_response = ""
        async for content in generate_response(prompt, messages):
            full_response += content
            yield f"data: {content}\n\n"
        
        ai_message.content = full_response
        db.commit()
    
    return StreamingResponse(stream_with_ids(), media_type="text/event-stream")


@router.get("/initiate")
async def initiate():
    return {"message": "List of messages"}








# ------------------------------------------------------------------------------------------------


@router.get("/sessions")
async def chat_sessions():
    return {"message": [{"id": "1", "name": "Session 1"}, {"id": "2", "name": "Session 2"}]}


@router.get("/chat/sessions/{session_id}")
async def chat_session_history(session_id: str):
    return {"message": "Chat session history"}


@router.put("/chat/message/{message_id}")
async def chat_message(message_id: str):
    return {"message": "Chat message saved"}
