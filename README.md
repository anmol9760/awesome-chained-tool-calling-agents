# Awesome Chained Tool-Calling Agents

A curated research repository focused on **Failure Modes in Chained Tool-Calling Agents Operating Without Human Checkpoints**.

This repository brings together an AI-assisted research paper, citation-integrity audit, verified scholarly references, datasets, tools, GitHub implementations, and learning resources related to the reliability, safety, security, and evaluation of autonomous LLM agents.

## Table of Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Curated Research Papers](#curated-research-papers)
  - [Agent Safety and Failure Modes](#agent-safety-and-failure-modes)
  - [Tool Use and Agent Interaction](#tool-use-and-agent-interaction)
  - [Security and Prompt Injection](#security-and-prompt-injection)
  - [Long-Horizon and Autonomous Agents](#long-horizon-and-autonomous-agents)
  - [Verification and Human Oversight](#verification-and-human-oversight)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [License](#license)

---

## Overview

Large Language Model (LLM) agents can perform tasks by planning actions, calling external tools, processing tool outputs, and using the results to determine subsequent actions. In a chained tool-calling system, an early mistake can therefore influence multiple later steps. When human checkpoints are removed, these errors may continue through the workflow before being detected.

Failure modes in such systems include reasoning and planning errors, incorrect tool selection, invalid tool parameters, memory and context degradation, coordination failures between agents, and security problems such as indirect prompt injection. Long-horizon autonomous execution also makes failures more difficult to detect and attribute because several actions may depend on an earlier incorrect state.

Research has therefore moved beyond simple task-success measurements toward agent safety benchmarks, failure taxonomies, tool-use evaluation, security testing, and methods for identifying the root cause of failures. Benchmarks such as AgentBench and WebArena examine agents in interactive environments, while work such as ReAct, Gorilla, ToolLLM, and ToolEmu investigates reasoning, tool use, and tool-related risks.

Human oversight is another important direction. Instead of allowing an agent to operate completely unchecked, verification gates, risk-based oversight, and intermediate checkpoints can be used for higher-risk actions.

This repository organizes research and practical resources around these problems to help students and researchers understand, evaluate, and improve the reliability and safety of chained LLM agents.

---

## AI-Assisted Research Paper

### Failure Modes in Chained Tool-Calling Agents Operating Without Human Checkpoints

**A Systematic Review of Reliability, Safety, and Oversight Gaps in Autonomous Multi-Step LLM Agents**

The AI-assisted research paper reviews failure modes that can occur when autonomous LLM agents plan, invoke external tools, and chain the results of one action into subsequent actions without intermediate human review.

The paper organizes failures around reasoning and planning, tool use and parameter errors, memory and context degradation, and multi-agent coordination failures. It also discusses security threats, long-horizon execution, mitigation strategies, verification, and human oversight.

**[Read the AI-Assisted Research Paper](paper/AI_Assisted_Research_Paper.pdf)**

---

## Citation Integrity Audit

The AI-generated research paper originally contained **25 references**. A systematic sample of **10 references** was selected and audited for publication existence, metadata, identifiers, and claim-citation support.

The audit found:

- 7 references fully verified
- 3 references with metadata problems
- 0 Frankenstein references
- 0 fabricated references
- 0 identifier mismatches
- Authenticity Score: **92.5/100**

The main problem observed was incomplete or incorrect author metadata even when the cited publication itself existed. All 10 audited publications were found to exist, and the checked references supported their associated claims.

**[View the Citation Integrity Audit](citation-audit/Citation_Integrity_Audit.pdf)**

---

# Curated Research Papers

The repository contains verified scholarly resources related to the failure, evaluation, safety, security, and oversight of LLM-based agents.

**[View the complete reference collection](references/references.md)**

## Agent Safety and Failure Modes

- **Agent-SafetyBench: Evaluating the Safety of Large Language Model Agents**  
  Evaluates safety-related behaviors and failure modes in LLM agents.

- **Why Do Multi-Agent LLM Systems Fail?**  
  Studies recurring failure patterns in multi-agent LLM systems.

- **AgentErrorTaxonomy**  
  Organizes failure modes across planning, tool use, memory, and reflection components.

- **Identifying the Risks of LM Agents with an LM-Emulated Sandbox (ToolEmu)**  
  Provides a sandbox-based approach for investigating risks associated with language-model agents.

- **StepFinder: A Temporal Semantic Framework for Failure Attribution in Multi-Agent Systems**  
  Addresses the problem of identifying and attributing failures in multi-agent execution traces.

## Tool Use and Agent Interaction

- **ReAct: Synergizing Reasoning and Acting in Language Models**  
  Introduces an approach that combines reasoning with external actions.

- **Toolformer: Language Models Can Teach Themselves to Use Tools**  
  Investigates how language models can learn when and how to invoke external tools.

- **Gorilla: Large Language Model Connected with Massive APIs**  
  Studies reliable API and tool invocation by language models.

- **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs**  
  Investigates large-scale real-world API and tool use.

- **Reflexion: Language Agents with Verbal Reinforcement Learning**  
  Explores self-reflection as a mechanism for improving language-agent performance.

## Security and Prompt Injection

- **InjectAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents**  
  Evaluates indirect prompt injection attacks against tool-integrated agents.

- **From Prompt Injections to Protocol Exploits**  
  Examines security risks created by interactions between LLMs, tools, and external inputs.

- **Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?**  
  Examines limitations of defenses against indirect prompt injection.

- **Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents**  
  Studies adaptive attacks and defenses for prompt-injection scenarios.

- **Domain-Conditioned Safety in Frontier Computer-Using Agents**  
  Evaluates safety behavior in computer-using autonomous agents.

## Long-Horizon and Autonomous Agents

- **AgentBench: Evaluating LLMs as Agents**  
  Provides interactive environments for evaluating LLM agents.

- **WebArena: A Realistic Web Environment for Building Autonomous Agents**  
  Evaluates autonomous agents on realistic web-based tasks.

- **Measuring AI Ability to Complete Long Software Tasks**  
  Studies the ability of AI agents to complete increasingly long software tasks.

- **The Long-Horizon Task Mirage?**  
  Investigates reliability problems that emerge during long-horizon agent execution.

- **τ²-bench**  
  Provides an environment for evaluating tool-using agents in realistic tasks.

## Verification and Human Oversight

- **Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents**  
  Investigates deterministic verification gates for tool-using agents.

- **Risk-Based Framework for AI and Human Oversight**  
  Discusses risk-based approaches for assigning appropriate levels of human oversight.

- **Levels of Autonomy for AI Agents**  
  Provides a framework for understanding different levels and roles of human involvement.

- **SHIELDA: Structured Handling of Exceptions in LLM-Driven Agentic Workflows**  
  Focuses on structured exception handling in agentic workflows.

The complete collection contains the required scholarly references with bibliographic information and relevance descriptions in [`references/references.md`](references/references.md).

---

## Datasets

Datasets and benchmarks are useful for evaluating agent safety, tool use, long-horizon execution, and failure behavior.

**[View Datasets and Benchmarks](datasets/datasets.md)**

Key resources include:

- **Agent-SafetyBench** — Benchmark for evaluating safety of LLM agents.
- **AgentBench** — Interactive benchmark for evaluating LLMs as agents.
- **ToolEmu** — Sandbox-based resource for investigating risks in tool-using agents.
- **ToolBench** — Resources for evaluating large-scale API and tool use.
- **WebArena** — Realistic environment for evaluating autonomous web agents.
- **METR Long-Horizon Evaluations** — Resources for measuring AI performance on long software tasks.

---

## Tools and Libraries

Useful frameworks for building and experimenting with LLM-based agents include:

- **LangChain** — Framework for developing LLM applications and tool-using agents.
- **LangGraph** — Framework for building stateful, graph-based agent workflows.
- **AutoGen** — Framework for developing multi-agent applications.
- **CrewAI** — Framework for orchestrating role-based AI agents.
- **LlamaIndex** — Framework for connecting LLM applications with external data and tools.

**[View Tools and Libraries](tools/tools.md)**

---

## GitHub Implementations

Open-source implementations provide practical environments for experimenting with agent workflows and evaluating agent behavior.

- **LangChain** — LLM applications, agents, and tool calling.
- **LangGraph** — Stateful agent workflows and graph-based execution.
- **AutoGen** — Multi-agent communication and collaboration.
- **CrewAI** — Multi-agent orchestration.
- **LlamaIndex** — Data-connected LLM applications.
- **WebArena** — Autonomous web-agent evaluation environment.
- **ToolBench / ToolLLM** — Tool and API-use resources.

**[View GitHub Implementations](implementations/github-repositories.md)**

---

## Tutorials and Learning Resources

Learning resources for understanding and implementing LLM agents include:

- **Hugging Face Agents Course** — Practical introduction to AI agents and tools.
- **LangChain Documentation** — Tutorials and documentation for LLM applications and agents.
- **LangGraph Documentation** — Resources for stateful agent workflows.
- **Microsoft AutoGen Documentation** — Documentation for multi-agent applications.
- **LlamaIndex Documentation** — Tutorials for data-connected LLM applications.
- **ReAct** — Research resource for reasoning-and-acting agents.
- **Toolformer** — Research resource for tool-using language models.
- **WebArena** — Research and resources for autonomous web-agent evaluation.

**[View Tutorials and Learning Resources](tutorials/tutorials.md)**

---

## Research Themes

The resources in this repository can be explored through the following themes:

1. Agent safety and reliability
2. Tool selection and parameter errors
3. Cascading and compounding failures
4. Multi-agent coordination
5. Prompt injection and security
6. Long-horizon autonomous execution
7. Failure attribution
8. Verification and recovery
9. Human checkpoints
10. Risk-based autonomy

---

## Repository Structure

```text
awesome-chained-tool-calling-agents/
│
├── README.md
├── LICENSE
│
├── citation-audit/
│   └── Citation_Integrity_Audit.pdf
│
├── datasets/
│   └── datasets.md
│
├── implementations/
│   └── github-repositories.md
│
├── paper/
│   └── AI_Assisted_Research_Paper.pdf
│
├── references/
│   └── references.md
│
├── tools/
│   └── tools.md
│
└── tutorials/
    └── tutorials.md
