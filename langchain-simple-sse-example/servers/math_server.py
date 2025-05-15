from mcp.server.fastmcp import FastMCP

# Create FastMCP instance
mcp = FastMCP("Math")

# Register tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def magic_number() -> int:
    """Return the magic number"""
    return 5


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="sse")