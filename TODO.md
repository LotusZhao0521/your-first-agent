## 项目路线 & 执行计划（your-first-agent）

> 目的：帮助你快速了解「这个项目能学什么、怎么学」，同时也记录作者/贡献者的开发计划，方便后续维护与扩展（也方便 Cursor 恢复上下文）。

---

### 1. 项目整体目标（你能学到什么）

- **面向对象**：完全不懂代码的小白。
- **核心场景**：内容生产团队（主编 / 资料检索 / 写作 / 审稿 等多 Agent 协作）。
- **对比框架**：LangChain、LangGraph、CrewAI、openai-agents-sdk。
- **技术栈约定**：Python + `uv` 做包管理；统一在根目录管理依赖。
- **最终形态**：一个 GitHub 仓库 + 配套文档，读者只需复制命令即可体验从单 Agent 到多 Agent 内容生产流水线。

---

### 2. 分阶段大计划（高层路线）

- **第 0 层：环境准备 & 基础概念（目录：`00_fundamentals/`）**
  - 用图文 + 极简代码，让小白完成：
    - 安装 Python 与 `uv`，并能在根目录执行 `uv sync`。
    - 运行第一个 LLM 调用脚本（体验「模型会说话」）。
    - 用内容生产团队的故事理解：LLM、Agent、多 Agent 协作的基本概念。

- **第 1 层：单 Agent「智能小编辑」（目录：`01_single_agent_editor/`）**
  - 统一任务：输入一段文本 → 输出润色结果 + 3 个标题 + 一句读者画像描述。
  - 在多个框架中分别实现一个「单 Agent 小编辑」，让读者体验不同框架的“手感”。

- **第 2 层：小型内容团队（2–3 个 Agent 协作）（目录：`02_small_content_team/`）**
  - 场景：资料检索 Agent + 写作 Agent + 审稿 Agent 的迷你内容团队。
  - 先在多 Agent 友好的框架（如 CrewAI / LangGraph）实现，再扩展到其他框架。

- **第 3 层：完整内容生产流水线（复杂多 Agent + 工具）（目录：`03_full_content_pipeline/`）**
  - 场景：输入「主题 + 目标读者 + 平台」，输出：
    - 长文（公众号/小红书）。
    - 几条短视频脚本。
    - 审稿报告（逻辑/风格问题）。
  - 引入工具（搜索/向量检索/模板），展示更接近真实生产环境的工作流。

- **第 4 层：跨框架对比与选型（目录：`04_framework_comparison/`）**
  - 整理不同框架在：
    - 上手难度
    - 多 Agent 支持
    - 工程化能力
    - 生态/文档
  - 上的优缺点，对小白给出选型建议。

- **第 5 层：工程化 & 可持续维护（目录：`05_engineering_maintenance/`）**
  - 记录日志、简单评估、部署方式（本地脚本/命令行/简单服务）。
  - 制定依赖版本更新和文档更新的流程（如每季度扫一遍主要框架的 release）。

---

### 3. 当前开发任务（对想参与开发的人，可勾选）

- [ ] **搭建基础工程与环境层**
  - [ ] 在根目录补全 `pyproject.toml`，统一声明：LangChain、LangGraph、CrewAI、openai-agents-sdk 等依赖。
  - [ ] 使用 `uv` 初始化环境，确认 `uv sync` 正常工作。
  - [ ] 添加 `.env.example`，约定 API Key 等环境变量写法。
  - [ ] 创建 `00_fundamentals/` 目录结构：
    - [ ] `01_install_python_uv.md`（极简安装指南，面向完全小白）。
    - [ ] `02_first_llm_call.py`（第一次调用 LLM 的脚本）。
    - [ ] （可选）`03_first_llm_call.ipynb`（Notebook 版本）。
    - [ ] `04_what_is_agent.md`（用内容团队故事讲解 Agent 概念）。

- [ ] **选择并实现第一个框架的 Level 1（单 Agent 智能小编辑）**
  - [ ] 选定第一个主打框架（建议：CrewAI 或 LangChain）。
  - [ ] 创建 `01_single_agent_editor/<framework>/main.py`，实现：
    - 输入一段原始文本。
    - 输出：润色结果 + 3 个标题 + 一句读者画像描述。
  - [ ] 在 `01_single_agent_editor/<framework>/README.md` 中，用小白友好语言解释：
    - 如何运行（`uv run python ...`）。
    - 每一段代码大致在做什么。
    - 读者可以安全修改的部分（如角色描述、语气、平台）。

- [ ] **在第二个框架中复刻单 Agent 智能小编辑**
  - [ ] 选择第二个框架（在：LangChain / CrewAI / LangGraph / openai-agents-sdk 中选一个与第一个不同的）。
  - [ ] 同样实现 `main.py` + `README.md`，保证任务行为一致（便于对比）。

- [ ] **开始设计和实现「小型内容团队」场景**
  - [ ] 在 `02_small_content_team/` 下建立框架子目录（优先 CrewAI / LangGraph）。
  - [ ] 设计三角色协作流程：资料检索 Agent → 写作 Agent → 审稿 Agent。
  - [ ] 写出第一版 `main.py`，可以先用简单串行流程（不追求复杂控制）。

- [ ] **统一 MCP 工具层（所有框架共用同一套工具）**
  - [ ] 在 `docs/` 中创建 `mcp_tools_plan.md`，列出需要的工具清单（如：`web_search`、`kb_query`、`file_read`、`template_render` 等）及输入/输出约定。
  - [ ] 创建 `mcp/servers/` 目录，实现基础的 `content_tools_server` MCP 服务器（按照 MCP 协议提供上述工具）。
  - [ ] 创建 `mcp/client.py`，实现通用 MCP 客户端适配器（至少包含 `call_mcp_tool(name: str, params: dict) -> dict` 之类的接口）。
  - [ ] 在 LangChain 示例中新增 `McpTool` 适配器类，将至少 1 个工具改为通过 MCP 调用。
  - [ ] 在 CrewAI 或 LangGraph 示例中复用同一个 MCP 工具，验证「跨框架共用 MCP 工具」的可行性。

---

### 4. 约定与注意事项

- **统一包管理**：所有示例通过 `uv` 管理依赖，不再使用裸 `pip`。
- **示例尽量保持「任务一致」**：同一层级（单 Agent / 小团队 / 流水线）在不同框架中尽量做同一件事情，方便对比。
- **对小白友好**：所有 README 和文档优先解释「怎么跑、能看到什么、可以改哪」，暂时不过度深入底层实现细节。
- **版本记录**：后续增加/修改依赖或框架版本时，更新：
  - 根目录的 `pyproject.toml`。
  - `05_engineering_maintenance/changelog_guide.md` 中的说明。

---

### 5. 已完成/历史记录（后续补充）

- 当前：项目处于设计与规划阶段，核心大纲已在 `TODO.md` 中记录。
- 后续：完成重要里程碑后，在此简单记录（时间 + 完成内容），方便回顾。


