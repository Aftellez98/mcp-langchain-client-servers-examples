import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_openai import AzureChatOpenAI, ChatOpenAI

load_dotenv()


def initialize_azure_model(temperature: float = 0.0) -> AzureChatOpenAI:
    """
    Initializes the Azure OpenAI model with the specified temperature.
    Args:
        temperature (float): The temperature for the model. Default is 0.0.
    Returns:
        AzureChatOpenAI: An instance of the AzureChatOpenAI model.
    """
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

def initialize_openai(temperature: float = 0.0) -> ChatOpenAI:
    llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo", temperature=temperature)
    return llm