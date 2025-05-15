# **LangChain Loop (No Memory)**

This example demonstrates a LangChain-based agent interacting with an MCP server using **stdio transport**. The agent operates in a loop, allowing you to make multiple requests through the terminal. As the name suggests, this implementation is stateless and does not use memory.

## **🚀 How to Run**

### **1. Start the Server**
Run the MCP server using the following command:
```bash
python -m langchain-simple-example/servers/math_server
```

2. Start the Client
Run the client script to initialize the agent:
```bash
python -m langchain-simple-example/client/client
```

3. Interact with the Agent
Once the client is running, you can interact with the agent by typing your queries in the terminal. The agent will process each query and respond accordingly. To exit the loop, type: "quit"

## ⚠️ Notes
This example uses stdio transport for communication between the client and server.
The implementation is stateless, meaning no memory is retained between requests.