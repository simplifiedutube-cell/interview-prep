"""Learn / Practise / Evidence for track t01 (CCAR-F — the exam blueprint).

Format: see t03.

Researched Oct 2026 against the live exam guide PDF (v1.0, July 2026, 39pp),
the Partner Academy eligibility page, the certification FAQ and the Pearson VUE
program page. The track's logistics were verified claim by claim and were
almost entirely correct; the corrections that mattered are in the item metas.

Two things worth knowing that are not item-shaped:
  - guide §11 says the reschedule window is 24 hours and the FAQ says 48, three
    times. Assume 48.
  - Pearson lists a 7 Dec 2026 content refresh for CCAO-F, CCDV-F and CCAR-P.
    CCAR-F is NOT on that list, so this v1.0 guide stays authoritative.
"""

GUIDE = ("https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F"
         "6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect"
         "+%E2%80%93+Foundations+Exam+Guide.pdf")
APPENDIX = ("Exam guide &sect;17 Appendix - Out-of-Scope Topics, pp. 37-38, the official "
            "exclusion list|" + GUIDE)
DRIFT = "https://github.com/dnacenta/claude-certified-architect"

DATA = {
# ---- Logistics ------------------------------------------------------------
"Registration requires a partner email": (
 "Partner Academy &sect; Who can take a Claude certification exam - the partner-network eligibility rules|https://anthropic-partners.skilljar.com/page/certification-eligibility",
 "Sign in to the CCAR-F page with your company email. Pass = the Purchase button renders instead of a not-a-partner-employee error|https://anthropic.skilljar.com/claude-certified-architect-foundations-certification",
 "https://anthropic-partners.skilljar.com/page/certification-eligibility|Sign in with a company email on a domain listed in your organization's partner record, because a personal address won't work."),

"Check the partner tier before paying": (
 "Certification FAQ &sect; Pricing and payment - the tier discounts, including the Global Premier window|https://anthropic-partners.skilljar.com/page/faq-certifications",
 "Open checkout and read the price. Pass = $62.50 at Select/Preferred, $0 at Global Premier before 31 Dec 2026, $125 at Registered|https://anthropic.skilljar.com/claude-certified-architect-foundations-certification",
 "https://anthropic-partners.skilljar.com/page/faq-certifications|Through December 31, 2026, Global Premier partners receive a 100% discount on all certification exams."),

"Download the free 39-page exam guide": (
 "Claude Certified Architect - Foundations Exam Guide, v1.0, July 2026, 39pp. Public, no login|" + GUIDE,
 "Against each of the 24 task statements in &sect;6, write one line naming something you have shipped. Pass = 18 or more filled|" + GUIDE,
 "https://anthropic-partners.skilljar.com/page/partner-certifications|~Claude Certified Architect - Foundations $125 USD Prep courses Exam guide Register"),

"Work exam guide §9": (
 "Exam guide &sect;9 Sample Questions - 12 items with full rationales, pp. 26-34, covering 4 of the 6 scenarios|" + GUIDE,
 "Answer all 12 cold, writing which layer you chose and why BEFORE reading the rationale. Pass = 10/12 with your reason matching Anthropic's",
 GUIDE + "|The following sample questions illustrate the format and difficulty level of the exam. These are drawn from the practice test."),

"Work exam guide §8": (
 "Exam guide &sect;8 Preparation Exercises 1-4, pp. 22-25, each labelled with the domains it reinforces|" + GUIDE,
 "Build Exercise 1 end to end. Pass = a hook blocks a refund above $500 and routes to escalate_to_human without touching the prompt",
 GUIDE + "|Complete these hands-on exercises to build practical familiarity with the topics covered on the exam."),

"Pay on Partner Academy, then schedule with Pearson VUE": (
 "Pearson VUE &middot; Anthropic program page - scheduling, OnVUE vs test centre, retake and no-show rules|https://www.pearsonvue.com/us/en/anthropic.html",
 "Run Pearson's OnVUE system test on the machine you will actually sit on, then book. Pass = confirmation email and the date in your Pearson profile|https://www.pearsonvue.com/us/en/anthropic.html",
 "https://www.pearsonvue.com/us/en/anthropic.html|Register at the Anthropic Partner Academy to begin the scheduling process."),

"Know the retake ladder before setting a date": (
 "Exam guide &sect;12 Exam Policies - the retake policy, p. 36|" + GUIDE,
 "Write the four dates your attempts could fall on from your chosen sitting. Pass = attempt 4 still lands inside the same rolling 12 months",
 "https://anthropic-partners.skilljar.com/page/faq-certifications|Waiting periods increase with each failed attempt: 14 days after the first, 30 days after the second, and 90 days after the third."),

"There is no official practice exam": (
 "Certification FAQ &sect; Exam content and prep - the practice exam was retired in the move to Pearson|https://anthropic-partners.skilljar.com/page/faq-certifications",
 "Use &sect;9 as the only authoritative question style. If you buy a third-party mock, treat it as pacing practice only, never as content|" + GUIDE,
 "https://anthropic-partners.skilljar.com/page/faq-certifications|The practice exam available on the previous platform was retired in the move to Pearson."),

# ---- What the pass reports converge on ------------------------------------
"Budget 40–80 hours": (
 "Exam guide &sect;7 How to Prepare - seven build-first directives, p. 21. Worth more than any prep course|" + GUIDE,
 "Timebox a two-week sprint against &sect;7. Pass = all four &sect;8 exercises running, committed, and re-runnable from a clean clone",
 "https://www.reddit.com/r/ClaudeAI/comments/1wzrlxg/i_just_passed_the_claude_certified_architect_prof/|You have to build actual agentic workflows. Reading the docs isn't enough because the test asks you why a specific architecture failed."),

"The exam asks which <i>layer</i> solves the problem": (
 "Exam guide &sect;6 Task 1.4 and 1.5 - programmatic enforcement vs prompt guidance, pp. 8-10|" + GUIDE,
 "Work the Domain 1 practice questions with answers folded until you commit. Pass = you name the layer before reading the options|https://github.com/dnacenta/claude-certified-architect/blob/main/domains/d1-agentic-architecture.md",
 GUIDE + "|When deterministic compliance is required, prompt instructions alone have a non-zero failure rate."),

"Foundations is <i>harder</i> than Professional": (
 "Read the CCAR-P guide beside the CCAR-F one - 11pp vs 39pp, 63 items, five different domains|https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf",
 "Map the two blueprints onto one page. Pass = you can say in a sentence why CCAR-F loads recall and CCAR-P loads judgement",
 "https://www.reddit.com/r/ClaudeAI/comments/1wzrlxg/i_just_passed_the_claude_certified_architect_prof/|Architect Professional (CCAR-P) - The final boss. It assumes you already know the Foundations material and goes deep"),

# ---- Domain 1 -------------------------------------------------------------
"1.1 Agentic loops": (
 "Claude docs &sect; Handle tool calls - the tool_use loop, appending tool_result, and when to stop|https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls",
 "Build a multi-tool agent loop. Pass = two tool iterations before end_turn, and the iteration cap is never what stops it|https://claudecertificationguide.com/learn/1-agentic-architecture/1-1-agentic-loops",
 GUIDE + "|Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps"),

"1.2 Coordinator-subagent orchestration": (
 "Anthropic Engineering &sect; Architecture overview for Research - the orchestrator-worker pattern as actually shipped|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Run the orchestrator-workers cookbook, then make the coordinator skip a worker on a narrow query. Pass = worker count varies with the query|https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/orchestrator_workers.ipynb",
 "https://www.anthropic.com/engineering/multi-agent-research-system|Each subagent also provides separation of concerns - distinct tools, prompts, and exploration trajectories - which reduces path dependency."),

"1.3 Subagent invocation": (
 "Agent SDK docs &sect; Subagents - AgentDefinition, tool restrictions, and passing context explicitly|https://code.claude.com/docs/en/agent-sdk/subagents",
 "Exam guide &sect;8 Exercise 4 step 2: emit two Task calls in one coordinator response. Pass = measured wall-clock beats the sequential run|https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb",
 DRIFT + "/blob/main/domains/d1-agentic-architecture.md|older material (including the exam guide's wording) calls this the Task tool"),

"1.4 Multi-step workflows with enforcement": (
 "Claude Code docs &sect; Get started with hooks - PreToolUse blocking, the prerequisite-gate pattern|https://code.claude.com/docs/en/hooks-guide",
 "Run the human-in-the-loop gate cookbook. Pass = the gated call is refused until approval, with no prompt instruction doing the work|https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb",
 GUIDE + "|blocking process_refund until get_customer has returned a verified customer ID"),

"1.5 Agent SDK hooks": (
 "Agent SDK docs &sect; Hooks - PostToolUse result transformation and the hook JSON shape|https://code.claude.com/docs/en/agent-sdk/hooks",
 "Write a PostToolUse hook. Pass = Unix timestamps and numeric status codes arrive in one normalised shape before the model sees them|https://claudecertificationguide.com/learn/1-agentic-architecture/1-5-agent-sdk-hooks",
 GUIDE + "|Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes)"),

"1.6 Task decomposition strategies": (
 "Anthropic Engineering &sect; Building effective agents - Prompt chaining and Orchestrator-workers|https://www.anthropic.com/engineering/building-effective-agents",
 "Run the dynamic-workflows notebook, then redo it as a fixed chain. Pass = you can state which task each shape is wrong for|https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/08_Dynamic_workflows.ipynb",
 GUIDE + "|prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks"),

"1.7 Session state, resumption and forking": (
 "Claude Code docs &sect; Manage sessions - naming, --resume, branching, and when a fresh session beats resuming|https://code.claude.com/docs/en/sessions",
 "Fork two branches from one analysis baseline. Pass = each is resumable by name after a file change|https://claudecertificationguide.com/learn/1-agentic-architecture/1-7-session-state-resumption",
 "https://code.claude.com/docs/en/cli-reference|--fork-session When resuming, create a new session ID instead of reusing the original"),

# ---- Domain 2 -------------------------------------------------------------
"2.1 Tool interfaces with clear descriptions": (
 "Anthropic Engineering &sect; Prompt-engineering your tool descriptions and &sect; Namespacing your tools|https://www.anthropic.com/engineering/writing-tools-for-agents",
 "Run the tool-evaluation harness twice: two near-identical descriptions, then renamed. Pass = selection accuracy rises measurably|https://github.com/anthropics/claude-cookbooks/blob/main/tool_evaluation/tool_evaluation.ipynb",
 "https://www.anthropic.com/engineering/writing-tools-for-agents|Too many tools or overlapping tools can also distract agents from pursuing efficient strategies."),

"2.2 Structured error responses": (
 "MCP spec 2026-07-28 &sect; Tools &gt; Error Handling - protocol errors vs tool execution errors with isError|https://modelcontextprotocol.io/specification/2026-07-28/server/tools",
 "Give transient, validation, business and permission errors each a distinct errorCategory and isRetryable. Pass = the agent retries only the transient one|https://claudecertificationguide.com/learn/2-tool-design-mcp/2-2-structured-error-responses",
 "https://modelcontextprotocol.io/specification/2026-07-28/server/tools|Clients SHOULD provide tool execution errors to language models to enable self-correction."),

"2.3 Tool distribution across agents": (
 "Anthropic Engineering &sect; Choosing the right tools for agents - why fewer, sharper tools select better|https://www.anthropic.com/engineering/writing-tools-for-agents",
 "Run the tool_choice cookbook through auto, any and a forced name. Pass = you predict each run's behaviour before executing the cell|https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/tool_choice.ipynb",
 GUIDE + "|giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability"),

"2.4 Integrating MCP servers into Claude Code": (
 "Claude Code docs &sect; Connect Claude Code to tools via MCP - the scopes, and .mcp.json env expansion|https://code.claude.com/docs/en/mcp",
 "Exam guide &sect;8 Exercise 2 step 4. Pass = /mcp lists a project server from .mcp.json with ${TOKEN} resolved AND a personal one from ~/.claude.json",
 GUIDE + "|Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets."),

"2.5 The built-in tools": (
 "Claude Code docs &sect; Tools reference - what each tool is for and how its permissions behave|https://code.claude.com/docs/en/tools-reference",
 "Trace a function's callers with Grep then Read. Pass = you fall back to Read plus Write when Edit cannot find a unique anchor|https://claudecertificationguide.com/learn/2-tool-design-mcp/2-5-built-in-tools",
 GUIDE + "|When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications."),

# ---- Domain 3 -------------------------------------------------------------
"3.1 CLAUDE.md files": (
 "Claude Code docs &sect; Choose where to put CLAUDE.md files, and &sect; Import additional files|https://code.claude.com/docs/en/memory",
 "Build user, project and directory CLAUDE.md plus one @import. Pass = /context lists all four in load order|https://code.claude.com/docs/en/memory",
 "https://code.claude.com/docs/en/memory|CLAUDE.md files can live in several locations, each with a different scope. The table below lists them in load order"),

"3.2 Custom slash commands and skills": (
 "Claude Code docs &sect; Extend Claude with skills - SKILL.md frontmatter, context: fork, allowed-tools, argument-hint|https://code.claude.com/docs/en/skills",
 "Build a context: fork skill. Pass = its verbose output never appears in the parent transcript|https://claudecertificationguide.com/learn/3-claude-code-config/3-2-slash-commands-skills",
 GUIDE + "|The context: fork frontmatter option for running skills in an isolated sub-agent context"),

"3.3 Path-specific rules": (
 "Claude Code docs &sect; Organize rules with .claude/rules/ - path-specific rules and the paths frontmatter field|https://code.claude.com/docs/en/memory",
 "Exam guide &sect;8 Exercise 2 step 2. Pass = a rule with paths **/*.test.* is absent from /context until you open a test file, then present",
 "https://code.claude.com/docs/en/memory|Rules can be scoped to specific files using YAML frontmatter with the paths field."),

"3.4 Plan mode vs direct execution": (
 "Claude Code docs &sect; Choose a permission mode - analyze before you edit with plan mode|https://code.claude.com/docs/en/permission-modes",
 "Call it right on three cases: a one-file fix, a 45-file migration, and a feature with competing approaches. Pass = 3 of 3|https://claudecertificationguide.com/learn/3-claude-code-config/3-4-plan-mode-execution",
 "https://code.claude.com/docs/en/best-practices|Letting Claude jump straight to coding can produce code that solves the wrong problem."),

"3.5 Iterative refinement": (
 "Claude Code docs &sect; Let Claude interview you, and &sect; Course-correct early and often|https://code.claude.com/docs/en/best-practices",
 "Take a prose spec that failed twice and supply three input/output pairs. Pass = it succeeds, and you batch interacting fixes into one message|https://claudecertificationguide.com/learn/3-claude-code-config/3-5-iterative-refinement",
 "https://code.claude.com/docs/en/best-practices|For larger features, have Claude interview you first. Start with a minimal prompt and ask Claude to interview you"),

"3.6 Claude Code in CI/CD": (
 "Claude Code docs &sect; Run Claude Code programmatically - -p, --output-format json, --json-schema|https://code.claude.com/docs/en/headless",
 "Run claude -p with a --json-schema in a GitHub Action against a seeded bug. Pass = the job posts an inline PR comment from validated JSON|https://code.claude.com/docs/en/github-actions",
 "https://code.claude.com/docs/en/cli-reference|--json-schema Get validated JSON output matching a JSON Schema after the agent completes its workflow (print mode only)."),

"Do this by building, not reading": (
 "Exam guide &sect;8 Exercise 2, Configure Claude Code for a Team Development Workflow - five steps, p. 23|" + GUIDE,
 "Do this FIRST in the whole track, in one real repo, in an afternoon. Pass = /context shows the CLAUDE.md chain, the path rule, the forked skill and both MCP scopes",
 GUIDE + "|Verify the skill runs in isolation without polluting the main conversation context."),

# ---- Domain 4 -------------------------------------------------------------
"4.1 Explicit criteria to reduce false positives": (
 "Claude Code docs &sect; Customize code review - what Important means here, Do not report, Always check|https://code.claude.com/docs/en/code-review-customize",
 "Replace a be-conservative instruction with categorical rules. Pass = your measured false-positive count drops|https://claudecertificationguide.com/learn/4-prompt-engineering/4-1-system-prompts",
 "https://code.claude.com/docs/en/code-review-customize|require evidence before a class of finding is posted. For example, behavior claims need a file:line citation"),

"4.2 Few-shot prompting": (
 "Claude docs &sect; Use examples (multishot prompting) - how many, and how to choose the ambiguous ones|https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting",
 "Pit 2-4 examples covering the ambiguous cases against a longer prose instruction. Pass = the examples win on a held-out set|https://claudecertificationguide.com/learn/4-prompt-engineering/4-2-few-shot-prompting",
 GUIDE + "|Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen"),

"4.3 Structured output via tool use": (
 "Claude docs &sect; Structured outputs - what schema-guaranteed output does, and what it does NOT guarantee|https://platform.claude.com/docs/en/build-with-claude/structured-outputs",
 "Run the structured-JSON extraction cookbook on a document missing two fields. Pass = nullable fields come back null rather than fabricated|https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/extracting_structured_json.ipynb",
 GUIDE + "|strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors"),

"4.4 Validation, retry and feedback loops": (
 "Exam guide &sect;6 Task 4.4 - retry-with-error-feedback, and when retries cannot work, p. 17|" + GUIDE,
 "Build the Pydantic validate-and-retry loop, then feed it a document missing the field. Pass = you stop retrying instead of looping|https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/tool_use_with_pydantic.ipynb",
 GUIDE + "|retries are ineffective when the required information is simply absent from the source document"),

"4.5 Batch processing": (
 "Claude docs &sect; Message Batches - 50% discount, 24-hour window, no latency SLA, custom_id, limits|https://platform.claude.com/docs/en/build-with-claude/batch-processing",
 "Submit 100 requests, fail some deliberately, resubmit by custom_id. Pass = only the failures go back, and you can compute the SLA window|https://github.com/anthropics/claude-cookbooks/blob/main/misc/batch_processing.ipynb",
 GUIDE + "|The batch API does not support multi-turn tool calling within a single request"),

"4.6 Multi-instance and multi-pass review": (
 "Claude Code docs &sect; Add an adversarial review step - why a fresh reviewer context beats self-review|https://code.claude.com/docs/en/best-practices",
 "Pass = an independent reviewer finds a defect that both the generating session AND extended thinking missed|https://claudecertificationguide.com/learn/4-prompt-engineering/4-6-multi-pass-review",
 "https://code.claude.com/docs/en/best-practices|A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change."),

# ---- Domain 5 -------------------------------------------------------------
"5.1 Context across long interactions": (
 "Anthropic Engineering &sect; Context engineering for long-horizon tasks - compaction, note-taking, attention budget|https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
 "Pass = a persistent case-facts block survives summarisation with every amount, date and order number intact|https://claudecertificationguide.com/learn/5-context-management/5-1-context-window-management",
 "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents|Context, therefore, must be treated as a finite resource with diminishing marginal returns."),

"5.2 Escalation and ambiguity resolution": (
 "Exam guide &sect;6 Task 5.2 - the three valid triggers and the two unreliable proxies, p. 19|" + GUIDE,
 "Pass = an angry-but-simple request resolves, an explicit human request escalates at once, and two customer matches triggers an identifier question|https://claudecertificationguide.com/learn/5-context-management/5-2-escalation-ambiguity",
 GUIDE + "|Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity"),

"5.3 Error propagation": (
 "Anthropic Engineering &sect; Production reliability and engineering challenges - stateful agents and compounding errors|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Exam guide &sect;8 Exercise 4 step 4. Pass = a simulated subagent timeout returns failure type, attempted query and partial results, and the run finishes with a coverage-gap note",
 "https://www.anthropic.com/engineering/multi-agent-research-system|Agents are stateful and errors compound."),

"5.4 Context in large codebase exploration": (
 "Claude Code docs &sect; Set up Claude Code in a monorepo or large codebase - scoping, delegation, scratchpads|https://code.claude.com/docs/en/large-codebases",
 "Run the explore-unfamiliar-codebase agent. Pass = a resumed session answers from the scratchpad, not from typical patterns|https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_explore_unfamiliar_codebase.ipynb",
 "https://code.claude.com/docs/en/best-practices|Since context is your fundamental constraint, use subagents to keep research out of it."),

"5.5 Human review workflows": (
 "Anthropic Engineering &sect; Effective evaluation of agents - why aggregate numbers mislead, and how they sampled|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Build an eval that scores by document type, not overall. Pass = you surface a segment under 70% hiding inside a 97% aggregate|https://github.com/anthropics/claude-cookbooks/blob/main/misc/building_evals.ipynb",
 GUIDE + "|The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types"),

"5.6 Provenance and uncertainty": (
 "Claude docs &sect; Citations - carrying claim-to-source mappings through a pipeline|https://platform.claude.com/docs/en/build-with-claude/citations",
 "Exam guide &sect;8 Exercise 4 step 5. Pass = two conflicting statistics both survive synthesis with source AND publication date, neither silently dropped",
 GUIDE + "|require publication dates so a temporal difference isn't read as a contradiction"),

# ---- The 6 scenarios ------------------------------------------------------
"Customer Support Resolution Agent": (
 "Claude docs &sect; Use case guide - Customer support chat, backend tool integration and resolution targets|https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat",
 "Run the customer-service-agent cookbook, add escalate_to_human and a refund threshold hook. Pass = a $600 refund escalates with a structured handoff|https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/customer_service_agent.ipynb",
 GUIDE + "|Your target is 80%+ first-contact resolution while knowing when to escalate."),

"Code Generation with Claude Code": (
 "Anthropic Academy &sect; Claude Code in Action - the Configure Claude module: CLAUDE.md, skills, permission modes, hooks|https://anthropic.skilljar.com/claude-code-in-action",
 "Take the end-of-course quiz. Pass = certificate of completion issued|https://anthropic.skilljar.com/claude-code-in-action",
 GUIDE + "|~Primary domains: Claude Code Configuration & Workflows, Context Management & Reliability"),

"Multi-Agent Research System": (
 "Anthropic Engineering &middot; How we built our multi-agent research system - the whole post, Appendix included|https://www.anthropic.com/engineering/multi-agent-research-system",
 "Extend the one-liner research agent into a coordinator plus search and synthesis subagents. Pass = synthesis cites sources it never fetched itself|https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/00_The_one_liner_research_agent.ipynb",
 "https://www.anthropic.com/engineering/multi-agent-research-system|Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources"),

"Developer Productivity with Claude": (
 "Claude Code docs &sect; Common workflows - exploring unfamiliar code, legacy systems, repetitive automation|https://code.claude.com/docs/en/common-workflows",
 "Over-prepare this one: it spans three domains and has the least dedicated material. Pass = the Academy MCP final assessment passed|https://anthropic.skilljar.com/introduction-to-model-context-protocol",
 GUIDE + "|It uses the built-in tools (Read, Write, Bash, Grep, Glob) and integrates with Model Context Protocol (MCP) servers."),

"Claude Code for Continuous Integration": (
 "Claude Code docs &sect; Code review on pull requests - what runs, and where the review criteria come from|https://code.claude.com/docs/en/code-review-pull-requests",
 "Wire the action onto a repo with a seeded bug and a REVIEW.md. Pass = one inline comment on the bug and none in your do-not-report categories|https://code.claude.com/docs/en/github-actions",
 GUIDE + "|You need to design prompts that provide actionable feedback and minimize false positives."),

"Structured Data Extraction": (
 "Claude docs &sect; Define tools - schema design, required vs optional, and the enum patterns|https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools",
 "Exam guide &sect;8 Exercise 3, all five steps - the highest-yield single build in the track. Pass = nulls not fabrications, a retry loop that stops, 100 reconciled by custom_id",
 GUIDE + "|Process documents where some fields are absent and verify the model returns null rather than fabricating values."),

# ---- Free official prep ---------------------------------------------------
"Claude Code in Action": (
 "Anthropic Academy &middot; Claude Code in Action - four modules: Steer, Configure, Automate, Verify and Share|https://anthropic.skilljar.com/claude-code-in-action",
 "Course quiz at the end of Verify and Share. Pass = certificate of completion issued|https://anthropic.skilljar.com/claude-code-in-action",
 "https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses|Complete these free courses to help prepare yourself for the Claude Certified Architect - Foundations certification exam."),

"Claude Code 101": (
 "Skip it. Beginner material by its own description, not on the official prep list, and fully covered by Claude Code in Action|https://anthropic.skilljar.com/claude-code-101",
 "Spend the hours on exam guide &sect;8 Exercise 2 instead|" + GUIDE,
 "https://anthropic.skilljar.com/claude-code-101|designed for developers who are either new to software engineering or experienced engineers who haven't yet explored AI coding agents"),

"Introduction to Model Context Protocol": (
 "Anthropic Academy &middot; Introduction to MCP - Defining tools and Defining resources, in the Python SDK|https://anthropic.skilljar.com/introduction-to-model-context-protocol",
 "Final assessment on MCP. Pass = assessment passed and certificate issued|https://anthropic.skilljar.com/introduction-to-model-context-protocol",
 "https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses|Master MCP's three core primitives - tools, resources, and prompts"),

"Model Context Protocol: Advanced Topics": (
 "Mostly out of scope. Sampling, notifications, roots and transports appear nowhere in the CCAR-F blueprint|https://anthropic.skilljar.com/model-context-protocol-advanced-topics",
 "Watch only if your time is free. The guide's appendix explicitly excludes MCP hosting and infrastructure|" + GUIDE,
 "https://anthropic.skilljar.com/model-context-protocol-advanced-topics|~focusing on server-client communication, transport mechanisms"),

"Introduction to agent skills": (
 "Anthropic Academy &middot; Introduction to agent skills - Configuration and multi-file skills, plus Skills vs other features|https://anthropic.skilljar.com/introduction-to-agent-skills",
 "Build the course's skill with allowed-tools restricted. Pass = a disallowed tool call is refused inside the skill|https://anthropic.skilljar.com/introduction-to-agent-skills",
 "https://anthropic.skilljar.com/introduction-to-agent-skills|advanced configuration options like restricting tool access with allowed-tools and using scripts that execute without consuming context"),

"Introduction to subagents": (
 "Anthropic Academy &middot; Introduction to subagents - Designing effective subagents: structured output, obstacle reporting, tool limits|https://anthropic.skilljar.com/introduction-to-subagents",
 "Build a reviewer subagent with a structured output contract. Pass = the parent context receives only the summary, not the exploration|https://anthropic.skilljar.com/introduction-to-subagents",
 "https://anthropic.skilljar.com/introduction-to-subagents|They let you delegate tasks to isolated assistants that do their work separately and return just the information you need"),

"Building with the Claude API": (
 "Anthropic Academy &middot; Building with the Claude API - the Tool use and Prompt evaluation sections only|https://anthropic.skilljar.com/claude-with-the-anthropic-api",
 "Exercise on prompt evals, then the quiz. Pass = both quizzes passed. Skip the Temperature and Streaming lessons, they are out of scope|https://anthropic.skilljar.com/claude-with-the-anthropic-api",
 "https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses|This comprehensive course covers the full spectrum of working with Anthropic models using the Claude API"),

"These are <i>certificates of completion</i>": (
 "Partner Academy &sect; Certificates of completion and certifications - the distinction, stated officially|https://anthropic-partners.skilljar.com/page/certification-eligibility",
 "Say out loud what goes on LinkedIn. Pass = only the Credly badge from a passed Pearson VUE exam, never a course certificate",
 "https://anthropic-partners.skilljar.com/page/certification-eligibility|A Claude Academy certificate of completion records that you finished a course and passed its quiz. A Claude certification is a proctored exam"),

# ---- Explicitly out of scope ----------------------------------------------
"Fine-tuning · Claude's internal architecture": (
 APPENDIX,
 "Delete these from your notes. Pass = nothing in your revision file mentions fine-tuning, weights, RLHF or Constitutional AI",
 GUIDE + "|Fine-tuning Claude models or training custom models"),

"Embedding models and vector DB implementation": (
 APPENDIX,
 "Skip every RAG and embeddings notebook in the cookbook. Pass = you open none of them while revising for this exam",
 GUIDE + "|Embedding models or vector database implementation details"),

"Deploying or hosting MCP servers": (
 APPENDIX,
 "Keep your MCP work local over stdio. Pass = you configure servers in .mcp.json and never containerise or deploy one",
 GUIDE + "|Deploying or hosting MCP servers (infrastructure, networking, container orchestration)"),

"Computer use · vision and image analysis": (
 APPENDIX,
 "Skip the Streaming and multimodal lessons in Building with the Claude API. Pass = you still pass that course's quizzes",
 GUIDE + "|Computer use (browser automation, desktop interaction) / Vision/image analysis capabilities"),

"API auth, billing and account management": (
 APPENDIX,
 "Do not revise pricing tables. Pass = the only cost arithmetic you practise is the 4.5 batch SLA window, which IS in scope",
 GUIDE + "|Rate limiting, quotas, or API pricing calculations / OAuth, API key rotation, or authentication protocol details"),

"Prompt caching implementation detail": (
 APPENDIX,
 "Write one sentence on what prompt caching is for. Pass = you can say it, and then stop reading about it",
 GUIDE + "|Prompt caching implementation details (beyond knowing it exists)"),
}
