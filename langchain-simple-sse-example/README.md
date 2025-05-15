# **Simple LangChain Client-Server Example (Azure OpenAI)**
This is a minimal example showcasing how to use a client-server architecture with LangChain, where the client communicates with a server and utilizes an Azure OpenAI model.

## **🧩 Overview**
- Server: Handles computation or API requests.

- Client: Uses LangChain and connects to an Azure OpenAI model to send queries to the server.

⚠️ This example does not use memory, making it suitable for stateless use cases or demos.

## 🚀 **How to Run**

### Start the servers

MCP Math Server via SSE
```bash
uvicorn langchain-simple-sse-example.sse.main:app --reload
```

This will trigger the fatsapi endpoint to consume. So we will only have to run the client to test everything:

MCP Client Server
```bash
python -m langchain-simple-sse-example.client.client
```

Make sure your environment is set up with any required API keys and dependencies, especially for LangChain and Azure OpenAI.