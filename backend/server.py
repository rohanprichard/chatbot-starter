import fastapi
from .chat.server import router as chat_router
from .auth.server import router as auth_router

app = fastapi.FastAPI()

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/health", tags=["health"])
def read_root():
    return {"message": "ok"}
