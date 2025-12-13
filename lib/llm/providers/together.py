import os
from langchain_community.chat_models import ChatTogether
from lib.llm.base import BaseLLM
from config.llm import LLM_CONFIG

class TogetherLLM(BaseLLM):
    def __init__(self):
        self.llm = ChatTogether(
            model=LLM_CONFIG["model"],
            api_key=os.getenv("TOGETHER_API_KEY"),
            temperature=LLM_CONFIG["temperature"],
            max_tokens=LLM_CONFIG["max_tokens"],
            request_timeout=LLM_CONFIG["timeout"]
        )

    def invoke(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content
