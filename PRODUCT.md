# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
One user: Dinesh, a senior AI/ML engineer preparing for the Claude Certified Architect – Foundations exam (CCAR-F) and AI engineer interviews. He uses the tracker every day: ticking the daily routine as the day goes, then grading syllabus items as he learns them. Nobody else uses it; it sits behind a passphrase.

## Product Purpose
A personal study tracker that turns a fixed daily routine and a researched syllabus into one checklist. **The near-term goal is passing CCAR-F**; AI engineer interview prep (tracks 02–12) comes second. Success = the exam passed, with every syllabus item graded honestly on the three-state scale (not started → read it → can explain cold).

## Positioning
Not a generic to-do or flashcard app. Every item is tied to one specific source to learn from and one concrete practice task with a pass condition. Grading is about whether you can explain something without notes, not whether you read it.

## Operating Context
- Track 00 "Today" resets at local midnight; syllabus grades persist.
- Tracks: 01 CCAR-F blueprint, 02–10 syllabus, 11 interview rounds, 12 resource library, plus links to the rendered library (`library.html`, question bank, metric defence, real questions, diagrams).
- Progress is cached in the browser (`mt.v3`, `mt.days.v2`) and synced to Turso via Vercel functions (`api/`). The JSON backup in the drawer is the real backup.
- Source of truth is `master-tracker.html`; `python3 build/build.py` (needs pandoc 3) writes `public/`, which is committed and served by Vercel with no build step.

## Capabilities and Constraints
- **Dated, verified sources only** (confirmed by the user). Every resource is first-hand or official, carries a date, and is HTTP-checked (`build/sources/check.py`). No listicles or course-funnel content.
- From the code (not separately confirmed): item text and group titles are hashed into storage keys (`idFor`), so rewording them orphans saved grades. Add or remove items freely; change only meta/source/practice/evidence slots of existing ones.
- From the code: installable PWA with a service worker and offline page; regression harnesses in `build/dev/` (`_func`, `_regress`, `_sync`; 46 checks) must keep passing.

## Evidence on Hand
- Syllabus content and per-item sources: `master-tracker.html`, `build/sources/curriculum.py`, `build/sources/sources.py`, `build/sources/tables/`.
- Supporting documents: `answers/`, `ai-engineer-interviews/`, `diagrams/`, `story-bank.md`, `resource-refresh-2026-10.md`.
- No testimonials, metrics or external users exist; future work must not invent them.

## Product Principles
1. The exam comes first: CCAR-F material (track 01 and the block C slot) outranks interview extras when space or attention is limited.
2. An unverified resource is worse than no resource: every new item needs a date and a working first-hand or official link.
3. Grades are the user's record: no change may silently reset, reinterpret or orphan them.
4. Tick, don't read: the daily view exists to be acted on quickly; reference material lives one tap away, not on the checklist.
