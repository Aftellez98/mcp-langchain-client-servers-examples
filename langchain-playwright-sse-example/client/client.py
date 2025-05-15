import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from llm import initialize_openai

message = """What is imbd most popular movies?"""


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8931/sse",
                "transport": "sse",
            },
        }
    ) as client:
        
        agent = create_react_agent(model=model, tools=client.get_tools())

        math_response = await agent.ainvoke({"messages": message})
        print(math_response)


if __name__ == "__main__":
    model = initialize_openai()
    asyncio.run(main())