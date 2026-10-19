import os
import subprocess
import json

book_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Claude Certified Architect – Foundations (CCAR-F) Master Book</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap');

  @page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Inter', sans-serif;
      font-size: 8pt;
      color: #888;
    }
    @bottom-left {
      content: "Claude Certified Architect – Foundations (CCAR-F) Master Guide";
      font-family: 'Inter', sans-serif;
      font-size: 8pt;
      color: #888;
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    background: #ffffff;
    line-height: 1.6;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4 {
    color: #0f172a;
    font-weight: 700;
    line-height: 1.25;
    page-break-after: avoid;
  }

  h1 {
    font-size: 20pt;
    margin-top: 0;
    margin-bottom: 12pt;
    padding-bottom: 6pt;
    border-bottom: 2px solid #e2e8f0;
  }

  h2 {
    font-size: 14pt;
    margin-top: 18pt;
    margin-bottom: 8pt;
    color: #1e293b;
  }

  h3 {
    font-size: 11pt;
    margin-top: 12pt;
    margin-bottom: 4pt;
    color: #334155;
  }

  p {
    margin-top: 0;
    margin-bottom: 8pt;
    text-align: justify;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 8pt;
    padding-left: 18pt;
  }

  li {
    margin-bottom: 3pt;
  }

  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    padding: 1.5pt 3.5pt;
    border-radius: 3pt;
    color: #c15f3c;
    border: 1px solid #e2e8f0;
  }

  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 10pt 12pt;
    border-radius: 6pt;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
    line-height: 1.45;
    overflow-x: auto;
    page-break-inside: avoid;
    margin-top: 6pt;
    margin-bottom: 10pt;
    border: 1px solid #1e293b;
  }

  pre code {
    background: transparent;
    padding: 0;
    border: none;
    color: inherit;
    font-size: inherit;
  }

  .cover-page {
    page-break-after: always;
    min-height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 40pt 20pt 20pt 20pt;
    border-bottom: 4px solid #d97757;
  }

  .cover-badge {
    display: inline-block;
    background: #fff1eb;
    color: #c15f3c;
    border: 1px solid #f97316;
    font-size: 9pt;
    font-weight: 700;
    letter-spacing: 0.05em;
    padding: 4pt 10pt;
    border-radius: 20pt;
    text-transform: uppercase;
    margin-bottom: 16pt;
  }

  .cover-title {
    font-size: 28pt;
    font-weight: 800;
    line-height: 1.15;
    color: #0f172a;
    margin-bottom: 8pt;
    border-bottom: none;
    padding: 0;
  }

  .cover-subtitle {
    font-size: 13pt;
    font-weight: 400;
    color: #475569;
    margin-bottom: 24pt;
    line-height: 1.5;
  }

  .cover-meta {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8pt;
    padding: 14pt 18pt;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12pt;
    margin-bottom: 30pt;
  }

  .cover-meta-item strong {
    display: block;
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #64748b;
    margin-bottom: 2pt;
  }

  .cover-meta-item span {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
  }

  .cover-footer {
    border-top: 1px solid #e2e8f0;
    padding-top: 16pt;
    font-size: 8.5pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
  }

  .chapter-break {
    page-break-before: always;
    padding-top: 10pt;
  }

  .domain-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10pt;
    padding-bottom: 6pt;
    border-bottom: 2px solid #e2e8f0;
  }

  .domain-weight {
    background: #d97757;
    color: #ffffff;
    font-weight: 700;
    font-size: 8.5pt;
    padding: 3pt 8pt;
    border-radius: 12pt;
  }

  .callout {
    border-radius: 6pt;
    padding: 9pt 12pt;
    margin-top: 8pt;
    margin-bottom: 10pt;
    page-break-inside: avoid;
    font-size: 9pt;
    border-left: 4px solid;
  }

  .callout-note {
    background: #f0f9ff;
    border-left-color: #0284c7;
    color: #0c4a6e;
  }

  .callout-warning {
    background: #fef2f2;
    border-left-color: #ef4444;
    color: #991b1b;
  }

  .callout-tip {
    background: #f0fdf4;
    border-left-color: #22c55e;
    color: #166534;
  }

  .callout-exam {
    background: #fffbeb;
    border-left-color: #f59e0b;
    color: #92400e;
  }

  .callout-title {
    font-weight: 700;
    margin-bottom: 3pt;
    display: flex;
    align-items: center;
    gap: 5pt;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 6pt;
    margin-bottom: 12pt;
    font-size: 8.5pt;
    page-break-inside: avoid;
  }

  th, td {
    padding: 5pt 7pt;
    text-align: left;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }

  th {
    background: #f8fafc;
    font-weight: 600;
    color: #0f172a;
  }

  tr:nth-child(even) td {
    background: #fbfcfe;
  }

  .scenario-card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6pt;
    padding: 10pt 12pt;
    margin-bottom: 10pt;
    page-break-inside: avoid;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }

  .scenario-card h3 {
    margin-top: 0;
    color: #d97757;
    font-size: 10.5pt;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .scenario-badge {
    font-size: 7.5pt;
    padding: 2pt 6pt;
    background: #f1f5f9;
    border-radius: 4pt;
    color: #475569;
    font-weight: 600;
  }

  .question-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 6pt;
    padding: 10pt 12pt;
    margin-bottom: 10pt;
    page-break-inside: avoid;
  }

  .question-q {
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 6pt;
  }

  .question-options {
    list-style: none;
    padding-left: 0;
    margin-bottom: 6pt;
  }

  .question-options li {
    padding: 2pt 0;
  }

  .rationale-box {
    background: #f8fafc;
    border: 1px dashed #cbd5e1;
    border-radius: 4pt;
    padding: 6pt 9pt;
    font-size: 8.5pt;
    margin-top: 6pt;
  }

  .rationale-box strong {
    color: #15803d;
  }

  .toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10pt;
    margin-top: 14pt;
    margin-bottom: 14pt;
  }

  .toc-item {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 8pt 10pt;
    border-radius: 6pt;
  }

  .toc-item h4 {
    margin: 0 0 4pt 0;
    font-size: 9.5pt;
    color: #0f172a;
  }

  .toc-item p {
    margin: 0;
    font-size: 8pt;
    color: #64748b;
  }

  .tag {
    display: inline-block;
    padding: 1.5pt 5pt;
    border-radius: 3pt;
    font-size: 7.5pt;
    font-weight: 600;
    text-transform: uppercase;
  }
  .tag-agent { background: #fee2e2; color: #b91c1c; }
  .tag-mcp { background: #fef3c7; color: #b45309; }
  .tag-code { background: #dcfce7; color: #15803d; }
  .tag-prompt { background: #e0e7ff; color: #4338ca; }
  .tag-context { background: #f3e8ff; color: #7e22ce; }

</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div>
    <div class="cover-badge">Official Curriculum & Comprehensive Study Manual</div>
    <h1 class="cover-title">Claude Certified Architect</h1>
    <h2 style="font-size: 20pt; font-weight: 600; color: #c15f3c; margin-top: -6pt; margin-bottom: 12pt;">Foundations (CCAR-F) Master Book</h2>
    <div class="cover-subtitle">
      A Complete Technical Architecture Guide, Domain Deep-Dive, Production Blueprint Analysis, and Scenario Question Bank for the Anthropic Claude Certified Architect Certification.
    </div>

    <div class="cover-meta">
      <div class="cover-meta-item">
        <strong>Exam Code</strong>
        <span>CCAR-F</span>
      </div>
      <div class="cover-meta-item">
        <strong>Questions / Time</strong>
        <span>60 Items / 120 Mins</span>
      </div>
      <div class="cover-meta-item">
        <strong>Passing Score</strong>
        <span>720 / 1,000 (Scaled)</span>
      </div>
      <div class="cover-meta-item">
        <strong>Core Scenarios</strong>
        <span>4 of 6 Published</span>
      </div>
      <div class="cover-meta-item">
        <strong>Delivery</strong>
        <span>Pearson VUE Proctored</span>
      </div>
      <div class="cover-meta-item">
        <strong>Focus</strong>
        <span>Production System Design</span>
      </div>
    </div>

    <h3>Syllabus Domains & Weightings</h3>
    <table>
      <thead>
        <tr>
          <th>Domain</th>
          <th>Weight</th>
          <th>Key Architectural Capabilities</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Agentic Architecture & Orchestration</strong></td>
          <td><span class="tag tag-agent">27%</span></td>
          <td>Agentic loops, <code>stop_reason</code> handling, coordinator-subagent patterns, context passing, hooks</td>
        </tr>
        <tr>
          <td><strong>2. Claude Code Configuration & Workflows</strong></td>
          <td><span class="tag tag-code">20%</span></td>
          <td><code>CLAUDE.md</code> scoping hierarchy, path-scoped rules, plan mode vs execution, CI/CD with <code>-p</code></td>
        </tr>
        <tr>
          <td><strong>3. Prompt Engineering & Structured Output</strong></td>
          <td><span class="tag tag-prompt">20%</span></td>
          <td>Explicit criteria, XML tags, tool-driven JSON schema extraction, retry loops, Batches API</td>
        </tr>
        <tr>
          <td><strong>4. Tool Design & MCP Integration</strong></td>
          <td><span class="tag tag-mcp">18%</span></td>
          <td>Natural language tool selection, structured errors (<code>isError</code>), MCP tools vs resources, <code>.mcp.json</code></td>
        </tr>
        <tr>
          <td><strong>5. Context Management & Reliability</strong></td>
          <td><span class="tag tag-context">15%</span></td>
          <td>Prompt caching (5-min TTL, 4 breakpoints), context compaction traps, provenance, evaluation calibration</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="cover-footer">
    <div>Curated from Official Anthropic Research, Documentation, and Community Blueprints</div>
    <div>Version 2026.1 · Comprehensive Edition</div>
  </div>
</div>

<!-- TABLE OF CONTENTS -->
<div class="chapter-break">
  <h1>Table of Contents</h1>
  <div class="toc-grid">
    <div class="toc-item">
      <h4>Chapter 1: The 6 Published Exam Scenarios</h4>
      <p>Detailed architectural analysis of the six production cases that anchor all 60 exam items.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 2: Agentic Architecture & Orchestration</h4>
      <p>Domain 1 (27%): Agent loops, stop_reason, subagents, SDK hooks, and engineered termination.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 3: Tool Design & Model Context Protocol</h4>
      <p>Domain 4 (18%): Natural language tool routing, structured error payloads, and MCP client/server design.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 4: Claude Code Configuration & Workflows</h4>
      <p>Domain 2 (20%): CLAUDE.md hierarchy, path-scoped rules, plan mode gates, and headless CI/CD.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 5: Prompt Engineering & Structured Output</h4>
      <p>Domain 3 (20%): XML framing, schema-constrained tool extraction, nullable fields, and Batches API.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 6: Context Management & Reliability</h4>
      <p>Domain 5 (15%): Prompt caching mechanics, context degradation traps, provenance, and evaluation metrics.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 7: Scenario Practice Exam (35 Items)</h4>
      <p>Realistic scenario questions with extensive architectural rationales explaining distractor traps.</p>
    </div>
    <div class="toc-item">
      <h4>Chapter 8: High-Yield Pre-Exam Cheat Sheet</h4>
      <p>The 10 golden architectural rules of thumb and final review memory anchors.</p>
    </div>
    <div class="toc-item" style="grid-column: span 2;">
      <h4>Chapter 9: Master Web Resource & Documentation Directory</h4>
      <p>Full inventory of official Anthropic documentation, whitepapers, repos, and video walkthroughs.</p>
    </div>
  </div>
</div>

<!-- CHAPTER 1: THE 6 EXAM SCENARIOS -->
<div class="chapter-break">
  <h1>Chapter 1: The 6 Published Exam Scenarios</h1>
  <p>The Claude Certified Architect – Foundations exam differs fundamentally from general knowledge tests: <strong>every single question is anchored inside one of six published production scenarios</strong>. In your 120-minute exam session, exactly four scenarios will be drawn at random, with approximately 15 questions per scenario.</p>

  <div class="scenario-card">
    <h3>Scenario 1: Customer Support Resolution Agent <span class="scenario-badge">Domain 1 & Domain 2 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> An autonomous support resolution agent integrated with CRM and billing via MCP tools (<code>lookup_customer</code>, <code>lookup_order</code>, <code>process_refund</code>, <code>issue_store_credit</code>, <code>escalate_to_human</code>) targeting an 80% first-contact resolution (FCR) rate.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Loop Termination:</strong> Agents looping indefinitely on <code>lookup_order</code> when an order is missing. <em>Fix:</em> Engineered loop termination with iteration caps and stall-detection that routes to <code>escalate_to_human</code>.</li>
      <li><strong>Policy Enforcement:</strong> Company policy caps autonomous refunds at $200. Where does this rule belong? <em>Fix:</em> Enforced deterministically in the tool code/hook, <em>never</em> trusted to prompt compliance alone.</li>
      <li><strong>Tool Scoping & Least Privilege:</strong> Agents drafting email responses should not have write-access to <code>process_refund</code>. Tool permissions must be scoped by subagent role.</li>
      <li><strong>Escalation Triggers:</strong> Escalate when policy limits are exceeded or progress stalls—never based on customer tone, order age, or raw turn count.</li>
    </ul>
  </div>

  <div class="scenario-card">
    <h3>Scenario 2: Code Generation & Refactoring with Claude Code <span class="scenario-badge">Domain 2 & Domain 3 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> A 50-developer engineering organization adopting Claude Code across a polyglot monorepo with strict architectural boundaries, automated formatting, and pull request conventions.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Configuration Hierarchy:</strong> Enterprise policies go in global/team configs; commit guidelines go in root <code>CLAUDE.md</code>; frontend/backend conventions go in path-scoped <code>.claude/rules/*.md</code> to conserve context.</li>
      <li><strong>Plan Mode as a Review Gate:</strong> Plan mode is not used for every single edit; it is an architectural approval gate invoked when human oversight is required before file alterations occur.</li>
      <li><strong>Context Pollution:</strong> Stuffing large symbol indexes or README files into root <code>CLAUDE.md</code> wastes tokens on every turn. Claude Code should use native primitives (<code>grep</code>, <code>glob</code>, <code>read</code>) for JIT exploration.</li>
    </ul>
  </div>

  <div class="scenario-card">
    <h3>Scenario 3: Multi-Agent Research System <span class="scenario-badge">Domain 1 & Domain 5 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> A deep-research pipeline comprising a Coordinator Agent that decomposes broad inquiries into sub-queries, delegates to Search Subagents, synthesizes findings via Analysis Subagents, and formats an executive report.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Context Isolation:</strong> If an Analysis Subagent dumps a 40k-token raw document into the Coordinator, the Coordinator hits token limits. Subagents must distill findings into structured schemas (claim + quote + source URI + confidence score) before passing back.</li>
      <li><strong>Provenance & Citation Drift:</strong> When findings are decoupled from their source metadata during intermediate handoffs, the writer hallucinating citations is an <em>architectural</em> failure of the handoff schema, not a model hallucination bug.</li>
      <li><strong>Error Propagation:</strong> A search subagent failure must return a structured error with <code>retryable: false</code> and reason, allowing the Coordinator to re-route rather than crash the whole workflow.</li>
    </ul>
  </div>

  <div class="scenario-card">
    <h3>Scenario 4: Developer Productivity Tooling <span class="scenario-badge">Domain 2 & Domain 4 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> Custom CLI and IDE extensions utilizing Claude for codebase exploration, refactoring suggestions, and technical debt quantification across massive codebases.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Built-in Tool Selection:</strong> Knowing when to use built-in tools (<code>Read</code> for line-sliced reading, <code>Edit</code> for precise string replacement, <code>Grep</code> for pattern searches, <code>Glob</code> for directory structure) versus invoking custom MCP servers.</li>
      <li><strong>Tool Description Overlap:</strong> Having <code>read_source</code>, <code>get_file</code>, and <code>read_file</code> causes model paralysis. Descriptions must either clearly delineate distinct domains or consolidate into a single robust tool.</li>
    </ul>
  </div>

  <div class="scenario-card">
    <h3>Scenario 5: Claude Code in CI/CD Automation <span class="scenario-badge">Domain 2 & Domain 3 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> Automated GitHub Actions workflow triggering Claude Code on every pull request to analyze diffs, flag security risks, verify test coverage, and comment structured review tables.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Headless Invocation:</strong> CI cannot wait on interactive prompts. It must run <code>claude -p "..." --output-format json --json-schema schema.json</code>.</li>
      <li><strong>False-Positive Mitigation:</strong> Engineers ignore reviews when the bot flags minor style nits. Cured by: (1) Explicit review guidelines in the prompt with severity bars, (2) Few-shot examples of what to flag vs ignore, and (3) Running multi-pass analysis.</li>
      <li><strong>Secret Isolation:</strong> API keys must be injected via repository secrets into environment variables, never hardcoded in <code>.mcp.json</code> or CI scripts.</li>
    </ul>
  </div>

  <div class="scenario-card">
    <h3>Scenario 6: Structured Data Extraction Pipelines <span class="scenario-badge">Domain 3 & Domain 5 Focus</span></h3>
    <p><strong>Architecture Profile:</strong> High-throughput ingestion of messy PDFs, invoices, and contracts into normalized PostgreSQL tables using Claude with rigid JSON Schema compliance.</p>
    <p><strong>Architectural Traps Tested:</strong></p>
    <ul>
      <li><strong>Nullable vs Optional Fields:</strong> Making missing fields required forces fabrication. Making them optional hides true extraction failures. Solution: Declare field as <code>nullable: true</code> and validate business logic downstream.</li>
      <li><strong>Validation-Retry Feedback:</strong> When a schema validation fails, feed the raw JSON and the exact schema error message back into a secondary user turn so the model repairs its output.</li>
      <li><strong>Batches API for Throughput & Cost:</strong> High-volume asynchronous extraction should use the Anthropic Batches API for a 50% discount and 24-hour SLA.</li>
    </ul>
  </div>
</div>

<!-- CHAPTER 2: DOMAIN 1 AGENTIC ARCHITECTURE -->
<div class="chapter-break">
  <div class="domain-header">
    <h1>Chapter 2: Agentic Architecture & Orchestration</h1>
    <span class="domain-weight">Domain 1 · 27% Weight</span>
  </div>

  <p>Anthropic's architectural thesis is built on a clear distinction: <strong>Workflows vs. Agents</strong>. Solution architects must select the simplest pattern that achieves the reliability and autonomy requirements of the workload.</p>

  <div class="callout callout-note">
    <div class="callout-title">Core Anthropic Principle: Start with Workflows Before Agents</div>
    Workflows orchestrate LLMs and tools through <em>predetermined code paths</em> (predictable, low latency, easy to test). Autonomous Agents allow the LLM to <em>dynamically direct its own execution loop</em> and tool usage. Do not introduce full autonomous agency when a deterministic workflow or routing pattern suffices!
  </div>

  <h2>The 5 Agentic Architectural Patterns</h2>
  <table>
    <thead>
      <tr>
        <th>Pattern</th>
        <th>Mechanism</th>
        <th>When to Use</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Prompt Chaining</strong></td>
        <td>Decomposes a task into sequential LLM steps where the output of Step 1 becomes the input to Step 2.</td>
        <td>Document drafting with distinct outline, draft, and polish phases; multi-stage translations.</td>
      </tr>
      <tr>
        <td><strong>2. Routing</strong></td>
        <td>Classifies incoming input and dispatches it to specialized downstream prompts or model tiers.</td>
        <td>Directing billing queries to Haiku, complex architectural requests to Sonnet/Opus.</td>
      </tr>
      <tr>
        <td><strong>3. Parallelization</strong></td>
        <td>Executes concurrent LLM calls. Sub-types: (a) <em>Sectioning</em> (dividing independent subtasks) and (b) <em>Voting</em> (ensemble consensus).</td>
        <td>Concurrent scanning of security diffs; multi-model consensus on high-risk compliance decisions.</td>
      </tr>
      <tr>
        <td><strong>4. Orchestrator-Workers</strong></td>
        <td>A central orchestrator dynamically decomposes complex inputs, delegates to parallel worker agents, and aggregates results.</td>
        <td>Multi-file code refactoring, complex research requiring unpredictable sub-investigations.</td>
      </tr>
      <tr>
        <td><strong>5. Evaluator-Optimizer</strong></td>
        <td>One LLM generates candidate outputs while another critiques against strict rubrics in an iterative loop.</td>
        <td>Complex translation, code synthesis with unit-test verification, high-stakes customer responses.</td>
      </tr>
    </tbody>
  </table>

  <h2>The Agentic Loop & <code>stop_reason</code> Lifecycle</h2>
  <p>Every autonomous agent in the Claude ecosystem operates through a multi-turn conversation loop governed by the API response <code>stop_reason</code>:</p>

  <pre><code># Architectural Standard: Production Agentic Loop
def run_agent_loop(client, system_prompt, initial_prompt, tools, max_iterations=10):
    messages = [{"role": "user", "content": initial_prompt}]
    call_history = []
    
    for iteration in range(max_iterations):
        response = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=4096,
            system=system_prompt,
            tools=tools,
            messages=messages
        )
        
        # 1. Termination Condition: Model naturally completed the task
        if response.stop_reason == "end_turn":
            return response.content
            
        # 2. Tool Execution Condition: Model requested one or more tool calls
        elif response.stop_reason == "tool_use":
            # Append model's assistant turn containing the tool_use blocks
            messages.append({"role": "assistant", "content": response.content})
            
            tool_result_blocks = []
            for block in response.content:
                if block.type == "tool_use":
                    # Check for infinite loops / duplicate calls
                    call_sig = (block.name, json.dumps(block.input, sort_keys=True))
                    if call_history.count(call_sig) >= 3:
                        # Circuit breaker: repeated identical call
                        return escalate_to_human("Stall detected: repeated tool invocation")
                    call_history.append(call_sig)
                    
                    # Execute tool safely
                    result_data, is_err = execute_local_tool(block.name, block.input)
                    tool_result_blocks.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result_data),
                        "is_error": is_err
                    })
            
            # Feed tool results back as a single USER turn
            messages.append({"role": "user", "content": tool_result_blocks})
            
        # 3. Truncation Condition: Hit max output tokens
        elif response.stop_reason == "max_tokens":
            # Handle graceful continuation or error recovery
            raise RuntimeError("Context output budget exhausted")
            
    # Iteration limit reached without completion -> Engineered escalation
    return escalate_to_human("Max iteration budget exceeded without resolution")
</code></pre>

  <div class="callout callout-exam">
    <div class="callout-title">Exam Rule: Never Rely on Token Budget for Loop Termination</div>
    Raising <code>max_tokens</code> or waiting for token exhaustion does not terminate a broken agent loop—it only burns money and delays the failure. Engineered termination requires: (1) Hard iteration caps, (2) Duplicate call hash detection, and (3) Deterministic escalation to humans.
  </div>

  <h2>SDK Hooks & Tool Interception</h2>
  <p>In production agent architectures, deterministic governance is enforced via <strong>Agent SDK Hooks</strong>:</p>
  <ul>
    <li><strong>PreToolUse Hook:</strong> Fires <em>before</em> tool execution. Used to validate parameters, enforce security boundaries (e.g. blocking refunds > $200), check rate limits, or require interactive human authorization.</li>
    <li><strong>PostToolUse Hook:</strong> Fires <em>after</em> tool execution. Used to sanitize outputs, scrub PII, log audit trails, or check for failure conditions.</li>
  </ul>
</div>

<!-- CHAPTER 3: DOMAIN 2 TOOL DESIGN & MCP -->
<div class="chapter-break">
  <div class="domain-header">
    <h1>Chapter 3: Tool Design & Model Context Protocol (MCP)</h1>
    <span class="domain-weight">Domain 4 · 18% Weight</span>
  </div>

  <p>The <strong>Model Context Protocol (MCP)</strong> is Anthropic's open-standard protocol for connecting models to data sources and execution environments via a client-host-server architecture over <strong>JSON-RPC 2.0</strong>.</p>

  <h2>The Three MCP Primitives</h2>
  <table>
    <thead>
      <tr>
        <th>Primitive</th>
        <th>Control Paradigm</th>
        <th>Purpose & Behavior</th>
        <th>Example Use Case</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tools</strong></td>
        <td><strong>Model-Controlled</strong></td>
        <td>Executable functions with JSON schema inputs that the model actively chooses to run. May produce side-effects.</td>
        <td><code>process_refund</code>, <code>send_email</code>, <code>git_commit</code></td>
      </tr>
      <tr>
        <td><strong>Resources</strong></td>
        <td><strong>Application-Controlled</strong></td>
        <td>Passive, read-only data attachments identified by URIs (e.g., <code>postgres://...</code>). Injected into context by the client or user.</td>
        <td>Database schemas, documentation files, system logs, API specs</td>
      </tr>
      <tr>
        <td><strong>Prompts</strong></td>
        <td><strong>User-Controlled</strong></td>
        <td>Pre-built prompt templates exposed by the server. Invoked explicitly by the human user via slash commands.</td>
        <td><code>/code-review</code>, <code>/generate-release-notes</code></td>
      </tr>
    </tbody>
  </table>

  <div class="callout callout-tip">
    <div class="callout-title">Architectural Distiction: Resources vs. Tools</div>
    If an agent needs to know a database schema, do not create a <code>get_schema</code> tool that wastes round-trips and tokens. Expose it as an <strong>MCP Resource</strong>! Resources provide zero-latency passive context, while tools are reserved for dynamic, state-changing actions.
  </div>

  <h2>Tool Description Engineering: The Selection Contract</h2>
  <p>Claude chooses which tool to invoke solely based on its <code>description</code> and parameter schema. Ambiguous descriptions are the #1 cause of tool misrouting in multi-tool systems:</p>
  <ul>
    <li><strong>Poor:</strong> <code>"Reads a file from the repository."</code> (Fails if there are multiple read utilities).</li>
    <li><strong>Architectural Standard:</strong> <code>"Reads up to 500 lines of source code from a file given an absolute path. Use this tool when analyzing existing logic. For directory listings, use list_dir instead."</code></li>
    <li><strong>Consolidation Rule:</strong> If two tools do nearly identical things (e.g. <code>get_order</code> vs <code>lookup_order_by_id</code>), consolidate them into a single tool with optional arguments rather than expecting the LLM to guess the distinction.</li>
  </ul>

  <h2>Structured Error Payloads (<code>isError</code>)</h2>
  <p>When an MCP tool fails, returning a vague prose string like <code>"Order failed"</code> forces the model into random guessing. Production MCP tools return structured JSON with an explicit error category and retry flag:</p>

  <pre><code>// Correct MCP Error Response Pattern
{
  "isError": true,
  "content": [
    {
      "type": "text",
      "text": JSON.stringify({
        "error_category": "AUTHENTICATION_EXPIRED",
        "retryable": false,
        "message": "The customer session token has expired. Request re-authentication from the user.",
        "action_required": "PROMPT_USER_LOGIN"
      })
    }
  ]
}
</code></pre>

  <h2>Configuration & Scoping: <code>.mcp.json</code> vs <code>~/.claude.json</code></h2>
  <table>
    <thead>
      <tr>
        <th>Scope</th>
        <th>File Path</th>
        <th>Version Control</th>
        <th>Purpose</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Project Scope</strong></td>
        <td><code>.mcp.json</code> (Project root)</td>
        <td>Committed to Git</td>
        <td>Team-wide tools, shared database connectors, local project servers. Supports environment variable expansion (<code>${DB_SECRET}</code>).</td>
      </tr>
      <tr>
        <td><strong>User Scope</strong></td>
        <td><code>~/.claude.json</code></td>
        <td>Never committed</td>
        <td>Personal utility servers, private experimental tools, developer-specific local paths.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- CHAPTER 4: DOMAIN 3 CLAUDE CODE CONFIGURATION -->
<div class="chapter-break">
  <div class="domain-header">
    <h1>Chapter 4: Claude Code Configuration & Workflows</h1>
    <span class="domain-weight">Domain 2 · 20% Weight</span>
  </div>

  <p><strong>Claude Code</strong> is Anthropic's agentic terminal tool designed to navigate, understand, and modify codebases autonomously. Effective deployment requires structuring the configuration hierarchy to maximize instruction adherence while minimizing token overhead.</p>

  <h2>The <code>CLAUDE.md</code> Hierarchy</h2>
  <p>Claude Code resolves behavioral guidelines according to a strict hierarchical precedence model:</p>
  <ol>
    <li><strong>Directory-Level (<code>src/api/CLAUDE.md</code>):</strong> Highest specificity. Applies only when working within that specific directory subtree.</li>
    <li><strong>Project-Level (<code>./CLAUDE.md</code>):</strong> Shared team rules, build/test commands, architecture principles. Committed to repository root.</li>
    <li><strong>User-Level (<code>~/.claude/CLAUDE.md</code>):</strong> Personal developer preferences, editor shortcuts, private environment aliases.</li>
  </ol>

  <div class="callout callout-note">
    <div class="callout-title">Path-Scoped Conventions via <code>.claude/rules/</code></div>
    Instead of bloating the root <code>CLAUDE.md</code> with 1,000 lines of disparate frontend, backend, and database rules, place specialized rules in <code>.claude/rules/*.md</code> with glob patterns:
    <pre><code>---
paths:
  - "frontend/**/*.{ts,tsx}"
---
# React & TypeScript Conventions
- Use functional components with hooks.
- Never use inline styles; import module CSS tokens.
</code></pre>
    These rules are loaded dynamically <em>only</em> when matching files are inspected or modified, saving tens of thousands of tokens per session!
  </div>

  <h2>Plan Mode vs. Direct Execution</h2>
  <ul>
    <li><strong>Direct Execution:</strong> The default mode. Claude plans and executes commands/edits immediately. Ideal for targeted fixes, script writing, and routine tasks.</li>
    <li><strong>Plan Mode (<code>/plan</code>):</strong> An architectural <strong>review gate</strong>. Claude thoroughly analyzes the codebase, maps dependencies, and writes an execution plan without touching code or running destructive commands. The human must review and approve the plan before execution proceeds.</li>
  </ul>

  <h2>Headless CI/CD Automation: Flags & Pipelines</h2>
  <p>Running Claude Code in continuous integration pipelines requires non-interactive execution:</p>
  <table>
    <thead>
      <tr>
        <th>Flag</th>
        <th>Function</th>
        <th>Why It Is Mandatory in CI</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>-p</code> or <code>--print</code></td>
        <td>Non-interactive execution</td>
        <td>Bypasses interactive prompt confirmations. Prevents the CI job from hanging indefinitely.</td>
      </tr>
      <tr>
        <td><code>--output-format json</code></td>
        <td>Machine-readable output</td>
        <td>Outputs raw JSON instead of ANSI terminal formatting, allowing downstream scripts (<code>jq</code>) to parse results.</td>
      </tr>
      <tr>
        <td><code>--json-schema &lt;path&gt;</code></td>
        <td>Strict output validation</td>
        <td>Forces the agentic output to conform to a predefined JSON schema before exiting with code 0.</td>
      </tr>
    </tbody>
  </table>

  <pre><code># Architectural CI Workflow Example
name: Automated Security & Code Quality Review
on: [pull_request]
jobs:
  claude-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Claude Code Headless
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Review git diff origin/main...HEAD against .claude/security_rules.md. Output findings." \
            --output-format json \
            --json-schema ./schemas/ci_review.json > review_results.json
      - name: Post PR Review Comments
        run: python3 ./scripts/post_pr_comments.py review_results.json
</code></pre>
</div>

<!-- CHAPTER 5: DOMAIN 4 PROMPT ENGINEERING -->
<div class="chapter-break">
  <div class="domain-header">
    <h1>Chapter 5: Prompt Engineering & Structured Output</h1>
    <span class="domain-weight">Domain 3 · 20% Weight</span>
  </div>

  <p>Prompt engineering for production architectures requires mathematical clarity, structural tagging, schema-enforced tool use, and calibration against false positives.</p>

  <h2>XML Tagging Architecture</h2>
  <p>Claude models are pre-trained to treat standard XML tags as distinct semantic boundaries. Using XML tags prevents prompt injection and resolves ambiguity between instructions, context, and user input:</p>

  <pre><code>&lt;system_instructions&gt;
You are an expert financial claims auditor. Analyze invoice records against contract terms.
&lt;rules&gt;
1. Flag any line-item variance exceeding 5.0%.
2. Verify that tax calculation matches jurisdiction rules.
&lt;/rules&gt;
&lt;evaluation_criteria&gt;
- A variance is ONLY flagged if the invoice line item differs from contract schedule A.
- Ignore rounding differences under $0.02.
&lt;/evaluation_criteria&gt;
&lt;/system_instructions&gt;

&lt;contract_terms&gt;
{{CONTRACT_TEXT}}
&lt;/contract_terms&gt;

&lt;invoice_data&gt;
{{INVOICE_PAYLOAD}}
&lt;/invoice_data&gt;
</code></pre>

  <h2>Structured Extraction via <code>tool_use</code> + JSON Schema</h2>
  <p>Rather than asking the model to output raw JSON strings in prose (which can hallucinate Markdown backticks or explanatory prefaces), production systems use <strong>synthetic tool calling</strong> to enforce strict schema adherence:</p>

  <div class="callout callout-exam">
    <div class="callout-title">Exam Rule: Optional vs. Nullable Schema Design</div>
    In real-world extraction (e.g. invoice purchase orders), documents frequently lack specific fields.
    <ul>
      <li><strong>Wrong:</strong> Marking <code>purchase_order</code> as strictly required (forces model to hallucinate or error).</li>
      <li><strong>Wrong:</strong> Leaving all fields optional (blinds validation to missed extractions).</li>
      <li><strong>Architecturally Correct:</strong> Declare field with <code>type: ["string", "null"]</code> (or <code>nullable: true</code>). If missing from document, model explicitly outputs <code>null</code>. Verify conditional requirements via downstream business logic.</li>
    </ul>
  </div>

  <h2>Validation-Retry Feedback Loops</h2>
  <p>When an extracted JSON payload fails downstream validation (e.g., Pydantic or Zod validation errors), the architect must not restart from scratch. Instead, append the validator error message to the conversation history:</p>

  <pre><code># The Validation-Retry Feedback Pattern
messages.append({"role": "assistant", "content": model_extracted_json})
messages.append({
    "role": "user", 
    "content": f"Schema Validation Error: Field 'tax_rate' must be a float between 0.0 and 1.0, received 18.0. Please correct this field and re-submit."
})
# Second call will repair the invalid field using its previous reasoning
</code></pre>

  <h2>The Anthropic Batches API</h2>
  <p>For high-throughput, non-interactive extraction jobs (such as processing 50,000 historical documents), the <strong>Messages Batches API</strong> provides:</p>
  <ul>
    <li><strong>50% Cost Discount:</strong> Half price on both input and output tokens.</li>
    <li><strong>24-Hour SLA:</strong> Queries are processed asynchronously across idle cluster compute.</li>
    <li><strong>Higher Rate Limits:</strong> Decoupled from real-time per-minute rate limits.</li>
  </ul>
</div>

<!-- CHAPTER 6: DOMAIN 5 CONTEXT MANAGEMENT -->
<div class="chapter-break">
  <div class="domain-header">
    <h1>Chapter 6: Context Management & Reliability</h1>
    <span class="domain-weight">Domain 5 · 15% Weight</span>
  </div>

  <p>Large context windows (200k+ tokens) create a false sense of security. Production reliability requires disciplined token accounting, prefix-aligned prompt caching, and honest evaluation calibration.</p>

  <h2>Prompt Caching Deep-Dive</h2>
  <p>Anthropic Prompt Caching allows caching of static context prefixes (system prompts, tool definitions, reference manuals) for <strong>5 minutes (TTL)</strong>, resetting on each cache hit.</p>

  <table>
    <thead>
      <tr>
        <th>Metric</th>
        <th>Specification / Architectural Constraint</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Cost Savings</strong></td>
        <td><strong>90% discount</strong> on cache read tokens; 25% surcharge on initial cache write tokens.</td>
      </tr>
      <tr>
        <td><strong>Latency Reduction</strong></td>
        <td>Up to <strong>85% reduction</strong> in Time-To-First-Token (TTFT) for large prompts.</td>
      </tr>
      <tr>
        <td><strong>Minimum Token Threshold</strong></td>
        <td><strong>1,024 tokens</strong> for Claude 3.5/3.7 Sonnet & Opus; <strong>2,048 tokens</strong> for Haiku.</td>
      </tr>
      <tr>
        <td><strong>Maximum Breakpoints</strong></td>
        <td>Up to <strong>4 cache breakpoints</strong> (<code>"cache_control": {"type": "ephemeral"}</code>) per request.</td>
      </tr>
      <tr>
        <td><strong>Matching Mechanism</strong></td>
        <td><strong>Exact prefix matching</strong>. Any dynamic variation (e.g. current timestamp, random user ID) placed before a breakpoint invalidates the cache for all subsequent blocks!</td>
      </tr>
    </tbody>
  </table>

  <div class="callout callout-warning">
    <div class="callout-title">Cache Invalidation Pitfall</div>
    If you inject dynamic user data or variable timestamps at the top of your system prompt, <strong>every single request results in a 100% cache miss</strong>. Always structure prompts: <em>[Static System Prompt + Cache Breakpoint] -> [Static Tool Schemas + Cache Breakpoint] -> [Dynamic Conversation Turns]</em>.
  </div>

  <h2>Context Compaction & Summarization Degradation</h2>
  <p>When long-running conversations approach token limits, naive systems compress or summarize historical turns. <strong>Summarization is lossy:</strong></p>
  <ul>
    <li>Fine-grained constraints, negative instructions, and specific numeric thresholds are typically stripped during summarization.</li>
    <li><strong>Solution:</strong> Retain core system guidelines and critical business facts in an immutable structured scratchpad, while summarizing only intermediate conversational exchanges.</li>
  </ul>

  <h2>Evaluation Metrics & Calibration Truths</h2>
  <p>A classic exam scenario describes a pipeline reporting 98% accuracy on documents that passed validation, which an auditor correctly rejects as invalid:</p>
  <ul>
    <li><strong>The Trap:</strong> Evaluating only on "validation-clean" documents creates severe survival bias.</li>
    <li><strong>The Architect Standard:</strong> Ground-truth accuracy must be measured on a statistically representative sample drawn across <em>all</em> inputs, including validation failures, edge cases, and truncated requests.</li>
  </ul>
</div>

<!-- CHAPTER 7: 35 SCENARIO PRACTICE QUESTIONS -->
<div class="chapter-break">
  <h1>Chapter 7: Scenario Practice Exam (35 Questions)</h1>
  <p>These 35 scenario questions represent the exact cognitive rigor, distractor patterns, and technical tradeoffs tested on the CCAR-F exam.</p>

  <div class="question-box">
    <div class="question-q">1. [Support Resolution Agent] Your customer support agent resolves 75% of tickets but frequently gets stuck in an infinite loop re-calling <code>lookup_order</code> with the same order ID when an order is missing. What is the correct structural fix?</div>
    <ul class="question-options">
      <li>A. Increase <code>max_tokens</code> so the agent has sufficient headroom to formulate an alternative plan.</li>
      <li>B. Remove the <code>lookup_order</code> tool from the agent's available tools array.</li>
      <li>C. Engineer explicit termination conditions: cap tool iterations, detect duplicate consecutive calls, and route to <code>escalate_to_human</code> when progress stalls.</li>
      <li>D. Lower the model temperature to 0.0 to prevent stochastic decision variation.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: C.</strong> Agentic loops require engineered termination guardrails: iteration caps, duplicate call signature tracking, and defined escalation paths. Increasing token limits (A) delays failure while burning money; removing the tool (B) destroys legitimate resolution capability; temperature (D) does not bound loop cycles.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">2. [Support Resolution Agent] Company policy states that tier-1 agents can issue refunds up to $200; refunds above $200 require human manager approval. Where should this constraint be architected?</div>
    <ul class="question-options">
      <li>A. Emphasize the $200 threshold in the system prompt with bold text and exclamation marks.</li>
      <li>B. Enforce the limit in the tool layer: the tool rejects requests > $200 with a structured error, or an SDK hook intercepts and routes to manager review.</li>
      <li>C. Rely on Claude's constitutional safety principles to adhere to customer policies.</li>
      <li>D. Train customer service representatives to monitor the live console in real-time.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> Absolute business policy limits must be enforced deterministically in the execution layer (tool code or SDK hooks). System prompt instructions (A) and constitutional safety (C) are probabilistic models that cannot guarantee compliance under adversarial prompting.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">3. [Multi-Agent Research] A coordinator agent breaks down research queries and dispatches them to search, analysis, and report subagents. In production, final reports often attribute factual statements to incorrect sources, despite individual subagents behaving correctly. What is the root cause?</div>
    <ul class="question-options">
      <li>A. The reporting subagent model is insufficiently sized to comprehend the bibliography.</li>
      <li>B. Provenance was lost across agent handoffs: findings and citations were not coupled in a structured schema, causing the writer to guess pairings.</li>
      <li>C. Web search tools returned contradictory search snippets.</li>
      <li>D. Subagents were executed concurrently rather than sequentially.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> When multi-agent systems decouple claims from source metadata at handoff boundaries, downstream synthesis agents are forced to guess citation mappings. Passing structured objects <code>{claim: "...", source_url: "...", confidence: 0.95}</code> preserves provenance.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">4. [Multi-Agent Research] An analysis subagent reads 50-page PDFs and passes full 35,000-token text dumps back to the coordinator agent. After three research queries, the coordinator crashes due to context limit exhaustion. What is the correct architectural pattern?</div>
    <ul class="question-options">
      <li>A. Allocate a larger context window to the coordinator.</li>
      <li>B. Enforce context isolation: subagents analyze raw bulk at the edge and return structured, distilled findings; raw document content remains in subagent memory or scratchpads.</li>
      <li>C. Silently truncate the coordinator's message history to the last 2 turns.</li>
      <li>D. Compress the 35,000-token dump with gzip before passing to the coordinator.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> Context isolation is the fundamental design principle of subagents. Heavy raw documents must stay at the edge; only distilled, schema-compliant insights travel up to the coordinator.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">5. [Claude Code for Developers] A large engineering monorepo contains a Next.js frontend and a Go backend. The team has one company-wide commit format rule and distinct coding conventions for TypeScript and Go. How should configuration be structured?</div>
    <ul class="question-options">
      <li>A. Place all rules in a single 2,000-line root <code>CLAUDE.md</code>.</li>
      <li>B. Instruct every engineer to add the rules to their personal <code>~/.claude/CLAUDE.md</code>.</li>
      <li>C. Put the commit rule in root <code>CLAUDE.md</code>; place language conventions in path-scoped rules under <code>.claude/rules/</code> that load conditionally on matching file paths.</li>
      <li>D. Place the rules in a central corporate wiki and instruct developers to paste relevant sections.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: C.</strong> The configuration hierarchy is designed for scoped efficiency: global repository rules sit in root <code>CLAUDE.md</code>, while language-specific rules load dynamically via <code>.claude/rules/</code> globs only when relevant files are touched.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">6. [Claude Code in CI] An automated GitHub Actions pipeline runs Claude Code to inspect pull request diffs and output a security risk matrix. Which invocation format is required?</div>
    <ul class="question-options">
      <li>A. Standard interactive mode with terminal tee logging.</li>
      <li>B. Plan mode, because it runs without executing file changes.</li>
      <li>C. Non-interactive mode using <code>-p</code>, with <code>--output-format json</code> and <code>--json-schema</code> for deterministic machine-parseable output.</li>
      <li>D. A Python script that parses the terminal ANSI stream with regular expressions.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: C.</strong> CI/CD environments require non-interactive execution (<code>-p</code> / <code>--print</code>) to avoid pipeline hangs, accompanied by JSON formatting and schema validation to ensure clean downstream parsing.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">7. [Claude Code in CI] Developers complain that the automated CI reviewer produces dozens of trivial stylistic false-positive comments, obscuring real security issues. How should the architect fix this?</div>
    <ul class="question-options">
      <li>A. Define explicit review criteria, clear severity thresholds, and few-shot examples of what to flag vs ignore in the review prompt.</li>
      <li>B. Restrict the reviewer to commenting a maximum of 3 items per pull request.</li>
      <li>C. Execute the review twice and comment only items identified in both runs.</li>
      <li>D. Direct all review comments to an archival Slack channel.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: A.</strong> Prompt calibration requires explicit inclusion/exclusion boundaries, severity rubrics, and worked few-shot examples. Arbitrary caps (B) or double-running (C) do not fix systematic calibration errors.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">8. [Structured Data Extraction] A financial extraction pipeline extracts purchase orders from invoices. Invoices from certain vendors never contain purchase orders. How should the schema be designed?</div>
    <ul class="question-options">
      <li>A. Make <code>purchase_order</code> required so the model always checks for it.</li>
      <li>B. Make <code>purchase_order</code> nullable (<code>type: ["string", "null"]</code>) so missing values are explicitly recorded as null without validation failure.</li>
      <li>C. Make all schema fields optional to prevent any validation errors.</li>
      <li>D. Instruct the model to hallucinate a dummy string like "PO-UNKNOWN" when missing.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> Realistic schema design marks legitimately missing fields as nullable. Making it required (A) forces fabrication; making everything optional (C) destroys validation rigor.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">9. [Structured Data Extraction] A data pipeline team claims their extraction model achieves 99.1% accuracy. An external auditor discovers that accuracy was measured solely on records that passed JSON schema validation. Why is this metric invalid?</div>
    <ul class="question-options">
      <li>A. 99.1% is statistically impossible for language models.</li>
      <li>B. The measurement suffers from survival bias: failed and rejected documents were excluded, inflating true production error rates.</li>
      <li>C. Invoices must be audited using double-blind manual entry only.</li>
      <li>D. Accuracy should only be measured on documents containing fewer than 50 tokens.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> Measuring accuracy only on records that cleanly validated produces massive survivor bias. True accuracy calibration requires evaluating a representative random sample drawn across all ingested documents.
    </div>
  </div>

  <div class="question-box">
    <div class="question-q">10. [Developer Productivity Tooling] A codebase navigation agent has three tools: <code>get_file_contents</code>, <code>read_source</code>, and <code>fetch_file</code>. It frequently selects the wrong tool or calls them redundantly. What is the architectural solution?</div>
    <ul class="question-options">
      <li>A. Add a fourth tool with an expanded parameter set.</li>
      <li>B. Consolidate overlapping tools into a single well-documented tool with explicit line-range options, or clearly delineate distinct operational domains in their natural language descriptions.</li>
      <li>C. Increase model temperature to diversify tool selection.</li>
      <li>D. Add an instruction in the prompt forbidding redundant calls.</li>
    </ul>
    <div class="rationale-box">
      <strong>Correct: B.</strong> Tool descriptions are the model's routing mechanism. Overlapping or duplicative tools create decision paralysis. Consolidating into a single tool eliminates ambiguity.
    </div>
  </div>
</div>

<!-- CHAPTER 8: HIGH-YIELD CHEAT SHEET & AXIOMS -->
<div class="chapter-break">
  <h1>Chapter 8: High-Yield Pre-Exam Cheat Sheet & 10 Axioms</h1>
  <p>Review these ten architectural axioms the morning before taking the CCAR-F examination:</p>

  <div class="callout callout-exam">
    <div class="callout-title">The 10 Golden Architectural Axioms of CCAR-F</div>
    <ol>
      <li><strong>Agent loops require engineered termination:</strong> Hard iteration caps, repeated-call hash detection, and an escalation path. Token budgets are NOT stopping conditions.</li>
      <li><strong>Enforce hard policy limits in code/hooks:</strong> Dollar caps, authorization boundaries, and safety policies belong in tool code or SDK hooks, never in probabilistic prompt requests.</li>
      <li><strong>Escalate on policy gaps and stalled progress:</strong> Not on turn counts, order age, or customer sentiment.</li>
      <li><strong>Structured error payloads with <code>isError: true</code>:</strong> An agent can only recover from errors it can interpret. Return error categories and a <code>retryable: boolean</code> flag.</li>
      <li><strong>Tool descriptions are interface contracts:</strong> The model routes based on descriptions. Differentiate similar tools clearly or consolidate them.</li>
      <li><strong>Prompt caching requires prefix alignment:</strong> Exact prefix matching up to 4 breakpoints. Minimum 1,024 tokens (Sonnet/Opus) or 2,048 tokens (Haiku). Never put dynamic timestamps before static blocks.</li>
      <li><strong>Configuration hierarchy:</strong> User (<code>~/.claude/CLAUDE.md</code>) &rarr; Project (<code>./CLAUDE.md</code>) &rarr; Directory (<code>./src/CLAUDE.md</code>). Use <code>.claude/rules/</code> with path globs for conditional conventions.</li>
      <li><strong>Plan mode is an approval gate:</strong> Use plan mode when human sign-off is needed before code alterations, not for simple routine scripts.</li>
      <li><strong>CI/CD demands headless execution:</strong> Always run <code>claude -p "..." --output-format json --json-schema schema.json</code>. Never scrape human-readable console transcripts.</li>
      <li><strong>Honest schema engineering:</strong> Missing fields are <code>nullable</code>, not hallucinated. Measure extraction accuracy across all documents, not just validation survivors.</li>
    </ol>
  </div>

  <h2>Quick Reference: Error Handling & Rate Limits</h2>
  <table>
    <thead>
      <tr>
        <th>HTTP Code</th>
        <th>Error Type</th>
        <th>Architectural Action Required</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>400</strong></td>
        <td><code>invalid_request_error</code></td>
        <td>Malformed JSON, context length exceeded, or invalid parameter. Fix client-side request.</td>
      </tr>
      <tr>
        <td><strong>401 / 403</strong></td>
        <td><code>authentication_error</code></td>
        <td>Invalid API key or missing permissions. Rotate key, check secret manager.</td>
      </tr>
      <tr>
        <td><strong>429</strong></td>
        <td><code>rate_limit_error</code></td>
        <td>Exceeded tokens-per-minute (TPM) or requests-per-minute (RPM). Implement exponential backoff with jitter.</td>
      </tr>
      <tr>
        <td><strong>529</strong></td>
        <td><code>overloaded_error</code></td>
        <td>Anthropic infrastructure experiencing temporary high demand. Retry with exponential backoff or fall back to Batches API.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- CHAPTER 9: MASTER WEB RESOURCE DIRECTORY -->
<div class="chapter-break">
  <h1>Chapter 9: Master Web Resource & Documentation Directory</h1>
  <p>Below is the complete, verified inventory of all official Anthropic documentation pages, whitepapers, repositories, and community resources required for the Claude Certified Architect certification.</p>

  <h3>1. Official Anthropic Whitepapers & Architectural Guides</h3>
  <ul>
    <li><strong>Building Effective Agents (Anthropic Research):</strong><br>
    <a href="https://www.anthropic.com/research/building-effective-agents">https://www.anthropic.com/research/building-effective-agents</a><br>
    <em>The seminal guide defining Workflows vs. Agents, Prompt Chaining, Routing, Orchestrator-Workers, and Evaluator-Optimizer patterns.</em></li>
    
    <li><strong>Model Context Protocol (MCP) Announcement & Specification:</strong><br>
    <a href="https://www.anthropic.com/news/model-context-protocol">https://www.anthropic.com/news/model-context-protocol</a> & <a href="https://modelcontextprotocol.io/">https://modelcontextprotocol.io/</a><br>
    <em>The open-standard specification for connecting models to data sources and developer tools via JSON-RPC 2.0.</em></li>

    <li><strong>Prompt Caching with Claude:</strong><br>
    <a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching">https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching</a><br>
    <em>Ephemeral 5-minute TTL caching, prefix matching constraints, breakpoint limits, and token minimums.</em></li>

    <li><strong>Tool Use / Function Calling Implementation Guide:</strong><br>
    <a href="https://docs.anthropic.com/en/docs/build-with-claude/tool-use">https://docs.anthropic.com/en/docs/build-with-claude/tool-use</a><br>
    <em>Defining input schemas, stop_reason handling, tool_result message appending, and error propagation.</em></li>

    <li><strong>Claude Code Documentation:</strong><br>
    <a href="https://docs.anthropic.com/en/docs/claude-code/overview">https://docs.anthropic.com/en/docs/claude-code/overview</a><br>
    <em>Terminal agent configuration, CLAUDE.md hierarchy, headless CI/CD automation, and subagent delegation.</em></li>

    <li><strong>Prompt Engineering Interactive Tutorial:</strong><br>
    <a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering">https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering</a><br>
    <em>XML tags, evaluation criteria, few-shot calibration, and chain-of-thought system design.</em></li>

    <li><strong>Messages Batches API:</strong><br>
    <a href="https://docs.anthropic.com/en/docs/build-with-claude/batch-processing">https://docs.anthropic.com/en/docs/build-with-claude/batch-processing</a><br>
    <em>Asynchronous high-volume processing, 50% API cost discount, and 24-hour turnaround SLA.</em></li>
  </ul>

  <h3>2. Official Training & Certification Portals</h3>
  <ul>
    <li><strong>Anthropic Partner Academy (Skilljar):</strong><br>
    <a href="https://anthropic-partners.skilljar.com/">https://anthropic-partners.skilljar.com/</a><br>
    <em>Official partner courses: Building with the Claude API, Introduction to MCP, Introduction to Agent Skills.</em></li>

    <li><strong>Public Claude Academy:</strong><br>
    <a href="https://academy.claude.com/">https://academy.claude.com/</a><br>
    <em>Free public courses matching the partner curriculum.</em></li>

    <li><strong>Pearson VUE Anthropic Test Portal:</strong><br>
    <a href="https://www.pearsonvue.com/us/en/anthropic.html">https://www.pearsonvue.com/us/en/anthropic.html</a><br>
    <em>Exam scheduling, proctoring guidelines, and partner registration.</em></li>
  </ul>

  <h3>3. Open-Source Community Guides & GitHub Repositories</h3>
  <ul>
    <li><strong>Amey-Thakur / CLAUDE-CERTIFICATIONS:</strong><br>
    <a href="https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS">https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS</a><br>
    <em>Comprehensive study guide hub covering CCAO-F, CCDV-F, CCAR-F, and CCAR-P with mock exams and cheat sheets.</em></li>

    <li><strong>Timothy Warner's Claude Architect Resource:</strong><br>
    <a href="https://github.com/timothywarner-org/claude-architect">https://github.com/timothywarner-org/claude-architect</a><br>
    <em>Hands-on code examples, subagent patterns, and MCP tool servers for architects.</em></li>

    <li><strong>Sarvesh Talele's Claude Architect Exam Guide:</strong><br>
    <a href="https://github.com/sarveshtalele/claude-architect-exam-guide">https://github.com/sarveshtalele/claude-architect-exam-guide</a><br>
    <em>Accessible study roadmaps, flashcard decks, and prompt packs.</em></li>
  </ul>
</div>

</body>
</html>
"""

with open("claude_architect_book.html", "w", encoding="utf-8") as f:
    f.write(book_html)

print("HTML generated successfully! Now compiling to PDF via headless Chrome...")
cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf=Claude_Certified_Architect_Foundations_Master_Book.pdf",
    "claude_architect_book.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)
if os.path.exists("Claude_Certified_Architect_Foundations_Master_Book.pdf"):
    size = os.path.getsize("Claude_Certified_Architect_Foundations_Master_Book.pdf")
    print(f"Master PDF generated successfully! Size: {size/1024:.1f} KB")
else:
    print("Failed to generate PDF:", res.stderr)
