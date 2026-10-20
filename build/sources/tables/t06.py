"""Learn / Practise / Evidence for track t06 (Agents, tools & MCP). Format: see t03.

Researched Oct 2026 against MCP spec revision 2026-07-28, whose changelog was
read directly. That revision is a breaking one and it invalidates a lot of
2025 writing: protocol sessions and Mcp-Session-Id are gone, the
initialize/notifications/initialized handshake is gone, server/discover is
mandatory, SSE resumability is gone, and Roots, Sampling and Logging are all
Deprecated under SEP-2577. Anything teaching the handshake is now wrong rather
than merely dated - including the Hugging Face MCP course, which is why no
item here points at it.
"""

DATA = {
# ---- Agent architecture ---------------------------------------------------
"The five patterns, and which problem each fits": (
 "Anthropic &middot; Building effective agents &sect; Building blocks, workflows, and agents - all five, each with a When-to-use|https://www.anthropic.com/engineering/building-effective-agents",
 "Run the cookbook notebooks, then rebuild basic_workflows.ipynb from scratch. Pass = the chain, route and parallel traces differ|https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents",
 "https://www.anthropic.com/engineering/building-effective-agents|we'll start with our foundational building block - the augmented LLM - and progressively increase complexity"),

"What lives in the orchestrator vs what lives in the model": (
 "12-Factor Agents &sect; Factor 8 'Own your control flow' - three concrete intents that break the loop vs stay in it|https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md",
 "Move one routing decision out of your LangGraph prompt into a conditional edge. Pass = the prompt no longer names any node|https://docs.langchain.com/oss/python/langgraph/graph-api",
 "https://www.reddit.com/r/LangChain/comments/1wmafge/langgraph_vs_crewai_for_multiagent_handoffs_which/|For complicated systems I'd keep autonomy inside the nodes and make the edges deterministic."),

"How an agent chooses a tool": (
 "Anthropic &middot; Writing effective tools for agents &sect; namespacing and prompt-engineering tool descriptions (Sep 2025)|https://www.anthropic.com/engineering/writing-tools-for-agents",
 "Build a 20-tool eval and rename pairs prefix- vs suffix-namespaced. Pass = you can show selection accuracy moving|https://www.anthropic.com/engineering/writing-tools-for-agents",
 "https://www.anthropic.com/engineering/writing-tools-for-agents|namespacing tools by service (e.g., asana_search, jira_search) and by resource ... can help agents select the right tools"),

"Tool failure: retries, idempotency keys": (
 "Marc Brooker &middot; Fixing retries with token buckets and circuit breakers - the retry token bucket, with simulation numbers|https://brooker.co.za/blog/2022/02/28/retries.html",
 "Put a retry token bucket in front of one flaky tool and drive it to 100% failure. Pass = total work stays bounded, not 1+N times|https://brooker.co.za/blog/2022/02/28/retries.html",
 "https://www.reddit.com/r/LangChain/comments/1wmafge/langgraph_vs_crewai_for_multiagent_handoffs_which/|the idempotency key has to commit in the same transaction as the write, otherwise a retry that dies between the two still doubles it"),

"Detecting and stopping infinite planning loops": (
 "12-Factor Agents &sect; Factor 7 'Contact humans with tools' - a request_human_input tool as the loop's real exit|https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md",
 "Replace max_iterations with a harness-captured check gate. Pass = a run that skipped the tests is marked not-done regardless of the model's summary|https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md",
 "https://www.reddit.com/r/AI_Agents/comments/1x3tklw/looping_agents/|stop judging the output and start judging evidence the agent cannot fake ... If the checks did not run, the task is not done"),

"When is an agent the wrong solution?": (
 "Anthropic &middot; Building effective agents &sect; When (and when not) to use agents, plus When and how to use frameworks|https://www.anthropic.com/engineering/building-effective-agents",
 "Take one shipped jobagent feature and rebuild it as a fixed workflow. Pass = you can state the latency, cost and accuracy deltas as numbers|https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents",
 "https://www.anthropic.com/engineering/building-effective-agents|for many applications, optimizing single LLM calls with retrieval and in-context examples is usually enough"),

"Multi-agent coordination, and its honest cost": (
 "Anthropic &middot; How we built our multi-agent research system &sect; Benefits of a multi-agent system - the 90.2% win and the token cost|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Run the same brief single-agent and orchestrator-workers, logging tokens both ways. Pass = you can name your own multiplier|https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents",
 "https://www.anthropic.com/engineering/multi-agent-research-system|agents typically use about 4x more tokens than chat interactions, and multi-agent systems use about 15x more tokens than chats"),

"Agent memory: scratchpads, summarisation": (
 "Anthropic &middot; Effective context engineering &sect; long-horizon techniques - compaction, structured note-taking, sub-agents|https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
 "Add a LangGraph checkpointer and resume a 12-step run from step 3. Pass = the next node reads the earlier decision out of graph state|https://docs.langchain.com/oss/python/langgraph/persistence",
 "https://www.reddit.com/r/LangChain/comments/1wmafge/langgraph_vs_crewai_for_multiagent_handoffs_which/|I'd treat graph state as the canonical handoff record, not just natural language transcript."),

"Context engineering as a named discipline": (
 "Anthropic &middot; Effective context engineering &sect; Context engineering vs prompt engineering, and the attention-budget framing|https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
 "Instrument one run's token split across system, tools, MCP and history. Pass = cut 30% with no accuracy drop on your eval|https://www.anthropic.com/engineering/code-execution-with-mcp",
 "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents|Context, therefore, must be treated as a finite resource with diminishing marginal returns."),

# ---- MCP, at spec depth ---------------------------------------------------
"The primitive control model": (
 "MCP docs &middot; Understanding MCP servers &sect; Core Server Features - the who-controls-it table for tools / resources / prompts|https://modelcontextprotocol.io/docs/latest/learn/server-concepts",
 "Expose the same data as a tool, a resource and a prompt on one server. Pass = you can say which of the three a client surfaces without the model asking|https://github.com/modelcontextprotocol/servers/tree/main/src/everything",
 "https://modelcontextprotocol.io/specification/2026-07-28/changelog|Deprecate the Roots, Sampling, and Logging features ... new implementations should not add support for them"),

"Transports: stdio vs Streamable HTTP": (
 "MCP spec &middot; Key Changes for 2026-07-28 - the stateless rewrite, then the stdio and Streamable HTTP bindings|https://modelcontextprotocol.io/specification/2026-07-28/changelog",
 "Run one server over both bindings via Inspector CLI. Pass = tools/list succeeds on each with no Mcp-Session-Id anywhere|https://modelcontextprotocol.io/docs/latest/tools/inspector/cli",
 "https://modelcontextprotocol.io/specification/2026-07-28/changelog|Make MCP stateless: remove the initialize/notifications/initialized handshake. Every request now carries its protocol version"),

"Tool schema design, and the <code>isError</code> convention": (
 "MCP spec &middot; Tools &gt; Error Handling - protocol errors vs tool execution errors, and when isError true is correct|https://modelcontextprotocol.io/specification/latest/server/tools",
 "Return a bad date two ways: as JSON-RPC -32602, and as isError true with a corrective message. Pass = only the second gets self-corrected|https://modelcontextprotocol.io/docs/latest/tools/inspector/cli",
 "https://modelcontextprotocol.io/specification/latest/server/tools|Clients SHOULD provide tool execution errors to language models to enable self-correction."),

"Resources vs tools": (
 "MCP spec &middot; Resources - the application-driven model, resource templates, and the new ttlMs / cacheScope fields|https://modelcontextprotocol.io/specification/latest/server/resources",
 "Replace a list_items tool with a resource plus template URI. Pass = a cold client gets the catalog in one resources/list and zero tool calls|https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem",
 "https://modelcontextprotocol.io/specification/latest/server/resources|Resources in MCP are designed to be application-driven, with host applications determining how to incorporate context"),

"Server configuration and scope": (
 "Claude Code MCP docs &sect; Environment variable expansion in .mcp.json, and the project/user/local scope precedence|https://code.claude.com/docs/en/mcp",
 "Commit a .mcp.json using ${VAR:-default} and Bearer ${API_KEY}. Pass = an unset var gives a named warning and a credential var gives a 401|https://code.claude.com/docs/en/mcp",
 "https://code.claude.com/docs/en/mcp|~Environment variables can be expanded in .mcp.json using ${VAR} and ${VAR:-default} syntax"),

"MCP-specific attack classes": (
 "Invariant Labs &middot; Tool poisoning attacks - where rug pull, tool shadowing and tool poisoning as terms actually come from|https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks",
 "Hide an instruction in a tool description on your own server and connect it alongside a trusted one. Pass = you can show it overriding the trusted tool|https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices",
 "https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks|a malicious server cannot only exfiltrate sensitive data from the user but also hijack the agent's behavior"),

"Build one: a 3-tool MCP server": (
 "MCP docs &middot; Build an MCP server, pinned to /docs/latest - the weather server, then the resources and prompts additions|https://modelcontextprotocol.io/docs/latest/develop/build-server",
 "Build it, then verify headlessly: Inspector CLI --method tools/list, resources/list and prompts/get must all exit 0 before you wire a client|https://modelcontextprotocol.io/docs/latest/tools/inspector/cli",
 "https://modelcontextprotocol.io/docs/latest/tools/inspector/cli|~Each CLI run connects to a server, invokes the single request you name with --method, prints the result, and exits."),

"Debugging: why anything written to stdout": (
 "MCP spec &middot; stdio binding - the server MUST NOT write anything to stdout that is not a valid MCP message; stderr is for logging|https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio",
 "Add a stray print to a working stdio server, confirm the client breaks, move it to stderr. Pass = tools/list recovers with the log still visible|https://modelcontextprotocol.io/docs/latest/tools/debugging",
 "https://www.reddit.com/r/mcp/comments/1wqqq3s/heads_up_if_a_stdio_mcp_server_suddenly_shows/|the server connects and the client shows it green with zero tools, so you go looking at your own config first"),

# ---- Safety and injection -------------------------------------------------
"Prompt injection — direct, and indirect": (
 "Simon Willison &middot; The lethal trifecta for AI agents - private data plus untrusted content plus external communication|https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/",
 "Run AgentChaos against your own server twice, once with a working egress path and once without. Pass = you report both numbers separately|https://www.reddit.com/r/mcp/comments/1wfv39d/agentchaos_testing_prompt_injection_in_mcp_and/",
 "https://www.reddit.com/r/mcp/comments/1wfv39d/agentchaos_testing_prompt_injection_in_mcp_and/|marking results untrusted by default is right, but on its own it mostly changes the prompt"),

"Sandboxing tool execution": (
 "MCP docs &middot; Local Server Security - what a stdio server actually inherits, and the client/server shared trust domain|https://modelcontextprotocol.io/docs/latest/tutorials/security/local-server-security",
 "Audit your own client config, remove unused servers, pin every version. Pass = you can name each remaining server's origin and pinned version|https://modelcontextprotocol.io/docs/latest/tutorials/security/local-server-security",
 "https://modelcontextprotocol.io/docs/latest/tutorials/security/local-server-security|That process inherits your environment variables, can read anything your account can read - SSH keys, cloud credentials, browser profiles"),

"Human-in-the-loop gates for irreversible operations": (
 "12-Factor Agents &sect; Factor 7 - deploy_backend as a high-stakes intent that breaks the loop and waits for approval|https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-07-contact-humans-with-tools.md",
 "Add a LangGraph interrupt before one irreversible write and resume on approve. Pass = the deny path leaves zero side effects behind|https://docs.langchain.com/oss/python/langgraph/interrupts",
 "https://modelcontextprotocol.io/specification/latest/server/tools|there SHOULD always be a human in the loop with the ability to deny tool invocations"),

# ---- Read these, in date order --------------------------------------------
"Anthropic engineering — the five-post arc": (
 "Anthropic &middot; Demystifying evals for AI agents (Jan 2026) - the task / trial / grader vocabulary, newest in the arc|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "Write 10 tasks with graders for one jobagent flow, 3 trials each. Pass = your pass rate moves under 10 points across repeat runs|https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
 "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents|A grader is logic that scores some aspect of the agent's performance. A task can have multiple graders"),

"modelcontextprotocol.io": (
 "MCP spec &middot; Key Changes for 2026-07-28 - start here, not the Overview, which hides the breaking parts|https://modelcontextprotocol.io/specification/2026-07-28/changelog",
 "Read the deprecated-features registry and list what your own servers still use. Pass = you can name each feature's migration path and earliest removal|https://modelcontextprotocol.io/specification/2026-07-28/deprecated",
 "https://modelcontextprotocol.io/specification/2026-07-28/changelog|Remove protocol-level sessions and the Mcp-Session-Id header from the Streamable HTTP transport"),

"NirDiamant/GenAI_Agents": (
 "all_agents_tutorials/agent_while_loop_from_scratch.ipynb - the no-framework loop, the one notebook worth reading closely|https://github.com/NirDiamant/GenAI_Agents/tree/main/all_agents_tutorials",
 "Pick three notebooks naming patterns you have not built, port one to the Anthropic SDK. Pass = it runs with no LangChain imports|https://github.com/NirDiamant/GenAI_Agents/tree/main/all_agents_tutorials",
 "https://github.com/NirDiamant/GenAI_Agents|~one of the most extensive and dynamic collections of Generative AI agent tutorials and implementations available today"),

"Lilian Weng — LLM Powered Autonomous Agents": (
 "Lilian Weng &middot; LLM Powered Autonomous Agents - the planning / memory / tool-use decomposition interview questions are built on|https://lilianweng.github.io/posts/2023-06-23-agent/",
 "Map your own agent onto her three components and name what you have no equivalent of. Pass = you defend each gap as a deliberate choice|https://lilianweng.github.io/posts/2023-06-23-agent/",
 "https://lilianweng.github.io/posts/2023-06-23-agent/|~Component One: Planning ... Component Two: Memory ... Component Three: Tool Use"),

"The ReAct paper": (
 "Yao et al. &middot; ReAct: Synergizing Reasoning and Acting in Language Models, arXiv:2210.03629|https://arxiv.org/abs/2210.03629",
 "Hand-roll a ReAct loop against a scripted fake search tool, no framework. Pass = a tool error is recovered from in the next thought|https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/lib/tools/_tool_dispatch.py",
 "https://arxiv.org/abs/2210.03629|reasoning traces help the model induce, track, and update action plans as well as handle exceptions"),

"Know LangGraph and CrewAI by name": (
 "r/LangChain &middot; LangGraph vs CrewAI handoffs - the checkpoint-replays-the-write failure, and the fix|https://www.reddit.com/r/LangChain/comments/1wmafge/langgraph_vs_crewai_for_multiagent_handoffs_which/",
 "Kill a node after its DB write and resume from checkpoint. Pass = run_id + node_id as an idempotency key stops the double write|https://docs.langchain.com/oss/python/langgraph/persistence",
 "https://www.reddit.com/r/LangChain/comments/1wmafge/langgraph_vs_crewai_for_multiagent_handoffs_which/|LangGraph re-enters the node from the old checkpoint, so agent B writes twice unless you check the db or an idempotency key"),
}
