import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load the .env file from the backend directory for local development.
# Render environment variables take precedence over .env values.
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path, override=False)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY environment variable is not configured."
    )

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    streaming=True,
    api_key=api_key,
)
