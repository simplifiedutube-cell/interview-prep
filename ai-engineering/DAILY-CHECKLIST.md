# 28-Day AI Engineering Interview Sprint — Daily Checklist

**Target:** 8h/day, Mon–Sat, Sunday fully off.

---

## The standing day (every Mon–Sat)

| Time | Block | What |
|---|---|---|
| 08:00 | **0 · AI Theory Warm-up** (30m) | Recall yesterday's LLM mechanics / architectures closed-book. |
| 08:30 | **1 · Hard block A — AI Theory/Implementation** (90m) | ↓ see the day. E.g., paper reading or PyTorch loops. |
| 10:00 | break (20m) | Walk outside. No phone |
| 10:20 | **2 · Hard block B — DSA & Code** (60m) | ↓ Reduced DSA time to focus on AI implementation. 2 problems max. |
| 11:20 | break (30m) | |
| 11:50 | **3 · Hard block C — ML System Design & Evals** (90m) | ↓ see the day. Focus on RAG, Agents, and Evals. |
| 13:20 | lunch (45m) | |
| 14:05 | **4 · Low-energy block** (75m) | Applications, recruiters, admin. Focus on AI Engineer roles. |
| 15:20 | exercise (30m) | Non-negotiable |
| 15:50 | **5 · Evening retrieval** (45m) | **Test** this morning's block A closed-book, then check and correct. |
| 16:35 | **6 · Speaking rep** (20m) | Record ONE artifact. (e.g., Explain KV Cache). Watch it back once. |

---

# WEEK 1 — Foundation: Inference, Cost, & Fundamentals

## Day 1 · Mon
- [ ] **A — Tokenization & Context:** Read Anthropic's *Contextual Retrieval*.
- [ ] **B — DSA:** `Contains Duplicate`, `Valid Anagram`.
- [ ] **C — ML Sys Design:** System Design in a Hurry (Hello Interview). Map the 6 steps to an AI problem (e.g., URL shortener -> LLM serving).
- [ ] **6 — Speaking rep:** Pitch the AML/CTF RAG project in 3 mins.

## Day 2 · Tue
- [ ] **A — Attention Mechanism:** Read *Attention Is All You Need* + 7 deltas to modern Llama. 
- [ ] **B — DSA:** `Two Sum`, `Group Anagrams`.
- [ ] **C — ML Sys Design:** Build a 1-page metric defense doc for your resume (Latency, Cost reductions).
- [ ] **6 — Speaking rep:** Explain the 7 differences in modern Llama blocks vs 2017 Transformer.

## Day 3 · Wed
- [ ] **A — Behavioral:** Brainstorm 10 stories mapped to Amazon LPs.
- [ ] **B — DSA:** `Top K Frequent Elements`, `Valid Sudoku`.
- [ ] **C — Eval Harness:** Read Hamel Husain's LLM Evals FAQ.
- [ ] **6 — Speaking rep:** Defend "-40% Latency" for 60 seconds.

## Day 4 · Thu
- [ ] **A — Model Serving:** vLLM Docs (PagedAttention, KV Caching).
- [ ] **B — DSA:** `Product of Array Except Self`, `Valid Palindrome`.
- [ ] **C — Implementation:** Write out the formula for RRF (Reciprocal Rank Fusion).
- [ ] **6 — Speaking rep:** Explain KV Cache and how it impacts TTFT.

## Day 5 · Fri — 🎤 Mock Day
- [ ] **A — PyTorch:** Karpathy Zero-to-Hero L1 (micrograd), typed line by line.
- [ ] **B — DSA:** `Two Sum II`, `3Sum`.
- [ ] **C — Mock prep:** Fact sheets for top 5 behavioral stories.
- [ ] **🎤 Mock:** System Design (LLM Inference focus) or AI peer mock.

## Day 6 · Sat
- [ ] **A — Theory Review:** Karpathy "Deep Dive into LLMs" video.
- [ ] **B — DSA:** `Container With Most Water`, `Best Time to Buy and Sell Stock`.
- [ ] **C — 3 Recorded ML Design Reps:** 
  - [ ] RAG over 10k enterprise docs (Tenant isolation).
  - [ ] LLM Support Agent with Tool Calling.
  - [ ] Eval/Observability platform for LLM apps.

## Day 7 · Sun — OFF

---

# WEEK 2 — RAG, Retrieval, and Evals

## Day 8 · Mon
- [ ] **A — RAG Deep Dive:** Read *RAG (Lewis et al. 2020)* and *Lost in the Middle*.
- [ ] **B — DSA:** `Longest Substring Without Repeating Characters`, `Valid Parentheses`.
- [ ] **C — Build:** Build a local test harness for RRF (dense + sparse retrieval).
- [ ] **6 — Speaking rep:** Why rank-fusion beats score-fusion.

## Day 9 · Tue
- [ ] **A — Evaluation Metrics:** Eugene Yan LLM-as-Judge survey.
- [ ] **B — DSA:** `Min Stack`, `Evaluate Reverse Polish Notation`.
- [ ] **C — Evals Implementation:** Open-code 50 traces by hand to build a failure taxonomy.
- [ ] **6 — Speaking rep:** Pass@k vs pass^k and why it matters.

## Day 10 · Wed
- [ ] **A — PyTorch:** Raschka Ch 2 (Text Data, BPE). 
- [ ] **B — DSA:** `Generate Parentheses`, `Binary Search`.
- [ ] **C — Evals Implementation:** Separate retrieval metrics (recall@k, nDCG) from generation metrics (groundedness).
- [ ] **6 — Speaking rep:** MRR vs MAP vs nDCG.

## Day 11 · Thu
- [ ] **A — PyTorch:** Raschka Ch 3 (Simplified attention -> multi-head).
- [ ] **B — DSA:** `Search a 2D Matrix`, `Koko Eating Bananas`.
- [ ] **C — ML Sys Design:** ByteByteGo GenAI Ch 6 (RAG).
- [ ] **6 — Speaking rep:** Why the √d_k in scaled dot-product attention?

## Day 12 · Fri — 🎤 Mock Day
- [ ] **A — Theory:** Whiteboard causal multi-head attention from memory.
- [ ] **B — DSA:** `Find Minimum in Rotated Sorted Array`, `Search in Rotated Sorted Array`.
- [ ] **C — Build:** Run an LLM judge reporting TPR/TNR against your human labels.
- [ ] **🎤 Mock:** ML System Design mock.

## Day 13 · Sat
- [ ] **A — Coursera:** ML Spec C2 Week 3 (Advice for Applying ML).
- [ ] **B — DSA:** `Reverse Linked List`, `Merge Two Sorted Lists`.
- [ ] **C — 3 Recorded ML Design Reps:**
  - [ ] YouTube transcode pipeline (classic).
  - [ ] ChatGPT inference serving at scale.
  - [ ] Real-time Indic voice agent (latency budget).

## Day 14 · Sun — OFF

---

# WEEK 3 — Agents & MCP (Model Context Protocol)

## Day 15 · Mon
- [ ] **A — Agent Architecture:** ReAct Paper + Anthropic's *Building Effective Agents*.
- [ ] **B — DSA:** `Reorder List`, `Remove Nth Node From End of List`.
- [ ] **C — MCP Spec:** Read MCP spec (rev 2026-07-28). Tools vs Resources vs Prompts.
- [ ] **6 — Speaking rep:** The MCP primitive control model.

## Day 16 · Tue
- [ ] **A — MCP Deep Dive:** Anthropic *Code Execution with MCP* (Tool poisoning, rug pull).
- [ ] **B — DSA:** `Copy List with Random Pointer`, `Linked List Cycle`.
- [ ] **C — Build:** Build a 3-tool FastMCP server over your AML corpus.
- [ ] **6 — Speaking rep:** How to debug an MCP server whose stdout corrupts the stream.

## Day 17 · Wed
- [ ] **A — Fine-tuning & LoRA:** Read LoRA paper + Coursera LLMs Week 2.
- [ ] **B — DSA:** `Invert Binary Tree`, `Maximum Depth`.
- [ ] **C — Implementation:** Write out $\Delta W = BA$ and explain target modules.
- [ ] **6 — Speaking rep:** Why DPO instead of PPO?

## Day 18 · Thu
- [ ] **A — Alignment:** DPO paper + InstructGPT paper.
- [ ] **B — DSA:** `Diameter of Binary Tree`, `Balanced Binary Tree`.
- [ ] **C — ML Sys Design:** Chip Huyen AI Engineering Ch 9 (Inference).
- [ ] **6 — Speaking rep:** Merge vs multi-LoRA serving.

## Day 19 · Fri — 🎤 Mock Day
- [ ] **A — Agent Evals:** Anthropic *Demystifying Evals for AI Agents*.
- [ ] **B — DSA:** `Same Tree`, `Subtree of Another Tree`.
- [ ] **C — Build:** README generation for your MCP project (the 8-section standard).
- [ ] **🎤 Mock:** System Design (Agent / Orchestrator focus).

## Day 20 · Sat
- [ ] **A — MLOps:** Coursera MLOps C1 Week 1 (Concept drift).
- [ ] **B — DSA:** `Lowest Common Ancestor of a BST`, `Binary Tree Level Order Traversal`.
- [ ] **C — 3 Recorded ML Design Reps:**
  - [ ] Agentic coding assistant with sandboxed execution.
  - [ ] Multi-tenant AML search generalized to 1000 tenants.
  - [ ] Your custom MCP evaluation framework.

## Day 21 · Sun — OFF

---

# WEEK 4 — Refinement & Simulated Screens

## Day 22 - Day 27
- **Format Rehearsal:** 45-min simulated screens (2 problems each, webcam on, talking continuously).
- **Final Mock Deep Dive:** *"Design a RAG system for 10k regulatory documents with tenant isolation, then tell me how you'd know it works."*
- **DSA:** Wrap up Top 50 NeetCode if not finished. (Graphs, Heap/PQ).
- **Build:** Publish a blog post on hybrid retrieval vs RRF. No generic content.
