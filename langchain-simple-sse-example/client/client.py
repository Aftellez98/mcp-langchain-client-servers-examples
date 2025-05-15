import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from llm import initialize_azure_model

async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    ) as client:
        
        agent = create_react_agent(model=model, tools=client.get_tools())

        math_response = await agent.ainvoke({"messages": "what's the magic number?"})
        print(math_response)


if __name__ == "__main__":
    model = initialize_azure_model()
    asyncio.run(main())