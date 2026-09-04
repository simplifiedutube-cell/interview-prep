# Accenture — Custom Software Engineer, Skills Interview
## Question Bank · 5 Aug 2026, 15:00–16:00 IST

**Scope note.** Your existing `ai-engineer-interviews/real-questions.md` is calibrated for frontier-lab and AI-native product loops (Anthropic, Sierra, Harvey, Glean). This round is different and generally easier: an India ATCI lateral "Skills Interview" for **Custom Software Engineer**, one hour, one or two interviewers, submitted via BSL Placement. Expect breadth over depth — Python and backend fundamentals first, GenAI second, one light design question, and resume probing throughout. Do not walk in optimised for a research-lab bar; walk in able to explain ordinary engineering cleanly.

The Accenture-attested verbatim questions below are marked **[ACN-verbatim]** and come from your own corpus (Accenture, Dec 2025 first-person accounts). Those are the highest-value items on this page.

---

## Tier 1 — Prepare cold. Highest probability.

### Python & backend
1. Difference between a list and a tuple; when would you use each. *(Near-universal opener in Indian service-company technical rounds.)*
2. Mutable vs immutable types — and the classic trap: what happens when you use a mutable default argument.
3. Decorators — what they are, and one you've actually written.
4. Generators vs lists; when memory matters. *(Ties to your 1M-events/day pipeline.)*
5. `*args` / `**kwargs`.
6. What is the GIL, and what does it mean for concurrency in Python.
7. `asyncio` vs threading vs multiprocessing — and which you'd pick for an I/O-bound API. *(FastAPI makes this near-certain.)*
8. Shallow vs deep copy.
9. Exception handling: `try/except/else/finally`, and custom exceptions.
10. List comprehension vs `map`/`filter`.

### FastAPI / API design
11. Why FastAPI over Flask or Django — you claim 4 years on it, so have a real answer, not "it's fast."
12. How Pydantic validation works, and what you gain from it.
13. Dependency injection in FastAPI — what you use it for.
14. `async def` vs `def` endpoints — what actually happens differently.
15. REST design: status codes, versioning, pagination, idempotency.
16. Authentication — JWT/OAuth2 flow at a high level.
17. How would you handle a long-running request (background tasks, queues).

### SQL & data
18. `JOIN` types; write a query with a `GROUP BY` and a `HAVING`.
19. Indexes — what they cost, when they don't get used.
20. N+1 query problem and how you fix it in SQLAlchemy.
21. Transactions and ACID; what isolation level problems look like in practice.

### GenAI / RAG — your differentiator
22. **"Explain how RAG works, end to end."** **[ACN-verbatim]** — the single most-asked question in your entire corpus. Must be crisp.
23. **"What are you storing in the vector database?"** **[ACN-verbatim]** — they want: embeddings + the chunk text + metadata for filtering. Say all three.
24. **"What are embeddings?"** / **"How does chunking happen?"** **[ACN-verbatim]**
25. **"What is the key difference between a Generative AI system and an Agentic AI system?"** **[ACN-verbatim]**
26. **"Have you heard about MCP?"** **[ACN-verbatim]** — know the control model: tools are model-controlled, resources app-controlled, prompts user-controlled.
27. **"Which framework did you use — LangChain or CrewAI — and why?"** **[ACN-verbatim]** — answer honestly from what you actually used; do not claim CrewAI depth you don't have.
28. When do you fine-tune vs RAG vs prompt engineering.
29. Your RAG returns the right chunks but the answer still hallucinates — fix it.
30. How do you evaluate a RAG pipeline. *(Faithfulness, answer relevance, context precision/recall.)*

---

## Tier 2 — Likely. Have the shape ready.

31. Temperature, top-k, top-p.
32. What is a context window; what happens when you exceed it.
33. Why do hallucinations happen.
34. Hybrid search — BM25 + dense, and what RRF does. *(Your AML/CTF project is the answer here.)*
35. Reranking — why, and what it costs you in latency.
36. How do you refresh embeddings when source documents change.
37. Which vector DB and why; what were the alternatives. *(You have real Pinecone production experience — lead with that, not the hobby projects.)*
38. How does an agent decide which tool to call; what happens when a tool fails.
39. How do you stop an agent looping forever.
40. Prompt injection — through retrieved content or tool output.
41. Docker: image vs container, what goes in a Dockerfile, why you'd use compose. *(Your air-gapped build work is unusually strong here.)*
42. CI/CD — what your pipeline actually ran.
43. Git: merge vs rebase, resolving a conflict, what you'd do about a bad commit on main.
44. Unit vs integration tests; what you test in an LLM system specifically.

---

## Tier 3 — Design & scenario. One of these is likely.

45. Design a document Q&A system for an enterprise with 10,000+ documents and per-user permissions. *(This is your day job plus your tenant-isolation work — the strongest possible draw.)*
46. Design a REST API for a booking/ticketing system.
47. Scale a RAG system from 10k to 10M documents — what breaks first. *(Use the 6-move template in `story-bank.md`. The answer is never "the LLM.")*
48. How would you debug an API that got slow in production but is fine in staging.
49. How would you add caching to reduce LLM cost. *(You have the −30% cost claim; this is an invitation to use it.)*

---

## Tier 4 — Behavioural / HR. Short answers, then stop talking.

50. Walk me through your resume. *(90 seconds. Not five minutes.)*
51. Why are you looking to change.
52. Why Accenture / why a services company after product work. *(Have a real answer. This one catches people who obviously only want a raise.)*
53. Tell me about a difficult bug and how you found it.
54. A time you disagreed with a technical decision.
55. Biggest project you've owned end to end.
56. Where do you see yourself in three years.
57. Are you comfortable with client-facing work, shifts, relocation, return-to-office. *(Accenture asks. Know your answer before it's asked.)*
58. Notice period and expected CTC. *(One number, not a range — see `story-bank.md`.)*

---

## The three questions most likely to hurt you

**"You say 8+ years but your B.Tech is 2014."** One consistent number tied to 2016, one line, no defensiveness. Script it before you log in.

**"You were at Turing and KNS at the same time."** 25 seconds, volunteered before they find it. Your `answers/metric-defence.md` has the script — read it once today.

**"How exactly did you measure that 40% latency reduction?"** Every number on your resume is a live grenade if you can't state metric definition, baseline, n, and confounder in 30 seconds. See the claim-defence sheet.

---

## Ask them at the end (have two ready)

- What does the delivery team look like, and what would the first project be?
- Is this role building GenAI systems for clients, or maintaining existing applications? *(A real question, and it signals you're evaluating them too.)*
