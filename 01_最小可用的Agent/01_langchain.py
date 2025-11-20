"""
使用langchain搭建一个最小可用Agent
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
    extra_body={"thinking": {"type": "disabled"}},
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


## .get_tools 是一个异步方法，并且他的输出：StructuredTool 也必须在异步环境中使用
## 所以后面全是async function
async def get_tools():
    """获取mcp客户端的工具"""
    tools = await mcp_client.get_tools()
    print("tools:", tools)
    return tools


# tools:
# [
#   StructuredTool(
#       name='get-cls-hot-news',
#       description='get the latest finance hot news from cls.cn',
#       ......
#   )
# ]


# 初始化agent，把刚才拿到的工具给agent
async def get_agent():
    """初始化agent, 绑定工具和提示词"""
    tools = await get_tools()
    system = "你是一个人工智能助手，专注于分析财经相关新闻"
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system,  # 给他一个system prompt，明确一下身份
        debug=True,  # 方便看更多信息，values表示完整的状态值，updates表示状态更新
    )  # type: ignore
    return agent


async def execute_task(task: str):
    """让绑定了工具agent去执行任务"""
    messages = {
        "messages": [
            {"role": "user", "content": task},
        ]
    }
    agent = await get_agent()
    response = await agent.ainvoke(messages)
    return response


response = asyncio.run(execute_task("帮我查一下最近的财经新闻，并且整理一下。"))

# 打印出markdown
console = Console()
md = Markdown(response["messages"][-1].content)
console.print(md)

# 这样就实现了一个能够帮你实时整理新闻的Agent，当然如果有其他数据源的话，还可以做别的事。
# 后面章节会尝试使用别的工具，让他多做一些事
