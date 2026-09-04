# Claim Defence Card — read this last, ~15 minutes before

Every number on your resume is a question waiting to be asked. `answers/metric-defence.md` has the full drill; this is the compressed version for today.

**The 30-second test:** metric definition + baseline + n + who measured + biggest confounder. If you can't do that for a number, **don't lead with the number** — give the qualitative claim and offer the method. A dropped number costs nothing. A collapsed one is a trust finding, and trust findings don't recover in a debrief.

---

## The numbers, and what to say

| Claim | Say this | If pressed hard |
|---|---|---|
| **~35% answer relevance ↑** (10k-doc RAG) | Measured on a held-out eval set — class B. Name who labelled it. | Drop to "materially better on our eval set" + describe the harness |
| **~40% latency ↓** | Split the mechanism: prompt/context reduction vs caching. Say which dominated. | Name it as measured on p50 from tracing over N weeks, or declare it directional |
| **~30% cost ↓** | Same mechanism split; cost per request, not total spend | "Did quality regress?" is the killer follow-up — have the answer |
| **~45% review turnaround ↓** (coding assistant) | Turnaround = PR opened → first review complete. Give the baseline. | Attribution: your contribution vs the team's |
| **~20% agent task success ↑** | Post-benchmark, against the rubric you wrote | Judge validation — how did you know the eval was right |
| **~60% tagging effort ↓** | Manual hours before/after | Directional if you didn't time-track it — say so |
| **~85% accuracy** (student ML, 50k records) | Accuracy on what split, what baseline, class balance | ⚠️ Your own dossier flags this as the longest follow-up chain. Know precision/recall, not just accuracy |
| **10k docs / 1M events per day / 50k records** | Scale claims — just be sure the units are right | These are usually safe; don't inflate them under pressure |

---

## The three narrative landmines

**"8+ years, but B.Tech 2014."** One number, tied to 2016 (freelance start), one line, no apology. Say it the same way every time it comes up.

**Turing (Jan 2024–Jan 2025) overlapping KNS (Aug 2023–present).** Volunteer it in ~25 seconds before they find it: part-time contract engagement alongside the full-time role, disclosed, no conflict. Waiting to be caught is what makes it look like something.

**MCP timeline.** Announced 25 Nov 2024; Turing engagement ended Jan 2025. Say "adopted it in the last stretch of that engagement." Never imply it spanned the whole thing.

---

## Measurement classes — declare honestly

- **A — Instrumented:** continuously measured in production, dashboard exists
- **B — Sampled/evaluated:** measured on an eval set or sample
- **C — Directional:** reasoned from partial data

Proactively saying "that one's directional, and here's what I'd instrument to make it real" reads as *more* senior, not less. Being caught presenting a C as an A is fatal.

---

## The anti-rehearsal rule

A technical claim is only worth making if you can attach one concrete, slightly boring detail — a bug, a column name, an argument you had, a number that came out wrong. Recited depth with no texture reads as *studied*, and an interviewer who suspects that will probe one level lower until you break. **No texture → one sentence, then move on.**

---

## Logistics — 15:00–16:00 IST today

- Join link is in the "Your Interview has been successfully Scheduled" email from Interview.Schedule@accenture.com
- **Log in at 14:50.** They say 10 minutes early, and setup delays are on you
- Camera and mic on throughout; stay clearly in frame
- Recorded and audited. No second screen, no external assistance — Accenture's terms are explicit that this disqualifies you from this role and future ones
- Have water, a pen, and your own two questions for them

**Last thing before you join:** close the prep files. Everything you're going to use is already in your head by then, and having them open only invites the eye-drift that interviewers read as reading.

Good luck.
