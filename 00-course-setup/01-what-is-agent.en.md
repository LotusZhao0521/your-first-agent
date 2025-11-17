# What is an AI Agent?

~~This chapter mainly digests Oracle's documentation; the more nutritious content is in Oracle's [post](https://www.oracle.com/cn/artificial-intelligence/ai-agents/#what-is-ai).~~

_This is a hands-on guide for application developers. Some conceptual details may deviate; here, "Agent" specifically refers to an LLM agent._

## What is AI?

[AI](https://www.oracle.com/cn/artificial-intelligence/what-is-ai/), i.e., artificial intelligence, refers to trained computing systems that can simulate human intelligence. This capability is now widely applied across many industries, such as customer service, personalized marketing, and financial assistants.

## What is an Agent?

[AI Agent](https://www.oracle.com/cn/artificial-intelligence/ai-agents/#what-are-ai-agents) refers to a system with AI capabilities that can **accept tasks**, **inspect the environment**, **execute tasks according to its role**, and **adapt its execution based on experience**.

Given specific needs, people set goals for AI agents. With a goal, the agent can use knowledge learned from training and application-specific experience to **plan**, **execute**, and **achieve the goal**.

## How an Agent Works

An agent is more like a planner; it is no longer just a tool that generates replies from prompts. An agent needs, given its assigned **goal**, to identify the tasks or steps required to achieve it.
Take a common e-commerce customer-service agent as an example. When a user asks when a specified item will arrive, the agent needs to plan its actions: query the user's specified order, check the item's real-time location, estimate the expected arrival time based on experience and context, and finally respond to the user with the useful information.

## Advantages of Agents

1. **Accuracy**: Agents can leverage large amounts of data to make decisions, getting closer to the truth.
2. **Consistency**: Compared with humans working long hours ~~(workhorses)~~, agents—or intelligent programs—tend to handle the same tasks in the same way.
3. **Cost savings**: ~~That's what Oracle says; in my workplace the situation is the opposite—R&D, labor, and other costs (servers) have already far exceeded buying an off-the-shelf solution.~~ Once agents start to deliver, they may save even more cost.
4. **Data analysis**: There are more and more tools for descriptive or inferential statistics. Let LLMs handle simple tasks and let tools handle complex ones.
5. **Personalization**: By analyzing user data, agents can remember their traits ~~(e.g., some anime fans prefer catgirls)~~ and better cater to user preferences.

## Challenges for Agents

1. **Generality**: An agent usually needs a clear identity and task, much like how it's hard to use Copilot for things other than coding.
2. **Complex tasks**: Agents are adept at simple, mechanical work, such as generating a daily summary from today's documents. As tasks become more complex—especially those requiring heavy human involvement and that are ill-defined—agents become difficult to design and maintain. For such tasks, it is important to get every step right.
3. **Dependence on high-quality data**: To ensure an agent's effectiveness and trustworthiness (for users, trust is often one of the most critical factors), the data provided to the agent must be accurate, timely, and usable.
4. **Security risks**: For users, confidentiality is also one of the most critical factors. Some things seem trivial until put on the scale; then they weigh a thousand jin. Trade secrets can be invaluable. Therefore, security teams must continuously learn new skills to ensure data does not leak by any means.

## Components of an Agent

1. **Acting**: Enables the agent to interact with the external environment, such as helping users program or write emails.
2. **Memory**: Allows the agent to remember past information; by using it appropriately, the agent can make better decisions.
3. **Reasoning**: Enables the agent to identify alternatives and make decisions based on available information.
4. **Goals and utility**: Goals define the outcomes expected of the agent; utility measures how well the agent achieves them. For example, when an agent performs personalized marketing, click-through rate can be used to measure effectiveness.
5. **Perception**: The agent can capture external information through various mechanisms, such as users' text input and voice input.

## Types of Agents

Common types in agent development include:

1. Task-oriented agents: These agents have clear tasks, such as programming and data analysis.
2. Planning and reasoning agents: These agents emphasize autonomously decomposing tasks, planning, and executing.
3. Exploration and learning agents: These agents emphasize learning through interaction with the environment and can reflect on outcomes to adjust their execution strategy.
4. Multi-agent systems: Systems composed of multiple agents, which may be any one or a combination of the above types.
