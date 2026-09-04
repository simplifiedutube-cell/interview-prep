# Answer Frameworks — Accenture Custom Software Engineer

Format per the helper-app instructions: **Core Answer → Key Points → Mini Explanation → Example to Cite → Watch-outs.** The Mini Explanation is there so you can *explain the mechanism*, not recite it. Read it, close the file, say it in your own words. If you can't, you don't have it yet.

All examples are drawn from `Kadiam_Rao_Resume.docx`. Nothing here is invented.

---

## 1. "Explain how RAG works, end to end." [ACN-verbatim, highest frequency]

**Core Answer:** Retrieve relevant context from a knowledge base at query time, put it in the prompt, and have the model answer grounded in it rather than from memory.

**Key Points**
- Ingestion: documents → chunks → embeddings → vector store (+ metadata)
- Query: embed the question → similarity search → top-k chunks
- Optional: rerank, hybrid BM25 + dense, metadata filters
- Generation: chunks + question → prompt → answer, with citations
- Guardrail: if context is insufficient, say "I don't know" rather than generate

**Mini Explanation:** The core problem RAG solves is that an LLM only knows what was in its training data, and it can't tell you when it doesn't know something — it will produce fluent text either way. RAG fixes that by making the answer conditional on documents you control. At ingestion you split documents into chunks, convert each to a vector that captures its meaning, and store it. At query time you embed the question the same way and pull the nearest chunks. Those chunks go into the prompt as context, so the model is summarising a source rather than recalling. Everything hard about RAG is in the retrieval half — if the right chunk never gets fetched, no amount of prompting saves the answer.

**Example to Cite:** The 10,000+ document EdTech knowledge assistant — Pinecone, hallucination guardrails, automated eval dashboards, ~35% relevance improvement.

**Watch-outs:** They almost always follow with "what are you storing in the vector DB?" Answer: the embedding, the chunk text, and metadata for filtering — all three, not just the vector.

---

## 2. "What is the difference between Generative AI and Agentic AI?" [ACN-verbatim]

**Core Answer:** Generative AI produces an output; agentic AI decides on a sequence of actions and executes them against real systems.

**Key Points**
- GenAI: one input → one output, no state, no side effects
- Agentic: planning loop, tool calls, memory, termination condition
- The model becomes the reasoning engine, not the product
- Failure modes differ — GenAI hallucinates text, agents take wrong *actions*
- Needs orchestration, observability, guardrails, human-in-the-loop escalation

**Mini Explanation:** With plain generative AI the model writes something and a human decides what to do with it — the blast radius is a bad paragraph. An agent is given a goal instead of a prompt, and it loops: decide what to do, call a tool, look at the result, decide again, until some stopping condition. That loop is where all the engineering lives. The model is no longer producing the deliverable; it's choosing actions, and a wrong choice mutates a real system — a CRM record updated, a PR merged, an email sent. So agentic systems need things generative ones don't: retry and idempotency on tools, loop termination, tracing so you can reconstruct why it did what it did, and an escalation path when it's uncertain.

**Example to Cite:** The agentic coding assistant at Turing — multi-step orchestration with tool calls wired into PR and CI/CD hooks, ~45% cut in manual review turnaround.

**Watch-outs:** Follow-up is usually "when is an agent the *wrong* solution?" Have it: when the task is deterministic, when a wrong action is expensive and irreversible, or when a scripted pipeline would do the same job more cheaply and predictably.

---

## 3. "Have you heard about MCP?" [ACN-verbatim]

**Core Answer:** Model Context Protocol — an open standard for connecting models to tools and data sources, so integrations aren't rebuilt per app.

**Key Points**
- Solves the M×N integration problem: M apps × N tools becomes M + N
- Client–server: your app hosts a client, each integration is a server
- Three primitives with different control: **tools** model-controlled, **resources** app-controlled, **prompts** user-controlled
- Announced Nov 2024; you adopted it late in the Turing engagement as it emerged

**Mini Explanation:** Before MCP every team wrote bespoke glue between their app and each tool, and none of it was reusable. MCP standardises that boundary: a tool provider writes one server, any MCP-aware client can use it. The control distinction is the part worth knowing because it's a safety design, not a technicality — tools are the things the *model* decides to invoke, resources are context the *application* chooses to supply, and prompts are templates the *user* triggers. Keeping those separate means the model can't quietly pull in context nobody sanctioned.

**Example to Cite:** MCP adoption in the coding-assistant work at Turing, in the last stretch of the engagement.

**Watch-outs:** ⚠️ Timeline trap flagged in your own `metric-defence.md` — MCP was announced 25 Nov 2024 and the Turing engagement ended Jan 2025. Say "in the last stretch of that engagement," not "throughout." Don't let them do that subtraction out loud.

---

## 4. "Your RAG hallucinates even though the right context was retrieved. Fix it."

**Core Answer:** Retrieval is fine, so the problem is in generation — constrain the model to the context and make abstention possible.

**Key Points**
- Prompt: explicit instruction to answer only from context, and to say "I don't know"
- Require citations per claim — makes ungrounded claims visible
- Lower temperature; check whether context is buried mid-prompt (lost-in-the-middle)
- Post-hoc faithfulness check: does each claim trace to a retrieved chunk
- Check the chunk actually *contains* the answer, not just the topic

**Mini Explanation:** When retrieval is correct and the answer still drifts, the model is blending the context with its own parametric knowledge — usually because nothing in the prompt told it that the context is the *only* permitted source, or because there's no acceptable way for it to fail. If "I don't know" isn't an allowed output, the model will always produce something. Adding citations helps twice: it disciplines the generation, and it makes the failure auditable afterwards. Position matters too — models attend less to material in the middle of a long prompt, so a correct chunk sitting in the middle of fifteen others can effectively be ignored.

**Example to Cite:** The hallucination guardrails on the 10k-doc assistant, with continuous accuracy tracking.

**Watch-outs:** Don't jump straight to "fine-tune it." That reads as reaching for the expensive tool first.

---

## 5. "How do you evaluate a RAG pipeline / LLM system?"

**Core Answer:** Evaluate retrieval and generation separately, against a golden set, with production monitoring on top.

**Key Points**
- Retrieval: context precision / recall, hit rate at k
- Generation: faithfulness (grounded in context), answer relevance
- Golden dataset of question/answer pairs; who labelled it matters
- LLM-as-judge for scale, but validate the judge against human labels
- Production: track accuracy continuously, not just at build time

**Mini Explanation:** The reason you split the two is diagnostic — a bad answer tells you nothing on its own, but "retrieval recall was 0.9 and faithfulness was 0.4" tells you exactly which half to fix. The golden set is the expensive part and the part people skip; without it you're comparing vibes across prompt versions. LLM-as-judge makes evaluation affordable, but a judge is a model with its own biases — it favours longer answers and its own phrasing — so you validate it against a few hundred human-labelled examples before trusting it, and you re-check when you change judge models.

**Example to Cite:** The eval harnesses, rubrics and benchmark definitions you built at Turing — accuracy, latency, reliability, cost — after which agent task success rose ~20%.

**Watch-outs:** This is your strongest territory and most candidates are weak in it. Spend a beat longer here than elsewhere. Follow-up: "how does LLM-as-judge fail?"

---

## 6. "async vs threading vs multiprocessing in Python — and the GIL"

**Core Answer:** async for I/O-bound concurrency, multiprocessing for CPU-bound work, threading rarely the right answer in between.

**Key Points**
- GIL = one thread executes Python bytecode at a time in a process
- I/O releases the GIL, so threads help with I/O but not CPU
- asyncio: single thread, cooperative, no GIL contention, huge concurrency at low cost
- multiprocessing: separate interpreters, real parallelism, IPC cost
- FastAPI: `async def` runs on the event loop; blocking code inside it stalls everything

**Mini Explanation:** The GIL means CPU-bound Python doesn't get faster with threads, because only one thread runs bytecode at a time. But most backend work isn't CPU-bound — it's waiting on a database, an HTTP call, an LLM API. During that wait the GIL is released, so concurrency is achievable. Async is the cleaner way to express it: one thread, an event loop, and tasks that voluntarily yield while waiting. The trap in FastAPI is mixing models — if you put a blocking call inside an `async def` handler you block the whole event loop, and throughput collapses for every request, not just that one. Blocking work goes in a regular `def` handler, which FastAPI runs in a threadpool.

**Example to Cite:** The .NET → FastAPI/Pydantic/SQLAlchemy migration, and the LLM-serving paths where latency dropped ~40%.

**Watch-outs:** Be ready for "so how did you actually cut latency 40%?" — that's a metric-defence question, not a Python question. Prefill vs decode, caching, prompt/context reduction. See `answers/01-latency-and-cost.md`.

---

## 7. "Why FastAPI over Flask or Django?"

**Core Answer:** Native async plus Pydantic type validation and generated OpenAPI docs — it fits API-first services better than either.

**Key Points**
- Async-first: matters when every request awaits an LLM or DB call
- Pydantic: validation and serialisation from type hints, errors at the boundary
- Auto OpenAPI/Swagger — real value on client-facing integration work
- Django is heavier and batteries-included; right for admin/ORM-driven apps, not thin services
- Flask is minimal but async support and validation are bolt-ons

**Mini Explanation:** The honest version is that the choice follows the workload. If your service spends most of its time waiting on other systems, async concurrency is the difference between handling tens and thousands of simultaneous requests on the same box. Pydantic then removes an entire class of bug by validating at the edge — bad input fails with a clear 422 instead of surfacing as a `None` three layers down. Django earns its weight when you want its ORM, admin and auth as a package; for the API-and-integration services you've been building, most of that goes unused.

**Example to Cite:** Migrating legacy .NET logic to FastAPI/Pydantic/SQLAlchemy services — improved response times, easier to maintain.

**Watch-outs:** Don't say "FastAPI is faster" and stop. That's the answer of someone who read a benchmark chart, and the follow-up ("faster at what?") is where it falls apart.

---

## 8. "Design a document Q&A system for an enterprise, with per-user permissions"

**Core Answer:** Standard RAG pipeline, but permissions enforced as a hard filter in the data layer — never as a prompt instruction.

**Key Points**
- Ingest → chunk → embed → store with tenant/ACL metadata
- Query: resolve user's permissions *first*, filter, then search
- Hybrid retrieval (dense + BM25, RRF) then rerank if latency allows
- Citations back to source documents
- Eval harness + monitoring; freshness/re-index strategy for changed docs

**Mini Explanation:** The interesting decision here isn't the retrieval stack, it's where isolation lives. If you tell the model "only use documents this user can see," you've made a security control out of an instruction the model may ignore or be talked out of — one prompt injection in a retrieved document and it leaks. Enforcing it as a predicate in the query means the unauthorised chunks are never candidates in the first place; the model cannot leak what was never put in front of it. The cost is that filtering before an approximate nearest-neighbour search can hurt recall, especially when a user can see only a small slice of the corpus, and that trade-off is worth naming out loud.

**Example to Cite:** The AML/CTF compliance assistant — multi-tenant, tenant isolation as a SQL predicate rather than a prompt instruction, hybrid dense + BM25 with RRF and cross-encoder rerank. Also the 10k-doc production system at KNS.

**Watch-outs:** This is the strongest single design decision you have. Know precisely *why* prompt-level isolation fails, because if they're any good that's the follow-up.

---

## 9. "Walk me through your resume"

**Core Answer:** 90 seconds, arc not inventory: backend → ML → owning AI features, with the through-line being systems that had to work in production.

**Key Points**
- 8+ years, started 2016; Centific (enterprise assistants) → KNS (AI features on an EdTech platform) → Turing contract (agent training and evaluation)
- Currently: own the AI features end to end — backend, ML pipelines, dashboards
- Signature work: 10k-doc RAG with guardrails and eval dashboards; agentic coding assistant into PR/CI-CD; air-gapped agent training environments
- The differentiator: evaluation — you built the harnesses that decided ship/no-ship

**Mini Explanation:** Interviewers use this to pick what to probe, so it's a menu you're writing for them, not an autobiography. Lead with the shape of the career and land on the two or three things you most want to be asked about. Stop at 90 seconds even if you haven't covered everything — trailing off into year five of a chronological list is the most common way this question goes badly, and the interviewer stops listening well before you stop talking.

**Example to Cite:** Land on the 10k-doc RAG and the eval-harness work; let them pull the rest.

**Watch-outs:** Don't open with tool names. Open with the problem. And expect the Turing/KNS overlap question immediately after — volunteer it rather than waiting.

---

## 10. "Why Accenture?"

**Core Answer:** Breadth of client problems and the chance to apply GenAI systems across industries rather than one product surface.

**Key Points**
- Your consulting-shaped background already: 6+ client engagements, five-system CRM integration, offline/air-gapped constraints
- You like shipping under real client constraints, not lab conditions
- Scale of GenAI delivery Accenture is doing across regulated industries
- Hyderabad-based, comfortable with client-facing work and office presence

**Mini Explanation:** The failure mode on this question is answering it as if it were "why any job." Interviewers at services firms are specifically screening for people who will be fine with client-facing delivery, changing project contexts, and constraints someone else set — because that's the job, and people who quietly wanted a product role leave within a year. Your actual history supports the honest version: multi-client delivery, integration work against systems you didn't control, and shipping into an air-gapped environment is about as constrained as delivery gets.

**Example to Cite:** The 6+ client engagements at Turing and the offline containerised training environments.

**Watch-outs:** Don't say anything that reads as "I want out of my current role." Frame forward.
