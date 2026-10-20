"""Learn / Practise / Evidence data for track t03 (Python for AI engineering).

This module also documents the field format used by every other table in this
package.

Keyed by a distinctive substring of the item text, because idFor() hashes the
group title and the item text — so slots 0-2 of every item must stay byte
identical. Only slots 3 (learn), 4 (practise) and 5 (evidence) are written.

Field format:
  learn, practise  "Label|https://url"   (url optional; label-only renders plain)
  evidence         "https://url|verbatim quote"   prefix the quote with ~ for weak

Every URL here was opened by a research agent. Evidence is Hacker News, a
published review, a merged PR or a primary source: reddit.com is unreachable
from this environment, both at the fetch layer and through the Chrome extension.
"""

DATA = {
# ---- Tier 1 ---------------------------------------------------------------
"Progressive multi-level class design": (
 "CodeSignal's own technical brief, pp. 1-5 - the four level definitions plus the worked sample task|https://discover.codesignal.com/rs/659-AFH-023/images/Industry-Coding-Skills-Evaluation-Framework-CodeSignal-Skills-Evaluation-Lab-Short.pdf",
 "PaulLockett/CodeSignal_Practice_Industry_Coding_Framework - file_storage, four levels, one 90-min clock|https://github.com/PaulLockett/CodeSignal_Practice_Industry_Coding_Framework",
 "https://news.ycombinator.com/item?id=42917519|~the CodeSignal screen is intended to test your ability to quickly and correctly write and refactor working code"),

"asyncio.Semaphore": (
 "Fowler, Python Concurrency with asyncio &middot; Ch 11 &sect;11.3 'Limiting concurrency with semaphores'|https://livebook.manning.com/book/python-concurrency-with-asyncio/chapter-11",
 "Write the bounded batch client blind, then diff against openai-cookbook's api_request_parallel_processor.py|https://github.com/openai/openai-cookbook/blob/main/examples/api_request_parallel_processor.py",
 "https://death.andgravity.com/limit-concurrency|~No, it's not Semaphore, despite what Stack Overflow may tell you."),

"Retry with exponential backoff": (
 "Amazon Builders' Library &middot; Timeouts, retries and backoff with jitter - incl. the token-bucket retry limit|https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter",
 "Write @retry from blank - sync and async, full jitter, a cap, an exception predicate - then diff the API against tenacity|https://tenacity.readthedocs.io/en/latest/",
 "https://news.ycombinator.com/item?id=44145960|Full agreement from me that jitter is essential. Here's AWS on good retry policies"),

"The GIL, and asyncio vs threading": (
 "Beazley, 'Understanding the Python GIL' (PyCon 2010) for the mechanism; the free-threading HOWTO for the 2026 answer|https://www.youtube.com/watch?v=Obt-vMVdM8s",
 "fluentpython/example-code-2e &middot; 19-concurrency, 20-executors, 21-async - one workload three ways, measured|https://github.com/fluentpython/example-code-2e",
 "https://news.ycombinator.com/item?id=32419870|David Beazley does a much better illustrating the nuances than I ever could"),

"Mutability, lists vs tuples": (
 "Fluent Python 2e &middot; Ch 6 'Object References, Mutability, and Recycling'|https://github.com/fluentpython/example-code-2e",
 "Turn on ruff B006, B008 and RUF012 across your own code; for every hit write the failing test first|https://docs.astral.sh/ruff/rules/mutable-argument-default/",
 "https://news.ycombinator.com/item?id=49061460|Probably the most common is the mutable default argument gotcha."),

"OOP fundamentals": (
 "Brandon Rhodes, 'Composition Over Inheritance' - four solutions, and the four dodges he rejects|https://python-patterns.guide/gang-of-four/composition-over-inheritance/",
 "dabeaz-course/python-mastery &middot; sections 3 and 4 (ex3_1-ex3_8, ex4_1-ex4_4), solutions included|https://github.com/dabeaz-course/python-mastery",
 "https://news.ycombinator.com/item?id=31875878|The author very clearly enumerates the trade-offs of choosing the if-statement solution"),

"REST semantics": (
 "RFC 9110 &sect;9.3.4 and &sect;15 for PUT and status codes - then RFC 5789 &sect;2, because 9110 never defines PATCH|https://www.rfc-editor.org/rfc/rfc9110.html",
 "FastAPI 'Dependencies with yield' - build PUT and PATCH with ETag/If-Match, 412, 415, and a yield-scoped session|https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/",
 "https://news.ycombinator.com/item?id=46096823|~RFC 9110 clearly and unambiguously states that only the GET, HEAD, OPTIONS, and TRACE methods are defined to be safe."),

"Generators and lazy evaluation": (
 "Beazley, 'Generator Tricks for Systems Programmers' v3.0 - parts 2-5, the gen_find/gen_open/gen_cat pipeline|https://simonwillison.net/2019/Apr/9/generator-tricks-for-systems-programmers/",
 "dabeaz-course/python-mastery &middot; section 8, ex8_1-ex8_6, plus a tracemalloc assertion that peak memory stays flat|https://github.com/dabeaz-course/python-mastery/blob/main/Exercises/index.md",
 "https://news.ycombinator.com/item?id=5291475|For the first time I've totally and fully groked why generators are good at a practical rather than just theoretical level."),

# ---- Tier 2 ---------------------------------------------------------------
"Pydantic v2 and typing": (
 "Pydantic docs &middot; Concepts, in this order: Models &rarr; Fields &rarr; Validators &rarr; Strict mode &rarr; Serialization|https://pydantic.dev/docs/validation/latest/concepts/models/",
 "Blind: a Literal-discriminated union of three tool-call shapes, a before- and an after-validator, one TypeAdapter. Then the part the docs skip - feed the ValidationError back to the model and retry, the way Instructor does|https://pydantic.dev/docs/validation/latest/concepts/validators/",
 "https://pithycyborg.substack.com/p/the-llm-retry-loop-that-looks-like|~Instructor's built-in retry with repair is designed for this, sending the validation error back to the model"),

"Context managers": (
 "contextlib docs - the only page carrying sync, async and ExitStack together|https://docs.python.org/3/library/contextlib.html",
 "Python Morsels, context-manager tag: suppress, Timer, Timer redux, cd, reloopable|https://www.pythonmorsels.com/exercises/",
 "https://news.ycombinator.com/item?id=25041793|the documentation for contextlib describes its need and use very well"),

"pytest — fixtures": (
 "Okken, Python Testing with pytest 2e &middot; Ch 3, 5, 10, 16 - then LangChain's unit-testing page for the fake-model half|https://docs.langchain.com/oss/python/langchain/test/unit-testing",
 "Test your SSE drill against GenericFakeChatModel, which really chunks. Then do it again with respx at the HTTP layer and argue which you'd defend|https://raw.githubusercontent.com/langchain-ai/langchain/master/libs/core/langchain_core/language_models/fake_chat_models.py",
 "https://github.com/langchain-ai/docs/pull/3398|Emphasizes deterministic testing by controlling model outputs instead of relying on live LLMs"),

"Dunder methods beyond": (
 "Fluent Python 2e &middot; Ch 1 'The Python Data Model' &rarr; Ch 11 'A Pythonic Object' &rarr; Ch 16 'Operator Overloading'|https://github.com/fluentpython/example-code-2e",
 "Python Morsels, dunder tag: Vector, OrderedSet, Month, MonthDelta, RomanNumeral, float_range|https://www.pythonmorsels.com/exercises/",
 "https://news.ycombinator.com/item?id=39916949|as it explains the Python Data Model in depth"),

"Pythonic idioms": (
 "Slatkin, Effective Python 3e - 2024, 125 items, current to 3.13 &middot; Items 1-30 plus the comprehensions and functions chapters|https://www.informit.com/store/effective-python-125-specific-ways-to-write-better-9780138172183",
 "Exercism's Python track, mentored, for idiom feedback - plus 15 Morsels exercises passed before watching the screencast|https://exercism.org/tracks/python/exercises",
 "https://news.ycombinator.com/item?id=34569660|Effective Python This teaches 90 specific ways to be more Pythonic"),

# ---- Tier 3 ---------------------------------------------------------------
"Metaclasses": (
 "Willison's TIL, quoting Beazley: 95% of what once needed a metaclass is now __init_subclass__. One screen, and that is the whole item|https://til.simonwillison.net/python/init-subclass",
 "A plugin registry twice from blank - metaclass __new__, then __init_subclass__ - then say in 60 seconds when you'd still pick the metaclass|https://docs.python.org/3/reference/datamodel.html",
 "https://news.ycombinator.com/item?id=29816906|This is my most common use of metaclasses, and __init_subclass__ looks to be a much cleaner solution."),

"Memory model": (
 "Ned Batchelder, 'Facts and myths about Python names and values'|https://nedbatchelder.com/text/names.html",
 "Predict the output of 10 snippets before running them: a = b = [], [[0]*3]*3, a += [1] vs a = a + [1], is on 256 vs 257, a cycle needing gc.collect(). Pass = 10/10 first try",
 "https://news.ycombinator.com/item?id=16896411|Here is, what I thought, is an excellent video and the related article for Python"),

# ---- Timed drills ---------------------------------------------------------
"Async batch client": (
 "openai-python &middot; _calculate_retry_timeout, _base_client.py L875-896 - real jitter is 1 - 0.25*random()|https://raw.githubusercontent.com/openai/openai-python/main/src/openai/_base_client.py",
 "Nothing grades this. 12 min, self-graded: 100 x 100ms finish in ~0.6s not ~10s, in-flight never exceeds 20, and forced failures on #7 and #42 still return 100 entries",
 "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/|it should be considered a standard approach for remote clients"),

"SSE streaming handler": (
 "anthropic-sdk-python &middot; accumulate_event, the input_json_delta branch - partial JSON buffered per content-block index|https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/src/anthropic/lib/streaming/_messages.py",
 "15 min, self-graded: feed the same bytes whole, one byte at a time, and split mid-data: and mid-UTF-8 - all three must yield identical snapshots",
 "https://news.ycombinator.com/item?id=42515621|The double newline block separator also shows up in a bunch of our text, making parsing a nightmare."),

"Token-bucket rate limiter": (
 "openai-cookbook &middot; api_request_parallel_processor.py - two buckets, fractional refill, tokens spent per request not per call|https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/api_request_parallel_processor.py",
 "Deep-ML 1098 grades the refill half; add release(est, actual) reconciliation yourself, and guard est &gt; tpm or it blocks forever - 45 min|https://www.deep-ml.com/problems/1098",
 "https://reference.langchain.com/python/langchain-core/rate_limiters/InMemoryRateLimiter|These tokens have nothing to do with LLM tokens."),

"Tool-dispatch loop": (
 "anthropic-sdk-python &middot; _beta_runner.py - the _steps() loop and _determine_next_step_from_stop_reason|https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/src/anthropic/lib/tools/_beta_runner.py",
 "50 min against a scripted fake client, no API key: sequential, parallel, a handler that fails then succeeds, a nonexistent tool, and an infinite caller stopping at max_steps",
 "https://news.ycombinator.com/item?id=46019052|Agent runs in a loop (max of n times)."),

"Cosine similarity and top-k": (
 "LangChain &middot; cosine_similarity_top_k, utils/math.py L13-74 - zero-norm masking, then argpartition &rarr; argsort &rarr; unravel_index|https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/utils/math.py",
 "Deep-ML 1072 'Pairwise Cosine Similarity Matrix' - graded, and it demands the zero-norm rule. 15 min|https://www.deep-ml.com/problems/1072",
 "https://github.com/langchain-ai/langchain/pull/8151|np.argpartition is utilized to find the top_k largest scores indices, this operation has a time complexity of O(n)"),

"BM25 and Reciprocal Rank Fusion": (
 "Cormack et al., the RRF paper (SIGIR '09) - k=60 was 'fixed during a pilot investigation'; BM25 in IR-book &sect;11.3.4|http://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf",
 "Deep-ML 90 grades BM25 - but with its own IDF, not Robertson's. Nothing grades RRF: check ranks 1 and 2 give 1/61 + 1/62 = 0.03252. 35 min|https://www.deep-ml.com/problems/90",
 "https://www.elastic.co/search-labs/blog/improving-information-retrieval-elastic-stack-hybrid|The paper that introduces Reciprocal Rank Fusion suggests a value of 60 for k"),

"LRU cache in O(1)": (
 "CPython &middot; _lru_cache_wrapper, Lib/functools.py L551 - the circular doubly-linked list, PREV/NEXT/KEY/RESULT|https://github.com/python/cpython/blob/3.13/Lib/functools.py",
 "Both passes are graded: Deep-ML 1099 (decorator, kwargs order-independent) then 1095 (persistent). 20 min each, and no OrderedDict|https://www.deep-ml.com/problems/1099",
 "https://news.ycombinator.com/item?id=44971374|implement a Python LRU cache that handles args and kwargs, with a follow-up on making it persistent"),

"In-memory KV store with TTL": (
 "CodeSignal's framework datasheet for the level structure - then SQLite SAVEPOINT for what nesting actually means|https://www.sqlite.org/lang_savepoint.html",
 "PaulLockett's file_storage, four levels, one 90-min clock. Then Deep-ML 1093 for the KV-shaped version with TICK/SCAN/BACKUP|https://github.com/PaulLockett/CodeSignal_Practice_Industry_Coding_Framework",
 "https://news.ycombinator.com/item?id=42917519|90 minutes to implement a series of increasingly difficult specs and pass all the unit tests"),

"Refactor 100": (
 "Emily Bache, 'Fun Refactoring! - Gilded Rose, hands-on with approval testing'|https://youtu.be/OdnV8hc9L7I",
 "emilybache/GildedRose-Refactoring-Kata, python/. Generate the approval baseline BEFORE reading the code - that is the point. 50 min|https://github.com/emilybache/GildedRose-Refactoring-Kata",
 "https://www.eficode.com/blog/advanced-testing-refactoring-techniques|One of the exercises I've used for years to help programmers improve their skills is the Gilded Rose Kata."),

"Logistic regression with SGD": (
 "Raschka, Machine Learning with PyTorch and Scikit-Learn &middot; AdalineSGD (ch02.py L459) and LogisticRegressionGD (ch03.py L296)|https://github.com/rasbt/machine-learning-book/blob/main/ch02/ch02.py",
 "Three graded Deep-ML problems together, because no single one covers it: 106 logistic SGD, 198 L2 as weight decay, 913 early stopping. 40 min|https://www.deep-ml.com/problems/106",
 "https://news.ycombinator.com/item?id=24462716|write a stochastic gradient descent logistic regression model with training, inference, etc. without any libraries beyond pandas/numpy"),
}
