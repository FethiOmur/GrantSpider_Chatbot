"""
Configuration settings - OpenRouter integration for DeepSeek R1
"""

import os
from typing import Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Define project root directory
PROJECT_ROOT = Path(__file__).parent.parent

class Settings:
    """Application configuration settings"""
    
    # API Keys - OpenAI Direct API
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    

    
    # Model settings - OpenAI
    DEFAULT_LLM_MODEL: str = os.getenv("LLM_MODEL", "o4-mini")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "o4-mini")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    
    # Vector database settings
    VECTOR_DB_TYPE: str = "chromadb"  # chromadb, faiss
    VECTOR_DB_PATH: str = str(PROJECT_ROOT / "data" / "db")  # Absolute path
    
    # PDF processing settings
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "200"))
    
    # Application settings
    MAX_CHAT_HISTORY: int = 50
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Additional settings for OpenRouter
    OPENROUTER_APP_NAME: str = os.getenv("OPENROUTER_APP_NAME", "GrantSpider")
    OPENROUTER_SITE_URL: str = os.getenv("OPENROUTER_SITE_URL", "https://github.com/your-username/GrantSpider")

settings = Settings()

# SETTINGS alias for backward compatibility
SETTINGS = settings 