from dotenv import load_dotenv
load_dotenv()
import os
from agents import AsyncOpenAI,OpenAIChatCompletionsModel

gemini_provider = AsyncOpenAI(
    api_key=os.getenv("gemini_api_key"),base_url=os.getenv("base_url")
)
gemini_model = OpenAIChatCompletionsModel(
    model=os.getenv("gemini_model"),openai_client=gemini_provider
    )
