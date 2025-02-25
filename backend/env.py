from dotenv import load_dotenv
import os


load_dotenv()

def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url is None:
        raise ValueError("DATABASE_URL is not set")
    return url.replace("postgresql", "postgresql+psycopg")

# DB configuration
DATABASE_URL = get_database_url()

# LLM configuration
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")

# Generic configuration
PORT = os.getenv("PORT")
SECRET_KEY = os.getenv("SECRET_KEY")