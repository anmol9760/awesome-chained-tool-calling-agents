# Tools and Libraries

Tools and libraries useful for building, testing, evaluating, and monitoring LLM-based agents and tool-calling workflows.

## 1. LangChain

**LangChain** is a framework for developing applications powered by language models. It provides components for building agent workflows, tool calling, memory, and multi-step reasoning.

- GitHub: https://github.com/langchain-ai/langchain
- Documentation: https://python.langchain.com/

**Relevance:** Useful for implementing chained tool-calling agents and studying how errors propagate across multiple agent steps.

---

## 2. LangGraph

**LangGraph** is a framework for building stateful, multi-step agent workflows as graphs.

- GitHub: https://github.com/langchain-ai/langgraph
- Documentation: https://langchain-ai.github.io/langgraph/

**Relevance:** Its graph-based workflow representation is useful for designing agents with explicit states, transitions, checkpoints, and error-handling mechanisms.

---

## 3. AutoGen

**AutoGen** is a framework for creating applications involving multiple AI agents that communicate and collaborate with one another.

- GitHub: https://github.com/microsoft/autogen
- Documentation: https://microsoft.github.io/autogen/

**Relevance:** Useful for studying multi-agent interaction, communication failures, coordination problems, and cascading errors.

---

## 4. CrewAI

**CrewAI** is a framework for orchestrating role-based AI agents that collaborate to complete tasks.

- GitHub: https://github.com/crewAIInc/crewAI
- Documentation: https://docs.crewai.com/

**Relevance:** Provides a practical environment for experimenting with sequential and collaborative agent workflows.

---

## 5. LlamaIndex

**LlamaIndex** is a framework for connecting LLM applications with external data sources, tools, and retrieval systems.

- GitHub: https://github.com/run-llama/llama_index
- Documentation: https://docs.llamaindex.ai/

**Relevance:** Useful for building tool-augmented and retrieval-based agents where incorrect data retrieval or tool use can contribute to downstream failures.

---

## Comparison

| Tool / Library | Main Purpose | Relevance to Topic |
|---|---|---|
| LangChain | LLM applications and agents | Tool calling and chained workflows |
| LangGraph | Stateful agent workflows | State management and checkpoints |
| AutoGen | Multi-agent applications | Agent coordination and failures |
| CrewAI | Multi-agent orchestration | Sequential agent workflows |
| LlamaIndex | Data-connected LLM applications | Retrieval and tool-augmented agents |

## Why These Tools Matter

These frameworks provide practical environments for investigating failure modes in agentic systems, including:

- Incorrect tool selection
- Invalid tool parameters
- State-management errors
- Error propagation
- Multi-agent communication failures
- Missing verification steps
- Lack of intermediate human checkpoints
