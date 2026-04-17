"""
Mission Control MCP Server — Entry Point
Run with: uv run mission_control
"""

import os

from mcp.server.fastmcp import FastMCP
from mission_control.tools import register_all_tools
from mission_control.prompts import register_all_prompts
from mission_control.resources import register_all_resources
from mission_control.config import config

MCP_HOST = os.getenv("MCP_HOST", "127.0.0.1")
MCP_PORT = int(os.getenv("MCP_PORT", "8000"))

# Create the MCP server instance
mcp = FastMCP(
    name=config.SERVER_NAME,
    instructions=(
        "You are Mission Control, a polished operations assistant. "
        "You have access to a set of tools to help the user. "
        "Be concise, accurate, and operationally sharp."
    ),
    host=MCP_HOST,
    port=MCP_PORT,
)

# Register tools, prompts, and resources
register_all_tools(mcp)
register_all_prompts(mcp)
register_all_resources(mcp)

def main():
    mcp.run(transport='sse')

if __name__ == "__main__":
    main()
