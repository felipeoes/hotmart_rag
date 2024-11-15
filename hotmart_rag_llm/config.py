""" CONSTANTS AND CONFIGURATIONS """
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Constants
DB_API_SEARCH_ENDPOINT = "database/search"

# Environment variables
DB_API_HOST = os.getenv("DB_API_HOST")
DB_API_PORT = int(os.getenv("DB_API_PORT"))

RAG_LLM_FASTAPI_PORT = int(os.getenv("RAG_LLM_FASTAPI_PORT"))
RAG_LLM_FASTAPI_HOST = os.getenv("RAG_LLM_FASTAPI_HOST")
print(f"RAG_LLM_FASTAPI_PORT: {RAG_LLM_FASTAPI_PORT}")
print(f"RAG_LLM_FASTAPI_HOST: {RAG_LLM_FASTAPI_HOST}")

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
SYSTEM_MESSAGE = os.getenv("SYSTEM_MESSAGE")
TEMPERATURE = float(os.getenv("TEMPERATURE"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
SEED = int(os.getenv("SEED"))
