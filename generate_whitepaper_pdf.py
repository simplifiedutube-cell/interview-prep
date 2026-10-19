import os
import subprocess

whitepaper_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Anthropic Architectural Whitepaper: Building Effective Agents</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap');

  @page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Inter', sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
    @bottom-left {
      content: "Anthropic Architectural Whitepaper · Building Effective Agents";
      font-family: 'Inter', sans-serif;
      font-size: 8pt;
      color: #64748b;
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Newsreader', Georgia, serif;
    color: #1a1a1a;
    background: #ffffff;
    line-height: 1.65;
    font-size: 10pt;
    margin: 0;
    padding: 0;
  }

  h1, h2, h3, h4, h5, th, .sans {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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
    margin-bottom: 10pt;
    padding-bottom: 6pt;
    border-bottom: 1.5pt solid #e2e8f0;
  }

  h2 {
    font-size: 13.5pt;
    margin-top: 18pt;
    margin-bottom: 8pt;
    color: #1e293b;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 3pt;
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
    background-color: #f8fafc;
    padding: 1pt 3pt;
    border-radius: 3pt;
    color: #c15f3c;
    border: 1px solid #e2e8f0;
  }

  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 9pt 12pt;
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
    padding: 35pt 20pt 20pt 20pt;
    border-bottom: 4pt solid #d97757;
  }

  .cover-badge {
    display: inline-block;
    background: #fff1eb;
    color: #c15f3c;
    border: 1px solid #f97316;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.05em;
    padding: 3pt 8pt;
    border-radius: 20pt;
    text-transform: uppercase;
    margin-bottom: 14pt;
  }

  .cover-title {
    font-size: 30pt;
    font-weight: 800;
    line-height: 1.15;
    color: #0f172a;
    margin-bottom: 6pt;
    border-bottom: none;
    padding: 0;
  }

  .cover-subtitle {
    font-size: 13pt;
    font-weight: 400;
    color: #475569;
    margin-bottom: 20pt;
    line-height: 1.5;
    font-family: 'Newsreader', Georgia, serif;
    font-style: italic;
  }

  .cover-authors {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8pt;
    padding: 12pt 16pt;
    margin-bottom: 24pt;
    font-family: 'Inter', sans-serif;
  }

  .cover-authors-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10pt;
    margin-top: 6pt;
  }

  .cover-author-item strong {
    display: block;
    font-size: 8pt;
    text-transform: uppercase;
    color: #64748b;
  }

  .cover-author-item span {
    font-size: 10pt;
    font-weight: 600;
    color: #0f172a;
  }

  .chapter-break {
    page-break-before: always;
    padding-top: 10pt;
  }

  .callout {
    border-radius: 6pt;
    padding: 8pt 11pt;
    margin-top: 8pt;
    margin-bottom: 10pt;
    page-break-inside: avoid;
    font-size: 9pt;
    border-left: 3.5pt solid;
    font-family: 'Inter', sans-serif;
  }

  .callout-principle {
    background: #fff8f5;
    border-left-color: #d97757;
    color: #7c2d12;
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

  .callout-title {
    font-weight: 700;
    margin-bottom: 3pt;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 6pt;
    margin-bottom: 10pt;
    font-size: 8.5pt;
    font-family: 'Inter', sans-serif;
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

  .workflow-diagram {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6pt;
    padding: 10pt 14pt;
    margin: 8pt 0 12pt 0;
    page-break-inside: avoid;
    font-family: 'Inter', sans-serif;
  }

  .workflow-title {
    font-weight: 700;
    font-size: 9.5pt;
    color: #0f172a;
    margin-bottom: 6pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .flow-steps {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6pt;
    margin: 8pt 0;
  }

  .flow-box {
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 4pt;
    padding: 6pt 8pt;
    text-align: center;
    font-size: 8pt;
    font-weight: 600;
    flex: 1;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
  }

  .flow-box.active {
    border-color: #d97757;
    background: #fff8f5;
    color: #9a3412;
  }

  .flow-box.gate {
    border-color: #0284c7;
    background: #f0f9ff;
    color: #0369a1;
  }

  .flow-arrow {
    font-size: 10pt;
    font-weight: bold;
    color: #64748b;
  }

  .agenda-list {
    list-style: none;
    padding-left: 0;
    font-family: 'Inter', sans-serif;
  }

  .agenda-item {
    display: flex;
    justify-content: space-between;
    padding: 5pt 0;
    border-bottom: 1px dotted #cbd5e1;
    font-size: 9pt;
  }

  .agenda-item strong {
    color: #0f172a;
  }

  .agenda-item span {
    color: #64748b;
  }

  .tag {
    display: inline-block;
    padding: 1.5pt 5pt;
    border-radius: 3pt;
    font-size: 7.5pt;
    font-weight: 600;
    text-transform: uppercase;
    font-family: 'Inter', sans-serif;
  }
  .tag-workflow { background: #e0f2fe; color: #0369a1; }
  .tag-agent { background: #fee2e2; color: #b91c1c; }
  .tag-poka { background: #fef3c7; color: #b45309; }

</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div>
    <div class="cover-badge">Official Anthropic Architecture Series</div>
    <h1 class="cover-title">Building Effective Agents</h1>
    <div class="cover-subtitle">
      Architectural Patterns, Production Design Principles, and Implementation Frameworks for Reliable LLM Systems
    </div>

    <div class="cover-authors">
      <div style="font-size: 8.5pt; color: #475569; margin-bottom: 4pt;">
        <strong>Research & Engineering Whitepaper:</strong> Published by Anthropic
      </div>
      <div class="cover-authors-grid">
        <div class="cover-author-item">
          <strong>Authors</strong>
          <span>Erik Schluntz & Barry Zhang</span>
        </div>
        <div class="cover-author-item">
          <strong>Original Release</strong>
          <span>Anthropic Engineering Blog</span>
        </div>
        <div class="cover-author-item">
          <strong>Exam Relevance</strong>
          <span>Primary Blueprint Source (CCAR-F)</span>
        </div>
      </div>
    </div>

    <h3 class="sans" style="margin-top: 16pt; margin-bottom: 6pt;">Official Whitepaper Agenda</h3>
    <ul class="agenda-list">
      <li class="agenda-item">
        <strong>1. Executive Philosophy & What Are Agents?</strong>
        <span>Workflows vs. Agents Distinction</span>
      </li>
      <li class="agenda-item">
        <strong>2. When (and When Not) to Use Agents</strong>
        <span>The Latency, Cost, and Complexity Trade-off</span>
      </li>
      <li class="agenda-item">
        <strong>3. When and How to Use Frameworks</strong>
        <span>SDKs, Abstraction Layers, and Direct API Discipline</span>
      </li>
      <li class="agenda-item">
        <strong>4. The Foundational Building Block: The Augmented LLM</strong>
        <span>Retrieval, Memory, and Model Context Protocol (MCP)</span>
      </li>
      <li class="agenda-item">
        <strong>5. The 5 Core Workflow Patterns</strong>
        <span>Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator</span>
      </li>
      <li class="agenda-item">
        <strong>6. Autonomous Agents in Production</strong>
        <span>Execution Loops, Ground Truth, and Stopping Conditions</span>
      </li>
      <li class="agenda-item">
        <strong>7. The Three Core Principles for Effective Design</strong>
        <span>Simplicity, Transparency, and Agent-Computer Interfaces (ACI)</span>
      </li>
      <li class="agenda-item">
        <strong>8. Appendix 1: Agents in Practice</strong>
        <span>Customer Support Architectures & SWE-bench Verified Coding Agents</span>
      </li>
      <li class="agenda-item">
        <strong>9. Appendix 2: Prompt Engineering Your Tools (The ACI Handbook)</strong>
        <span>Poka-Yoke Tool Design, Absolute Paths, and Token Budgeting</span>
      </li>
      <li class="agenda-item">
        <strong>10. Anthropic Cookbook Implementation Blueprints</strong>
        <span>Runnable Python Implementations for Each Pattern</span>
      </li>
    </ul>
  </div>

  <div class="sans" style="border-top: 1px solid #e2e8f0; padding-top: 12pt; font-size: 8.5pt; color: #64748b; display: flex; justify-content: space-between;">
    <div>Anthropic Engineering Research & Architecture Guide</div>
    <div>Comprehensive Reference Edition · 2026</div>
  </div>
</div>

<!-- SECTION 1 & 2: WHAT ARE AGENTS & WHEN TO USE THEM -->
<div class="chapter-break">
  <h1>1. What Are Agents? Workflows vs. Agents</h1>
  
  <p>Over the past year, Anthropic worked with dozens of teams deploying large language model (LLM) agents across every major industry. Consistently, the most successful implementations were not using complex frameworks, multi-layered abstractions, or specialized libraries. Instead, they were building with <strong>simple, composable patterns</strong>.</p>

  <p>The term "Agent" has become overloaded in the industry. Some define agents as fully autonomous entities that operate independently over extended periods, exploring tools and environments to accomplish open-ended goals. Others use the term to describe deterministic pipelines that follow predefined steps. At Anthropic, we categorize all of these variations as <strong>agentic systems</strong>, but draw a fundamental architectural distinction:</p>

  <table>
    <thead>
      <tr>
        <th>System Type</th>
        <th>Architectural Definition</th>
        <th>Control Flow Paradigm</th>
        <th>System Properties</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Workflows</strong></td>
        <td>Systems where LLMs and tools are orchestrated through <strong>predefined code paths</strong>.</td>
        <td><strong>Deterministic & Code-Directed:</strong> Logic branches, validation steps, and sequences are dictated by your application code.</td>
        <td>Predictable, highly consistent, easy to test, lower latency, transparent error modes.</td>
      </tr>
      <tr>
        <td><strong>Agents</strong></td>
        <td>Systems where LLMs <strong>dynamically direct their own processes and tool usage</strong>.</td>
        <td><strong>Model-Directed:</strong> The model decides which tools to call, what arguments to pass, and when the task is finished based on intermediate results.</td>
        <td>Autonomous, flexible, handles unpredictable tasks, higher cost, potential for compounding errors.</td>
      </tr>
    </tbody>
  </table>

  <div class="callout callout-principle">
    <div class="callout-title">The First Principle of Agent Architecture: Simplicity First</div>
    When building applications with LLMs, always find the <strong>simplest solution possible</strong>, and only increase complexity when task performance demonstrably demands it. Often, this means <em>not building an agentic system at all</em>. For many production applications, optimizing a single LLM call with retrieval (RAG) and calibrated in-context examples is all that is required.
  </div>

  <h2>When (and When Not) to Use Agents</h2>
  <p>Agentic systems introduce an inescapable engineering trade-off: they <strong>trade latency and cost for better task performance</strong>. An autonomous agent that takes 8 turns calling tools will incur 8x to 15x higher token costs and substantially greater wall-clock latency than a single request.</p>

  <ul>
    <li><strong>When Workflows Are Better:</strong> Well-defined tasks with clear, sequential steps (e.g. document summarization, fixed support ticket triage, structured invoice extraction). Workflows provide predictability, strict latency ceilings, and straightforward debugging.</li>
    <li><strong>When Agents Are Better:</strong> Open-ended problems where it is impossible to predict the exact number of steps in advance, or where the optimal path depends entirely on intermediate discoveries (e.g. debugging a software repository across unknown files, recursive scientific literature research).</li>
  </ul>

  <h2>When and How to Use Frameworks</h2>
  <p>Many commercial and open-source frameworks aim to simplify agent development (including the Claude Agent SDK, AWS Strands, Rivet, and Vellum). While these tools make prototyping fast by abstracting tool parsing and message chaining, they frequently introduce <strong>thick layers of abstraction</strong> that obscure underlying prompts and responses.</p>
  <p>Anthropic's architectural recommendation is unambiguous: <strong>Start by using LLM APIs directly.</strong> Many foundational agentic patterns require only 30 to 50 lines of Python code. When you understand the raw API mechanics, you eliminate incorrect assumptions about what happens under the hood—which is the single most frequent cause of agent failure in production.</p>
</div>

<!-- SECTION 3: THE AUGMENTED LLM -->
<div class="chapter-break">
  <h1>2. The Foundational Building Block: The Augmented LLM</h1>

  <p>Every workflow and autonomous agent is constructed from one foundational primitive: <strong>The Augmented LLM</strong>. An augmented LLM is a frontier model enhanced with three core capabilities:</p>

  <ol>
    <li><strong>Retrieval:</strong> The ability to pull relevant context dynamically from vector databases, knowledge bases, or search APIs.</li>
    <li><strong>Tools:</strong> The ability to execute functions, query databases, make REST calls, and inspect environments via structured schemas.</li>
    <li><strong>Memory:</strong> The ability to maintain state, recall user preferences, and track scratchpads across multi-turn exchanges.</li>
  </ol>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Primitive: The Augmented LLM Architecture</span>
      <span class="tag tag-workflow">Core Building Block</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">User Input</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Frontier Model<br/>(Claude 3.5 / 3.7)</div>
      <div class="flow-arrow">&harr;</div>
      <div class="flow-box gate">Augmentations:<br/>Retrieval · Tools · Memory</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box">Augmented Output</div>
    </div>
  </div>

  <p>Modern Claude models do not merely respond to prompts—they actively command these augmentations by generating their own search queries, choosing appropriate tools from complex catalogs, and determining what facts to commit to memory.</p>

  <div class="callout callout-note">
    <div class="callout-title">Model Context Protocol (MCP) as the Standard ACI</div>
    To avoid writing custom, proprietary integration wrappers for every database and tool, Anthropic developed the <strong>Model Context Protocol (MCP)</strong>. MCP provides a universal, standardized protocol (over JSON-RPC 2.0) connecting LLM clients to external tools, resources, and prompt templates.
  </div>
</div>

<!-- SECTION 4: THE 5 CORE WORKFLOW PATTERNS -->
<div class="chapter-break">
  <h1>3. The 5 Core Workflow Patterns</h1>

  <p>Anthropic identifies five proven architectural patterns that structure how LLMs and tools interact to solve complex problems reliably.</p>

  <!-- PATTERN 1: PROMPT CHAINING -->
  <h2>Pattern 1: Prompt Chaining</h2>
  <p><strong>Mechanism:</strong> Prompt chaining decomposes a large task into a sequence of steps, where each LLM call processes the output of the preceding one. Programmatic validation checks ("gates") are inserted between steps to ensure intermediate quality before downstream computation occurs.</p>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Workflow 1: Prompt Chaining with Validation Gate</span>
      <span class="tag tag-workflow">Sequential Workflow</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">Input Prompt</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">LLM 1:<br/>Outline Draft</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Gate:<br/>Rule Check</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">LLM 2:<br/>Full Synthesis</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box">Final Output</div>
    </div>
  </div>

  <p><strong>When to Use:</strong> When a problem decomposes cleanly into fixed subtasks, and trading a small amount of latency for substantially higher accuracy is desirable. Example: Generating marketing copy, verifying compliance against legal guidelines, and translating into target languages.</p>

  <pre><code># Architectural Implementation: Prompt Chaining with Gate
def prompt_chain_workflow(client, document_text):
    # Step 1: Generate structured outline
    step1_res = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Extract key arguments into outline:\\n{document_text}"}]
    )
    outline = step1_res.content[0].text
    
    # Validation Gate: Programmatic check
    if len(outline.splitlines()) < 3:
        raise ValueError("Gate Failed: Outline lacks sufficient structural depth.")
        
    # Step 2: Expand outline into final executive brief
    step2_res = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        messages=[{"role": "user", "content": f"Write an executive brief using this outline:\\n{outline}"}]
    )
    return step2_res.content[0].text
</code></pre>

  <!-- PATTERN 2: ROUTING -->
  <h2>Pattern 2: Routing</h2>
  <p><strong>Mechanism:</strong> Routing classifies an input and directs it to a specialized downstream prompt, tool set, or model tier. This prevents prompt interference, where optimizing a single prompt for one use case degrades its performance on others.</p>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Workflow 2: Routing Classification & Dispatch</span>
      <span class="tag tag-workflow">Classification Workflow</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">User Query</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Router / Classifier<br/>(Haiku or Regex)</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Path A: Billing (Haiku)<br/>Path B: Technical (Sonnet)<br/>Path C: Legal (Opus)</div>
    </div>
  </div>

  <p><strong>When to Use:</strong> Complex domains with distinct categories that require separate tools and prompts. It is also the primary mechanism for cost/latency optimization: routing 80% of common queries to cost-efficient models (Haiku) and reserving advanced models (Sonnet/Opus) for high-complexity requests.</p>
</div>

<!-- PATTERN 3, 4, 5 -->
<div class="chapter-break">
  <h2>Pattern 3: Parallelization (Sectioning & Voting)</h2>
  <p><strong>Mechanism:</strong> Running multiple LLM calls concurrently and aggregating their outputs programmatically. Anthropic highlights two distinct implementations:</p>
  <ul>
    <li><strong>Sectioning:</strong> Breaking a large task into independent, parallel subtasks. For example, running security guardrail checks concurrently with main answer generation.</li>
    <li><strong>Voting:</strong> Executing the same task multiple times with varying prompts or temperatures to achieve consensus, reducing false positives in vulnerability scanning or content moderation.</li>
  </ul>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Workflow 3: Parallelization (Sectioning vs. Voting)</span>
      <span class="tag tag-workflow">Concurrent Workflow</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">Input Prompt</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Worker 1 (Syntax)<br/>Worker 2 (Security)<br/>Worker 3 (Performance)</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Programmatic<br/>Aggregator / Voter</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box">Unified Result</div>
    </div>
  </div>

  <!-- PATTERN 4: ORCHESTRATOR-WORKERS -->
  <h2>Pattern 4: Orchestrator-Workers</h2>
  <p><strong>Mechanism:</strong> A central Orchestrator LLM dynamically analyzes the user's request, determines what subtasks are necessary, delegates them to Worker subagents, and synthesizes the returned findings into a coherent response.</p>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Workflow 4: Dynamic Orchestrator-Workers</span>
      <span class="tag tag-workflow">Hierarchical Multi-Agent</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">Complex Goal</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Orchestrator LLM<br/>(Task Decomposition)</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Dynamic Workers:<br/>[Subagent 1] [Subagent 2]</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Orchestrator Synthesis</div>
    </div>
  </div>

  <p><strong>Key Distinction from Parallelization:</strong> Parallelization uses pre-defined static subtasks; the Orchestrator-Workers pattern determines subtasks dynamically based on the input (e.g. deciding which 4 files out of a 2,000-file repository must be edited to implement a feature).</p>

  <!-- PATTERN 5: EVALUATOR-OPTIMIZER -->
  <h2>Pattern 5: Evaluator-Optimizer</h2>
  <p><strong>Mechanism:</strong> A generator LLM produces a solution, and a separate evaluator LLM critiques it against explicit rubrics, providing actionable feedback in a loop until quality criteria are satisfied or iteration limits are reached.</p>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Workflow 5: Evaluator-Optimizer Iterative Loop</span>
      <span class="tag tag-workflow">Feedback Loop</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">Task Request</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Generator LLM</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Evaluator LLM<br/>(Meets Rubric?)</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box">Final Approved Result</div>
    </div>
  </div>

  <p><strong>When to Use:</strong> Tasks with clear, articulable evaluation criteria where iterative human-style refinement measurably improves the result (e.g. complex translation, code generation with test feedback, high-stakes executive correspondence).</p>
</div>

<!-- SECTION 5: AUTONOMOUS AGENTS -->
<div class="chapter-break">
  <h1>4. Autonomous Agents in Production</h1>

  <p>Agents emerge when frontier models can plan, use tools reliably, observe environmental feedback, and recover from errors in a dynamic loop. In an autonomous agent architecture, the model operates in a continuous turn cycle:</p>

  <ol>
    <li><strong>Interactive Direction:</strong> The user gives a high-level command or converses with the agent to set objectives.</li>
    <li><strong>Execution Loop:</strong> The agent calls tools to inspect the environment (running terminal commands, reading files, querying APIs).</li>
    <li><strong>Ground Truth Observation:</strong> Crucially, the agent receives <strong>ground truth from the environment</strong> (standard error streams, tool outputs, HTTP status codes) to calibrate its progress.</li>
    <li><strong>Engineered Termination:</strong> The task terminates either upon completion or when an engineered stopping condition (e.g. maximum iteration cap, stall detection) triggers human escalation.</li>
  </ol>

  <div class="workflow-diagram">
    <div class="workflow-title">
      <span>Production Autonomous Agent Loop</span>
      <span class="tag tag-agent">Autonomous Cycle</span>
    </div>
    <div class="flow-steps">
      <div class="flow-box">Task Command</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box active">Reasoning & Tool Selection</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box gate">Environment Execution<br/>(Bash / Files / APIs)</div>
      <div class="flow-arrow">&rarr;</div>
      <div class="flow-box">Ground Truth Feedback</div>
    </div>
  </div>

  <h2>Anthropic Case Studies: Coding Agents & Computer Use</h2>
  <ul>
    <li><strong>SWE-bench Verified Coding Agent:</strong> Anthropic built an autonomous agent capable of resolving complex real-world GitHub issues based solely on the pull request issue description. The agent navigates the repository, writes tests, reproduces bugs, edits source code, and iterates until the test suite passes.</li>
    <li><strong>Computer Use:</strong> A reference architecture where Claude observes screen pixels, moves the mouse cursor, clicks elements, and types keyboard input to interact with software applications natively.</li>
  </ul>

  <div class="callout callout-warning">
    <div class="callout-title">Compounding Errors and Sandboxing</div>
    The autonomous nature of agents introduces compounding error risks: a mistake in step 2 cascades into hallucinations in step 5. Always run autonomous agents inside sandboxed execution environments with non-root permissions, strict network boundaries, and human-in-the-loop checkpoints for irreversible actions.
  </div>

  <h1>5. The Three Core Principles for Effective Design</h1>

  <div class="callout callout-principle">
    <div class="callout-title">Principle 1: Maintain Simplicity in Design</div>
    Do not add orchestration frameworks, complex DAGs, or multi-turn agent loops when a single prompt or simple prompt chain solves the problem. Every added layer of agency increases latency, token expense, and debug complexity.
  </div>

  <div class="callout callout-principle">
    <div class="callout-title">Principle 2: Prioritize Transparency</div>
    Make the agent's internal planning and reasoning visible. Log every tool call, input schema, tool result, and intermediate thought step. If users and operators cannot inspect what the agent is doing, they cannot trust it.
  </div>

  <div class="callout callout-principle">
    <div class="callout-title">Principle 3: Carefully Craft the Agent-Computer Interface (ACI)</div>
    Just as human-computer interface (HCI) design dictates software usability for people, ACI design dictates usability for LLMs. Invest as much effort into tool descriptions, parameter names, and error payloads as you do into overall system prompts.
  </div>
</div>

<!-- SECTION 6: APPENDICES -->
<div class="chapter-break">
  <h1>6. Appendix 1: Agents in Practice</h1>

  <p>Anthropic's customer engagements identified two primary commercial domains where autonomous agents deliver measurable production ROI:</p>

  <h2>A. Customer Support Resolution Agents</h2>
  <p>Customer support combines conversational interfaces with deterministic backend actions. Key architectural principles:</p>
  <ul>
    <li><strong>Tool Integration:</strong> Expose read tools (<code>lookup_customer</code>, <code>check_order_status</code>) and write tools (<code>update_shipping_address</code>, <code>issue_refund</code>).</li>
    <li><strong>Hard Policy Enforcement:</strong> Never ask the model in a prompt to enforce refund caps. Enforce limits deterministically in the tool code (e.g. rejecting refunds > $200 with <code>isError: true</code> and routing to human agents).</li>
    <li><strong>Outcome-Based Pricing Models:</strong> Enterprises are shifting to usage-based pricing that charges customers only for successful first-contact ticket resolutions.</li>
  </ul>

  <h2>B. Autonomous Coding Agents</h2>
  <p>Software engineering is an ideal agent domain because solutions are objectively verifiable via unit tests. Key architectural principles:</p>
  <ul>
    <li><strong>Feedback Loops:</strong> The agent runs test commands, inspects stack traces, and iterates on code edits until tests pass.</li>
    <li><strong>Human Review Gates:</strong> While automated tests verify functional correctness, human code review remains mandatory to verify architecture fit, performance, and maintainability.</li>
  </ul>

  <h1>7. Appendix 2: Prompt Engineering Your Tools (The ACI Handbook)</h1>

  <p>Anthropic discovered while building the SWE-bench agent that <strong>optimizing tool interfaces yielded larger performance gains than tweaking system prompts</strong>. Key guidelines:</p>

  <table>
    <thead>
      <tr>
        <th>Design Principle</th>
        <th>Problem / Anti-Pattern</th>
        <th>Architectural Solution</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Thinking Room</strong></td>
        <td>Model generates output immediately without planning token budget.</td>
        <td>Allow the model to emit reasoning blocks (or thinking mode) before committing to tool parameters.</td>
      </tr>
      <tr>
        <td><strong>Natural Formats</strong></td>
        <td>Requiring rigid multi-line escaping (e.g. escaping JSON newlines inside code strings).</td>
        <td>Use formats natural to pre-training (e.g. markdown blocks or simple file rewrites rather than intricate unified diffs).</td>
      </tr>
      <tr>
        <td><strong>Eliminate Counting Overhead</strong></td>
        <td>Unified diff tools that require the model to count line additions before writing code.</td>
        <td>Use string-replacement tools (<code>old_string</code> / <code>new_string</code>) that do not require counting lines.</td>
      </tr>
      <tr>
        <td><strong>Poka-Yoke Tool Design</strong></td>
        <td>Relative file paths (<code>../../foo.py</code>) fail when the agent navigates into subdirectories.</td>
        <td>Design tools to <strong>strictly require absolute file paths</strong>. Anthropic found this single change completely eliminated path errors in SWE-bench.</td>
      </tr>
      <tr>
        <td><strong>Docstring Discipline</strong></td>
        <td>Vague tool descriptions (e.g. <code>"Reads a file"</code>).</td>
        <td>Write tool descriptions like docstrings for a junior engineer: define exact parameter types, default behaviors, edge cases, and boundaries from adjacent tools.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- SECTION 7: CODE NOTEBOOK BLUEPRINTS -->
<div class="chapter-break">
  <h1>8. Anthropic Cookbook: Reference Implementations</h1>
  <p>The following production Python scripts represent the reference implementations for the core patterns from Anthropic's official cookbook repository.</p>

  <h2>1. The Complete ReAct-Style Autonomous Agent Loop</h2>
  <pre><code>import json
from anthropic import Anthropic

client = Anthropic()

def execute_tool(tool_name, tool_args):
    # Deterministic backend tool router
    if tool_name == "lookup_order":
        order_id = tool_args.get("order_id")
        if order_id == "ORD-123":
            return {"status": "shipped", "carrier": "FedEx", "tracking": "12345678"}, False
        return {"error": "Order not found", "retryable": False}, True
    elif tool_name == "process_refund":
        amount = tool_args.get("amount", 0)
        # Deterministic policy enforcement in the tool layer
        if amount > 200:
            return {"error": "Amount exceeds autonomous limit ($200). Escalation required.", "retryable": False}, True
        return {"status": "refund_approved", "transaction_id": "TXN-999"}, False
    return {"error": f"Unknown tool: {tool_name}"}, True

def run_agent(task_prompt, tools, max_turns=10):
    messages = [{"role": "user", "content": task_prompt}]
    
    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            tools=tools,
            messages=messages
        )
        
        # Check termination condition
        if response.stop_reason == "end_turn":
            return response.content[0].text
            
        elif response.stop_reason == "tool_use":
            # Append assistant's turn
            messages.append({"role": "assistant", "content": response.content})
            
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result_data, is_err = execute_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result_data),
                        "is_error": is_err
                    })
            
            # Feed tool results back as a single user turn
            messages.append({"role": "user", "content": tool_results})
            
    return "Error: Maximum turns reached without task completion."
</code></pre>

  <h2>2. The Evaluator-Optimizer Feedback Pattern</h2>
  <pre><code>def evaluator_optimizer_loop(task_description, rubric, max_iterations=3):
    current_solution = ""
    feedback = "Initial generation."
    
    for iteration in range(max_iterations):
        # 1. Generator LLM
        gen_prompt = f"Task: {task_description}\\nPrevious Feedback: {feedback}\\nGenerate improved solution:"
        gen_res = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": gen_prompt}]
        )
        current_solution = gen_res.content[0].text
        
        # 2. Evaluator LLM
        eval_prompt = f"Rubric:\\n{rubric}\\n\\nCandidate Solution:\\n{current_solution}\\n\\nDoes it pass? Output PASS or provide feedback:"
        eval_res = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": eval_prompt}]
        )
        critique = eval_res.content[0].text
        
        if "PASS" in critique:
            return current_solution, iteration + 1
        feedback = critique
        
    return current_solution, max_iterations
</code></pre>

  <div class="callout callout-tip" style="margin-top: 14pt;">
    <div class="callout-title">Summary Takeaway for Architects</div>
    True mastery of the Anthropic ecosystem lies in knowing <strong>when not to build an agent</strong>. Use single prompts when possible; compose workflows when predictability and latency matter; deploy autonomous agents only when dynamic, environmental exploration is strictly necessary.
  </div>
</div>

</body>
</html>
"""

with open("anthropic_architectural_whitepaper.html", "w", encoding="utf-8") as f:
    f.write(whitepaper_html)

print("Whitepaper HTML written! Now compiling to PDF via headless Google Chrome...")

cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf=Anthropic_Architectural_Whitepaper_Building_Effective_Agents.pdf",
    "anthropic_architectural_whitepaper.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

if os.path.exists("Anthropic_Architectural_Whitepaper_Building_Effective_Agents.pdf"):
    size = os.path.getsize("Anthropic_Architectural_Whitepaper_Building_Effective_Agents.pdf")
    print(f"Whitepaper PDF generated successfully! Size: {size/1024:.1f} KB")
else:
    print("Failed to generate PDF:", res.stderr)
