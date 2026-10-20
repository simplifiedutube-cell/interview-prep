"""Learn / Practise / Evidence for track t08 (Inference, cost & serving).

Format: see t03.

Researched Oct 2026. Two source problems in the original track:
  - five items cited 'Claude Cookbook, Cost' and its seven-step checklist. No
    such public page could be opened. The real article is Anthropic's docs page
    'Optimizing for cost and intelligence', whose lever order matches closely.
  - the LLM Inference Handbook moved from bentoml.com/llm to
    handbook.modular.com; the old URLs 301.
CS336 Lecture 10 timestamps were all verified correct against the live chapter
list (Spring 2026 edition, uploaded 12 May 2026, 1:25:30).
"""

CS336 = "https://www.youtube.com/watch?v=EfM546A79aM"
BENCH = "https://docs.vllm.ai/en/latest/cli/bench/serve.html"
COST = "https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence"
CACHE = "https://platform.claude.com/docs/en/build-with-claude/prompt-caching"

DATA = {
"Time to first token vs total latency": (
 "Stanford CS336 Spring 2026 L10 Inference &middot; the Fundamentals and metrics chapter at 5:16|" + CS336,
 "vllm bench serve with --percentile-metrics ttft,tpot,itl,e2el. Pass = you state p50 TTFT and p50 E2EL as two separate numbers|" + BENCH,
 BENCH + "|Allowed values are ttft, tpot, itl, e2el, client_queue_time, and e2el_including_client_queue"),

"KV cache and PagedAttention": (
 "Kwon et al. &middot; PagedAttention (vLLM) &sect;1 Introduction and &sect;4 Method - internal/external fragmentation, block tables|https://arxiv.org/abs/2309.06180",
 "Sweep --gpu-memory-utilization from 0.70 to 0.95 under load and plot preempted requests. Pass = a preemption-vs-KV-space curve|https://docs.vllm.ai/en/latest/configuration/optimization.html",
 "https://arxiv.org/abs/2309.06180|KV cache memory can be significantly wasted by fragmentation and redundant duplication, which limits batch size"),

"Continuous batching": (
 "LLM Inference Handbook &sect; Continuous batching, plus &sect; Chunked prefill on the same page|https://handbook.modular.com/inference-optimization/static-dynamic-continuous-batching",
 "vllm bench serve on a mixed-length dataset at --max-concurrency 1,2,4,8,16,32,64. Pass = the throughput curve shows a knee you can name|" + BENCH,
 "https://handbook.modular.com/inference-optimization/static-dynamic-continuous-batching|it lets each sequence in a batch finish independently and immediately replaces it with a new one"),

"Speculative decoding": (
 "Leviathan, Kalman and Matias &middot; Fast Inference from Transformers via Speculative Decoding - &sect;2 and Algorithm 1|https://arxiv.org/abs/2211.17192",
 "Serve with --speculative-config, logging acceptance rate and tok/s vs baseline. Pass = greedy output is token-identical AND you quote the accept rate|https://www.reddit.com/r/LocalLLaMA/comments/1uyg3za/i_tested_all_llamacpps_speculative_decoding/",
 "https://www.reddit.com/r/LocalLLaMA/comments/1sf57nh/serving_1b_tokensday_locally_in_my_research_lab/|Speculative decoding for GPT-OSS-120B gave ~150 tok/s - the draft model overhead killed it for this setup"),

"GQA and MQA": (
 "Ainslie et al. &middot; GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints, &sect;2 and &sect;3|https://arxiv.org/abs/2305.13245",
 "Compute KV bytes/token from config.json (layers x kv_heads x head_dim x 2 x dtype) for an MHA and a GQA model. Pass = within 10% of vLLM's reported blocks|https://handbook.modular.com/getting-started/calculating-gpu-memory-for-llms",
 "https://www.reddit.com/r/LocalLLaMA/comments/1sf57nh/serving_1b_tokensday_locally_in_my_research_lab/|~With 65 GB taken by the model we have 50GB for KV cache. This allows several million tokens"),

"Quantization for serving": (
 "Stanford CS336 Spring 2026 L10 &middot; the Quantization and pruning chapter at 1:04:29|" + CS336,
 "Serve the same model at BF16, FP8 and NVFP4, recording tok/s, VRAM and score on a fixed eval. Pass = all three columns, and you defend the pick|https://www.reddit.com/r/LocalLLaMA/comments/1uo32yw/qwen_36_27b_vllm_performance_benchmark_results/",
 "https://www.reddit.com/r/LocalLLaMA/comments/1uo32yw/qwen_36_27b_vllm_performance_benchmark_results/|NVFP4 dominates token generation speed (~2.6x faster than BF16): Because token decoding is strictly memory-bandwidth bound"),

"Prefill vs decode": (
 "Stanford CS336 Spring 2026 L10 &middot; Arithmetic intensity analysis at 14:23, then Performance bottlenecks at 25:08|" + CS336,
 "Plot TTFT vs input length at batch 1, then ITL vs batch size at fixed length. Pass = TTFT scales with prompt tokens while ITL stays flat until bandwidth saturates|https://handbook.modular.com/inference-optimization/prefill-decode-disaggregation",
 "https://www.reddit.com/r/LocalLLaMA/comments/1uo32yw/qwen_36_27b_vllm_performance_benchmark_results/|Because token decoding is strictly memory-bandwidth bound, compressing weights to 4-bit dramatically slashes PCIe/VRAM data transfers"),

"1M queries a day": (
 "Anthropic docs &middot; Optimizing for cost and intelligence - cut spend without losing quality, then trade cost against intelligence|" + COST,
 "Pull 30 days from the Usage and Cost Admin API grouped by model, then write before/after $/day for each lever. Pass = both totals are real numbers|https://platform.claude.com/docs/en/manage-claude/usage-cost-api",
 COST + "|The multi-model strategies exist to spend frontier intelligence on that tail without paying frontier rates for the rest"),

"Prompt caching vs semantic caching": (
 "Anthropic prompt caching docs &middot; What invalidates the cache, and Tracking cache performance - the tools, system, messages hierarchy|" + CACHE,
 "Report cache_read_input_tokens over total input for a day, then add a semantic cache and report hit rate AND false-hit rate. Pass = both numbers|https://docs.litellm.ai/docs/proxy/caching",
 CACHE + "|Cache prefixes are created in the following order: tools, system, then messages. This order forms a hierarchy"),

"Model tiering": (
 "Ong et al. &middot; RouteLLM: Learning to Route LLMs with Preference Data - the strong/weak formulation and the cost-quality curve|https://arxiv.org/abs/2406.18665",
 "Run real traffic cheap-first-with-gate. Pass = cost per ACCEPTED result (not per call) and escalation rate, both measured|https://www.reddit.com/r/LLMDevs/comments/1vx4ihl/our_model_router_starts_with_the_cheapest_model/",
 "https://www.reddit.com/r/LLMDevs/comments/1vx4ihl/our_model_router_starts_with_the_cheapest_model/|It is not cost per call. It is cost per accepted change, including every failed tier and retry"),

"Batch APIs": (
 "Anthropic Batch processing docs &middot; How the Message Batches API works, plus the limitations and pricing bullets|https://platform.claude.com/docs/en/build-with-claude/batch-processing",
 "Submit a real 1000-request batch. Pass = wall clock to completion, $ spent vs the same work sync, and the expired-request count|https://platform.claude.com/docs/en/api/messages/batches/create",
 "https://platform.claude.com/docs/en/build-with-claude/batch-processing|All usage is charged at 50% of the standard API prices"),

"Cost arithmetic out loud": (
 "Anthropic Pricing &middot; the model table and its five columns: base input, 5m cache write, 1h cache write, cache hits, output|https://platform.claude.com/docs/en/about-claude/pricing",
 "Hand-compute a month from tokens x volume x $/MTok, then diff against the Cost API total. Pass = within 5%, and you can explain the gap|https://platform.claude.com/docs/en/manage-claude/usage-cost-api",
 CACHE + "|Cache read tokens are 0.1 times the base input tokens price"),

"Provider failover, circuit breakers": (
 "Google SRE Book Ch 22 Addressing Cascading Failures &middot; &sect; Queue Management and &sect; Load Shedding and Graceful Degradation|https://sre.google/sre-book/addressing-cascading-failures/",
 "Kill the primary provider mid-load-test. Pass = failover p99, error rate and seconds-to-recovery are all numbers, not adjectives|" + BENCH,
 "https://sre.google/sre-book/addressing-cascading-failures/|Load shedding drops some proportion of load by dropping traffic as the server approaches overload conditions"),

"Benchmark every hop": (
 "LLM Inference Handbook &middot; LLM observability - the four signals, and what to monitor by layer|https://handbook.modular.com/infrastructure-and-operations/comprehensive-observability",
 "Span every hop (retrieve, rerank, LLM, tools) into a per-hop p50 table that sums to end-to-end p50. Pass = the biggest row surprises you|https://platform.claude.com/docs/en/api/opentelemetry/spans",
 "https://handbook.modular.com/infrastructure-and-operations/comprehensive-observability|Traces follow one request across services, such as a gateway, a router, the inference engine, and any tool calls"),

"p50 vs p95 vs p99": (
 "LLM Inference Handbook &middot; Key metrics for LLM inference - &sect; mean, median and P99 latency, then &sect; Goodput|https://handbook.modular.com/llm-inference-basics/llm-inference-metrics",
 "vllm bench serve --metric-percentiles 50,95,99 at rising concurrency. Pass = find where p99/p50 crosses 3x and explain the queueing|" + BENCH,
 "https://handbook.modular.com/llm-inference-basics/llm-inference-metrics|P99 reveals worst-case performance for the slowest 1% of requests"),

"Load-testing an LLM endpoint": (
 "vllm bench serve CLI reference &middot; --request-rate, --burstiness, --max-concurrency, --ramp-up-strategy, --goodput, --probe-request-rate|" + BENCH,
 "Run --ramp-up-strategy linear with --goodput set to your TTFT SLO. Pass = you state the max RPS the endpoint sustains inside the SLO|https://github.com/vllm-project/guidellm",
 BENCH + "|Sends single-token probe requests alongside the main workload and reports their latency separately"),

"ray-project/llm-numbers": (
 "Read it once for the habit, not the figures - its own README says Last updates: 2023-05-17|https://github.com/ray-project/llm-numbers",
 "Rebuild it as your own one-pager: $/MTok for your three models, your tok/s, your p99, your cache hit rate. Pass = every row measured by you|https://platform.claude.com/docs/en/about-claude/pricing",
 "https://github.com/ray-project/llm-numbers|At Google, there was a document put together by Jeff Dean, the legendary engineer, called Numbers every Engineer should know"),
}
