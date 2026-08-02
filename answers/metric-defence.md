# Metric Defence Dossier

**Do this Days 1–2, before anything else.** 49% of hiring managers report that candidates cannot defend resume claims under probing. One collapsed number retroactively discredits every other number on the page.

---

## 📁 Model answers — `answers/`

Worked model answers for every question in this file, with the follow-up chains interviewers actually run:

| File | Covers |
|---|---|
| [`answers/01-latency-and-cost.md`](answers/01-latency-and-cost.md) | Claims 1 & 2 — −40% latency, −30% cost. Prefill vs decode, the mechanism split, the "did quality regress?" killer |
| [`answers/02-relevance-and-agent-success.md`](answers/02-relevance-and-agent-success.md) | Claims 3 & 5 — +35% relevance, +20% agent success. Judge validation, pass^k, the Turing attribution problem |
| [`answers/03-turnaround-and-effort.md`](answers/03-turnaround-and-effort.md) | Claims 4 & 6 — −45% turnaround, −60% tagging effort. Includes the **MCP timeline trap** (see below) |
| [`answers/04-sklearn-accuracy.md`](answers/04-sklearn-accuracy.md) | Claim 7 — the ~85% accuracy claim. The longest follow-up chain of any claim; treat it as the one most likely to go badly |
| [`answers/05-scale-and-narrative.md`](answers/05-scale-and-narrative.md) | Scale claims (10k docs / 1M events / 50k records), "8+ years" vs a 2014 B.Tech, the Turing overlap, being between jobs, and the **universal closing moves** |

**Three rules for using them:**

1. **They are scripts for things you actually did.** Every fact only you know is a `[BRACKETED SLOT]`. **Never speak an unfilled bracket** — it sounds exactly like a lie. Fill this dossier in first; the answers show the *shape*, not the data.
2. **Each answer has honest branches.** Where a claim may not survive, there's a version that keeps your credibility and drops the number. Use it. A rehearsed false claim about methodology is worse than losing the number, because it's a **trust finding**, not a skills gap — and trust findings are close to unrecoverable in a debrief.
3. **The anti-rehearsal rule.** A technical line is only worth saying if you can attach one concrete, slightly boring detail from the real project — a column name, a bug, a number that came out wrong, an argument you had. **Recited depth with no texture reads as *studied***, and an interviewer who suspects that probes one level lower until you break. No texture → say it in one sentence and move on.

> ⚠️ **One thing the adversarial pass caught that you should fix on the resume today:** MCP was announced **25 Nov 2024**, and your Turing engagement ended **Jan 2025**. The resume line reads as though you did MCP work across that whole engagement. Split the claim — tool-calling and PR/CI-CD orchestration across the engagement, MCP specifically in the last stretch — before someone does that subtraction in front of you.

---

## The rule

For each claim, answer the **9-question drill** cold. Then apply the **30-second test**:

> Can you state **metric definition + baseline + n + who labelled + biggest confounder** in 30 seconds?
> **No → DELETE the number from the resume and keep the qualitative claim.**

A deleted number costs you nothing. A collapsed one costs you the loop. There is no third option where you keep a number you can't defend and hope nobody asks — they always ask, and *"how exactly did you measure that?"* is the standard opener.

## The 9-question drill (what they actually ask)

1. How did you measure it?
2. What was the baseline, and how was it established?
3. What was n / over what time window?
4. Was it statistically significant? *(If the honest answer is "we didn't test," say so and say what you'd run now — that reads as more senior than a number nobody challenged)*
5. What else changed at the same time?
6. What was **your** contribution vs the team's?
7. What did you try that **failed**?
8. What would you do differently?
9. What is that number today?

## Measurement class — declare it honestly

| Class | Meaning | How to say it |
|---|---|---|
| **A — Instrumented** | Continuously measured in production with a dashboard | *"Instrumented — p50/p95 from our tracing, measured over N weeks"* |
| **B — Sampled / evaluated** | Measured on a sample or an eval set, not continuously | *"Measured on a held-out set of N examples labelled by X"* |
| **C — Directional estimate** | Reasoned from partial data | *"That's a directional estimate — here's what it's based on and here's what I'd instrument to make it real"* |

**Declaring class C proactively is a strength signal.** Getting caught presenting a C as an A is fatal.

---

## Claim 1 — "Cut average LLM latency by about 40%"

- **Claim as written on the resume:**
- **What exactly was measured** (p50? p95? end-to-end? TTFT? which endpoint?):
- **Instrument** (tracing tool / logs / manual timing):
- **Baseline value + date established:**
- **After value + date:**
- **n / time window:**
- **Measurement class (A / B / C):**
- **The mechanism split — how much came from each?** *(prompt shortening · context trimming · prompt-prefix caching · semantic caching · model swap/routing · streaming/TTFT vs total · batching · retrieval funnel reduction)*
- **Biggest confounder** *(traffic mix changed? provider-side model update? cache warm-up? different question distribution?)*:
- **What you tried that failed:**
- **What you'd do differently:**
- **What it is today:**
- **The 25-second spoken answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

> ⚠️ This one and Claim 2 will be attacked in **every single loop**. Do the Week-2 work (Huyen Ch 9 + vLLM docs + PagedAttention) so the answer is a mechanism list with tradeoffs, not a percentage.

---

## Claim 2 — "Cut inference cost by about 30%"

- **Claim as written:**
- **Cost of what** (per query? per conversation? monthly bill? per resolved task?):
- **Instrument:**
- **Baseline + date:**
- **After + date:**
- **n / window:**
- **Measurement class:**
- **The mechanism split:** *(prompt-prefix caching ≈10% of input price — and note ~30% total saving usually comes from prompt* shape*, not the discount alone · semantic cache hit rate · model routing/cascade · output-token reduction — remember output is 2–4× input price · context trimming)*
- **Biggest confounder** *(provider price change? volume discount? traffic drop?)*:
- **Did quality regress? How do you know?** ← ***this is the killer follow-up, and your Week-3 eval harness is the answer***
- **What failed:**
- **What you'd do differently:**
- **Today:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

---

## Claim 3 — "Answer relevance improved by around 35%"

- **Claim as written:**
- **Metric definition** — relevance measured how? *(human rating? LLM judge? thumbs up/down? task completion?)*:
- **Who labelled it, and how many labellers?**
- **Was inter-rater agreement measured?** *(If no: say so. If you can reconstruct it, Cohen's κ)*
- **Baseline + date:**
- **n:**
- **Measurement class:**
- **Was the eval set generated from the indexed chunks?** ← ***the RAG-era data-leakage trap; if yes, say so unprompted — it's a maturity signal***
- **Biggest confounder:**
- **What failed:**
- **Today:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

> ⚠️ Flagged as one of the two most exposed claims on your resume. If the methodology can't be reconstructed, **delete the 35% and keep "improved answer relevance, measured against a hand-labelled eval set"** — then let the Week-3 eval harness be the proof of how you'd do it properly.

---

## Claim 4 — "Manual review turnaround dropped by about 45%"

- **Claim as written:**
- **Turnaround of what, measured from when to when:**
- **Instrument:**
- **Baseline + date:**
- **n / window:**
- **Measurement class:**
- **⚠️ Attribution: this is a Turing client engagement. Do you own or have access to the data?** If not, say so upfront: *"That's the client's measurement, reported back to us — here's how it was defined and here's what I'd want to verify."*
- **Your contribution vs the team's** — you led or co-led several engagements; be specific:
- **Biggest confounder:**
- **What failed:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

---

## Claim 5 — "Agent task success rates rose by around 20%"

- **Claim as written:**
- **Success defined how** — end-state verification? trajectory? tool-call accuracy? **pass@k or pass^k?**
- **Which benchmark / task set, and how many tasks:**
- **Baseline + date:**
- **How many runs per task** *(single-run numbers on agent benchmarks are inflated 5–15 points — if it was single-run, say so)*:
- **Measurement class:**
- **⚠️ Turing client attribution — same question as Claim 4:**
- **Biggest confounder** *(task set changed? model version changed underneath you?)*:
- **What failed:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

> ⚠️ The second most exposed claim. But it's also your best one if it survives — *"deterministic UI state verification"* on your resume **is a verifiable reward function**, and that framing is worth a lot in 2026. Learn to say it that way.

---

## Claim 6 — "Automated content tagging reduced manual effort by roughly 60%"

- **Claim as written:**
- **Effort measured how** — hours? items/person/day? headcount?
- **Baseline + date:**
- **n / window:**
- **Measurement class:**
- **Tagging accuracy** — what precision/recall did the automation hit, and what was the human review rate after?
- **Biggest confounder:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ DELETE

---

## Claim 7 — "~85% accuracy on ~50,000 assessment records" (scikit-learn + Bayesian networks)

**This one invites a 20-minute classical-ML mauling. Prepare it as if for an ML interviewer, not an LLM one.**

- **Claim as written:**
- **What was the class balance?** ← *first question, every time*
- **What was the majority-class baseline?** ← ***if 85% vs a 71% baseline, say the baseline; if the baseline was 82%, the number is nearly meaningless and should be deleted***
- **Why accuracy and not PR-AUC / F1?** *(At low prevalence, accuracy is the wrong metric and they know it)*
- **Train/test split** — random, temporal, or grouped by student? **Was there leakage across the group boundary?**
- **Cross-validation?** Nested?
- **What did the Bayesian network actually do** vs the sklearn classifiers?
- **n = 50,000 records, but how many *students*?** *(records ≠ independent samples — this is the leakage question in disguise)*
- **Calibration** — were the probabilities calibrated, or just the argmax used?
- **Did it ship? What happened in production? Drift?**
- **What failed:**
- **25-second answer:**
- **VERDICT:** ☐ DEFEND  ☐ REPHRASE as precision/recall  ☐ DELETE

> **Prep support:** Coursera **ML Specialization C2 Week 3 "Advice for Applying ML"** (Day 18) is the single best hour available for this claim — baseline/Bayes error, error analysis, the bias-variance intervention ladder.

---

## Scale claims — reframe, don't defend

| On the resume | The problem | Say this instead |
|---|---|---|
| **"knowledge base of 10,000+ documents"** | Laptop-scale. Leading with it invites *"what breaks at 10M?"* — a question you'd currently lose | Lead with **the eval layer and the guardrails**. *"A 10k-document corpus with hallucination guardrails and an automated eval harness — the interesting part was measurement, not volume"* |
| **"around 1M events a day"** | ≈ 12 events/sec. Not a scale story | Sell **pipeline discipline and the analytics/training dual consumption**, not size |
| **"around 50,000 assessment records"** | Small; and records ≠ independent samples | Lead with the **grouping/leakage handling** — that's the senior signal |

---

## Resume edits checklist (Days 1–2)

- [ ] Retitle to **Senior AI Engineer (Agentic Systems & Evaluation)**
- [ ] Add a **"Selected AI/Agent Work"** block **above** the chronology, leading with the Turing eval/environments work
- [ ] Relabel Turing: **`AI Consultant (part-time contract engagement), ~N hrs/week`** — this pre-empts the KNS overlap being read as undisclosed moonlighting
- [ ] Move the three personal projects **above** the older chronology, each with architecture + eval results
- [ ] One consistent experience number, tied to 2016 *(recruiters subtract 2014 from today in four seconds — have a one-line, non-defensive account of 2014–16)*
- [ ] **Delete every metric that failed the 30-second test**
- [ ] Reposition the summary around: *"I build LLM systems that survive contact with production — retrieval, agents, and the eval harnesses that tell you when they break"*
- [ ] Resume budget is **4 hours total for all 4 weeks.** Then stop. interviewing.io's own founder: resume optimisation is low-ROI for candidates without brand names — **direct outreach wins**

## The overlap script (25 seconds, volunteered *before* they find it)

Draft it here, rehearse it 10 times, and say it unprompted in the recruiter screen:

> *"One thing I'll flag upfront — the Turing engagement overlapped my full-time role. It was part-time contract work, roughly N hours a week outside my employment hours. [Your honest account of whether it was disclosed.]"*

**Do not claim you disclosed it in writing unless you did** — background checks do direct employer verification. If you didn't, the honest version is: *"In hindsight I'd have put it in writing, and I would with you."* That's a recoverable answer. A false one isn't.

**Note:** contract work carries no PF, so EPFO/UAN cross-checks won't surface it. The only place it appears is your own resume — which is exactly why you control the framing by volunteering it.
