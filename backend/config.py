"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-4.1",                  # OpenAI's latest flagship
    "google/gemini-2.5-pro-preview",   # Google's latest (1st on LMArena)
    "anthropic/claude-opus-4.5",       # Anthropic's frontier model
    "anthropic/claude-sonnet-4",       # Anthropic's fast model (for diversity)
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "anthropic/claude-opus-4.5"  # Best reasoning model

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
