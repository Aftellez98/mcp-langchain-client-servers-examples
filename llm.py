import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI

load_dotenv()


def initialize_azure_model(temperature: float = 0.0) -> AzureChatOpenAI:
    llm = AzureChatOpenAI(
        azure_deployment="gpt-4",
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    return llm


def initialize_ollama() -> ChatOllama:
    return ChatOllama(model="llama3")
