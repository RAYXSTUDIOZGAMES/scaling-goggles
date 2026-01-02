import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "DISCORD_TOKEN": os.getenv("DISCORD_TOKEN"),
        "GEMINI_KEY": os.getenv("GEMINI_KEY"),
        "LOG_CHANNEL_ID": os.getenv("LOG_CHANNEL_ID")
    }
