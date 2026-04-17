"""
Data resources — expose static content or dynamic data via MCP resources.
"""


def register(mcp):

    @mcp.resource("mission-control://info")
    def server_info() -> str:
        """Returns basic info about this MCP server."""
        return (
            "Mission Control MCP Server\n"
            "A polished voice and operations assistant demo.\n"
            "Built with FastMCP."
        )
