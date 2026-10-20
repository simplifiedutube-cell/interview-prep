"""Learn / Practise / Evidence for track t10 (GenAI system design). Format: see t03.

Researched Oct 2026. Three corrections carried into the item metas rather than
the hashed item text:
  - the 800ms voice budget is not reachable through a cascaded STT/LLM/TTS
    pipeline. The primer the track itself cites targets 1500ms and its own
    per-hop table totals 1293ms, with LLM TTFB alone at 650ms.
  - 'the four patterns every prompt maps to' has no published source. The page
    it cited lists generic infra patterns instead.
  - Hello Interview premium is not worth buying for this track: its ML module
    is three problems (bot detection, harmful content, video recs) with no
    GenAI design content, and the thread recommending it reads as astroturf.
"""

HI = "https://www.hellointerview.com/learn/system-design/"
PREP = HI + "in-a-hurry/how-to-prepare"
RDLC = "https://www.reddit.com/r/leetcode/comments/1wf1zfp/how_id_approach_system_design_prep_if_i_started/"
AGENTS = "https://www.anthropic.com/engineering/building-effective-agents"

DATA = {
"URL shortener": (
 "Hello Interview &middot; Design a URL Shortener Like Bitly - High-Level Design plus the four deep dives|" + HI + "problem-breakdowns/bitly",
 "25 min in Excalidraw, recorded, no lookups. Pass = you hit all four of its deep dives unprompted|" + HI + "problem-breakdowns/bitly",
 PREP + "|Only after you have tried to answer the question, read the answer key to see how your answer compares."),

"Distributed rate limiter": (
 "Hello Interview &middot; Design a Distributed Rate Limiter - High-Level Design and Deep Dives|" + HI + "problem-breakdowns/distributed-rate-limiter",
 "25 min recorded. Pass = you name the algorithm chosen AND the two you rejected, with a reason for each|" + HI + "problem-breakdowns/distributed-rate-limiter",
 PREP + "|~telling your design out loud under time pressure is a different skill than reading about it"),

"RAG over 10k enterprise documents": (
 "r/OfferEngineering &middot; RAG system design interviews - &sect;5 Multi-tenancy and the framework-to-use section|https://www.reddit.com/r/OfferEngineering/comments/1x54sxn/rag_system_design_interviews_the_pipeline_is_the/",
 "45 min recorded. Pass = all 7 stages covered and the 6 multi-tenancy follow-ups answered. Namespace-per-tenant, not just a filter|https://docs.pinecone.io/guides/index-data/implement-multitenancy",
 "https://www.reddit.com/r/OfferEngineering/comments/1x54sxn/rag_system_design_interviews_the_pipeline_is_the/|So authorization needs to happen as part of retrieval - not after you've already put confidential chunks into the prompt."),

"Real-time chat": (
 "Hello Interview &middot; Design a Messaging App Like WhatsApp - High-Level Design, connection and delivery guarantees|" + HI + "problem-breakdowns/whatsapp",
 "30 min recorded, immediately BEFORE the serving rep. Pass = you justify WebSocket over SSE over long-poll and say what breaks on reconnect|" + HI + "problem-breakdowns/whatsapp",
 HI + "in-a-hurry/delivery|many top FAANGs directly evaluate you on your ability to focus on what matters"),

"LLM customer-support agent": (
 "DoorDash &middot; Path to high-quality LLM-based Dasher support automation - the LLM Guardrail and LLM Judge sections|https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/",
 "45 min recorded. Pass = the escalation trigger is stated as an explicit cost-vs-risk rule, not just low confidence|https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/agentic_ai_agents_system_design_interview/",
 "https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/agentic_ai_agents_system_design_interview/|the interesting part is deciding WHEN to trigger it. Cost vs risk tradeoff. That decision logic is where the actual design challenge lives"),

"Evaluation and observability platform": (
 "Hamel Husain &middot; Your AI Product Needs Evals - The Types Of Evaluation: L1 unit tests, L2 human plus judge, L3 A/B|https://hamel.dev/blog/posts/evals/",
 "45 min recorded. Pass = you draw trace storage, the L1/L2/L3 split, and the path from a prod failure back into the eval set|https://hamel.dev/blog/posts/evals/",
 "https://hamel.dev/blog/posts/evals/|You must remove all friction from the process of looking at data."),

"LLM inference serving at scale": (
 "Hello Interview &middot; Design ChatGPT - deep dives 1-5: streaming, reconnects, GPU routing, tier fairness, context cost|" + HI + "problem-breakdowns/chatgpt",
 "45 min recorded. Pass = all five named deep dives plus cancel-and-reclaim-the-GPU. Get the mechanism names from vLLM|https://blog.vllm.ai/2023/06/20/vllm.html",
 HI + "problem-breakdowns/chatgpt|Because GPUs are limited and expensive, the system has to be deliberate about who gets compute and when."),

"Real-time voice agent": (
 "Voice AI and Voice Agents, An Illustrated Primer &sect;5.1 Latency - the 1293ms per-hop table - and &sect;5.9 Interruption handling|https://voiceaiandvoiceagents.com/#latency",
 "30 min recorded. Pass = your budget sums to a real number and you name the two hops you cut to get there|https://voiceaiandvoiceagents.com/#latency",
 "https://voiceaiandvoiceagents.com/|If you are building conversational AI applications, 1,500 ms voice-to-voice latency is an important target to aim for."),

"Agentic coding assistant": (
 "Anthropic &middot; Effective context engineering &sect; Context retrieval and agentic search - just-in-time vs pre-indexed|https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
 "45 min recorded. Pass = you argue grep-and-glob against an embedding index on freshness and cost, and commit to one|https://www.anthropic.com/engineering/claude-code-sandboxing",
 "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents|Of course, there's a trade-off: runtime exploration is slower than retrieving pre-computed data."),

"Document Q&A with citations": (
 "Anthropic &middot; Contextual Retrieval - Implementing Contextual Retrieval, then Further boosting performance with Reranking|https://www.anthropic.com/news/contextual-retrieval",
 "40 min recorded. Pass = you quote a target retrieval failure rate and name the reranker's latency and dollar cost|https://www.anthropic.com/engineering/multi-agent-research-system",
 "https://www.anthropic.com/news/contextual-retrieval|Reranked Contextual Embedding and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 67% (5.7% to 1.9%)"),

"Design a search engine with LLM synthesis": (
 "Hello Interview &middot; Design Facebook's Post Search - High-Level Design (inverted index) and its four deep dives|" + HI + "problem-breakdowns/fb-post-search",
 "40 min recorded. Pass = classic IR underneath, then synthesis bolted on, and you say aloud why the LLM is NOT in the retrieval path|https://huyenchip.com/2024/07/25/genai-platform.html",
 HI + "problem-breakdowns/fb-post-search|we can create a dictionary which maps keywords to the documents that contain them"),

"Cross-conversation memory": (
 "LangChain &middot; Memory for agents - the semantic/episodic/procedural split, and how to update memory|https://www.langchain.com/blog/memory-for-agents",
 "30 min recorded. Pass = every write placed as hot-path or background, with what each costs the user in latency|https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
 "https://www.langchain.com/blog/memory-for-agents|One way to update agent memory is in the hot path."),

"Then re-do the first two": (
 "r/leetcode &middot; How I would approach System Design prep if I started over - step 3, timer then whiteboard then answer|" + RDLC,
 "Re-do bitly and the rate limiter cold. Pass = both finish inside 25 min with no dead air longer than 10 seconds|" + RDLC,
 RDLC + "|Pick a problem, set a timer, and design it yourself before you check anyone else's answer. This is the step most people skip"),

"The four patterns every prompt maps to": (
 "Anthropic &middot; Building effective agents - Building blocks, workflows and agents, plus When not to use agents|" + AGENTS,
 "Label each of your 13 reps with one line: which pattern, therefore where the deep dive goes. Pass = all 13 labelled before the loop",
 AGENTS + "|we recommend finding the simplest solution possible"),

"Senior signal: reasoning under uncertainty": (
 "Hello Interview &middot; What is Expected at Each Level - the Senior row: breadth, depth, proactiveness|https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level",
 "Score every rep 0-10 on breadth, depth and proactiveness before any lookup. Pass = depth 8+ in exactly 2 places, not 5|https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level",
 "https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level|I want to see you go deep in around 2 places, demonstrating this practical experience."),

"Cost and latency arithmetic out loud": (
 "Hello Interview &middot; Mastering Estimation - How to Estimate Like an Engineer, and Facts to Know|https://www.hellointerview.com/blog/mastering-estimation",
 "Every rep ends with $/1k requests and p95 TTFT said aloud. Pass = both spoken before minute 10, not at the end|https://www.hellointerview.com/blog/mastering-estimation",
 "https://www.hellointerview.com/blog/mastering-estimation|Candidates who proactively estimate seem more experienced and senior than those that don't."),

"The documented mistakes": (
 "Hello Interview &middot; Over-engineering is getting you down-levelled - First, simplify where possible|https://www.hellointerview.com/blog/over-engineering-is-getting-you-down-levelled",
 "Watch each recording at 1.5x with the mistake list on screen. Pass = zero hits on jumping-to-solution and zero on naming-a-tool-without-a-mechanism|https://huyenchip.com/2024/07/25/genai-platform.html",
 "https://www.hellointerview.com/blog/over-engineering-is-getting-you-down-levelled|One of the most common ways to get down-levelled in system design interviews is to over-engineer."),

"huyenchip.com/2024/07/25/genai-platform": (
 "Chip Huyen &middot; Building A Generative AI Platform - steps 1-5: context, guardrails, router/gateway, cache, write actions|https://huyenchip.com/2024/07/25/genai-platform.html",
 "Redraw all five steps from memory in 15 min, twice a week. Pass = every component in the final figure, in build order|https://huyenchip.com/2024/07/25/genai-platform.html",
 "https://huyenchip.com/2024/07/25/genai-platform.html|The order discussed in this post is common, though you don't need to follow the exact same order."),

"anthropic.com/engineering/multi-agent-research-system": (
 "Anthropic &middot; How we built our multi-agent research system - Benefits, Architecture overview, Production reliability|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Write 150 words on when you would REFUSE a multi-agent design. Pass = you cite the token multiple and a shared-context failure|https://www.anthropic.com/engineering/multi-agent-research-system",
 "https://www.anthropic.com/engineering/multi-agent-research-system|There is a downside: in practice, these architectures burn through tokens fast."),

"evidentlyai.com/ml-system-design": (
 "Evidently AI &middot; ML and LLM system design case studies - filter to the Generative AI, LLM, RAG and AI agents tags only|https://www.evidentlyai.com/ml-system-design",
 "Week of the loop, read 5 in your target industry. Pass = 5 sentences of the form: company X does A, we would do B because our constraint is C|https://www.evidentlyai.com/ml-system-design",
 "https://www.evidentlyai.com/ml-system-design|A database of 800 case studies from 150+ companies."),

"uber.com/blog/genai-gateway": (
 "Slack &middot; How We Built Slack AI To Be Secure and Private - the data-access constraint that forced the design|https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/",
 "One page per company naming the single constraint that forced the design. Pass = three different constraints, no overlap|https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/",
 "https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/|Slack AI only operates on the data that the user can already see."),

"hellointerview.com/learn/system-design/in-a-hurry": (
 "Hello Interview &middot; System Design Delivery Framework - the six phases with minute budgets, Requirements to Deep Dives|" + HI + "in-a-hurry/delivery",
 "Recite the six phases and their minute budgets cold before every rep. Pass = correct order and timings, no notes. Do not buy premium for this track|" + HI + "in-a-hurry/delivery",
 RDLC + "|the free material, especially for HLD, is enough to sail in interviews"),

"Excalidraw": (
 "Excalidraw &middot; open it, draw once, stop. Hello Interview names it as the whiteboard to practise on|https://excalidraw.com/",
 "15 min, one file, 8 shapes max. Pass = the timer goes off and you never open it again except to run a rep|" + PREP,
 PREP + "|Either practice with our Guided Practices (below) or on a virtual whiteboard like Excalidraw."),
}
