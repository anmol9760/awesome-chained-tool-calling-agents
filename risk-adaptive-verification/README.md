
# Risk-Adaptive Verification for Tool-Using AI Agents

## 1. Overview
This project investigates risk-adaptive verification for tool-using AI agents.
It compares three strategies:
- No Verification
- Always Verification
- Risk-Adaptive Verification

The prototype uses simulated tool actions and synthetic controlled scenarios.

## 2. Research Question
Does risk-adaptive verification reduce verification overhead while maintaining
protection against unsafe tool actions compared with no verification and
always-on verification?

## 3. Literature Baseline
AIRGuard: Guarding Agent Actions with Runtime Authority Control

Paper: https://arxiv.org/abs/2605.28914
Repository: https://github.com/Sophie508/AIRGuard

Our implementation is a simplified experimental prototype, not a reproduction
of the complete AIRGuard framework.

## 4. Experimental Design
- Dataset: 28 synthetic scenarios
- Risk levels: Low, Medium, High
- Common authorization check across all strategies
- Simulated user confirmation
- Threshold sensitivity: Low, Medium, High

## 5. Evaluation Metrics
- Unauthorized Action Rate
- Unsafe Action Execution Rate
- Legitimate Task Success
- False Rejection Rate
- Verification Prompt Rate

Prompt rate is used as a proxy for verification overhead, not actual latency.

## 6. Project Structure
- results/: CSV experiment outputs and configuration
- src/: implementation modules
- experiments/: experiment scripts
- notebooks/: Google Colab notebook
- baseline/: baseline research material

## 7. Execution
Open the experiment notebook in Google Colab and run all cells from top to bottom.

## 8. Limitations
- Synthetic scenarios rather than real-world agent traces.
- Simulated user confirmation.
- Manually assigned risk predictions.
- Simplified authorization model.
- No measurement of actual execution latency or monetary cost.

## 9. Reproducibility
The dataset is deterministic. Environment details and experiment settings
are recorded in results/experiment_config.json.
