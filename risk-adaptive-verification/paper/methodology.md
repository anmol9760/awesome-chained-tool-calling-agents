
# Methodology and Experimental Setup

## 1. Experimental Design

We conduct a controlled simulation to compare three verification
strategies for tool-using AI agents:

1. No Verification
2. Always Verification
3. Risk-Adaptive Verification

All strategies operate on the same set of 28 synthetic scenarios.

## 2. Scenario Design

Each scenario represents a potential tool action, such as:
- Reading files
- Modifying configuration or project files
- Deleting files
- Executing scripts
- Transferring simulated funds
- Accessing databases or sending data externally

Each scenario contains:
- Action description
- Actual risk level
- Predicted risk level
- Authorization status
- Task legitimacy
- Simulated user consent

Risk levels are low, medium, and high.

## 3. Verification Strategies

### 3.1 No Verification
The system checks authorization and executes authorized actions
without requesting additional confirmation.

### 3.2 Always Verification
The system checks authorization and requests confirmation for
every authorized action.

### 3.3 Risk-Adaptive Verification
The system checks authorization first. It requests confirmation
when predicted risk is medium or high. Low-risk actions proceed
without additional confirmation.

## 4. Threshold Sensitivity Analysis

We evaluate three risk thresholds:

- Low: confirmation for low-, medium-, and high-risk actions.
- Medium: confirmation for medium- and high-risk actions.
- High: confirmation only for high-risk actions.

This evaluates how the verification threshold affects security
and operational overhead.

## 5. Experimental Assumptions

- Authorization checks are common to all strategies.
- Unauthorized actions are blocked before verification.
- User consent is simulated using predefined scenario values.
- Actual and predicted risk labels are manually assigned.
- The risk estimator is a controlled simulation, not a trained
  machine-learning model.
- All experiments use deterministic scenarios.

## 6. Evaluation Metrics

### Unauthorized Action Rate
Percentage of unauthorized actions that were executed.

### Unsafe Action Execution Rate
Percentage of illegitimate actions that were executed.

### Legitimate Task Success
Percentage of legitimate actions that were executed.

### False Rejection Rate
Percentage of legitimate actions that were blocked.

### Verification Prompt Rate
Percentage of all scenarios for which confirmation was requested.

Prompt rate is used as a proxy for verification overhead.
Actual latency and computational cost are not measured.

## 7. Experimental Environment

Experiments were conducted in Google Colab using:
- Python 3.13.18
- Pandas 2.2.3
- NumPy 2.1.3
- Matplotlib 3.10.0

The experiment uses synthetic data and does not interact with
real files, databases, financial systems, or external tools.
