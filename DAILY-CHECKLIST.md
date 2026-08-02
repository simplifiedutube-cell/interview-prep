# 28-Day Interview Sprint — Daily Checklist

**Start date:** ______________  ·  **Target: 8h/day, Mon–Sat, Sunday fully off**

---

## The standing day (every Mon–Sat)

These repeat daily and are not re-listed per day. Tick them in `tracker.csv`, not here.

| Time | Block | What |
|---|---|---|
| 08:00 | **0 · Retrieval warm-up** (30m) | Closed-book on blank paper: yesterday + one item each from day −3, −7, −21. Then check. Anki 25 min lives here |
| 08:30 | **1 · Hard block A** (90m) | ↓ see the day |
| 10:00 | break (20m) | Walk outside. No phone |
| 10:20 | **2 · Hard block B — DSA** (90m) | ↓ see the day. **Timed, spoken aloud, camera on** |
| 11:50 | lunch (45m) | |
| 12:35 | **3 · Hard block C — Build** (75m) | ↓ see the day |
| 13:50 | break (15m) | |
| 14:05 | **4 · Low-energy block** (75m) | Applications, cold emails, LinkedIn DMs, recruiter replies, marketplace work, admin |
| 15:20 | exercise (30m) | Non-negotiable |
| 15:50 | **5 · Evening retrieval** (45m) | **Test** this morning's block A closed-book, then check and correct |
| 16:35 | **6 · Speaking rep** (20m) | Record ONE artifact. Watch it back once |
| — | Stop | Protect 7–8h sleep |

**Per DSA problem — the 25-minute protocol:**
1. 2 min: restate + brute force **out loud**
2. 23 min: attempt. **No AI, no autocomplete, timer visible**
3. On failure: editorial + the matching BCtCI pattern chapter
4. **Close everything. Blank file. Re-implement until it passes.** ← *this is the entire learning event*
5. 60-second card: pattern name / the trigger phrase in the problem statement / the one line that is the trick

**Per design rep — 45/20/40/30:** 45 min recorded in Excalidraw, hard timer, no lookups → 20 min watch back at 1.5× and self-score → 40 min re-do with the reference open → 30 min reading only what your two worst sub-scores demand. **Whiteboard cold, then read the reference. Never the other way round.**

**After every real interview, within 2 hours:** write down every question asked, **verbatim**, in `pipeline.md`.

---

# WEEK 1 — Stop losing winnable loops

*You are interviewing this week. The metric-defence doc protects live loops; everything else is groundwork.*

## Day 1 · Mon

- [ ] **A — Metric-defence doc, claims 1–3.** Open `metric-defence.md`. Fill: **−40% LLM latency**, **−30% inference cost**, **+35% answer relevance**. For each: metric definition · instrument · baseline + date · n · who labelled · biggest confounder · measurement class (A/B/C) · the 25-second spoken answer · **DEFEND or DELETE**
  - Model answers + full follow-up chains: **`answers/01-latency-and-cost.md`** and **`answers/02-relevance-and-agent-success.md`**. Fill your own facts first, *then* read the model — reading it first produces the illusion of competence
  - ⚠️ Fix on the resume today: **MCP was announced 25 Nov 2024**; your Turing engagement ended Jan 2025. Split the claim so it doesn't read as 14 months of MCP work
- [ ] **B — DSA.** Grokking Algorithms ch 1–4 (skim, no exercises, ~2h across today/tomorrow) + NeetCode: `Contains Duplicate`, `Valid Anagram`, `Two Sum`
- [ ] **C — Build.** Resume restructure: retitle to **Senior AI Engineer (Agentic Systems & Evaluation)**; add a **"Selected AI/Agent Work"** block above the chronology; relabel Turing as **`AI Consultant (part-time contract engagement), ~N hrs/week`**
- [ ] **4 — Outreach.** ⚡ **Runway priority:** apply to **Mercor**, reactivate your **Turing** account at a higher band, apply to **Scale / Surge / Outlier eval-and-environments** roles specifically. Also: Handshake AI, Invisible, Snorkel
- [ ] **Also:** order the 7 books (see `resources.md`). Enrol in the 4 sprint Coursera courses
- [ ] **6 — Speaking rep.** Record: 3-minute pitch of the AML/CTF compliance RAG. **No tool name in the first 30 seconds**

## Day 2 · Tue

- [ ] **A — Metric-defence doc, claims 4–7.** **−45% review turnaround**, **+20% agent task success**, **−60% manual tagging effort**, **~85% accuracy on 50k records**
- [ ] **B — DSA.** Grokking ch 5–8 skim + `Group Anagrams`, `Top K Frequent Elements`, `Encode and Decode Strings`
- [ ] **C — Build.** Finish resume. Record and host a **90-second demo video of the Indic voice agent** — link it from the resume header, LinkedIn Featured, and every outreach message
- [ ] **4 — Outreach.** 10 applications to companies ranked 15–40 on your list. Build the 60-company target list in `pipeline.md`
- [ ] **6 — Speaking rep.** Record: the 25-second answer for **−40% latency**, under pushback

> **The delete rule.** If you can't state *metric definition + baseline + n + who labelled + biggest confounder* in 30 seconds, **delete the number and keep the qualitative claim.** A deleted number costs nothing; a collapsed one discredits the whole page. Specifically: replace bare "~85% accuracy" with precision/recall or *"85% vs a 71% majority-class baseline."* And **stop leading with "10k docs" / "1M events/day" as scale** — 1M/day is ~12 events/sec, a laptop-scale number that invites *"what breaks at 10M?"*. Lead with the eval layer and the guardrails.

## Day 3 · Wed

- [ ] **A — Behavioral foundations.** interviewing.io: *Amazon Leadership Principles Interview Guide* + *"Stop memorizing STAR… start selecting better stories."* **30 minutes on frameworks total — STAR + the "L" from CARL. Then stop shopping.** Brainstorm **20 raw stories**
- [ ] **B — DSA.** `Product of Array Except Self`, `Valid Sudoku`, `Longest Consecutive Sequence`
- [ ] **C — Build.** LinkedIn rewrite: headline mirrors the resume title; Featured = AML repo + demo video; open-to-work set to recruiters only
- [ ] **4 — Outreach.** 8 referral asks (JNTU alumni, ex-Centific/Pactera colleagues, Turing client leads, KNS network). **Line up 3 referees now** — Anthropic runs references as a formal 1–2 week stage
- [ ] **Also:** BCtCI negotiation section (~1h). Haseeb Qureshi's negotiation post — **read for method, ignore every number (it's 2016)**
- [ ] **6 — Speaking rep.** Record: 60-second version of the voice-agent pitch

## Day 4 · Thu

- [ ] **A — Story bank v1.** Filter 20 → **10** in `story-bank.md`. Each needs 3–5 evidence points (**quantitative + qualitative + organizational**), a title teasing challenge *and* impact, a 60-sec and a 4-min version
- [ ] **B — DSA.** Two Pointers: `Valid Palindrome`, `Two Sum II`, `3Sum`, `Container With Most Water`
- [ ] **C — Build.** Hello Interview *System Design in a Hurry* (free tier): Delivery Framework · Core Concepts · Numbers to Know · Patterns. **Write the six steps with their minute counts by hand and keep the paper visible for 28 days**
- [ ] **4 — Outreach.** 10 hiring-manager cold DMs with the demo link
- [ ] **6 — Speaking rep.** Record: story #1 at 4-minute depth, no notes

## Day 5 · Fri — 🎤 mock day

- [ ] **A — Story → LP matrix.** Map all 10 stories to Amazon's 16 LPs and the 5 buckets (technical problem-solving / learning-failure / business delivery / interpersonal conflict / ambiguity). **Every column needs ≥2 entries; no story is primary for more than 3.** Then write **the two missing stories**: (a) a failure with a **named cost**, (b) a disagreement you **lost and then committed to**
- [ ] **B — DSA.** Sliding Window: `Best Time to Buy and Sell Stock`, `Longest Substring Without Repeating Characters`, `Longest Repeating Character Replacement`, `Permutation in String`, `Minimum Window Substring`
- [ ] **C — Build.** Back-pocket fact sheets for stories 1–5: numbers, dates, team size, who disagreed, the alternative, what it cost, what you'd change. **Must survive 4 follow-ups**
- [ ] **🎤 Mock (replaces block 4).** Exponent Practice ×2, behavioral, free peer
- [ ] **Debrief (replaces block 5).** **One page: three things to fix, ranked. The top item becomes tomorrow's block A.** A mock that doesn't change tomorrow's schedule was entertainment

## Day 6 · Sat — artifact + application day

- [ ] **A — Karpathy, "Deep Dive into LLMs like ChatGPT"** (3h31 @1.5×) with written notes. Target narrative: pretraining → tokenization → base → SFT → reward model → RLHF → hallucination → tool use → *"models need tokens to think"*
- [ ] **B — DSA.** Stack: `Valid Parentheses`, `Min Stack`, `Evaluate Reverse Polish Notation`, `Generate Parentheses`
- [ ] **C — 3 recorded design reps** (45/20/40/30 each, spread across the day):
  - [ ] Bitly / URL shortener — *pure framework rehearsal, deliberately trivial*
  - [ ] Distributed rate limiter
  - [ ] ⭐ **RAG over 10k enterprise docs with per-tenant isolation** — your day job; the first GenAI rep must be one you cannot fail
- [ ] **Expect 40–50/100 self-scored. That is the correct week-1 score.**
- [ ] **Outreach batch** (3h in one sitting): finish the week's application/DM/referral targets

## Day 7 · Sun — **OFF**

- [ ] Fully off. Not "light review." **Log it or it erodes and Monday's block A is worthless.**

### ✅ Week 1 exit test — recorded, out loud

- [ ] Defend −40% latency / −30% cost for **5 minutes under pushback**, naming the mechanism split
- [ ] Recite the six design steps with minute counts **from memory**
- [ ] Deliver **two behavioral stories at 4-minute depth without notes**

**Week 1 totals:** 22 DSA problems · 10-page metric doc · new resume + demo video · LinkedIn · 10 stories + LP matrix · 3 design recordings

---

# WEEK 2 — Close the training-loop hole

*Also running this week inside blocks 4/5: **Coursera "Generative AI with LLMs" Weeks 2 & 3** @1.5× (~6h) — instruction tuning, PEFT/LoRA, soft prompts, RLHF, reward modelling, scaling laws.*

## Day 8 · Mon

- [ ] **A — Karpathy Zero-to-Hero L1 (micrograd)**, typed line by line
- [ ] **B — DSA.** Binary Search: `Binary Search`, `Search a 2D Matrix`, `Koko Eating Bananas` + BCtCI binary-search chapter
- [ ] **C — Build.** Huyen *AI Engineering* **Ch 9 (Inference Optimization)** — KV cache, GQA/MQA, quantization, speculative decoding, continuous batching, prompt caching, semantic caching, model routing/cascades
- [ ] **6 — Speaking rep.** Record: "walk me through what happens in one training step"

## Day 9 · Tue

- [ ] **A — micrograd re-implemented from a blank file.** Then write a 30-line MLP training loop from memory, **twice**, no reference
- [ ] **B — DSA.** `Find Minimum in Rotated Sorted Array`, `Search in Rotated Sorted Array`, `Time Based Key-Value Store`
- [ ] **C — Build.** vLLM docs (Optimization & Tuning) + PagedAttention paper §1 and §4 → write the **one-page "how I got −40% latency / −30% cost" narrative**, naming each mechanism *and the tradeoff it cost*
- [ ] **6 — Speaking rep.** Record: "what does `optimizer.zero_grad()` actually do"

> This one-page narrative outranks *Attention Is All You Need* for you, because it is the question you are **guaranteed** to get.

## Day 10 · Wed

- [ ] **A — Raschka Appendix A + Ch 2** (text data, BPE, dataloaders), typed
- [ ] **B — DSA.** Linked List: `Reverse Linked List`, `Merge Two Sorted Lists`, `Reorder List`, `Remove Nth Node From End of List`
- [ ] **C — Build.** Anthropic engineering, **the 5 posts in date order**: *Contextual Retrieval* (Sep 2024) → *Building Effective Agents* (Dec 2024) → *Effective Context Engineering* (Sep 2025) → *Code Execution with MCP* (Nov 2025) → *Demystifying Evals for AI Agents* (Jan 2026). **Map every Turing engagement to one of the five named patterns** (prompt chaining / routing / parallelisation / orchestrator-workers / evaluator-optimiser)
- [ ] **6 — Speaking rep.** Record: BPE explained in 90 seconds, including **Indic token inflation (3–8× per char)** — your Telugu agent is a differentiated answer here

## Day 11 · Thu

- [ ] **A — Raschka Ch 3**, typed: simplified attention → scaled dot-product → causal masking → dropout → **multi-head**
- [ ] **B — DSA.** `Copy List with Random Pointer`, `Add Two Numbers`, `Linked List Cycle`, `Find the Duplicate Number`
- [ ] **C — Build.** Alex Xu Vol 1 — 4h targeted skim (start) + **GenAI System Design Interview Ch 1**
- [ ] **6 — Speaking rep.** Record: "why the √d_k?"

## Day 12 · Fri — 🎤 mock day

- [ ] **A — Whiteboard causal multi-head attention from memory, recorded.** Then Hands-On LLMs ch 2–3, **redraw 3 diagrams from memory on paper**
- [ ] **B — DSA.** Trees pt.1: `Invert Binary Tree`, `Maximum Depth`, `Diameter of Binary Tree`, `Balanced Binary Tree`
- [ ] **C — Build.** Back-pocket fact sheets for stories 6–10
- [ ] **🎤 Mock.** Exponent Practice coding (free peer) + **BCtCI's free AI interviewer** ×1
- [ ] **Debrief.** One page, three ranked fixes → top item becomes tomorrow's block A

## Day 13 · Sat — artifact day

- [ ] **A — GenAI System Design Interview Ch 4 (ChatGPT) + Ch 6 (RAG).** Write out the 7-step framework. **Do not read Ch 7–11 — they're diffusion/image/video**
- [ ] **B — DSA.** `Same Tree`, `Subtree of Another Tree`, `Lowest Common Ancestor of a BST`
- [ ] **C — README #1: AML/CTF RAG**, full 8-section standard:
  - [ ] One-line what + a GIF
  - [ ] The problem
  - [ ] **Whiteboard-reproducible architecture diagram**
  - [ ] **Evals table with honest limitations**
  - [ ] Latency & cost table
  - [ ] Run-in-5-minutes `docker-compose`
  - [ ] Limitations & next
  - [ ] **Design decisions and rejected alternatives** ← *this is what an interviewer reads before the onsite; it pre-loads them with the questions you want*
- [ ] **4 recorded design reps:**
  - [ ] Twitter feed — fan-out on write vs read
  - [ ] Real-time chat / WhatsApp — prerequisite for streaming LLM UIs
  - [ ] ⭐ LLM customer-support agent with tool calling and human escalation
  - [ ] ⭐ **Eval & observability platform for LLM applications** — your Turing work, verbatim
- [ ] **Target 55–65/100.** Outreach batch: 20 applications, 8 referrals, 10 HM DMs

## Day 14 · Sun — **OFF**

### ✅ Week 2 exit test

- [ ] Whiteboard **causal multi-head attention from memory**
- [ ] Explain **why the √d_k**
- [ ] Explain **why LLMs are decoder-only**
- [ ] Survive **5 minutes of pushback on the −40% / −30% numbers**

**Week 2 totals:** 21 problems (cum. ~43) · training-loop gap closed · MHA on video · mechanism narrative · README #1 · 4 design recordings

---

# WEEK 3 — ⭐ THE EVAL WEEK. The week that wins the offer.

*Highest-ROI block in the plan. Costs ₹0. Converts four unbacked resume claims into a screen-shareable artifact.*
*Interleaving starts now: **every block B is a mixed set** — problems drawn at random across everything learned. Don't tell yourself the pattern.*

## Day 15 · Mon

- [ ] **A — Hamel Husain, "LLM Evals: Everything You Need to Know"** (hamel.dev/blog/posts/evals-faq)
- [ ] **B — DSA.** Trees pt.2: `Binary Tree Level Order Traversal`, `Binary Tree Right Side View`, `Count Good Nodes`, `Validate Binary Search Tree`
- [ ] **C — ⭐ Eval harness, step 1.** Capture **100+ real traces** from the AML hybrid dense+BM25 → RRF → cross-encoder pipeline
- [ ] **6 — Speaking rep.** Record: "how would you evaluate a RAG system you just inherited?"

## Day 16 · Tue

- [ ] **A — Eugene Yan ×3:** LLM-as-Judge survey · Task-Specific Evals · Product Evals in Three Steps
- [ ] **B — DSA.** `Kth Smallest Element in a BST`, `Construct Binary Tree from Preorder and Inorder`, `Binary Tree Maximum Path Sum`
- [ ] **C — ⭐ Step 2.** **Open-code 60–100 traces by hand.** No shortcuts — this is the part everyone skips and it's the part that shows
- [ ] **6 — Speaking rep.** Record: position bias, verbosity bias and self-preference bias in LLM judges, and the order-swap fix

## Day 17 · Wed

- [ ] **A — Anthropic *Demystifying Evals for AI Agents*** + **Huyen Ch 3–4 (Evaluation)**
- [ ] **B — DSA.** Heap/PQ: `Kth Largest Element in a Stream`, `Last Stone Weight`, `K Closest Points to Origin`, `Kth Largest Element in an Array`, `Task Scheduler`
- [ ] **C — ⭐ Step 2 cont.** **Axial-code into a 5–8 mode failure taxonomy. Note saturation** (~100 traces; stop after 20 with no new category)
- [ ] **6 — Speaking rep.** Record: **pass@k vs pass^k**, and why the difference matters for agents

## Day 18 · Thu

- [ ] **A — Huyen Ch 6 (RAG & Agents)** + **Coursera ML Specialization C2 Week 3, "Advice for Applying ML"** ← *the single highest-ROI hour in the whole Coursera catalogue for you; it's what lets you defend the 85% line*
- [ ] **B — DSA.** Backtracking: `Subsets`, `Combination Sum`, `Permutations`, `Subsets II`, `Word Search`
- [ ] **C — ⭐ Step 3.** **Retrieval metrics separated from generation metrics** — recall@k, MRR, nDCG vs groundedness, citation-correctness. *Knowing these are two different eval problems is itself a differentiator*
- [ ] **6 — Speaking rep.** Record: MRR vs MAP vs nDCG vs recall@k — which for the retriever stage vs the reranker stage

## Day 19 · Fri — 🎤 mock day

- [ ] **A — Coursera "Machine Learning in Production" (MLOps C1) Week 1** — concept drift, data-centric AI, deployment monitoring
- [ ] **B — DSA.** Design: `LRU Cache`, `Implement Trie`, `Find Median from Data Stream` ← *disproportionately common in India product loops*
- [ ] **C — ⭐ Step 4.** One **binary** LLM judge for the top failure mode, aligned against your own labels, **reporting TPR/TNR on a held-out split**
- [ ] **🎤 Mock.** Exponent peer, system design + BCtCI AI interviewer
- [ ] **Debrief.** One page, three ranked fixes

## Day 20 · Sat — artifact day

- [ ] **⭐ Steps 5–6.** 20–50 case **regression suite running in CI** (exit code fails the build) + a one-page results doc with a **before/after delta**
- [ ] **3 recorded design reps:**
  - [ ] YouTube — upload → transcode → CDN
  - [ ] ⭐ **Design ChatGPT / LLM inference serving at scale** — queueing, GPU worker scheduling, **TTFT**, streaming, fairness across free/paid tiers, context management
  - [ ] ⭐ **Real-time Indic voice agent, sub-800ms** — your own project: STT→LLM→TTS pipelining, streaming partials, barge-in (<150ms flush), WebRTC, per-hop latency budget
- [ ] **Target 65–72 on GenAI prompts, 60–68 on classic**
- [ ] **Outreach batch:** 25 applications — **now including your top 15 companies** — 8 referrals, 10 HM DMs

## Day 21 · Sun — **OFF**

### ✅ Week 3 exit test

- [ ] A **10-minute unscripted recorded walkthrough** of the eval harness: failure taxonomy · judge alignment numbers (TPR/TNR) · retrieval-vs-generation metric split · what you'd do next

> **If you can do this, you out-depth most interviewers on this topic.** It converts *"eval dashboards," "guardrails," "benchmark definition," "eval prompts and rubrics"* from claims into an artifact. It retroactively defends −40%/−30% by proving quality didn't regress when cost was cut. And it's the answer to *"tell me about a time you measured AI quality"* — which you will be asked and almost no candidate can answer.

**Week 3 totals:** 20 problems (cum. ~63) · **public eval-harness repo** · 3 design recordings

---

# WEEK 4 — MCP at spec depth, papers, format rehearsal

## Day 22 · Mon

- [ ] **A — MCP spec, revision 2026-07-28** (modelcontextprotocol.io): tools vs resources vs prompts, **sampling**, **elicitation**, stdio vs **Streamable HTTP**, auth. ⚠️ Reject any MCP tutorial predating Streamable HTTP / elicitation
- [ ] **B — DSA.** Graphs: `Number of Islands`, `Max Area of Island`, `Clone Graph`, `Rotting Oranges`
- [ ] **C — Build a 3-tool FastMCP server** over your AML corpus + one resource + one prompt
- [ ] **6 — Speaking rep.** Record: the MCP primitive control model — tools are *model*-controlled, resources are *app*-controlled, prompts are *user*-controlled

> **Your resume claims MCP. This is mandatory, not optional.** A hostile expert will ask about the control model, transports, and tool-schema design in the first three minutes.

## Day 23 · Tue

- [ ] **A — Anthropic *Code Execution with MCP*** + the attack classes: tool poisoning, rug pull, tool shadowing, confused deputy
- [ ] **B — DSA.** `Pacific Atlantic Water Flow`, `Surrounded Regions`, `Course Schedule`, `Course Schedule II`
- [ ] **C — Finish the MCP server, wire it into Claude Code.** Then **draw the client↔server lifecycle from memory**
- [ ] **6 — Speaking rep.** Record: how you'd debug an MCP server whose stdout is corrupting the protocol stream

## Day 24 · Wed

- [ ] **A — Papers 1–4** (method + figures only, ~45 min each, one paragraph of notes each):
  - [ ] Attention Is All You Need — **plus the seven deltas to a modern Llama block**: decoder-only, pre-norm, RMSNorm, RoPE not sinusoidal, SwiGLU, GQA, no encoder
  - [ ] RAG (Lewis et al. 2020)
  - [ ] ReAct
  - [ ] **Lost in the Middle** — punches far above its fame; it justifies your reranking
- [ ] **B — DSA.** 1-D DP: `Climbing Stairs`, `Min Cost Climbing Stairs`, `House Robber`
- [ ] **C — README #2** (voice agent) to the 8-section standard
- [ ] **6 — Speaking rep.** Record: "what's different in a modern Llama block vs the 2017 paper?"

## Day 25 · Thu

- [ ] **A — Papers 5–8:**
  - [ ] InstructGPT
  - [ ] **LoRA** ← *highest risk per unit of likelihood — you've never fine-tuned.* ΔW = BA, B zero-init, α/r, target modules, merge vs multi-LoRA serving
  - [ ] **DPO** — *"why DPO instead of PPO"* is a standard 2026 question
  - [ ] Chain-of-Thought + Self-Consistency
- [ ] **B — DSA.** `Coin Change`, `Word Break`, `Longest Increasing Subsequence`
- [ ] **C — README #3** + draft the blog post: **"Hybrid retrieval that actually works: BM25 + dense + RRF + cross-encoder rerank, and how I evaluated it."** ⚠️ **Do not publish generic "What is RAG?" content — that is negative signal in 2026**
- [ ] **Also:** write out the RRF formula `Σ 1/(60 + rank)` by hand and be able to say **why rank-fusion beats score-fusion.** You use RRF in your own project

## Day 26 · Fri — 🎤 format rehearsal

- [ ] **STOP adding new problems.**
- [ ] **A + B — 3 full simulated screens:** 45 min, 2 problems each, **webcam on, talking continuously, no IDE autocomplete.** Use BCtCI's free AI interviewer
- [ ] **Pass = one clean medium + an articulate partial on the second**
- [ ] **C — Publish the blog post** to your own domain, cross-post to LinkedIn
- [ ] **Debrief:** pass/fail log per screen, three ranked fixes

## Day 27 · Sat — 🎓 graduation

- [ ] **3 more simulated screens** (same format)
- [ ] **🎓 The graduation exam:** re-do **Day 6's Bitly** and **Day 6's RAG-with-tenant-isolation** designs — **cold, recorded — then diff against the week-1 videos**
- [ ] **If the delta isn't obvious on camera, extend by a week before moving on.**
- [ ] **3 recorded design reps:**
  - [ ] Google Docs — OT / CRDT
  - [ ] ⭐ Agentic coding assistant — repo indexing, MCP tools, sandboxed execution, PR + CI/CD hooks
  - [ ] ⭐ Multi-tenant AML/CTF search generalised to **1000 tenants**
- [ ] **Target 72–80 on GenAI, 65–72 on classic**

## Day 28 · Sun — **OFF**

### ✅ Week 4 exit test

- [ ] A 45-minute mock GenAI deep dive — ***"Design a RAG system for 10k regulatory documents with tenant isolation, then tell me how you'd know it works"*** — answered **entirely from work you did in weeks 1–3**

**Week 4 totals:** ~14 new problems (cum. ~77) · working MCP server · 8 papers at mechanism depth · all 3 READMEs · 1 blog post published · 6 simulated screens

---

# After Day 28

Switch to the continuation phase in the plan (`~/.claude/plans/from-the-resume-that-refactored-hanrahan.md`, Part 6):

- **DSA moves to 3h/day.** Finish NeetCode 150, then Sean Prashad's 179 filtered to your pipeline. **Gate: week 8 = 2 mediums in 45 min on ≥5 of 10 recorded sessions (~180 problems). Week 12 = ≥11 of 15 (~300 problems) → Tier-3 companies unlock.**
- **Raschka Ch 5–7 + Appendix E** — your first real pretraining loop. *"I can fine-tune"* becomes a truthful claim.
- **Coursera PyTorch Professional Certificate C1 + C2.**
- **Géron 2025 (the PyTorch edition)** — the direct path to the deferred MLE target.
- **DDIA 2e** — *now*, not in the sprint.
- **Week 5 is a deload week if you're running on empty:** 4h/day, review + mocks + applications only, zero new material. The gap **improves** retention of weeks 1–4.

**Burnout tripwire:** when **hard-block hours stay flat but problems-solved-cold falls three days running**, deload immediately. Quality collapse, not quitting, is the failure mode.
