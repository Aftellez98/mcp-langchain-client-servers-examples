# **LangChain Multi-Server (No Memory)**

This example demonstrates a LangChain-based agent interacting with **two MCP servers** simultaneously using **stdio transport**. The implementation is stateless, with no memory retained between requests.

## **🚀 How to Run**

### **1. Start the Servers**
Run both MCP servers using the following commands (update the paths to your server scripts as needed):

**Server 1:**
```bash
python -m langchain-multi-server/servers/math_server
```

**Server 2:**
```bash
python -m langchain-simple-example/servers/text_server
```

### **2. Start the Client**
Run the client script to initialize the agent and connect to both servers:
```bash
python -m langchain-multi-server/client/client
```