"""The ordered document table that drives the whole build.

Explicit, not globbed. Three reasons:
  1. it resolves the DAILY-CHECKLIST.md name collision (root vs ai-engineering/)
  2. it gives deterministic nav order and prev/next chains
  3. it is where the visibility flag lives

`visibility` is one of:
  "public"   — published
  "private"  — published, but sensitive; sits behind the passphrase gate like
               everything else. Kept as a marker for a future public/private split.
  "archived" — NOT built into the site. The file stays in the repo and in git;
               it just stops being published. Flip it back to publish again.

Archived in Oct 2026 when the focus narrowed to three things: the Anthropic
certification, interview preparation, and skills. Everything archived below is
either an elapsed plan, a past engagement, or a duplicate of something kept.
"""

# (src, out, section, title_override, visibility)
DOCS = [
    # ---- Interview prep -------------------------------------------------
    ("ai-engineer-interviews/CHECKLIST.md",
     "ai-engineer-interviews/checklist.html", "Interview prep",
     "AI Engineer Interview Checklist", "public"),
    ("ai-engineer-interviews/real-questions.md",
     "ai-engineer-interviews/real-questions.html", "Interview prep",
     "Real Questions Asked", "public"),
    ("story-bank.md",
     "story-bank.html", "Interview prep",
     "Story Bank", "private"),

    # ---- Metric defence -------------------------------------------------
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

    # ---- Resources ------------------------------------------------------
    ("resources.md",
     "resources.html", "Resources",
     "Resources — buy list, canon, traps", "public"),
    ("ai-engineer-interviews/resources.md",
     "ai-engineer-interviews/resources.html", "Resources",
     "Resources by interview round", "public"),

    # ---- Diagrams -------------------------------------------------------
    ("diagrams/README.md",
     "diagrams/index.html", "Diagrams",
     "Architecture Diagrams", "private"),

    # ---- Archived: not built into the site ------------------------------
    # Two competing 28-day sprints, both with a blank start date, both elapsed
    # since late August. The tracker's repeating-routine model replaced them.
    ("DAILY-CHECKLIST.md",
     "daily-checklist.html", "Daily plans",
     "28-Day Interview Sprint", "archived"),
    ("ai-engineering/DAILY-CHECKLIST.md",
     "ai-engineering/daily-checklist.html", "Daily plans",
     "28-Day AI Engineering Sprint", "archived"),
    # An acknowledged subset of the root resources.md.
    ("ai-engineering/resources.md",
     "ai-engineering/resources.html", "Resources",
     "AI Engineering — Builder's Canon", "archived"),
    # Job-search logistics (outreach targets, company tiers, referees, comp).
    # That is getting interviews, not preparing for them.
    ("pipeline.md",
     "pipeline.html", "Story & narrative",
     "Pipeline", "archived"),
    # One specific interview, 5 Aug 2026.
    ("accenture/question-bank.md",
     "accenture/question-bank.html", "Company-specific",
     "Accenture — Question Bank", "archived"),
    ("accenture/answer-frameworks.md",
     "accenture/answer-frameworks.html", "Company-specific",
     "Accenture — Answer Frameworks", "archived"),
    ("accenture/claim-defence-card.md",
     "accenture/claim-defence-card.html", "Company-specific",
     "Accenture — Claim Defence Card", "archived"),
]

# Hand-written card descriptions, keyed by output path.
#
# The library index otherwise shows each doc's first sentence, and several of
# those still said "Do this Days 1-2" / "Build Days 3-5" — pointing at the
# 28-day sprint that is now archived. An extracted sentence is a reasonable
# default; it is not a substitute for saying what a document is for.
DESCRIPTIONS = {
    "ai-engineer-interviews/checklist.html":
        "What each interview round actually tests, built from first-hand accounts. Read by round, not end to end.",
    "ai-engineer-interviews/real-questions.html":
        "Verbatim questions, ranked by how often they recur, each attributed to a company and date.",
    "story-bank.html":
        "Behavioural answers: the coverage matrix, the stories you are missing, and the recruiter script.",
    "answers/metric-defence.html":
        "The index. Every number on your resume, how it was measured, and whether it survives being pushed on.",
    "answers/01-latency-and-cost.html":
        "-40% latency and -30% cost: prefill vs decode, the mechanism split, and the \u201cdid quality regress?\u201d follow-up.",
    "answers/02-relevance-and-agent-success.html":
        "+35% relevance and +20% agent success: judge validation, pass^k, and the attribution problem.",
    "answers/03-turnaround-and-effort.html":
        "-45% review turnaround and -60% tagging effort. Contains the MCP timeline trap.",
    "answers/04-sklearn-accuracy.html":
        "The ~85% accuracy claim \u2014 the longest follow-up chain of any number you cite.",
    "answers/05-scale-and-narrative.html":
        "Scale claims, the 2014-vs-8-years gap, the Turing overlap, and the universal closing moves.",
    "resources.html":
        "What to buy, what is free and worth it, and the well-reviewed things that are a trap.",
    "ai-engineer-interviews/resources.html":
        "The same material, mapped to the interview round it actually prepares you for.",
    "diagrams/index.html":
        "Six system architectures to redraw from memory before a design round.",
}

SECTION_ORDER = [
    "Interview prep",
    "Metric defence",
    "Resources",
    "Diagrams",
]

# Standalone app pages that are not markdown-derived but do appear in nav.
APP_PAGES = [
    ("index.html", "Tracker", "The certification blueprint, the syllabus, and the resource library"),
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
