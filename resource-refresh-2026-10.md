# Resource refresh — 24 Oct 2026

Checked against YouTube and Reddit (via Agent Reach), X and Instagram (via Chrome), plus first-party pages. Nothing existing was edited; this is a to-do list for the folder.

## Verdict

**Still relevant.** What people are actually asked in AI Engineer loops in Jul–Oct 2026 lines up with this folder's core: RAG design and debugging, hybrid retrieval and reranking, evals and LLM-as-judge, cost and latency, agents, tool use, MCP, LoRA vs RAG vs prompting, and defending your own project's architecture.

**Two layers have drifted apart.** The Oct layer (`master-tracker.html`, `build/sources/*`, `ai-engineer-interviews/*`) is current: it covers the MCP 2026-07-28 stateless rewrite, the AI-assisted coding round, the Field Guide and Deep-ML. The Aug layer (`resources.md`, `DAILY-CHECKLIST.md`, `ai-engineering/*`, `pipeline.md`) has gone stale in the places listed below. Treat the tracker as the source of truth.

## Fix in the August files

| Where | What's stale | Change to |
|---|---|---|
| `resources.md` §1 "months 2–6" | *Evals for AI Engineers* (Shankar & Husain) is listed as a future, month-2 book | **It is out now (O'Reilly, Oct 2026).** Make it the core evals text. Ch 3 (open/axial coding), Ch 5 (judge validation), Ch 7 (RAG evals), Ch 8 (tool use and agents) and Ch 9 (CI and regression) map one-to-one onto your Week-3 eval harness. https://www.oreilly.com/library/view/evals-for-ai/9798341660717/ |
| `resources.md`, `DAILY-CHECKLIST.md`, sources.py | `tryexponent.com/practice` | Exponent has rebranded as **Aced**: https://www.aced.io/practice. I couldn't confirm whether peer mocks are still free, so check the pricing page before you rely on them |
| `DAILY-CHECKLIST.md` Day 22, `ai-engineering/resources.md` | MCP is framed as "tools/resources/prompts, sampling, elicitation, stdio vs Streamable HTTP" | The 2026-07-28 revision is the biggest since launch: a **stateless core** (no initialize handshake, no `Mcp-Session-Id`), **Tasks** (long-running work), **MCP Apps** (server-rendered UI), OAuth/OIDC-aligned auth and a deprecation policy. The tracker already has the stateless part. **Tasks and MCP Apps appear nowhere in the folder.** https://blog.modelcontextprotocol.io/tags/protocol/ |
| `DAILY-CHECKLIST.md` (the "no AI" rule everywhere) | Treats every coding round as AI-free | AI-assisted rounds are now reported at Meta, Microsoft, Amazon (OA) and Stripe (new "AI Programming Exercise", Jun 2026). Keep the no-AI drills, but add **one AI-assisted rep a week** (decompose → delegate → verify → integrate, narrated) |
| `resources.md` dated items | Maven cohort Sep 5–Oct 3, Arpit cohort, levels.fyi "Aug 2026" | All expired. Re-pull comp numbers before you negotiate |

## New resources worth adding

### Interview format (YouTube)
- **Hello Interview, "AI Coding Interview w/ Meta Staff Engineer"** (May 2026, 53 min, 138K views). The best single walkthrough of the AI-assisted round. https://www.youtube.com/watch?v=A1kX8fJx53c · written guide: https://www.hellointerview.com/blog/meta-ai-enabled-coding
- **Aced, "AI Coding Mock Interview (Senior FAANG Engineer)"** (Dec 2025). https://www.youtube.com/watch?v=ZE_YEn-okfk
- **Aced, Anthropic SWE process** + **Anthropic culture fit** (Nov–Dec 2025, short). Useful for the values round your pipeline flags as the main point of rejection. https://www.youtube.com/watch?v=6Dx2EOh53VQ · https://www.youtube.com/watch?v=fRVfozP5Ryc
- **Think in Models, "Inside a Real AI Engineer Interview"** (Apr 2026, 151K views) and **"What do they ask in an AI System Design Interview?"** (Jul 2026). Good for format calibration. https://www.youtube.com/watch?v=O-kuHMOdjX4 · https://www.youtube.com/watch?v=icd5KdbtwxM

### Depth (YouTube)
- **Pragmatic Engineer, "Context engineering with Dex Horthy"** (Jul 2026, 93 min). The talk behind the 12-Factor Agents repo your tracker already cites. https://www.youtube.com/watch?v=Usufn8IQJgw
- **Gaurav Sen, "AI Interview Questions #4 – Evals"** (Aug 2026, 11 min). Quick to rehearse against. https://www.youtube.com/watch?v=dzVogKf9jIM
- **freeCodeCamp, "MCP Security Fundamentals"** (22 Oct 2026, 2h10). Covers your Day-23 attack classes (tool poisoning, rug pull, shadowing, confused deputy). https://www.youtube.com/watch?v=gYXLRMycVMk
- **Mark Moyou, "Mastering LLM Inference Optimization"** (AI Engineer conf). Mechanism-level backing for your −40% latency / −30% cost story. https://www.youtube.com/watch?v=9tvJ_GYJA-o

### Real-question corpora (X)
- **Suraj Sharma, 25 practice problems** (13 Oct 2026, 2.7K bookmarks). Use it as a coverage checklist; most items are already in the tracker. Ones to confirm: semantic cache with hit-rate tracking, cheap/smart model routing, rolling back a bad prompt change, SSE disconnects, PII redaction. https://x.com/suraj_sharma14/status/2109864205251993874
- **Kris, AI Engineer interview transcript** (31 Jul 2026, 88K views). A typical India mid-level screen: project architecture → vector DB internals → chunking → doc parsing → transformer/self-attention → LoRA vs full fine-tuning → RAG eval → chain vs agent → hallucinations → precision@k. https://x.com/kris_aieng/status/2083237800326189270
- **Alexey Grigorev, AI Engineering Field Guide** (updated 29 Sep 2026: 6,964 JDs, Jan–Aug 2026, plus interview experiences). Already cited in 2 places; re-pull its `interview/` section. https://github.com/alexeygrigorev/ai-engineering-field-guide

### Reddit (titles and dates only; Reddit blocked reading the threads)
- r/leetcode: Microsoft SDE2 AI-assisted coding experience (Apr 2026); Amazon OA AI coding round (Feb, Apr 2026); Meta "Coding with AI" round (Oct 2025, Feb 2026)
- r/InterviewDB: Stripe's new AI Programming Exercise (Jun 2026)
- r/cscareerquestions: "Best book for OpenAI / Anthropic system design" (Sep 2026)
- r/LLMDevs: LLM inference systems interview experience (Feb 2026)

## Skip
- **Instagram AI-interview content.** It's almost all "comment REPO / AI and I'll DM you the PDF" engagement funnels. Its value is as a signal: the topic lists in those reels (structured outputs, memory systems, guardrails, streaming, MCP, latency) match your tracker.
- YouTube "100% guaranteed questions" and course-funnel videos (Intellipaat, BEPEC). They target freshers and sit below your level.
