# research_gaps.md

**Project:** From literature review to experimental paper on failure modes in chained tool-calling agents without human checkpoints
**Prompt:** 02, five evidence-based computational research gaps
**Date:** 2026-10-21 | **Companion file:** `research_decisions.md`
**Honesty note:** No experiment has been run. No code exists yet. Every number below is either quoted from a source I opened (and marked as such) or is explicitly marked INFERRED or UNKNOWN. Scores in Section 4 are my judgment, not measurements.

---

## 0. Label rules (same as `research_decisions.md`)

| Label | Meaning |
|---|---|
| **VERIFIED** | I opened the cited source in this session and the statement matches it. The "Depth" column says whether I read the full text or only the abstract page. |
| **INFERRED** | My reasoning. Could be wrong. |
| **UNKNOWN** | Not opened, not reproduced, or not found. |

"Author-reported" means your review itself states it. "Inference" means I am adding it.

---

## 1. Verification pass on the review's cited sources

### 1.1 What I opened

| ID | Review claim (location) | What the source says | Status | Depth |
|---|---|---|---|---|
| V-1 | MAST: 14 modes, 3 clusters, 1,600+ traces, 7 frameworks, kappa 0.88 on 150 traces (§1, §2.2) | Matches. v3 says 1,642 traces, 14 modes, 3 categories, human kappa 0.88. The LLM annotator's agreement with humans is lower: kappa 0.77 (0.79 on unseen systems) | VERIFIED | Full text (arXiv:2503.13657v3) |
| V-2 | MAST split ~42% / ~37% / ~21% (§2.2, §3.1, §3.4) | Not reproduced in the v3 text I read. v3 lists per-mode prevalences; summing them gives about 44% / 32% / 24% (my arithmetic). Your numbers may come from an earlier version | UNKNOWN (INFERRED version drift) | Full text |
| V-3 | MAST category names "specification" and "inadequate verification" (§1, §3) | v3 names them "system design issues," "inter-agent misalignment," "task verification" | VERIFIED (review wording differs) | Full text |
| V-4 | Failures stem from "design, not capability" (§1, §4.3, §7) | The authors call this a conjecture. Their interventions gave at most +15.6% success and they say completion rates "still remain low." Swapping GPT-4o for Claude 3.7 changed system-design failures by 39% in one comparison, so model choice matters | VERIFIED (review overstates) | Full text |
| V-5 | Time horizon doubles ~every 7 months since 2019; driven by tool use and error recovery "rather than raw reasoning alone" (§1, §6.4) | Doubling ~7 months: matches, but the abstract adds "the trend may have accelerated in 2024." The abstract lists drivers as reliability, adapting to mistakes, logical reasoning and tool use, so "rather than raw reasoning" is not what it says. The metric is human-time on software tasks, not number of tool calls. Latest revision is v4 (Jul 2026) | VERIFIED (review simplifies) | Abstract only |
| V-6 | §6.4: horizon growth is driven by error recovery "rather than raw task difficulty tolerance" | Not found in the abstract | UNKNOWN | Abstract only |
| V-7 | WebArena: 14.41% best GPT-4 agent vs 78.24% human (§1) | Matches. It is a 2023 result on GPT-4 | VERIFIED | Abstract only (arXiv:2307.13854v4) |
| V-8 | Agent-SafetyBench: 10 failure modes (§2.2, §3.2) | Matches, plus 349 environments, 2,000 test cases, 8 risk categories, 16 agents, none above 60% safety. Public repo stated. "Two lowest-scoring modes are parameter fabrication and ignoring tool risk" is not in the abstract | VERIFIED (modes); UNKNOWN (lowest-two claim) | Abstract only |
| V-9 | tau2-bench airline: 78% of failures silent; gates 29.6% -> 42.0%; +19.2 pp where gates fire (§3.2, §4.1) | All match arXiv:2607.07405: 78% silent on gpt-4o-mini; +12.4 pp (replicated +12.3 pp); +19.2 pp on 26 firing tasks; non-firing +5.0 pp with interval including zero; negative controls (retail, BFCL) | VERIFIED | Full text |
| V-10 | (Caveats the review omits about V-9) | KDD workshop paper, 7 pages. One positive domain. Lift carried almost entirely by one gate; another gate has 5% precision. Frontier-model result is n=5, unreplicated, lower bound near zero. Code "will be released upon publication." Authors list reflection/prompting baselines, held-out tasks, and rejection-message effects as untested | VERIFIED | Full text |
| V-11 | ">50% bypass of eight defenses" cited to arXiv:2606.05233 (§4.4, §5, §6.5) | Not supported by either candidate. 2606.05233 is a single-author browser benchmark reporting 0/140 hand-crafted multi-step attack successes on two frontier agents (but up to 100% on a coding-agent benchmark). 2606.26479 tests one out-of-band defense (Progent) on one 7B model: attack success 25.8% -> 4.2%, adaptive hand-crafted attack 2.6%, explicitly "one small-scale data point." It also mentions prior work breaking twelve in-band defenses at >90%, which I did not open | UNKNOWN (miscitation likely) | Abstract only |
| V-12 | AgentErrorTaxonomy / error propagation is the "primary bottleneck" (§2.2, §3.3) | Taxonomy covers memory, reflection, planning, action, system-level. Dataset from ALFWorld, GAIA, WebShop. AgentDebug: +24% all-correct accuracy, +17% step accuracy, up to 26% relative task success. Abstract says single root errors cascade; it does not say "primary bottleneck." Authors are credited (Zhu et al.), unlike the review's "uncredited" note | VERIFIED (core); UNKNOWN ("primary bottleneck") | Abstract only |
| V-13 | SEMAP: 69.6% and 56.7% failure reduction (§4.3) | Matches. Measured as MAST failure-count reduction on software-engineering tasks, not task success | VERIFIED | Abstract only |
| V-14 | Knight Institute autonomy framework (§2.4, §4.5) | Five roles and autonomy certificates confirmed. Authors are Kevin Feng, David McDonald, Amy Zhang (July 2025), not "Shavit et al." Conceptual essay, no empirical validation. It also lists open questions: how agents know when to seek approval; reviewer rubber-stamping | VERIFIED | Full text |
| V-15 | HIC / HITL / HOTL risk framework (§2.4, §4.5) | Exists (Kandikatla and Radeljic). Conceptual, about AI oversight generally, not agents specifically. The review's specific recommendations are not visible in the abstract | VERIFIED (existence); UNKNOWN (specific recommendations) | Abstract only |
| V-16 | Subplanning failures are a dominant bottleneck (§3.1, arXiv:2604.11978) | Paper exists (HORIZON benchmark, 3,100+ trajectories, four domains, LLM-judge attribution). Subplanning claim not in abstract | VERIFIED (existence); UNKNOWN (claim) | Abstract only |
| V-17 | StepFinder quote on single-step errors (§3.4) | Matches. Also: evaluated on Who&When, claims 79% less inference time than the fastest LLM-based method; code link stated | VERIFIED | Abstract only |

### 1.2 Sources the review does not cite that bear on its gaps (all opened this session)

| Source | What it adds | Depth |
|---|---|---|
| Who&When (Zhang et al., ICML 2025, arXiv:2505.00212) | 127 multi-agent systems; dataset on Hugging Face lists 184 annotated failure tasks (GAIA and AssistantBench queries). Best method: 53.5% agent-level, 14.2% step-level accuracy | Abstract + dataset card |
| AgentDojo (NeurIPS 2024 D&B, arXiv:2406.13352) | Extensible tool-calling environment: 97 tasks, 629 security test cases, supports new defenses and adaptive attacks; code released | Abstract |
| 2606.26479 | Names out-of-band deterministic defenses (CaMeL, FIDES, Progent, RTBAS, FORGE), all validated on static benchmarks per its authors | Abstract |
| 2607.07405 related work | Cites runtime-enforcement systems AgentSpec (arXiv:2503.18666) and AEGIS (arXiv:2603.12621) that your review does not mention. I have not opened them | Citation only |

### 1.3 Not opened in this pass (UNKNOWN as claims)
ReAct, Toolformer, Gorilla, ToolLLM, AgentBench, InjectAgent, ToolEmu, Instruction Hierarchy, Reflexion, Ferrag 2025, SHIELDA (2508.07935), 2510.04465, 2510.05244, the Cloud Security Alliance "NIST agentic profile" page, and arXiv:2605.08715. The last is cited in §5 but missing from your reference list, and a web search did not identify it.

### 1.4 Corrections to carry into the paper
1. Replace "failures are due to design, not capability" with the MAST authors' actual wording (a conjecture with limited intervention gains).
2. Fix the Knight Institute authorship.
3. Replace the ">50% bypass of eight defenses" claim until the source is found. As written, the two candidate sources do not support it.
4. Update the MAST percentages from the exact version you cite.
5. Add the Kwa "may have accelerated in 2024" caveat and read v4.
6. Note that the gate results come from a workshop preprint with one domain and no released code.

---

## 2. The five gaps

### G1. Checkpoint placement and verification timing have never been compared

1. **Gap.** The review argues that a checkpoint only at the start or end of a task "offers little protection" (§3.3), but no cited study runs the same agent with no checkpoint, an end-only check, and a pre-write check. The only direct evidence, the gate study (V-9), compares gates with vanilla.
2. **Support in review.** §3.3 (the start-or-end claim), §6.2 (gates' generalization "remains largely unstudied"), §6.6 (checkpoint treated as binary), Abstract. External: MAST argues final-stage checks are insufficient and multi-level verification is needed (V-1, full text), but from multi-agent software traces. The gate paper lists reflection and prompting baselines as untested (V-10).
3. **Origin.** Mixed. Author-reported: §6.2 and §6.6. INFERRED: that the placement comparison itself is untested, based on my reading of the review plus the sources above. I have not done a systematic search for prior placement studies, so this is UNKNOWN until you do.
4. **Research question.** In policy-permissive tool environments, how do success and silent-violation rate change across no checkpoint, end-of-episode audit, pre-write deterministic gate, pre-write self-check, and pre-write LLM verifier?
5. **Experiment.**
   - *Benchmark:* tau2-bench airline (arXiv:2506.07982 as cited by 2607.07405; availability and licence UNKNOWN, I did not open it).
   - *Conditions:* C0 vanilla; C1 end-of-episode audit (detects only); C2 re-implemented pre-write gates (the four rules described in Table 1 of 2607.07405: cancellation eligibility, baggage allowance, passenger count, must-read-before-write); C3 self-check prompt before writes; C4 LLM-judge check before writes; C5 oracle check (upper bound, labeled as such).
   - *Controls:* gates written on a dev split of tasks and frozen for a held-out split; informative vs generic rejection message.
   - *Metrics:* pass^1 and pass^k (tau-bench estimator), silent-violation rate, true-block precision and false-block rate (gold-trajectory audit, as the gate paper does), tool calls and tokens per trial, rejection-loop rate.
   - *Statistics:* paired task-level bootstrap with 95% intervals.
6. **Assumptions, limits, missing evidence.** Gate code is not released per the paper, so you re-implement from the paper's description. One positive domain. Oracle and simulated checks are not humans. Only state-decidable policies are covered. User-simulator cost per trial is UNKNOWN until a small pilot. Need to confirm tau2-bench access first.

### G2. Error compounding (Eq. 1) is asserted but never measured on chained tool calls

1. **Gap.** The review gives the chain-product formula and argues longer unchecked chains raise risk, but reports no per-step success rates or success-versus-chain-length data. Kwa et al. measure human-time horizons, not numbers of chained calls (V-5).
2. **Support in review.** §3 (Eq. 1 and the sentence introducing it, which carries a broken citation key), §1 (the ten-step example), §6.4 (model "capability growth, checkpoint frequency, expected undetected-failure rate"). External: AgentErrorBench paper describes cascading failures (V-12); the gate paper shows pass^k collapsing from 29.6% to 8.0% on the same tasks (V-9, full text), which shows inconsistency but not stepwise decay.
3. **Origin.** Author-reported: §6.4. INFERRED: the specific measurement design and the claim that independence-style decay may not hold, because Kwa et al. attribute horizon gains partly to adapting to mistakes (V-5).
4. **Research question.** How does end-to-end success vary with the number of dependent tool calls k, and is it better described by constant per-step decay or by a model with error recovery?
5. **Experiment.**
   - *Method:* (a) programmatic generator of k-step dependent tool tasks with deterministic ground-truth state, k swept across a range you choose after a pilot; (b) a real-benchmark check by stratifying tau2-bench airline tasks by number of required write actions in the gold trajectory.
   - *Models:* at least two (one open-weight, one API), per your budget (UNKNOWN).
   - *Baselines:* Eq. 1 with constant p estimated from k=1; a no-decay null; a recovery model with probability r of finishing correctly after an error.
   - *Metrics:* success vs k with intervals, estimated per-step success p-hat, first-failure-step distribution, recovery rate, silent vs loud failure share per step. Compare models by likelihood or AIC.
   - *Extension:* oracle verification every m steps (links to G1).
6. **Assumptions, limits, missing evidence.** Synthetic chains may not match real tasks. "Step" must be defined precisely. Novelty is UNKNOWN: I did not search for prior chain-length decay studies. Run counts per k must be large enough for stable intervals; cost depends on the model.

### G3. Risk-threshold routing (Eq. 2) is under-specified and unvalidated

1. **Gap.** Eq. 2 routes an action to human review when risk R(a) exceeds tau, but R(a) and tau are undefined in the review, and the equation is cited to Kwa et al., whose abstract is about time horizons. No evidence in the review shows which risk scorer works.
2. **Support in review.** §4.5 (Eq. 2 and the sentence introducing it), §6.3 (frameworks not yet validated against measured failure rates). External: the Knight essay lists "how can the agent reliably know when to seek approval" as an open question and warns of rubber-stamping (V-14, full text); MAST's appendix suggests confidence thresholds for agent actions, so the idea has prior art as a proposal (V-1, full text). The HIC/HITL/HOTL paper is conceptual (V-15).
3. **Origin.** Author-reported: §6.3. INFERRED: that Eq. 2 is under-specified (I-3 in `research_decisions.md`) and that no empirical test appears in the sources I opened. Broader literature on selective escalation is UNKNOWN.
4. **Research question.** Under a fixed review budget B (maximum fraction of write actions escalated), which risk scorer catches the most policy-violating writes, and what success versus review-cost tradeoff results?
5. **Experiment.**
   - *Data:* write actions from G1's vanilla (C0) trajectories, labeled violating or not using the gold-trajectory audit.
   - *Scorers:* random; escalate-all; write-type prior (rule-based reversibility ordering); LLM-verbalized confidence; LLM-estimated impact; small supervised classifier on action features with task-level cross-validation (split by task to avoid leakage).
   - *Policy:* I(a)=1 if R(a) >= tau (Eq. 2), tau set to meet budget B.
   - *Reviewer:* simulated oracle, plus a noisy reviewer with error rate swept as a stated assumption to approximate rubber-stamping.
   - *Metrics:* recall and precision of violating writes at budget B, area under the escalation-cost vs residual-violation curve, calibration error of R(a), task success with reviewer.
   - *Baselines:* no review, review-all (cost upper bound), random at equal budget.
6. **Assumptions, limits, missing evidence.** Oracle reviewer is not a human. Labels cover only gate-defined violations, so unknown violations are missed. Violating-write counts may be small (the gate paper's audit reports 161 fires for its best gate, over its own runs). Classifier may learn domain-specific cues. Single domain.

### G4. Evidence on tool-boundary defenses under adaptive attack is thin and partly miscited; injection depth is untested

1. **Gap.** The review concludes current defenses are "risk-reducing rather than risk-eliminating" and cites bypass rates above 50%. The cited source does not report that (V-11), and the defenses it omits (out-of-band deterministic enforcement) show a different picture in a small test. Nothing in the review studies where in a call chain an injection lands.
2. **Support in review.** §3.5 (each unreviewed call is "an additional opportunity"), §4.4, §5 (arms race), §6.5. External: 2606.26479 (Progent held in one small adaptive test, authors say the result "does not establish" the hypothesis); 2606.05233 (browser-domain resistance did not carry to coding agents); AgentDojo (extensible environment for adaptive attacks).
3. **Origin.** Author-reported: §5 and §6.5. The review's evidence for them is unverified. INFERRED: the injection-depth dimension, and that out-of-band defenses are a missing part of the review.
4. **Research question.** On AgentDojo, how does attack success vary with the position of the injected tool output in the chain, and does a deterministic least-privilege tool-call policy reduce it more than an in-band detector under a defense-aware attack?
5. **Experiment.**
   - *Benchmark:* AgentDojo. Whether the injection point can be moved is UNKNOWN; check the framework first.
   - *Defenses:* none; AgentDojo's built-in defenses (names to check in its repo); a task-derived allow-list policy layer you implement; Progent-style enforcement only if its code is available (UNKNOWN).
   - *Attacks:* AgentDojo's built-in attacks plus a defense-aware hand-crafted template, following the protocol described in 2606.26479.
   - *Metrics:* targeted attack success rate, benign utility, utility under attack, with repeated seeds and intervals.
6. **Assumptions, limits, missing evidence.** A hand-crafted adaptive attacker cannot support a robustness claim; optimized attacks are out of scope for a small project. Compute: the cited reproduction used a single H200 with a 7B open model; your hardware is UNKNOWN. Position may be confounded with task length. Keep all work inside the benchmark.

### G5. Failure attribution lacks objective ground truth, and taxonomies are not comparable

1. **Gap.** The review lists attribution difficulty, LLM-as-judge circularity and fragmented taxonomies as open (§5, §6.1). The evidence I opened shows attribution is being worked on (Who&When, StepFinder, HORIZON, AgentDebug) but evaluated against human or LLM labels, and on mostly multi-agent data.
2. **Support in review.** Abstract (attribution), §5 (attribution difficulty; judge circularity; fragmented taxonomies), §6.1 (standard taxonomy). External: Who&When best step-level accuracy is 14.2% (V-17 section 1.2); HORIZON reports inter-annotator kappa 0.61 and human-judge kappa 0.84 (V-16); MAST annotator kappa is 0.77 (V-1).
3. **Origin.** Author-reported: §5 and §6.1. INFERRED: that in policy-permissive environments the root-cause step is computable (first policy-violating write), which allows circularity-free evaluation. Note the review's §6 has no attribution subsection, which conflicts with the Abstract.
4. **Research question.** On tau2-bench airline trajectories where the root-cause step is computable, how accurately do LLM-judge and lightweight baselines recover it, and how well do MAST and AgentErrorTaxonomy labels agree on the same traces?
5. **Experiment.**
   - *Data:* vanilla trajectories from G1; ground truth = first write violating policy per the gold audit.
   - *Methods:* random; first-write and last-write heuristics; LLM judge (all-at-once and step-by-step formats, as used on Who&When; details to read); StepFinder (code link stated, applicability UNKNOWN); AgentDebug (code release status UNKNOWN).
   - *Taxonomy agreement:* label a stratified sample under MAST (annotator package per the MAST paper) and AgentErrorTaxonomy, then compute Cohen's kappa between crosswalked labels; add a small human-labeled subset (size set by pilot).
   - *Metrics:* step accuracy, within-one-step accuracy, mean step error, cost and latency, cross-taxonomy kappa.
6. **Assumptions, limits, missing evidence.** Ground truth exists only for state-decidable violations in one domain. Single-agent traces are not comparable to Who&When's headline numbers. MAST's annotator targets multi-agent traces, so its fit here is UNKNOWN. Taxonomy labeling still uses an LLM judge.

---

## 3. Evidence summary for each gap

| Gap | Strongest verified support | Weakest link |
|---|---|---|
| G1 | Gate study shows large effect where gates fire; MAST says multi-level verification needed | Prior placement studies not searched; one domain; no released code |
| G2 | Review's own §6.4; Kwa measures horizons, not chain length | Novelty unchecked; synthetic-to-real transfer |
| G3 | Review's §6.3; Knight open questions | Eq. 2 undefined; oracle reviewer |
| G4 | AgentDojo exists and is extensible; contrast between 2606.05233 and 2606.26479 | Review's bypass claim unsupported; adaptive attacker hard |
| G5 | Who&When and HORIZON show the problem is active | Crowded; LLM-judge circularity persists |

---

## 4. Gap matrix and ranking

Scores are 1 to 5, higher is better. "Resources" scores 5 for cheapest. Weights are equal. All scores are INFERRED from my reading, and I assumed one researcher with API access but no GPU cluster (UNKNOWN, please confirm).

| Gap | Origin | Primary dataset / benchmark | Baseline | Key metrics | Significance | Resources | Feasibility | Total | Rank |
|---|---|---|---|---|---|---|---|---|---|
| G1 Checkpoint placement | Mixed | tau2-bench airline | Vanilla; self-check; LLM verifier | pass^k, silent-violation rate, false blocks | 5 | 3 | 4 | 12 | 1 |
| G2 Compounding measurement | Author-reported + inference | Synthetic chains + tau2-bench strata | Constant-p (Eq. 1); no-decay null | success vs k, p-hat, recovery rate | 3 | 4 | 5 | 12 | 2 |
| G3 Risk-threshold routing | Author-reported + inference | G1 trajectories | Random; review-all; no review | recall at budget, cost-safety curve | 4 | 3 | 3 | 10 | 3 |
| G4 Tool-boundary defense by depth | Author-reported, weak evidence | AgentDojo | No defense; built-in detector | attack success, utility under attack | 5 | 2 | 2 | 9 | 4 |
| G5 Attribution ground truth | Author-reported + inference | G1 trajectories; Who&When | Heuristics; LLM judge | step accuracy, cross-taxonomy kappa | 3 | 3 | 3 | 9 | 5 |

Tie-breaks: G1 over G2 on significance; G4 over G5 on significance.

---

## 5. Top three and why

**1. G1.** It is the only gap that directly tests your review's central claim, which no cited study does. It also targets limitations the gate paper itself lists (untested reflection baseline, held-out tasks, rejection-message effect), so you can state concrete additions to prior work. Main risk: tau2-bench access and re-implementing gates without released code.

**2. G2.** Cheapest and most feasible. It gives your paper a measured basis for Eq. 1 instead of a formula, and its chain-length sweep feeds G1's design. Main risk: significance depends on novelty, which I have not checked.

**3. G3.** It turns Eq. 2 from a sketch into a testable policy and reuses G1's logged trajectories and labels. Main risk: the simulated reviewer; report it as a limitation, not a human result.

**Why not G4 or G5 first.** G4 has the highest upside but the weakest feasibility: adaptive attackers are hard, hardware is unknown, and the review's own premise needs repair (V-11). It is the right alternative if you decide security is your priority. G5 is crowded; its best idea, computing ground truth from policy violations, costs almost nothing as a secondary analysis of G1's logs.

**Dependency note.** G1, G2 and G3 share one harness (tau2-bench airline trajectories plus gates). That is efficient, but it also means a single point of failure: if tau2-bench is unavailable, all three need a replacement benchmark. Check access before committing.

---

## 6. Open questions and assumptions

1. Budget, hardware and deadline are still UNKNOWN (asked in the previous turn). The ranking assumes API access, no GPU cluster, and a few weeks.
2. Is a simulated or oracle checkpoint acceptable as a stand-in for a human? G1 and G3 depend on this.
3. Do you want one paper (G1 + G2 + G3 as a single study) or separate directions?
4. Where did the review's MAST percentages come from (which version)?

## 7. Next actions

1. Confirm tau2-bench access, licence and compute needs by opening its paper and repository (not done yet).
2. Run a targeted literature search for prior placement and chain-length-decay studies before claiming novelty for G1 or G2.
3. Identify what arXiv:2605.08715 is, and find the real source for the defense-bypass claim.
4. Decide on the top three, then write a one-page experiment spec (variables, metrics, controls, stopping rules) before any code.
5. Merge Section 1's verification results into `research_decisions.md` Section 7.
