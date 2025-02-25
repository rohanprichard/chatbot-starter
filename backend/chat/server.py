import logging
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from .llm import generate_response
from .util import get_prompt
from .model import ChatRequest


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest):
    
    logger.info(f"Chat request received: {request.message}")

    prompt = get_prompt("chat-prompt")
    messages = [{"role": "user", "content": request.message}]

    return StreamingResponse(generate_response(prompt, messages), media_type="text/event-stream") 


@router.get("/initiate")
async def initiate():
    return {"message": "List of messages"}


@router.get("/sessions")
async def chat_sessions():
    return {"message": [{"id": "1", "name": "Session 1"}, {"id": "2", "name": "Session 2"}]}


@router.get("/chat/sessions/{session_id}")
async def chat_session_history(session_id: str):
    return {"message": "Chat session history"}


@router.put("/chat/message/{message_id}")
async def chat_message(message_id: str):
    return {"message": "Chat message saved"}
