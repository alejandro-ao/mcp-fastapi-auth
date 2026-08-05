from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from typing import Dict, List

try:
    from .config import settings
except ImportError:
    from config import settings

# Create an MCP server
mcp = FastMCP("web-search")

# Initialize Tavily client
tavily_client = TavilyClient(settings.TAVILY_API_KEY)

# Add a tool that uses Tavily
@mcp.tool()
def web_search(query: str) -> List[Dict]:
    """
    Use this tool to search the web for information.

    Args:
        query: The search query.

    Returns:
        The search results.
    """
    try:
        response = tavily_client.search(query)
        return response["results"]
    except Exception as e:
        return {"error": str(e)}

