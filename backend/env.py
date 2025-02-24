from dotenv import load_dotenv
import os


load_dotenv()

# DB configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# LLM configuration
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER")
LLM_MODEL = os.getenv("LLM_MODEL")

# Generic configuration
PORT = os.getenv("PORT")
SECRET_KEY = os.getenv("SECRET_KEY")
