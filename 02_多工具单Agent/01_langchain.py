"""
使用 langchain 搭建一个带有多个工具的单 Agent 应用
"""

import os
import asyncio
from dotenv import load_dotenv

from rich.console import Console
from rich.markdown import Markdown

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient  # type: ignore

# 初始化一个llm，可以去glm注册一个，他有一款免费的大模型用
# 然后配到项目的.env中
load_dotenv()
model = os.getenv("MODEL", "")
api_key = os.getenv("API_KEY", "")
base_url = os.getenv("BASE_URL", "")

# 我使用的是豆包的大模型，和glm都会遵守openai api 规范，所以可以用langchain_openai的拓展
llm = ChatOpenAI(
    model=model,
    api_key=api_key,  # type: ignore
    base_url=base_url,
    extra_body={"thinking": {"type": "disabled"}},  # 我用的是doubao-seed，不想让他思考
    timeout=60,
)

# 初始化mcp客户端
mcp_client = MultiServerMCPClient(
    {
        "finance": {
            "command": "python",
            "args": ["mcp_servers/finance.py"],
            "transport": "stdio",
        },
    }
)
