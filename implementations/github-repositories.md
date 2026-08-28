# GitHub Implementations

Open-source GitHub repositories that implement or demonstrate LLM agents, tool calling, multi-agent workflows, and agent evaluation.

## 1. LangChain

**Repository:** https://github.com/langchain-ai/langchain

LangChain provides implementations for building LLM-powered applications and agents with support for tools, chains, and agent workflows.

**Relevance:** Useful for experimenting with chained tool-calling workflows and observing how failures can propagate between steps.

---

## 2. LangGraph

**Repository:** https://github.com/langchain-ai/langgraph

LangGraph provides a graph-based approach to building stateful agent workflows.

**Relevance:** Particularly useful for studying state transitions, checkpoints, retries, and failure recovery in multi-step agents.

---

## 3. Microsoft AutoGen

**Repository:** https://github.com/microsoft/autogen

AutoGen provides implementations for applications involving multiple AI agents that communicate and collaborate.

**Relevance:** Useful for studying inter-agent communication failures and cascading errors.

---

## 4. CrewAI

**Repository:** https://github.com/crewAIInc/crewAI

CrewAI provides an open-source framework for orchestrating multiple role-based AI agents.

**Relevance:** Useful for experimenting with sequential multi-agent task execution and coordination failures.

---

## 5. LlamaIndex

**Repository:** https://github.com/run-llama/llama_index

LlamaIndex provides tools for building LLM applications connected to external data and tools.

**Relevance:** Useful for studying retrieval-augmented and tool-augmented agent workflows.

---

## 6. WebArena

**Repository:** https://github.com/web-arena-x/webarena

WebArena provides a realistic web environment for evaluating autonomous agents performing tasks on websites.

**Relevance:** Useful for investigating long-horizon agent behavior, incorrect actions, and failures during autonomous task execution.

---

## 7. ToolLLM

**Repository:** https://github.com/OpenBMB/ToolBench

ToolBench provides resources and implementations associated with training and evaluating LLMs for real-world API/tool use.

**Relevance:** Directly related to tool selection and tool-calling reliability.

---

## Comparison

| Implementation | Main Focus | Relevance |
|---|---|---|
| LangChain | LLM agents and tools | Chained tool calling |
| LangGraph | Stateful agent workflows | State and checkpoints |
| AutoGen | Multi-agent systems | Coordination failures |
| CrewAI | Agent orchestration | Sequential workflows |
| LlamaIndex | Data-connected agents | Retrieval/tool failures |
| WebArena | Autonomous web agents | Long-horizon failures |
| ToolLLM / ToolBench | Tool/API use | Tool-calling reliability |

## What Can Be Studied Using These Implementations

These repositories can be used to investigate:

- Tool-selection errors
- Incorrect tool arguments
- State-transition failures
- Cascading errors
- Multi-agent coordination failures
- Long-horizon task failures
- Missing checkpoints
- Error recovery and verification
