# Resources mapped to real AI-engineer interview rounds

**How this differs from `../resources.md`.** That file answers *"what should I learn?"* — books, Coursera, the canon. This one answers a narrower question: **for each round that actually appears in real AI-engineer loops, what practice material rehearses that round's real format?**

The filter is match-to-format, not popularity. A resource that teaches the right topic in the wrong format doesn't rehearse the round — and that mismatch is where prep hours die.

---

## Per-round resource map

| Real round | Primary | Backup | Why it matches |
|---|---|---|---|
| **Practical LLM-API coding** (the modal round) | Build 2–3 **real published take-homes** under a clock, from `alexeygrigorev/ai-engineering-field-guide` → `interview/questions/06-home-assignments.md` | Anthropic + OpenAI cookbooks for async/streaming/tool-call patterns | The only corpus of *actual* specs with candidate submissions attached. Rehearsing a real spec is the round |
| **NumPy / ML-from-scratch drills** | **[Deep-ML.com](https://www.deep-ml.com/)** — free, 100+ graded from-scratch problems, linear algebra → attention | **[TensorGym](https://tensorgym.com/)** — free browser PyTorch tensor drills | Replicates the exact format: blank editor, implement from memory, instant tests. Independently recommended by two candidates who ran full lab loops |
| **Transformer components from memory** | **Karpathy — "Let's build GPT" + nanoGPT** | **Raschka, Ch 2–3** (already on your buy list) | Named specifically as prep for the "code architectures from memory" bar. Builds causal-attention / KV-cache muscle |
| **OOP multi-level round** (Anthropic/OpenAI/Databricks) | **LeetCode "Design" tag** — LC-2408 Design SQL, LRU/LFU, Time-Based KV Store | NeetCode's design/OOP material | Maps directly to the progressive-levels format these labs use instead of classic LeetCode |
| **Take-home** | Same field-guide take-home bank + **steal its rubric**: eval harness first, README trade-offs, cost table, demo video | Your own AML/CTF repo as the reusable skeleton | The rubric *is* the grading signal. "Doesn't start with evals" is documented red flag #1 |
| **Eval design round** | **Hamel Husain's Evals FAQ** (free, `hamel.dev/blog/posts/evals-faq`) + write real evals over your own mini-RAG | Eugene Yan's three eval posts | The vocabulary in the FAQ (error analysis, judge validation with TPR/TNR, binary over Likert) is what the round tests |
| **Debugging round** | Clone an unfamiliar repo, **plant 3 bugs a week earlier, fix them cold in 45 min** | Sierra's format description as the rubric | No product rehearses this. Self-administration is the only faithful option |
| **RAG-debugging scenario** | Rehearse the retrieval-failure vs generation-failure split out loud until it's 60 s | Your Week-3 eval harness as the worked example | It's a *verbal* round. Practising it silently doesn't rehearse it |
| **GenAI system design** | **[evidentlyai.com/ml-system-design](https://www.evidentlyai.com/ml-system-design)** — 800 real case studies, 150+ companies, updated Dec 2025 | Hello Interview free tier for the 45-min structure | *"DoorDash does X, we'd do Y because our constraint is Z"* is the single highest-value sentence in this round |
| **AI-assisted coding round** | **interviewing.io's Meta AI-assisted round guide** (real prompts and examples) | Any repo + narrate: decompose → delegate → **verify** → integrate | The round grades decomposition and verification of AI output, not typing |
| **Customer / discovery round** | Peer roleplay: "VP Eng at a 5,000-person fintech." Rule: **no solution before five questions** | Your own 6+ Turing client engagements as the story bank | Documented failure mode is pitching instead of investigating — only roleplay rehearses that |
| **Classical-ML ambush** | **Coursera ML Specialization C2 Wk3 "Advice for Applying ML"** (already enrolled) + Chip Huyen's free *ML Interviews* book as a hole-finder | Deep-ML for the from-scratch implementations | Two documented rejections trace to this bucket. C2 Wk3 is the highest-ROI hour for your 85%-accuracy claim |
| **Verbal question drilling** | **`real-questions.md` in this folder** — frequency-ranked from actual accounts | field-guide `01-theory.md` | Drill the recurring 20%; skip the long tail |
| **DSA (unicorns/GCCs only)** | **NeetCode 150** — arrays/hashing, sliding window, trees, graphs/BFS, 1-D DP | Sean Prashad's 179 as a week-5+ second pass | The problems actually named in accounts cluster exactly there. No hard DP appears anywhere in the corpus |
| **Mock reps** | **Exponent Practice** (free peer) + **BCtCI's bundled AI interviewer** | Self-recording, watched back once | You've excluded paid mocks; these are the credible free substitutes |

---

## Free and essential — bookmark today

- **[Deep-ML.com](https://www.deep-ml.com/)** — the closest thing to a rehearsal environment for the NumPy/ML-from-scratch round
- **[alexeygrigorev/ai-engineering-field-guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)** — 51 documented company processes, ~60 real take-homes with candidate submissions, real question banks. **The single most useful free artifact for this search**
- **[hamel.dev/blog/posts/evals-faq](https://hamel.dev/blog/posts/evals-faq)** — the eval round, free, by the person who taught it to 4,500+ engineers
- **[evidentlyai.com/ml-system-design](https://www.evidentlyai.com/ml-system-design)** — 800 real architectures to cite
- **[interviewing.io/blog](https://interviewing.io/blog)** — the Meta AI-assisted round guide with real prompts; the Amazon LP guide
- **[sierra.ai/blog/the-ai-native-interview](https://sierra.ai/blog/the-ai-native-interview)** — a company describing its own loop in detail. Read it as a rubric
- **[anthropic.com/candidate-ai-guidance](https://www.anthropic.com/candidate-ai-guidance)** — first-party AI-usage policy; settles the "can I use AI?" question for one major target
- **Karpathy — "Let's build GPT"** and **nanoGPT**
- **Glassdoor / AmbitionBox interview tabs** for every company you apply to — read them the week before the loop. This is free, company-specific, and almost nobody does it

---

## Mismatched for these rounds — don't spend hours here

| Resource | Why it doesn't rehearse the real round |
|---|---|
| **Grinding LC Hard / DP** | Anthropic, OpenAI and Scale ran **zero classic LeetCode rounds** in a documented Fall-2024 loop — they use OOP/practical instead. No hard DP appears anywhere in this corpus. LC grind pays only at Google/Meta/Glean/Perplexity |
| **"Top 50 LLM interview questions" listicles** | Synthesized from each other, not from candidates. Overlap `real-questions.md` only at the surface, and contain **zero** coding/debugging/take-home formats — which is where loops are actually decided |
| **`ombharatiya/AI-Engineer-Interview-Questions`** | The repo itself states questions are built from **public info — job posts and blogs, not real interviews**. Fine as a syllabus checklist; invalid as evidence of what's asked |
| **Ranking/recsys ML system design** (DLRM, ads CTR) | Real and heavy in *MLE* loops, wasted for AI-engineer/GenAI product roles unless the JD says recommendations |
| **Framework tutorial completion** (LangChain/CrewAI courses) | Interviewers report the pipeline is flooded with *"tutorial-completers who never shipped systems that failed."* Design exercises exist specifically to filter them. You get grilled *underneath* your framework choice, not on it |
| **Heavy math rederivation** | An experienced interviewer calls expecting rederivation-from-memory a broken interview. Survives mainly in research-scientist tracks — which you're not targeting |
| **PyTorch training-loop mastery** | Training-from-scratch rounds concentrate in **research-engineer** tracks. Product AI-eng loops test fine-tune *decisions* (LoRA vs RAG vs prompt) verbally. **Your no-training-loop gap matters far less than your NumPy-from-scratch gap** — which shows up everywhere |
| **AI interview copilots** (Final Round AI et al.) | ~1/3 of surveyed FAANG interviewers have caught suspected AI cheating; 11% run detection; Meta mandates full-screen share. Permanent-blacklist event |

---

## The reprioritisation this research implies

Three things move, given your profile:

1. **NumPy-from-scratch moves UP, PyTorch training moves DOWN.** Cosine similarity, k-means, logistic regression with SGD, softmax, attention — these appear in real screens at Mistral, Amazon, Adobe. A full training loop appears mainly in research-engineer tracks you're not targeting. This inverts the earlier plan's emphasis. **Deep-ML.com, 30 min/day, is the highest-value new habit here.**

2. **The practical async/streaming coding round moves UP.** It's the modal AI-engineer round and it was under-weighted before. Six drills, timed, camera on.

3. **Classical ML moves UP from "remediation" to "will decide a loop."** Two documented rejections trace to it, and it's your `~85% accuracy` resume line's home turf. Coursera ML Spec C2 Wk3 is already in your plan for Day 18 — that placement is right, don't let it slip.

Everything else in the 28-day plan stands. This folder complements it; it doesn't replace it.
