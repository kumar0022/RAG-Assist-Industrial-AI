import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"
EMB_DIM = 1536

if not API_KEY:
    raise ValueError("API_KEY not found. Set it in .env file.")