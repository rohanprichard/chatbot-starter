import fastapi
from .chat.server import router as chat_router

app = fastapi.FastAPI()

app.include_router(chat_router, prefix="/chat")

@app.get("/health")
def read_root():
    return {"message": "ok"}
