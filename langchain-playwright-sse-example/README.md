# **Simple LangChain Client-Server Example (Azure OpenAI)**
This is a minimal example showcasing how to use a client-server architecture with LangChain, where the client communicates with a playwright server and utilizes an Azure OpenAI model.

You can obtain the playwright server at: https://github.com/microsoft/playwright-mcp#

**Run:**
```bash
npm install
npm build
npx @playwright/mcp@latest --port 8931 --browser=chromium
npx @playwright/mcp@latest --browser=chrome --port=8931 

```


## **🧩 Overview**
- Server: Handles computation or API requests.

- Client: Uses LangChain and connects to an Azure OpenAI model to send queries to the server.

⚠️ This example does not use memory, making it suitable for stateless use cases or demos.

## 🚀 **How to Run**

### Start the client

MCP Client Server
```bash
python -m langchain-playwright-sse-example.client.client
```

Make sure your environment is set up with any required API keys and dependencies, especially for LangChain and Azure OpenAI.