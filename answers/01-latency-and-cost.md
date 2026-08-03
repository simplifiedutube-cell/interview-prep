# Claims 1 & 2 — Latency −40% and Cost −30%

> **Model answers — read this first.**
>
> These are *scripts for things you actually did*. Every fact only you can know appears as a `[BRACKETED SLOT]`. **Never walk into an interview with a bracket unfilled** — an unfilled bracket spoken aloud sounds exactly like a lie.
>
> If a sentence in a model answer isn't true of your work, **don't say it** — use the honest variant printed alongside it. A rehearsed false claim about methodology is the worst outcome available in these interviews, worse than losing the number, because it's a trust finding rather than a skills gap.
>
> Fill your real facts into `metric-defence.md` first. This file shows you the *shape*, *depth* and *honesty calibration* of a strong answer — not the data.

---

> ⚠️ **ILLUSTRATIVE NUMBERS, NOT YOUR DATA.** Every figure below (latencies, percentages, dates, counts, dashboards, tool names) is ONE internally-consistent fictional-but-plausible example, built so you can see what a *complete* answer sounds like with no missing pieces. **None of it is verified fact about your actual systems or your life.** Before you say any of this in an interview, replace every number with your real one — and where your real answer is "I don't know" or "I never measured that," use the honest fallback script the document already gives you for that case, don't just leave this illustrative number in. The biographical details in this file (disclosure stories, dates, reasons for gaps) are ESPECIALLY placeholder — they are not a suggestion of what actually happened to you. Use your own true story there, always.

---

## Claim 1 — "Cut average LLM latency by about 40%"

**Why this one is dangerous:** The word "average" is a percentile-shaped hole — every senior interviewer will ask "p50 or p95?" within thirty seconds, and "average" usually means p50, which is the least interesting number. Worse, latency is the metric where candidates most often credit the wrong mechanism: they say "prompt optimization" when the wall-clock was dominated by decode, which prompt length barely touches. If he can't split prefill from decode, the number reads as borrowed from a dashboard he didn't build.

**The second danger, which the old version of this doc missed:** the same three mechanisms (caching, context trimming, model routing) are credited for *both* the 40% latency claim and the 30% cost claim. An interviewer reading both resume lines in sequence will ask whether this is one project counted twice. See "The attribution-overlap trap" below — he must have that answer ready before he walks in.

### Before he uses any of this — the honesty gate

Every ✅ answer below contains sentences that **assert instrumentation**. Before rehearsing them, he must answer these three questions truthfully, because each answer unlocks a different tier of the script:

| Did he actually… | If yes | If no |
|---|---|---|
| Log per-stage timings (retrieval / rerank / LLM / guardrail) per request? | He can use the full decomposition script. | He must say "I didn't decompose it at the time" and use the Tier-2 script. Do **not** say "the decomposition surprised me." |
| Run ablations (turn one mechanism off, measure)? | He can attribute per-mechanism deltas in ms. | He can only **rank** mechanisms and must say so. Do **not** fill in per-mechanism ms brackets. |
| Have a named observability tool (OTel / Langfuse / Datadog / etc.)? | Name it — for this scenario, that's per-stage timings written to structured JSON application logs, aggregated nightly into a Postgres table, and visualized in an internal Metabase dashboard. | Say what he actually had: "timings written to application logs and aggregated in SQL," or "a benchmark script over a fixed query set." That is a legitimate answer. A made-up tool name invented under pressure is not. |

**The rule:** if a bracket below cannot be filled with something he could produce evidence for in ten minutes, he drops the sentence containing it rather than guessing. A shorter true answer beats a longer defensible-sounding one.

### The opening question

> "40% — walk me through how you measured that, and where the time actually went."

**❌ What most candidates say** (and why it loses):

> "We optimized our prompts, trimmed the context we were sending, and added caching. That brought our average response time down by about 40%, which was a big win for the user experience — the assistant felt a lot snappier."

The tell is "felt a lot snappier" sitting next to a hard number. It signals the 40% came from a vibe or one before/after screenshot, not an instrumented comparison — and once an interviewer decides one number is soft, they re-read the entire resume as soft.

**✅ Model answer — 25 seconds** (recruiter screen or passing mention):

> "That's p95, end-to-end from the user's message to the last token — 4,100 ms down to 2,500 ms, about a 39% cut — over 6 weeks and roughly 850,000 requests, measured from per-stage timings written to our application logs. Three mechanisms, in order of impact: prompt-prefix caching on the frozen system prompt and few-shot examples, cutting the retrieval funnel to top-50 retrieve, rerank, top-5 into the prompt, and routing about 60% of queries — the simple factual lookups — to a smaller model. Streaming was separate — that moved perceived latency, not total."

**✅ Model answer — 2 minutes, Tier 1** (use only if he genuinely has per-stage timings):

> "Let me start with what I measured, because that determines whether the number means anything. It's end-to-end, request received to last token emitted, at p50 and p95, over 6 weeks and about 850,000 requests — per-stage timings logged to structured JSON, aggregated nightly into Postgres, visualized in Metabase — against a 6-week baseline window immediately prior. Headline is about 39% at p95 — 4,100 ms down to 2,500 ms; at p50 it was about 28% — 1,800 ms down to 1,300 ms. I want to flag that gap rather than let it hide: the optimizations targeted the tail, not the median, so p50 moving less than p95 is expected, not a discrepancy.
>
> On the decomposition: total per LLM call is TTFT plus output tokens times inter-token latency. Prefill — that's TTFT — is compute-bound and scales with input length. Decode is memory-bandwidth-bound: every output token streams the model weights and the KV cache out of memory, so prompt size barely touches it. I did the arithmetic on our actual shape rather than assuming: roughly 2,000 input tokens and about 450 output tokens, at roughly 4 ms per output token, put decode at about 78% of the LLM-call time — call it 500 ms TTFT plus 1,800 ms of decode, so about 2,300 ms per call. And our request wasn't one call — it was retrieval, then rerank, then the generation call, then the groundedness check, so the LLM call was about 56% of end-to-end on the baseline (roughly 2,300 ms of the 4,100 ms), and the rest was pipeline.
>
> What actually moved it: prompt-prefix caching on the frozen system prompt and few-shot examples, about 650 ms. Cutting the retrieval funnel — top-50 candidates into a cross-encoder rerank, top-5 into the prompt — saved roughly 730 ms in prefill from the shorter context, but that buys a reranker on the critical path at around 180 ms, so the net was about 550 ms. Routing about 60% of queries — the simple factual lookups — to a smaller, faster model saved roughly 670 ms on that slice, about 400 ms weighted across all traffic.
>
> One nuance on caching that took me a while to see: prefix caching only covers the *stable head*. The retrieved chunks are volatile and sit after the cache breakpoint, so they get re-prefilled every single request. That's exactly why trimming the retrieval funnel still moved TTFT even after caching was on — they're not redundant, they hit different halves of the prompt.
>
> Two things I don't claim. Streaming changed perceived latency — TTFT to the user went from about 1,100 ms to about 350 ms — but the last token landed at roughly the same time, so it doesn't belong in a total-latency number. And continuous batching, speculative decoding, and quantization are serving-layer levers; we were on a hosted API, so those weren't mine.
>
> The confounder I couldn't fully rule out is that the mechanism split itself isn't from a controlled experiment — I shipped it as a staged rollout, one flag at a time for about a week each, and the prompt-caching change and the retrieval-funnel change both landed inside the same two-week release window. So the total, 1,600 ms at p95, is solid — that's measured before and after the whole window. But the exact 650/550 split between those two specific mechanisms is an estimate from watching the dashboard move as each flag went live, not an ablation, and I'd say that plainly if pushed. The clean version is an interleaved A/B on live traffic — same window, same mix, both arms — and that's what I'd run now."

**✅ Model answer — 2 minutes, Tier 2** (use if he did *not* instrument per-stage — this is the honest version and it still scores well):

> "I'll be precise about what I can and can't back. The measurement was end-to-end wall clock — timestamped at request-in and last-token-out in our application logs — over 6 weeks and about 850,000 requests, and I report it at p95. What I did **not** do at the time was decompose it per stage — I know the total moved, I can rank the mechanisms by when the drop appeared relative to when each shipped, but I can't hand you a per-mechanism millisecond breakdown and I'm not going to invent one.
>
> What I can tell you is the model of where the time goes, because it's what I'd use now. Total per call is TTFT plus output tokens times inter-token latency. Prefill is compute-bound and scales with input length; decode is memory-bandwidth-bound and barely cares about prompt size. On our shape — roughly 2,000 input and 450 output tokens — decode should dominate the LLM call, which means the instinct to shorten the prompt was aimed at the smaller half. That's the thing I'd check first if I did it again, and it's the reason I now profile the split before choosing a lever.
>
> Streaming I keep separate — it changed perceived latency, not total. And serving-layer levers like continuous batching and speculative decoding weren't mine on a hosted API.
>
> The clean way to get a defensible number is an interleaved A/B on live traffic, reported at p50 and p95 separately with a sample size that supports a p95. That's what I'd run now."

**Why this works:**
- Leads with the measurement definition before the number — the single strongest anti-inflation signal.
- Names the prefill/decode split and gets the physics right (compute-bound vs memory-bandwidth-bound), without claiming to have profiled a serving engine he never ran.
- Does the arithmetic *out loud* rather than asserting "decode dominated" — because in a long-context RAG system with short answers, prefill genuinely can dominate, and an interviewer who has seen that regime will test whether he's reciting or reasoning.
- Names the caching/retrieval interaction (stable head cached, retrieved chunks not) — this is the sentence that separates people who turned caching on from people who understand it.
- Tier 2 exists so the honest version is still a *good* answer, not a retreat.
- Ends by naming a confounder and the experiment that resolves it.

### The follow-up chain — they will not stop at one question

**Q: "Is that p50 or p95? What happened to the tail?"**
**A:** "p95 moved about 39%; p50 moved about 28% — and I care more about p95, because that's the number users actually feel and the one an SLO gets written against. If I'd only moved p50 I'd say so, because a p50 win with a flat p95 usually means you sped up the easy path and left the pathological queries alone. In our case the tail was driven by long retrieved documents pushing close to the context window and occasional reranker latency spikes under school-hours load, and I added a token budget that truncates the lowest-ranked chunk before it can blow the context window — that closed most of the gap between the p50 and p95 wins. If the p95 hadn't moved, the honest framing is 'faster on the common path, tail unchanged,' and the tail is what I'd have gone after next."
*Signal:* Knows the tail is the real SLO, and will state a weaker result accurately rather than let "average" do the hiding.

**Q: "How many requests is that p95 computed over?"** ← *new; the quantitative interviewer's first move*
**A:** "About 850,000 requests over 6 weeks. And I'd flag that a p95 needs volume to be stable — only 5% of your sample sits above it, so a few hundred requests gives you a handful of observations defining the number and the rank-based confidence interval is wide. Below roughly a thousand requests per arm I'd report the p95 with an explicit caveat rather than to two decimal places. Our volume was adequate here — at 850,000 requests, even the top 5% is over 40,000 observations, so the p95 itself is stable; where I'd be more careful is a p99, which is a much smaller slice of that same sample."
*Signal:* Knows percentiles have sampling error. Most candidates have never thought about this and will confidently quote a p99 computed over 300 requests.

**Q: "Was that measured client-side or server-side? Where were the clients?"** ← *new*
**A:** "Server-side, at our API boundary — so it excludes the student's client network. That matters here: we were serving from India against a provider region in the US, so there's a fixed round trip of roughly 200 ms in every client-observed number that no prompt change will ever touch. If the 40% is a server-side number, the user-perceived improvement is smaller in percentage terms because the network constant dilutes it. Region selection wasn't a lever available to us — we were on a single shared hosted endpoint. I'd rather tell you which boundary I measured at than let the bigger-sounding number stand unqualified."
*Signal:* Understands that a percentage is meaningless without a boundary, and that geography is a latency term.

**Q: "What about retries and rate limits? Those usually own the tail."** ← *new*
**A:** "That's the right question and it's where a lot of tail lives. SDKs retry 429s and 5xxs with backoff by default — commonly a couple of retries — so a single logical request can be three round trips plus backoff and land far out in the tail without anything being 'slow.' We did see a meaningful retry rate, mostly during the school-hours bursts when traffic climbed toward its peak — I tracked attempts-per-request as a field alongside the stage timings, and it ran a couple of percent of requests with more than one attempt. If I hadn't separated retried requests from clean ones, my p99 would be measuring my rate-limit headroom, not my prompt. The fix is to log attempt count per request and report clean-path and retried latency separately."
*Signal:* Has thought about the operational layer, not just the prompt layer. This one is almost never prepared for.

**Q: "Which single change gave you the most, and what did it cost you?"**
**A:** "Prefix caching — the largest single contributor, about 650 ms of the 1,600 ms we saved at p95. The cost was accuracy on the boundary cases from the routing change: the router misclassifies some hard queries as easy, so I had to add an escalation path when the small model's answer failed the groundedness check, which means those queries pay both models. I tracked the escalation rate — the share of small-model answers that failed the groundedness check and got retried on the larger model — as the guardrail; it ran around 10%. If it crossed that, the routing was net-negative on both cost and latency, because you're double-paying."
*Signal:* Understands that every latency lever has a price, and that a cascade's escalated queries cost small + large, not just large.

**Q: "You added a cross-encoder reranker. That's pure added latency. How did that net out?"**
**A:** "It is — a hosted cross-encoder on ~50 documents is typically low hundreds of milliseconds, and it varies a lot with document length, batch size, and network distance to the provider, so I'd quote our measured number rather than a general one: about 180 ms for us. The reranker is a floor I'm paying to buy token reduction. It nets positive only if the tokens I remove from the prompt cost more prefill time than the rerank costs. For us at top-50 → top-5, roughly 1,200 tokens removed from what used to go straight into the prompt, that was worth it: about 730 ms saved in prefill against about 180 ms of rerank, a net win of roughly 550 ms. If my prompt had been small to start with, adding a reranker would have made latency worse. The real reason we kept it was retrieval recall and grounding quality — fewer but higher-relevance chunks meant the groundedness check passed more often too — and the latency was a genuine net win on top of that."
*Signal:* Can reason about a component that hurts one metric to help another, and won't retrofit a quality decision as a latency win.

**Q: "Did you consider caching at the app layer, not just the provider's prefix cache? What's the difference?"**
**A:** "Yes — they're different mechanisms. Provider prefix caching is a prefix match on the rendered prompt: it skips prefill for the stable head, so it cuts TTFT and input cost, but you still generate every output token — it does nothing for decode. Semantic caching is app-layer: embed the incoming query, ANN lookup against past queries, and if similarity clears a threshold you return the stored answer and skip the model entirely — that's a sub-100 ms response instead of seconds. We did run semantic caching, because an ~18% hit rate on our workload made it worth the added lookup and the correctness risk was manageable with the right guardrails. The guardrails I'd insist on are a conservative similarity threshold tuned on labeled near-miss pairs, a TTL so answers go stale when the corpus changes, and a per-tenant namespace so one org can never read another's cached answer."
*Signal:* Distinguishes two things most candidates blur into "caching," notes that prefix caching can't touch decode, and reaches for tenant isolation unprompted.

**Q: "Your resume also says you have hallucination guardrails. Isn't that another model call on the critical path?"** ← *new; he wrote this on his own resume, so it's fair game*
**A:** "It is, and it belongs in the latency budget. Ours was a groundedness check that ran synchronously before returning, only on the small-model path, as the escalation trigger — if it failed, we retried on the larger model. That means end-to-end on that slice is the sum of the generation call and the check, and the check has its own TTFT plus decode. It cost us roughly 150 ms on the slice where it ran. If I were optimizing that today the options are: run it on a small model, run it only on the routed-to-small slice, run it concurrently with streaming the answer and retract or annotate on failure, or make it a non-LLM check where the claim-to-span match can be done with retrieval overlap. The honest version is what we actually did — running it synchronously only on the routed-to-small-model slice, since that's the path where a wrong answer was most likely."
*Signal:* Treats his own guardrail as a latency cost rather than a free feature. An interviewer who spots the guardrail on the resume and finds it missing from the latency budget concludes he never owned the budget.

**Q: "What did you try that didn't work?"**
**A:** "Aggressive prompt shortening was the biggest disappointment. I cut about 400 tokens out of the system prompt expecting a real win and got about 40 ms — because prefill was a smaller slice of the total than I'd assumed, and the stable head was already being prefix-cached, so I was optimizing a part that was nearly free. Second: I tried lowering top-k below 5 and retrieval recall dropped enough that the groundedness score fell, so I reverted it. The lesson was to profile the split before choosing the lever — I did those in the wrong order."
*Signal:* Failure with a diagnosis attached. The specific admission that he optimized the wrong half is more credible than any success story.

**Q: "Who else was changing the system during your measurement window?"** ← *new*
**A:** "I owned that latency path end to end, but the retrieval and indexing side of the system was shared — a teammate was iterating on chunking strategy in the same quarter, so a corpus re-chunk could in principle have shifted retrieval time independent of anything I shipped. It's a fair challenge: if the before and after windows are weeks apart, anything could have moved in between — infrastructure changes, a provider-side model update behind a stable alias, a dependency upgrade, seasonal traffic mix. That's a large part of why I'd run it as an interleaved A/B now: both arms take the same drift, so the comparison survives things I don't control and don't know about."
*Signal:* Understands that a before/after window is a quasi-experiment with an unbounded confounder set, and names the design that closes it.

**Q: "What would you do next for another 40%?"**
**A:** "Output tokens, because that's where the wall clock is in the generation call. Concretely: cap max output length and enforce a response-shape contract so the model stops padding, structured output instead of prose where the consumer is code, and parallelize the retrieval, guardrail, and embedding calls that are currently serial — that's often the biggest single win in a multi-call pipeline and it costs no quality. Then a semantic cache on the head of the query distribution if the hit rate justifies it, and check whether a nearer provider region is available. If we ever self-hosted, continuous batching and speculative decoding are the next tier — but I'd be learning those, I haven't run them."
*Signal:* Targets the dominant term rather than listing tactics, names serial-to-parallel (free latency, no quality cost), and draws a clean line around what he hasn't done.

**Q: "Did the latency win show up in any business metric?"** ← *new*
**A:** "I don't have a clean read on that, and I'd rather say so. We were in EdTech, so the plausible downstream metrics are session completion, questions per session, abandonment. If I'd designed the rollout as an A/B I'd have had that read; as a before/after I don't, because anything seasonal in student behavior sits on top of it. The engineering claim I'll defend is the latency; the business claim I won't assert without the experiment."
*Signal:* Refuses to bolt an unearned business outcome onto a technical win. This is the exact restraint that makes the technical number believable.

### If the number does not survive

Two versions, depending on which is true.

**If he measured it badly:**

> "I want to be straight about that one. The 40% came from a before-and-after window comparison, and I can't reconstruct the methodology cleanly enough to defend the exact figure — I don't know that the traffic mix was comparable across the two windows, and our cache was warm on one side and cold on the other. What I can defend is the mechanism and the direction: prefix caching, retrieval funnel reduction, and routing each moved it, and I can tell you which mattered most and why. If I were doing it today I'd run it as an interleaved A/B on live traffic so mix and provider drift hit both arms, and report p50 and p95 separately with the sample size."

**If he never measured it at all** — say this instead, and do not try to bridge to the first script:

> "Honestly, that number is softer than the resume makes it look, and I'd rather correct it here than have you find it. I don't have an instrumented before-and-after I can stand behind. What's true is that I shipped prefix caching, funnel reduction, routing, I understand why each one moves latency and which half of the budget each one touches, and the system was faster afterwards in a way users and the team noticed. I should have written the resume line as the work, not as a percentage — and I'm going to change it. What I'd want to show you instead is how I'd measure it properly, because that's the part that transfers."

**Where he *can* speak with total confidence — use this as the anchor:** the personal Indic voice agent on Pipecat, with Sarvam STT/TTS and a sub-800 ms end-to-end budget. That project is his, it's recent, and latency is its entire design constraint: the budget has to be split across STT, LLM TTFT, and TTS first-audio; TTFT dominates perceived responsiveness; streaming and barge-in are functional requirements, not polish. If the KNS number wobbles, pivoting to "here's a system where I actually owned a latency budget end to end, and here's how I split it" recovers the entire conversation — and it's true.

**Resume line — before:**
> Cut average LLM latency by about 40%

**Resume line — after:**
> Cut p95 response latency on the RAG assistant via prompt-prefix caching, retrieval-funnel reduction (top-50 → cross-encoder rerank → top-5), and small-model routing; measured end-to-end against a fixed query set

If he *can* defend a scoped number: `Cut p95 latency ~39% on the doc-QA path, measured end-to-end over 6 weeks (~850,000 requests) in per-stage application logs aggregated into Postgres`.
If the measurement is soft, drop the number entirely and keep the mechanisms. A mechanism list with no number invites a good conversation; a number he can't defend ends one.

### The numbers/vocabulary he must have cold for this claim

- **Per LLM call: `Total = TTFT + (N_out − 1) × ITL`.** Write it on a whiteboard without pausing.
- **End-to-end for a RAG pipeline is a *sum*, not one call:** `retrieval + rerank + LLM call(s) + guardrail + serialization`. Saying "total latency" while quoting a single-call formula is the tell that he's reciting. His own system has at least three network hops before a token is generated.
- **TTFT / prefill:** compute-bound, scales with input tokens. **Decode / ITL (a.k.a. TPOT):** memory-bandwidth-bound — each token streams weights + KV cache from HBM.
- **Batching:** continuous batching raises *throughput*; it does not reduce single-request latency and under contention it can raise per-request ITL. Say it that way, not "it doesn't affect latency."
- **KV cache** is inside the serving engine (reuse of attention keys/values across decode steps). **Prompt-prefix cache** is the provider-side skip-prefill feature — implemented on top of KV-cache reuse, which is why the names collide. He can explain the relationship; he must not claim to have operated the former on a hosted API.
- **Prefix caching cuts prefill only, never decode.** And it covers only the stable head — retrieved chunks after the breakpoint are re-prefilled every request.
- **Streaming changes perceived latency (TTFT-to-user), not total.** Say this before being asked. (Exception worth knowing: in a voice pipeline, time-to-first-audio *is* the SLO, so there streaming changes the number that matters.)
- **Reranker latency is a floor,** and it's workload-dependent: low hundreds of milliseconds is a reasonable order of magnitude for a hosted cross-encoder over ~50 documents, but it scales with document length and batch size and adds a network hop. Quote his measured number, not a blog-post number.
- **Cascade escalation double-pays:** blended latency/cost = `h × small + (1−h) × (small + large)`.
- **Percentiles have sampling error.** Only ~5% of observations define a p95; below roughly a thousand samples per arm the interval is wide. Know this before quoting a p99.
- **Retries are a tail mechanism.** SDK defaults retry 429/5xx with backoff; log attempt counts or your tail measures your rate-limit headroom.
- **Serving-side levers he doesn't own on a hosted API:** continuous batching, speculative decoding, tensor/pipeline parallelism, quantization. Naming them and disclaiming them is a strength.
- **The confounders, by name:** percentile substitution (p50 dressed as "average"), cache warm-up, provider-side model updates behind a stable alias, traffic-mix shift, region/network constant, retries, and concurrent work by other people.

### Things that will get him caught on this claim

- Saying "average" and then defending it as p95 when pressed. Pick one before the interview.
- Quoting per-mechanism milliseconds he derived from nothing.
- Saying "decode dominated" as a memorized fact instead of computing it from his own token shape — because in a long-context / short-answer RAG regime, prefill can dominate, and that's a common enough shape that a good interviewer will probe it.
- Claiming a KV-cache optimization on a hosted API.
- Letting "40% faster" and "30% cheaper" both be attributed to model routing without acknowledging it.

---

## The attribution-overlap trap (read before either claim)

Both resume lines credit overlapping work. An interviewer who reads them together will ask some version of: **"Is this one project counted twice?"** There is exactly one good answer, and it must be volunteered rather than extracted:

> "They overlap, and I should say so up front. Model routing and context trimming moved both numbers, because a smaller model on fewer tokens is both faster and cheaper — that's one piece of work with two effects, not two pieces of work. What's genuinely separate is prefix caching, which actually moved the latency number proportionally *more* than the cost number — 41% of the p95 win versus 33% of the cost win — because it only skips prefill, and prefill was the smaller half of my wall clock (about 22% of the LLM call), so a discount on the whole cacheable prefix shows up bigger against a smaller latency slice than against total spend. And semantic caching, which was almost entirely a cost lever — it skips the model call outright on repeated questions, but it barely moved p95 because it only fired on about 18% of traffic and most of the tail lived elsewhere. If you want the cleanest framing: one project, two metrics, and the mechanisms are weighted differently against each."

*Signal:* This is the answer that converts a trap into a credibility gain. Candidates who try to present them as two independent achievements lose both.

---

## Claim 2 — "Cut inference cost by about 30% through prompt and context optimization and caching, with production accuracy tracked continuously"

**Why this one is dangerous:** The arithmetic doesn't close on its own — an interviewer who has run prompt caching knows the discount alone can't produce 30% unless the cached fraction of the prompt is enormous, so they'll ask where the rest came from. And the clause "with production accuracy tracked continuously" is a claim he *volunteered*, which makes it fair game: every cost reduction is a quality risk, and he's asserted he controlled for it. If he can't describe the harness in detail, that clause converts from an asset into evidence he writes resume lines he can't back.

### The honesty gate for this claim

| Did he actually… | If yes | If no |
|---|---|---|
| Read `cache_read_input_tokens` (or the provider's equivalent) off responses? | Say so — it's the single most checkable claim in the whole answer. | Do **not** say "I verified it with the telemetry field." Say "I'd verify it with that field; at the time I inferred it from the bill, which is weaker." |
| Compute cost per request/unit rather than reading the monthly invoice? | Lead with the denominator. | Say plainly that he was looking at spend, and that spend moves with traffic. That admission costs less than being caught. |
| Have an eval harness gating merges, versus a dashboard he looked at? | Describe the gate. | Say "it was a dashboard, not a gate" — those are different things and the interviewer will know. |
| Have a production quality signal (escalation / thumbs-down / retry / flag)? | Name it and its rate. | Say which signal he *would* use and why he didn't have one. |

### The opening question

> "Break the 30% down. Caching gives you a discount on cached input tokens — that can't be 30% of your bill on its own."

**❌ What most candidates say** (and why it loses):

> "We turned on prompt caching and shortened our prompts, and our monthly API bill dropped about 30%. We were watching accuracy the whole time and didn't see any issues."

Two tells: "API bill dropped" is a number that moves with traffic volume, seasonality, and provider pricing changes, none of which are his work — and "didn't see any issues" is the absence of a measurement, not a measurement. An interviewer hears "we shipped a quality regression and nobody noticed."

**✅ Model answer — 25 seconds** (recruiter screen or passing mention):

> "It's cost per resolved query, not the bill — the bill moves with traffic. The caching discount was a minority of it; the biggest single piece was actually a semantic cache serving near-duplicate questions straight back at an ~18% hit rate. Prompt-shape fixes and model routing made up the rest. Every change was gated on an eval harness, because output tokens are where the money is and cutting the wrong thing is where quality dies."

**✅ Model answer — 2 minutes** (deep dive):

> "First, the denominator: it's cost per resolved query over the same 6-week window, about 850,000 requests, not the monthly bill — the bill tracks traffic, so on its own it isn't evidence of anything I did.
>
> The arithmetic has to close, and the caching discount alone doesn't close it. On Anthropic, cache reads are roughly a tenth of the base input price and cache writes carry a premium — around 1.25× on the short TTL. So a single subsequent read already pays the write back: 1.25 plus 0.1 is 1.35 against 2.0 uncached. On the longer TTL the write is around 2× and you need about two reads: 2 plus 0.2 against 3.0. That's derivable live, and I'd rather derive it than quote it.
>
> But even at a perfect hit rate, that only discounts the *cached input tokens*. Output tokens are priced 5× input on Anthropic, so on our shape — roughly 2,000 input, 450 output tokens — output was the majority of the per-call cost, around 53%, and no amount of input caching touches it.
>
> So the real split of the $0.0063 per query we saved — baseline was $0.0210/query, after was $0.0147/query — was: prompt-prefix caching, about 33% ($0.0021) — restructuring so the frozen system prompt and tool definitions come first and the retrieved chunks, timestamp, and user question come last, which took our cache-read fraction from about 20% to about 90%. I verified that with `cache_read_input_tokens` on every response, not by assuming. Semantic caching, about 40% ($0.0025) — a near-duplicate-query cache that serves repeated questions straight back without a model call, at roughly an 18% hit rate on our traffic. Context trimming didn't get its own line item — its cost effect is already inside the routing number, because the same top-5 funnel feeds every model regardless of which one answers. And model routing, about 27% ($0.0017), on the slice the small model could handle.
>
> The single biggest silent killer was invalidation: we had a timestamp in the system prompt, which meant the prefix changed byte-for-byte every request and nothing cached at all. Fixing that was most of the prompt-shape win.
>
> On quality — and this is the part I'd want you to push on — I'd actually been manually re-running our 220-question eval set, the same one built for the relevance-lift benchmark, before and after every one of these changes from day one. What I didn't have until about three weeks in was an automated CI gate — before that, a bad merge could still have slipped through even though I was checking by hand. Once it was wired in, every prompt, model, or retrieval change ran the suite automatically: retrieval recall@k, groundedness, citation accuracy, and abstention rate. I'd ship only if faithfulness didn't drop more than 2 points, measured as a paired comparison on the same items. And the number I actually trusted most was the production one: the escalation rate, because that's the metric that catches a regression the judge misses."

**Why this works:**
- Fixes the denominator before touching the number — cost-per-unit vs bill is the distinction that separates people who've owned a budget from people who've looked at one.
- Makes the arithmetic close out loud, **with the break-even correct**, so the interviewer's skepticism is answered before it's voiced.
- Puts output tokens at the center, which is where the money actually is and where most candidates never look.
- Names a specific, checkable telemetry field rather than making a claim.
- Volunteers the gap between manual checking and an automated gate *before* being caught, which buys credibility for everything else.
- Says "paired comparison on the same items" — a one-word signal that he knows a gate threshold has to clear the noise floor.

### The follow-up chain — they will not stop at one question

**Q: "Did quality regress, and how do you know?"** ← *the one that decides the interview*
**A:** "Here's the honest sequence. I was manually re-running the 220-question golden set — same one behind the relevance-lift number — before and after every cost change from the start, so nothing shipped fully unchecked. What landed later, about three weeks in, was wiring that same set into CI as an automated blocking gate; before that, the first change I shipped was manually verified but not gated, meaning nothing would have automatically stopped a bad one. After that, every change ran the suite in CI. The set is scored on retrieval recall@k, groundedness — is every claim supported by a retrieved span — citation accuracy, and abstention rate, with an LLM judge on a rubric. I don't take the judge on faith: I calibrated it against 150 human-labeled examples — the same calibration set used for the relevance-lift claim — and reported Cohen's kappa of 0.71 against a second human rater as the agreement number. The gate was no more than 2 points of faithfulness drop on a paired comparison. The one that caught a real regression was context trimming — cutting top-k too aggressively dropped recall, groundedness fell, and I reverted it. And the metric I trusted most wasn't in the harness: escalation rate in production, because a judge can be wrong in a correlated way and a human signal can't."
*Signal:* This is the whole answer. It shows he knows an eval harness is a gate and not a dashboard, that LLM judges need calibration, that offline metrics need a production ground-truth partner, and that he'll disclose a coverage gap rather than paper over it.

**Q: "Your golden set is 220 items and your gate is 2 points. Isn't that inside the noise?"** ← *new; the sharpest attack on the eval clause and almost nobody prepares for it*
**A:** "It can be, and it depends on how you compare. If you score two runs independently and diff the proportions, at 220 items and around 90% pass rate the standard error on a single proportion is roughly two points, so a difference of two independent proportions has a standard error near three — a three-point gate would be indistinguishable from noise, and our 2-point gate would be worse than that if I'd scored the two runs independently. The fix is not a bigger set first, it's a **paired** comparison: same items, same order, and you only count the items where the two runs disagree. That kills most of the variance because item difficulty cancels. We ran it paired — that's the only way a 2-point gate means anything at this sample size. If I needed to detect a smaller effect than the paired test can resolve, then yes — size the set to the effect, and be explicit that below that effect size we're shipping on judgment, not on the gate."
*Signal:* Understands that a threshold without a variance estimate is theatre. This single answer will out-perform most senior candidates.

**Q: "Tell me about the golden set. Who labeled it, and how do you keep it from going stale?"** ← *new*
**A:** "220 queries sampled from real production traffic, stratified across query types and deliberately including the failure modes we'd already seen. Labels came from two instructional designers on the content team, working from the authoritative source passage, so the label is 'which span should ground this answer' rather than 'here is the perfect prose.' That framing matters: labeling the *supporting span* is far more reproducible than labeling a gold answer, and it's what groundedness actually scores against. Staleness is the real weakness — the corpus changed, so the set decays. We didn't re-sample it on a schedule, and that's a real gap — the set was built once for the relevance-lift benchmark and I leaned on it for cost gating too, which saves effort but means it slowly goes stale as the corpus changes. I'd also keep a held-out slice so the prompts don't slowly overfit to the set."
*Signal:* Knows that "golden set" is a claim about labeling process, not a noun, and that overfitting to your own eval is a real failure mode.

**Q: "Where did the 30% actually come from? Rank the mechanisms."**
**A:** "Prompt-prefix caching, about 33% — and most of that was fixing invalidation, not adding cache headers. Semantic caching, about 40% — the single largest contributor, because a meaningful slice of student questions repeat near-verbatim within a unit, so roughly 18% of traffic never touched a model at all. Context trimming didn't get its own line — its savings show up inside the routing number, since the same top-5 funnel feeds every model. Model routing, about 27%. If I had to keep one, it's semantic caching: an 18% hit rate means 18% of queries cost effectively zero, and that beats shaving tokens off the other 82%."
*Signal:* Ranks by leverage and names the mechanism that actually dominates, rather than defaulting to the most commonly-cited lever.

**Q: "How did you attribute cost per request in the first place? Where did that number come from?"** ← *new*
**A:** "Per-call token accounting, not the invoice. Every response carries a usage object — input tokens, output tokens, cache-creation tokens, cache-read tokens — and I logged those per request with a feature tag and a tenant tag, then priced them in SQL. That gives you cost per request, cost per feature, and cost per tenant, and it reconciles against the invoice as a sanity check rather than being derived from it. We had this — it's what made 'cost per resolved query' a real number instead of a guess. Without that logging, 'cost per request' is just the bill divided by traffic, which hides every mix shift."
*Signal:* The difference between someone who reduced cost and someone who could *prove* they reduced cost. Also sets up per-tenant unit economics, which is a product-thinking signal.

**Q: "How much of that 30% is just the provider cutting prices, or you moving to a cheaper model?"** ← *new; the single hardest question on any cost claim*
**A:** "That's the challenge I'd expect, and I can't fully rule it out for a cross-window comparison. Per-token prices moved downward over that period industry-wide, and providers ship model updates behind the same alias. Two things separate my work from the drift: first, the prompt-shape change is verifiable independent of price — the cache-read fraction went from about 20% to about 90% and I can show you that field, and it's a ratio, not a currency amount. Second, output tokens per response fell from about 490 to about 450 once I capped max output length, which is also price-independent. If you want the cost number stripped of price drift, the right way to report it is **tokens per resolved query**, holding the price list fixed — that's the number I'd put on a resume if I were writing it today."
*Signal:* Proposes a price-invariant metric unprompted. This converts the hardest attack into the best answer in the interview.

**Q: "Does that 30% include your vector database, embeddings, and reranker — or just the LLM?"** ← *new; his resume says Pinecone, so this is fair game*
**A:** "Just the model calls, and I should be explicit about that rather than let 'inference cost' imply total AI spend. The rest of the stack was Pinecone, which was a largely fixed monthly cost that didn't scale with my per-request optimizations, embedding cost, which is dominated by re-indexing the corpus rather than by query-time embedding, and the reranker, which is per-call and actually went *up* as a consequence of the funnel change. So total AI spend fell by less than 30%, and if I'd trimmed the funnel enough to shrink the index I'd have moved the fixed cost too. The honest sentence is 'model-call cost per request,' not 'inference cost.'"
*Signal:* Distinguishes marginal from fixed cost, and volunteers that one of his own mechanisms *increased* a cost line. Nothing buys credibility faster.

**Q: "What about reasoning tokens? Did any of this involve a thinking model?"** ← *new; the 2026 question the old version of this doc had no answer for*
**A:** "That's a big one and it's the fastest way to blow up a cost model. On reasoning models, the thinking tokens bill at the **output** rate and they're usually not visible in the response text by default — so you can swap models with an identical prompt and see cost jump several-fold with nothing in your prompt to explain it. And caching doesn't help at all: it discounts input, and thinking is output. We weren't on a reasoning model for this system — the RAG assistant used a standard chat model on both the large and small side of the router. If we had been, the lever there would be the effort/depth setting — turning it down on the routine slice is a direct cost cut, and it's exactly the kind of change that would need to be eval-gated because it trades intelligence for spend. Since we weren't, this wasn't a lever I had. The general rule I'd apply now: measure `output_tokens` including reasoning, not the visible response length, or your per-request cost model is fiction."
*Signal:* Current on how 2026-era model billing actually works. Most candidates will still be describing 2023 pricing shapes.

**Q: "What was your semantic cache hit rate, and how do you avoid serving a wrong cached answer?"**
**A:** "Our hit rate was about 18% on the doc-QA path. I'd resist quoting that as a general number — hit rate is workload-shaped, not a tuning knob. A support or FAQ workload with a fat head of repeated questions can hit meaningfully higher; open-ended queries over a large corpus hit single digits and you've added a vector lookup for nothing. I'd measure the repeat rate on the query distribution before promising anything. On correctness: a semantic cache fails differently from a prefix cache — a prefix cache is an exact match so it can't be wrong, but a semantic cache can serve a confidently wrong answer to a query that's merely *similar*. The controls are a conservative similarity threshold tuned on labeled near-miss pairs, a TTL so the corpus changing invalidates answers, and namespacing by tenant so one org can never read another's cache. In a compliance-oriented RAG project I built separately, tenant isolation was a SQL predicate, not a prompt instruction — I applied the same rule to the cache key here."
*Signal:* Treats a cache as a correctness surface, not a cost surface; refuses to quote a hit rate as a universal fact; the tenant-isolation instinct is a genuine security signal.

**Q: "Your cache TTL is minutes. What happens on a low-traffic tenant?"** ← *new; specific enough to be a strong differentiator*
**A:** "You re-pay the write. The short TTL means the entry expires between requests, so a tenant sending one query every ten minutes pays the 1.25× write premium nearly every time and reads almost never — caching is net-negative for them at that traffic level. Three things follow. One: the same optimization has different economics per tenant, so a blended cost-per-request average hides it. Two: the longer TTL trades a higher write premium for surviving the gaps, and whether that's worth it is an arithmetic question per traffic pattern. Three: concurrent requests are a trap — several identical requests fired in parallel before the first write completes each pay the write, so a fan-out pattern should send one, wait for it to start returning, then send the rest. I'd check for it — I didn't specifically instrument concurrent-write collisions at the time, so I can't say for certain how often it happened, but the school-hours burst pattern is exactly the shape where it would."
*Signal:* Has thought about caching as a distributed-systems behaviour rather than a config flag.

**Q: "What's your cost per resolved task, not cost per call? And what counts as resolved?"**
**A:** "That's the framing I'd defend, and 'resolved' is where it gets real. Cost per call is easy to game — route everything to the cheap model and it drops. But if the cheap model's answer fails the groundedness check and you escalate, that query cost small *plus* large, and if it reaches a human it cost far more than either. So the real metric is total spend divided by queries resolved without escalation. I define resolved as the user didn't retry the same question within 5 minutes, didn't thumbs-down, and it wasn't escalated — that's a proxy, and I'd say so; the ideal definition needs a ground-truth signal most products don't have. On our workload, cost per call fell about 30% while cost per resolved query fell about 26% — the gap was the escalation rate, around 10%. If I only had one number to report, it's that second one."
*Signal:* The strongest available demonstration of business-level thinking about LLM economics, plus the discipline to flag that "resolved" is an operational definition rather than a fact.

**Q: "What's the number today?"**
**A:** "I can't tell you, and I'd distrust anyone who claimed they could. I measured it over a specific 6-week window and don't have production access anymore to re-pull it. And even if nothing on our side changed, the number drifts: the provider ships model updates behind the same alias, per-token prices move, and our traffic mix was seasonal — in EdTech, exam season shifts the query distribution enough to move cost per call on its own. The durable part isn't the percentage, it's that the shape is now cache-friendly and gated on evals, so it doesn't silently regress."
*Signal:* Refuses to invent a number under pressure, and turns the refusal into a statement about metric drift.

**Q: "What would you do next for another 30%?"**
**A:** "In order: batch the non-interactive work — nightly tagging and re-embedding don't need real-time pricing, and batch endpoints are commonly around half price; the tradeoff is an asynchronous SLA measured in hours, so it's only for work with no user waiting. Push the routing threshold harder now that the eval harness can tell me when it costs quality — before the harness existed I couldn't safely tune it. A wider semantic cache with the threshold tuned against labeled near-misses, since 18% is likely not the ceiling. Cap or tune reasoning depth on the routine slice if we're ever on a thinking model. And re-examine whether the retrieval funnel is over-fetching — every chunk that doesn't earn its place in the answer is input tokens plus rerank compute for nothing. I'd sequence them by cost-per-unit-of-risk, and each one ships behind the eval gate."
*Signal:* Has levers he hasn't spent, sequences by risk, knows the batch-endpoint tradeoff rather than just the discount, and explicitly ties the ability to tune aggressively back to having built the eval harness.

### If the number does not survive

> "I'd rather scope that one down than defend it as written. The 30% came from comparing spend across two windows, and I can't rule out that traffic mix and the provider's pricing or model changes moved it as much as I did. What I'll stand behind: I found and fixed the reason our prefix cache was never hitting — a timestamp in the system prompt was invalidating the prefix on every request — and that's verifiable as a *ratio* rather than a currency amount, so price drift can't explain it. I restructured the prompt so the stable head is first and the volatile content last, I capped output length, and I trimmed the retrieval funnel. Every one of those was checked against the same 220-question golden set before and after, though the automated CI gate only landed about three weeks in. The direction is solid; the exact percentage isn't something I can reconstruct honestly, and the clean way to get it is an interleaved A/B measured as tokens — and cost — per resolved query."

**And if the eval clause is the part that doesn't survive**, say this rather than defending it:

> "The 'accuracy tracked continuously' line overstates what we had. It was a set of checks I ran manually before releases, not a gate that blocked a merge. Those are different things and I shouldn't have written it the way a gate reads. What I can tell you is exactly what I'd build, why each metric is in it, and which of my cost changes was the one that would have needed it most."

### Resume lines

**Before:**
> Cut inference cost by about 30% through prompt and context optimization and caching, with production accuracy tracked continuously

**After:**
> Cut model-call cost per resolved query via prompt-prefix caching (fixed cache-invalidating prompt structure, verified with cache-hit telemetry), output-length control, and context trimming — each change gated on an eval harness (golden set, groundedness + citation accuracy) so cost reductions couldn't ship a silent quality regression

Note two deliberate edits: **"model-call cost"** rather than "inference cost" (so the Pinecone/embedding/rerank question isn't a gotcha), and **"gated on an eval harness"** rather than "tracked continuously" (a gate is a stronger and more specific claim, and it's the one he can describe).

If he wants a number and can defend a price-invariant one: `Cut output tokens per resolved query ~8% and model-call cost per query ~30% on the doc-QA path`.

### The numbers/vocabulary he must have cold for this claim

- **`cost/call = in_tok × p_in + out_tok × p_out`.** On Anthropic's current line the ratio is **exactly 5×** ($5/$25, $3/$15, $1/$5 per million); across providers 3–5× is the usual range. Quote **his** provider's actual numbers, and know that the consequence — a few hundred output tokens can outweigh a few thousand input tokens — is the sentence that reframes the whole conversation.
- **Cache read ≈ 0.1× base input price** on Anthropic; other providers commonly discount cached input less (roughly a quarter). Quote his provider. **Cache write ≈ 1.25× (short TTL) / 2× (1-hour TTL).**
- **Break-even, derived live — and get this right, the old version of this note had it wrong:**
  - Short TTL: `1.25 + 0.1 = 1.35 < 2.0` → **one read after the write already pays it back** (two total requests).
  - Long TTL: `2.0 + 0.2 = 2.2 < 3.0` → **two reads** (three total requests).
  - Saying "you need two hits to break even" on the short TTL is wrong and an interviewer who has run this will notice.
- **Prefix caching matches on the rendered prompt prefix.** Render order is tools → system → messages. **Minimum cacheable prefix is model-dependent and *not* monotonic across generations** — on current Anthropic models it ranges from **512 to 4096 tokens** depending on the model, and below it nothing caches with no error raised. Do not quote a single number as if it were universal; the correct answer is "it depends on the model, check the current table, and verify with the telemetry field."
- **Invalidation is tiered, not all-or-nothing** — this is the precise version of "any change invalidates everything":
  - Changing **tool definitions or the model** invalidates everything.
  - Changing the **system prompt** preserves the tools cache but invalidates system + messages.
  - Changing `tool_choice`, toggling thinking, or changing **message content** preserves tools + system.
  - Being able to state this hierarchy is a much stronger signal than the blanket claim.
- **The silent invalidator list:** `datetime.now()` in the system prompt, UUIDs/request IDs early in the prefix, unsorted JSON serialization, per-user IDs in the system prompt, a tool set that varies by user, switching models mid-conversation (caches are model-scoped), conditional system-prompt sections.
- **The verification field: `cache_read_input_tokens`** (and `cache_creation_input_tokens`). Zero across repeated identical-prefix requests means an invalidator is live. **Total prompt = `input_tokens + cache_creation_input_tokens + cache_read_input_tokens`** — so a small `input_tokens` doesn't mean a small prompt.
- **Breakpoints are limited** (a handful per request), so placement matters: put the marker at the end of the *shared* prefix, not the end of the whole prompt — otherwise every request writes a distinct entry and nothing is ever read.
- **TTL behaviour:** short-TTL entries expire in minutes, so low-traffic paths re-pay the write. Concurrent identical requests fired before the first write lands each pay a write.
- **Reasoning/thinking tokens bill at the output rate**, are frequently not surfaced in the response text, count against the output cap, and are **not** helped by input caching. On models with an effort/depth control, that control is a first-class cost lever — and one that must be eval-gated.
- **Cascade blended cost:** `h × c_small + (1−h) × (c_small + c_large)` — escalated queries pay twice.
- **Semantic cache saving:** `hit_rate × cost_per_call − embedding_cost`; hit rate is workload-determined, not a tuning knob.
- **Cost per resolved task = total spend / tasks resolved without escalation.** The metric that can't be gamed by routing — and "resolved" needs an operational definition he can state.
- **Tokens per resolved query** — the price-invariant version, immune to provider price cuts. This is the number to reach for when accused of riding a price drop.
- **Batch endpoints ≈ 50% of standard price**, with an asynchronous SLA (hours, up to a day) and out-of-order results — non-interactive work only (tagging, re-embedding, backfills).
- **Fixed vs marginal:** vector DB spend, index storage, and re-embedding are largely fixed or corpus-driven; per-request prompt optimization doesn't touch them. "Inference cost" ≠ "AI spend."
- **Eval vocabulary:** golden set (with a labeling process, not just a size), recall@k, groundedness/faithfulness (claim → supporting-span), citation accuracy, abstention rate, LLM-as-judge with human calibration and reported agreement, **paired** comparison and effect size vs noise floor, CI gate with a drop threshold, held-out slice to prevent overfitting the set, online sampled eval, production ground-truth signal (escalation / thumbs-down / retry / flag rate).

### Things that will get him caught on this claim

- Saying "you need two hits to break even" on a 1.25× write. It's one.
- Quoting a single minimum-cacheable-prefix number as universal. It's model-dependent and spans an 8× range.
- Saying output is "3–5×" input while naming a provider where it's flatly 5×.
- Claiming he verified cache hits with a telemetry field he never read.
- Describing a dashboard as a gate.
- Setting an eval gate threshold with no notion of the noise floor.
- Saying "inference cost" while a fixed Pinecone bill sits unmentioned on the same resume.
- Presenting the 30% and the 40% as two independent achievements.
