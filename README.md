# **MCP Experiments with LangChain**

This repository showcases my experiments with Model Context Protocols (MCPs). While MCPs are intriguing, I firmly believe that **Chainlit** remains the go-to standard for AI-driven products. Chainlit's flexibility and robustness make it unparalleled in building AI applications.

That said, these experiments serve as a foundation for future MCP projects. They demonstrate various use cases of MCPs using LangChain, focusing on stateless implementations without memory.

## **🧩 Included Examples**

1. **Simple MCP with Standard Transport**  
   A minimal example of an MCP server using standard transport (stdio).

2. **MCP Server with HTTP SSE**  
   An example of an MCP server mounted and consumed via HTTP Server-Sent Events (SSE).

3. **Handling Multiple MCP Servers**  
   A demonstration of interacting with multiple MCP servers simultaneously.

4. **MCP in a Loop**  
   An interactive example showcasing an MCP client running in a loop.

⚠️ **Note:** None of these examples use memory, making them suitable for stateless use cases or demos.

## **🚀 How to Run**

Each example is self-contained and can be executed independently. Refer to the respective directories for detailed instructions.

These experiments are just the beginning of my journey with MCPs, and I look forward to building more complex and robust systems in the future.

## **📦 Poetry Environment Setup**

This project uses [Poetry](https://python-poetry.org/) for dependency management. Follow the steps below to set up the environment:

1. **Ensure Python 3.11+ is installed**  
   Verify that Python 3.11 or higher is installed on your system. You can check your Python version with:
   ```bash
   python3 --version
   ```

2. **Ensure Poetry is installed**  
   Verify that Poetry is installed with:
   ```bash
   poetry --version
   ```

3. **Install dependencies**  
   Verify that Poetry is installed with:
   ```bash
   poetry install
   ```