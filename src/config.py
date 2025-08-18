import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Tavily API Key
    TAVILY_API_KEY: str = os.environ.get("TAVILY_API_KEY", "")

    # Server Port
    PORT: int = int(os.environ.get("PORT", 10000))

    def __post_init__(self):
        if not self.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY environment variable not set")

settings = Settings()