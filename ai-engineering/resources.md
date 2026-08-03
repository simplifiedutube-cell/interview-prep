# AI Engineering Resources — The "Builder's" Canon

Filtered specifically for AI Engineering FTE loops. The focus is on GenAI system design, rigorous evaluation, and practical training/serving mechanics. 

---

## 1 · Buy today — The AI Engineering Core

| # | Title | Author / Publisher | ~Cost | Focus Area |
|---|---|---|---|---|
| 1 | **AI Engineering** | Chip Huyen — O'Reilly, 2025 | ₹1,150 | The definitive text on modern AI infra. Focus on **Ch 9 (Inference Optimization)**, **Ch 3-4 (Evals)**, and **Ch 6 (RAG & Agents)**. |
| 2 | **Generative AI System Design Interview** | Aminian, Sheng, Xu — ByteByteGo, 2024 | ₹1,000 | The only book-form GenAI system design framework. Focus on **Ch 1-4, 6 (RAG)**. |
| 3 | **Build a Large Language Model (From Scratch)** | Raschka — Manning, 2024 | $29.99 | Antidote to "I just call APIs". Code a PyTorch training loop. **App A, Ch 2, Ch 3 (TYPED)**. |
| 4 | **Hands-On Large Language Models** | Alammar & Grootendorst — 2024 | ₹1,300 | Whiteboard diagrams. **Ch 2, 3, 8**. Redraw these diagrams from memory. |
| 5 | **Grokking Algorithms, 2nd ed.** | Bhargava — Manning, 2024 | $29.99 | Essential DSA refresher to speed up coding rounds without grinding 300+ LeetCode hard problems. |

---

## 2 · Free Canon — Bookmark These Today

### System Design & Inference
*   **vLLM Docs (Optimization & Tuning):** Not optional. Understand PagedAttention, KV Cache, and continuous batching. This is how you defend latency/cost numbers.
*   **evidentlyai.com/ml-system-design:** 800 case studies. "DoorDash does X, we'd do Y" is your cheat code.

### Evaluation & MLOps
*   **hamel.dev/blog/posts/evals-faq:** "LLM Evals: Everything You Need to Know." The most vital resource for defending your evaluation metrics.
*   **Eugene Yan's Writing (eugeneyan.com):** LLM-as-Judge survey, Task-Specific Evals.

### Agents & Model Context Protocol (MCP)
*   **Anthropic Engineering Blog (anthropic.com/engineering):** Read the 5-post set in order (Contextual Retrieval, Effective Agents, Context Engineering, Code Execution with MCP, Evals for AI Agents).
*   **Model Context Protocol Spec (modelcontextprotocol.io):** Read the 2026-07-28 revision. Understand tools vs. resources vs. prompts, and the control model.

### Papers (Method + Figures only)
1.  **Attention Is All You Need** (Plus the 7 deltas to modern Llama: decoder-only, pre-norm, RMSNorm, RoPE, SwiGLU, GQA, no encoder).
2.  **RAG (Lewis et al. 2020)**
3.  **PagedAttention (Kwon et al., 2023)** — Sections 1 & 4.
4.  **Lost in the Middle** — Justifies your reranking strategies.
5.  **LoRA** — $\Delta W = BA$. Know target modules and serving trade-offs.

---

## 3 · Coursera (Targeted Video Only)

*   **Generative AI with LLMs (DeepLearning.AI):** Weeks 2 & 3 only @1.5x (Instruction tuning, PEFT/LoRA, RLHF).
*   **Machine Learning Specialization (Ng):** C2 Week 3, "Advice for Applying ML" (Bias-variance, error analysis).
*   **Machine Learning in Production (MLOps C1):** Week 1 only (Concept drift, monitoring).
