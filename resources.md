# Resources — buy list, enrolments, free canon, traps

Filtered to **books + Coursera + free**, per budget. Nothing here without evidence it's a multi-year practitioner default, a recognized author, or a first-party spec. **Decide once here, then don't re-decide mid-sprint.**

---

## 1 · Buy today — 7 books

| # | Title | Author / Publisher / Year | ISBN | ~Cost (India) | Read |
|---|---|---|---|---|---|
| 1 | **Beyond Cracking the Coding Interview** | McDowell, Mroczka, Lerner, Mamano — CareerCup, Jan 2025, 646pp | 978-1955706001 (Shroff Indian ed. 9789355424488) | ₹1,000 | Negotiation §Day 1 · behavioral ch wk1–2 · 13 pattern chapters as an **index** throughout |
| 2 | **Grokking Algorithms, 2nd ed.** | Bhargava — Manning, Feb 2024, 320pp, Python 3 | 9781633438538 | $29.99 (print+eBook) | **Ch 1–8, skim, no exercises, Days 1–3** |
| 3 | **AI Engineering** | Chip Huyen — O'Reilly, 2025, ~532pp | 978-1098166304 | ₹1,150 | **Ch 9** wk2 · **Ch 3–4** wk3 · **Ch 6** wk3 · Ch 5 later. **Skip Ch 7–8 in the sprint** |
| 4 | **Generative AI System Design Interview** | Aminian, Sheng, Xu — ByteByteGo, Nov 2024 | 978-1736049143 (Shroff 9789355424969) | ₹1,000–1,300 | **Ch 1, 2, 3, 4, 6 ONLY** |
| 5 | **Build a Large Language Model (From Scratch)** | Raschka — Manning, 2024, 368pp | 978-1633437166 | $29.99 | **App A + Ch 2 + Ch 3, TYPED**, wk2. Ch 5–7 + App E in months 2–3 |
| 6 | **Hands-On Large Language Models** | Alammar & Grootendorst — O'Reilly, 2024 | 978-1098150969 | ₹1,300 | **Ch 2, 3, 8** — for the diagrams you redraw from memory |
| 7 | **System Design Interview, Vol 1** | Alex Xu, 2020 | — | ₹800–1,000 | **4h targeted skim, wk2 only** |

**Total ≈ ₹11,000–13,000** using Shroff Indian editions for #1/#3/#4/#6/#7 and Manning ebook bundles for #2/#5.

**Ordering notes:**
- Order **BCtCI online** — it includes a **free AI interviewer (200+ problems)** and a **$50 interviewing.io credit**. The AI interviewer is your substitute for paid mocks; use it for *verbalisation*, never for solving.
- 9 BCtCI chapters are free at **bctci.co/free-chapters** — start there today while shipping arrives.
- Raschka's repo **`rasbt/LLMs-from-scratch`** (~100k stars) is free and has bonus modules the print book lacks (GQA, MLA, MoE, DPO, Llama/Qwen/Gemma/Olmo-3). Everything runs on a laptop — no GPU needed.

**Why each is standard:**
- **BCtCI** — official sequel to the best-selling technical interview book ever, co-authored by interviewing.io's founder. Its unique asset is **~100 real interview replays and rubrics drawn from 100,000+ FAANG mock interviews.** It hits four of your declared weaknesses in one volume.
- **Grokking Algorithms** — the default "I know nothing about algorithms" on-ramp for a decade. **Skipping this is the most common near-zero mistake**; it makes every NeetCode problem afterward ~2× faster.
- **AI Engineering** — the **most-read book on the O'Reilly platform since release**, 14+ translations in 18 months; the author wrote the prior de-facto reference. It's your target role's definitive text *and* your resume-defence manual.
- **GenAI System Design Interview** — the ByteByteGo/Alex Xu imprint, the highest-selling interview line after CTCI, and **the only book-form GenAI system-design framework that exists.**
- **Raschka** — the direct antidote to "never written a PyTorch training loop," your single biggest credibility risk.
- **Alammar & Grootendorst** — Alammar's *Illustrated Transformer* is the most-linked explainer in the field. Bought for one purpose: whiteboard diagrams. *Alammar = can explain it; Raschka = can build it.*

### Books for months 2–6 (do NOT buy now)

**DDIA 2e** (Kleppmann & Riccomini, Mar 2026, 670pp) — month 3 · **Géron, *Hands-On ML with Scikit-Learn and PyTorch*, O'Reilly 2025** (the PyTorch edition, ISBN 9798341607972, repo `ageron/handson-mlp`) — months 2–4 · **Shankar & Husain, *Evals for AI Engineers*, O'Reilly 2026** — month 2 · **Raschka, *Build a Reasoning Model (From Scratch)*, Manning Jun 2026** — month 5 · **Aminian & Xu, *ML System Design Interview*** — for the MLE track · ***Fluent Python 2e*** · **Orosz, *The Software Engineer's Guidebook*** Part 3.

### ❌ Do NOT buy

| Book | Why |
|---|---|
| **CTCI 6th ed. (2015)** | Eleven years old, Java-centric, **predates the pattern-vocabulary era** — it scatters two-pointers/sliding-window across chapters instead of naming them as tools. **Superseded by its own official sequel, by its own author.** The most commonly-bought wrong book in your exact situation |
| **Elements of Programming Interviews in Python (2017)** | Abandoned since the Jan 2018 EPI Judge beta. Its problems assume you already recognise the pattern. At <30 problems solved ever it's a morale grinder that breaks you in week 1 |
| **Goodfellow, *Deep Learning* (2016)** | The prestige purchase. No transformers, no LLMs, no modern training practice. 800 pages at the wrong abstraction level. It sits unopened and generates guilt → **Prince, *Understanding Deep Learning*, free PDF at udlbook.github.io** |
| **DDIA (either edition) — in the sprint** | 60–80h with no meaningful skip-to; the value is cumulative. **It will not appear in a GenAI Engineer loop.** Reading it now is procrastination that feels like rigour. Buy it for month 3 |
| **Géron *Hands-On ML* 3rd ed. (2022, Keras/TF)** | Superseded. **Nobody hires for Keras in 2026.** Get the 2025 PyTorch edition — and even that is a months-2–4 book |
| ***NLP with Transformers* (2022)** | **Broken.** Its own repo says the TF sections are untested (Keras 3 incompatible) and Ch 7 is unmaintained — it needs farm-haystack 0.9, Elasticsearch 7.x and **pydantic 1.x**. You ship v2. Hours of dependency hell → Alammar & Grootendorst is its living successor |
| ***LLM Engineer's Handbook*** | Teaches ZenML + SageMaker + MongoDB + Qdrant + Comet + Poetry — none of your stack — and the repo's own README concedes it has drifted from the book |

---

## 2 · Coursera — 4 in the sprint (~18h), 1 later

You have full access, so the only question is which hours are worth it. **Coursera is ~9% of this sprint.**

| Course | Provider | Do what | h | When |
|---|---|---|---|---|
| **Generative AI with LLMs** | DeepLearning.AI + AWS | **Weeks 2 & 3 only @1.5×** — instruction tuning, PEFT/LoRA, soft prompts, RLHF, reward modelling, scaling laws. Your only zero-experience zone and table stakes in a 2026 GenAI loop | 6 | Wk 2 |
| **Retrieval Augmented Generation (RAG)** | Zain Hasan, DeepLearning.AI | **Enrol for the syllabus. Watch zero video.** Its module list is a free interview checklist for something you do for a living | 2 | Wk 1 |
| **Machine Learning Specialization** | Ng, DeepLearning.AI | **C2 Week 3, "Advice for Applying ML"** ← *the single highest-ROI hour in the entire catalogue for you.* Baseline/Bayes error, error analysis, the bias-variance intervention ladder. **This is what lets you defend the 85% line** | 5 | Wk 3, Day 18 |
| **Machine Learning in Production (MLOps C1)** | Ng | **Week 1 only** — concept drift, data-centric AI, deployment monitoring | 5 | Wk 3, Day 19 |
| **PyTorch for Deep Learning Prof. Cert.** | DeepLearning.AI (Moroney) | **C1 + C2.** Datasets/DataLoaders → loss → optimizers → GPU → train/eval loop | 35 | **Months 2–4, NOT the sprint** |

### ❌ Coursera traps — the famous ones, with the specific reason

| Course | Social proof | Why it's wrong for you |
|---|---|---|
| **Deep Learning Specialization** (Ng) | 4.8★, **147,142 reviews**, 995k learners | **127.5h.** Core content is **2017**; the only substantive refresh was an April 2021 TensorFlow-2 port. C5 teaches attention as a **bolt-on to RNNs** — a 2018 framing. Eats a third of your sprint and hands you TensorFlow muscle memory the market stopped hiring for. → **Karpathy L1 + L7, free, 12h** |
| **NLP Specialization** | 4.6★ | 111h. Courses 1–2 are naïve Bayes/TF-IDF/HMMs; C3 is RNN/LSTM. Significant portions built on **Trax, an effectively dead Google framework.** Last substantive update Oct 2021. It's the lowest-rated flagship DLAI spec and **that rating gap is the signal.** You do NLP for a living |
| **Mathematics for ML and Data Science** | — | **94.5h = 24% of your budget** for something no AI/GenAI interview tests directly. Classic "feels productive, isn't." → **3Blue1Brown, ~5h, free** |
| **Algorithms Part I** (Princeton, Sedgewick) | 4.9★, **1,465,075 learners — highest signal in the whole catalogue** | Magnificent course, catastrophic fit. **Java. 50h. Nine hours on union-find.** Never mentions sliding window or backtracking templates. You'd finish month 1 with union-find mastery and fail Two Sum variants |
| **DSA Specialization** (UC San Diego) | 4.6★, 381k learners | **182 hours** = 2.5× your entire DSA budget. **One of its six courses is Genome Assembly.** Brittle autograders |
| **Algorithms Specialization** (Stanford, Roughgarden) | 4.8★ | World-class algorithm *design theory*, 57h, proof-oriented, **zero interview-format practice.** Won't move a near-zero baseline in 4 weeks |
| **Software Design and Architecture** (U. Alberta) | — | **The course people mistake for system design.** It's OOD/UML/GoF and SOA/REST — almost no scalability, sharding, caching, consistency or capacity estimation. 52h wasted |
| **IBM AI Engineering / IBM GenAI Engineering / Microsoft GenAI / Vanderbilt GenAI** | — | 143–198h beginner certificates. IBM's GenAI cert includes *Python for Data Science* and *Developing AI Applications with Flask* — you did the .NET→FastAPI migration. **Worse than neutral: a beginner certificate next to frontier-model agent-training work reads as insecurity about your own background** |
| **Vanderbilt "AI Agent Developer"** | 4.8★, **10,124 reviews** — highest social proof in the agent category | **Half the program is *Prompt Engineering for ChatGPT* (19h), *OpenAI GPTs*, and *ChatGPT Advanced Data Analysis*.** A ChatGPT-power-user program wearing an agent title |
| **Duke MLOps Specialization** | **4.2★** | Lowest rating of any serious program audited. **43h of "Python Essentials for MLOps."** Its sibling *LLMOps* spec has a *Rust for LLMOps* course rated 4.3★ on 15 reviews |
| **Coursera's in-house "ML Production Systems" and "Full Stack Agentic AI"** | no rating, no reviews | Authored by content vendors (Hurix Digital, ansrsource, LearnKartS). Content-mill filler occupying the MLOps- and agent-shaped holes in the catalogue |
| **The entire Coursera "LLM evaluation" shelf** | 8–14 reviews each | **Coursera has nothing credible on evals.** Painful, because evals are your sharpest edge → **Hamel Husain, free** |
| **All Coursera behavioral/interview courses** | 10–148 reviews | On a platform where established courses carry 50,000–500,000+. Fails the adoption bar outright → **interviewing.io free guides** |
| **The original *Machine Learning* (Octave)** | — | Deprecated and superseded in 2022. Any listicle pointing there pre-dates the rebuild |

> ⚠️ **"Starts Aug 2" on every Coursera page is a rolling enrolment date — not a launch or refresh date.** It is precisely how stale specializations look current. Judge freshness by the framework (TF vs PyTorch) and the model names in the labs.
>
> ⚠️ **Andrew Ng's *Agentic AI* course is NOT on Coursera** — it's on `learn.deeplearning.ai` and needs DLAI Pro (~$30/mo). Coursera Plus doesn't cover it. Defer to month 2 if you want it.

---

## 3 · Free canon — bookmark these today

### DSA
- **neetcode.io/practice** — roadmap + NeetCode 150, one video per problem. **Topologically ordered**, which is exactly what a from-zero learner needs and what Blind 75 lacks. Blind consensus: *"Do neetcode.io. Similar thing but free."* → beats AlgoExpert ($99–149), Educative Grokking ($199–299/yr), DesignGurus ($197)
- **techinterviewhandbook.org/grind75** — set to "4 weeks / 20h per week." By Yangshun Tay, creator of Blind 75
- **seanprashad.com/leetcode-patterns** — 179 questions, company-filterable, with a "when should I use X" tips column. **Week 5+ second pass**
- ❌ **NeetCode Pro / NeetCode 250** — the roadmap and all 150 videos are already free, and 250 problems is 3× over budget
- ❌ **LeetCode Premium in week 1** — its only real value is company-frequency tags, useless until you have a named company and a date. **Buy one month at week 9**, or the week an onsite is scheduled
- ❌ **Codeforces / CSES for "fundamentals"** — competitive programming ≠ interviews, and the speed-contest format **actively trains habits that hurt interview performance**: rushed, unexplained code, no verbalisation

### System design
- **hellointerview.com/learn/system-design/in-a-hurry** — free tier, explicitly stated sufficient to pass. The only resource publishing an **explicit minute-by-minute framework** (Requirements 5 / Entities 2 / API 5 / Data Flow 5 / HLD 10–15 / Deep Dives 10) **and the four-axis rubric interviewers actually grade on** (Problem Navigation · Solution Design · Technical Excellence · Communication & Collaboration)
- **excalidraw.com** — the de-facto whiteboard in remote design interviews. **Build ONE template in 15 minutes.** Building a beautiful component library is procrastination with the aesthetics of preparation
- **evidentlyai.com/ml-system-design** — **800 case studies from 150+ companies** (Netflix, Airbnb, DoorDash), updated Dec 2025, tagged GenAI/RAG/agents. *"DoorDash does X, we'd do Y because our constraint is Z"* is the single highest-value sentence in a GenAI design round
- **Arpit Bhayani on YouTube** — LSM trees, B-trees, WAL, indexing, distributed locks (~2h). Principal Engineer II @ Razorpay, ex-Google Cloud, ex-Amazon. ❌ Not his ₹49,999 masterclass — the cohort started 1 Aug 2026 and ends after your window
- ⚠️ **`donnemartin/system-design-primer` (360k stars)** — **star count ≠ currency.** Content is the 2017–2019 canon: no serverless, no modern streaming, no AI/ML serving, no vector stores. Recent commits are translations and link fixes. **90-minute checklist skim, once, then close the tab**

### LLM / transformer theory
- **Karpathy, "Deep Dive into LLMs like ChatGPT"** (Feb 2025, 3h31) — ~4M views, the most-cited whole-lifecycle explainer in the field
- **Karpathy, Neural Networks: Zero to Hero** — **L1 (micrograd)** and **L7 ("Let's build GPT")**. karpathy.ai/zero-to-hero.html
- **3Blue1Brown** — *Essence of Linear Algebra* (~3h) + *Neural Networks* (~2h)
- **Burkov, *The Hundred-Page Language Models Book*** — thelmbook.com, free to read online, pay-what-you-want. Endorsed by Tomáš Mikolov and Vint Cerf
- **Prince, *Understanding Deep Learning***, MIT Press 2023 — **free PDF at udlbook.github.io**, 846 commits, actively maintained. The modern replacement for Goodfellow

### ⭐ Evaluation — your differentiator
- **hamel.dev/blog/posts/evals-faq** — *"LLM Evals: Everything You Need to Know."* Published May 2025, **last modified 18 Jul 2026.** Husain (25+ yrs ML, ex-GitHub/Airbnb) with Shreya Shankar (UC Berkeley) created the most-taken evals course in the industry — **4,500+ students from OpenAI/Google/Meta/Amazon/Microsoft**
- **eugeneyan.com/writing** — LLM-as-Judge survey · Task-Specific Evals · Product Evals in Three Steps. Amazon Principal Applied Scientist; the most-linked practitioner treatment of LLM-as-judge
- ❌ **Maven "AI Evals for Engineers & PMs" — $4,200.** Genuinely the best evals instruction available, and wrong for you: **the next cohort runs Sep 5–Oct 3 2026, ending after your hiring window**, it competes for exactly the hours you need, and it costs a month of senior Indian salary. The free FAQ is **~98% of the interview-relevant value by the same author.** Ask a future employer to expense it

### Agents & MCP
- **anthropic.com/engineering — the 5-post set, read in date order:** *Contextual Retrieval* (Sep 2024) → *Building Effective Agents* (Dec 2024) → *Effective Context Engineering for AI Agents* (Sep 2025) → *Code Execution with MCP* (Nov 2025) → *Demystifying Evals for AI Agents* (Jan 2026). ⚠️ **Citing the Dec 2024 post alone dates you** — treat 2025–26 as amendments
- **modelcontextprotocol.io — spec revision 2026-07-28.** First-party. Cross-vendor adoption (Claude, ChatGPT, VS Code, Cursor) is the strongest possible proof of standard status. ⚠️ **Reject any MCP tutorial predating Streamable HTTP / elicitation**
- **OpenAI, "A Practical Guide to Building Agents"** (~34pp PDF) + Agents SDK docs — your second vendor vocabulary
- ❌ **HF Agents Course (25–30h)** — 30h to re-learn what you ship in production, and **it doesn't even cover MCP** (separate course). Month 3 if you want the certificate
- ❌ **HF Deep RL Course (60h)** for the "RL gym environments" resume line — you need **2 hours** of targeted vocabulary (reward shaping, sparse vs dense reward, episode/rollout, environment determinism, why air-gapped envs matter for reproducibility), not 60

### RAG & serving
- **Jason Liu, "Systematically Improving RAG Applications"** — open-sourced Feb 2026 (567-labs). Author of `instructor`; he shut the course down and released it free, so there's no marketing incentive behind it
- **vLLM docs (Optimization & Tuning) + PagedAttention (Kwon et al., SOSP 2023)** — ⚠️ **not optional: your "−40% latency, −30% cost" line will be attacked in every loop**

### Behavioral, mocks, job search
- **interviewing.io/guides/amazon-leadership-principles** + *"Stop memorizing STAR…"* — built on **~500 recorded Amazon LP interviews with outcomes**, 100+ Amazon engineers, from 100,000+ mocks, and the dataset skews L6/SDE-III ≈ your target level
- **tryexponent.com/practice** — ex-Pramp, **still free**, global peer pool, timezone-friendly from India
- **BCtCI's free AI interviewer** — 200+ problems, ships with the book. Use for **verbalisation**, never for solving
- **levels.fyi/t/software-engineer/locations/india** (updated 2026-08-01) + **AmbitionBox** + **aijobs.net** (47,667 listings, remote toggle, INR filter)
- **haseebq.com/how-not-to-bomb-your-offer-negotiation** — de-facto standard for a decade. ⚠️ 2016: **read for method, ignore every number**
- **Orosz, *The Tech Resume Inside Out*** — thetechresume.com, $20, **free copies for unemployed devs — claim it, you're eligible.** ⚠️ 2020, skip the COVID/market chapter
- ❌ **AI interview copilots (Final Round AI et al.)** — **career-threatening in 2026.** ~1/3 of surveyed FAANG interviewers caught suspected AI cheating; 11% run detection software; Meta mandates full-screen share; getting caught is a permanent-blacklist event. Separately: **no Copilot, no autocomplete, no LLM during the 25-minute problem attempt** — the MIT EEG study (Kosmyna et al., arXiv:2506.08872) found LLM-assisted users showed the weakest neural connectivity and **could not accurately quote their own work**

---

## 4 · Two phrasings that change outcomes

**Never recite "Attention Is All You Need" as the architecture answer.** In 2026 that marks you as a reader, not a builder. The real question is *"what's different in a modern Llama-style block vs the 2017 paper?"* — **decoder-only · pre-norm · RMSNorm · RoPE instead of sinusoidal · SwiGLU · GQA · no encoder.** Know all seven.

**Never name RAGAS as a talking point.** Hamel's critique has propagated widely: *"All you get from using these prefab evals is you don't know what they actually do."* Say instead:

> *"We started with RAGAS-style metrics, found they didn't correlate with our reviewers' judgments, so we built a domain-specific binary judge and validated it against 100 hand-labelled traces."*

That one sentence out-depths most interviewers.

## 5 · One more trap, specific to you

**Do not build a 4th portfolio project.** Highest-appeal, lowest-return move available. You have **three good projects and zero of them have an evals section or a demo video.** 9h of READMEs + 3h of demo video beats any new build — and the Week-3 eval harness on the AML repo is worth more than all of it.

## 6 · Papers — ranked by interview relevance, not fame

Read method + figures only, ~45 min each, one paragraph of notes.

1. **Attention Is All You Need** — *plus the seven deltas above*
2. **RAG** (Lewis et al. 2020)
3. **ReAct**
4. **Lost in the Middle** — punches far above its fame; **it justifies your reranking**
5. **InstructGPT**
6. **LoRA** — ⚠️ highest risk per unit of likelihood, since you've never fine-tuned
7. **DPO** — *"why DPO instead of PPO"* is a standard 2026 question
8. **Chain-of-Thought + Self-Consistency**
9. **PagedAttention** (§1, §4 only) — read with the vLLM docs in week 2
10. **Contextual Retrieval** (Anthropic) — −35% / −49% / −67% retrieval-failure reductions; memorise those numbers
