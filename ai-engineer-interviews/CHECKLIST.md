# AI Engineer Interview Checklist — built from real interview experiences

**What this is.** The other checklist (`../DAILY-CHECKLIST.md`) is organised by *day* and leans heavily on system-design reps. This one is organised by **round type**, and every round below comes from first-person accounts — Glassdoor, AmbitionBox, LeetCode Discuss, Blind, Reddit, GeeksforGeeks interview experiences, candidate Medium/Substack writeups, and company-published process posts.

**Roles covered:** AI Engineer · GenAI Engineer · Applied AI Engineer · LLM Engineer · Agent Engineer · ML Engineer (applied) · Forward-Deployed / AI Solutions Engineer. These share one loop shape with different weightings — the per-round notes flag where they diverge.

**Evidence tags:** `[company, date, source-type]`. `first-person` = a candidate describing their own loop. `company-published` = the employer describing their own process. `aggregate` = review-site or field-guide compilation of many candidate reports. Anything I could only find on a prep-marketing site is excluded or explicitly marked.

---

## The headline finding

Across every account I found, the loop is **3–5 rounds over 2–4 weeks**, and the decisive round is almost never DSA. It's one of these three:

1. **A practical build** — you build something working, in 60 min to 3 days, using real LLM APIs.
2. **Your own project, interrogated to production depth** — chunking, refresh, eval, troubleshooting, "why this and not that."
3. **A customer/discovery conversation** — for FDE and Applied-AI roles specifically.

And the most-asked single question in the entire corpus, across companies and countries:

> **"Explain how RAG works, end to end."**
> *[5+ independent accounts; Sierra uses it as its SWE screen opener — company-published; also Accenture, ZS, Tiger Analytics, Fractal — first-person]*

You do this for a living. That question should be the easiest 90 seconds of your loop, and right now it's unrehearsed. Fix that first.

---

## Round 1 — Recruiter / HR screen  ·  ~100% of loops

**What actually happens:** comp expectation, notice period, location/visa, why-this-company. Short. High rejection rate.

**Real failure modes from accounts:**
- OpenAI FDE: recruiter arrived 5 min late, cut the call 17 min short, rejected for "lacking signals." *[OpenAI, ~2025, Glassdoor first-person]*
- ElevenLabs FDE: verbal approval **withdrawn at final stage over visa/location risk**. *[ElevenLabs, ~2025, first-person]*

**Checklist**
- [ ] One comp number, not a range. India senior AI eng ≈ ₹42–66L Hyderabad / ₹48–72L Bangalore
- [ ] **Force the location/visa question in round 1** for any US/EU company — before you invest 4 weeks
- [ ] Immediate availability stated as an advantage (you have no notice period; most India candidates have 60–90 days)
- [ ] The Turing/KNS overlap volunteered in 25 seconds (script in `../answers/metric-defence.md`)
- [ ] 3 prepared questions about *their* product

---

## Round 2 — The practical coding round  ·  the modal AI-engineer round

This has largely **replaced** LeetCode at AI-first companies. It is project-style: build a small working thing against a real LLM API.

**What was actually given:**

| Task | Company | Source |
|---|---|---|
| Call a flaky API that fails intermittently but eventually succeeds; parse product list with fallback IDs. Graded on **flexible, extensible code — not algorithms** | Sierra | first-person |
| **Build a Voice Activity Detector from scratch, 2.5 hr proctored, ~50 audio files.** Any tool except external APIs. Judged on accuracy, code quality, proposed improvements. *"No DSA was asked."* Offer: ₹84 LPA | Sarvam AI, Dec 2024 | first-person (Blind) |
| File-system permission inheritance with nested-folder conflicts + timestamp resolution — **written in a Google Doc** | ElevenLabs FDE | first-person |
| Sound-classification task in the coding round | Observe.AI, Nov 2025 | Glassdoor |
| 5-part real-world machine-coding problem | Perplexity | first-person (Blind) |
| Parse complex JSON by pattern → feed to LLM → generate summary, 30 min, **ChatGPT allowed** | unnamed GenAI startup, Oct 2024 | first-person (hired) |
| FastAPI API optimisation with an obscure DB driver, **AI explicitly allowed** | LangChain, Mar 2026 | Glassdoor |

**The sub-skills these actually test** — drill these, not LeetCode:
- [ ] Async client with **bounded concurrency** (`Semaphore`), retry with exponential backoff, timeouts. *"100 sequential LLM calls → ≤20 in flight, handle partial failure"* is the archetype
- [ ] Which HTTP codes to retry (429, 5xx) and which not to (4xx). Rate-limit handling
- [ ] Streaming: SSE handling, partial-JSON accumulation, time-to-first-token
- [ ] Cost awareness stated out loud while coding
- [ ] Clean, extensible structure over clever algorithms — Sierra grades exactly this

**Drills (do 6, timed, camera on, talking aloud):**
- [ ] Async batch client: 100 prompts, ≤20 concurrent, retry/backoff, collect partial results
- [ ] SSE streaming handler that accumulates partial JSON into a validated Pydantic model
- [ ] Token-bucket rate limiter for *tokens*, not requests
- [ ] Tool-dispatch loop with retries and a step budget
- [ ] Cosine similarity + top-k in NumPy, batched
- [ ] BM25 and RRF (`Σ 1/(60+rank)`) from scratch — **you use RRF in your own project and must be able to write it**

---

## Round 3 — The OOP / "design a small system in code" round  ·  the lab replacement for LeetCode

Progressive-difficulty, multi-level, 60 min. Common at OpenAI, Anthropic, Databricks.

**Real examples:** in-memory KV store with SET/GET/DELETE, extended level by level *[Anthropic]* · in-memory SQL-like DB / LC-2408 "Design SQL" *[OpenAI L5]* · GPU-credits management system *[OpenAI]* · LRU cache in O(1) *[xAI]* · rate limiter, circuit breaker, thread pool. *[all: first-person compilations]*

- [ ] LRU cache, O(1), from blank file — twice
- [ ] In-memory KV store with TTL, then extend: transactions, then nested transactions
- [ ] Rate limiter (token bucket + sliding window)
- [ ] Practice the *progressive* format: solve level 1 fast and cleanly, because level 4 is where they actually judge you

---

## Round 4 — Debugging / code-review round  ·  blindsides candidates who only prep greenfield

**Real formats:**
- Sierra: **4–5 file agent codebase + intended-behaviour diagram; find and fix ~3 planted bugs**, optimise if time remains *[first-person]*
- Sierra (2026 pilot): pull down a colleague's **draft PR**, review and improve it, "iterating with coding agents" *[company-published]*
- DeepMind: a dedicated **code-review interview** *[Blind]*
- Multi-file phases: find bugs → analyse complexity → implement feature → optimise, ~60 min *[OpenAI, Meta]*

**The canonical AI-specific debugging scenario, seen in 4+ accounts:**
> *"Your RAG gives confident wrong answers. The right document IS in the index. Debug it."*

The expected answer is **not** "switch to a better model" or "re-index." It's: isolate the variable — log exactly what landed in the context window, and split **retrieval failure** (right doc never retrieved / retrieved but ranked below the cutoff) from **generation failure** (right doc in context, model ignored it).

- [ ] Rehearse that answer out loud until it's 60 seconds and structured
- [ ] Memorise your 5-layer agent-failure taxonomy: context → retrieval → tool → orchestration → prompt
- [ ] Practice on a repo you don't know: clone something, plant 3 bugs yourself a week earlier, fix them cold
- [ ] Say the diagnostic *before* the fix. Candidates fail this round by guessing fixes

---

## Round 5 — The take-home  ·  ~33% of loops, and you should win it

**Real specs, with real time budgets:**

| Spec | Company | Budget |
|---|---|---|
| Build on OpenAI APIs + **recorded video walkthrough** | OpenAI FDE | ~5 hr |
| Build an agentic AI application (1 of 2 briefs) | Eightfold, Nov 2025 | ~1 week |
| Agent build against a provided API key, then a **60-min "why" defense** | Sierra | — |
| Timed assessment | Harvey | 1 hr |
| RAG over PDFs with citations; must say "I don't have that information" when unsupported | 5+ companies — **>40% of all AI take-homes** | 2–4 hr |
| Refactor a deliberately messy RAG app; preserve API behaviour, kill global mutable state, make it testable | BitHealth | — |
| Sales-insights agent that **detects and refuses PII requests**, passes only aggregates to the LLM | Cohere-adjacent | — |
| Graph workflow engine, max 50 steps, **infinite-cycle protection required, unit tests mandatory** | Tredence | — |
| Turnaround **within 24 hours** | Fireworks | 24 hr |

**What graders actually reward** *[practitioner reports + one leaked rubric: 30% functionality, 30% challenge completion, 25% context engineering, 15% code quality]*:
- [ ] **Start with the eval harness.** "Doesn't start with evals" is documented red flag #1 at YC-startup graders
- [ ] README stating trade-offs and *rejected alternatives*
- [ ] Cost + latency table
- [ ] Error handling, retries, and a test that the AI output is actually validated
- [ ] A Loom/video demo (repeatedly cited as a differentiator)
- [ ] Configurability (one candidate's config-file-driven CLI "got two competing offers within 72 hours")

**The time trap:** advertised 2–4 hr, real spend routinely 2×+. One Anthropic candidate: **"listed as 5 hours, took 15."**
- [ ] **Build the reusable skeleton before you apply** — FastAPI + hybrid retrieval + RRF + rerank + citations + eval harness + Docker + README. Then each take-home is 4 h of customisation, not 14
- [ ] Refuse anything >4 h scope offered before a human conversation

---

## Round 6 — Your project, interrogated  ·  the most-failed round at labs

**This is the highest-frequency deep round in the India corpus** — at Accenture, ZS, Tiger Analytics, Fractal, McKinsey QB the loop is *substantially* this round.

**Real questions, verbatim:**
- "What are you storing in the Vector Database?" · "Explain step by step how RAG works behind the scenes" · "What is the key difference between a Generative AI system and an Agentic AI system?" · "Have you heard about MCP?" · "Which framework did you use (LangChain or CrewAI) and why?" · "Can agents work asynchronously in CrewAI?" *[Accenture LLM Ops, Dec 2025, first-person — selected]*
- Scenario grilling on the candidate's own pipeline: chunking strategy, vector-DB choice **and alternatives**, how you refresh embeddings when source data updates, retrieval flow, evaluation, production troubleshooting *[Tiger Analytics, Nov 2025, Glassdoor first-person]*
- "Why did you fine-tune LLaMA?" · vector-DB alternatives *[Fractal, Dec 2024, first-person]*
- "Tell me about the biggest project you're proud of — **be specific about what *you* built yourself**" *[ElevenLabs, first-person]*
- Deep dive on the most complex thing you've shipped — **repeatedly called the hardest round in the loop** *[OpenAI Applied, first-person Blind]*

**Checklist**
- [ ] Lead with the **AML/CTF compliance RAG** — sole ownership, no client-attribution risk, and it's a complete senior retrieval architecture
- [ ] Architecture reproducible on a whiteboard in 3 min → **use `../diagrams/01-aml-ctf-compliance-rag.excalidraw`**
- [ ] 3 decisions you can defend *with the alternative you rejected* — RRF vs score-fusion; cross-encoder rerank vs bigger top-k; **tenant isolation as a SQL predicate vs a prompt instruction** (know exactly why prompt-level isolation fails)
- [ ] 2 real failures and what they cost
- [ ] The "what breaks at 100×" answer — 6-move template in `../story-bank.md`
- [ ] **"How do you refresh embeddings when the source changes?"** — asked verbatim; have the incremental-reindex answer ready
- [ ] Every metric defended per `../answers/metric-defence.md`

> **Honesty beats bluffing here, with evidence:** the Accenture candidate couldn't write live code for one prompt, *"simply told him honestly,"* and **was still selected**. The GenAI-intern candidate had never used CrewAI before the take-home and got hired anyway. Both cited clarity of thought over buzzwords.

---

## Round 7 — LLM / ML theory  ·  ~50% of loops, and the classical-ML ambush is real

### The recurring questions (frequency-ranked from independent accounts)

**LLM fundamentals**
- [ ] Explain self-attention / how transformers work **[5+ accounts]** — labs may ask you to *code* it
- [ ] Temperature / top-p / top-k and their effect **[3–4]**
- [ ] Context window: what happens when you exceed it; how to extend **[3–4]**
- [ ] KV cache: what it is, why it speeds inference, **calculate its size** **[3]**
- [ ] Tokenization: BPE vs WordPiece **[3]** — and **Indic token inflation (3–8× per char)**, which is *your* differentiated answer
- [ ] Encoder-only vs decoder-only vs encoder-decoder, and when **[2]**
- [ ] Why hallucinations happen and what forms they take **[3–4]**
- [ ] MoE — what and why **[2]**

**RAG (the densest bucket)**
- [ ] Explain RAG end to end **[5+ — the single most-asked question in the corpus]**
- [ ] Fine-tune vs RAG vs prompt engineering — the decision framework **[4]**
- [ ] What drives chunk size? How do you chunk tables and PDFs? **[3]**
- [ ] Scale RAG to 10M+ documents / retrieval is too slow, fix it **[3]**
- [ ] Hybrid search, BM25 + vector, RRF **[2–3]**
- [ ] HNSW / vector-DB internals; vector DB vs traditional DB **[2]**
- [ ] How to choose and benchmark an embedding model **[2]**

**Agents**
- [ ] Production agent architecture — **what logic lives in the orchestrator vs the LLM** **[3]**
- [ ] How does the agent choose a tool? What happens when a tool fails — retries, idempotency **[3]**
- [ ] Detecting and stopping infinite planning loops; termination conditions **[3]**
- [ ] When is an agent the *wrong* solution? **[2]**
- [ ] Sandboxing, prompt injection via tool output **[2–3]**
- [ ] MCP — rising but still rare in verbatim reports; asked directly at Accenture. Know the control model (tools = model-controlled, resources = app-controlled, prompts = user-controlled)

**Evals**
- [ ] How do you evaluate a RAG pipeline / chatbot? (faithfulness, answer relevancy, context precision/recall) **[5+]**
- [ ] LLM-as-judge: how it works and its failure modes **[3]**
- [ ] Building a golden dataset from a vague spec **[3]**
- [ ] Measuring hallucination rate in production **[3–4]**

**Fine-tuning** *(decision-level, not PyTorch mechanics, for product AI-eng roles)*
- [ ] LoRA / QLoRA / PEFT — what and when over full FT **[4]**
- [ ] RLHF vs DPO; reward hacking **[3]** — **DPO vs PPO asked directly at Flipkart**
- [ ] Why quantization barely hurts accuracy **[3]**
- [ ] Catastrophic forgetting **[2]**

**Inference / cost**
- [ ] "1M queries/day — reduce token cost" **[4]**
- [ ] Design an inference batching system (single GPU, ≤100/batch) — **Anthropic reuses this across SWE, ML, hardware and EM loops** **[2–3]**
- [ ] TTFT and why streaming matters **[3]**
- [ ] Model tiering/routing, exact + semantic caching, provider failover **[3]**

### ⚠️ The classical-ML ambush — the most-reported surprise

> An Amazon Applied Scientist candidate was *"surprised by the depth of classical ML questioning despite focusing on modern deep learning"* — and was asked to **derive entropy and Gini by hand**. *[Nov 2025, first-person]*
>
> A McKinsey QuantumBlack candidate was **rejected in round 5 on traditional-ML case studies**: *"wasn't aware of how I can solve those and couldn't find material to study."* *[Nov 2025, first-person Blind]*

**GenAI-only prep is a repeatedly-documented losing strategy.** And this is precisely your `~85% accuracy / 50k records / Bayesian networks` resume line's home turf.

- [ ] Bias–variance, regularization (L1 → sparsity, and *why*), overfitting interventions
- [ ] Precision/recall/F1, ROC-AUC **vs PR-AUC at low prevalence**, threshold from a cost matrix
- [ ] Class imbalance; why SMOTE is the wrong first answer
- [ ] Data leakage taxonomy — including **grouped splitting** (your 50,000 records ≈ 4,150 students)
- [ ] Bagging vs boosting and when; how to pick k in clustering; optimizers
- [ ] Implement k-means / logistic regression / cosine similarity **in NumPy from scratch** — asked at Mistral (logreg with SGD + L2 + early stopping) and Amazon (cosine similarity)
- [ ] Full model-family sweep: linear → trees → NN → RNN/LSTM → LLMs, **plus offline validation for each**

---

## Round 8 — DSA  ·  survives at ~one round, LC easy-medium, at unicorns and GCCs only

**Evidence for how much it actually matters:**

*Absent at:* Sarvam (*"No DSA was asked"*) · Accenture LLM Ops (zero) · Tiger Analytics (3 rounds, all project-scenario) · Observe.AI (domain task instead) · Anthropic/OpenAI/Scale in one documented Fall-2024 loop (**zero classic LeetCode** — OOP rounds instead).

*Present at:* Groww (full LC round first) · Amazon AS (OA + dedicated DSA round) · Eightfold (graph DSA even after an agentic take-home) · Salesforce LMTS (2× LC medium in 75 min) · Adobe ("basic LeetCode-type") · Fractal (one medium sliding-window) · ZS (two easy-mediums *inside* the LLM round) · Glean (LC medium/hard — the AI-native outlier) · Perplexity OA (*"wildly difficult"*) · Google, Meta, DeepMind.

**Actual problems named in accounts:** Single Element in a Sorted Array · Container With Most Water · Minimum Window Substring · distance between two nodes of a binary tree · islands grid + BFS · minimum coins (1-D DP) · longest repeated substring · detect cycle in linked list · 2-Sum · max-stack · graph BFS with directions · prime check · anagram check.

**Your read, given near-zero baseline:**
- [ ] Target the segment where DSA is absent — AI-first startups, services-to-AI (Accenture/ZS/Tiger/Fractal class), FDE roles. **That's most of your realistic pipeline anyway**
- [ ] Keep 90 min/day on NeetCode 150 per `../DAILY-CHECKLIST.md` — the named problems above cluster hard in arrays/hashing, sliding window, trees, graphs/BFS, 1-D DP. **No hard DP**
- [ ] Don't burn a Google/Meta/Databricks application until the week-12 gate

---

## Round 9 — AI-assisted coding  ·  rapidly growing, and structurally your advantage

**Real formats:**
- **Meta** (piloted Oct 2025): 60 min, 3-panel CoderPad — file explorer / editor / AI assistant — iterating on a **multi-file project**. Replaces one of two onsite coding rounds. The other round stays AI-free. *[company + first-person]*
- **Microsoft**: solve with ChatGPT, then **the interviewer mutates the problem and watches you re-prompt** *[first-person]*
- **Sierra**: 2-hour solo Build phase with "the AI tooling and frameworks of their choice" *[company-published]*
- **Cursor**: AI banned except autofill in early checks, then a **paid 2-day work trial** *[CEO, June 2025]*

**The trap, reported consistently:** the problem is tuned so the model *can't* solve it alone. Blind prompting hits dead ends, and you must defend every line.

- [ ] 5 recorded sessions narrating: decompose → delegate a subtask → **verify the output** → integrate
- [ ] Loud catches: *"the model generated raw SQL here — I'm parameterising it"*
- [ ] Know when to stop the agent and write it yourself
- [ ] **Ask the recruiter per round** whether AI is allowed — several companies split it round-by-round
- [ ] One prepared story where you deliberately did **not** use AI

> **Never use an AI interview copilot.** ~1/3 of surveyed FAANG interviewers have caught suspected AI cheating; 11% run detection software; Meta mandates full-screen share. It's a permanent-blacklist event.

---

## Round 10 — Customer / discovery conversation  ·  ~60% of FDE and Applied-AI loops

**Real scenarios:**
- Airline CTO wants rescheduling automation — graded on **discovery questioning and pain-point identification, explicitly not on jumping to an AI solution** *[ElevenLabs FDE, first-person]*
- Discovery-call roleplay with the hiring manager *[Fireworks, Glassdoor first-person]*
- Open-ended customer solution design: *"Who uses this? What decisions do they make? What does success look like?"* *[OpenAI FDE, first-person]*

**The documented failure mode: candidates pitch a solution instead of investigating.**

- [ ] **Rule: no solution until you've asked five questions**
- [ ] 3 recorded reps with a peer playing "VP Eng at a 5,000-person fintech"
- [ ] Your 6+ client engagements at Turing are the story bank here — you've done this work, you've just never rehearsed it as an interview format

---

## Round 11 — System design  ·  GenAI-flavoured, not classic distributed systems

Real prompts: *"Design a RAG system for a customer support chatbot"* (**reported as the single most common opener**) · inference-serving for large models *[Mistral]* · retrieval/search architecture *[Glean]* · ML infra: feature stores, distributed training, serving *[Databricks]* · job-scheduler LLD+HLD *[Salesforce]* · product decomposition: messy manual workflow → UI + API + backend *[ElevenLabs]*.

Your existing 28-day plan already over-serves this round. Keep those reps, and just add:
- [ ] The customer-support-chatbot RAG design, cold, timed — it's the most likely single prompt you'll get
- [ ] Cost and latency arithmetic out loud, every rep
- [ ] `evidentlyai.com/ml-system-design` — 800 real case studies from 150+ companies. *"DoorDash does X, we'd do Y because our constraint is Z"* is the highest-value sentence in this round

---

## Round 12 — Behavioral / HM  ·  ~90% of loops

- [ ] 10-story bank per `../story-bank.md`, **"I" not "we"** — your Turing client stories are the exposure
- [ ] The two missing stories: a failure with a named cost; a disagreement you lost and then committed to
- [ ] Company-specific motivation — checked everywhere, and India loops ask *why-this-company* directly
- [ ] Expect India-specific oddities: **family-background questions** were asked at both ZS and Fractal *[first-person, 2024]*
- [ ] Amazon: 45-question Leadership Principles battery **inside the OA** *[Nov 2025, first-person]*

---

## The 14-day drill rotation

Run this **alongside** the existing 28-day plan. It replaces the design-rep blocks (block C on Sat, and roughly half of block A), and leaves DSA/blocks B untouched.

| Day | Drill | Output |
|---|---|---|
| 1 | "Explain RAG end to end" + "fine-tune vs RAG vs prompt" | 2 recordings, 90 s each |
| 2 | Async batch client: 100 prompts, ≤20 concurrent, retry/backoff | Working code + tests |
| 3 | The RAG-debugging scenario, out loud; 5-layer failure taxonomy | 1 recording |
| 4 | BM25 + RRF from scratch; cosine top-k in NumPy | Working code |
| 5 | AML/CTF project deep dive, 20 min, using the Excalidraw diagram | 1 recording |
| 6 | Classical-ML ambush drill: baseline, PR-AUC, grouped splitting, leakage | Written answers |
| 7 | Rest |
| 8 | LRU cache + KV store with TTL, progressive levels | Working code |
| 9 | Take-home skeleton: FastAPI + hybrid retrieval + eval harness | Repo scaffold |
| 10 | SSE streaming + partial-JSON accumulation; token-bucket limiter | Working code |
| 11 | Customer-discovery roleplay ×3 (peer or recorded solo) | 3 recordings |
| 12 | Debug an unfamiliar repo with 3 planted bugs, 45 min | Fix log |
| 13 | "Design a RAG system for a customer support chatbot", cold, 45 min | 1 recording |
| 14 | Full mock: practical coding + project deep dive | Debrief page |

**Exit test:** a 60-minute self-run mock containing one practical build, one RAG-debug scenario, and a 20-minute project interrogation — all answered without notes.

---

## What the accounts say kills candidates

1. **Vague, team-level project narration.** *"Be specific about what YOU built"* — the most-failed round at labs.
2. **GenAI-only prep** — the classical-ML ambush ends loops at Amazon, McKinsey, Flipkart.
3. **No evals in the take-home** — documented red flag #1.
4. **Pitching instead of investigating** in discovery rounds.
5. **Blind AI dependence** in AI-assisted rounds — the problems are tuned to defeat it.
6. **Assuming AI-native means no LeetCode** — Glean, Perplexity, Windsurf, DeepMind all still gate on it.
7. **Not forcing the location/visa question early** — ElevenLabs withdrew a verbal approval over it.
8. **Take-home time inflation** — 5 listed, 15 actual. Build the skeleton first.
