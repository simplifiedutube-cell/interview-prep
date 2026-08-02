# Story Bank

**Build Days 3–5.** The strongest evidence base in behavioral research — ~500 recorded Amazon LP interviews with outcomes, from 100,000+ mocks — produced one finding that kills the framework debate:

> **The #1 reason for a no-hire is the *wrong story*, not the delivery.**
> Every identified error in down-levelled senior candidates was story **selection**, not delivery.

So: **30 minutes on frameworks total, then stop shopping.** Use **STAR + the "L" from CARL** (add a Learning beat at the end). Spend the other 20 hours on selection and evidence.

**Timing:** 10 / 10 / 50 / 30 — Situation 10%, Task 10%, **Action 50%**, Result 30%. Two lengths per story: a **60-second** version and a **4-minute** version.

**Two rules that decide the senior signal:**
1. **"I", never "we", in every Action beat.** Your Turing client stories are the exposure — you led or co-led several engagements, so say what *you* did.
2. Every story needs a **"delta from the level below"** line: what makes this a *senior* story rather than a competent mid-level one. Usually: scope, ambiguity absorbed, people influenced without authority, or a decision you owned that could have gone wrong.

---

## Coverage matrix

Fill as you go. **Every column needs ≥2 entries. No story may be primary for more than 3 competencies.**

| # | Story title | Tech problem-solving | Learning / failure | Business delivery | Interpersonal conflict | Ambiguity / ownership |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |

### Amazon's 16 Leadership Principles → story map

| LP | Primary story | Backup |
|---|---|---|
| Customer Obsession | | |
| Ownership | | |
| Invent and Simplify | | |
| Are Right, A Lot | | |
| Learn and Be Curious | | |
| Hire and Develop the Best | | |
| Insist on the Highest Standards | | |
| Think Big | | |
| Bias for Action | | |
| Frugality | | |
| Earn Trust | | |
| Dive Deep | | |
| Have Backbone; Disagree and Commit | | |
| Deliver Results | | |
| Strive to be Earth's Best Employer | | |
| Success and Scale Bring Broad Responsibility | | |

---

## ⚠️ The two mandatory missing stories

Research flagged these as absent and as the exact place senior candidates get down-levelled. **Most people only prepare the version where they were right — that's the tell.** Write these first.

### Missing story A — A failure with a *named cost*

Not "I learned a lot." A number, a delay, a customer, a rollback. What it actually cost, who it affected, what you did in the next 24 hours, and what changed structurally afterward so it couldn't recur.

- **Title:**
- **Situation:**
- **Task:**
- **Action (I, not we):**
- **Result — the cost, named:**
- **Learning + the structural change:**
- **Delta from the level below:**
- **60-second version:**

### Missing story B — A disagreement you **lost** and then **committed to**

The senior signal is the commit, not the disagreement. Show that you argued a real position with evidence, lost, and then executed the other path well — without sandbagging it.

- **Title:**
- **Situation:**
- **Task:**
- **Action — your argument, the evidence you brought, who decided:**
- **Result — how you executed the decision you disagreed with:**
- **Learning — what you'd revisit, and whether you were later proved right or wrong:**
- **Delta from the level below:**
- **60-second version:**

---

## Story template ×10

Copy this block for each. Candidate raw material from your background, so you don't stare at a blank page:

> Air-gapped Dockerized agent training environments (no network at all) · deterministic UI-state verification so every agent action could be checked rather than eyeballed · the 10k-doc RAG with hallucination guardrails · the −40%/−30% latency and cost work · the .NET → FastAPI/Pydantic/SQLAlchemy migration · leading/co-leading delivery across 6+ Turing client engagements · CRM integration across five systems validated end to end · the sub-800ms Indic voice agent and its config-driven multi-tenancy · tenant isolation enforced as a SQL predicate rather than a prompt instruction · reviewing and rating model-generated code · RL gym environments and the rubrics that went with them · Microsoft security ops incident response at Centific · running freelance client work from first scoping call through delivery.

### Story __

- **Title** *(must tease both the challenge and the impact — this is what makes an interviewer pick it):*
- **Competency bucket(s):**
- **LPs it serves:**

**Evidence points — need 3–5, and they must span all three types:**
- Quantitative:
- Qualitative:
- Organizational *(who was affected / who changed behaviour / what process changed)*:

**Situation (10%):**

**Task (10%):**

**Action (50%) — "I", specific, decision-by-decision:**

**Result (30%) — numbers, and what happened afterward:**

**Learning:**

**Delta from the level below:**

**60-second version:**

**4-minute version:** *(record it, watch it back once)*

**Back-pocket fact sheet — must survive 4 follow-ups:**
- Numbers:
- Dates:
- Team size, and your role in it:
- Who disagreed, and what they argued:
- The alternative you rejected, and why:
- What it cost:
- What you'd change:

---

## The project deep-dive round (50 minutes, PARL)

**Lead with the AML/CTF compliance RAG.** It's the right choice specifically because it is **solely yours** — no client attribution risk, no numbers you can't access, and it's a complete senior retrieval architecture (hybrid dense + BM25 → RRF → cross-encoder rerank, tenant isolation as a SQL predicate rather than a prompt instruction).

Prepare:

- [ ] **A drawn architecture diagram you can reproduce on a whiteboard in 3 minutes**
- [ ] **3 decisions you can defend**, each with the alternative you rejected and why *(e.g. RRF over score-fusion; cross-encoder rerank over bigger top-k; SQL predicate over prompt-level tenant instruction — that last one is the strongest single design decision on your resume, so know exactly why prompt-level isolation fails)*
- [ ] **2 real failures** and what they cost
- [ ] **Results with method and honest confidence intervals**
- [ ] The **"what would you do at 100×"** answer (below)

## "What would you do at 100×" — the 6-move template

Prepare one per project. This is asked constantly and almost nobody has a structured answer.

1. **State the unit and the load.** *"Today it's X docs / Y QPS / Z tenants. At 100× that's…"*
2. **Do the arithmetic out loud.** *(e.g. 10M docs × 15 chunks × 1024 dims × 4 bytes ≈ 600 GB of vectors — so the index no longer fits in memory, and that's the first thing that changes)*
3. **Name what breaks first — and it is never "the LLM."** Usually: the index doesn't fit in RAM, the reranker becomes the latency floor, the tenant filter turns ANN search into a recall cliff, or the ingestion pipeline can't keep up with freshness.
4. **Give the cheap fix, then the structural fix, then say where you'd stop.**
5. **Do the cost math and name a >50% lever.**
6. **Say what you'd degrade rather than scale.** *(Which is the senior move, and the one most candidates never make)*

- [ ] AML/CTF RAG at 100×
- [ ] Voice agent at 100×
- [ ] The 10k-doc EdTech RAG at 100×

## Pitches — record 10 takes each, watch back once

- [ ] AML/CTF compliance RAG — 3 min + 60 sec
- [ ] Indic voice agent — 3 min + 60 sec
- [ ] Eval harness (once built, Week 3) — 3 min + **10-min unscripted walkthrough**

**Exit criterion:** delivered in **one take**, no filler, and **no tool name in the first 30 seconds.** Start with the problem and the constraint, not with "I used Pinecone and FastAPI."

---

## Recruiter-screen script

The highest-rejection-rate round in any loop, and currently unscripted. Write your lines here.

- **Comp — one number, not a range.** *(A range is heard as its floor.)* Benchmarks: senior AI engineer at 6–9 yrs ≈ **₹42–66L Hyderabad-indexed, ₹48–72L Bangalore**; AI Engineer carries a **40–60% premium over Backend**. India SWE median TC ₹29.7L, p75 ₹48.6L, p90 ₹69.9L (levels.fyi, Aug 2026).
  - My number: ______________
- **Current CTC** — decline politely, give expected instead. A small-EdTech CTC will anchor you low.
- **Availability** — ⚡ **you can start immediately, and that's a real advantage.** Notice period is the #1 silent killer of US-startup processes from India, and you don't have one. Volunteer it.
- **Timezone** — never "I'm flexible." *"I'll hold 6:30–11:30 pm IST as core hours; I did exactly that for a year on US-client work at Turing."* That's a credential, not a promise.
- **Ask them in round 1:** EOR, contractor, or GCC entity? It determines equity eligibility, comp and tax.
- **The 2014 B.Tech vs "8+ years"** — one consistent number tied to 2016, one line, not defensive:
- **The Turing/KNS overlap** — 25 seconds, volunteered before they find it (script in `metric-defence.md`):

## Company values prep

- [ ] **Anthropic** — read the RSP; be ready to discuss honest moral complexity, not just enthusiasm. *(Apply to **Applied AI**, 3/5 difficulty — not MTS Track A, which is a 90-min CodeSignal gate at 4.5/5)*
- [ ] **Sierra** — their five values; their engineering blog on the AI-native interview
- [ ] **Harvey** — why legal AI specifically
- [ ] **Glean** — enterprise search + permissions, which maps directly to your tenant-isolation work

## Customer-conversation / discovery round (FDE + Anthropic Applied AI)

~60% of FDE/Applied-AI loops include this, and **the failure mode is demoing instead of investigating.** Practice with a peer playing *"VP Eng at a 5,000-person fintech."* Your consulting background helps; you've just never rehearsed discovery questioning.

- [ ] 3 reps, recorded
- [ ] Rule: **no solution before you've asked five questions**
