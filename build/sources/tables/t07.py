"""Learn / Practise / Evidence for track t07 (Evaluation). Format: see t03.

Researched Oct 2026. Every Arize citation this track previously carried was
wrong: the chapter titles ('Step 1: Tracing with Phoenix', 'Step 4:
LLM-as-a-judge', 'Step 7: Experiments') do not exist, and none of the cited
timestamps is a chapter start. The real artifact is Laurie Voss's 2:04:18
AI Engineer Europe workshop, whose 22 chapters are descriptive sentences.
Verified against the talk page; all five are repointed here.

The CME 295 citations in this track, by contrast, all checked out.
"""

VOSS = "https://www.youtube.com/watch?v=Xfl50508LZM"
FAQ = "https://hamel.dev/blog/posts/evals-faq/"

DATA = {
"Capture real traces before doing anything else": (
 "Voss (Arize) &middot; Ship Real Agents - 22:04 instrument the notebook, then 33:24 build a varied trace set|" + VOSS + "&t=1324",
 "Instrument your LangGraph jobagent with Phoenix and collect 100 real traces. Pass = quote mean spans/trace and p95 latency|" + VOSS + "&t=1324",
 "https://ai.engineer/talks/ship-real-agents-hands-on-evals-for-agentic-applications|Build a varied set of traces before writing checks"),

"Open-code the traces by hand": (
 "Husain &middot; Error Analysis: The Highest ROI Technique In AI Engineering - watch the live open-coding pass|https://www.youtube.com/watch?v=e2i6JbU2R-s",
 "One freeform failure note per trace on 100 traces, the first 30 unaided. Pass = quote the % of traces with at least one defect|" + FAQ + "#q-how-many-examples-do-i-need-for-an-eval",
 FAQ + "#q-how-many-examples-do-i-need-for-an-eval|Start with 100 diverse traces and annotate at least the first 30 yourself."),

"Axial-code those notes": (
 "Lenny's Podcast &middot; Husain and Shankar - 28:07 theoretical saturation, then 31:39 axial codes from error notes|https://www.youtube.com/watch?v=BsWxPI9UM4c&t=1687",
 "Collapse your notes to 8 modes or fewer, then code 20 fresh traces. Pass = zero new categories, plus a per-mode frequency table|https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill",
 "https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill|~28:07 Theoretical saturation: when to stop"),

"Separate retrieval metrics from generation metrics": (
 "Jason Liu &middot; There Are Only 6 RAG Evals - Tier 1 IR metrics, then the Tier 2/3 conditionals: C given Q, A given C, A given Q|https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/",
 "Reverse-generate 100 query-doc pairs from your corpus. Pass = recall@5 and MRR for the retriever, and a SEPARATE faithfulness pass rate|" + FAQ + "#q-how-should-i-approach-evaluating-my-rag-system",
 FAQ + "|The retrieval component is a search problem. Evaluate it using traditional information retrieval (IR) metrics."),

"Build one binary LLM judge": (
 "Voss &middot; Ship Real Agents - 1:17:27 calibrate against explicit human judgments, then 1:22:17 which mistakes the judge makes|" + VOSS + "&t=4647",
 "Hand-label 50 pass and 50 fail, hold out 30. Pass = quote judge TPR, TNR and Cohen's kappa on the held-out split|" + FAQ + "#q-what-should-i-do-when-i-cant-get-my-llm-judge-to-agree-with-human-reviewers",
 FAQ + "|we recommend at least 50 passing and 50 failing examples"),

"Turn 20–50 cases into a regression suite": (
 "Voss &middot; Ship Real Agents - 1:50:16 start small, then decide where evaluations run, and 1:54:12 scope and cost|" + VOSS + "&t=6616",
 "Ship a GitHub Action over 30 curated cases that exits non-zero. Pass = one red run on a deliberately regressed prompt, plus runtime and $/run|" + FAQ,
 FAQ + "|Favor assertions or other deterministic checks over LLM-as-judge evaluators."),

"Write the before/after delta on one page": (
 "Voss &middot; Ship Real Agents - 1:32:03 the controlled improvement loop, then 1:40:29 a release decision needs uncertainty|" + VOSS + "&t=6029",
 "One page: baseline vs post-fix pass rate with 95% CIs AND your measured noise floor. Pass = the CI on the delta excludes zero|https://www.reddit.com/r/LLMDevs/comments/1wzertm/we_ran_the_same_agent_eval_3_times_37_of_the/",
 "https://www.reddit.com/r/LLMDevs/comments/1wzertm/we_ran_the_same_agent_eval_3_times_37_of_the/|We measure the noise floor by splitting one arm's own replicates, where the true difference is zero. It came out at 5.4 points."),

"LLM-as-judge: how it works": (
 "Stanford CME 295 Lecture 8 &middot; 28:00 LLM-as-a-judge through 38:47 position, verbosity and self-enhancement bias|https://www.youtube.com/watch?v=8fNP4N46RRo&t=2327",
 "Run 100 pairwise comparisons, then swap candidate order and rerun. Pass = quote the position-bias flip rate and the verbosity correlation|https://www.youtube.com/watch?v=8fNP4N46RRo&t=2327",
 "https://eugeneyan.com/writing/llm-patterns/|GPT-4 favors itself with a 10% higher win rate while Claude-v1 favors itself with a 25% higher win rate."),

"Binary judgements beat Likert scales": (
 "Hamel and Shreya &middot; Evals FAQ Q19 - binary pass/fail vs 1-5 ratings, and the sub-component workaround|" + FAQ + "#q-why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales",
 "Relabel the same 100 outputs binary and 1-5 with a second rater. Pass = quote both agreement rates, and binary is higher|" + FAQ + "#q-how-many-people-should-annotate-my-llm-outputs",
 FAQ + "|Binary evaluations force clearer thinking and more consistent labeling."),

"Building a golden dataset from a vague spec": (
 "Husain &middot; Field Guide &sect;4.1 A Framework for Generating Realistic Test Data - dimensions, tuples, queries|https://hamel.dev/blog/posts/field-guide/",
 "Build 50 cases by structured dimension sampling. Pass = two reviewers independently reach the same verdict on 90% or more|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents|20-50 simple tasks drawn from real failures is a great start."),

"pass@k vs pass^k</b>": (
 "Anthropic &middot; Demystifying evals &sect; How to think about non-determinism in evaluations for agents|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "Run your 30-case suite 5 times. Pass = quote pass@5, pass^5, and the count of tasks that both passed AND failed across runs|https://www.reddit.com/r/LLMDevs/comments/1wzertm/we_ran_the_same_agent_eval_3_times_37_of_the/",
 "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents|pass^k measures the probability that all k trials succeed."),

"Agent-specific metrics": (
 "Stanford CME 295 L8 &middot; 1:00:15 agent evaluation through 1:23:50, then 1:40:51 Tau-Bench for end-state scoring|https://www.youtube.com/watch?v=8fNP4N46RRo&t=3615",
 "Implement action advancement and tool-selection quality over 30 runs. Pass = both scores plus cost per successful task in dollars|https://docs.galileo.ai/concepts/metrics/agentic/agentic-overview",
 "https://docs.galileo.ai/concepts/metrics/agentic/agentic-overview|Action advancement: Scores how well each action moves the agent toward its goal."),

"Measuring hallucination rate in production": (
 "Evals FAQ Q48 &middot; the online-monitoring half - sampling, reference-free judges, confidence intervals|" + FAQ + "#onnline-monitoring-for-production",
 "Sample 200 live traces a week through a groundedness judge. Pass = the rate with a 95% Wilson interval and a week-over-week delta|" + FAQ + "#q-how-are-evaluations-used-differently-in-cicd-vs-monitoring-production",
 FAQ + "|track confidence intervals for production metrics. If the lower bound crosses your threshold, investigate further."),

"Aggregate accuracy hides per-segment failure": (
 "Evals FAQ Q20 &middot; combining evals into a single metric - the pass-all rate with drill-down and severity groups|" + FAQ + "#q-how-do-i-combine-my-evals-into-a-single-metric",
 "Stratify your suite by document type and by check. Pass = quote the overall pass-all rate beside the worst segment's rate, and the gap|" + FAQ + "#q-how-do-i-combine-my-evals-into-a-single-metric",
 FAQ + "|Design your report or dashboard so you can drill down from the overall pass-all rate to the pass rate for each check"),

"Don't name a prefab eval framework": (
 "Evals FAQ Q27 &middot; Should I use ready-to-use evaluation metrics, plus Why generic eval metrics are misleading|" + FAQ + "#q-should-i-use-ready-to-use-evaluation-metrics",
 "Record a 60-second swap sentence. Pass = it names your judge's TPR/TNR and your hand-label count, and no vendor at all|https://eugeneyan.com/writing/eval-process/",
 FAQ + "|No. Generic evaluations waste time and create false confidence when you use them as quality measures."),

"Lead any project discussion with the eval layer": (
 "Husain &middot; Field Guide &sect;6 Your AI Roadmap Should Count Experiments, Not Features, and &sect;6.3 on communicating it|https://hamel.dev/blog/posts/field-guide/",
 "Record two 90-second project openings. Pass = the first two sentences contain an eval number AND a dollars-per-successful-task figure|" + VOSS + "&t=6361",
 "https://hamel.dev/blog/posts/field-guide/|The key metric for AI roadmaps isn't features shipped - it's experiments run."),

"hamel.dev": (
 "Hamel and Shreya &middot; LLM Evals FAQ, rev. 18 Sep 2026 - read Error Analysis first, then Evaluation Design|" + FAQ,
 "Write your own answer to Q7, Q19, Q25, Q27 and Q48 BEFORE reading each. Pass = score yourself and quote how many of 5 you got right|" + FAQ + "#all-questions",
 "https://github.com/benchflow-ai/awesome-evals|~Must-read starter set (read these first)"),

"eugeneyan.com/writing/llm-patterns": (
 "Eugene Yan &middot; Patterns for Building LLM-based Systems - pattern 1 Evals: Why, More about, How to apply|https://eugeneyan.com/writing/llm-patterns/",
 "Whiteboard all seven patterns from memory in 10 minutes. Pass = all 7 names, plus the 85% vs 81% judge-vs-human agreement figure|https://eugeneyan.com/writing/llm-patterns/",
 "https://eugeneyan.com/writing/llm-patterns/|GPT-4 had higher agreement with humans (85%) than the humans had amongst themselves (81%)."),

"eugeneyan.com/writing/how-to-interview": (
 "Eugene Yan, Jul 2024 &middot; What technical skills to consider, and Calibrating the phone screen for loop success|https://eugeneyan.com/writing/how-to-interview/",
 "Score yourself 1-5 on each skill he names, then fix the lowest two. Pass = quote your own before and after on the weakest one|https://eugeneyan.com/writing/how-to-interview/",
 "https://eugeneyan.com/writing/how-to-interview/|having a basic understanding of evals is key for anyone building ML-powered products."),

"Anthropic — Demystifying Evals for AI Agents": (
 "Anthropic, 9 Jan 2026 &middot; Going from zero to one: a roadmap to great evals for agents - all three sub-steps|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "Rewrite your own eval docs in their task / trial / grader vocabulary. Pass = quote your task count, trials per task and grader mix|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents|A task (a.k.a problem or test case) is a single test with defined inputs and success criteria."),

"benchflow-ai/awesome-evals": (
 "benchflow-ai/awesome-evals &middot; the 12-link Must-read starter set, then &sect;8 LLM-as-judge and &sect;9 agent evaluation|https://github.com/benchflow-ai/awesome-evals",
 "Read the 12 starter links and write 150 words on each. Pass = quote how many you had already covered elsewhere in this track|https://github.com/benchflow-ai/awesome-evals",
 "https://github.com/benchflow-ai/awesome-evals|~Must-read starter set (read these first)"),
}
