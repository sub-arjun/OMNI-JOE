import os

from bots.types import BotConfig

DEFAULT_LLM_CONTEXT = [
    {
        "content": {
            "role": "system",
            "content": "You are SesameBot, a friendly assistant. Keep your responses brief, when possible or not requested differently. Avoid bold and italic text formatting (**bold** and *italic*) in your responses.",
        }
    }
]


DEFAULT_BOT_CONFIG = BotConfig(
    config=[
        {"options": [{"name": "params", "value": {"stop_secs": 0.5}}], "service": "vad"},
        {
            "options": [
                {"name": "run_on_config", "value": False},
            ],
            "service": "llm",
        },
    ],
)

SERVICE_API_KEYS = {
    "gemini": os.getenv("GEMINI_API_KEY"),
    "daily": os.getenv("DAILY_API_KEY"),
}
