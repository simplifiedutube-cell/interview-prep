# Real Questions Asked — AI Engineer / GenAI / Applied AI / MLE / FDE roles

Every question here comes from a first-person interview account or a company-published process description. Nothing from prep-site listicles.

**Frequency:** `[5+]` seen in five or more independent accounts · `[3-4]` · `[2]` · `[1]` single but credibly attributed.
**Tags:** `[company, date, source]`. Where a question recurs across many companies, the tag names the most specific attested instance.

---

## 1. RAG & retrieval — the densest bucket in the entire corpus

**Lead with these five. They recur more than anything else in AI-engineer loops.**

1. **"Explain how RAG works, end to end."** `[5+]` — *Sierra uses it as its SWE screen opener [company-published]; also Accenture Dec 2025, ZS late 2024, unnamed GenAI intern Oct 2024 [all first-person]*
2. **"When do you fine-tune vs use RAG vs just prompt engineering?"** `[4]` — *[Mistral, McKinsey QB, field-guide aggregate]*
3. **"What drives chunk size? How do you chunk tables and PDFs?"** `[3]` — *[Tiger Analytics Nov 2025, first-person]*
4. **"Your RAG hallucinates even though the right context was retrieved. Fix it."** `[4]` — *[multiple; also a debugging-round staple]*
5. **"Scale this to 10M+ documents"** / **"retrieval is too slow, speed it up"** `[3]`

Then:
- "What are you storing in the Vector Database?" — *[Accenture LLM Ops, Dec 2025, first-person, verbatim]*
- "What are embeddings?" / "How does chunking happen?" — *[GenAI intern, Oct 2024, first-person, verbatim]*
- **"How do you refresh embeddings when the source data updates?"** — *[Tiger Analytics, Nov 2025, Glassdoor first-person]* ← asked directly; have the incremental-reindex answer
- "Which vector DB did you choose and what are the alternatives?" — *[Tiger Analytics; Fractal Dec 2024, both first-person]*
- Hybrid search: BM25 + vector, RRF, text-vs-vector trade-offs `[2-3]`
- Vector DB internals: HNSW / LSH indexing; vector DB vs traditional DB `[2]`
- How do you benchmark and choose an embedding model for your data `[2]`
- Citations / source attribution; answering "I don't know" when context is insufficient `[3]` — *an explicit requirement in 5+ real take-homes*
- Semantic caching `[2]`
- Reranking: why, and what it costs you in latency
- "Latest advancements in GenAI" — hybrid RAG, multimodal agents, MoE-LLaVA — *[ZS, late 2024, first-person]*

---

## 2. LLM & transformer fundamentals

1. **"Explain self-attention / how do transformers work."** `[5+]` — *asked everywhere from Adobe to frontier labs; labs may ask you to* code *it*
2. **"Temperature, top-k, top-p — what do they do?"** `[3-4]` — *[ZS, first-person, verbatim]*
3. **"What is the context window? What happens when you exceed it? How do you extend it?"** `[3-4]`
4. **"What is the KV cache, why does it speed up inference, and how big is it?"** `[3]`
5. **"Explain tokenization — BPE vs WordPiece."** `[3]`

Then:
- Encoder-only vs decoder-only vs encoder-decoder, and when to use each `[2]` — *[Sarvam, Dec 2024; Amazon AS, Nov 2025]*
- "Why do hallucinations happen, and what forms do they take?" `[3-4]`
- Mixture of Experts — what and why `[2]`
- BERT vs GPT; masked vs causal language modelling — *[Amazon AS Intern, Nov 2025, first-person]*
- "Attention is O(N²) — how do Sparse/Flash Attention help?" — *[Amazon AS Intern, Nov 2025, first-person]*
- Softmax and the temperature parameter (rapid-fire phone-screen style) `[2]`
- RNN vs LSTM, "why transformers" — *[Capgemini GenAI, Aug 2025, first-person]*
- "Explain the Whisper-JAX architecture" · optimizing Whisper latency · VAD on CPU vs GPU — *[Sarvam AI, Dec 2024, first-person]* ← **directly relevant to your voice agent**
- Benchmark literacy: define MMLU, HELM, HumanEval, Big-Bench — *[ZS, late 2024, first-person]*

---

## 3. Agents, tool use & MCP

1. **"Walk me through a production agent architecture — what logic lives in the orchestrator vs the LLM?"** `[3]`
2. **"How does the agent decide which tool to call? What happens when a tool fails — retries, idempotency?"** `[3]`
3. **"How do you detect and stop infinite planning loops? Implement termination conditions."** `[3]`
4. **"When is an agent the wrong solution?"** `[2]`

Then:
- "What is the key difference between a Generative AI system and an Agentic AI system?" — *[Accenture, Dec 2025, first-person, verbatim]*
- **"Have you heard about MCP?"** — *[Accenture, Dec 2025, first-person, verbatim]*. MCP is rising but still rare in verbatim reports `[1-2]`. Know the control model: tools = model-controlled, resources = app-controlled, prompts = user-controlled
- "Which framework did you use — LangChain or CrewAI — and why?" · "What are the components of CrewAI?" · "Can agents work asynchronously in CrewAI?" — *[Accenture, Dec 2025, first-person, verbatim]*
- Sandboxing tool execution; prompt injection via retrieved content or tool output `[2-3]`
- "Explain ReAct — with code" `[2]`
- Design a customer-support-ticket or code-review agent `[2]` — *[Scale: insurance-claims agent with cost control; Sierra: customer-service agents]*
- Agent misbehaviour triage: loops forever / over-plans / picks wrong tools — detect, add termination + observability

---

## 4. Evaluation

1. **"How do you evaluate an LLM system / RAG pipeline / chatbot?"** `[5+]` — expects faithfulness, answer relevancy, context precision/recall vocabulary; **an explicit rubric item in 10%+ of real take-homes**
2. **"How do you detect and measure hallucination rate in production?"** `[3-4]`
3. **"How does LLM-as-judge work, and how does it fail?"** `[3]`
4. **"How would you build a golden dataset from a vague spec?"** `[3]`

Then:
- "Metrics beyond perplexity for generation quality" `[2]`
- "How would you evaluate the quality of an LLM's response — what criteria for correctness, relevance, clarity?" — *[Turing LLM Trainer, 2024-25, Glassdoor]*
- "The model is confident but factually wrong in a high-risk context — diagnose it" — *[Anthropic ML track]*
- Separating **retrieval** metrics (recall@k, MRR, nDCG) from **generation** metrics (groundedness, citation correctness) — *knowing these are two different eval problems is itself a differentiator*
- A good reverse-question candidates report asking: *"Is there an actual eval framework here, or is it vibes-based?"*

> **Never name RAGAS as your talking point.** Say instead: *"We started with RAGAS-style metrics, found they didn't correlate with our reviewers' judgments, so we built a domain-specific binary judge and validated it against 100 hand-labelled traces."*

---

## 5. Fine-tuning & training

*For product AI-engineer roles this is tested at the level of* decisions*, not PyTorch mechanics. Training-loop questions concentrate in research-engineer tracks.*

1. **"What is LoRA / QLoRA / PEFT, and when over full fine-tuning?"** `[4]`
2. **"Explain RLHF. Compare with DPO."** `[3]` — **"reward policies: DPO vs PPO" asked directly** *[Flipkart DS2 Foundational Model Team, 2025, first-person]*
3. **"Why does quantization barely hurt accuracy? What are the trade-offs?"** `[3]`
4. Instruction tuning vs pre-training `[2]` · catastrophic forgetting `[2]` · "how would you fine-tune with limited data?" `[2]`

Also seen: fine-tuning LLMs **and VLMs**; "explain your VLM's architecture and justify the design choices" — *[Flipkart; Amazon AS, both first-person]*

---

## 6. Inference, serving & cost

1. **"You get 1M queries/day — reduce token cost."** `[4]`
2. **"Design an inference batching system"** (single GPU, ≤100 inputs/batch, synchronous users) `[2-3]` — *Anthropic reportedly reuses this across SWE, ML, hardware and EM loops*
3. **"What is time-to-first-token, and why does streaming matter?"** `[3]`
4. Model tiering / routing, exact + semantic caching, provider failover `[3]`
5. Handling 429s and rate limits: exponential backoff, which codes to retry `[2-3]`

Also: quantization/distillation for serving `[2]` · KV-cache sizing · distributed training + non-LeetCode coding — *[Nvidia, 2025, first-person]* · KV-cache, LoRA, beam search, MoE routing at Nvidia LLM teams

---

## 7. Classical ML — the ambush bucket

**Do not skip this because you're targeting GenAI roles.** Two documented rejections trace directly to it.

1. **"What was the class balance? What does a majority-class baseline get?"** — the first question on any accuracy claim
2. **Bias–variance, overfitting scenarios, regularization** — *"explain the gradient effects that make L1 produce sparsity"* *[DeepMind, first-person]*
3. **Precision/recall/F1, ROC-AUC vs PR-AUC at low prevalence, threshold from a cost matrix**
4. **Bagging vs boosting, and when to use each** — *[Amazon AS, late 2025, first-person]*
5. **Implement from scratch in NumPy:** logistic regression with SGD + L2 + early stopping *[Mistral]* · cosine similarity *[Amazon GenAI L6]* · k-means / KNN / decision tree `[4]`

Then:
- **Compute entropy and Gini by hand** — *[Amazon AS Intern, Nov 2025, first-person — a reported surprise]*
- How to pick the number of clusters; optimizers; activation and loss functions; LR schedules; vanishing gradients `[3]`
- Data leakage; train/test split design; **grouped splitting** `[2]`
- Bayesian coin-toss coding problem — *[Amazon AS, first-person]*
- Full sweep in one round: linear → logistic → trees → NN → RNN/LSTM → LLMs, **plus offline validation for each** — *[LinkedIn Senior AI Eng, ~2024, first-person — rejected]*
- Logistic regression depth + CLIP/BLIP in a "Depth in Math Modelling" round — *[Flipkart, 2025, first-person]*
- Traditional-ML **case studies** — *[McKinsey QuantumBlack, Nov 2025, first-person — this is what he was rejected on]*

---

## 8. Practical coding tasks actually given

Ranked by frequency across accounts.

1. **Project-style LLM-API build** — a small working feature calling OpenAI/Anthropic live, with async retry, backoff, timeouts, streaming, cost awareness. 45–90 min. **The modal AI-engineer coding round.**
2. **OOP multi-level toy systems** (the lab replacement for LeetCode), 60 min, progressive levels: in-memory KV store with SET/GET/DELETE *[Anthropic]* · in-memory SQL-like DB / LC-2408 "Design SQL" *[OpenAI L5]* · GPU-credits management system *[OpenAI]* · LRU cache O(1) *[xAI]* · rate limiter, circuit breaker, thread pool
3. **ML classics in NumPy**, 20–45 min — logistic regression w/ SGD *[Mistral]*, cosine similarity *[Amazon]*, k-means, then overfit on toy data
4. **Transformer components from scratch** — causal self-attention, softmax, layer norm, beam search, LoRA layer, KV cache. Adobe asked attention in TF + NumPy *[first-person]*. **Common for lab/research-adjacent roles, rare at product startups**
5. **Mini-RAG build** — dominant as a take-home (40%+ of all real take-homes), occasionally live in 60–90 min
6. **Agent / tool-calling loop build** — 30%+ of take-homes
7. **AI-assisted coding round** — drive an AI to fix/extend a multi-file codebase *[Meta Oct 2025; Microsoft]*
8. **Eval harness / LLM-judge build** — usually a take-home sub-requirement *[Hippocratic AI: Spec Builder → Storyteller → LLM Judge → Rewriter]*
9. **Refactor messy code** — OpenAI: refactor 100–120 lines of deeply nested code · BitHealth: refactor a messy RAG app preserving API behaviour
10. **Domain-specific builds** — Voice Activity Detector from scratch, 2.5 hr *[Sarvam]* · sound classification *[Observe.AI]* · streaming Whisper transcription + SSE insight extraction

**Rare but reported:** implement a research paper live *[Contextual AI]* · autograd from scratch · website crawler · OCR + LLM document-extraction pipelines

---

## 9. Debugging scenarios

1. **"RAG gives confident wrong answers — the right doc IS in the index. Debug it."** `[4+]` — the canonical scenario. Expected: don't guess ("switch to GPT-4", "re-index"); isolate via trace logs, inspect exactly what landed in the context window, split **retrieval failure** from **generation failure**
2. **Debug a hallucinating prompt** — given prompt + source doc + 5 sample outputs, some hallucinated: find root cause, propose targeted fixes. 20–30 min
3. **Find ~3 planted bugs in a 4–5 file agent codebase**, with an intended-behaviour diagram; interviewer narrates scenarios *[Sierra, first-person]*
4. **Review and improve a colleague's draft PR**, iterating with coding agents *[Sierra 2026 pilot, company-published]*
5. **Model/training code with planted issues** — explain why performance is bad, fix it
6. **Multi-file phases**: find bugs → analyse complexity → implement feature → optimise, ~60 min. *Orientation eats 5–6 min; budget ~35–40 min of real work*
7. **Agent misbehaviour triage** — loops forever, over-plans, wrong tools
8. **Senior variant:** a failing production pipeline — propose and *prioritise* a debugging plan (cost spike, quality regression, latency)
9. **AI-assisted twist:** your AI-generated solution breaks when the interviewer mutates the problem — debug your own prompt *[Microsoft, first-person]*

---

## 10. System design prompts

- **"Design a RAG system for a customer support chatbot"** — reported as the single most common opener
- Design ChatGPT / LLM inference serving at scale — queueing, GPU worker scheduling, TTFT, streaming, fairness across tiers
- Inference-serving system for large models; training clusters *[Mistral]*
- Retrieval / search architecture *[Glean]*
- ML infra: feature stores, distributed training, serving *[Databricks, late 2025]*
- "Improve the Task Queue System" *[Notion, Nov 2025, first-person]*
- Job scheduler, LLD + HLD *[Salesforce LMTS India, Sept 2025, first-person]*
- Product decomposition: messy manual workflow → design UI, API and backend end-to-end *[ElevenLabs]*
- GenAI business case studies *[McKinsey QB]* · product-underperformance KPI case *[Microsoft IDC]*

---

## 11. DSA problems actually named in accounts

*Cluster: arrays/hashing, sliding window, trees, graphs/BFS, 1-D DP. No hard DP appears anywhere in this corpus.*

Single Element in a Sorted Array · Container With Most Water *[Groww, Oct 2025]* · Minimum Window Substring · distance between two nodes of a binary tree *[Amazon AS, Nov 2025]* · islands grid + BFS shortest path · Minimum Coins (1-D DP) *[Amazon AS]* · longest repeated substring ("banana" → "ana") · detect cycle in a linked list *[ZS, late 2024]* · medium sliding-window *[Fractal, Dec 2024]* · graph BFS with directions *[Eightfold, Dec 2025]* · 2-Sum, Python slicing/scope, constructors *[Quantiphi, 2024]* · max-stack, k-th greatest in subarrays, positive/negative reorder *[Salesforce LMTS, 2025]* · primes, anagram check *[GenAI intern, Oct 2024]* · kth largest across m sorted arrays, min-distance-in-string + 2D Manhattan, prove median minimises sum of absolute deviations *[Glean, 2024-25]* · graph shortest path *[Google SWE III AI/ML, early 2025]* · Connect4 backend *[Glean SDE II]*

---

## 12. Prompt engineering

- Structured outputs / reliable JSON `[3]` — *strict JSON required in several real take-homes*
- Prompt injection & jailbreak defenses `[3]` — *one take-home is literally "resist prompt injection"*
- In-context learning; zero/few-shot; CoT vs ToT and when `[2-3]`
- **"Which prompt techniques improved quality in your real projects?"** `[2]` — *interviewers probe for lived experience, not taxonomy*

---

## 13. Behavioral & the India-specific oddities

- **"Tell me about the biggest project you're proud of — be specific about what YOU built yourself"** *[ElevenLabs, first-person]*
- Deep dive on the most complex thing you've shipped — **repeatedly the hardest round** *[OpenAI Applied, first-person]*
- Ownership, ambiguity, explaining technical limitations to non-technical stakeholders *[OpenAI FDE HM round]*
- Why-this-company motivation checks — **everywhere**, and India loops ask directly
- **45-question Leadership Principles battery inside the OA** *[Amazon, Nov 2025, first-person]*
- **Family-background questions** *[ZS and Fractal, both 2024, first-person]* — unusual to Western candidates, normal in Indian services-firm loops
- "Have you led a project / handled conflict?" · managing internship alongside coursework *[Fractal]*

---

## 14. Adjacent-stack questions that appear inside "AI engineer" loops

Don't be caught out — these were asked in AI-titled interviews:

- "What is Docker?" · "Why Selenium?" · "Have you heard about Redis?" *[GenAI intern, Oct 2024, first-person]*
- REST methods, PUT vs PATCH, `__init__` and dunder naming *[Accenture, Dec 2025, first-person]*
- async/await, DOM manipulation *[Fractal, Dec 2024, first-person]*
- AWS SageMaker / Azure ML / Databricks + networking *[Mastercard GenAI, ~2025]*
- AWS Bedrock usage *[ZS, late 2024]*
- SQL: joins, p-test/t-test, random forest, clustering scenarios *[Flipkart DS, Nov 2025]* · medium SQL in the OA *[Fractal]* · top-5 customers by revenue in 30 days
- Java + GenAI + "core subjects mentioned in your resume" *[Walmart Global Tech India, 2025]*

---

## Source notes

**Primary (first-person):** Blind threads (Sarvam MLE, OpenAI Applied, Anthropic Applied AI, Cursor work trial, Meta AI-enabled round, McKinsey QB, Intuit, DeepMind) · LeetCode Discuss (Groww, Eightfold, Flipkart DS2, Salesforce LMTS, Glean full loop/MLE/SDE-II, Nvidia) · GeeksforGeeks interview experiences (Accenture LLM Ops Dec 2025, ZS LLM Engineer, Quantiphi) · Medium (Amazon AS Intern ×2, Eightfold, Fractal, Google SWE III AI/ML, GenAI engineer hired Oct 2024) · gaijineer.co (Sierra SWE-Agent, OpenAI FDE) · Taro (Notion Nov 2025, Adobe Oct 2025, Capgemini Aug 2025, Glean Bengaluru) · Exponent experiences (ElevenLabs Solutions Architect).

**Company-published:** Sierra "The AI-native interview" · Anthropic candidate AI-usage guidance · Anysphere/Cursor CEO via Business Insider Jun 2025 · Decagon "Introducing the Agent Engineer".

**Aggregate:** Glassdoor / AmbitionBox interview sections · `alexeygrigorev/ai-engineering-field-guide` (51 documented company processes, ~60 real take-homes with candidate submissions) · interviewing.io interviewer survey (67 FAANG+ interviewers, 2025).

**Caveats.** (1) Blind, LeetCode and Grapevine partially block automated fetching; several details came from search-index snippets rather than full threads. (2) Verbal-question frequencies are **floor estimates** — the true counts are higher. (3) The take-home inventory skews toward candidates who publish submissions publicly (startup/India/EU-heavy); US big-tech take-homes are under-represented because they're NDA'd. (4) Krutrim, Postman, Hasura, Atlan, Chargebee, CRED, PhonePe, Swiggy and several US AI-natives (Vapi, Retell, Braintrust, Baseten, Together, Pinecone, Weaviate, Qdrant, LlamaIndex, Cognition) surfaced **no verifiable first-person AI-role accounts** — claims about them elsewhere are prep-site marketing and were excluded.
