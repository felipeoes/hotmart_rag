""" CONSTANTS AND CONFIGURATIONS """
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Constants
DB_API_SEARCH_ENDPOINT = "/database/search"

# Environment variables
DB_API_HOST = os.getenv("DB_API_HOST")
DB_API_PORT = int(os.getenv("DB_API_PORT"))

FASTAPI_PORT = int(os.getenv("FASTAPI_PORT"))
FASTAPI_HOST = os.getenv("FASTAPI_HOST")

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
SYSTEM_MESSAGE = os.getenv("SYSTEM_MESSAGE")
TEMPERATURE = float(os.getenv("TEMPERATURE"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
SEED = int(os.getenv("SEED"))
