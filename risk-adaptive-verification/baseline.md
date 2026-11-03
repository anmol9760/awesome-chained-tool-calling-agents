# Baseline Documentation

## Project: Risk-Adaptive Verification for Tool-Using AI Agents

## 1. Purpose

This document identifies the research papers and reference implementation used to guide the design of the risk-adaptive verification experiment.

The project investigates whether risk-adaptive verification can reduce confirmation overhead while retaining protection against unsafe tool actions, compared with no additional verification and always-on verification.

The primary reference implementation is **AIRGuard**. Its design motivates the use of runtime checks and risk-aware enforcement before tool actions are executed.

---

## 2. Primary Reference: AIRGuard

### Research Paper

**Title:** AIRGuard: Guarding Agent Actions with Runtime Authority Control

**Authors:** Suliu Qin, Haomin Zhuang, Yujun Zhou, Yufei Han, and Xiangliang Zhang (2026).

- **Paper:** https://arxiv.org/abs/2605.28914
- **PDF:** https://arxiv.org/pdf/2605.28914

### Official GitHub Repository

https://github.com/Sophie508/AIRGuard

### Description

AIRGuard is a runtime security framework designed to protect tool-using language agents against unsafe actions, particularly actions influenced by untrusted external content.

Its architecture incorporates:

- Authority context and action-level authorization.
- Resource trust labels.
- LLM-based risk simulation.
- Tiered enforcement decisions.
- Cross-step risk auditing.
- Runtime interception of tool calls.

### Relevance to This Project

AIRGuard provides the primary architectural reference for examining runtime verification of tool-using AI agents.

The project adopts the broader idea of checking proposed actions before execution and exploring how risk information can influence verification decisions.

However, this project uses a substantially simplified experimental model. It does not reproduce AIRGuard's authority derivation, trust-labeling system, LLM-based risk simulation, or complete enforcement pipeline.

**Use in this project:** Conceptual reference and source-code inspection, not a reproduced baseline implementation.

---

## 3. Additional Research Reference: Deterministic Verification Gates

### Research Paper

**Title:** Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents

**Authors:** Vikas Reddy, Sumanth Reddy Challaram, and Abhishek Basu (2026).

- **Paper:** https://arxiv.org/abs/2607.07405
- **PDF:** https://arxiv.org/pdf/2607.07405

### GitHub Repository

No official source-code repository was verified for this paper during preparation of this document. Do not treat the AIRGuard repository as its implementation.

### Description

This work investigates deterministic, read-only pre-execution gates that inspect proposed tool calls and current environment state against explicit policy rules.

The gates intervene before a state-changing action is executed.

### Relevance to This Project

This paper provides additional context for action-level verification and the use of pre-execution checks to prevent policy violations.

It is relevant to the project's shared authorization pre-check and the distinction between deterministic authorization and risk-based confirmation.

**Use in this project:** Related methodological reference. Its implementation and experimental results are not reproduced.

---

## 4. Experimental Baselines Used in This Project

The experiment compares three verification strategies under a shared authorization pre-check.

| Strategy | Description |
|---|---|
| No Verification | Executes authorized actions without additional confirmation. |
| Always-on Verification | Requests confirmation for every authorized action. |
| Risk-Adaptive Verification | Requests confirmation when the predicted risk meets the selected threshold. |

The experiment also evaluates different risk thresholds:

- **Low:** Prompts for all authorized actions.
- **Medium:** Prompts for authorized actions classified as medium or high risk.
- **High:** Prompts only for authorized actions classified as high risk.

All strategies use the same authorization pre-check. Unauthorized actions are blocked before policy-specific verification is applied.

Therefore, the no-verification strategy means no additional confirmation, not the absence of access control.

---

## 5. Relationship Between the References and This Project

| Component | Reference or implementation |
|---|---|
| Runtime action verification motivation | AIRGuard |
| Authority and pre-execution checking concepts | AIRGuard |
| Deterministic pre-execution verification | Reddy et al. (2026) |
| No-verification strategy | Implemented in this project |
| Always-on verification strategy | Implemented in this project |
| Risk-adaptive verification strategy | Implemented in this project |
| Synthetic scenario dataset | Created for this project |
| Experimental evaluation | Independently implemented in this project |

The three experimental strategies are implemented and evaluated within this project's own simulation. They should not be described as AIRGuard's original baseline methods.

---

## 6. Implementation and Reproducibility

**Project repository:**

https://github.com/anmol9760/awesome-chained-tool-calling-agents/tree/main/risk-adaptive-verification

The project contains the experimental notebook, source modules, scenario data, evaluation metrics, result figures, and research documentation.

The experimental results should be attributed to this project's implementation and synthetic scenarios, not to AIRGuard or the deterministic-gates paper.

---

## 7. References

[1] S. Qin, H. Zhuang, Y. Zhou, Y. Han, and X. Zhang, "AIRGuard: Guarding Agent Actions with Runtime Authority Control," arXiv preprint arXiv:2605.28914, 2026. https://arxiv.org/abs/2605.28914

[2] S. Qin, H. Zhuang, Y. Zhou, Y. Han, and X. Zhang, "AIRGuard," GitHub repository, 2026. https://github.com/Sophie508/AIRGuard

[3] V. Reddy, S. R. Challaram, and A. Basu, "Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents," arXiv preprint arXiv:2607.07405, 2026. https://arxiv.org/abs/2607.07405

[4] Anmol, "Awesome Chained Tool-Calling Agents: Risk-Adaptive Verification," GitHub repository, 2026. https://github.com/anmol9760/awesome-chained-tool-calling-agents/tree/main/risk-adaptive-verification

---

## 8. Important Scope Note

This project is an independent, controlled simulation study inspired by prior work on runtime authority control and deterministic action verification.

It does not claim to reproduce AIRGuard, reproduce the deterministic-gates experiments, or establish equivalent performance on real-world agent benchmarks.

All experimental claims must be interpreted within the limitations of the project's synthetic scenario dataset, manually assigned risk labels, simulated consent, and simplified authorization model.
