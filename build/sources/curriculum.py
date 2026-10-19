"""Per-item learning sources, produced by a 37-agent research workflow and
adversarially verified (191 confirmed, 66 corrected, 3 rejected).
Regenerate labels from scratchpad/research.json; see DEPLOY.md."""
CURRICULUM = {
 "t03": [
  {
   "item": "Progressive multi-level class design",
   "label": "Fluent Python · Ch 11 'A Pythonic Object' → Ch 12 'Speci…",
   "url": "https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md",
   "full": "Ch 11 'A Pythonic Object' → Ch 12 'Special Methods for Sequences' → Ch 14 'Inheritance: For Better or For Worse' — build the object, extend it into a sequence, then reshape it under inheritance, which is the same shape as the round. The round format itself (implementation rounds, 45–90 min, levels that build on your earlier code) is described in https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md"
  },
  {
   "item": "asyncio.Semaphore for bounded concurrency",
   "label": "Fluent Python · Ch 21 'Asynchronous Programming' (Part I…",
   "url": "https://docs.python.org/3/library/asyncio-sync.html",
   "full": "Ch 21 'Asynchronous Programming' (Part IV, Control Flow) for the async model. The exact idiom an interviewer wants to see is in the Python docs, https://docs.python.org/3/library/asyncio-sync.html — 'The preferred way to use a Semaphore is an async with statement': sem = asyncio.Semaphore(10), then 'async with sem:'. Semaphore(value=1), counter never below zero, and it is not thread-safe."
  },
  {
   "item": "Retry with exponential backoff, as a decorator",
   "label": "Fluent Python · Ch 9 'Decorators and Closures' for the p…",
   "url": "https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits",
   "full": "Ch 9 'Decorators and Closures' for the parameterised-decorator mechanics. The backoff policy is not in the book — take it from https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits §'Retrying with exponential backoff', which gives three versions: tenacity, @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6)); backoff, @backoff.on_exception(backoff.expo, openai.RateLimitError, max_time=60, max_tries=6); and a dependency-free retry_with_exponential_backoff with initial_delay, exponential_base, jitter and max_retries."
  },
  {
   "item": "The GIL, and asyncio vs threading vs multiprocessing",
   "label": "Fluent Python · Ch 19 'Concurrency Models in Python' is…",
   "url": "https://docs.python.org/3/howto/free-threading-python.html",
   "full": "Ch 19 'Concurrency Models in Python' is this question end to end, then Ch 20 'Concurrent Executors'. Currency patch, because the book is 2022: https://docs.python.org/3/howto/free-threading-python.html — free-threaded CPython exists from 3.13 (PEP 703), the GIL can be re-enabled at runtime via PYTHON_GIL or -X gil, sysconfig.get_config_var('Py_GIL_DISABLED') == 1 is the build check and sys._is_gil_enabled() the process check."
  },
  {
   "item": "Mutability, lists vs tuples, and the shared-mutable-default trap",
   "label": "Fluent Python · Ch 6 'Object References, Mutability, and…",
   "url": "https://www.fluentpython.com/",
   "full": "Ch 6 'Object References, Mutability, and Recycling' for aliasing, copies and defaults, plus Ch 2 'An Array of Sequences' for lists vs tuples. Two-minute version if you are short on time: Effective Python 3rd ed Item 30 'Know That Function Arguments Can Be Mutated' and Item 36 'Use None and Docstrings to Specify Dynamic Default Arguments'."
  },
  {
   "item": "OOP fundamentals — __init__, abstraction, inheritance, composition over inheritance",
   "label": "Fluent Python · Ch 11 'A Pythonic Object', Ch 13 'Interf…",
   "url": "https://www.fluentpython.com/",
   "full": "Ch 11 'A Pythonic Object', Ch 13 'Interfaces, Protocols, and ABCs', Ch 14 'Inheritance: For Better or For Worse'. For the composition-over-inheritance answer specifically, the crisper formulations are Effective Python 3rd ed Item 48 'Accept Functions Instead of Classes for Simple Interfaces', Item 49 'Prefer Object-Oriented Polymorphism over Functions with isinstance Checks' and Item 54 'Consider Composing Functionality with Mix-in Classes'."
  },
  {
   "item": "REST semantics — PUT vs PATCH, status codes, FastAPI dependency injection",
   "label": "FastAPI docs tutorial, §'Body - Updates…",
   "url": "https://fastapi.tiangolo.com/tutorial/body-updates/",
   "full": "not in primary — FastAPI docs tutorial, §'Body - Updates' (https://fastapi.tiangolo.com/tutorial/body-updates/): PUT replaces, and its own worked example shows an omitted field silently reset to the model default (stored tax 20.2 becomes 10.5), while PATCH is item.model_dump(exclude_unset=True) then stored_item_model.model_copy(update=update_data). Then §'Dependencies' (https://fastapi.tiangolo.com/tutorial/dependencies/) for Depends() and its five sub-pages: Classes as Dependencies, Sub-dependencies, Dependencies in path operation decorators, Global Dependencies, Dependencies with yield."
  },
  {
   "item": "Generators and lazy evaluation for memory-bounded processing",
   "label": "Fluent Python · Ch 17 'Iterators, Generators, and Classi…",
   "url": "https://www.fluentpython.com/",
   "full": "Ch 17 'Iterators, Generators, and Classic Coroutines' (Part IV, Control Flow). Compressed version: Effective Python 3rd ed Item 43 'Consider Generators Instead of Returning Lists', Item 44 'Consider Generator Expressions for Large List Comprehensions' and Item 45 'Compose Multiple Generators with yield from'."
  },
  {
   "item": "Pydantic v2 and typing",
   "label": "Pydantic v2 docs, Concepts → Models: the…",
   "url": "https://pydantic.dev/docs/validation/latest/concepts/models/",
   "full": "not in primary — Pydantic v2 docs, Concepts → Models: https://pydantic.dev/docs/validation/latest/concepts/models/ then Fields, Validators, Serialization and JSON. Note the host moved: docs.pydantic.dev/latest/concepts/models/ now returns 301 to this address, so any 2024 bookmark is stale. For the typing half, Effective Python Item 124 'Consider Static Analysis via typing to Obviate Bugs' plus Ch 7 Items 51 and 56 on dataclasses."
  },
  {
   "item": "Context managers",
   "label": "Effective Python · Ch 10 'Robustness', Item 82 'Consider co…",
   "url": "https://effectivepython.com/",
   "full": "Ch 10 'Robustness', Item 82 'Consider contextlib and with Statements for Reusable try/finally Behavior', with Item 80 'Take Advantage of Each Block in try/except/else/finally' read before it and Item 89 'Always Pass Resources into Generators and Have Callers Clean Them Up Outside' after it."
  },
  {
   "item": "pytest — fixtures, parametrize, and mocking the LLM client",
   "label": "Ch 13 Items 108–115 teach unittest, not…",
   "url": "https://docs.pytest.org/en/stable/how-to/fixtures.html",
   "full": "not in primary — Ch 13 Items 108–115 teach unittest, not pytest. Use the official how-to guides: 'How to use fixtures' (https://docs.pytest.org/en/stable/how-to/fixtures.html), whose own sections cover Scope and conftest.py sharing, Autouse fixtures, Teardown via yield, and Parametrizing fixtures; then 'How to monkeypatch/mock modules and environments' (https://docs.pytest.org/en/stable/how-to/monkeypatch.html) §'Monkeypatching returned objects: building mock classes', which patches requests.get with a MockResponse and then moves that patch into a fixture — exactly the shape of mocking an LLM client — plus §'Global patch example' for the autouse conftest fixture that blocks all HTTP in tests."
  },
  {
   "item": "Dunder methods beyond __init__",
   "label": "Effective Python · Ch 8 'Metaclasses and Attributes', Items…",
   "url": "https://effectivepython.com/",
   "full": "Ch 8 'Metaclasses and Attributes', Items 58–66 — in particular 59 'Consider @property Instead of Refactoring Attributes', 60 'Use Descriptors for Reusable @property Methods', 61 'Use __getattr__, __getattribute__, and __setattr__ for Lazy Attributes', 62–63 on __init_subclass__ and 64 'Annotate Class Attributes with __set_name__' — plus Ch 7 Item 57 'Inherit from collections.abc Classes for Custom Container Types'. For the operator-overloading half, Fluent Python Ch 16 'Operator Overloading'."
  },
  {
   "item": "Pythonic idioms",
   "label": "Effective Python · Ch 1 'Pythonic Thinking', Items 1–9 (PEP…",
   "url": "https://effectivepython.com/",
   "full": "Ch 1 'Pythonic Thinking', Items 1–9 (PEP 8, helper functions over complex expressions, multiple-assignment unpacking, conditional expressions, assignment expressions, match for destructuring), then Ch 5 'Functions' Items 30–39 and Ch 6 'Comprehensions and Generators' Items 40–47."
  },
  {
   "item": "Metaclasses",
   "label": "Python Language Reference · §3.3.3.1 'Metaclasses', reached as 3 Dat…",
   "url": "https://docs.python.org/3/reference/datamodel.html",
   "full": "§3.3.3.1 'Metaclasses', reached as 3 Data model → 3.3 Special method names → 3.3.3 Customizing class creation. Read it, write three sentences, stop. If an interviewer pushes to 'would you actually use one?', the answer is Effective Python 3rd ed Item 66, 'Prefer Class Decorators over Metaclasses for Composable Class Extensions'; one level deeper is Fluent Python Ch 24 'Class Metaprogramming'."
  },
  {
   "item": "Memory model",
   "label": "Python Language Reference · §3.1 'Objects, values and types'",
   "url": "https://docs.python.org/3/reference/datamodel.html",
   "full": "§3.1 'Objects, values and types' — 'An object's identity never changes once it has been created; you may think of it as the object's address in memory' (so id() and is), mutable versus immutable value, and the implementation note that 'CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references'. That last clause is the whole answer to why reference cycles delay collection."
  },
  {
   "item": "Async batch client: 100 prompts, ≤20 concurrent, retry with backoff, collect partial results",
   "label": "openai-cookbook, examples/api_request_pa…",
   "url": "https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/api_request_parallel_processor.py",
   "full": "not in primary — openai-cookbook, examples/api_request_parallel_processor.py (https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/api_request_parallel_processor.py): this drill already solved, with asyncio.create_task over one shared aiohttp session, max_attempts defaulting to 5, and the input streamed so a large job never lands in memory. One caveat I verified in the source and you must fix yourself: its retries are NOT exponentially backed off — a failure goes straight back on the retry queue, and the only pause is 15s after a rate-limit error — so take the backoff decorator from https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits. Then rewrite it blind with asyncio.Semaphore(20) and gather(..., return_exceptions=True) for partial results."
  },
  {
   "item": "SSE streaming handler that accumulates partial JSON into a validated Pydantic model",
   "label": "two pages",
   "url": "https://fastapi.tiangolo.com/tutorial/server-sent-events/",
   "full": "not in primary — two pages. FastAPI §'Server-Sent Events (SSE)' (https://fastapi.tiangolo.com/tutorial/server-sent-events/, added in FastAPI 0.135.0) for the wire format: text/event-stream, EventSourceResponse, ServerSentEvent with event/id/retry, raw_data for a [DONE] sentinel, and resuming via the Last-Event-ID header. Then Pydantic §'JSON' (https://pydantic.dev/docs/validation/latest/concepts/json/) for the accumulate half: pydantic_core.from_json(data, allow_partial=True) then model_validate. Know the two gotchas it states — model_validate_json and TypeAdapter.validate_json do not support partial parsing yet, and every field should have a default."
  },
  {
   "item": "Token-bucket rate limiter for tokens, not requests",
   "label": "the same openai-cookbook script, api_req…",
   "url": "https://www.deep-ml.com/problems",
   "full": "not in primary — the same openai-cookbook script, api_request_parallel_processor.py, whose docstring line is 'Throttles request and token usage, to stay under rate limits'. It holds two separate budgets, available_request_capacity and available_token_capacity, refilled from elapsed time against max_requests_per_minute (default 1,500) and max_tokens_per_minute (default 125,000), and fires only when both allow. That refill-on-elapsed-time pattern is the token bucket; rewrite it from scratch against a monotonic clock."
  },
  {
   "item": "Tool-dispatch loop with retries and a step budget",
   "label": "Anthropic, 'Building effective agents' (…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "not in primary — Anthropic, 'Building effective agents' (https://www.anthropic.com/engineering/building-effective-agents, 19 Dec 2024), which names your step budget in as many words: 'it's also common to include stopping conditions (such as a maximum number of iterations)'. Read it for the loop shape only — the page now carries its own banner that 'Much of the tooling landscape described in this post has changed since December 2024', so do not copy its API details."
  },
  {
   "item": "Cosine similarity and top-k in NumPy, batched",
   "label": "Deep-ML · problem 76, 'Calculate Cosine Similarity…",
   "url": "https://www.deep-ml.com/problems/76",
   "full": "Deep-ML problem 76, 'Calculate Cosine Similarity Between Vectors' (https://www.deep-ml.com/problems/76) for the metric itself — but that problem is pairwise, not batched, so get the batching from Python Data Science Handbook §02.08 'Sorting Arrays' (https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html), whose k-nearest-neighbours example builds the whole pairwise matrix in one expression, np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1), then uses np.argsort(dist_sq, axis=1) and the cheaper np.argpartition(dist_sq, K + 1, axis=1). Normalise then matmul instead of squared distance and you have batched cosine top-k."
  },
  {
   "item": "BM25 and Reciprocal Rank Fusion (Σ 1/(60+rank)) from scratch",
   "label": "Deep-ML · BM25: Deep-ML problem 90, 'BM25 Ranking…",
   "url": "https://www.deep-ml.com/problems/90",
   "full": "BM25: Deep-ML problem 90, 'BM25 Ranking' (https://www.deep-ml.com/problems/90), with the formula from Introduction to Information Retrieval (Manning, Raghavan & Schütze, CUP 2008, free online edition), 'Okapi BM25: a non-binary model' (https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html) — implement its Equation (86), and note the book's recommended k1 between 1.2 and 2 with b = 0.75. RRF is not on Deep-ML: use the original two-page paper, Cormack, Clarke & Büttcher, 'Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods', SIGIR'09 (http://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf), §1 — RRFscore(d) = Σ over r in R of 1/(k + r(d)), with 'k = 60 was fixed during a pilot investigation and not altered during subsequent validation'."
  },
  {
   "item": "LRU cache in O(1), from a blank file, twice",
   "label": "Python docs, collections, §'OrderedDict…",
   "url": "https://docs.python.org/3/library/collections.html",
   "full": "not in primary — Python docs, collections, §'OrderedDict Examples and Recipes' (https://docs.python.org/3/library/collections.html), whose TimeBoundedLRU and MultiHitLRUCache recipes are pass one: move_to_end(args) on a hit, popitem(last=False) to evict the least recently used entry. Pass two is the same semantics with a plain dict plus a hand-rolled doubly linked list and sentinel node, which is what the interviewer is actually checking."
  },
  {
   "item": "In-memory KV store with TTL, then transactions, then nested transactions",
   "label": "no book covers this; it is a multi-level…",
   "url": "https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md",
   "full": "not in primary — no book covers this; it is a multi-level implementation round. The problem statement is the field guide's, verbatim: 'Build a key-value database starting with basic operations (SET/GET/DELETE)' (https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md). Copy the semantics from SQLite §SAVEPOINT (https://www.sqlite.org/lang_savepoint.html) — savepoints form a stack, RELEASE of an inner savepoint 'does not cause any changes to be written to the database file', and ROLLBACK TO reverts while 'The SAVEPOINT with the matching name remains on the transaction stack' — and from Redis §Transactions (https://redis.io/docs/latest/develop/using-commands/transactions/) for MULTI/EXEC/DISCARD/WATCH and the design argument that 'Redis does not support rollbacks of transactions since supporting rollbacks would have a significant impact on the simplicity and performance of Redis'. Implement nesting as a stack of overlay dicts."
  },
  {
   "item": "Refactor 100–120 lines of deeply nested code into something testable",
   "label": "Emily Bache's GildedRose Refactoring Kat…",
   "url": "https://github.com/emilybache/GildedRose-Refactoring-Kata",
   "full": "not in primary — Emily Bache's GildedRose Refactoring Kata (https://github.com/emilybache/GildedRose-Refactoring-Kata), the python/ folder: it is this drill as a standing exercise, and the README's 'Text-Based Approval Testing' section gives you the TextTest fixture so you can pin behaviour before you touch anything. Its stated discipline is also the scoring rubric — small steps, run the tests often, improve the design incrementally rather than rewriting. Name each move out loud as you make it (guard clause, extract function, decompose conditional); that is half the score."
  },
  {
   "item": "Logistic regression with SGD, L2 and early stopping, in NumPy",
   "label": "Deep-ML · Four Deep-ML problems that together are…",
   "url": "https://www.deep-ml.com/problems/106",
   "full": "Four Deep-ML problems that together are this drill: 106 'Train Logistic Regression with Gradient Descent' (https://www.deep-ml.com/problems/106), 104 'Binary Classification with Logistic Regression' (https://www.deep-ml.com/problems/104), 43 'Implement Ridge Regression Loss Function' (https://www.deep-ml.com/problems/43) for the L2 term, and 135 'Implement Early Stopping Based on Validation Loss' (https://www.deep-ml.com/problems/135). Do them separately, then write the whole thing once from a blank file against a stopwatch."
  },
  {
   "item": "Deep-ML.com — free, 100+ graded from-scratch problems, linear algebra through attention",
   "label": "Deep-ML · live, and enter instead via for the pace…",
   "url": "https://www.deep-ml.com/problems",
   "full": "https://www.deep-ml.com/problems — live, and enter instead via https://www.deep-ml.com/interview-prep for the paced path. Correct your syllabus note with care rather than a new number: the site's own navigation advertises '1,200+ hands-on ML problems' while the body text of the same page still says '100+ machine learning coding challenges', so both figures are unreliable. What is verifiable: category filters for linear algebra, machine learning, deep learning, NLP and computer vision, difficulty filters, a separate Math section, and a Premium tier whose price the page does not state. Use the linear-algebra set for drill 5 and the retrieval problems for drill 6."
  },
  {
   "item": "openai/openai-cookbook",
   "label": "Deep-ML · live, MIT, 76.7k stars, 'Examples and gu…",
   "url": "https://github.com/openai/openai-cookbook",
   "full": "https://github.com/openai/openai-cookbook — live, MIT, 76.7k stars, 'Examples and guides for using the OpenAI API', and the README points to its rendered home at cookbook.openai.com. Only two things here matter for this syllabus: examples/api_request_parallel_processor.py (concurrency, separate request and token throttling, retries) and the rate-limit guide, which renders at https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits and holds the tenacity, backoff and hand-rolled retry decorators."
  },
  {
   "item": "ai-engineering-field-guide → interview/questions/02-coding.md",
   "label": "Deep-ML · live, and verifiably the source of your…",
   "url": "https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md",
   "full": "https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/interview/questions/02-coding.md — live, and verifiably the source of your drill list: it names 'Refactor 100-120 lines of convoluted, deeply nested code', 'Build a key-value database starting with basic operations (SET/GET/DELETE)', 'LRU Cache with O(1) time complexity' and 'Implement logistic regression with SGD, L2 regularization, and early stopping in NumPy'. Use it to generate drills and timings, accepting two things: it ships questions with no solutions, and it is internally inconsistent on the algorithm-round clock (25–70 min in its overview, 15–60 min in its detail section). The implementation-round figure, 45–90 min with levels that build, is consistent."
  },
  {
   "item": "TensorGym — supplementary only",
   "label": "Tensor Puzzles (srush) — TensorGym retired",
   "url": "https://github.com/srush/Tensor-Puzzles",
   "full": "DEAD — delete it from the syllabus. https://tensorgym.com/ now states 'TensorGym has retired' and that 'The interactive exercises and accounts are no longer available'. Two replacements, depending on budget: free, srush/Tensor-Puzzles (https://github.com/srush/Tensor-Puzzles) — 21 broadcasting puzzles, one line each under 80 columns, with view, sum, take, squeeze and tensor banned, MIT-licensed and runnable in Colab, which is exactly the index-gymnastics muscle TensorGym trained; or paid, CodeCrafters (the backup below) for systems-flavoured implementation rounds."
  }
 ],
 "t04": [
  {
   "item": "Self-attention, from scratch on paper",
   "label": "Stanford CME 295 · Lecture 1 : 55:18 Attention → 57:16 Self…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 1 (youtu.be/114i2Kz-LZA): 55:18 Attention → 57:16 Self-attention mechanism → 59:54 Query, key, value = slides 58-62 of cme295.stanford.edu/slides/fall26-cme295-lecture1.pdf. Then work slides 80-115, the 36-slide 'Stitching all the pieces together with an example' (video 1:27:35), by hand on paper — that run of slides is this item."
  },
  {
   "item": "Causal masking, and why decoder-only won",
   "label": "Stanford CME 295 · Masking: Lecture 1 at 1:22:16 'Computati…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Masking: Lecture 1 at 1:22:16 'Computational tricks' = slide 75, titled 'Computational trick: masking'. Why decoder-only won: Lecture 2 (youtu.be/GaIeu3npx04) 04:47 BERT and encoder-only models → 13:47 GPT and decoder-only models → 16:10 'Encoder-decoder versus decoder-only' = slides 18-21."
  },
  {
   "item": "Multi-head attention — what the heads buy you",
   "label": "Stanford CME 295 · Lecture 1, 1:22:16-1:27:35 = slide 76…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 1, 1:22:16-1:27:35 = slide 76, 'Computational trick: multi-head attention'. Then Lecture 2 at 1:13:15 'Group Query Attention (GQA)' = slides 80-83 'Sharing attention heads', which is where MHA → MQA → GQA and the memory argument for sharing them live."
  },
  {
   "item": "Positional encoding: sinusoidal → learned → RoPE, and why rotation generalises to longer contexts",
   "label": "Stanford CME 295 · Lecture 2: 45:36 'Position embeddings…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 2: 45:36 'Position embeddings' → 1:01:58 'Rotary position embeddings (RoPE)'. Slides 52-54 need for position info, 55-65 hardcoded/sinusoidal and learned, 66-67 'From absolute to relative position info', 68-69 linear bias in the attention layer, 70-73 'Default choice nowadays: rotations in attention layer', and slide 74 'Attention weight has a long-term decay' — slide 74 is the one that answers the 'why does rotation generalise' half of the question."
  },
  {
   "item": "Encoder-only vs decoder-only vs encoder-decoder, and when each is right",
   "label": "Stanford CME 295 · Lecture 2, 04:47 → 13:47 → 16:10, the th…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 2, 04:47 → 13:47 → 16:10, the three families back to back in twenty minutes = slides 5-21: slide 7 'Transformer variant: encoder-only', 8-17 BERT, 18 'Transformer variant: decoder-only', 19 GPT, 20-21 'Encoder-decoder versus decoder-only'."
  },
  {
   "item": "The seven deltas from the 2017 paper to a modern Llama block",
   "label": "Stanford CME 295 · Lecture 2 gives six of them with timesta…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 2 gives six of them with timestamps: 29:05 MoE, 1:01:58 RoPE, 1:09:28 Sliding Window Attention, 1:13:15 GQA, 1:18:13 Pre-Norm versus Post-Norm, 1:19:41 LayerNorm versus RMSNorm (= slides 84-88, ending on 'Evolution of normalization'). It never covers the gated feedforward (SwiGLU) or the dropping of bias terms — for those two, and for the deltas written out as one enumerated list with ablation data, read CS336 Spring 2026 lecture_03.pdf (github.com/stanford-cs336/lectures) slides 3-29: slide 3 'the original transformer' → 4 'simple, modern variant' → 10-13 pre-vs-post norm → 14-17 RMSNorm → 18 'More generally: dropping bias terms' → 20-26 gated activations (*GLU) → 27-28 serial vs parallel layers → 29 'Summary: architectures'."
  },
  {
   "item": "Mixture of Experts — what it is and what it buys",
   "label": "Stanford CME 295 · Lecture 2: 29:05 'Mixture of experts (Mo…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Lecture 2: 29:05 'Mixture of experts (MoE)' → 33:11 'MoE-based LLMs' → 36:03 'Load balancing loss' = slides 36-50: 36-39 motivation, 40-41 overview, 42-43 MoE in transformer-based models, 44-45 'Training challenges include routing collapse', 46 'Interpreting experts', 47-50 recent trends."
  },
  {
   "item": "Attention is O(n²) — what Flash Attention and sparse attention actually change",
   "label": "Stanford CME 295 · Sparse attention IS in the primary: Lect…",
   "url": "https://cme295.stanford.edu/syllabus/",
   "full": "Sparse attention IS in the primary: Lecture 2 at 1:09:28 = slides 75-79, 'Sparse attention: Longformer' and 'Leveraging local and global attention'. Flash Attention is not — CME 295's own Flash Attention lecture is Lecture 5 'LLM systems', scheduled 30 Oct 2026 and not yet posted. So for Flash Attention: not in primary — Stanford CS336 Spring 2026, Lecture 5 'GPUs, TPUs', lecture_05.pdf slides 50-56 (Part 3 'Using what we know to understand Flash Attention': slide 52 tiling the KQV matmul, 53 'incremental computation of the softmax', 54 'Putting it all together – the forward pass of flash attention')."
  },
  {
   "item": "Tokenization: BPE vs WordPiece vs SentencePiece",
   "label": "Jurafsky & Martin SLP3 · Ch 2 §2.4 'Subword Tokenization: Byte-Pa…",
   "url": "https://web.stanford.edu/~jurafsky/slp3/",
   "full": "Ch 2 §2.4 'Subword Tokenization: Byte-Pair Encoding' (p. 10), with §2.4.1 BPE training (p. 11), §2.4.2 BPE encoder (p. 13), §2.4.3 'BPE in practice' (pp. 13-15: byte-level BPE over UTF-8, GPT-4o's 200K vocabulary, the tiktokenizer visualiser), plus §2.6.9 'Regular Expressions for BPE pre-tokenization' (p. 23). Note the real limit: SLP3 names unigram LM and SentencePiece only in a footnote on p. 11 and never covers WordPiece at all. For the three-way comparison with a runnable from-scratch implementation of each, use Hugging Face LLM Course chapter 6: huggingface.co/learn/llm-course/chapter6/6 is the WordPiece section (score-based merge rule, longest-subword-first tokenizing), with BPE and Unigram/SentencePiece either side of it at /chapter6/5 and /chapter6/7."
  },
  {
   "item": "What the context window is, what happens when you exceed it, and how it gets extended",
   "label": "Jurafsky & Martin SLP3 · Ch 7 §7.4 'The input: embeddings for tok…",
   "url": "https://web.stanford.edu/~jurafsky/slp3/",
   "full": "Ch 7 §7.4 'The input: embeddings for token and position' (pp. 15-17) defines N as the context length and shows why learned absolute position embeddings degrade at the tail; §7.7 (pp. 25-26) on training by filling the whole window. Extension is genuinely absent from SLP3 — no interpolation, no YaRN, no extrapolation anywhere in Ch 7 — so for that, MIT 6.5940 Fall 2024 Lecture 15 'Long Context LLM' deck (Lec15-Long-Context-LLM.pdf, linked from hanlab.mit.edu/courses/2024-fall-65940): slides 4-5 relative positional encoding, 7-12 LongLoRA, 16-17 Needle-In-A-Haystack and LongBench for what failure looks like, 22-38 the attention-sink phenomenon and StreamingLLM."
  },
  {
   "item": "The KV cache: what it stores, why it makes generation linear rather than quadratic, and how to estimate its size",
   "label": "Jurafsky & Martin SLP3 · Ch 7 §7.8 'Current models and some numbe…",
   "url": "https://web.stanford.edu/~jurafsky/slp3/",
   "full": "Ch 7 §7.8 'Current models and some numbers' (p. 28, Fig 7.23) covers the first two clauses — what gets stored and why you stop recomputing keys and values for every prior token. Sizing is not in SLP3: for that, CS336 Spring 2026 lecture_10.py 'Inference' (raw.githubusercontent.com/stanford-cs336/lectures/main/lecture_10.py), which states the cache shape as 'for every sequence (B), token (S), layer (L), head (K), store an H-dimensional vector' and then writes the formula out as kv_cache_size_per_seq = S * (K*H) * L * 2 * 2 (2 for key plus value, 2 for bf16); its reduce_kv_cache_size section adds 'GQA reduces the KV cache by a factor of N/K'."
  },
  {
   "item": "Sampling: temperature, top-k, top-p, and what each does to the distribution",
   "label": "Jurafsky & Martin SLP3 · Ch 7 §7.6 'Decoding' in full (pp. 20-25)…",
   "url": "https://web.stanford.edu/~jurafsky/slp3/",
   "full": "Ch 7 §7.6 'Decoding' in full (pp. 20-25): 7.6.1 greedy decoding, 7.6.2 random sampling, 7.6.3 temperature sampling, 7.6.4 top-k and top-p sampling. Then do Exercise 7.5 on p. 32 — 'With the logits in Fig. 7.17, compute the probabilities at τ = 0.2 and τ = 2. Verify each sums to 1. What happens as τ → 0? As τ → ∞?' — which is exactly this item said out loud."
  },
  {
   "item": "Why hallucinations happen, and the distinct forms they take",
   "label": "the word 'hallucination' does not occur…",
   "url": "https://web.stanford.edu/~jurafsky/slp3/",
   "full": "not in primary — the word 'hallucination' does not occur once in SLP3 chapters 2, 7 or 9. Use Andrej Karpathy, 'Deep Dive into LLMs like ChatGPT' (youtube.com/watch?v=7xTGNNLPyMI, 3h31, Feb 2025), the 45-minute run from 1:20:32 'hallucinations, tool use, knowledge/working memory' → 1:41:46 'knowledge of self' → 1:46:56 'models need tokens to think' → 2:01:11 'tokenization revisited: models struggle with spelling' → 2:04:53 'jagged intelligence'. That stretch is the taxonomy."
  },
  {
   "item": "The lifecycle: pretraining → SFT → reward model → RLHF, and where DPO short-circuits it",
   "label": "MIT 6.5940 · Lecture 14 'LLM Post-Training' , 77 min…",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "Lecture 14 'LLM Post-Training' (youtu.be/OCdwWfVoQ-Q, 77 min; deck Lec14-LLM-Post-training.pdf) slides 5 SFT, 7-9 RLHF, 10-11 DPO — but this is the thinnest part of the lecture, five slides for the whole chain. For the decision-depth version, CME 295 Fall 2026 Lecture 3 (youtu.be/S3bCDcJhz4s): 03:36 Pretraining → 22:18 Midtraining → 31:47 Supervised finetuning → 46:37 Preference tuning → 54:44 Bradley-Terry formulation (the reward model) → 1:01:49 RLHF → 1:05:38 DPO, then 1:20:56 GRPO and 1:23:31 on-policy distillation, which a 2024 course cannot have."
  },
  {
   "item": "LoRA: ΔW = BA, B zero-initialised, the α/r ratio, which modules to target, merge vs multi-LoRA serving",
   "label": "MIT 6.5940 · Lecture 14 slides 27-30 give four of the…",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "Lecture 14 slides 27-30 give four of the five sub-parts verbatim: 'A: projects d dim to low-rank r dim, initialized with gaussian distribution. B: projects low-rank r dim back to d dim, initialized 0s', then h = x@W + x@A@B, then the merge x@(W + A@B) = x@W′ with the line 'Thus no extra inference latency!'; slides 31-35 practical cases, 40-42 BitDelta multi-tenant serving. The α/r ratio and which modules to target are not there — for which modules, CME 295 Lecture 3 at 40:15, slides 55-56 'Locations where to apply LoRA', whose second slide is headed 'Updated guidance. As done and recommended nowadays' with 'most important location' marked, citing Schulman et al., 'LoRA Without Regret', 2025; for alpha/rank in code, the LoRALayer class in github.com/rasbt/LLMs-from-scratch appendix-E/01_main-chapter-code/appendix-E.ipynb."
  },
  {
   "item": "QLoRA and PEFT — when parameter-efficient beats full fine-tuning",
   "label": "MIT 6.5940 · Lecture 14 slides 13-25, the PEFT family…",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "Lecture 14 slides 13-25, the PEFT family in order — BitFit (13-15) → TinyTL lite residual learning (16) → Adapter (17-19) → Prompt tuning (20-22) → Prefix-tuning (23-24) → slide 25 'Parameter-Efficient Fine-Tuning', the comparison slide that is the actual answer to 'when does it beat full fine-tuning'. Then slides 36-39 for QLoRA: NF4, double quantization of the scaling factors, and paged optimizers."
  },
  {
   "item": "Quantization: int8, int4, GPTQ/AWQ — and why accuracy holds up better than intuition suggests",
   "label": "MIT 6.5940 · Lecture 6 'Quantization Part II' , 68 mi…",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "Lecture 6 'Quantization Part II' (youtu.be/wrcgWm_nUeE, 68 min; deck Lec06-Quantization-II.pdf) slides 3-49: K-means vs linear quantization (4-9), post-training quantization and granularity (10-28, including per-channel 16-20 and group quantization 23-28), dynamic range for activations (30-38), adaptive rounding (40-42), post-training INT8 (44-45), QAT (46-49). Then Lecture 13 'LLM Deployment Techniques' (youtu.be/sTz2tXG1T0c, 76 min; deck Lec13-LLM-Deployment.pdf) slides 4-17 SmoothQuant and 19-33 AWQ — slide 26 is literally titled 'Why AWQ reduces quantization error?', which is the 'why accuracy holds up' half of this item."
  },
  {
   "item": "Catastrophic forgetting, and how instruction tuning mitigates it",
   "label": "neither MIT lecture names it",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "not in primary — neither MIT lecture names it. CS336 Spring 2026 lecture_15.pdf (github.com/stanford-cs336/lectures) slides 29-30: slide 29 'Turning instruction tuning into pretraining' lays out the three-step recipe (pre-train on web data → mix instruction-tuning data into pre-training → a short real instruction-tuning round) and ends on the line 'Lets you scale up instruction tuning w/o catastrophic forgetting'; slide 30 'Midtraining / Two-phase training' names it as the undocumented common practice."
  },
  {
   "item": "Scaling laws and the compute-vs-data tradeoff, at a conversational level",
   "label": "MIT 6.5940 never covers scaling laws",
   "url": "https://hanlab.mit.edu/courses/2024-fall-65940",
   "full": "not in primary — MIT 6.5940 never covers scaling laws. CME 295 Fall 2026 Lecture 2 (youtu.be/GaIeu3npx04) at 19:23 'Scaling laws' = slides 23-28 of fall26-cme295-lecture2.pdf: 23 'Better performance with bigger models and more data', 24 'Bigger models are more token efficient', 25-26 notations, 27-28 'Takeaways on compute-optimal training'. Six slides, which is exactly the conversational level this item asks for."
  },
  {
   "item": "Karpathy, micrograd — typed line by line, then rewritten from a blank file",
   "label": "Karpathy, Zero to Hero · Lecture 1, 'The spelled-out intro to neu…",
   "url": "https://karpathy.ai/zero-to-hero.html",
   "full": "Lecture 1, 'The spelled-out intro to neural networks and backpropagation: building micrograd' (youtu.be/VMj-3S1tku0, 2h25): 19:09 starting the core Value object and its visualization → 32:10 manual backpropagation example #1 → 52:52 example #2, a neuron → 1:09:02 implementing the backward function for each operation → 1:22:28 fixing a backprop bug when one node is used multiple times → 1:43:55 building out the MLP library → 2:01:12 doing gradient descent manually → 2:16:46 walkthrough of the full code on GitHub. Rewrite from blank against github.com/karpathy/micrograd."
  },
  {
   "item": "Karpathy, “Let's build GPT” and nanoGPT",
   "label": "Karpathy, Zero to Hero · Lecture 7, 'Let's build GPT: from scratc…",
   "url": "https://karpathy.ai/zero-to-hero.html",
   "full": "Lecture 7, 'Let's build GPT: from scratch, in code, spelled out' (youtube.com/watch?v=kCc8FmEb1nY, 1h56): 42:13 averaging past context with for loops → 47:11 the matmul trick → 54:42 adding softmax → 1:00:18 positional encoding → 1:02:00 'THE CRUX OF THE VIDEO: version 4: self-attention' → 1:11:38-1:16:56 the six notes, ending on 'why divide by sqrt(head_size)' → 1:21:59 multi-headed self-attention → 1:24:25 feedforward → 1:26:48 residual connections → 1:32:51 layernorm → 1:46:22 nanoGPT walkthrough. Code: github.com/karpathy/ng-video-lecture. One currency warning that matters: nanoGPT's own README now reads 'nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity' and points to github.com/karpathy/nanochat instead — so watch the nanoGPT walkthrough for the ideas, but do the actual reproduction against github.com/karpathy/build-nanogpt or nanochat."
  },
  {
   "item": "A 30-line MLP training loop from memory, twice",
   "label": "Karpathy, Zero to Hero · Lecture 3, 'Building makemore Part 2: ML…",
   "url": "https://karpathy.ai/zero-to-hero.html",
   "full": "Lecture 3, 'Building makemore Part 2: MLP' (youtu.be/TCH_1BHY58I, 1h15): 32:17 summary of the full network → 32:49 introducing F.cross_entropy and why → 37:56 implementing the training loop, overfitting one batch → 41:25 training on the full dataset, minibatches → 45:40 finding a good initial learning rate → 53:20 splitting into train/val/test and why. The stretch from 32:17 to 45:40 is the thing to reproduce from memory; if your second attempt silently fails to learn, lecture 4 (Activations & Gradients, BatchNorm) is the diagnosis."
  },
  {
   "item": "Causal multi-head attention on a whiteboard, from memory, recorded",
   "label": "Karpathy, Zero to Hero · Lecture 7 again, the two specific marks:…",
   "url": "https://karpathy.ai/zero-to-hero.html",
   "full": "Lecture 7 again, the two specific marks: 1:02:00 'version 4: self-attention' for the masked single head built with tril, and 1:21:59 'multi-headed self-attention' for stacking them. Watch once, record yourself without it, then check the recording against 1:11:38-1:16:56 — the six notes are the follow-up questions an interviewer asks after you finish drawing."
  },
  {
   "item": "rasbt/LLMs-from-scratch — Appendix A, Ch 2 and Ch 3, typed",
   "label": "appendix-A/01_main-chapter-code ('Introd…",
   "url": "https://karpathy.ai/zero-to-hero.html",
   "full": "not in primary — github.com/rasbt/LLMs-from-scratch: appendix-A/01_main-chapter-code ('Introduction to PyTorch', code-part1.ipynb and code-part2.ipynb), ch02/01_main-chapter-code ('Working with Text Data', ch02.ipynb) with ch02/05_bpe-from-scratch as the bonus worth doing, and ch03/01_main-chapter-code ('Coding Attention Mechanisms', ch03.ipynb) with ch03/02_bonus_efficient-multihead-attention. Book: Build a Large Language Model (From Scratch), Manning 2024, ISBN 978-1633437166 — the repo code stands alone without it."
  }
 ],
 "t05": [
  {
   "item": "Explain RAG end to end, in 90 seconds, out loud [most-asked]",
   "label": "DeepLearning.AI RAG · Module 1",
   "url": "https://www.youtube.com/watch?v=0nA5QG3087g",
   "full": "Module 1 — 'Introduction to RAG' (5 min) then 'RAG architecture overview' (6 min). For a spoken version to imitate, Ben Clavié builds the whole pipeline in 90 seconds at 06:29 'RAG MVP Pipeline' → 07:54: https://www.youtube.com/watch?v=0nA5QG3087g"
  },
  {
   "item": "Chunking: what drives the size, and how you handle tables, PDFs and code",
   "label": "DeepLearning.AI RAG · Module 3",
   "url": "https://www.youtube.com/watch?v=RrDBV6odPKo",
   "full": "Module 3 — 'Chunking' (7 min) + 'Advanced chunking techniques' (6 min), then the ungraded lab 'Chunking' (60 min). Tables, PDFs and code are genuinely absent from the course: Jason Liu, 52:37 'Parsing Tables and PDFs' → 55:48 'Strategic Approaches to Document Chunking in RAG Systems': https://www.youtube.com/watch?v=RrDBV6odPKo"
  },
  {
   "item": "Embedding models: how to choose one and how to benchmark it on your own data",
   "label": "DeepLearning.AI RAG · Choosing",
   "url": "https://www.coursera.org/learn/retrieval-augmented-generation-rag",
   "full": "Choosing — Module 2 'Semantic search - embedding model deepdive' (6 min) + ungraded lab 'Vector embeddings in RAG' (60 min). Benchmarking on your own data — Module 2 'Evaluating retrieval' (8 min) + ungraded lab 'Retrieval metrics' (60 min), which is the half interviewers actually probe."
  },
  {
   "item": "Vector index internals — HNSW and IVF, and what recall/latency knobs each exposes",
   "label": "Module 3 'Approximate nearest neighbors…",
   "url": "https://www.pinecone.io/learn/series/faiss/vector-indexes/",
   "full": "not in primary — Module 3 'Approximate nearest neighbors algorithms (ANN)' (8 min) names the algorithms but not the knobs. Pinecone, 'Faiss: The Missing Manual', ch 2 'Nearest Neighbor Indexes for Similarity Search' for IVF — nlist, nprobe and the cell-edge problem, with Sift1M figures (~520 MB, 1–9 ms, 0.70–0.95 recall): https://www.pinecone.io/learn/series/faiss/vector-indexes/ — and ch 6 'Hierarchical Navigable Small Worlds (HNSW)' for M, efConstruction and efSearch (index size 0.5 GB at M=2 rising to ~5 GB at M=512): https://www.pinecone.io/learn/series/faiss/hnsw/"
  },
  {
   "item": "Vector DB vs Postgres+pgvector vs plain full-text search, and when each is right",
   "label": "Module 3 'Vector databases' (5 min) is d…",
   "url": "https://github.com/pgvector/pgvector",
   "full": "not in primary — Module 3 'Vector databases' (5 min) is descriptive, not comparative (the full-text side you do get, in Module 2's TF-IDF and BM25 lessons). For the pgvector argument read the README: https://github.com/pgvector/pgvector — HNSW (m default 16, ef_construction default 64, hnsw.ef_search default 40) and IVFFlat (lists = rows/1000 up to 1M rows, then sqrt(rows); ivfflat.probes starting at sqrt(lists)) inside Postgres, plus its Hybrid Search section using plainto_tsquery and ts_rank_cd with Reciprocal Rank Fusion. That section is the whole argument for not buying a vector DB."
  },
  {
   "item": "Hybrid retrieval: dense + BM25 fused with Reciprocal Rank Fusion",
   "label": "DeepLearning.AI RAG · Module 2",
   "url": "https://www.coursera.org/learn/retrieval-augmented-generation-rag",
   "full": "Module 2 — 'Keyword search - TF-IDF' (7 min) → 'Keyword search - BM25' (5 min) → 'Hybrid search' (8 min), then implement the fusion yourself in the Module 2 graded programming assignment 'Implementing retriever functions in a RAG system' (180 min)."
  },
  {
   "item": "Cross-encoder reranking: what it buys and what it costs in latency",
   "label": "DeepLearning.AI RAG · What it buys",
   "url": "https://www.coursera.org/learn/retrieval-augmented-generation-rag",
   "full": "What it buys — Module 3 'Cross-encoders and ColBERT' (8 min) + 'Reranking' (4 min). What it costs — Module 5 'Latency vs Response Quality' (5 min) + 'Cost vs Response Quality' (6 min). Both halves are inside the primary; you do not need an outside source for this one."
  },
  {
   "item": "Lost in the Middle — accuracy sags when the relevant passage sits mid-context",
   "label": "Kelly Hong (Chroma), 'Context Rot: When…",
   "url": "https://www.youtube.com/watch?v=3s_N60u0jEY",
   "full": "not in primary — Kelly Hong (Chroma), 'Context Rot: When Long Context Fails' (10 Sep 2025, 31 min): 09:39 'Experiment 2: Adding Distractors', 14:12 'Experiment 3: Shuffling Haystack Content', 20:15 'Key Takeaways', then 29:05 'Q&A: Does the U-Shaped Retrieval Curve (Beginning/End Priority) Still Hold?' — where she reports Chroma did NOT reproduce the U-shape. That is the 2026 answer: https://www.youtube.com/watch?v=3s_N60u0jEY . Read the claim being revised first — Liu et al., 'Lost in the Middle', TACL: https://arxiv.org/abs/2307.03172"
  },
  {
   "item": "Contextual retrieval — prepending chunk-level context before embedding",
   "label": "Anthropic's cookbook guide 'Contextual E…",
   "url": "https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide",
   "full": "not in primary — Anthropic's cookbook guide 'Contextual Embeddings': https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide — build the ContextualVectorDB (it situates each chunk with Claude under prompt caching, ~62% of input tokens read from cache), then quote its Pass@20 ladder: 90.06% baseline → 94.29% contextual embeddings → 94.99% + contextual BM25 → 97.45% + reranking."
  },
  {
   "item": "Citations and source attribution, and refusing when context is insufficient",
   "label": "DeepLearning.AI RAG · Refusal half",
   "url": "https://platform.claude.com/docs/en/build-with-claude/citations",
   "full": "Refusal half — Module 4 'Handling hallucinations' (8 min). Citation half is not in primary: Claude's Citations docs: https://platform.claude.com/docs/en/build-with-claude/citations — 'How citations work' → 'Citable versus non-citable content' and 'Citation indices', then 'Document types' → 'Custom content documents', which is where you control citation granularity over your own RAG chunks instead of letting the provider sentence-chunk them."
  },
  {
   "item": "Index freshness: incremental re-embedding, delete-then-upsert by doc ID, and the stale-answer window",
   "label": "LangChain's indexing API reference:",
   "url": "https://reference.langchain.com/python/langchain-core/indexing/api/index",
   "full": "not in primary — LangChain's indexing API reference: https://reference.langchain.com/python/langchain-core/indexing/api/index — the record manager, hash-based tracking so unchanged content is skipped, and the four cleanup modes (None, incremental, full, scoped_full). The stale-answer window is stated outright for full mode: 'Clean up runs after all documents have been indexed' and 'users may see duplicated content during indexing.' scoped_full exists for loaders that cannot return the whole dataset at once."
  },
  {
   "item": "Multi-tenant isolation as a filter in the query, never as a prompt instruction",
   "label": "DeepLearning.AI RAG · Mechanism",
   "url": "https://qdrant.tech/documentation/guides/multiple-partitions/",
   "full": "Mechanism — Module 2 'Metadata filtering' (4 min) + Module 5 'Security' (5 min). The threat model and the real configuration are not in primary: Qdrant, 'Multitenancy and custom sharding': https://qdrant.tech/documentation/guides/multiple-partitions/ — one collection, a tenant field in the payload (group_id in their example), a keyword index with \"is_tenant\": true, and under 'Calibrate Performance' payload_m: 16 with m: 0 so graphs are built per tenant. It also states the counter-position — separate collections only for 'a limited number of tenants that need strict isolation' — which is exactly what the follow-up question pushes on."
  },
  {
   "item": "The canonical debugging question: confident wrong answers, and the right document is in the index",
   "label": "RAG Master Series · Post 8, 'RAG Anti-Patterns with Skylar P…",
   "url": "https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/",
   "full": "Post 8, 'RAG Anti-Patterns with Skylar Payne': https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/ — it splits failures into six stages (data collection and curation, extraction and enrichment, indexing and storage, retrieval, re-ranking, generation). The sentence that answers this exact question is 'Many teams evaluate only the documents they retrieve, missing critical insights about false negatives,' with the fix 'Look beyond your retrieval window when logging and evaluating.' Then Post 3, 'Systematically Improving Your RAG' (https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/) and Post 5, 'Low-Hanging Fruit for RAG Search' (https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)."
  },
  {
   "item": "Scaling to 10M+ documents — what breaks first",
   "label": "Pablo Castro, 'RAG at scale': 02:58 'Cha…",
   "url": "https://www.youtube.com/watch?v=_2tZaDs-w5s",
   "full": "not in primary — Pablo Castro, 'RAG at scale': 02:58 'Challenges in scaling RAG' → 16:04 'Scaling vector density' → 16:58 'Customer scaling examples' → 17:50 'Vector quantization techniques': https://www.youtube.com/watch?v=_2tZaDs-w5s . For what breaks in numbers, the Faiss wiki 'Guidelines to choose an index': https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index — read the dataset-size rows in order (1M–10M → IVF65536_HNSW32, 10M–100M → IVF262144_HNSW32, 100M–1B → IVF1048576_HNSW32). What breaks first is training time and RAM: the page gives HNSW's per-vector cost as (d*4 + M*2*4) bytes and warns training gets 'even slower' at each step up."
  },
  {
   "item": "Retrieval is too slow — the ordered list of things you'd try",
   "label": "Qdrant, 'Optimize performance':",
   "url": "https://qdrant.tech/documentation/ops-optimization/optimize/",
   "full": "not in primary — Qdrant, 'Optimize performance': https://qdrant.tech/documentation/ops-optimization/optimize/ — it is written as three named recipes you can recite as a list: 'High-speed search with low memory usage', 'High precision with low memory usage', 'High precision with high-speed search', plus a 'Balancing latency and throughput' section (segment count near your core count for latency; ~2 large segments for throughput). The knobs it names are hnsw_ef, quantization with cold/pinned memory tiers, params.quantization.rescore (disable it for speed), and m / ef_construct. Pair with Pablo Castro 10:52 'Improving retrieval quality'."
  },
  {
   "item": "Semantic caching, and where it silently returns the wrong answer",
   "label": "the series never mentions caching)",
   "url": "https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html",
   "full": "not in primary (the series never mentions caching) — RedisVL, 'Semantic Caching for LLMs': https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html — work the 'Customize the Distance Threshold' section, where llmcache.set_threshold(0.5) makes 'What is the capital of the country where Nice is located?' hit an entry cached for a different question. One correction to the story you may have heard: the returned answer there, Paris, is actually correct, so the doc does not demonstrate a wrong answer — the transferable point is that the threshold is the only thing standing between a loose match and a wrong one. Then 'Utilize TTL' and 'Cache Access Controls, Tags & Filters'."
  },
  {
   "item": "Fine-tune vs RAG vs prompt engineering — the decision framework [near-guaranteed]",
   "label": "Why Fine Tuning is Dead · 02:29 'Trends and priors' → 07:12 'Hot t…",
   "url": "https://www.youtube.com/watch?v=h1c_jmk97Ss",
   "full": "02:29 'Trends and priors' → 07:12 'Hot takes vs reality' → 12:14 'Fine-tuning vs RAG' (the core segment) → 38:01 'Fine-tuning as a trap' → 39:01 'Hierarchy of needs' → 41:37 'Future outlook'. Then cross-check the written version in the backup — Huyen Ch 7, 'When to Finetune' → 'Reasons to Finetune' / 'Reasons Not to Finetune' / 'Finetuning and RAG' (Chapter 7 opens at p. 307) — and against Coursera Module 4 'RAG vs. Fine-Tuning' (6 min), so you can argue the cheap option first."
  },
  {
   "item": "Long context vs RAG — argued, not settled, in 2026",
   "label": "the talk predates the long-context evide…",
   "url": "https://www.youtube.com/watch?v=Evlk9J-B_uc",
   "full": "not in primary (the talk predates the long-context evidence) — Ben Clavié, 'I don't use RAG, I just retrieve documents' (25 Jun 2025, 25 min): 05:10 'Why RAG is dead' → 06:48 'Limitations of RAG' → 09:45 'Context Window' → 14:32 'Summary': https://www.youtube.com/watch?v=Evlk9J-B_uc . Then take the measured evidence from Kelly Hong, 'Context Rot' (10 Sep 2025) at 20:15 'Key Takeaways' and the 29:05 Q&A: https://www.youtube.com/watch?v=3s_N60u0jEY . The defensible answer is that retrieval is not replaced by a long window because performance degrades with input length and distractors, not because retrieval is cheaper."
  },
  {
   "item": "NirDiamant/RAG_Techniques",
   "label": "RAG_Techniques · Run all_rag_techniques/ in this order: s…",
   "url": "https://github.com/NirDiamant/RAG_Techniques",
   "full": "Run all_rag_techniques/ in this order: simple_rag.ipynb → choose_chunk_size.ipynb → semantic_chunking.ipynb → fusion_retrieval.ipynb (dense + BM25) → reranking.ipynb → reliable_rag.ipynb (relevance filtering, hallucination check and source highlighting — this is the citations item from group 1) → contextual_chunk_headers.ipynb → hierarchical_indices.ipynb. Finish with the evaluation/ folder: end-2-end_rag_evaluation.ipynb and evaluation_deep_eval.ipynb. Every filename here is taken from the README's own technique table, not reconstructed."
  },
  {
   "item": "Jason Liu — Systematically Improving RAG Applications",
   "label": "the free recording carries the whole fra…",
   "url": "https://www.youtube.com/watch?v=RrDBV6odPKo",
   "full": "not in primary — the free recording carries the whole framework: https://www.youtube.com/watch?v=RrDBV6odPKo (68 min, Jul 2024). The talk proper is 02:03 'Overview of RAG Playbook and Feedback Mechanisms' → 15:02, with the production cases in the Q&A from 18:12 to 1:07:21; along the way 07:02 'Analyzing User Satisfaction and Relevance' and 08:31 'Differentiating Between Topic and Capability Queries' are the two ideas to steal. The written equivalent is his 11-post index: https://jxnl.co/writing/2025/09/11/rag-series-index/ . The paid cohort version is https://maven.com/applied-llms/rag-playbook (six prerecorded lectures plus ~2 live hours a week) — the free talk carries the framework, so only pay if you want the cohort."
  },
  {
   "item": "The original RAG paper (Lewis et al., 2020) — method and figures only",
   "label": "(v1 22 May 2020, v4 12 Apr 2021)",
   "url": "https://arxiv.org/abs/2005.11401",
   "full": "not in primary — https://arxiv.org/abs/2005.11401 (v1 22 May 2020, v4 12 Apr 2021). Read §2 Methods for the two formulations the abstract contrasts — one set of retrieved passages for the whole output versus a different passage per token — plus Figure 1, then stop, exactly as your syllabus says. If you would rather hear a co-author present it, Douwe Kiela teaches it in Stanford CS25 V3, 'Retrieval Augmented Language Models' (79 min): 00:00 'Introduction to RAG' → 10:55 'Frozen RAG approach' → 11:59 'Retrieval methods': https://www.youtube.com/watch?v=mE7IDf2SmJg"
  },
  {
   "item": "Anthropic — Contextual Retrieval",
   "label": "though all_rag_techniques/contextual_chu…",
   "url": "https://www.anthropic.com/news/contextual-retrieval",
   "full": "not in primary, though all_rag_techniques/contextual_chunk_headers.ipynb is the cheaper variant worth comparing against — https://www.anthropic.com/news/contextual-retrieval (19 Sep 2024). The three numbers to memorise are its top-20-chunk retrieval-failure reductions: contextual embeddings 35% (5.7% → 3.7%), plus contextual BM25 49% (→ 2.9%), plus reranking 67% (→ 1.9%). Then run it rather than just quoting it: https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide"
  }
 ],
 "t06": [
  {
   "item": "The five patterns, and which problem each fits",
   "label": "Anthropic, Effective Agents · section 'Building blocks, workflows, and…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "Building effective agents, section 'Building blocks, workflows, and agents' — five consecutive sub-sections: 'Workflow: Prompt chaining', 'Workflow: Routing', 'Workflow: Parallelization', 'Workflow: Orchestrator-workers', 'Workflow: Evaluator-optimizer', each with its own 'When to use' paragraph. Read 'Building block: The augmented LLM' first and 'Combining and customizing these patterns' last."
  },
  {
   "item": "What lives in the orchestrator vs what lives in the model [common]",
   "label": "Anthropic, Effective Agents · section 'What are agents?' (workflows =…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "Building effective agents, section 'What are agents?' (workflows = predefined code paths; agents = the LLM directs its own process), then 'Workflow: Orchestrator-workers'. Reinforce with 12-Factor Agents Factor 8 'Own your control flow' (github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md), which states the deterministic-code-executes / model-chooses split as a switch on next_step.intent."
  },
  {
   "item": "How an agent chooses a tool — and why the tool description is the real mechanism",
   "label": "Anthropic, Effective Agents · 'Writing effective tools for agents",
   "url": "https://www.anthropic.com/engineering/writing-tools-for-agents",
   "full": "'Writing effective tools for agents — with agents' (11 Sep 2025), https://www.anthropic.com/engineering/writing-tools-for-agents — section 'Principles for writing effective tools', sub-sections 'Choosing the right tools for agents', 'Namespacing your tools', 'Returning meaningful context from your tools', 'Prompt-engineering your tool descriptions'. Then Building effective agents, 'Appendix 2: Prompt engineering your tools'."
  },
  {
   "item": "Tool failure: retries, idempotency keys, and bounded retry budgets so a retry storm doesn't become the outage",
   "label": "Marc Brooker, 'Timeouts, retries, and ba…",
   "url": "https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter:",
   "full": "not in primary — Marc Brooker, 'Timeouts, retries, and backoff with jitter', AWS Builder Center, 5 Dec 2019, https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter: section 'Retries and backoff' for the token-bucket retry limit ('we can mitigate this risk by limiting retries locally using a token bucket') and idempotency ('APIs with side effects aren't safe to retry unless they provide idempotency', with EC2 RunInstances' token mechanism), section 'Jitter' for the storm. Pair with 12-Factor Agents Factor 9 (content/factor-09-compact-errors.md) for the per-tool error counter capped at ~3 attempts, reset on success. 2019, but this is distributed systems, so age is fine."
  },
  {
   "item": "Detecting and stopping infinite planning loops; termination conditions that aren't just an iteration cap",
   "label": "12-Factor Agents (I checked 'Effective h…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "not in primary — 12-Factor Agents (I checked 'Effective harnesses for long-running agents', 26 Nov 2025, and it does not cover this): Factor 8 'Own your control flow' — break the loop on specific model intents and resume on a webhook rather than spinning; Factor 9 'Compact Errors into Context Window' — the consecutive_errors counter that resets on success and at 3 breaks, resets context or escalates to a human; Factor 10 'Small, Focused Agents' — keep agents to 3–10, max 20 steps, named as the main defence against losing the plot."
  },
  {
   "item": "When is an agent the wrong solution?",
   "label": "Anthropic, Effective Agents · sections 'When (and when not) to use age…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "Building effective agents, sections 'When (and when not) to use agents' and the one right after it, 'When and how to use frameworks' — the second is what interviewers probe, since it argues most teams should not reach for a framework at all."
  },
  {
   "item": "Multi-agent coordination, and its honest cost",
   "label": "Anthropic, Effective Agents · 'How we built our multi-agent research s…",
   "url": "https://www.anthropic.com/engineering/multi-agent-research-system",
   "full": "'How we built our multi-agent research system' (13 Jun 2025), https://www.anthropic.com/engineering/multi-agent-research-system — section 'Benefits of a multi-agent system' for the honest numbers ('agents typically use about 4× more tokens than chat interactions', 'multi-agent systems use about 15× more tokens than chats') and the stated anti-fit: domains requiring all agents to share the same context, or with many dependencies between agents. Then section 'Production reliability and engineering challenges' for error compounding and synchronous-execution bottlenecks."
  },
  {
   "item": "Agent memory: scratchpads, summarisation, and what to persist between sessions",
   "label": "Anthropic, Effective Agents · 'Effective context engineering for AI ag…",
   "url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
   "full": "'Effective context engineering for AI agents' (29 Sep 2025), https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — section 'Context engineering for long-horizon tasks' and its three bolded sub-sections: 'Compaction', 'Structured note-taking' (the NOTES.md scratchpad), 'Sub-agent architectures'."
  },
  {
   "item": "Context engineering as a named discipline",
   "label": "Anthropic, Effective Agents · 'Effective context engineering for AI ag…",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "'Effective context engineering for AI agents' — sections 'Context engineering vs. prompt engineering', 'Why context engineering is important to building capable agents', 'The anatomy of effective context', 'Context retrieval and agentic search', in that order. This post is where the term got its working definition."
  },
  {
   "item": "The primitive control model",
   "label": "MCP spec · Docs > Learn > 'Understanding MCP server…",
   "url": "https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts",
   "full": "Docs > Learn > 'Understanding MCP servers', https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts — the 'Core Server Features' table at the top, whose 'Who controls it' column reads Tools = Model, Resources = Application, Prompts = User. Then the 'User Interaction Model' sub-section under each of Tools, Resources and Prompts on the same page."
  },
  {
   "item": "Transports: stdio vs Streamable HTTP",
   "label": "MCP spec · Spec /specification/2026-07-28/basic/tra…",
   "url": "https://modelcontextprotocol.io/specification/2026-07-28",
   "full": "Spec /specification/2026-07-28/basic/transports/stdio — short, read whole; the opening bullet list is the contract. Then /specification/2026-07-28/basic/transports/streamable-http, sections 'Security & Endpoint', 'Sending Messages', 'Receiving Messages', 'Request Metadata', and above all 'Backward Compatibility' > 'Earlier Streamable HTTP Revisions', which lists what 2026-07-28 deleted: the GET stream, Mcp-Session-Id, Last-Event-ID resumption."
  },
  {
   "item": "Tool schema design, and the isError convention",
   "label": "MCP spec · Spec /specification/2026-07-28/server/to…",
   "url": "https://modelcontextprotocol.io/specification/2026-07-28",
   "full": "Spec /specification/2026-07-28/server/tools — section 'Data Types' > 'Tool' for inputSchema/outputSchema (JSON Schema, 'Defaults to 2020-12 if no $schema field is present'), 'Tool Names' rules, and the warning that clients MUST treat annotations as untrusted; then section 'Error Handling', which splits protocol errors (JSON-RPC, model unlikely to fix) from tool execution errors returned with isError: true, which clients SHOULD feed back so the model self-corrects."
  },
  {
   "item": "Resources vs tools — exposing a catalog instead of forcing exploratory calls",
   "label": "MCP spec · Spec /specification/2026-07-28/server/re…",
   "url": "https://www.anthropic.com/engineering/code-execution-with-mcp",
   "full": "Spec /specification/2026-07-28/server/resources — sections 'User Interaction Model' (application-driven, not model-driven), 'Listing Resources', 'Resource Templates' (RFC 6570 URI templates plus the completion API), 'Annotations' (audience/priority/lastModified). Read it against server/tools' own 'User Interaction Model' to feel the contrast. Then 'Code execution with MCP' (4 Nov 2025), https://www.anthropic.com/engineering/code-execution-with-mcp, section 'Benefits of code execution with MCP' > 'Progressive disclosure', with the 150,000-to-2,000-token figure for not loading every definition up front."
  },
  {
   "item": "Server configuration and scope: .mcp.json project scope vs user scope, and env-var expansion",
   "label": "it is a client concern the spec does not…",
   "url": "https://code.claude.com/docs/en/mcp",
   "full": "not in primary (it is a client concern the spec does not define) — Claude Code docs, https://code.claude.com/docs/en/mcp, section 'MCP installation scopes' with sub-sections 'Local scope', 'Project scope', 'User scope' and 'Scope hierarchy and precedence' (local > project > user > plugin > claude.ai connectors; the whole entry from the winning source is used, fields are never merged); then 'Environment variable expansion in .mcp.json' for ${VAR} and ${VAR:-default}, the five expansion sites (command, args, env, url, headers), and 'Credential variables that read as empty', which is why Bearer ${ANTHROPIC_AUTH_TOKEN} silently sends nothing."
  },
  {
   "item": "MCP-specific attack classes",
   "label": "MCP spec · Docs > Tutorials > Security > 'Security…",
   "url": "https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices",
   "full": "Docs > Tutorials > Security > 'Security Best Practices', https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices — section 'Attacks and Mitigations', one sub-section per class, in order: Confused Deputy Problem, Token Passthrough, Server-Side Request Forgery (SSRF), State Handle Hijacking, Local MCP Server Compromise, OAuth Authorization URL Validation, stdio Transport Security in Proxy Scenarios, Mix-Up Attacks, Localhost Redirect URI Impersonation, CIMD Trust Policies, Scope Minimization."
  },
  {
   "item": "Build one: a 3-tool MCP server with one resource and one prompt, wired into a real client",
   "label": "MCP spec · Docs > Develop > 'Build an MCP server'",
   "url": "https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server",
   "full": "Docs > Develop > 'Build an MCP server', https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server — it builds get_alerts and get_forecast in Python or TypeScript and wires them into a host, and states it 'will primarily focus on tools', so add your third tool, then add the resource and the prompt using learn/server-concepts sections 'Resources' and 'Prompts'. Verify before touching a client with Docs > Tools > 'MCP Inspector', https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector — `npx @modelcontextprotocol/inspector node path/to/server.js`."
  },
  {
   "item": "Debugging: why anything written to stdout corrupts a stdio server, and where logs must go instead",
   "label": "MCP spec · Spec /specification/2026-07-28/basic/tra…",
   "url": "https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging",
   "full": "Spec /specification/2026-07-28/basic/transports/stdio, opening bullet list: 'The server MUST NOT write anything to its stdout that is not a valid MCP message' and 'The server MAY write UTF-8 strings to stderr for any logging purposes'. Then Docs > Tools > 'Debugging', https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging, section 'Implementing logging' > 'Server-side logging' — stderr is captured by the host on stdio, is not captured on Streamable HTTP (use OpenTelemetry), and protocol logging via notifications/message is deprecated as of 2026-07-28."
  },
  {
   "item": "Prompt injection — direct, and indirect via retrieved content or tool output",
   "label": "OWASP Agentic Top 10 · 'ASI01: Agent Goal Hijack', pp. 9–11",
   "url": "https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/",
   "full": "OWASP Top 10 for Agentic Applications 2026, 'ASI01: Agent Goal Hijack', pp. 9–11 — its 'Common Examples of the Vulnerability' list is indirect injection via hidden payloads in web pages or RAG documents, via email/calendar/Teams, and via tool output; 'Example Attack Scenarios' opens with EchoLeak, the zero-click Microsoft 365 Copilot exfiltration. Then 'ASI06: Memory & Context Poisoning', pp. 24–26, for the persisted variant. For the framing that makes it stick, Simon Willison, 'The lethal trifecta' (16 Jun 2025), https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ — private data + untrusted content + external communication, with the GitHub MCP exploit as the worked example."
  },
  {
   "item": "Sandboxing tool execution; least privilege; capability bloat",
   "label": "OWASP Agentic Top 10 · 'ASI02: Tool Misuse and Exploitation', p…",
   "url": "https://arxiv.org/abs/2506.08837",
   "full": "OWASP Top 10 for Agentic Applications 2026, 'ASI02: Tool Misuse and Exploitation', pp. 12–14, Prevention items 1 'Least Agency and Least Privilege for Tools' (per-tool scope, rate and egress-allowlist profiles) and 3 'Execution Sandboxes and Egress Controls'; then 'ASI03: Identity and Privilege Abuse', pp. 15–17, on why passing the full agent identity downstream makes real least privilege impossible; then 'ASI05: Unexpected Code Execution (RCE)', pp. 21–23, Prevention item 4 'Execution environment security' ('Never run as root', sandboxed containers, restricted filesystem). For the architectural answer rather than the control list, arXiv:2506.08837, https://arxiv.org/abs/2506.08837, section 3 — Action-Selector, Plan-Then-Execute, Dual LLM, Code-Then-Execute, Context-Minimization."
  },
  {
   "item": "Human-in-the-loop gates for irreversible operations",
   "label": "OWASP Agentic Top 10 · 'ASI03: Identity and Privilege Abuse', P…",
   "url": "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/",
   "full": "OWASP Top 10 for Agentic Applications 2026, 'ASI03: Identity and Privilege Abuse', Prevention item 4 on p. 17: 'Apply Human-in-the-Loop for Privilege Escalation: Require human approval for high-privilege or irreversible actions.' Then 'ASI09: Human-Agent Trust Exploitation', pp. 33–35, Prevention item 1 'Explicit confirmations' — and the failure mode where the gate exists but gets rubber-stamped. Cross-check against the MCP spec's normative line, /specification/2026-07-28/server/tools section 'User Interaction Model': there SHOULD always be a human in the loop with the ability to deny tool invocations."
  },
  {
   "item": "Anthropic engineering — the five-post arc",
   "label": "Anthropic Engineering · in date order: 'Building effective agent…",
   "url": "https://www.anthropic.com/engineering",
   "full": "https://www.anthropic.com/engineering, in date order: 'Building effective agents' (19 Dec 2024), 'How we built our multi-agent research system' (13 Jun 2025), 'Writing effective tools for agents — with agents' (11 Sep 2025), 'Effective context engineering for AI agents' (29 Sep 2025), 'Code execution with MCP: Building more efficient agents' (4 Nov 2025). Worth adding from the same index: 'Effective harnesses for long-running agents' (26 Nov 2025) and 'Demystifying evals for AI agents' (9 Jan 2026)."
  },
  {
   "item": "modelcontextprotocol.io — the spec itself",
   "label": "Anthropic Engineering · Start at , which states 'The current pro…",
   "url": "https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning",
   "full": "Start at https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning, which states 'The current protocol version is 2026-07-28' and explains the per-request _meta negotiation that replaced the initialize handshake. Then https://modelcontextprotocol.io/specification/2026-07-28, then basic/transports/{stdio,streamable-http}, then server/{tools,resources,prompts}. Do not read the 2025-06-18 revision most tutorials still link to."
  },
  {
   "item": "NirDiamant/GenAI_Agents",
   "label": "Anthropic Engineering · directory all_agents_tutorials/, in this…",
   "url": "https://github.com/NirDiamant/GenAI_Agents",
   "full": "https://github.com/NirDiamant/GenAI_Agents, directory all_agents_tutorials/, in this order: agent_while_loop_from_scratch.ipynb → one_step_decision_router.ipynb → memory-agent-tutorial.ipynb → human_in_the_loop_approval_agent.ipynb → multi_agent_collaboration_system.ipynb → mcp-tutorial.ipynb. Skip the business/creative/shopping categories."
  },
  {
   "item": "Lilian Weng — LLM Powered Autonomous Agents",
   "label": "Anthropic Engineering · (23 Jun 2023)",
   "url": "https://lilianweng.github.io/posts/2023-06-23-agent/",
   "full": "https://lilianweng.github.io/posts/2023-06-23-agent/ (23 Jun 2023). Sections 'Agent System Overview', 'Component One: Planning' (Task Decomposition, Self-Reflection), 'Component Two: Memory', 'Component Three: Tool Use', 'Challenges'. Read it as the taxonomy everyone else inherited — its specific techniques are three years stale, its decomposition is not."
  },
  {
   "item": "The ReAct paper — reasoning and acting interleaved",
   "label": "Anthropic Engineering · arXiv:2210.03629",
   "url": "https://arxiv.org/abs/2210.03629",
   "full": "arXiv:2210.03629, https://arxiv.org/abs/2210.03629 — Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao. Read v3 (10 Mar 2023), which the arXiv listing marks as 'the ICLR camera ready version with some typos fixed', not v1 (6 Oct 2022)."
  },
  {
   "item": "Know LangGraph and CrewAI by name even if you'd hand-roll it",
   "label": "Anthropic Engineering · LangGraph:",
   "url": "https://docs.langchain.com/oss/python/langgraph/overview",
   "full": "LangGraph: https://docs.langchain.com/oss/python/langgraph/overview — the 'Core benefits' section alone is enough (low-level orchestration and runtime, persistence and resuming from where it left off, human-in-the-loop by inspecting and modifying agent state). CrewAI: https://docs.crewai.com/en/introduction — you need exactly one distinction, from sections '1. Flows: The Backbone' (the manager, the process definition, owning state and control flow) versus '2. Crews: The Intelligence' (the teams that do the heavy lifting inside a Flow step), plus 'When to Use Crews vs. Flows'."
  }
 ],
 "t07": [
  {
   "item": "Capture real traces before doing anything else",
   "label": "Arize, Agent Evals · 16:32–36:36 'Step 1: Tracing with Phoeni…",
   "url": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
   "full": "16:32–36:36 'Step 1: Tracing with Phoenix'. Set-up runs from 0:00; the argument for doing this first is 2:47 ('\"Looks good to me\" isn't a test suite') and 4:57 ('Traces vs. evals: the mental model')."
  },
  {
   "item": "Open-code the traces by hand",
   "label": "Arize, Agent Evals · 36:36–50:36 'Step 2: Reading your traces…",
   "url": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
   "full": "36:36–50:36 'Step 2: Reading your traces', with the concrete find at 43:21 ('The 116% analyst consensus bug') — that bug is the whole reason the workshop exists."
  },
  {
   "item": "Axial-code those notes into a 5–8 mode failure taxonomy, and stop at saturation",
   "label": "Lenny's Podcast, 'Why AI evals are the h…",
   "url": "https://www.youtube.com/watch?v=BsWxPI9UM4c",
   "full": "not in primary — Lenny's Podcast, 'Why AI evals are the hottest new skill for product builders' with Hamel Husain & Shreya Shankar (25 Sep 2025, 1h46m33s), chapter 31:39 'Using axial codes to help categorize and synthesize error notes', preceded by 28:07 'Theoretical saturation: when to stop' and 16:51 'Writing notes on errors': https://www.youtube.com/watch?v=BsWxPI9UM4c — the episode notes even include their prompt, which asks the model to 'propose 5-6 categories that we can create axial codes from'."
  },
  {
   "item": "Separate retrieval metrics from generation metrics",
   "label": "Evidently AI course, lesson 6.1 'How to…",
   "url": "https://www.youtube.com/watch?v=qI2qQfOG0Js",
   "full": "not in primary — Evidently AI course, lesson 6.1 'How to evaluate a RAG system: methods and metrics' (Elena Samuylova, 7m07s), 01:03 'How to evaluate RAG? Look at both sides', then 01:34–03:55 retrieval quality (ground truth, labelling relevance, context-quality judge) set against 03:55–06:09 generation quality (faithfulness, completeness): https://www.youtube.com/watch?v=qI2qQfOG0Js"
  },
  {
   "item": "Build one binary LLM judge for the top failure mode, and validate it against your own labels",
   "label": "Arize, Agent Evals · 56:11 'Step 4: LLM-as-a-judge' → 1:00:30…",
   "url": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
   "full": "56:11 'Step 4: LLM-as-a-judge' → 1:00:30 'Why the correctness eval failed every report' (the one-judge-for-everything trap) → 1:10:41 'Step 5: Writing your own judge' → 1:24:45 'Step 6: Testing your judge', which is the validation-against-your-own-labels step."
  },
  {
   "item": "Turn 20–50 cases into a regression suite that runs in CI and fails the build",
   "label": "Arize, Agent Evals · 1:50:55 'Evals in CI'",
   "url": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
   "full": "1:50:55 'Evals in CI' — the suite is gated with `npm test`. Follow it with 1:55:25 'Where to start on Monday'."
  },
  {
   "item": "Write the before/after delta on one page",
   "label": "Arize, Agent Evals · 1:38:55 'Step 7: Experiments'",
   "url": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
   "full": "1:38:55 'Step 7: Experiments' — the dataset-versus-version comparison is the delta — then 1:48:30 'Upgrading to Claude Haiku 4.5 to 5.5' as a worked before/after he can copy the shape of."
  },
  {
   "item": "LLM-as-judge: how it works and its failure modes",
   "label": "Stanford CME 295 · 28:00 'LLM-as-a-judge' → 33:44 'Structur…",
   "url": "https://www.youtube.com/watch?v=8fNP4N46RRo",
   "full": "28:00 'LLM-as-a-judge' → 33:44 'Structured outputs' → 36:48 'Variants' (pointwise vs pairwise) → 38:47 'Position, verbosity, self-enhancement bias'. The deck's mitigation slide reads 'Mitigate biases (position, verbosity, self-enhancement, etc.)'. The agreement maths you defend a judge with is earlier, at 07:08 'Inter-rater agreement metrics'."
  },
  {
   "item": "Binary judgements beat Likert scales",
   "label": "Stanford CME 295 · 47:22 'Best practices'",
   "url": "https://www.youtube.com/watch?v=Bc15F1xlbTA",
   "full": "47:22 'Best practices' — the slide bullet is literally 'Binary scale over more granular ones'. For the argued version rather than the asserted one, Hamel Husain, 'I Ranked Every AI Eval Concept From Worst to Best' (7 Oct 2026), 04:28 'Binary pass/fail vs 1 to 5 scales': https://www.youtube.com/watch?v=Bc15F1xlbTA"
  },
  {
   "item": "Building a golden dataset from a vague spec",
   "label": "Hamel Husain, 'A Field Guide to Rapidly…",
   "url": "https://hamel.dev/blog/posts/field-guide/",
   "full": "not in primary — Hamel Husain, 'A Field Guide to Rapidly Improving AI Products' (24 Mar 2025), §4 'Bootstrapping Your AI With Synthetic Data Is Effective (Even With Zero Users)', sub-sections 'A Framework for Generating Realistic Test Data' and 'Guidelines for Using Synthetic Data': https://hamel.dev/blog/posts/field-guide/ — then the hamel.dev Evals FAQ question 'Do I need a reference answer or rubric before annotating data?'"
  },
  {
   "item": "pass@k vs pass^k, and why the difference matters for agents",
   "label": "Stanford CME 295 · 1:40:51 'Agents with Tau-Bench'",
   "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
   "full": "1:40:51 'Agents with Tau-Bench'. The deck gives τ-bench's criterion as 'Maximize reward and pass^k' and defines 'Pass^k = Probability that all k attempts succeed' — reliability across repeated runs, not best-of-k. For the worked number to quote, Anthropic's 'Demystifying evals for AI agents' §4 computes 0.75 per trial → (0.75)³ ≈ 42% over three: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"
  },
  {
   "item": "Agent-specific metrics: tool-selection quality, action advancement, end-state vs trajectory scoring, cost per successful task",
   "label": "Stanford CME 295 · 1:00:15–1:23:50 'Agent evaluation' cover…",
   "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
   "full": "1:00:15–1:23:50 'Agent evaluation' covers the tool-call failure taxonomy. End-state vs trajectory and cost are not there: Anthropic, 'Demystifying evals for AI agents' §2 'The structure of an evaluation' defines outcome ('the final state in the environment at the end of the trial') against transcript ('the complete record of a trial, including outputs, tool calls, reasoning, intermediate results') and argues you should 'grade what the agent produced, not the path it took'; §4 lists 'latency, token usage, cost per task, and error rates': https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents . Be aware 'action advancement' is a Galileo product term, not standard vocabulary — no source here uses it."
  },
  {
   "item": "Measuring hallucination rate in production, not just offline",
   "label": "Stanford CME 295 · The offline half is 54:06 'Factuality'",
   "url": "https://hamel.dev/blog/posts/evals-faq/",
   "full": "The offline half is 54:06 'Factuality'. The production half is not in primary — hamel.dev Evals FAQ, 'How are evaluations used differently in CI/CD vs. monitoring production?' under 'Production & Deployment', read alongside 'What's the difference between guardrails & evaluators?' and 'How often should I run my evals?': https://hamel.dev/blog/posts/evals-faq/"
  },
  {
   "item": "Aggregate accuracy hides per-segment failure",
   "label": "hamel.dev Evals FAQ, 'How do I approach…",
   "url": "https://hamel.dev/blog/posts/evals-faq/",
   "full": "not in primary — hamel.dev Evals FAQ, 'How do I approach evaluation when my system handles diverse user queries?', whose answer opens 'Your evaluation strategy should emerge from observed failure patterns'; pair it with 'How can I efficiently sample production traces for review?': https://hamel.dev/blog/posts/evals-faq/"
  },
  {
   "item": "❌ Don't name a prefab eval framework as your answer",
   "label": "Husain, Field Guide · §1 'The Most Common Mistake: Skipping Er…",
   "url": "https://www.youtube.com/watch?v=Bc15F1xlbTA",
   "full": "§1 'The Most Common Mistake: Skipping Error Analysis', including 'The Error Analysis Process' and 'Bottom-Up vs. Top-Down Analysis' — this is what he should say instead. For the blunt version, Hamel Husain, 'I Ranked Every AI Eval Concept From Worst to Best' (13m23s, 7 Oct 2026) ranks the traps one by one: 08:59 'Picking an eval vendor first', 03:25 'Off the shelf LLM judges', 00:27 'Generic metrics like helpfulness and conciseness', 05:24 'Public benchmarks as product evals' — against 00:51 'Error analysis' and 10:54 'Validating judges against human labels': https://www.youtube.com/watch?v=Bc15F1xlbTA"
  },
  {
   "item": "Lead any project discussion with the eval layer and the cost number, not the framework name",
   "label": "Husain, Field Guide · §6 'Your AI Roadmap Should Count Experim…",
   "url": "https://www.youtube.com/watch?v=c5wyHzPU4yE",
   "full": "§6 'Your AI Roadmap Should Count Experiments, Not Features' → 'The Foundation: Evaluation Infrastructure' → 'Communicating This to Stakeholders' ('The key metric for AI roadmaps isn't features shipped – it's experiments run'). The Field Guide carries the eval half but quotes no cost figures; for the cost half, Pratik Bhavsar (Galileo), 'AI Agent Evaluation' (DAIR.AI, 22 Jul 2025, 1h18m50s), 1:02:20 'Cost vs Performance' and 1:08:34 'The Triad of Tradeoffs': https://www.youtube.com/watch?v=c5wyHzPU4yE . For what the interviewer is scoring, Eugene Yan asks 'How did you evaluate and perform error analysis on the model or system?' and looks for 'quantifiable outcomes such as customer impact, new capabilities, revenue, or cost savings': https://eugeneyan.com/writing/how-to-interview/"
  },
  {
   "item": "⭐ hamel.dev — LLM Evals FAQ",
   "label": "Hamel & Shreya, Evals FAQ · The primary itself",
   "url": "https://hamel.dev/blog/posts/evals-faq/",
   "full": "The primary itself. Read 'Getting Started & Fundamentals' (6 questions) first, then all 12 questions under 'Error Analysis & Data Collection' before anything else — 'theoretical saturation' is defined there, under 'How many examples do I need for an eval?' → 'When to stop' ('Continue until new traces stop revealing failure modes or changing existing ones… We recommend reviewing at least 100 traces'). 'Tools & Infrastructure' is the section that will date fastest."
  },
  {
   "item": "Eugene Yan — Patterns for Building LLM-based Systems",
   "label": "pattern 1 of 7, 'Evals', with sub-headin…",
   "url": "https://eugeneyan.com/writing/llm-patterns/",
   "full": "not in primary — https://eugeneyan.com/writing/llm-patterns/ , pattern 1 of 7, 'Evals', with sub-headings 'Why evals?', 'More about evals' and 'How to apply evals?'. Written around Aug 2023, so take the shape of the seven patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, collect user feedback) and ignore its specific metric recommendations."
  },
  {
   "item": "Eugene Yan — How to Interview and Hire ML/AI Engineers",
   "label": "(Jul 2024), §1 'What technical skills to…",
   "url": "https://eugeneyan.com/writing/how-to-interview/",
   "full": "not in primary — https://eugeneyan.com/writing/how-to-interview/ (Jul 2024), §1 'What technical skills to consider' and §3 'Calibrating the phone screen for loop success'. §5 'For interviewers: Candidates are rough diamonds' and §6 'For hiring managers: Sell on mission & talent density' are written for the other side of the table and he can skim them."
  },
  {
   "item": "Anthropic — Demystifying Evals for AI Agents",
   "label": "(9 Jan 2026), §5 'Going from zero to one…",
   "url": "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents",
   "full": "not in primary — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (9 Jan 2026), §5 'Going from zero to one: a roadmap to great evals for agents' is the core; §4 'How to evaluate AI agents' for grader types, capability-vs-regression evals and pass^k; the closing 'Appendix: Eval frameworks' if he wants tool names on hand."
  },
  {
   "item": "benchflow-ai/awesome-evals",
   "label": "'Must-read starter set' first, then §8…",
   "url": "https://github.com/benchflow-ai/awesome-evals",
   "full": "not in primary — https://github.com/benchflow-ai/awesome-evals , 'Must-read starter set' first, then §8 'LLM-as-judge & verifiers' and §9 'Agent-specific evaluation'. 987 stars, 59 commits on main; treat the other 14 sections as an index, not a reading list."
  }
 ],
 "t08": [
  {
   "item": "Time to first token vs total latency, and why streaming changes perceived speed",
   "label": "Stanford CS336 · Lecture 10, 5:16 \"Fundamentals and metri…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 5:16 \"Fundamentals and metrics\" — TTFT, latency in seconds/token and throughput defined as three separate targets (TTFT = how long the user waits before anything appears; per-token latency = how fast tokens appear for one query; throughput = many queries), then 35:05 \"Throughput and latency trade-offs\""
  },
  {
   "item": "KV cache and PagedAttention — why memory fragmentation was the bottleneck",
   "label": "Stanford CS336 · Lecture 10, 20:34 \"The KV cache mechanis…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 20:34 \"The KV cache mechanism\" (naive generation is O(T³); what the cache stores per sequence/token/layer/head), then 1:16:56 \"Dynamic workload optimization\" for the vLLM PagedAttention part — the fragmentation diagram, the OS-paging fix and block sharing"
  },
  {
   "item": "Continuous batching, and why it beats static batching under mixed request lengths",
   "label": "Stanford CS336 · Lecture 10, 1:16:56 \"Dynamic workload op…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 1:16:56 \"Dynamic workload optimization\" — the three reasons live traffic breaks static batching (requests arrive at different times, prefixes are shared, lengths are ragged so padding wastes compute); the same section is spelled out in the free notes at cs336.stanford.edu/lectures/?trace=lecture_10"
  },
  {
   "item": "Speculative decoding — a draft model proposes, the target verifies",
   "label": "Stanford CS336 · Lecture 10, 1:11:56 \"Speculative decoding",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 1:11:56 \"Speculative decoding\" — the draft/verify loop, the accept-reject rule that makes the output distributed exactly like the target model's, then Medusa and EAGLE as draft variants"
  },
  {
   "item": "GQA and MQA — sharing key/value heads to shrink the cache",
   "label": "Stanford CS336 · Lecture 10, 46:16 \"KV cache reduction te…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 46:16 \"KV cache reduction techniques\" — GQA with N = K·G (heads split across K groups), MQA as the K = 1 limit, then MLA, cross-layer attention and sliding-window attention as the alternatives"
  },
  {
   "item": "Quantization for serving: the size, speed and accuracy triangle",
   "label": "Stanford CS336 · Lecture 10, 1:04:29 \"Quantization and pr…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 1:04:29 \"Quantization and pruning\" — the quantize/dequantize arithmetic with scale and zero-point, QAT vs post-training quantization, GPTQ, then activation-aware quantization (AWQ)"
  },
  {
   "item": "Prefill vs decode: why they have completely different bottlenecks",
   "label": "Stanford CS336 · Lecture 10, 14:23 \"Arithmetic intensity…",
   "url": "https://www.youtube.com/watch?v=EfM546A79aM",
   "full": "Lecture 10, 14:23 \"Arithmetic intensity analysis\" (compute-bound only once batch > ~295 on an H100) then 25:08 \"Performance bottlenecks\" — prefill is compute-bound, generation memory-bound, and generation attention intensity is <1 so batching cannot rescue it"
  },
  {
   "item": "\"1M queries a day — cut the cost\" [near-guaranteed]",
   "label": "Claude Cookbook, Cost · The seven-step checklist in the intro ce…",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "The seven-step checklist in the intro cell (before §\"Prerequisites\"), then §\"Before you start optimizing\" → the lever sections in order → §\"Putting it all together\" (cheapest config that still clears 10/10) → §\"Takeaways and next steps\", whose workload-shape → lever table is the skeleton of the spoken answer"
  },
  {
   "item": "Prompt caching vs semantic caching — different mechanisms, different failure modes",
   "label": "Claude Cookbook, Cost · §\"Prompt caching\" for the prompt-cache h…",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "§\"Prompt caching\" for the prompt-cache half (what a prefix is, what invalidates it, how it stacks with batching). Semantic caching: not in primary — Chip Huyen, \"Building A Generative AI Platform\" (huyenchip.com, 25 Jul 2024), Step 4 → §\"Exact cache\" then §\"Semantic cache\", which names the failure mode outright: a wrong similarity match serves an incorrect cached answer confidently"
  },
  {
   "item": "Model tiering: route easy queries to a small model, escalate on a confidence or validation signal",
   "label": "Claude Cookbook, Cost · §\"Model selection and effort",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "§\"Model selection and effort\" — the model × effort sweep against the eval (drop to `low` effort, then drop a model tier and reset effort, repeat until the pass rate slips), plus the triage pattern in §\"Batch API\", where a cheap classification pass decides which items even reach the expensive agent"
  },
  {
   "item": "Batch APIs: roughly half price for a 24-hour window, no latency SLA",
   "label": "Claude Cookbook, Cost · §\"Batch API",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "§\"Batch API\" — 50% off every token for requests processed asynchronously within 24 hours, prompt caching still applying inside the batch so the discounts stack, and the runnable side-by-side where the token columns match but cost per task halves; the caveat that batch requests are single-shot (no mid-batch tool loop) is the detail interviewers push on"
  },
  {
   "item": "Cost arithmetic out loud",
   "label": "Claude Cookbook, Cost · §\"Before you start optimizing\" (pass rat…",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "§\"Before you start optimizing\" (pass rate and cost per task as the two axes, and why cost per completed task beats cost per token — a pricier model that finishes in fewer turns is cheaper), then §\"Putting it all together\" where every lever is re-priced per task, and the first takeaway in §\"Takeaways and next steps\""
  },
  {
   "item": "Provider failover, circuit breakers, and graceful degradation",
   "label": "Google SRE Book (free online), Ch 22 \"Ad…",
   "url": "https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb",
   "full": "not in primary — Google SRE Book (free online), Ch 22 \"Addressing Cascading Failures\" §\"Load Shedding and Graceful Degradation\", §\"Retries\", §\"Latency and Deadlines\" and §\"Test Until Failure and Beyond\", plus Ch 21 \"Handling Overload\" §\"Client-Side Throttling\" (the circuit breaker by another name) and §\"Deciding to Retry\" — sre.google/sre-book/addressing-cascading-failures/ and /handling-overload/; for the provider-failover half specifically, Chip Huyen's \"Building A Generative AI Platform\" Step 3 → §\"Gateway\" (fallback policies on rate limits and API failures)"
  },
  {
   "item": "Benchmark every hop in a multi-step pipeline to find the real bottleneck",
   "label": "LLM Inference Handbook · Infra and operations → \"LLM observabilit…",
   "url": "https://handbook.modular.com/",
   "full": "Infra and operations → \"LLM observability\" (handbook.modular.com/infrastructure-and-operations/comprehensive-observability/) §\"What to monitor: LLM metrics by layer\" — cluster → GPUs → inference engine → requests and latency → application, where the application layer is explicitly per-step and per-tool-call latency inside a pipeline or agent loop — then §\"How to diagnose common LLM inference problems\"; set the pipeline shapes first with \"Multi-model inference pipelines\" §\"What a multi-model pipeline looks like\" and §\"Single model vs. multi-model pipeline\""
  },
  {
   "item": "p50 vs p95 vs p99 — and why an average latency claim invites a follow-up",
   "label": "LLM Inference Handbook · Foundations → \"Key metrics for LLM infer…",
   "url": "https://handbook.modular.com/",
   "full": "Foundations → \"Key metrics for LLM inference\" §\"Understanding mean, median, and P99 latency\" — the mean is inflated by a single slow TTFT, the median is the typical user, P99 is the SLA question, and P90/P95 are what you use when P99 is too noisy — then §\"Goodput\", which reframes the whole question as requests per second that meet your SLO"
  },
  {
   "item": "Load-testing an LLM endpoint: concurrency, queueing and tail behaviour",
   "label": "LLM Inference Handbook · Inference optimization → \"LLM performanc…",
   "url": "https://handbook.modular.com/",
   "full": "Inference optimization → \"LLM performance benchmarks\" §\"Choosing the right benchmark tools\" (general load testers like Locust and K6 vs LLM-specific tools vs the engine's built-in benchmark), §\"What metrics should you benchmark\", §\"How to create good LLM performance benchmarks\" and §\"When benchmarks don't help\"; read the queueing and tail behaviour off the observability page's diagnose table — \"TTFT rises under load → waiting requests, queue time, KV cache usage → replicas saturated and queueing\""
  },
  {
   "item": "ray-project/llm-numbers",
   "label": "the repo itself, , whose README states…",
   "url": "https://handbook.modular.com/",
   "full": "not in primary — the repo itself, github.com/ray-project/llm-numbers, whose README states \"Last updates: 2023-05-17\": drill the ratios that still hold (1.3:1 tokens per word, ~2× params for serving memory, >10× throughput from batching) and re-derive every dollar figure, because the prices are GPT-3.5/GPT-4-era; replace its sizing numbers with the handbook's \"Calculating GPU memory for LLMs\" under Planning your deployment"
  }
 ],
 "t09": [
  {
   "item": "Bias–variance, and the intervention ladder for each",
   "label": "Hands-On ML (PyTorch) · Ch 4 'Training Models' → 'Learning Curve…",
   "url": "https://cs229.stanford.edu/materials/ML-advice.pdf",
   "full": "Ch 4 'Training Models' → 'Learning Curves' — reading underfit vs overfit off the training and validation curves, with the bias/variance trade-off note. The intervention ladder itself is not in the book: use Andrew Ng, CS229 'Advice for applying Machine Learning' (PDF, ~30 slides — I extracted the text to confirm), the run of slides 'Fixing the learning algorithm' → 'Diagnostic for bias vs. variance' → 'More on bias vs. variance', which sets each fix (more data, fewer features, more features, more iterations, Newton's method, different λ, an SVM) against the symptom it actually treats. https://cs229.stanford.edu/materials/ML-advice.pdf"
  },
  {
   "item": "Regularisation: L1 vs L2, and why L1 produces sparsity",
   "label": "Hands-On ML (PyTorch) · Ch 4 → '# Regularized Linear Models…",
   "url": "https://ageron.github.io/",
   "full": "Ch 4 → '# Regularized Linear Models' → '## Ridge Regression', then 'Lasso Regression' (where the sparsity argument and the ℓ1-vs-ℓ2 contour figure sit) and 'Elastic Net'. I confirmed this heading path directly in the companion notebook 04_training_linear_models.ipynb."
  },
  {
   "item": "Precision, recall, F1 — and PR-AUC over ROC-AUC at low prevalence",
   "label": "Hands-On ML (PyTorch) · Ch 3 'Classification' → 'Performance Mea…",
   "url": "https://ageron.github.io/",
   "full": "Ch 3 'Classification' → 'Performance Measures' → 'Confusion Matrix' → 'Precision and Recall' → 'Precision/Recall Trade-off' → 'The ROC Curve', which closes on the rule of thumb to prefer the PR curve whenever the positive class is rare."
  },
  {
   "item": "Choosing a threshold from a cost matrix rather than defaulting to 0.5",
   "label": "Ch 3 gives the precision/recall trade-of…",
   "url": "https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html",
   "full": "not in primary (Ch 3 gives the precision/recall trade-off but never prices the errors) — scikit-learn example 'Post-tuning the decision threshold for cost-sensitive learning': gain_matrix = [[0, -1], [-5, 0]] on the Statlog German credit data, tuned best_threshold_ = 0.03, test-set business gain improving from -209 to -143. https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html — read it straight after User Guide §3.3 'Tuning the decision threshold for class prediction' (TunedThresholdClassifierCV, FixedThresholdClassifier), https://scikit-learn.org/stable/modules/classification_threshold.html"
  },
  {
   "item": "Class imbalance — and why SMOTE is the wrong first answer",
   "label": "van den Goorbergh, van Smeden, Timmerman…",
   "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9382395/",
   "full": "not in primary — van den Goorbergh, van Smeden, Timmerman & Van Calster, 'The harm of class imbalance corrections for risk prediction models', JAMIA 29(9):1525–1534 (2022); read Results then Discussion. RUS, ROS and SMOTE never beat uncorrected AUROC, and all three wrecked calibration (strongly negative intercepts, SMOTE slopes below 1 so predictions come out too extreme); the authors' remedy is to move the threshold instead. Open access: https://pmc.ncbi.nlm.nih.gov/articles/PMC9382395/"
  },
  {
   "item": "Data leakage taxonomy, including grouped splitting",
   "label": "Kapoor & Narayanan, 'Leakage and the rep…",
   "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/",
   "full": "not in primary — Kapoor & Narayanan, 'Leakage and the reproducibility crisis in machine-learning-based science', Patterns 4(9):100804 (2023), Results → 'Toward a solution: A taxonomy of data leakage' — the eight types L1.1 to L3.3; grouped splitting is L3.2, 'Nonindependence between training and test samples'. https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/ . Pair it with scikit-learn §12.2 'Data leakage' → 12.2.1 'How to avoid data leakage' and 12.2.2, whose SelectKBest demo turns a true 0.50 accuracy into 0.76 and then fixes it with a Pipeline: https://scikit-learn.org/stable/common_pitfalls.html"
  },
  {
   "item": "Always establish the majority-class or simple baseline first",
   "label": "Hands-On ML (PyTorch) · Ch 3 → 'Performance Measures' → 'Measuri…",
   "url": "https://ageron.github.io/",
   "full": "Ch 3 → 'Performance Measures' → 'Measuring Accuracy Using Cross-Validation' — the DummyClassifier on the MNIST 5-detector that clears 90% accuracy without ever predicting a 5, which is the whole argument against quoting accuracy."
  },
  {
   "item": "Bagging vs boosting, and when each is the right call",
   "label": "Hands-On ML (PyTorch) · Ch 6 'Ensemble Learning and Random Fores…",
   "url": "https://ageron.github.io/",
   "full": "Ch 6 'Ensemble Learning and Random Forests' → 'Bagging and Pasting' (with 'Out-of-Bag Evaluation') for the variance story, then 'Boosting' → 'AdaBoost' and 'Gradient Boosting' for the bias story, closing with 'Stacking'. Mind the renumbering: this is Ch 7 in the 2022 TensorFlow 3rd edition, because SVMs moved to Appendix C in this one."
  },
  {
   "item": "Cross-validation schemes, and when k-fold is wrong (time series, grouped data)",
   "label": "Hands-On ML (PyTorch) · Ch 2 'Better Evaluation Using Cross-Vali…",
   "url": "https://scikit-learn.org/stable/modules/cross_validation.html",
   "full": "Ch 2 'Better Evaluation Using Cross-Validation' only teaches plain k-fold, so the failure cases are not in primary — scikit-learn User Guide §3.1.2.4 'Cross-validation iterators for grouped data' (GroupKFold, StratifiedGroupKFold, LeaveOneGroupOut, LeavePGroupsOut, GroupShuffleSplit) and §3.1.2.6 'Cross validation of time series data' (TimeSeriesSplit, where successive training sets are supersets of the ones before). https://scikit-learn.org/stable/modules/cross_validation.html"
  },
  {
   "item": "Entropy and Gini — be able to compute both by hand",
   "label": "Hands-On ML (PyTorch) · Ch 5 'Decision Trees' → 'Making Predicti…",
   "url": "https://scikit-learn.org/stable/modules/tree.html",
   "full": "Ch 5 'Decision Trees' → 'Making Predictions' (Gini impurity worked on the iris tree) and the CART cost function. For the two formulas side by side before you hand-compute, scikit-learn §1.10.7.1 'Classification criteria': Gini H = Σ p(1−p) and Log Loss/Entropy H = −Σ p log p, plus the note that splitting on Shannon entropy is equivalent to minimising log loss. https://scikit-learn.org/stable/modules/tree.html — one correction to the reading lists that cite this: §1.10.7.1 does not give a misclassification criterion, which appears only in the pruning section 1.10.9."
  },
  {
   "item": "Choosing k in clustering; the elbow and silhouette methods",
   "label": "Hands-On ML (PyTorch) · Ch 8 'Unsupervised Learning Techniques…",
   "url": "https://ageron.github.io/",
   "full": "Ch 8 'Unsupervised Learning Techniques' → '# Clustering' → '## K-Means' → 'Finding the Optimal Number of Clusters' — inertia and the elbow first, then the silhouette score and the silhouette diagrams; 'Centroid Initialization Methods' immediately before it explains why inertia depends on the seed. Chapter title and the Clustering → K-Means heading path confirmed in 08_unsupervised_learning.ipynb."
  },
  {
   "item": "Gradient descent variants and what each optimizer actually fixes",
   "label": "Hands-On ML (PyTorch) · Two places",
   "url": "https://ageron.github.io/",
   "full": "Two places. Plain batch, stochastic and mini-batch GD are Ch 4 → '# Gradient Descent' → '## Batch Gradient Descent', 'Stochastic Gradient Descent', 'Mini-batch Gradient Descent' (heading path confirmed in the notebook). The optimizers are Ch 11 'Training Deep Neural Networks' → 'Faster Optimizers': Momentum, Nesterov Accelerated Gradient, AdaGrad, RMSProp and Adam, each introduced by the specific pathology it repairs, then 'Learning Rate Scheduling'."
  },
  {
   "item": "Cosine similarity, batched",
   "label": "Deep-ML · 1072, 'Pairwise Cosine Similarity Matrix'",
   "url": "https://www.deep-ml.com/problems/1072",
   "full": "Problem 1072, 'Pairwise Cosine Similarity Matrix' — https://www.deep-ml.com/problems/1072 — this is the batched one. Warm up on Problem 76, 'Calculate Cosine Similarity Between Vectors', for the single-pair case: https://www.deep-ml.com/problems/76 . If the definition is rusty, scikit-learn §8.8.1 'Cosine similarity' states it as the L2-normalised dot product k(x,y) = xyᵀ/(‖x‖‖y‖): https://scikit-learn.org/stable/modules/metrics.html"
  },
  {
   "item": "k-means",
   "label": "Deep-ML · 17, 'K-Means Clustering'",
   "url": "https://www.deep-ml.com/problems/17",
   "full": "Problem 17, 'K-Means Clustering' — https://www.deep-ml.com/problems/17 — then Problem 1465, 'Vectorized K-Means with Broadcasting', https://www.deep-ml.com/problems/1465, which is the version an interviewer actually wants to watch you write. If you stall on the loop, the worked expectation–maximisation version is VanderPlas, Python Data Science Handbook §05.11 'In Depth: k-Means Clustering' → 'k-Means Algorithm: Expectation–Maximization': https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html (swap its one pairwise_distances_argmin call for the broadcasting line in §02.08, dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1), https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html)"
  },
  {
   "item": "Logistic regression with SGD, L2 and early stopping",
   "label": "Deep-ML · No single problem bundles all three, and…",
   "url": "https://www.deep-ml.com/problems/106",
   "full": "No single problem bundles all three, and that recombination is the actual exercise. Problem 106, 'Train Logistic Regression with Gradient Descent' (https://www.deep-ml.com/problems/106) for the core loop; Problem 43, 'Implement Ridge Regression Loss Function' (https://www.deep-ml.com/problems/43) for the L2 term; Problem 135, 'Implement Early Stopping Based on Validation Loss' (https://www.deep-ml.com/problems/135). Then assemble them yourself and diff against the backup's exercise 12."
  },
  {
   "item": "Softmax, numerically stable",
   "label": "Deep-ML 39 · Log Softmax (1227 is PyTorch)",
   "url": "https://www.deep-ml.com/problems/39",
   "full": "Problem 1227, 'Numerically Stable Softmax' — https://www.deep-ml.com/problems/1227 . The reference implementation to check yourself against is in the backup notebook, which I read directly: np.exp(logits - logits.max(axis=1, keepdims=True))."
  },
  {
   "item": "Linear regression via the normal equation, and via gradient descent",
   "label": "Deep-ML · 14, 'Linear Regression Using Normal Equa…",
   "url": "https://www.deep-ml.com/problems/14",
   "full": "Problem 14, 'Linear Regression Using Normal Equation' (https://www.deep-ml.com/problems/14) and Problem 15, 'Linear Regression Using Gradient Descent' (https://www.deep-ml.com/problems/15) — deliberately the same model two ways, which is exactly how the question gets asked. The closed form and its cubic cost are written up in the backup, 04_training_linear_models.ipynb → '# Linear Regression' → '## The Normal Equation'."
  },
  {
   "item": "Concept drift vs data drift, and how each is detected",
   "label": "Ng, ML in Production · Week 1 'Overview of the ML Lifecycle and…",
   "url": "https://www.youtube.com/watch?v=UyEtTyeahus",
   "full": "Week 1 'Overview of the ML Lifecycle and Deployment' names and separates concept drift from data drift — Course 1, Week 1, Lesson 5, https://www.youtube.com/watch?v=UyEtTyeahus — but it teaches no detection at all. For detection, not in primary — Evidently ML Observability Course, lesson 1.1 'ML lifecycle. What can go wrong with ML in production?' for the full taxonomy (concept drift gradual vs sudden, data drift, training-serving skew, broken upstream models, underperforming segments), https://learn.evidentlyai.com/ml-observability-course/module-1-introduction/ml-lifecycle , then lessons 2.6 'Data and prediction drift in ML' and 2.7 'Deep dive into data drift detection' for the actual tests."
  },
  {
   "item": "Monitoring a model in production: what you log and what alerts",
   "label": "Ng, ML in Production · Course 1, Week 1, Lesson 7 'Monitoring'",
   "url": "https://www.youtube.com/watch?v=hq_XyP9y0xg",
   "full": "Course 1, Week 1, Lesson 7 'Monitoring' — https://www.youtube.com/watch?v=hq_XyP9y0xg — dashboards, which metrics belong on them, and setting the thresholds that page a human; then Lesson 8 'Pipeline monitoring', https://www.youtube.com/watch?v=79UqdjnPEZ0 , for multi-stage systems. Deepen with backup lessons 1.3 'ML monitoring metrics. What exactly can you monitor?', 4.1 'Logging for ML monitoring' and 4.2 'How to prioritize ML monitoring metrics' — that last pair is the half an interviewer pushes on with \"and what would you actually alert on\"."
  },
  {
   "item": "Data-centric AI — why improving labels usually beats improving the model",
   "label": "Ng, ML in Production · Course 1, Week 2, Lesson 10 'Data-centri…",
   "url": "https://www.youtube.com/watch?v=k3UYUmp3Bi4",
   "full": "Course 1, Week 2, Lesson 10 'Data-centric AI development' (https://www.youtube.com/watch?v=k3UYUmp3Bi4), then Week 2, Lesson 16 'From big data to good data' (https://www.youtube.com/watch?v=qOEeK1SNF3k), then Week 3 'Data Definition and Baseline' on small data and label consistency. For the rigorous version with labs, MIT 'Introduction to Data-Centric AI' (IAP 2024), Lecture 1 'Data-Centric AI vs. Model-Centric AI' — full written notes on the page, free, CC BY-NC-SA: https://dcai.csail.mit.edu/2024/data-centric-model-centric/ — then Lecture 2 'Label Errors and Confident Learning' and Lecture 6 'Data-centric Evaluation of ML Models' from the index at https://dcai.csail.mit.edu/"
  },
  {
   "item": "Andrew Ng — “Advice for applying machine learning”",
   "label": "Ng, ML in Production · Course 1, Week 2 'Modeling Challenges an…",
   "url": "https://www.youtube.com/watch?v=O5mqR4EFBQk",
   "full": "Course 1, Week 2 'Modeling Challenges and Strategies' is that lecture rebuilt: start at Lesson 4 'Establish a baseline' (https://www.youtube.com/watch?v=O5mqR4EFBQk) and run on through error analysis, prioritising what to work on, skewed datasets and performance auditing. Read the 2007 original alongside it, because it is short and still the sharpest statement — Andrew Ng, CS229 'Advice for applying Machine Learning', ~30 slides covering diagnostics for bias vs variance, optimisation-algorithm vs objective-function diagnostics, error analysis, ablative analysis and premature statistical optimisation: https://cs229.stanford.edu/materials/ML-advice.pdf (Machine Learning Yearning is the long-form version but is email-gated, so this deck is the better link)."
  }
 ],
 "t10": [
  {
   "item": "URL shortener",
   "label": "Hello Interview, \"Design a URL Shortener…",
   "url": "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly",
   "full": "not in primary — Hello Interview, \"Design a URL Shortener Like Bitly\", https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly : Deep Dive 1 unique short URLs (Hash Function vs Unique Counter with Base62), Deep Dive 2 fast redirects (Add an Index → in-memory Redis cache → CDN and edge), Deep Dive 3 scaling to 1B URLs and 100M DAU, then the closing \"What is Expected at Each Level\" box. Free, full text. Companion video (59 min, Hello Interview): https://www.youtube.com/watch?v=iUU4O1sWtJA"
  },
  {
   "item": "Distributed rate limiter",
   "label": "Hello Interview, \"Design a Distributed R…",
   "url": "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter",
   "full": "not in primary — Hello Interview, \"Design a Distributed Rate Limiter\", https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter : High-Level Design 1 (In-Process vs Dedicated Service vs API Gateway/Load Balancer), then Deep Dives 1–5 — 1M requests/second, high availability (Fail-Closed vs Fail-Open), latency overhead, hot keys, dynamic rule configuration (Poll-Based vs Push-Based). Companion video (56 min): https://www.youtube.com/watch?v=MIJFyUPG4Z4"
  },
  {
   "item": "⭐ RAG over 10k enterprise documents with per-tenant isolation",
   "label": "Huyen, AI Engineering · Primary Ch 6 \"RAG and Agents\", pp. 253–2…",
   "url": "https://qdrant.tech/documentation/manage-data/multitenancy/",
   "full": "Primary Ch 6 \"RAG and Agents\", pp. 253–273 — RAG Architecture p.256, Retrieval Algorithms p.257, Retrieval Optimization p.268. Tenant isolation is genuinely absent from the book: Qdrant, \"Multitenancy\" (§Partition by Payload, §Calibrate Performance, §Limitations, §Per-Tenant IDF Statistics, §User-Defined Sharding, §Tiered Multitenancy including promoting a tenant to a dedicated shard) — https://qdrant.tech/documentation/manage-data/multitenancy/"
  },
  {
   "item": "Real-time chat",
   "label": "Hello Interview, \"Design a Messaging App…",
   "url": "https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp",
   "full": "not in primary — Hello Interview, \"Design a Messaging App Like WhatsApp\", https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp : High-Level Design 1–4 (group chat, send/receive, offline delivery up to 30 days, media), Deep Dive 1 billions of concurrent users (Consistent Hashing of Chat Servers → Offload to Pub/Sub, with both fan-out scenarios worked), Deep Dive 3 WebSocket failure (ACK timeouts → application-level heartbeats), Deep Dive 4 undelivered messages (sequence numbers per chat with gap detection, piggybacked on heartbeats), Deep Dives 5–6 out-of-order messages and last-seen. Companion video (58 min): https://www.youtube.com/watch?v=cr6p0n0N-VA"
  },
  {
   "item": "⭐ LLM customer-support agent with tool calling and human escalation",
   "label": "Huyen, AI Engineering · Primary Ch 6 \"Agents\", pp. 275–300",
   "url": "https://www.anthropic.com/engineering/building-effective-agents",
   "full": "Primary Ch 6 \"Agents\", pp. 275–300 — Agent Overview p.276, Tools p.278, Planning p.281, Agent Failure Modes and Evaluation p.298. The escalation checkpoint and the control-flow patterns are not in the book: Anthropic, \"Building effective agents\" — §Workflow: Routing, §Workflow: Orchestrator-workers, §Workflow: Evaluator-optimizer, Appendix 1-A \"Customer support\" (the exact system in this rep), Appendix 2 \"Prompt engineering your tools\" — https://www.anthropic.com/engineering/building-effective-agents"
  },
  {
   "item": "⭐ Evaluation and observability platform for LLM applications",
   "label": "Huyen, AI Engineering · Primary Ch 3 \"Evaluation Methodology\" pp…",
   "url": "https://hamel.dev/blog/posts/evals-faq/",
   "full": "Primary Ch 3 \"Evaluation Methodology\" pp.113–156 (AI as a Judge p.136, Limitations of AI as a Judge p.141), Ch 4 \"Design Your Evaluation Pipeline\" pp.200–208 (Steps 1–3), Ch 10 §Monitoring and Observability p.465. For what an internal platform has to standardise, which the book does not cover: Husain and Shankar, \"AI Evals: Everything You Need to Know\" (published 18 Sep 2026, updated 21 Sep 2026) — §Tools & Infrastructure, specifically \"What should an internal eval platform standardize across teams?\" and \"What gaps in eval tooling should I be prepared to fill myself?\", plus \"What's the difference between guardrails and evaluators?\" and the CI/CD-versus-production-monitoring question — https://hamel.dev/blog/posts/evals-faq/"
  },
  {
   "item": "⭐ LLM inference serving at scale",
   "label": "Huyen, AI Engineering · Primary Ch 9 \"Inference Optimization\" pp…",
   "url": "https://jax-ml.github.io/scaling-book/inference",
   "full": "Primary Ch 9 \"Inference Optimization\" pp.405–447 — Inference Overview p.406, Inference Performance Metrics p.412, AI Accelerators p.419, Inference Service Optimization p.440. For the arithmetic the book states but does not derive: Austin et al. (Google DeepMind), \"How to Scale Your Model\", Part 7 \"All About Transformer Inference\" — §Theoretical estimates for LLM latency and throughput, §What about memory?, §Distributing Inference Over Multiple Accelerators (Prefill, Generation, Sharding the KV cache), §Designing an Effective Inference Engine (Continuous batching, Prefix caching) — https://jax-ml.github.io/scaling-book/inference (TPU-first; Part 12 covers GPUs)"
  },
  {
   "item": "⭐ Real-time voice agent under an 800ms budget",
   "label": "Voice AI & Voice Agents: An Illustrated…",
   "url": "https://voiceaiandvoiceagents.com/",
   "full": "not in primary — \"Voice AI & Voice Agents: An Illustrated Primer\" (2026 edition), https://voiceaiandvoiceagents.com/ : §5.1 Latency, §5.7 Network transport (5.7.1 WebSockets and WebRTC, 5.7.4 Network routing), §5.8 Turn detection (5.8.4 semantic VAD and smart turn, 5.8.5 state of the art), §5.9 Interruption handling, §5.11.2 Function call latency, §11.1 Architecture, §11.2 Calculating per-minute cost. Worth knowing before you quote a number in the room: §5.1 states 1,500 ms voice-to-voice as the target to aim for, not 800 ms — so defend the tighter budget rather than assuming it."
  },
  {
   "item": "⭐ Agentic coding assistant",
   "label": "the book gives it one page (Ch 1 §Coding…",
   "url": "https://arxiv.org/abs/2608.10934",
   "full": "not in primary — the book gives it one page (Ch 1 §Coding, p.20). Marco Tulio Valente, \"Understanding the Architecture of Coding Agents: An Exploratory Study Using a Research Prototype\", arXiv 2608.10934 (v1 11 Aug 2026, v2 25 Aug 2026): the main architectural components, their responsibilities, interactions and execution flow, plus Ark, a minimal open-source reference agent — https://arxiv.org/abs/2608.10934"
  },
  {
   "item": "⭐ Document Q&A with citations and multi-hop questions",
   "label": "Huyen, AI Engineering · Primary Ch 6 §Retrieval Optimization p.2…",
   "url": "https://platform.claude.com/docs/en/build-with-claude/citations",
   "full": "Primary Ch 6 §Retrieval Optimization p.268 (chunking, hybrid search, reranking) and §Planning p.281 (multi-hop is agentic retrieval). Citation mechanics are not in the book: Claude docs, \"Citations\" — §How citations work, §Citable versus non-citable content, §Citation indices, §Token costs, §Document types, which gives the three granularities char_location, page_location and content_block_location — https://platform.claude.com/docs/en/build-with-claude/citations"
  },
  {
   "item": "Design a search engine with LLM synthesis over results",
   "label": "Huyen, AI Engineering · Split it",
   "url": "https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-post-search",
   "full": "Split it. Retrieval half, not in primary — Hello Interview, \"Design Facebook's Post Search\", https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-post-search : High-Level Design 2 (Create an Inverted Index), High-Level Design 3 (Multiple Indexes for recency vs likes), Deep Dive 2 multi-keyword and phrase queries (Intersection-and-Filter vs Bigrams/Shingles), Deep Dive 3 write volume (two-stage architecture), Deep Dive 4 storage. Synthesis half: Anthropic, \"How we built our multi-agent research system\" §Architecture overview for Research — https://www.anthropic.com/engineering/multi-agent-research-system"
  },
  {
   "item": "Cross-conversation memory for a chat product",
   "label": "Huyen, AI Engineering · Primary Ch 6 §Memory pp.300–305",
   "url": "https://docs.langchain.com/oss/python/concepts/memory",
   "full": "Primary Ch 6 §Memory pp.300–305 — five pages, too thin to carry a rep. Use LangChain, \"Memory overview\": §Short-term memory (and Manage short-term memory), §Long-term memory — Semantic (Profile vs Collection), Episodic, Procedural — §Writing memories (In the hot path vs In the background), §Memory storage — https://docs.langchain.com/oss/python/concepts/memory"
  },
  {
   "item": "Then re-do the first two, cold and recorded, and diff against the originals",
   "label": "method, not content",
   "url": "https://www.hellointerview.com/blog/how-id-prepare",
   "full": "not in primary — method, not content. Hello Interview, \"How I'd Prepare for a System Design Interview if I Were Starting From Scratch\" §4 \"Work Backwards from Common Problems\" specifies the drill: attempt it cold on a blank board with the timer running, then read the breakdown to find where you went wrong — https://www.hellointerview.com/blog/how-id-prepare . Do the recorded re-run on Guided Practice, where \"Design Bitly\" is the free problem and returns per-step rubric coaching plus a final report with peer comparison — that report is your diff — https://www.hellointerview.com/practice/overview"
  },
  {
   "item": "The four patterns every prompt maps to",
   "label": "System Design in a Hurry · Primary's sibling page in the same free…",
   "url": "https://www.hellointerview.com/learn/system-design/in-a-hurry/patterns",
   "full": "Primary's sibling page in the same free course: \"Common Patterns\" — Pushing Realtime Updates, Managing Long-Running Tasks, Dealing with Contention, Scaling Reads, Scaling Writes, Handling Large Blobs, Multi-Step Processes, Proximity-Based Services, then §Pattern Selection — https://www.hellointerview.com/learn/system-design/in-a-hurry/patterns . It is eight, not four, so reconcile your four against this list rather than assuming they agree. The overview page is free; the individual /patterns/* deep-dive pages are paywalled. For the GenAI counterpart, AI Engineering Ch 10 Steps 1–5, pp.449–465."
  },
  {
   "item": "Senior signal: reasoning under uncertainty, tradeoff fluency, communication clarity",
   "label": "System Design in a Hurry · Hello Interview, \"The System Design Inte…",
   "url": "https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level",
   "full": "Hello Interview, \"The System Design Interview: What is Expected at Each Level\" — the three axes actually graded are Breadth, Depth and Proactiveness, each broken out Mid-level / Senior / Staff+ — https://www.hellointerview.com/blog/the-system-design-interview-what-is-expected-at-each-level . Then \"5 Keys to Staff-Level System Design Interviews\": 1) match your communication to the interviewer's level, 2) identify the crux of the problem, 3) ruthlessly cut complexity, 4) demonstrate your depth, 5) show off your instincts — https://www.hellointerview.com/blog/staff-level-system-design . Every problem breakdown also ends with its own \"What is Expected at Each Level\" box, so you can score each rep as you finish it. To calibrate tone, watch a senior candidate graded in real time: \"Senior System Design Mock Interview: Design an e-commerce platform\" (26 Apr 2026, 71 min) — feedback and reflection at 51:14 — https://www.youtube.com/watch?v=RuGY_1pap74"
  },
  {
   "item": "Cost and latency arithmetic out loud, in every rep",
   "label": "System Design in a Hurry · Primary page §Requirements (~5 minutes)…",
   "url": "https://www.hellointerview.com/blog/mastering-estimation",
   "full": "Primary page §Requirements (~5 minutes) → 3) Capacity Estimation, which tells you when the maths is worth doing at all; the primary also budgets the rep at 5 / 2 / 5 / 10–15 / 10 minutes. The method is in Hello Interview, \"System Design Interview Fundamentals: Mastering Estimation\" — §How to Estimate Like an Engineer, §What to Estimate, §Break it Down, §Facts to Know (Metrics, Latencies, Storage, Business), §Common Mistakes — https://www.hellointerview.com/blog/mastering-estimation . It is entirely classical and the in-course \"Numbers to Know\" page is paywalled, so take the GenAI units from Think in Models Ep. 4 \"LLM Cost & Capacity Planning: Tokens, Prefill and Decode\" (14 min) — 2:08 why RPS limits are the wrong unit, 4:15 tokens/prefill/decode, 7:27 how one request becomes 100x more expensive, 9:17 token-aware rate limiting and capacity planning, 12:12 the estimation exercise — https://www.youtube.com/watch?v=G7Yc-vzEl6g , plus AI Engineering Ch 4 §Cost and Latency p.177 and Ch 9 §Inference Performance Metrics p.412."
  },
  {
   "item": "❌ The documented mistakes",
   "label": "System Design in a Hurry · Hello Interview, \"Over-engineering is ge…",
   "url": "https://www.hellointerview.com/blog/over-engineering-is-getting-you-down-levelled",
   "full": "Hello Interview, \"Over-engineering is getting you down-levelled\" — §First, simplify where possible, §Next, research the downsides, §Lastly, learn the details — https://www.hellointerview.com/blog/over-engineering-is-getting-you-down-levelled ; plus §Common Mistakes in \"Mastering Estimation\" and the inline callouts on the primary Delivery page about unquantified non-functional requirements and estimation that changes nothing. For the LLM-specific failure list, which Hello Interview does not have: Think in Models Ep. 3 \"Why LLMs fail differently?\" (13 min) — 3:03 traditional software failures vs LLM failures, 3:41 a successful response that is still wrong, 4:36 silent failure, 8:08 common mistakes in AI system design interviews, 8:13 why a bigger model is not the answer, 8:40 why more metrics may not help, 12:30 why 200 OK does not mean the answer is correct, 12:43 the decomposition framework — https://www.youtube.com/watch?v=yW10lYS3PKM"
  },
  {
   "item": "Chip Huyen — Building a Generative AI Platform",
   "label": "Huyen, GenAI Platform · The primary itself: Step 1 Enhance Conte…",
   "url": "https://huyenchip.com/2024/07/25/genai-platform.html",
   "full": "The primary itself: Step 1 Enhance Context (RAGs, RAGs with tabular data, Agentic RAGs, query rewriting), Step 2 Put in Guardrails (input guardrails, private-information leaks, jailbreaking, output guardrails, failure management, guardrail tradeoffs), Step 3 Add Model Router and Gateway, Step 4 Reduce Latency with Cache (prompt, exact, semantic), Step 5 Add Complex Logic and Write Actions, then Observability (metrics, logs, traces) and AI Pipeline Orchestration — https://huyenchip.com/2024/07/25/genai-platform.html . It is Jul 2024, so Step 5 predates the agent vocabulary; the current version of the same argument is AI Engineering Ch 10 pp.449–474, where that step is renamed \"Add Agent Patterns\" (p.463)."
  },
  {
   "item": "Anthropic — Building a multi-agent research system",
   "label": "Anthropic, \"How we built our multi-agent…",
   "url": "https://www.anthropic.com/engineering/multi-agent-research-system",
   "full": "not in primary — Anthropic, \"How we built our multi-agent research system\": read §Architecture overview for Research and §Production reliability and engineering challenges, which are the two sections that get asked back at you; §Effective evaluation of agents is the third if you have time — https://www.anthropic.com/engineering/multi-agent-research-system (the URL has moved: /engineering/multi-agent-research-system, not /engineering/built-multi-agent-research-system)"
  },
  {
   "item": "evidentlyai.com/ml-system-design — 800 case studies from 150+ companies",
   "label": "the backup itself",
   "url": "https://www.evidentlyai.com/ml-system-design",
   "full": "not in primary — the backup itself, https://www.evidentlyai.com/ml-system-design . The page states its own filter instructions: use the technology tags \"Generative AI & LLM\", \"RAG\" and \"AI agents\". Unfiltered, the database is mostly classical recsys, search and ranking, and fraud, and will eat your week. Read two entries per rep you are about to do. Header confirms: 800 case studies, 150+ companies, last updated 22 Dec 2025."
  },
  {
   "item": "Uber GenAI Gateway · Slack AI · DoorDash eval flywheel",
   "label": "Uber, \"Navigating the LLM Landscape: Ube…",
   "url": "https://www.uber.com/en-US/blog/genai-gateway/",
   "full": "not in primary — Uber, \"Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway\" §Design & Architecture and §Challenges → PII Redactor: https://www.uber.com/en-US/blog/genai-gateway/ (the bare /blog/genai-gateway/ path returns 406 to non-browser clients; the /en-US/ path renders). Slack, \"How we built Slack AI to be secure and private\" — all four headings are trust-boundary arguments: customer data never leaves Slack, no LLM training on customer data, Slack AI only operates on data the user can already see, enterprise-grade compliance: https://slack.com/blog/news/how-we-built-slack-ai-to-be-secure-and-private . DoorDash — the original engineering post is Cloudflare-blocked, so read ByteByteGo, \"How DoorDash Built a Testing System to Evaluate LLMs\": §What the Flywheel Actually Does (offline simulator plus evaluation framework), §Simulating Customers That Push Back, §Using an LLM to Judge Another LLM, §Fixing Hallucinations by Giving the Chatbot Less Information: https://blog.bytebytego.com/p/how-doordash-built-a-testing-system"
  },
  {
   "item": "Hello Interview — System Design in a Hurry (free tier)",
   "label": "Huyen, GenAI Platform",
   "url": "https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction",
   "full": "not in primary — https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction . Verified free on 18 Oct 2026: the Delivery Framework, Core Concepts, Key Technologies, the Common Patterns overview, the Deep Dives (Redis, Kafka, Cassandra, DynamoDB, Elasticsearch, Temporal, vector databases), and all 32 problem breakdowns, Bitly / Distributed Rate Limiter / WhatsApp / FB Post Search among them. Verified paywalled: Numbers to Know, the individual /patterns/* deep-dive pages, and the ChatGPT breakdown (its deep-dive headings are visible, the body is not). Also verified: the ML track at /learn/ml-system-design is four concept pages plus three classical breakdowns (bot detection, harmful content, video recommendations) — no RAG, agents, serving or LLM evaluation, so do not plan the starred reps around it."
  },
  {
   "item": "Excalidraw — build one template in 15 minutes",
   "label": "opens and draws with no sign-in; pull re…",
   "url": "https://excalidraw.com/",
   "full": "not in primary — https://excalidraw.com/ opens and draws with no sign-in; pull reusable shapes from the directory at https://libraries.excalidraw.com/ . The 15-minute drill itself is specified in Hello Interview's \"How I'd Prepare\" §4 Work Backwards from Common Problems: blank board, timer running, no reference open — https://www.hellointerview.com/blog/how-id-prepare"
  }
 ],
 "t11": [
  {
   "item": "Two Sum",
   "label": "NeetCode · Two Sum (8m26s)",
   "url": "https://www.youtube.com/watch?v=KLlXCFG5TnA",
   "full": "Video \"Two Sum - Leetcode 1 - HashMap - Python\" (8m26s) — https://www.youtube.com/watch?v=KLlXCFG5TnA . Then type it at https://neetcode.io/solutions/two-sum , approach 4 \"Hash Map (One Pass)\" (verified: 4 approaches listed)."
  },
  {
   "item": "Group Anagrams",
   "label": "NeetCode · Group Anagrams - Categorize Strings by C…",
   "url": "https://www.youtube.com/watch?v=vzdNOK2oB2E",
   "full": "Video \"Group Anagrams - Categorize Strings by Count - Leetcode 49\" (8m11s) — https://www.youtube.com/watch?v=vzdNOK2oB2E . Written: https://neetcode.io/solutions/group-anagrams , approach 2 \"Hash Table\" (the count-tuple key); its pitfall \"Using a Mutable Key Type for the Hash Map\" is the bug you will hit first."
  },
  {
   "item": "Product of Array Except Self",
   "label": "NeetCode · Product of Array Except Self (11m53s)",
   "url": "https://www.youtube.com/watch?v=bNvIQI2wAjk",
   "full": "Video \"Product of Array Except Self - Leetcode 238 - Python\" (11m53s) — https://www.youtube.com/watch?v=bNvIQI2wAjk . Written: https://neetcode.io/solutions/product-of-array-except-self , approach 4 \"Prefix & Suffix (Optimal)\" — this is a prefix-product problem, not a hashing one, so expect the follow-up \"now do it in O(1) extra space\"."
  },
  {
   "item": "3Sum",
   "label": "NeetCode · 3Sum (12m53s)",
   "url": "https://www.youtube.com/watch?v=jzZsG8n2R9A",
   "full": "Video \"3Sum - Leetcode 15 - Python\" (12m53s) — https://www.youtube.com/watch?v=jzZsG8n2R9A . Then https://neetcode.io/solutions/3sum , approach 3 \"Two Pointers\", and read its pitfall \"Forgetting to Skip Duplicates\" — that single omission is what fails this problem in interviews."
  },
  {
   "item": "Container With Most Water",
   "label": "NeetCode · Container with Most Water (12m36s)",
   "url": "https://www.youtube.com/watch?v=UuiTKBwPgAo",
   "full": "Video \"Container with Most Water - Leetcode 11 - Python\" (12m36s) — https://www.youtube.com/watch?v=UuiTKBwPgAo . Then https://neetcode.io/solutions/container-with-most-water , approach 2 \"Two Pointers\" (move the shorter wall); its pitfall \"Moving the Wrong Pointer\" is the whole proof obligation."
  },
  {
   "item": "Longest Substring Without Repeating Characters",
   "label": "BCtCI · Ch 38 §\"Maximum Windows\" → RECIPE 3",
   "url": "https://www.youtube.com/watch?v=wiGpQwVHdE0",
   "full": "Ch 38 §\"Maximum Windows\" → RECIPE 3. MAXIMUM WINDOW RECIPE, introduced via Problem 38.8 \"Maximum With At Most 3 Bad Days\"; the nearest worked sibling is Problem 38.12 \"Longest Period At-Most K Distinct\". Recipe 3 is the template that solves LeetCode 3, but the exact problem is not in the chapter — pair it with NeetCode, \"Longest Substring Without Repeating Characters - Leetcode 3 - Python\" (6m45s) https://www.youtube.com/watch?v=wiGpQwVHdE0 and https://neetcode.io/solutions/longest-substring-without-repeating-characters approach 3 \"Sliding Window (Optimal)\"."
  },
  {
   "item": "Minimum Window Substring",
   "label": "BCtCI · Ch 38 §\"Minimum Windows Problem Set\" → P…",
   "url": "https://drive.google.com/drive/folders/1AdUu4jh6DGwmCxfgnDQEMWWyo6_whPHJ",
   "full": "Ch 38 §\"Minimum Windows Problem Set\" → Problem 38.15 \"Shortest With All Letters\" (pg 527). I checked the statement: it is this exact problem, renamed, returning the length. Read §\"Limitations of Maximum Windows\" and then RECIPE 4. MINIMUM WINDOW RECIPE immediately before it, so you see why the minimum-window template must differ."
  },
  {
   "item": "Valid Parentheses",
   "label": "NeetCode · Valid Parentheses - Stack (10m43s)",
   "url": "https://www.youtube.com/watch?v=WTzjTskDFMg",
   "full": "Video \"Valid Parentheses - Stack - Leetcode 20 - Python\" (10m43s) — https://www.youtube.com/watch?v=WTzjTskDFMg . Then https://neetcode.io/solutions/valid-parentheses , approach 2 \"Stack\"; its pitfalls \"Checking Stack Empty Before Popping\" and \"Forgetting to Check if Stack is Empty at the End\" are the two test cases that fail you."
  },
  {
   "item": "Min Stack",
   "label": "NeetCode · Design Min Stack - Amazon Interview Ques…",
   "url": "https://www.youtube.com/watch?v=qkLl7nAwDPo",
   "full": "Video \"Design Min Stack - Amazon Interview Question - Leetcode 155 - Python\" (8m53s) — https://www.youtube.com/watch?v=qkLl7nAwDPo . Then https://neetcode.io/solutions/min-stack , approach 3 \"One Stack\" is the one to be able to write; note the pitfall \"Integer Overflow in the Encoded Value Approach\" before you show off the encoded trick."
  },
  {
   "item": "Koko Eating Bananas",
   "label": "BCtCI · Ch 29 §\"Guess-and-Check Technique\" (star…",
   "url": "https://drive.google.com/drive/folders/1AdUu4jh6DGwmCxfgnDQEMWWyo6_whPHJ",
   "full": "Ch 29 §\"Guess-and-Check Technique\" (start at Problem 29.9 \"Min-Subarray-Sum Split\"), then §\"Guess-and-Check Problem Set\" → Problem 29.11 \"Min Pages Per Day\" (pg 341). I read the statement: minimum pages per day to finish in `days`, finishing each chapter before starting another — structurally identical to Koko, same sum-of-ceilings check."
  },
  {
   "item": "Search in Rotated Sorted Array",
   "label": "BCtCI · Ch 29 §\"Transition-Point Recipe\" → RECIP…",
   "url": "https://www.youtube.com/watch?v=U8XENwh8Oy8",
   "full": "Ch 29 §\"Transition-Point Recipe\" → RECIPE 1 (the book cross-references it as pg 329) for the one template to memorise, then Problem 29.3 \"Valley Bottom\" (pg 334, in §\"Binary Search Problem Set\") — that is the find-the-minimum/pivot half. The full LeetCode 33 rotated search is not in this chapter: not in primary — NeetCode, \"Search in rotated sorted array - Leetcode 33 - Python\" (13m28s) https://www.youtube.com/watch?v=U8XENwh8Oy8 , plus https://neetcode.io/solutions/search-in-rotated-sorted-array approach 3 \"Binary Search (Two Pass)\" and approach 4 \"Binary Search (One Pass)\"."
  },
  {
   "item": "Reverse Linked List",
   "label": "NeetCode · Reverse Linked List - Iterative AND Recu…",
   "url": "https://www.youtube.com/watch?v=G0_I-ZF0S38",
   "full": "Video \"Reverse Linked List - Iterative AND Recursive - Leetcode 206 - Python\" (11m07s) — https://www.youtube.com/watch?v=G0_I-ZF0S38 . One sitting gives you both forms, which matters because the recursive version is the standard follow-up. Written: https://neetcode.io/solutions/reverse-linked-list ; pitfall \"Losing the Reference to the Next Node\"."
  },
  {
   "item": "Merge Two Sorted Lists",
   "label": "NeetCode · Merge Two Sorted Lists (6m16s)",
   "url": "https://www.youtube.com/watch?v=XIdigk956u0",
   "full": "Video \"Merge Two Sorted Lists - Leetcode 21 - Python\" (6m16s) — https://www.youtube.com/watch?v=XIdigk956u0 . Written: https://neetcode.io/solutions/merge-two-sorted-lists , approach 2 \"Iteration\" with a dummy head — its pitfall \"Not Attaching the Remaining Nodes\" is the one-line omission that drops half your test cases."
  },
  {
   "item": "Linked List Cycle",
   "label": "NeetCode · Linked List Cycle - Floyd's Tortoise and…",
   "url": "https://www.youtube.com/watch?v=gBTe7lFR3vc",
   "full": "Video \"Linked List Cycle - Floyd's Tortoise and Hare - Leetcode 141 - Python\" (10m43s) — https://www.youtube.com/watch?v=gBTe7lFR3vc (confirmed present in this playlist). Then https://neetcode.io/solutions/linked-list-cycle : read approach 1 \"Hash Set\" first so you can offer the O(n)-space answer and then improve it to approach 2 \"Fast And Slow Pointers\", and take the pitfall \"Not Checking if Fast Pointer Can Advance Safely\" — that null check is the bug everybody writes."
  },
  {
   "item": "Invert Binary Tree",
   "label": "NeetCode · Invert Binary Tree - Depth First Search…",
   "url": "https://www.youtube.com/watch?v=OnSn2XEQ4MY",
   "full": "Video \"Invert Binary Tree - Depth First Search - Leetcode 226\" (3m54s) — https://www.youtube.com/watch?v=OnSn2XEQ4MY . Written: https://neetcode.io/solutions/invert-binary-tree (3 approaches: BFS, DFS, iterative DFS)."
  },
  {
   "item": "Binary Tree Level Order Traversal",
   "label": "NeetCode · Binary Tree Level Order Traversal - BFS…",
   "url": "https://www.youtube.com/watch?v=6ZnyEApgFYg",
   "full": "Video \"Binary Tree Level Order Traversal - BFS - Leetcode 102\" (9m35s) — https://www.youtube.com/watch?v=6ZnyEApgFYg . Written: https://neetcode.io/solutions/binary-tree-level-order-traversal ; its pitfall \"Processing Nodes Individually Instead of by Level\" is the difference between a flat list and the right answer."
  },
  {
   "item": "Binary Tree Maximum Path Sum",
   "label": "NeetCode · Binary Tree Maximum Path Sum - DFS (15m1…",
   "url": "https://www.youtube.com/watch?v=Hr5cWUld4vU",
   "full": "Video \"Binary Tree Maximum Path Sum - DFS - Leetcode 124 - Python\" (15m18s) — https://www.youtube.com/watch?v=Hr5cWUld4vU . Then https://neetcode.io/solutions/binary-tree-maximum-path-sum approach 2, and read all five of its pitfalls — especially \"Returning the Full Path Sum Instead of Single-Branch Sum\" and \"Initializing Result to Zero Instead of Negative Infinity\"."
  },
  {
   "item": "Validate Binary Search Tree",
   "label": "NeetCode · Approach 2 \"Depth First Search",
   "url": "https://www.youtube.com/watch?v=s6ATEkipzow",
   "full": "Approach 2 \"Depth First Search\" — carry a (min, max) bound downward. Read both pitfalls before you code: \"Only Comparing with the Immediate Parent\" (the wrong answer most people give first) and \"Using Inclusive Bounds Instead of Exclusive\". Companion video, 9m56s: \"Validate Binary Search Tree - Depth First Search - Leetcode 98\" https://www.youtube.com/watch?v=s6ATEkipzow ."
  },
  {
   "item": "K Closest Points to Origin",
   "label": "NeetCode · The page itself: read \"Recommended Time…",
   "url": "https://www.youtube.com/watch?v=rI2EBUEMfTk",
   "full": "The page itself: read \"Recommended Time & Space Complexity\" (it tells you to aim for O(n log k) time, O(k) space), then Hint 1 and Hint 2, which walk you from sorting to a size-k max-heap. Embedded video is \"K Closest Points to Origin - Heap / Priority Queue - Leetcode 973 - Python\" (9m28s) https://www.youtube.com/watch?v=rI2EBUEMfTk . Full write-up with all four approaches (sorting, min-heap, max-heap, quickselect) at https://neetcode.io/solutions/k-closest-points-to-origin — take its pitfall \"Computing Actual Distance with Square Root\" and compare squared distances."
  },
  {
   "item": "Kth Largest Element in an Array",
   "label": "NeetCode · The page itself (hints 1–2 build the siz…",
   "url": "https://www.youtube.com/watch?v=XEmy13g1Qxc",
   "full": "The page itself (hints 1–2 build the size-k min-heap), then the video \"Kth Largest Element in an Array - Quick Select - Leetcode 215 - Python\" (18m48s) https://www.youtube.com/watch?v=XEmy13g1Qxc . Write-up at https://neetcode.io/solutions/kth-largest-element-in-an-array : approaches 3 \"Quick Select\" and 4 \"Quick Select (Optimal)\", plus the pitfall \"QuickSelect Worst Case on Sorted Arrays\" — use a random pivot and say why."
  },
  {
   "item": "Subsets",
   "label": "NeetCode · Subsets - Backtracking (8m47s)",
   "url": "https://www.youtube.com/watch?v=REOH22Xwdkk",
   "full": "Video \"Subsets - Backtracking - Leetcode 78\" (8m47s) — https://www.youtube.com/watch?v=REOH22Xwdkk . Then https://neetcode.io/solutions/subsets : approach 1 \"Backtracking\" is the one to write, approach 3 \"Bit Manipulation\" is a cheap follow-up to have ready; pitfall \"Modifying the Subset After Adding to Result\" (append a copy, not the live list)."
  },
  {
   "item": "Combination Sum",
   "label": "NeetCode · Combination Sum - Backtracking (15m10s)",
   "url": "https://www.youtube.com/watch?v=GBKI9VSKdGg",
   "full": "Video \"Combination Sum - Backtracking - Leetcode 39 - Python\" (15m10s) — https://www.youtube.com/watch?v=GBKI9VSKdGg . Then https://neetcode.io/solutions/combination-sum ; its pitfall \"Moving to Next Index After Including an Element\" is the exact line that turns combinations into the wrong answer when reuse is allowed."
  },
  {
   "item": "LRU Cache",
   "label": "NeetCode · approach 2 \"Doubly Linked List",
   "url": "https://neetcode.io/solutions/lru-cache",
   "full": "https://neetcode.io/solutions/lru-cache , approach 2 \"Doubly Linked List\" — that is the one to be able to write. Approach 3 \"Built-In Data Structure\" is OrderedDict; know it as the one-liner you offer and then replace, because most interviewers disallow it. Pitfall \"Not Storing Keys in List Nodes\" is what breaks eviction. Video \"LRU Cache - Twitch Interview Question - Leetcode 146\" (17m49s) https://www.youtube.com/watch?v=7ABFKPK2hD4 ; editor at https://neetcode.io/problems/lru-cache/question ."
  },
  {
   "item": "Implement Trie",
   "label": "NeetCode · Sibling page in the same resource:",
   "url": "https://neetcode.io/solutions/implement-trie-prefix-tree",
   "full": "Sibling page in the same resource: https://neetcode.io/solutions/implement-trie-prefix-tree — approach 1 \"Prefix Tree (Array)\" for the 26-slot version, approach 2 \"Prefix Tree (Hash Map)\" for the general one. Pitfall \"Confusing search and startsWith\" is essentially the entire test-case set. Video \"Implement Trie (Prefix Tree) - Leetcode 208\" (18m55s) https://www.youtube.com/watch?v=oobqoCJlHA0 ."
  },
  {
   "item": "Number of Islands",
   "label": "NeetCode · NUMBER OF ISLANDS (11m41s)",
   "url": "https://www.youtube.com/watch?v=pV2kpPD66nE",
   "full": "Video \"NUMBER OF ISLANDS - Leetcode 200 - Python\" (11m41s) — https://www.youtube.com/watch?v=pV2kpPD66nE . Then https://neetcode.io/solutions/number-of-islands (DFS, BFS, and a union-find version); pitfall \"Not Marking Cells as Visited\" is the infinite loop."
  },
  {
   "item": "Clone Graph",
   "label": "NeetCode · Clone Graph - Depth First Search (11m48s)",
   "url": "https://www.youtube.com/watch?v=mQeF6bN8hMk",
   "full": "Video \"Clone Graph - Depth First Search - Leetcode 133\" (11m48s) — https://www.youtube.com/watch?v=mQeF6bN8hMk . Then https://neetcode.io/solutions/clone-graph ; pitfall \"Adding Clone to Map After Processing Neighbors\" is the subtle ordering bug that makes cycles blow the stack."
  },
  {
   "item": "Course Schedule",
   "label": "NeetCode · Course Schedule - Graph Adjacency List (…",
   "url": "https://www.youtube.com/watch?v=EgI5nU9etnU",
   "full": "Video \"Course Schedule - Graph Adjacency List - Leetcode 207\" (15m46s) — https://www.youtube.com/watch?v=EgI5nU9etnU . Then https://neetcode.io/solutions/course-schedule for both forms — approach 1 \"Cycle Detection (DFS)\" and approach 2 \"Topological Sort (Kahn's Algorithm)\" — plus the pitfall \"Using a Single Visited Set Instead of Tracking the Current Path\"."
  },
  {
   "item": "Climbing Stairs",
   "label": "\"Dynamic Programming 1D - Full · Climbing Stairs\" at 0:01:05 (runs to 0:1…",
   "url": "https://neetcode.io/solutions/climbing-stairs",
   "full": "Chapter \"Climbing Stairs\" at 0:01:05 (runs to 0:19:03, where \"Min Cost Climbing Stairs\" begins). Then https://neetcode.io/solutions/climbing-stairs , which ladders the same problem through six approaches from plain recursion to space-optimised DP."
  },
  {
   "item": "House Robber",
   "label": "\"Dynamic Programming 1D - Full · House Robber\" at 0:38:16, followed immed…",
   "url": "https://neetcode.io/solutions/house-robber",
   "full": "Chapter \"House Robber\" at 0:38:16, followed immediately by \"House Robber II\" at 0:48:45 — do both, the circular variant is a common follow-up. Then https://neetcode.io/solutions/house-robber , approach 4 \"Dynamic Programming (Space Optimized)\" for the two-variable rolling version."
  },
  {
   "item": "Coin Change",
   "label": "\"Dynamic Programming 1D - Full · Coin Change\" at 1:37:08",
   "url": "https://neetcode.io/solutions/coin-change",
   "full": "Chapter \"Coin Change\" at 1:37:08. Then https://neetcode.io/solutions/coin-change , approach 3 \"Dynamic Programming (Bottom-Up)\", and read its pitfall \"Using Greedy Instead of DP\" — greedy is the standard wrong first answer and interviewers wait for it."
  }
 ]
}
