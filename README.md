# Your First Agent

> 如果你想快速运行，那么只需要看代码部分就可以了！

一个面向 **完全不写过代码 / 只会一点点 Python** 的入门项目，  
帮你从零理解「什么是 Agent、什么是 MCP」，并用多种框架实现通用型 Agent 示例（统一使用 MCP 工具层）。

## 📖 项目简介

本项目的目标是：

- 用**尽量科普化**的方式解释：LLM、Agent、MCP 是什么，它们在真实应用里各自干什么。
- 用**统一的任务和统一的 MCP 工具**，对比不同 Agent 框架的「手感」和工程差异。
- 帮你建立一个**工程化视角**：什么时候用单 Agent，什么时候用多 Agent，什么时候只要「一个 Agent + 多工具」就够了。

在这个项目里，我们会用一个**三层的视角**来理解 Agent 规模：

- **第 1 层：单 Agent，完成一个清晰任务**（例如：问答助手、长文本总结助手）。
- **第 2 层：小型多 Agent 协作**（例如：检索 Agent → 分析 Agent → 汇总 Agent）。
- **第 3 层：带 MCP 工具的复杂流程**（可以是多 Agent 协作，也可以是一个 Agent + 多工具按步骤调用）。

我们在所有示例中都坚持两件事：

- **统一工具协议：使用 MCP（Model Context Protocol）作为工具层接口**，所有框架共用同一套 MCP 工具（例如财经新闻 MCP）。
- **统一包管理：使用 `uv` 管理依赖**，在项目根目录用一条 `uv sync` 搞定环境。

更详细的路线和规划可以参考仓库中的 `TODO.md`。

## 📚 导读与目录（持续演进中）

### 第 0 章：环境准备 & 基础概念

导言部分集中在 `00_导言/` 目录：

- `00_导言/01_环境配置.md`
  - 帮你完成：安装 Python、安装 `uv`、在根目录执行 `uv sync`。
- `00_导言/02_什么是 Agent.md`
  - 用生活化例子解释：AI、Agent 是什么；Agent 有哪些能力；单 Agent / 多 Agent 是怎么回事。
- `00_导言/03_什么是 MCP.md`
  - 用「USB‑C 接口」「按钮」等比喻解释 MCP：为什么要有统一工具层，为什么本项目所有框架都共用 MCP 工具。

从这里开始，后面的第 1 / 2 / 3 章，刚好对应前面提到的三层视角：

- 第 1 章 ≈ 第 1 层「单 Agent 任务」
- 第 2 章 ≈ 第 2 层「小型多 Agent 协作」
- 第 3 章 ≈ 第 3 层「带 MCP 工具的复杂流程」

### 第 1 章：任务导向型单 Agent 示例（规划中）

> 目录规划：`01_single_agent_examples/`

- 围绕若干清晰的小任务（例如「整理长文本要点」「结合财经新闻 MCP 做问答 / 解读」），  
  用不同框架分别实现一个「任务导向型单 Agent」。
- 通过「同一任务，不同框架」的方式，让你直观感受各框架的使用体验和代码结构差异。

### 第 2 章：小型多 Agent 协作（规划中）

> 目录规划：`02_multi_agent_team/`

- 设计 2–3 个 Agent 协作的小团队（例如：检索 Agent → 分析 Agent → 汇总 Agent），  
  体会「什么时候一个 Agent 就够，什么时候拆成多个更合适」。

### 第 3 章：带 MCP 工具的复杂流程（规划中）

> 目录规划：`03_tool_rich_pipeline/`

- 结合多个 MCP 工具（如财经数据、知识库、模板渲染等），  
  搭建一个更接近真实生产环境的多步骤流程。

### 第 4 章以后：对比与工程化（规划中）

> 目录规划：`04_framework_comparison/`、`05_engineering_maintenance/` 等

- 汇总不同框架在上手难度、多 Agent 支持、工程化能力、生态等方面的差异。
- 讨论日志、简单评估、部署和依赖维护等工程化话题。

> 由于项目仍在早期建设阶段，以上章节会逐步补齐，具体结构以仓库实际目录为准。

## 🚀 快速开始

### 环境要求

- Python >= 3.12（仓库中 `pyproject.toml` 要求 `>=3.12`）
- [uv](https://github.com/astral-sh/uv)（**本项目统一使用 `uv` 管理依赖**）

### 1. 安装依赖

在仓库根目录执行：

```bash
uv sync
```

这会根据根目录的 `pyproject.toml` / `uv.lock` 自动创建虚拟环境并安装所有依赖。

### 2. 配置环境变量

本项目会使用 `.env` 文件统一管理各类 API Key（如 OpenAI、通义千问等）。  
后续会提供 `.env.example`，你可以参考示例复制一份：

```bash
cp .env.example .env
```

然后在 `.env` 中填入自己的 API Key，示例（仅作占位说明）：

```bash
OPENAI_BASE_URL=your_base_url
OPENAI_API_KEY=your_api_key
MODEL=your_model_name
```

代码会通过 `python-dotenv` 自动加载这些配置。

### 3. 运行示例

推荐始终通过 `uv run` 来执行脚本或启动 Notebook，例如：

```bash
# 运行某个 Python 脚本
uv run python path/to/your_script.py

# 启动 Jupyter Notebook
uv run jupyter notebook
```

然后在浏览器中打开对应的 `.ipynb` 文件即可。

## 🛠️ 技术栈（持续演进中）

- **Agent / 应用框架（计划覆盖）**：

  - [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
  - [LangChain](https://docs.langchain.com/)
  - LangGraph / CrewAI / Autogen / ADK / Pydantic-AI 等（视精力逐步补充）

- **工具协议 & 实现**：

  - [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
  - 本仓库中的 MCP 服务器（例如财经新闻 MCP，位于 `mcp_servers/`）

- **基础工具**：
  - Python 3.12+
  - [uv](https://github.com/astral-sh/uv)（包管理 + 虚拟环境）
  - Jupyter Notebook（可选，用于交互式体验）

## 📁 当前项目结构（节选）

> 仅列出与导言和 MCP 相关的核心目录，后续章节会按 `TODO.md` 规划逐步补齐。

```
your-first-agent/
├── 00_导言/                  # 环境配置 & 基础概念（环境 / Agent / MCP）
│   ├── 01_环境配置.md
│   ├── 02_什么是 Agent.md
│   └── 03_什么是 MCP.md
├── mcp_servers/              # MCP 服务器实现（如财经新闻 MCP）
├── pyproject.toml            # 项目依赖（由 uv 管理）
├── TODO.md                   # 项目路线 & 执行计划
└── README.md                 # 当前文档
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
