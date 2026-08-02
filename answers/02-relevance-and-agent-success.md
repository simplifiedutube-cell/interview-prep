# Claims 3 & 5 — Answer relevance +35% and Agent task success +20%

> **Model answers — read this first.**
>
> These are *scripts for things you actually did*. Every fact only you can know appears as a `[BRACKETED SLOT]`. **Never walk into an interview with a bracket unfilled** — an unfilled bracket spoken aloud sounds exactly like a lie.
>
> If a sentence in a model answer isn't true of your work, **don't say it** — use the honest variant printed alongside it. A rehearsed false claim about methodology is the worst outcome available in these interviews, worse than losing the number, because it's a trust finding rather than a skills gap.
>
> Fill your real facts into `../metric-defence.md` first. This file shows you the *shape*, *depth* and *honesty calibration* of a strong answer — not the data.

---

# Interview Defence Pack — v2 (hardened)

> **How to use the truth gates.** Every ✅ answer below is a *script for something he actually did*. If a sentence in it isn't true of his work, he does not say it — he says the honest variant printed underneath. A rehearsed false claim about methodology is the single worst outcome available in these interviews, worse than losing the number, because it is discoverable in one follow-up and it retroactively poisons everything else on the resume.

---

> ⚠️ **ILLUSTRATIVE NUMBERS, NOT YOUR DATA.** Every figure below (latencies, percentages, dates, counts, dashboards, tool names) is ONE internally-consistent fictional-but-plausible example, built so you can see what a *complete* answer sounds like with no missing pieces. **None of it is verified fact about your actual systems or your life.** Before you say any of this in an interview, replace every number with your real one — and where your real answer is "I don't know" or "I never measured that," use the honest fallback script the document already gives you for that case, don't just leave this illustrative number in. The biographical details in this file (disclosure stories, dates, reasons for gaps) are ESPECIALLY placeholder — they are not a suggestion of what actually happened to you. Use your own true story there, always.

---

## Claim 3 — "Answer relevance improved by around 35% in student-facing responses"

**Why this one is dangerous:** "Relevance" is not a metric, it's a category of metrics, and the interviewer knows there are at least five incompatible ways to produce that number — human rating, LLM judge, thumbs-up rate, task completion, retrieval hit rate — with wildly different credibility. "Around 35%" is also ambiguous between relative and absolute, which means the same sentence covers a 0.60→0.81 move and a 0.60→0.95 move. Because this is RAG in 2023–2026, the single most likely origin of a clean +35% is an eval set generated *from the same chunks that were indexed*, which makes the number an artifact of the harness. And the second most likely origin — the one this document previously missed — is that **the eval set, the rubric, or the judge model changed between the "before" and the "after" measurement**, in which case there is no before/after at all, just two unrelated numbers subtracted from each other.

### The opening question

> "Relevance according to what? Walk me through exactly how a single answer got scored."

**❌ What most candidates say** (and why it loses):

> "We had an eval dashboard with a relevance score, and after we improved the retrieval and the prompts it went up about 35%. We used GPT-4 as a judge on a 1–5 scale and the average went from like 3.1 to 4.2."

Three tells, not one. **(1)** The 1–5 scale with no mention of who validated the judge — a Likert average from an unvalidated judge is a number with no unit, and the candidate has just revealed he never asked whether the judge agrees with a human. **(2)** "We improved the retrieval and the prompts" — two changes, one number, no attribution, volunteered without noticing it's a problem. **(3)** 3.1 → 4.2 is a 35% *relative* move on a 1–5 scale, which is a scale with an arbitrary zero — percentage change on an interval scale with no true zero is not a meaningful quantity at all. If he says "3.1 to 4.2, that's 35%," a statistically literate interviewer stops listening.

**✅ Model answer — 25 seconds** (recruiter screen / passing mention):

> "The unit is a question and the score is binary — did the answer address what the student asked, grounded in the retrieved material, yes or no. Frozen set of 220 questions, scored by an LLM judge validated against human labels, 58% passing before, 78% after — 20 points absolute, about 35% relative. Retrieval and generation were scored separately, so I can tell you which half moved."

*Recruiter screens don't want caveats — they want a crisp, non-evasive sentence. Save the confounder for the technical round.* If the interviewer is technical, or if they lean in, add exactly **one** sentence:

> "One honest caveat I'd flag up front: the retrieval-funnel change — reranking the top-50 candidates down to a top-5 — and a prompt-template change shipped in the same two-week window, so I can't cleanly split the credit between retrieval and generation."

**Truth gate:** say "binary" only if the rubric was binary. Say "frozen set" only if the question set was fixed and unchanged across both measurements. If either is false, use:

> "Honestly — the harness I built was a Metabase dashboard tracking an LLM-judge score per answer, and the question set drifted in composition over time rather than staying strictly frozen. If I were describing what I'd stand behind rather than what the resume says, it's that I built the eval loop; the specific 35% came out of a rolling weekly sample of student queries scored before and after the retrieval and prompt changes, and I'd want to caveat it, which I'm happy to do in detail."

**✅ Model answer — 2 minutes** (deep dive):

> "So the unit is a question, and the score is binary — did this answer actually address what the student asked, grounded in the retrieved material, yes or no.
>
> I moved off a 1–5 scale, and the reason isn't that means don't have confidence intervals — they do. It's three other things. A '4' under judge-prompt v1 isn't the same object as a '4' under v2, so Likert deltas aren't comparable across prompt revisions, which is exactly when you want to compare them. Judges use maybe two of the five bins in practice, so the mean is dominated by movement you can't interpret. And a mean has no decision semantics — you can't gate a deploy on 3.7, but you can gate on 'the pass rate must not drop below 75%'. The cost of binary is that you lose *how* wrong an answer was, so I kept a failure-reason label next to the pass/fail: pass rate is the gate, the reason codes are the diagnosis.
>
> Two things were separate metrics, not one. Retrieval I measured as recall@5 and MRR against gold chunk IDs annotated by hand for each of the 220 eval questions. Generation I measured as faithfulness — fraction of atomic claims in the answer entailed by the retrieved context — plus answer relevancy and citation correctness. They fail differently. If retrieval recall@5 is 82%, your ceiling is 82%, and no prompt work gets you past it.
>
> Two ablations bound the whole thing, and I'd run them before trusting any delta. Blank the context entirely — if the pass rate barely moves, the model is answering from parametric memory and my retrieval stack isn't doing the work I think it is. Then feed gold context only — that's the generation ceiling. The real system sits between the floor and the ceiling, and the gap tells you which side to spend on.
>
> The thing I'd want to flag before you ask: our first eval set was generated by an LLM from the indexed chunks, and that set is contaminated. The question inherits the chunk's exact vocabulary, so retrieval becomes lexical matching and the numbers are inflated. We rebuilt it from real, anonymized student queries pulled from the logs, and added unanswerable questions so we could measure abstention. The 35% is measured on that rebuilt 220-question set, sourced from real student queries, not the original synthetic one — and if it had been the synthetic one, I'd treat it as directional, not as a number I'd put in front of a customer.
>
> Judge validation: I hand-labelled 150 answers and scored the judge against them as a classifier — TPR 0.89, TNR 0.84. If I hadn't done that, the honest version is: I never validated the judge against human labels, and that's the gap I'd close first. What I'd do is hand-label 150 answers, get TPR and TNR, and correct the reported rate.
>
> On significance and comparability — 220 questions, same questions through both versions. And the question I'd ask myself hardest is whether the *harness* was constant: same question set, same rubric text, same judge model snapshot. If the judge model rolled between the two measurements, there's no before/after, there's just two numbers. In our case the set stayed frozen and version-controlled across the term, the rubric text didn't change, and the judge was pinned to a single model snapshot throughout, so I stand behind this as a genuine before/after. The confounder I couldn't rule out is that the retrieval-funnel change and the prompt-template change shipped in the same two-week window; the clean experiment is holding retrieval fixed and only changing the prompt."

**Why this works:**
- Separates retrieval eval from generation eval — the clearest marker of someone who has run a RAG eval rather than read about one.
- The binary-over-Likert justification is now *correct*. The old version ("a proportion has a confidence interval where a mean rating does not") is false and a sharp interviewer kills it in one sentence.
- Names the cost of binary and how he mitigated it, so it reads as a trade-off he chose rather than a slogan he heard.
- The empty-context / oracle-context ablation pair is the fastest way to prove he understands what a RAG number is *made of*. Almost nobody volunteers it.
- Volunteers data leakage *before* being asked.
- Treats the judge as a classifier to be validated, and — critically — has an honest branch for "I never validated it," because that is the likeliest truth and a fabricated TPR is a career-ending detail.
- Raises harness constancy (set / rubric / judge snapshot) unprompted. This is the attack the previous draft had no answer for.

### Brackets, triaged

He is interviewing now, 8h/day, under 3 months of runway. Fill these in this order:

**Must fill before the next technical round (do it on the AML/CTF RAG this week — it is the fastest way to make every bracket in this document real):**
`220` question-set size · `58%` / `78%` before-after · both stated together (20 points absolute, ~35% relative) · the rebuilt real-student-query set the number came from · the retrieval-funnel-and-prompt-change-shipped-together confounder · `82%` recall@5 value · what the remaining failures look like.

**Fill if he can honestly reconstruct it:** `TPR 0.89 / TNR 0.84`, `Cohen's kappa 0.71`, `McNemar result (never formally run)`, `1 run per question`.

**Do NOT fabricate; the honest branch is scripted for each:** judge validation numbers, kappa, significance test results. These are the brackets most likely to be unfillable, and every one of them has an "I didn't, and here's what it would have meant" variant below that scores *higher* than a made-up number and costs nothing if he's caught being right.

### The follow-up chain — they will not stop at one question

**Q: "How did you measure relevance — was that a human, a model, or thumbs-up data?"**
**A:** "GPT-4o, pinned to the gpt-4o-2024-08-06 snapshot, with a binary prompt, on a frozen set of 220 questions. Thumbs data existed but I didn't use it as the metric — thumbs are maybe 8% coverage and they're biased toward extremes; people click thumbs-down when they're angry, not when the answer is merely mediocre. I used thumbs as a *drift alarm*, not as the score. Where the two disagreed, it was almost always the judge failing an answer a student had thumbs-upped anyway — usually correct-but-terse, not a case where the judge missed a real failure."
*Signal:* Knows implicit feedback is a selection-biased sample and won't launder it into a quality metric.

**Q: "Did the thumbs-down rate move too?"** ← *new; this is the obvious triangulation question and the old draft walked straight into it*
**A:** "It did, and in the same direction, which is the corroboration you want — thumbs-down rate on rated responses fell from about 9% to 6% over the same term. If it hadn't moved, that's the uncomfortable part and I'd rather say it than have you find it: a big offline move with a flat online signal means one of three things — the eval set doesn't look like real traffic, the improvement was concentrated on a slice students don't actually hit, or thumbs are too noisy at our volume to resolve it. In our case I'd have leaned toward the second explanation, since the retrieval-funnel change disproportionately helped multi-hop questions, which are a minority of real traffic. And if I'd never checked at all, that would be the first thing I'd go verify — an offline number with no online corroboration is a hypothesis, not a result."
*Signal:* Understands offline/online metric divergence is the normal state of affairs and doesn't panic about it.

**Q: "Who labelled it? Did you check they agreed with each other?"**
**A:** "150 items labelled by me and a second human rater — one of the instructional designers who wrote the reference answers. Cohen's kappa was 0.71 — for two raters on a binary label that's substantial on the Landis–Koch bands. Earlier in the project, before that formal pass, I hadn't computed kappa at all, which in hindsight I should have done from day one; what I did instead was dual-label a small sample and reconcile disagreements by tightening the rubric wording, which is the same instinct without the number. If I hadn't gotten to the formal version, I'd label 150 items with two raters, compute kappa, and treat anything under 0.6 as a signal that the rubric is ambiguous rather than that the raters are bad — a low kappa usually means the *definition* is broken, and if humans can't agree, no judge is going to be reliable either. One caveat I'd add on kappa itself: it's sensitive to prevalence, so if 90% of answers pass, you can have 95% raw agreement and a terrible kappa. I'd report raw agreement alongside it rather than either alone."
*Signal:* Admitting kappa was never measured, and explaining what a bad kappa would have *meant*, is stronger than quoting one. The prevalence caveat is the detail that shows he's actually thought about kappa rather than memorised the bands.

**Q: "How do you know your judge is any good?"**
**A:** "I scored it against human labels as a binary classifier — TPR 0.89 on the answers humans passed, TNR 0.84 on the ones humans failed. Those two matter separately: the net bias on the reported pass rate is roughly (1−TNR)×(fraction truly failing) minus (1−TPR)×(fraction truly passing), so it can go either way, and if you know both you can back out a corrected rate — that's Rogan–Gladen, (observed + TNR − 1)/(TPR + TNR − 1), and it only works if TPR + TNR > 1.
>
> There's a second-order point I'd make: if the judge's error rates are the same before and after, a lot of that bias *cancels in the delta*, which is one reason I'd defend a delta harder than a level. But it only cancels if the errors are stable — and after prompt work the answers usually get longer, which trips verbosity bias, so the assumption is exactly the one that breaks. That's an argument for length-controlling the comparison, not for ignoring it.
>
> I also checked the known failure modes: verbosity bias, position bias in pairwise setups, and self-preference, where a judge favours output from its own family. The mitigation I actually applied was reference-guided grading against the instructional-designer-written reference answer for each question, plus swapping which answer went first whenever I ran any pairwise spot-checks. The place I'd push harder now is that the judge and the generator were the same model family — GPT-4o, the same model we used for the harder ~40% of queries that weren't routed to the smaller model — so on that slice the judge is grading a close cousin of itself, which is exactly the self-preference risk I just named.
>
> [If never validated:] I didn't, and I'm not going to invent a number for you. The reference point I'd anchor on is the MT-Bench result — a strong judge matching human preference at over 80% agreement, about the same as human-to-human — but that's *pairwise preference on open chat*, and it is not a licence to assume an arbitrary rubric on RAG groundedness transfers. So the honest position is: unvalidated judge, direction probably right, magnitude unverified."
*Signal:* Judge validation as measurement, named bias mechanisms with mitigations, and — the strongest bit — the observation that judge bias partially cancels in a delta but that verbosity bias is precisely the one that doesn't. This is the question most candidates have literally no answer for.

**Q: "Where did your eval questions come from?"**
**A:** "The final 220 came from real, anonymized student queries pulled from the logs, stratified by topic and by whether the assistant had previously failed on that question. There's no synthetic-from-chunks component left in that set — that was the first version, and I killed it once I realized what it was measuring. The synthetic ones I still treat with suspicion in general, because if you generate a question from chunk 4,312 and then ask the retriever to find chunk 4,312, you've built a keyword-matching test, not a retrieval test — the question carries the chunk's vocabulary. Fixes I applied: generate from documents held out of the index, paraphrase questions away from source wording, include multi-hop questions that need two chunks, and include unanswerable questions so you can measure whether the system correctly refuses. That last bucket is the one everybody skips and it's where hallucination guardrails actually get tested."
*Signal:* The highest-leverage answer in the whole claim. Naming the leakage mechanism concretely, and naming abstention as a required slice, separates him from ~90% of RAG candidates.

**Q: "How did you get gold chunk IDs? Is there exactly one right chunk per question?"** ← *new; follows inevitably from claiming recall@k*
**A:** "Annotated by hand while writing each question, and pooled from the top-k of a couple of different retriever configurations where the right answer wasn't obvious. And no — usually several chunks are acceptable, so I treated it as a *set* of relevant IDs, which is why recall@k and MRR rather than a strict accuracy. The honest weakness in any hand-built gold set is that you only ever label what some retriever surfaced, so unretrieved-but-relevant chunks are invisible and recall is biased upward. Pooling across retrievers reduces that; it doesn't eliminate it. That exact leakage pattern — gold IDs being just the source chunks of synthetic questions — was what happened with the very first version of this eval before we rebuilt it, and I'd concede that plainly rather than defend it."
*Signal:* Knows that a gold set is itself a measurement with its own bias, and names pooling bias by mechanism.

**Q: "Faithfulness is 'fraction of claims entailed by the context' — who decomposes the answer into claims?"** ← *new; the recursive-judge trap*
**A:** "An LLM does, which means faithfulness is a two-stage pipeline where both stages are model calls — a decomposer and an entailment check — and errors compound. So it's a *cheaper, noisier* proxy than the binary human-anchored rubric, not a more rigorous one. I used it for regression detection across many questions where I couldn't afford human labels, and the binary rubric on the frozen set for anything I'd report. Where a claim is a matter of degree, decomposition is genuinely ambiguous and I'd expect low agreement even between humans."
*Signal:* Doesn't treat RAGAS-style metrics as ground truth. Knowing that "the judge validating the judge" is a real regress, and having a policy about which metric he'd *report*, is senior.

**Q: "Was the eval set the same before and after? Same rubric? Same judge model?"** ← *new; this is the single most likely way a before/after is fake, and the old draft had nothing*
**A:** "Yes, I checked. It's the first thing I'd check on someone else's number, so I'll answer it before you press. Set was frozen and version-controlled, rubric text unchanged, judge pinned to a specific model snapshot — the whole comparison is worthless otherwise, because a provider rolling a model alias underneath you moves the score with no system change at all. If I couldn't have guaranteed that — say, if the harness had changed underneath a measurement — I can't guarantee the harness was identical across both measurements, and if it wasn't, the delta isn't a delta. The way to recover it is to re-run the *old* system today against the current harness and get a genuinely paired number. If I'm asked to defend the 35% and I can't establish harness constancy, I'd rather withdraw the number."
*Signal:* Naming the fix — re-run the old version through today's harness — is the thing that distinguishes someone who has been burned by this from someone who has read about it.

**Q: "What was the baseline? Before *which* change?"** ← *new*
**A:** "The baseline is the system as it stood at the start of the 10-week term — naive top-k dense retrieval, no rerank, with the original single-shot prompt. The window is that same 10-week term, and the changes inside it were the retrieval-funnel/rerank change, a chunking fix, and a prompt-template revision. If the baseline is 'the first thing that worked' rather than a tuned system, I'd say so — improving on a weak baseline is a real improvement but it isn't the same claim, and I don't want you to hear the stronger one. In this case it's honestly closer to the weaker claim: we hadn't tuned that first system much before we started measuring it."
*Signal:* Distinguishing "beat a strong baseline" from "beat the first thing we shipped" unprompted is exactly the kind of precision that buys trust for the rest of the resume.

**Q: "Was that significant, or is it noise?"**
**A:** "Depends on the design, and I want to be precise because the two cases need different tests.
>
> Single run per question, paired — same 220 questions through both versions — then it's McNemar on the discordant pairs, χ² = (b−c)²/(b+c), and with few discordant pairs the exact binomial version instead. Not a two-sample z-test, because the pairing is the whole source of power.
>
> Multiple runs per question, McNemar doesn't apply — it needs one binary outcome per unit per condition. There the practical answer is a cluster bootstrap on the *paired difference in pass rate*, resampling questions, not runs; the rigorous answer is a mixed-effects logistic model with a random intercept per question, or GEE with cluster-robust standard errors.
>
> I didn't run the test at the time. With n = 220, the 95% interval on a single proportion is roughly ±6.5 points, and the paired interval is tighter than that. So a move of 20 points is comfortably outside it and a 5-point move would not have been — I'd have been wrong to report one. Worth being precise about the claim itself: 20 points on a 0.58 base is 0.78; a 35% relative move on that same 0.58 base works out to about 0.78 as well — in this particular case the absolute and relative framings nearly coincide, since 20 points off a 58% baseline is a 34.5% relative lift, call it 35%. That's a coincidence of this baseline, not a general fact — I've seen the same headline number describe very different systems depending where you start. The one I'm claiming is both, stated together, precisely so there's no ambiguity.
>
> The other half of significance with LLM evals is run-to-run variance — the judge isn't deterministic even at temperature 0, because inference kernels aren't batch-invariant and the batch composition depends on server load. So the right shape is k = 3–5 runs per question, and when you bootstrap you resample the *questions*, because question difficulty is where almost all the variance lives. Cluster bootstrap, roughly 1,000 resamples."
*Signal:* The right test for the right design — and the fact that he *notices* multi-run breaks McNemar is the tell. Plus an honest "I didn't run it, here's the interval that would have mattered," and the relative/absolute ambiguity closed in one breath.

**Q: "Did the improvement hold on the hard slice, or just on average?"** ← *new*
**A:** "Sliced by topic, by question type, and separately by answerable vs. unanswerable, since those need very different behavior — answer vs. abstain. The gain held across most topics; the one slice that lagged was multi-step, formula-heavy math questions, which only moved from about 51% to 60% while everything else moved into the high 70s or low 80s. The failure mode I'd be watching for is an aggregate gain that comes entirely from easy questions while the hard slice is flat or down — that's a real risk when you tune a prompt, and the aggregate hides it. Same reason I'd want the unanswerable slice broken out separately: a system that got better at answering and worse at refusing can look like a clean win in aggregate and be strictly worse in production."
*Signal:* Slice-level thinking, and the specific insight that abstention regressions hide inside relevance gains.

**Q: "What did the remaining failures look like?"** ← *new; the most natural question after any pass-rate claim, and it was missing*
**A:** "Reason-coded. Roughly: right chunk retrieved but the answer ignored it, wrong chunk retrieved, answer correct but uncited, answer hedged into uselessness, and refused-when-it-shouldn't-have. The distribution was roughly a third right-chunk-ignored, a third wrong-chunk-retrieved, and the rest split across uncited, over-hedged, and wrongly-refused, which is why the next thing I worked on was the cross-encoder reranker — wrong-chunk-retrieved was the single largest bucket. If I couldn't tell you the shape of the residual failures, that would tell you I'd been watching a dashboard rather than reading transcripts."
*Signal:* He has read the failures. Everything else in this document is claims about method; this is the one that proves contact with the actual output.

**Q: "What did it cost you — did latency or spend regress?"** ← *new*
**A:** "The cross-encoder rerank step added about 550 ms at p95 and roughly 3% to cost per query — reranking is compute, not tokens, so the cost hit was much smaller than the latency hit. I'd report a quality gain next to its latency and cost cost, because a relevance number with no denominator in latency is half an answer. That trade was accepted: 550 ms of p95 latency for a jump in retrieval recall@5 from the low 60s to 82% was an easy call, especially once prompt-prefix caching and model routing clawed most of that latency back elsewhere."
*Signal:* Quality is a trade, not a free variable. This also sets up Claim 5's four-axis framing, so the two claims corroborate each other.

**Q: "Did retrieval get better or did the writing get better?"**
**A:** "Both moved, but retrieval moved more. I could tell because they're instrumented separately — recall@5 moved from about 63% to 82%, and faithfulness moved from about 71% to 85%. If only the generation metric moves, you've made the model better at writing around bad context, which is exactly how you get confident, fluent, wrong answers. The changes were chunking, the cross-encoder rerank, and the prompt template, and the one that actually mattered most was the rerank step. They shipped close together, so I can't cleanly split all of the credit — the ablation that would settle it is holding retrieval fixed and changing only the prompt."
*Signal:* Understands that a generation-only improvement over unchanged retrieval is a hallucination risk, not a win.

**Q: "What is it today?"**
**A:** "I don't have current access to pull today's number — I left KNS in June 2026, so 'today' really means 'as of my last day.' As of when I left, the eval still ran nightly and gated any retrieval or prompt change before rollout, and the pass rate was holding at 78%, in line with the term-end number I've quoted. The set had grown slightly since — we'd added about 40 questions covering a new curriculum unit — so that later number isn't strictly comparable to the original baseline, and I wouldn't quote a delta across that set change."
*Signal:* Refusing to compare across a changed eval set is a small, very senior refusal.

### If the number does not survive

Use these words, roughly verbatim:

> "I want to be straight about this one. The direction was real — we cut the retrieval funnel down to a reranked top-5 and fixed a chunking bug that was splitting worked examples across chunk boundaries, both of which obviously helped. What I can't reconstruct for you now is which scoring definition the 35% came from, and 'relevance' means four different things depending on the harness. So I'd rather tell you what I built and let you judge that than defend a number whose denominator I can't name. What I'd stand behind completely is the eval harness itself — the frozen 220-question set, the binary rubric, and the retrieval/generation split."

Note the edit: **not** "a real, large improvement." "Large" is a magnitude claim, and asserting magnitude in the same breath as admitting you can't measure it is the exact move the whole document exists to prevent. Say "real," let the mechanism carry the size, and let *them* infer.

Then pivot to the AML/CTF RAG side project — hybrid dense + BM25 with RRF, cross-encoder rerank, tenant isolation as a SQL predicate rather than a prompt instruction. Trading an undefendable number for a fully-defendable system is a *credibility gain*.

> **Guard on the pivot — this is load-bearing.** The pivot only works if the side project has an eval he can open. Pivoting from "I can't defend my eval numbers" to a project with *no* eval numbers converts one soft answer into two, and the interviewer will notice. Before the next onsite: build a 40-question set on the AML/CTF corpus with unanswerable negatives, a binary rubric, recall@k against annotated chunk IDs, and hand-label 30 judge decisions to get real TPR/TNR. That is roughly two days of work and it retroactively fills the majority of the brackets in this entire document with numbers he owns end to end. If he does one piece of prep from this pack, it is this.

**Resume line — before:**
> Built RAG assistant over 10,000+ documents with hallucination guardrails and automated eval dashboards; improved answer relevance by ~35% in student-facing responses.

**Resume line — after (keeps a number he can defend):**
> Built RAG assistant over 10,000+ docs; owned the eval loop — frozen 220-question set, binary groundedness/relevance rubrics, retrieval and generation scored separately — raising relevance pass rate from 58% to 78% and gating every retrieval/prompt change on it.

**Resume line — after (tighter, one line):**
> Built RAG assistant over 10,000+ docs and the eval loop that gated it: frozen 220-question set, binary groundedness rubric, retrieval and generation scored separately; pass rate 58% → 78%.

**Resume line — after (no result number at all, if none survives):**
> Built RAG assistant over 10,000+ docs with hallucination guardrails; built the answer-quality eval loop that gated it — frozen question set with unanswerable negatives, separate retrieval (recall@k, MRR) and generation (faithfulness, citation correctness) metrics, regression gate in CI.

> **Truth gate on the resume line.** "LLM judge validated against human labels" was in the previous version of this bullet. It has been removed from the default. Put it back **only** after he has actually hand-labelled a sample and computed TPR/TNR — on the side project counts. A resume bullet claiming judge validation, followed by "I never got round to computing it," is a worse outcome than the bullet that never claimed it.

The capability version is *harder to attack* than the original, because a capability claim has no denominator to interrogate.

### The numbers/vocabulary he must have cold for this claim

- **Relative vs absolute** stated in one breath: 35% relative on a 0.60 base is 0.81; 35 points is 0.95. Know which. Also know that **percentage change on a 1–5 Likert scale is meaningless** — no true zero.
- **Faithfulness / groundedness** = fraction of atomic claims in the answer entailed by the retrieved context. Computed by an LLM decomposer plus an LLM entailment check — two model calls, compounding error.
- **Answer relevancy** (RAGAS; renamed `ResponseRelevancy` in current versions) = generate questions back from the answer, cosine-similarity against the original question, average. **It measures whether the answer addresses the question, not whether it is correct** — a fluent, confident, wrong answer scores high. Never present it as accuracy.
- **Context precision@k** (are relevant chunks ranked high) vs **context recall** (did the context contain everything the gold answer needed) — retrieval metrics, *not* the same as faithfulness.
- **recall@k**; **MRR** = mean of 1/(rank of first relevant); **nDCG@k** = DCG/IDCG, DCG = Σ relᵢ/log₂(i+1), or the exponential-gain form Σ (2^relᵢ − 1)/log₂(i+1) for graded relevance.
- **The two bounding ablations:** empty-context floor (is retrieval doing anything, or is this parametric memory?) and oracle/gold-context ceiling (how good could generation be?). Report where the system sits between them.
- **Cohen's kappa** = (p_o − p_e)/(1 − p_e); Landis–Koch: 0.41–0.60 moderate, 0.61–0.80 substantial. **Kappa is prevalence-sensitive** — at 90% pass rate you can have 95% raw agreement and a bad kappa, so report both. **Krippendorff's alpha** for >2 raters or missing labels; **weighted kappa** for ordinal.
- **Judge as classifier**: TPR and TNR against human gold. Net bias on the reported pass rate = (1−TNR)·(fraction truly failing) − (1−TPR)·(fraction truly passing) — it can inflate *or* deflate. Prevalence correction (Rogan–Gladen): true ≈ (observed + TNR − 1)/(TPR + TNR − 1), valid only when TPR + TNR > 1. **Judge bias partly cancels in a delta** if error rates are stable — but verbosity bias is exactly the one that isn't stable after prompt work.
- **Judge biases**: position, verbosity, self-enhancement/self-preference. Mitigations: order-swapping, binary rubrics, reference-guided grading, judge from a different model family than the generator. Reference point: MT-Bench (arXiv 2306.05685) reported >80% judge–human agreement, "the same level of agreement between humans" — but that is *pairwise preference on open-ended chat*, and does not transfer automatically to a RAG groundedness rubric. Cite it as an anchor, never as a warrant.
- **McNemar** for paired binary before/after with **one run per question**: χ² = (b−c)²/(b+c) on discordant pairs; exact binomial when b+c is small. Not Pearson's chi-square test of independence, not a two-sample z-test. **With k runs per question McNemar does not apply** — use a cluster bootstrap of the paired difference, or a mixed-effects logistic model / GEE with cluster-robust SEs.
- **Cluster bootstrap**: resample questions (the cluster), k = 3–5 runs each, ~1,000 resamples. Question-level variance dominates run-level variance.
- **Non-determinism at temperature 0**: inference kernels are not batch-invariant and batch composition varies with server load; MoE routing adds more. "Temperature 0 is not deterministic" is a correct and current thing to say in 2026.
- **Leakage**: eval questions generated from indexed chunks → question inherits chunk vocabulary → retrieval becomes lexical matching. Fixes: held-out docs, paraphrase, multi-hop, real logs, unanswerable negatives.
- **Harness constancy**: same question set (hashed, version-controlled), same rubric text, same judge model *snapshot*. A rolled model alias moves the score with no system change. If constancy can't be established, re-run the old system through today's harness.
- **Gold-set bias**: you only label what some retriever surfaced, so recall is biased upward. Pooling across retrievers reduces it, doesn't remove it.
- **Why binary beats 1–5**: a "4" isn't stable across judge-prompt revisions; judges use two of five bins; a mean has no gate semantics; agreement is cleanly defined on binary. The cost — losing severity — is paid back with a failure-reason label alongside the pass/fail.

---

## Claim 5 — "Defined benchmarks and automated checks covering accuracy, latency, reliability and cost, after which agent task success rates rose by around 20%"

**Why this one is dangerous:** It has two independent attack surfaces. First, "agent task success rate" is systematically inflated by how almost everyone computes it — single run per task, end-state only, no retry accounting. Second, the sentence structure invites the killer question: *he defined the benchmark and he reported the improvement against it*, which is textbook Goodhart. Underneath both sits attribution — this is Turing client work, so he may not be able to produce the underlying data at all. And the previous version of this document missed the two confounds that move agent success rates more than anything else: **the step/turn cap** and **the model snapshot underneath the API**. Either one can produce 20 points with no engineering change whatsoever, and a good interviewer knows it.

### The opening question

> "You defined the benchmark and then reported a 20% improvement against your own benchmark. Why should I believe that?"

**❌ What most candidates say** (and why it loses):

> "It was a fair benchmark — we had a diverse set of tasks covering all the main flows, and we ran the agent against them before and after the changes. Task success went from about 60% to about 80%. The client signed off on the methodology."

The tell is "the client signed off," offered as a substitute for a mechanism. It converts a technical question into an appeal to authority, and it says that when pressed on rigour this candidate reaches for social proof. Two more: not one word about runs per task, which alone means the number is optimistic; and "60% to about 80%" is stated without ever saying whether the resume's "20%" is those 20 points or a 20% relative move — the same ambiguity as Claim 3, and it goes unaddressed for the whole claim.

**✅ Model answer — 25 seconds:**

> "Success was end-state, deterministic — the final repository, PR, or ticket-tracker state had to match the annotated goal state, plus any required information had to actually be communicated back. Aggregated over 3 runs per task, not one. The 20 is 20 points — pass³ success went from 51% to 71%. And I'll say up front: this was client work under NDA, so I can describe the method in full detail, but I can't pull the raw numbers, and I'm not going to pretend otherwise."

**Truth gate:** "over 3 runs per task, not one" is a strong claim and the most likely one to be false. If the benchmark ran once per task, say:

> "Single run per task, which I'd call out as the weakness — that's the optimistic tail of a distribution, not the distribution, and if I built it again multi-run reliability would be the first thing I'd add."

That answer *scores better* than a fabricated k, because it demonstrates he knows what single-run means, which is the actual thing being tested.

**✅ Model answer — 2 minutes:**

> "Four axes, deliberately in tension, because optimising any one alone gives you a worse agent.
>
> **Accuracy** was end-state verification — deterministic check that the final state of the environment matched an annotated goal state. That's the only way to score an agent where multiple valid paths exist; trajectory exact-match punishes an agent for solving it a different correct way. On top of end-state I scored the trajectory *diagnostically* — decomposed into: was a tool call needed at all, was it the right tool, were the arguments right, did it use the result, did it recover when the tool errored, did it terminate correctly. That decomposition is where the actionable signal lives; the aggregate rate just tells you up or down.
>
> **Reliability** is the axis people skip, and it's two different things. One is agent consistency: success over a single run is the optimistic number. The honest metric for a production agent is pass^k — the probability it succeeds on *all* k attempts — not pass@k, which is 'at least one of k' and is only appropriate when you have a verifier and get to pick the winner. A user doesn't get to retry and pick. The public reference point is τ-bench: GPT-4o under 50% at one trial and pass^8 under 25% in retail. That's a 2024 paper and a 2024 model — frontier models are far higher on single-trial retail now — but the *shape* is what generalises: the single-trial number always overstates what a user experiences, and the consistency gap is stubborn. I'd cite the shape, not the number.
>
> The other half of reliability is the environment. I tagged infrastructure failures separately from agent failures — container crash, stubbed API 5xx, network — because if you fold those into the success rate you're measuring your own test rig. I'd report agent success rate excluding infra failures *and* the infra failure rate itself, never silently drop them.
>
> **Latency** was p50 and p95 wall-clock per task, plus turn count and tool-call count, because in an agent step count is the latency driver, not token throughput. Two things I'd state alongside it: whether the percentile is conditioned on success — dropping failures makes latency look great — and the step-cap censoring rate, because runs that hit the cap are right-censored, so p95 is a lower bound, not a measurement.
>
> **Cost** was tokens split cached/uncached, and the one that actually matters — cost per *successful* task. The clean way to compute it is total spend across all attempts divided by the number of successes. The shorthand 'cost per attempt ÷ pass rate' is close but it understates, because failed runs are usually the expensive ones — they loop to the step cap. A cheaper model that needs three tries isn't cheaper.
>
> On 'did I tune it' — my 30 tasks and the grading harness were built independently of whoever was tuning the agent, and a fixed 15-task held-out slice went untouched by either side until the final measurement, with acceptance thresholds fixed with the client before the runs, not after. And the concrete evidence: the benchmark caught a real regression — a model-checkpoint swap that pushed small-fix-implementation success down 9 points because the new checkpoint got more aggressive about refactoring beyond the requested scope, and it was flagged before rollout. A benchmark that only ever goes up is a benchmark you're tuning to."

**Why this works:**
- pass^k vs pass@k with correct semantics *and* a correctly-dated reference point. The 2026 fix matters: quoting a 2024 GPT-4o number as though it's current is the fastest way to look like someone who read one paper in 2024 and stopped.
- End-state vs trajectory framed as a design decision with a reason.
- Tool-call decomposition shows he's debugged agents, not just scored them.
- The corrected cost formula — total spend ÷ successes, with the explicit note that the ÷ pass-rate shorthand understates because failures burn more — is a sharper practitioner tell than the shorthand was, and the shorthand was the thing a hostile interviewer would have picked off.
- Latency conditioning and step-cap censoring: almost nobody says this, and it's the correct objection to any agent latency percentile.
- Separating infra flakiness from agent failure is the detail that proves he ran a real harness against real containers — which, given the air-gapped Dockerized environments on his resume, is true and corroborating.
- "A benchmark that only ever goes up is a benchmark you're tuning to" pre-empts Goodhart by conceding its premise and answering with a named regression.
- The NDA boundary is stated by him first, making it a professional norm rather than an excuse extracted under pressure.

### The attribution problem — claims 4 and 5 are Turing client work

**How interviewers actually react.** Nobody expects an NDA breach, and no competent interviewer penalises "I can't share the client or the raw numbers." What they *do* penalise, hard, is a candidate who tries to satisfy the question anyway — producing suspiciously round numbers, or getting vaguer with each follow-up. The failure mode is not confidentiality, it's *evasiveness that looks like confidentiality*. The distinction they're testing: **methodology is almost never the confidential part.** Client identity, absolute numbers, and proprietary task content are. If he describes the eval design in full mechanical detail and redacts only identity and raw figures, that reads as someone who understands where the line is. If he redacts the methodology too, it reads as someone with nothing to describe.

**The exact framing — front-load it, don't wait to be asked:**

> "Quick flag before I get into it — this was consulting work for a client I can't name, and I don't have the data anymore; I never had a copy to take with me. So here's the deal I'd propose: I'll walk you through the method in as much depth as you want, because the method isn't the confidential part. Where I quote a number, I'll tell you whether it's one I personally computed or one that came from the client's side. And if you want a number I own end to end and can show you the code for, use the AML/CTF RAG side project instead — that one's mine, all of it."

That last sentence is the move. It converts "I can't verify this" into "here is something better I *can* verify," without defensiveness. Same guard as Claim 3: it only works if the side project actually has a harness to open.

**Separating his contribution from the team's — the formula.** Singular for what he did, plural for the team, and name the seam explicitly. Never let the two blur — blurring reads as overclaiming, and refusing to claim anything reads as junior:

> "Across 6 Turing engagements I co-led 4 of them. On the coding-agent evaluation engagement I specifically owned task authorship for 30 of the 80 benchmark tasks and the automated grading harness. What I did *not* own was the other 50 benchmark tasks or the underlying agent implementation — that was the client's engineering lead. So the 20% is a team number on a system I built the measurement layer for — I can defend how it was measured completely, and I'd be guessing if I told you which of the changes drove most of it."

"I can defend how it was measured, I'd be guessing on what drove it" claims exactly one thing and disclaims exactly one thing.

### Brackets, triaged

**Must fill:** `3` runs per task (pass³) (or the honest "one, and here's why that's a weakness") · `20 points` (51% → 71%) · `80` tasks in the benchmark · the checkpoint-swap regression the benchmark caught — this one is the whole Goodhart defence and an empty bracket here collapses the answer · `30-of-80 tasks plus the grading harness owned, vs. the other 50 tasks and the agent implementation not owned` · `25`-step cap.

**Fill if reconstructible:** `15`-task held-out split · malformed/hallucinated CI-hook tool-call arguments as the dominant failure category · the coding-agent evaluation engagement (PR review triage, bug triage, small-fix implementation).

**If the named regression can't be recalled, do not bluff it.** Say: "I can't give you a specific caught regression from memory, which weakens my answer and I know it. The structural defences were the held-out 15-task split and independent task authorship, and if I ran it again the named-regression log is the artefact I'd keep, precisely because it's the only falsifiable evidence that a benchmark isn't being tuned to."

### The follow-up chain — they will not stop at one question

**Q: "You defined the benchmark AND reported the improvement. How do I know it isn't tuned to the result?"**
**A:** "You can't fully rule that out from the outside, and I'm not going to pretend the design was bulletproof. What I can tell you is what constrained it. A held-out split of 15 tasks that neither side looked at while iterating, only at the end. Task authoring separated from optimisation on my side — I wrote 30 of the 80 tasks and built the grading harness without touching the agent implementation; the client's engineering lead wrote the other 50 tasks and owned the agent. Acceptance thresholds were fixed with the client before the runs, not after. And the falsifiable one: the benchmark caught a checkpoint-swap regression — it went *down* on small-fix implementation while aggregate success kept climbing, and we held that checkpoint back and root-caused it to the model getting more aggressive about refactoring outside the requested diff. The structural weakness I'd name honestly is that the client's engineering lead wrote 50 of the 80 tasks and also owned the agent implementation, so there's a shared-assumption risk on that majority slice that my independently-authored 30 tasks and the held-out split only partly offset. The fix is a third party authoring adversarial tasks after the fact, and if I ran it again that's the line item I'd add."
*Signal:* Concedes the premise, answers with mechanisms and a falsifiable example, then volunteers the residual weakness and the fix.

**Q: "Is that 20 points or 20% relative?"** ← *new; the same ambiguity Claim 3 makes a whole section of, and it was never closed here*
**A:** "20 points — 51% to 71%. Worth saying that the two are very different claims at that baseline, and if I couldn't tell you which, you should discount the number entirely."

**Q: "How many tasks in the benchmark? What's the interval on a 20-point move at that n?"** ← *new*
**A:** "80 tasks. Unpaired, the 95% interval on a proportion around 0.7 at n = 80 is roughly ±10 points, so a 20-point move clears it and a 5-point move wouldn't — but it's paired, same tasks both sides, which tightens it substantially, and the resampling unit is the task. The number I'd actually want next to the delta is the count of tasks that flipped each way, because 19 flipped up and 3 flipped down tells you more than the aggregate does."
*Signal:* Knows small agent benchmarks are noisy and that discordant counts are the informative quantity.

**Q: "What was the step cap? How many failures were just hitting it?"** ← *new; a top-two confound and it was missing entirely*
**A:** "25 steps, pinned across both runs. This matters more than people expect — raising a turn limit from 15 to 30 can move success rate by double digits with zero change to the agent, so if the cap moved between measurements the comparison is void. I reported the cap-hit rate as its own number — it fell from about 12% pre-change to 4% post-change — because a run that ends at the cap is censored, not failed-for-a-reason, and it's a different fix from a wrong-tool failure."
*Signal:* This is a "have you actually run an agent benchmark" question. The censoring point is the giveaway that he has.

**Q: "Did the underlying model change between your before and after?"** ← *new; the other top-two confound*
**A:** "Pinned to explicit model snapshot IDs, not aliases — true for both the agent model and the judge calls inside the grading harness. If a provider rolls the model behind an alias mid-window, you get a free delta you didn't earn, and you'd never see it in your own diff. Where I'd caveat it: I can't personally re-verify that today, since the engagement ended and I no longer have access to the harness config — if it turned out not to have been pinned, model drift would be a confound I couldn't exclude, and it moves in the direction that flatters me. That's a reason to weaken the claim, not defend it."
*Signal:* Naming the confound that would *inflate his own number*, unprompted, is the highest-trust move available in this whole document.

**Q: "Success rate on what — did the agent do the right thing, or just end up in the right place?"**
**A:** "Both, scored separately. End-state was the pass/fail — deterministic comparison against an annotated goal state, plus a check that required information was actually surfaced to the user, because an agent can leave the database correct and never tell anybody. Trajectory I used for diagnosis, not for the score, because there are usually several correct paths and exact-match trajectory scoring marks valid solutions wrong. Where trajectory did become pass/fail was policy: for example, it must not close out a bug-triage task as resolved before leaving a comment summarizing root cause on the ticket — those are hard constraints, and you check them on the path, not the endpoint."
*Signal:* Knows end-state scoring misses communication failures, and knows when trajectory constraints legitimately bind.

**Q: "Was there partial credit?"** ← *new*
**A:** "Binary end-state. I went binary because partial credit is gameable — you can raise the score by making the agent do more of the easy prefix and never finish — and because 'the task got done' is the thing the client is buying. The cost is sensitivity: binary can't see an agent that went from 20% of the way to 80% of the way. I recovered that through the failure taxonomy and the step at which it died, rather than by putting partial credit in the headline number."
*Signal:* Understands the gameability argument, and knows where the lost sensitivity went instead.

**Q: "How many runs per task?"**
**A:** "3. If it were one, I'd tell you the number is the optimistic tail of a distribution, not the distribution. Agent runs are high-variance — non-determinism in the model plus a stateful environment — and single-run numbers are both noisy and biased upward relative to what a user experiences, because a user has to hit it right the first time. In our case single-run success was 79% against a pass³ of 71% — about 8 points of exactly that inflation. That's why the headline was pass³, not the single-run number. When I put an interval on it, the resampling unit is the *task*, not the run — task difficulty is where the variance lives. One caveat on pass^k itself: it assumes attempts are independent, and in a stateful environment with a fixed seed they aren't fully, so I'd read it as a bound rather than a literal retry probability."
*Signal:* Multi-run necessity, direction of the bias, clustered resampling — and the independence caveat, which is the one thing a reader of the τ-bench paper would push on.

**Q: "Was the environment reset between runs? Any cross-run contamination?"** ← *new; and it's a strength for him, given the air-gapped Docker work*
**A:** "Full reset to a snapshot per run — fresh container, database restored to the seed state. Otherwise run 2 starts from run 1's mutations and the task isn't the same task anymore, which shows up as a mysteriously improving success rate over the course of a batch. Each run pulled a clean container image and reset the target repo to a pinned commit before the agent touched it. The related trap is task-order effects when tasks share a fixture; I isolated fixtures per task so ordering couldn't leak state between tasks."
*Signal:* This is infrastructure detail he genuinely owns, and it corroborates the "air-gapped Dockerized agent training environments" line on his resume rather than just repeating it.

**Q: "Was there a simulated user? What model played it?"** ← *new; unavoidable if he mentions τ-bench, and he does*
**A:** "No. Tasks were single-shot against a fixed repo and CI state, which removes the user-simulator confound entirely but also means the benchmark doesn't test multi-turn clarification — a real coverage gap, since a good chunk of actual PR review is back-and-forth with a human reviewer. If I built a version with a simulator, I'd treat it as a confound in its own right — a more compliant simulator inflates success, and swapping the simulator model changes your headline with no change to the agent — so it would need to be pinned alongside the agent model, with its variance sitting inside the k runs, not outside them, and validated by comparing simulator transcripts against real ones to check it isn't systematically more cooperative than a real user."
*Signal:* Almost nobody thinks of the user simulator as a measured component. Treating it as a pinned dependency with its own validity question is a strong differentiator.

**Q: "Did the task distribution look like production traffic?"** ← *new; construct validity, and it was missing*
**A:** "Partly, and I'd be careful here. Tasks were hand-authored from the client's own workflow docs and a sample of past closed PRs and bug tickets. Because they're hand-authored, the benchmark measures the flows we thought mattered, and an unweighted mean over those has no claim to represent production — a 20-point gain on a uniform task set can be a 3-point gain in production if the wins land on rare flows. They weren't frequency-weighted — all 80 tasks counted equally regardless of how often that flow actually occurs in the client's real PR volume, and that's a real gap I'd name. The honest framing is that it's a regression and comparison instrument, not an estimate of production success rate."
*Signal:* Distinguishing "my benchmark went up" from "production got better" is a distinction most candidates never draw, and drawing it *reduces* the claim, which is why it lands.

**Q: "What did the failures actually look like?"**
**A:** "I kept a failure taxonomy and a transition matrix rather than just a pass rate. Categories roughly: no call when one was needed, wrong tool, right tool with malformed or hallucinated arguments, correct call whose result the agent ignored, no recovery after a tool error, premature termination, looping to the step cap, and policy violation — plus infra failure as a separate non-agent bucket. The matrix is step-type by failure-category, and it makes the bottleneck obvious — on the coding-agent engagement it concentrated in malformed or hallucinated arguments on the CI/CD-hook tool calls, which is why we tightened tool-call schema validation and added a dry-run confirmation step before any CI-hook call that mutated state. Aggregate success rate can't tell you that; two systems at the same 70% can be broken in completely different ways."
*Signal:* Failure taxonomies and transition matrices are what people who actually shipped agents build. Very hard to fake.

**Q: "What would have made you say the agent got worse?"** ← *new; the falsifiability probe, and it's the natural escalation of the Goodhart question*
**A:** "Stated before the runs: a drop below 50% on the held-out split, any policy-violation rate above zero, a regression in any single failure category beyond 5 points even with aggregate up, or a rise in cost per successful task beyond 15%. If you can't tell me in advance what result would have made you ship nothing, the benchmark isn't a test, it's a press release."
*Signal:* Pre-registered failure criteria. This is the strongest single sentence available on this claim and the previous draft didn't have it.

**Q: "What was your specific contribution?"**
**A:** "Across 6 Turing engagements I co-led 4. On the coding-agent evaluation engagement, I specifically owned task authorship for 30 of the 80 benchmark tasks and the automated grading harness. What I did not own was the other 50 tasks or the underlying agent implementation — that was the client's engineering lead. So the 20-point gain is a team number on a system I built the measurement layer for; I can defend how it was measured completely, and I'd be guessing if I told you which of the changes drove most of it."
*Signal:* Precision about ownership boundaries. Interviewers are calibrating whether they can trust *future* claims from this person; a clean seam is the evidence.

**Q: "What's it today — is that agent still in production?"**
**A:** "I don't know, and I wouldn't guess — the engagement ended in January 2025 and I don't have visibility after that. What I'd tell you is which parts of the method I've since reused: the pass³ framing and the four-axis benchmark show up in how I built the eval harness for the AML/CTF RAG side project, where I can show you the code."
*Signal:* "I don't know and I won't guess" is a credibility deposit, not a withdrawal — especially followed by something he *can* show.

### If the number does not survive

> "I'll be honest with you — the 20% is a number I saw in a client-side report; I didn't compute it myself and I can't reconstruct the denominator for you. So I'd take it off the table. What I'd stand behind is that I defined the benchmark and built the automated checks it ran on, and I can walk you through that design in as much detail as you want, because that part is mine."

**Resume line — before:**
> Defined benchmarks and automated checks covering accuracy, latency, reliability and cost, after which agent task success rates rose by ~20%.

**Resume line — after (keeps a defensible number):**
> Defined the evaluation benchmark for 6 frontier-model agent engagements — deterministic end-state verification, tool-call-level failure taxonomy, pass³ reliability over 3 runs, p50/p95 latency, and cost per *successful* task — and the automated checks that ran it; used to gate rollout decisions across those 6 client engagements.

**Resume line — after (tighter, one line):**
> Defined agent evaluation across 6 frontier-model engagements: deterministic end-state verification, tool-call failure taxonomy, and accuracy/latency/reliability/cost benchmarks with automated regression gates.

**Resume line — after (result reframed as capability, no borrowed number):**
> Owned agent evaluation across 6+ frontier-model engagements: deterministic UI-state verification, end-state vs trajectory scoring, pass³ multi-run reliability, tool-call failure taxonomy, and accuracy/latency/reliability/cost benchmarks with automated regression checks.

> **Truth gate on the resume line.** Every mechanism listed is a claim he will be asked to describe in mechanical detail. `pass^k` is bracketed deliberately: if the harness ran once per task, **delete it**. A bullet listing pass^k followed by "we actually ran once per task" is worse than the bullet without it, because the interviewer now knows he lists techniques he didn't use. Same rule for "deterministic UI-state verification" — he did this, so it stays; anything he didn't do comes out.

Losing "20%" costs almost nothing here. The mechanism list is more impressive than the number ever was, and it's unattackable because it's true.

### The numbers/vocabulary he must have cold for this claim

- **pass@k** = 1 − C(n−c, k)/C(n, k) over n samples with c successes — "at least one of k succeeds." Optimistic. Correct only when you have a verifier and can select the winner.
- **pass^k** = probability *all* k independent attempts succeed; unbiased per-task estimator with c successes in n trials (n ≥ k) is C(c, k)/C(n, k), averaged over tasks. The honest metric for a production agent. **Assumes independent attempts** — in a stateful environment they aren't fully independent, so treat it as a bound.
- **Reference point, correctly dated:** τ-bench (arXiv 2406.12045) — "even state-of-the-art function calling agents (like gpt-4o) succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail)." That is a **2024 paper about a 2024 model**; frontier models score far higher on single-trial retail in 2026. Cite the *shape* — single-trial overstates user experience, the consistency gap persists — not the number as current SOTA. τ²-bench (arXiv 2506.07982) — dual-control, agent *and* user act on a shared environment; significant performance drops moving from no-user to dual-control.
- **End-state verification**: final environment state compared against an annotated goal state. Plus a communication check — did required info reach the user.
- **Trajectory scoring**: diagnostic, not pass/fail, because multiple valid paths exist. Exception: hard policy constraints, checked on the path.
- **Tool-call decomposition**: needed a call? → right tool? → right arguments? → used the result? → recovered from the error? → terminated correctly?
- **Failure taxonomy**: no-call, wrong-tool, malformed/hallucinated args, ignored-result, no-recovery, premature-stop, loop-to-step-cap, policy-violation — plus **infra failure as a separate non-agent bucket**, reported, never silently dropped.
- **Cost per successful task = total spend across all attempts ÷ number of successes.** The shorthand "cost per attempt ÷ pass rate" only holds if failures cost the same as successes; they don't — failures loop to the cap — so the shorthand **understates**. Know both and know why they differ.
- **Latency in agents**: p50/p95 wall-clock, plus turn count and tool-call count — step count is the driver, not token throughput. State whether percentiles are conditioned on success, and report the step-cap-hit rate, because capped runs are right-censored and p95 is then a lower bound.
- **The two confounds that move agent success rates most:** the **step/turn cap** (pin it; a cap change alone moves double digits) and the **model snapshot** (pin explicit snapshot IDs, never aliases). Also: environment reset between runs, and the **user simulator** if there is one — pin its model and prompt, and count its variance inside k.
- **Construct validity**: an unweighted mean over hand-authored tasks is a comparison instrument, not an estimate of production success rate. Say which one you're quoting.
- **Goodhart defences, in order of strength**: pre-registered failure criteria → held-out split untouched during iteration → task authoring separated from optimisation → thresholds pre-agreed → a *named regression the benchmark caught* → third-party adversarial tasks added after the fact.
- **The line:** "A benchmark that only ever goes up is a benchmark you're tuning to."
- **The other line:** "If you can't tell me in advance what result would have made you ship nothing, the benchmark isn't a test."

Sources: [τ-bench (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045), [τ²-Bench (arXiv:2506.07982)](https://arxiv.org/abs/2506.07982), [Judging LLM-as-a-Judge / MT-Bench (arXiv:2306.05685)](https://arxiv.org/abs/2306.05685)

---

## Appendix — what changed from v1 and why

**Technical errors corrected:**
1. *"A proportion has a confidence interval where a mean rating does not"* — false. Means have CIs. Replaced with the three correct reasons (scale instability across judge-prompt revisions, bin collapse, no gate semantics) plus the honest cost of binary.
2. *McNemar with k = 3–5 runs per question* — v1 recommended both in the same claim; they're incompatible. McNemar needs one binary outcome per unit per condition. Split into single-run (McNemar / exact binomial) vs multi-run (cluster bootstrap of the paired difference, or mixed-effects logistic / GEE).
3. *Judge bias "inflates the pass rate by (1−TNR) × failing fraction"* — only half the term. Net bias is (1−TNR)·(1−p) − (1−TPR)·p and can go either way. Added the delta-cancellation insight and the verbosity-bias exception that breaks it.
4. *"Cost per successful task = cost per attempt ÷ pass rate"* — understates, because failed runs loop to the step cap and cost more. Corrected to total spend ÷ successes, with the shorthand kept and its bias named.
5. *"Not chi-square"* in the McNemar bullet — McNemar's statistic *is* a chi-square; clarified to "not Pearson's test of independence."
6. *3.1 → 4.2 described as "35%"* in the ❌ example without flagging that percentage change on a Likert scale has no meaning. Now flagged as a third tell.
7. *τ-bench GPT-4o numbers presented as current* — verified accurate to the paper, but re-dated as 2024 and reframed as "cite the shape, not the number," which is the difference between current and stale in 2026.
8. *RAGAS answer relevancy* — added that it measures addressing, not correctness, and that a fluent wrong answer scores high.
9. *Faithfulness* — added that decomposition is itself an LLM call, so it's a judge validating a judge with compounding error.

**Missing follow-ups added — Claim 3:** did the thumbs rate move too; was the eval set / rubric / judge snapshot constant across before-and-after (the most common way a delta is fake); what was the baseline and before which change; how were gold chunk IDs produced and is there one right chunk; who decomposes claims for faithfulness; empty-context and oracle-context ablations; slice analysis and the abstention-regression trap; what did the remaining failures look like; what did the quality gain cost in latency and spend.

**Missing follow-ups added — Claim 5:** is it 20 points or 20% relative (v1 raised this for Claim 3 and never closed it here); how many tasks and what's the interval; what was the step cap and the cap-hit rate; did the model snapshot change underneath you; was the environment reset between runs; was there a user simulator and what played it; did the task distribution match production; was there partial credit; what would have made you say it got worse.

**Overclaim risks removed:** "a real, *large* improvement" in the Claim 3 fallback (asserting magnitude while admitting you can't measure it); "LLM judge validated against human labels" as a default resume bullet; `pass^k` and multi-run as unconditional claims in the Claim 5 scripts and resume lines. All now gated on "only if true," each with a scripted honest variant that scores at least as well.

**Practicality fixes:** every claim now has a bracket triage (must-fill / fill-if-reconstructible / never-fabricate), because v1 contained brackets — live TPR/TNR, kappa, McNemar results — he cannot fill and would have left as visible holes mid-answer. The pivot to the AML/CTF side project is now guarded: it only works if that project has a real harness, so the pack specifies the ~2-day build that fills most of these brackets with numbers he owns outright. Given he is interviewing now with 8h/day, that is the single highest-return item in this document. The 25-second Claim 3 answer no longer leads with a caveat, which is wrong for a recruiter screen.