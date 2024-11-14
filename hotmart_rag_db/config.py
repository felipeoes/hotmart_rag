""" CONSTANTS AND CONFIGURATIONS """
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Constants
DATA_DIR = Path("data")
DB_DIR = DATA_DIR / "db"
MODELS_DIR = DATA_DIR / "models"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Environment variables
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT"))
FASTAPI_HOST = os.getenv("FASTAPI_HOST")

CHROMA_HOST = os.getenv("CHROMA_HOST")
CHROMA_PORT = os.getenv("CHROMA_PORT")
CHROMA_CLIENT_AUTH_CREDENTIALS = os.getenv("CHROMA_CLIENT_AUTH_CREDENTIALS")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME")
CHROMA_EMBEDDING_MODEL = os.getenv("CHROMA_EMBEDDING_MODEL")