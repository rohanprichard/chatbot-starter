from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
from backend.env import LLM_API_KEY, LLM_MODEL, LLM_PROVIDER
import logging


client = AsyncOpenAI(api_key=LLM_API_KEY)
logger = logging.getLogger(__name__)

if LLM_PROVIDER == "openai":
    client = AsyncOpenAI(api_key=LLM_API_KEY)
elif LLM_PROVIDER == "anthropic":
    client = AsyncAnthropic(api_key=LLM_API_KEY)


async def generate_response(prompt: str, messages: list[dict]):

    if LLM_PROVIDER == "openai":
        logger.info(f"Generating response with OpenAI: {LLM_MODEL}")
        stream = await client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "system", "content": prompt}] + messages,
            stream=True,
        )

    elif LLM_PROVIDER == "anthropic":
        logger.info(f"Generating response with Anthropic: {LLM_MODEL}")
        stream = await client.messages.create(
            model=LLM_MODEL,
            messages=messages,
            system=prompt,
            stream=True,
        )

    async for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        yield content
