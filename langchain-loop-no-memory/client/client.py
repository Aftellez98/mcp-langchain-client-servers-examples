import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import sys

from llm import initialize_azure_model

# Set up your model (Azure OpenAI or other)
model = initialize_azure_model()

# Define server parameters (update path as needed)
server_params = StdioServerParameters(
    command="python",
    args=["anthropic-simple-example/servers/math_server.py"],  # Change this to your server script
)

async def run_agent_loop():
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("✅ MCP session initialized.")

                # Load tools
                tools = await load_mcp_tools(session)
                print(f"🔧 Loaded tools: {[tool.name for tool in tools]}")

                # Create LangChain agent
                agent = create_react_agent(model=model, tools=tools)

                # Run interactive chat loop
                print("\n🧠 Agent ready! Type your query or 'quit' to exit.")
                while True:
                    query = input("\n> ").strip()
                    if query.lower() == "quit":
                        print("👋 Goodbye!")
                        break

                    try:
                        result = await agent.ainvoke({"messages": query})
                        output = result.get("output", result)
                        print(f"\n🤖 {output}")
                    except Exception as e:
                        print(f"❌ Error while processing query: {e}")

    except Exception as e:
        print(f"🚨 Error initializing agent: {e}")

if __name__ == "__main__":
    asyncio.run(run_agent_loop())
