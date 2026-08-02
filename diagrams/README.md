# Architecture Diagrams

Six Excalidraw scenes, one per project. **Native Excalidraw elements** — every box, label and arrow is editable, movable, and re-drawable by hand.

## Opening them

Go to **[excalidraw.com](https://excalidraw.com)** → **File → Open** → pick a `.excalidraw` file. No account, no plugin. (Same file also opens in the Excalidraw VS Code extension.)

| File | Project | Use it for |
|---|---|---|
| `01-aml-ctf-compliance-rag.excalidraw` | AML/CTF Compliance Knowledge Assistant | **Your lead deep-dive.** Sole ownership, no client attribution risk |
| `02-indic-voice-agent.excalidraw` | Real-Time Indic Voice Agent | "Hardest technical problem" · voice-AI roles · the latency-budget story |
| `03-enterprise-rag-knowledge-assistant.excalidraw` | Enterprise RAG (KNS) | Defending the −40% / −30% and +35% claims |
| `04-agentic-coding-assistant.excalidraw` | Agentic Coding Assistant (Turing) | Agent design rounds · the −45% turnaround claim |
| `05-offline-air-gapped-training-envs.excalidraw` | Offline AI Training Environments (Turing) | Your rarest asset — evals, verifiable rewards, air-gapped delivery |
| `06-student-performance-ml-platform.excalidraw` | Student Performance ML Platform | Surviving the classical-ML probe on the ~85% claim |

## What's in each one

Beyond the architecture itself, each scene carries the **interview scaffolding** for that project:

- 🟨 **Yellow dashed notes** — the framing or metric story to lead with
- 🟥 **Red dashed notes** — the trap, the design decision to defend, or the thing to volunteer *before* you're asked
- 🟦 **Blue dashed notes** — scale reasoning and timeline corrections
- ⬜ **Grey dashed notes** — the follow-up questions this design invites

Blanks like `recall@5 ___` and `___ ms` are deliberate. **Fill them with your real measurements** — same rule as the answer files: never present a number you can't source.

## How to actually use these

**Don't present the file.** The point is that you can **redraw the core of any of these from memory, on a blank Excalidraw canvas, in about 3 minutes** while talking. That's what the deep-dive round tests.

Practice loop:
1. Open the finished diagram. Study it once.
2. New blank canvas. Redraw it cold, out loud, timed.
3. Diff against the original. Whatever you missed goes in tomorrow's warm-up.

Strip the notes when you present — they're prep scaffolding, not part of the architecture. Delete them, or move them far off-canvas before you share your screen.

**One layout habit worth keeping:** left-to-right pipeline, ingest lane on top, query lane in the middle, eval lane at the bottom. Reuse that skeleton for design prompts you've never seen — having a track to run on is most of the battle in a 45-minute round.
