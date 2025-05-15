import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from llm import initialize_azure_model

async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["langchain-multi-server/servers/math_server.py"],
                "transport": "stdio",
            },
            "text": {
                "command": "python",
                "args": ["langchain-multi-server/servers/text_server.py"],
                "transport": "stdio",
            }
        }
    ) as client:
        
        agent = create_react_agent(model=model, tools=client.get_tools())

        math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
        text_response = await agent.ainvoke({"messages": "Remove the vowels from this sentence: 'Hello, my name is Andres'"})

        print(math_response)
        print(text_response)

if __name__ == "__main__":
    model = initialize_azure_model()
    asyncio.run(main())