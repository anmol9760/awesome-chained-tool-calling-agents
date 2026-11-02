
# Experimental Findings

## Strategy Comparison
- No Verification: Unsafe execution 64.71%, task success 100%,
  false rejection 0%, prompt rate 0%.
- Always Verification: Unsafe execution 29.41%, task success 63.64%,
  false rejection 36.36%, prompt rate 78.57%.
- Risk-Adaptive: Unsafe execution 52.94%, task success 81.82%,
  false rejection 18.18%, prompt rate 35.71%.

## Interpretation
Risk-adaptive verification provides an intermediate trade-off.
Compared with no verification, it reduces unsafe execution but also
reduces legitimate task success.
Compared with always verification, it reduces prompt frequency and
false rejection, but permits more unsafe executions.

## Threshold Sensitivity
Low threshold: 29.41% unsafe execution, 78.57% prompt rate.
Medium threshold: 52.94% unsafe execution, 35.71% prompt rate.
High threshold: 64.71% unsafe execution, 14.29% prompt rate.

## Limitations
- 28 synthetic scenarios.
- Simulated consent and manually assigned risk predictions.
- Common authorization checks across strategies.
- Prompt frequency is a proxy, not measured latency or cost.
- Results are exploratory and do not establish real-world effectiveness.
