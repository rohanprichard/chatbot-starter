import logging
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import json
from fastapi import Depends
from sqlalchemy.orm import Session

from .llm import generate_response
from .util import get_prompt, update_ai_message, get_messages_for_chat_prediction, get_messages_for_chat_initiation
from .model import MessageRequest, ChatResponse, MessageResponse, MessageTypes
from backend.database.models import User
from backend.database.tools import (
    get_or_create_chat,
    save_message,
)
from backend.database.db import get_db
from backend.auth.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/")
async def chat(
    request: MessageRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    logger.info(f"Chat request received: {request.message}")
    try:
        chat = get_or_create_chat(current_user.id, db)

        user_message = save_message(
            chat_id=chat.id,
            content=request.message,
            is_user=True,
            type=request.message_type,
            db=db,
        )

        prompt = get_prompt("chat-prompt")
        messages = get_messages_for_chat_prediction(chat.id, db)

        ai_message = save_message(
            chat_id=chat.id,
            content="",  # Empty placeholder
            is_user=False,
            type="text",  # TODO: Add type
            db=db,
        )

        message_data = {
            "user_message_id": user_message.id,
            "ai_message_id": ai_message.id,
            "created_at": ai_message.created_at.isoformat(),
            "message_type": ai_message.type,
        }

        async def stream_with_ids():
            yield f"data: {json.dumps(message_data)}\n\n"

            full_response = ""
            async for content in generate_response(prompt, messages):
                full_response += content
                yield f"data: {content}\n\n"

            update_ai_message(ai_message.id, full_response)

        return StreamingResponse(stream_with_ids(), media_type="text/event-stream")
    except Exception as e:
        db.rollback()
        logger.error(f"Error in chat: {e}")
        return "Something went wrong"


@router.get("/messages")
async def initiate(
    db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    chat = get_or_create_chat(user_id=user.id, db=db)

    messages = get_messages_for_chat_initiation(chat.id, db=db)
    #  TODO: Add opener message

    return ChatResponse(
        id=chat.id,
        messages=messages
    )


# ------------------------------------------------------------------------------------------------


@router.get("/sessions")
async def chat_sessions():
    return {
        "message": [{"id": "1", "name": "Session 1"}, {"id": "2", "name": "Session 2"}]
    }


@router.get("/chat/sessions/{session_id}")
async def chat_session_history(session_id: str):
    return {"message": "Chat session history"}


@router.put("/chat/message/{message_id}")
async def chat_message(message_id: str):
    return {"message": "Chat message saved"}
