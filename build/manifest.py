"""The ordered document table that drives the whole build.

Explicit, not globbed. Three reasons:
  1. it resolves the DAILY-CHECKLIST.md name collision (root vs ai-engineering/)
  2. it gives deterministic nav order and prev/next chains
  3. it is where the public/private visibility flag lives

`visibility` is carried but unused today — the whole library ships in one dist/.
It exists so a public/private split is a one-flag change later.
"""

# (src, out, section, title_override, visibility)
DOCS = [
    ("DAILY-CHECKLIST.md",
     "daily-checklist.html", "Daily plans",
     "28-Day Interview Sprint", "private"),
    ("ai-engineering/DAILY-CHECKLIST.md",
     "ai-engineering/daily-checklist.html", "Daily plans",
     "28-Day AI Engineering Sprint", "public"),
    ("ai-engineer-interviews/CHECKLIST.md",
     "ai-engineer-interviews/checklist.html", "Daily plans",
     "AI Engineer Interview Checklist", "public"),

    ("answers/metric-defence.md",
     "answers/metric-defence.html", "Metric defence",
     "Metric Defence Dossier", "private"),
    ("answers/01-latency-and-cost.md",
     "answers/01-latency-and-cost.html", "Metric defence",
     "Claims 1 & 2 — Latency & Cost", "private"),
    ("answers/02-relevance-and-agent-success.md",
     "answers/02-relevance-and-agent-success.html", "Metric defence",
     "Claims 3 & 5 — Relevance & Agent Success", "private"),
    ("answers/03-turnaround-and-effort.md",
     "answers/03-turnaround-and-effort.html", "Metric defence",
     "Claims 4 & 6 — Turnaround & Tagging Effort", "private"),
    ("answers/04-sklearn-accuracy.md",
     "answers/04-sklearn-accuracy.html", "Metric defence",
     "Claim 7 — scikit-learn accuracy", "private"),
    ("answers/05-scale-and-narrative.md",
     "answers/05-scale-and-narrative.html", "Metric defence",
     "Scale claims & the narrative", "private"),

    ("story-bank.md",
     "story-bank.html", "Story & narrative",
     "Story Bank", "private"),
    ("pipeline.md",
     "pipeline.html", "Story & narrative",
     "Pipeline", "private"),

    ("ai-engineer-interviews/real-questions.md",
     "ai-engineer-interviews/real-questions.html", "Question banks",
     "Real Questions Asked", "public"),

    ("resources.md",
     "resources.html", "Resources",
     "Resources — buy list, canon, traps", "public"),
    ("ai-engineering/resources.md",
     "ai-engineering/resources.html", "Resources",
     "AI Engineering — Builder's Canon", "public"),
    ("ai-engineer-interviews/resources.md",
     "ai-engineer-interviews/resources.html", "Resources",
     "Resources by interview round", "public"),

    ("accenture/question-bank.md",
     "accenture/question-bank.html", "Company-specific",
     "Accenture — Question Bank", "private"),
    ("accenture/answer-frameworks.md",
     "accenture/answer-frameworks.html", "Company-specific",
     "Accenture — Answer Frameworks", "private"),
    ("accenture/claim-defence-card.md",
     "accenture/claim-defence-card.html", "Company-specific",
     "Accenture — Claim Defence Card", "private"),

    ("diagrams/README.md",
     "diagrams/index.html", "Diagrams",
     "Architecture Diagrams", "private"),
]

SECTION_ORDER = [
    "Daily plans",
    "Metric defence",
    "Story & narrative",
    "Question banks",
    "Resources",
    "Company-specific",
    "Diagrams",
]

# Standalone app pages that are not markdown-derived but do appear in nav.
APP_PAGES = [
    ("index.html", "Tracker", "The daily routine, the syllabus, and the resource library"),
    ("questions.html", "Resume Question Bank", "Every question your resume invites"),
]

# Diagrams, in gallery order. Rendered to SVG by excalidraw_svg.py.
DIAGRAMS = [
    ("diagrams/01-aml-ctf-compliance-rag.excalidraw",
     "AML/CTF Compliance Knowledge Assistant",
     "Your lead deep-dive. Sole ownership, no client attribution risk"),
    ("diagrams/02-indic-voice-agent.excalidraw",
     "Real-Time Indic Voice Agent",
     "The latency-budget story"),
    ("diagrams/03-enterprise-rag-knowledge-assistant.excalidraw",
     "Enterprise RAG Knowledge Assistant",
     "Defends the −40% / −30% / +35% claims"),
    ("diagrams/04-agentic-coding-assistant.excalidraw",
     "Agentic Coding Assistant",
     "The −45% review-turnaround claim"),
    ("diagrams/05-offline-air-gapped-training-envs.excalidraw",
     "Offline AI Training Environments",
     "Air-gapped evaluation and RL gyms"),
    ("diagrams/06-student-performance-ml-platform.excalidraw",
     "Student Performance ML Platform",
     "The ~85% accuracy claim"),
]

# Referenced from markdown but deliberately not published. Links to these are
# unwrapped to plain text rather than left dangling.
UNPUBLISHED = {"tracker.csv", "daily-log.csv",
               "Kadiam_Rao_Resume.docx",
               "Kadiam_Rao_Resume.backup-pre-restructure.docx"}
