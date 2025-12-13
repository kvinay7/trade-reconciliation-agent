from config.llm import LLM_CONFIG
from lib.llm.providers.together import TogetherLLM
from lib.llm.providers.openai import OpenAILLM

def get_llm():
    provider = LLM_CONFIG["provider"]

    if provider == "together":
        return TogetherLLM()

    if provider == "openai":
        return OpenAILLM()

    raise ValueError(f"Unsupported LLM provider: {provider}")
