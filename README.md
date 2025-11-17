# Your First Agent

一个全面的 Agent 开发框架横向比较项目，帮助你理解不同框架的差异，并选择最适合你需求的 Agent 开发方案。

## 📖 项目简介

本项目旨在通过实际案例对比不同 Agent 开发框架的特点、使用方式和最佳实践。我们使用统一的工具协议（MCP - Model Context Protocol）来确保公平比较，让你能够直观地看到各个框架的优缺点。

### 🎯 项目目标

- **横向比较**：对比主流 Agent 开发框架（OpenAI Agents SDK、LangChain、ADK 等）
- **统一标准**：使用 MCP 作为工具协议，确保比较的公平性
- **实践导向**：通过实际案例学习，而非纯理论讲解
- **易于上手**：提供清晰的代码示例和详细说明

## 📚 章节目录

### [第 0 章：导言](./00-course-setup/)

介绍 Agent 开发的基础概念和核心协议：

- **什么是 Agent？** - Agent 的基本概念、工作原理和应用场景
- **什么是 MCP？** - Model Context Protocol 的介绍，为什么选择 MCP 作为统一工具协议

### [第 1 章：搭建简单 Agent](./01-simple-agent/)

通过一个简单的财经新闻分析 Agent 案例，展示如何使用不同框架实现相同的功能：

- **特点**：
  - 以单个任务为导向（获取最新财经新闻并生成分析报告）
  - 使用 MCP 作为外接工具的统一协议
  - 对比多个框架的实现方式

- **涵盖框架**：
  - OpenAI Agents SDK
  - LangChain
  - ADK (Agent Development Kit)

## 🚀 快速开始

### 环境要求

- Python >= 3.12
- [uv](https://github.com/astral-sh/uv) (推荐) 或 pip

### 安装依赖

```bash
# 使用 uv (推荐)
uv sync
```

### 配置环境变量

创建 `.env` 文件并配置你的 API 密钥：

```bash
OPENAI_BASE_URL=your_base_url
OPENAI_API_KEY=your_api_key
MODEL=your_model_name
```

### 运行示例

每个章节都包含独立的 Jupyter Notebook，你可以直接运行：

```bash
# 启动 Jupyter
jupyter notebook

# 或使用 VS Code 打开对应的 .ipynb 文件
```

## 🛠️ 技术栈

- **Agent 框架**：
  - [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
  - [LangChain](https://docs.langchain.com/)
  - ADK (Agent Development Kit)

- **工具协议**：
  - [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
  - [FastMCP](https://gofastmcp.com/)

- **开发工具**：
  - Python 3.12+
  - Jupyter Notebook
  - uv (包管理)

## 📁 项目结构

```
your-first-agent/
├── 00-course-setup/          # 第 0 章：导言
│   ├── 01-what-is-agent.md   # Agent 介绍
│   └── 02-what-is-mcp.md     # MCP 介绍
├── 01-simple-agent/          # 第 1 章：简单 Agent
│   ├── 01-openai.ipynb       # OpenAI Agents SDK 示例
│   ├── 01-langchain.ipynb     # LangChain 示例
│   └── 02-adk.ipynb           # ADK 示例
├── mcp_servers/               # MCP 服务器实现
│   └── finance_hot_news.py    # 财经新闻 MCP 工具
└── README.md                  # 项目说明
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 [MIT License](LICENSE) 许可证。

MIT License 是一个宽松的开源许可证，允许你：
- ✅ 自由使用、修改、分发代码
- ✅ 用于商业项目
- ✅ 私有使用

唯一的要求是保留原始的版权声明和许可证文本。

## 🔗 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io/)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- [LangChain 文档](https://docs.langchain.com/)

---

⭐ 如果这个项目对你有帮助，欢迎给个 Star！

