## MCP 服务器目录（mcp_servers）

这里是项目里**统一的 MCP 工具层**，和 `00_导言/03_什么是 MCP.md` 里讲的概念一一对应：  
不同 Agent / 框架（LangChain、CrewAI、LangGraph、openai-agents-sdk 等）共用这里的 MCP 服务器，而不是各写一套工具。

---

### 1. 这里有什么？

- **`finance_hot_news.py`**
  - MCP Server 名称：`finance-news`
  - 工具：`get-cls-hot-news` → 从 `cls.cn` 聚合接口获取最新财经热点新闻（返回 JSON）

未来会在本目录继续补充其他 MCP 服务器，全部走统一 MCP 协议，并在各个框架示例中以「已经集成好的工具」形式出现，无需你单独启动或配置。
