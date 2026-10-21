# research_decisions.md

**Project:** From literature review to experimental paper on failure modes in chained tool-calling agents operating without human checkpoints
**Created:** 2026-10-21 | **Phase:** 0 (review analysis, no experiment chosen yet)
**Honesty note:** No code has been run. No experiments exist. No results, metrics, repos or datasets are claimed by this file. Everything below is analysis of the attached review PDF plus my reasoning.

---

## 0. Label definitions (read first)

| Label | Meaning in this file |
|---|---|
| **VERIFIED** | Checked directly. Right now this ONLY means "I read it in your review PDF," so it is a fact about what the review says or contains. It never means the underlying claim about the world is true. |
| **INFERRED** | My reasoning or conclusion. Could be wrong. Needs your challenge. |
| **UNKNOWN** | Not checked against a primary source. Every number or finding the review attributes to an outside paper is UNKNOWN until you open that paper and log it in Section 7. |

Rule: a claim "reported in review §X" is UNKNOWN as a claim about the world. Upgrade to VERIFIED only after the original source is read and logged in Section 7.

---

## 1. Topic and review summary

### 1.1 Topic
Failure modes, error propagation, safety and oversight gaps when LLM agents chain many tool calls with no human reviewing intermediate steps.

### 1.2 Scope and central problem
- [VERIFIED in review] Scope: failures in chained tool-calling LLM agents, organised into reasoning/planning, tool-use/parameter, memory/context, and multi-agent coordination, plus a separate security section on indirect prompt injection (Abstract, §3).
- [VERIFIED in review] Central thesis: removing human checkpoints removes the main way several serious failures get caught: silent wrong-state actions, cascading error propagation, inter-agent misalignment, prompt injection across the tool boundary (§7).
- [VERIFIED in review] Stated approach: "synthesizes recent empirical and conceptual literature" and is titled "A Systematic Review."
- [VERIFIED in review] No search protocol appears: no databases, search strings, inclusion/exclusion criteria, screening counts or PRISMA-style flow.
- [INFERRED] So this is a narrative/structured review, not a systematic one. Do not call it "systematic" in paper 2 without fixing this.

### 1.3 Failure categories (as the review presents them)

| Category | Review section | What the review says | Main cited sources |
|---|---|---|---|
| Reasoning and planning | §3.1 | Subplanning errors (constraint/modifier missed) are trajectory-dependent; early deviation propagates; agent self-report may hide it | Cemri 2025 (MAST); arXiv:2604.11978 |
| Tool-use and parameters | §3.2 | Wrong tool choice, fabricated parameters, misread outputs; "silent wrong-state" failures | Zhang 2024 (Agent-SafetyBench); arXiv:2607.07405 |
| Memory, context, error propagation | §3.3 | One root error cascades; agents repeat faulty actions without updating state | arXiv:2509.25370; arXiv:2508.07935 |
| Multi-agent coordination | §3.4 | Misalignment, ignored peer input, no verification of sub-results; attribution is hard | Cemri 2025; arXiv:2606.03467 |
| Security (prompt injection) | §3.5 | Agents follow instructions injected via tool outputs | Zhan 2024 (InjectAgent); Ferrag 2025 |

### 1.4 Key findings the review reports (ALL UNKNOWN as claims about the world until checked)

| ID | Claim as stated in review | Where | Cited source | Label |
|---|---|---|---|---|
| F1 | MAST: 14 failure modes, 3 clusters, 1,600+ traces, 7 frameworks; kappa = 0.88 on 150 hand-annotated traces | §1, §2.2 | Cemri 2025 | UNKNOWN |
| F2 | MAST split: ~42% specification/design, ~37% inter-agent misalignment, ~21% inadequate verification | §2.2, §3.1, §3.4 | Cemri 2025 | UNKNOWN |
| F3 | WebArena: best GPT-4 agent 14.41% vs human 78.24% | §1 | Zhou 2023 | UNKNOWN (and stale, see issue I-10) |
| F4 | Task horizon at 50% reliability doubling roughly every 7 months since 2019 | §1, §5, §6.4 | Kwa 2025 (METR) | UNKNOWN |
| F5 | Agent-SafetyBench: 10 failure modes; fabricating parameters and ignoring tool risk are the two lowest-scoring | §3.2 | Zhang 2024 | UNKNOWN |
| F6 | Silent wrong-state: 78% of failures on a budget agent config were silent/no-error (tau2-bench airline) | §3.2 | arXiv:2607.07405 | UNKNOWN |
| F7 | Four deterministic gates raised success 29.6% -> 42.0%; +19.2 pp on tasks where a gate fired; no movement elsewhere | §4.1 | arXiv:2607.07405 | UNKNOWN |
| F8 | Error propagation is the primary bottleneck for long-horizon agents | §2.2, §3.3 | arXiv:2509.25370 | UNKNOWN |
| F9 | SEMAP: up to 69.6% (function-level) and 56.7% (deployment-level) failure reduction | §4.3 | arXiv:2510.12120 | UNKNOWN |
| F10 | Adaptive attacks bypassed all 8 tested injection defenses, >50% success each | §4.4, §5, §6.5 | cited as arXiv:2606.05233 | UNKNOWN (likely mis-cited, see I-7) |
| F11 | Injected instructions in tool outputs are frequently followed | §2.3, §3.5 | Zhan 2024 | UNKNOWN |

### 1.5 Limitations the review reports (§5)
Benchmark-to-deployment gap; attribution difficulty; LLM-as-judge circularity; fast-shifting capability baselines; security arms race; fragmented taxonomies. [VERIFIED in review] These are limits of the *evidence base*. [VERIFIED in review] There is no section on limits of the review itself.

### 1.6 Research gaps in §6 (the review has six, not four)

| § | Gap | Matches your list? |
|---|---|---|
| 6.1 | Standardised cross-domain failure taxonomy and reporting (CVSS-like severity) | Partly. This is taxonomy, not attribution. |
| 6.2 | Intermediate-trajectory oversight mechanisms | Yes |
| 6.3 | Risk-calibrated autonomy assignment | Yes |
| 6.4 | Joint modelling of capability growth and oversight needs | Not in your list |
| 6.5 | Non-bypassable defenses at the tool boundary | Yes |
| 6.6 | Human factors in checkpoint design | Not in your list |

[VERIFIED in review] The Abstract promises a gap on "standardized failure-attribution methodology," but §6 has no attribution subsection. Attribution appears only in §5 and the Abstract. Fix this inconsistency.

### 1.7 Benchmarks, datasets, evaluation methods, mitigations named in the review
- **Benchmarks/datasets:** ALFWorld, WebShop (ReAct); AgentBench (8 environments); WebArena; MAST and MAST-Data; AgentErrorBench (ALFWorld, GAIA, WebShop); Agent-SafetyBench; InjectAgent; ToolEmu (LM-emulated sandbox); tau2-bench airline domain; OSWorld (mentioned via SHIELDA); a 793-episode browser benchmark (arXiv:2606.05233).
- **Evaluation methods:** end-to-end task success; functional correctness of final environment state (WebArena); human annotation with inter-annotator kappa; LLM-as-judge scaling; negative-control comparisons for gates; adaptive-attack success rates.
- **Mitigations:** deterministic pre-execution gates; Reflexion-style self-critique; SEMAP / behavioural contracts on A2A; input sanitisation, instruction hierarchy, firewall layers; tiered oversight (HIC/HITL/HOTL, five autonomy roles, autonomy certificates).
- [VERIFIED in review] Table 2 lists five future directions (runtime verification, typed inter-agent contracts, hierarchical plan validation, adversarial stress-testing, continuous behavioural audit) with no cited support.

---

## 2. Problems found in the review itself (fix before reusing its bibliography)

| ID | Issue | Location | Severity | Label |
|---|---|---|---|---|
| I-1 | Titled "Systematic Review" but no search protocol or selection criteria | Title, whole paper | High | VERIFIED in review |
| I-2 | Raw BibTeX keys printed in text: `cemri2025mast` (Table 1, §3 intro) and `kwa2025metr` (Eq. 2 paragraph) | Table 1, §3, §4.5 | Medium | VERIFIED in review |
| I-3 | Eq. 2 is cited to Kwa et al., whose described contribution is task horizons, not threshold routing. R(a) and tau are undefined, and tau clashes with tau2-bench | §4.5 | High | INFERRED miscitation |
| I-4 | Eq. 1 is just the chain rule. It has no data behind it, so it is decoration unless you measure it | §3 | Low | INFERRED |
| I-5 | §3 intro says failure categories and mitigations are "summarized in Table 2," but Table 2 is future directions; mitigations are Table 3 | §3 | Medium | VERIFIED in review |
| I-6 | "Four categories" in Abstract and §3, but §3 has five subsections (3.5 security) | Abstract, §3 | Low | VERIFIED in review |
| I-7 | ">50% bypass of eight defenses" is cited to arXiv:2606.05233, whose listed title is a 793-episode browser benchmark. The title that fits an adaptive-defense study (arXiv:2606.26479) is in the reference list but never cited in text | §4.4, §5, §6.5 | High | INFERRED |
| I-8 | arXiv:2605.08715 cited in §5 but missing from the reference list | §5 | Medium | VERIFIED in review |
| I-9 | Weak/secondhand attributions: "Shavit et al.-style framework" for the Knight Institute paper; "uncredited authorship"; "survey synthesis"; "industry system-card disclosures"; "MDPI review" (not in references); "secondary literature"; Kasirzadeh and Gabriel entry points to a differently titled paper. The "NIST Agentic Profile" source is a Cloud Security Alliance page, not NIST | §2.3, §2.4, §3.5, §4.4, refs | High | VERIFIED in review |
| I-10 | Intro and §2.2 use 2023 GPT-4 numbers to claim "failure is the dominant outcome." That is stale for an Oct 2026 paper | §1, §2.2 | High | INFERRED |
| I-11 | The central claim ("no checkpoints makes it worse") is argued, never shown. As described in the review, no cited study runs the same agent with and without checkpoints | §3, §7 | High | INFERRED |
| I-12 | Conclusion calls findings "cautiously optimistic" because failures are "design not capability." MAST labels where failures sit; it does not show stronger models would not fix them | §7 | Medium | INFERRED |
| I-13 | Figure 2 (citation map) names no tool or method, is not referenced in the text, and shows works (Brown 2020, Wei 2022, Nakano 2021, Achiam 2023, Park 2023, Li 2023, Zhao 2024) absent from the reference list | Fig. 2 | Medium | VERIFIED in review |
| I-14 | Several arXiv IDs are 2604-2607 (2026). I cannot confirm them from my own knowledge, so each must be opened | Many | High | UNKNOWN |

---

## 3. Candidate research directions (all INFERRED; none chosen)

| ID | Direction | Review gap | Draft testable question | Minimum experiment | Main risks / unknowns |
|---|---|---|---|---|---|
| C1 | Checkpoint placement ablation | 6.2, 6.4 | How do end-to-end failure and silent-violation rates change with chain length and checkpoint placement (none / end only / every step / risk-triggered)? | Pick a state-checked benchmark, vary chain length, compare checkpoint types, measure per-step conditional success to test Eq. 1 | A simulated checkpoint is not a human. Benchmark access/licence unknown. |
| C2 | Gate generalisation | 6.2 | Do deterministic pre-write gates help outside the airline domain? | Re-implement gate idea in other tau2 domains, compare with negative controls | Rests on one unverified preprint. Code availability unknown. Domain-specific rules. |
| C3 | Risk-threshold routing (Eq. 2) | 6.3 | What cost-vs-failures-caught tradeoff do different risk scorers R(a) give under a fixed review budget? | Compare rule-based vs LLM-estimated R(a) with a simulated reviewer | Needs risk labels. Eq. 2 is currently undefined. |
| C4 | Injection depth | 6.5, 6.2 | Does attack success change with the step at which injected content appears, and does a mid-chain gate help? | Inject at step k in a tool-calling harness, measure attack success with and without gate | Needs InjectAgent-style data (availability unknown). Non-adaptive attacks give a weak claim, as the review itself says. |
| C5 | Failure-attribution baselines | Abstract, §5 | How well do simple methods find the first causal wrong step in failed traces? | Implement baselines on annotated traces and score against labels | Needs labeled traces. LLM-judge circularity. Crowded (StepFinder). |
| C6 | Human-factors checkpoint study | 6.6 | Which checkpoint designs raise human error-catch rates? | Human subject study | Needs participants and ethics approval. Not feasible now. |

**My lean (INFERRED, your call):** C1, using C2-style gates as the working baseline. Reason: it is the only candidate that directly tests the review's central claim (I-11). Alternative if security is your priority: C4. Defer C6.

---

## 4. Decisions log

| ID | Decision | Status | Reason | Evidence |
|---|---|---|---|---|
| D-001 | Treat every review claim as a lead, not evidence, until the primary source is logged in Section 7 | DECIDED | Your instruction, plus issues I-3, I-7, I-9, I-14 | Review PDF |
| D-002 | Use the VERIFIED / INFERRED / UNKNOWN scheme defined in Section 0 | DECIDED | Your instruction. "VERIFIED" is restricted to avoid overclaiming. | This file |
| D-003 | Do not write paper 2 yet; no research question locked | DECIDED | Your instruction | This file |
| D-004 | Experiment must include a with-vs-without-checkpoint contrast | PROPOSED, needs your acceptance | Review never tests its central claim (I-11) | INFERRED |
| D-005 | Repair the review's bibliography and citations before it feeds paper 2 | PROPOSED, needs your acceptance | I-2, I-3, I-5, I-7, I-8, I-9 | Review PDF |

---

## 5. Unresolved questions

1. Deadline and target venue (course project, workshop, conference, arXiv only)?
2. Compute and API budget? Which models can you actually run?
3. Is a simulated or oracle checkpoint acceptable as a stand-in for a human, given the limitation it creates?
4. Do you have the review's LaTeX source and .bib file?
5. Which candidate (C1-C5) do you want to examine first?
6. Do you plan to release code and logs?

---

## 6. Claims requiring verification (priority order)

| Priority | Claim | Primary source to open |
|---|---|---|
| V1 | F1-F2 MAST counts, kappa, percentages | arXiv:2503.13657 |
| V2 | F4 doubling time and what drives it; check for newer METR updates | arXiv:2503.14499 |
| V3 | F6-F7 silent-failure rate and gate results; is code released? | arXiv:2607.07405 |
| V4 | F10 which paper actually supports ">50% across 8 defenses" | arXiv:2606.05233 and arXiv:2606.26479 |
| V5 | F3 WebArena numbers, and current state-of-the-art | arXiv:2307.13854 plus recent leaderboard |
| V6 | F5 ten failure modes and lowest-scoring two | arXiv:2412.14470 |
| V7 | F8 error propagation as primary bottleneck | arXiv:2509.25370 |
| V8 | F9 SEMAP reductions | arXiv:2510.12120 |
| V9 | Knight Institute: real authors, five roles, certificates | knightcolumbia.org link in references |
| V10 | HIC/HITL/HOTL mapping details | arXiv:2510.09090 |
| V11 | Subplanning claim | arXiv:2604.11978 |
| V12 | SHIELDA OSWorld claim | arXiv:2508.07935 |
| V13 | StepFinder quote | arXiv:2606.03467 |
| V14 | Missing reference arXiv:2605.08715 | Identify what it is |

---

## 7. Verification log (fill as you go)

| Claim ID | Source opened (URL/ID) | Date | What the source actually says (your words) | Matches review? | New label |
|---|---|---|---|---|---|
| | | | | | |

---

## 8. Next actions

1. Answer the questions in Section 5.
2. Accept or reject D-004 and D-005.
3. Verification pass on V1-V5 first. Log results in Section 7.
4. Narrow to two candidates. For each, check benchmark access, licence, and cost of a small pilot (no results claimed until you run it).
5. Write a one-page experiment spec before any code: question, hypotheses, variables, metrics, controls, stopping rules.
6. Only then: choose the baseline and set up the repo (seeds, configs, logging).
