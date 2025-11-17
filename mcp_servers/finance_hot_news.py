"""
This is a MCP server that provides the latest finance news.
"""

import requests

from fastmcp import FastMCP

mcp_server = FastMCP("finance-news")


@mcp_server.tool(
    name="get-cls-hot-news",
    description="get the latest finance hot news from cls.cn",
)
def get_cls_hot_news():
    """
    Get the latest finance hot news from cls.cn
    """
    response = requests.get("https://api.98dou.cn/api/hotlist/cls/all", timeout=30)
    if response.status_code != 200:
        return "Failed to get the latest finance hot news from cls.cn"
    return response.json()


if __name__ == "__main__":
    mcp_server.run(transport="stdio")
