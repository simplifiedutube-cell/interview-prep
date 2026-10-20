"""Learn / Practise / Evidence for track t05 (RAG & retrieval). Format: see t03.

Researched Oct 2026 with Reddit reachable through the user's own browser, so
most evidence here is a practitioner thread rather than a vendor page. Where a
vendor is the only source of a number (Anthropic on contextual retrieval,
Chroma on chunking) the NOTE in the research log says so; prefer the neutral
measurement when one exists.

Two of the track's own links were dead and are replaced here: LangChain's
how_to/indexing now redirects to a marketing overview, and the RAG playbook's
GitHub Pages site 404s, so the playbook is read from the repo.
"""

DATA = {
"Explain RAG end to end": (
 "RAG Playbook Ch 0 &middot; The Product Mindset for RAG - read it with the three-pipelines split in mind|https://raw.githubusercontent.com/jxnl/systematically-improving-rag/main/docs/book/chapter0.md",
 "Record 90s naming the offline and online paths and 3 rejected alternatives. Pass = a per-stage p95 ms and $/query table you can quote|https://www.reddit.com/r/Rag/comments/1pahsix/rag_isnt_one_system_its_three_pipelines/",
 "https://www.reddit.com/r/Rag/comments/1pahsix/rag_isnt_one_system_its_three_pipelines/|A lot of RAG confusion comes from treating ingestion, retrieval, and generation as one linear system"),

"Chunking: what drives the size": (
 "Chroma &middot; Evaluating Chunking Strategies for Retrieval - go to the Results table (recall, precision, IoU)|https://research.trychroma.com/evaluating-chunking",
 "Run chunking_evaluation on your own corpus across 3 sizes. Pass = recall and token-level IoU per strategy, and you name a winner|https://github.com/brandonstarxel/chunking_evaluation",
 "https://research.trychroma.com/evaluating-chunking|the choice of chunking strategy can have a significant impact on retrieval performance, with some strategies outperforming others by up to 9% in recall"),

"Embedding models: how to choose": (
 "Chroma &middot; Generative Benchmarking - the golden-dataset method, then its MTEB-vs-real-queries comparison|https://research.trychroma.com/generative-benchmarking",
 "Generate a golden set from your own docs and score 3 models. Pass = a recall@10 and nDCG@10 table with the best-to-worst spread|https://research.trychroma.com/generative-benchmarking",
 "https://research.trychroma.com/generative-benchmarking|our generated queries yield model performance metrics that closely align with those of the real queries and capture performance differences that MTEB fails to reflect"),

"Vector index internals": (
 "pgvector README &sect; HNSW (m, ef_construction, hnsw.ef_search) and &sect; IVFFlat (lists, ivfflat.probes)|https://github.com/pgvector/pgvector",
 "Sweep hnsw.ef_search from 10 to 400 on your index. Pass = a recall@10-vs-p95-latency curve and the knee value you would ship|https://github.com/pgvector/pgvector",
 "https://github.com/pgvector/pgvector|Specify the size of the dynamic candidate list for search (40 by default) ... A higher value provides better recall at the cost of speed."),

"Vector DB vs Postgres": (
 "Encore, Mar 2026 &middot; You probably do not need a vector database - the what-vectors-do and when-Postgres-is-enough sections|https://encore.dev/blog/you-probably-dont-need-a-vector-database",
 "Answer the same 20 queries three ways: pgvector HNSW, Postgres tsvector FTS, a dedicated DB. Pass = nDCG@10, p95 and monthly cost for each|https://encore.dev/blog/you-probably-dont-need-a-vector-database",
 "https://www.reddit.com/r/vectordatabase/comments/1rp3k9e/you_probably_dont_need_a_vector_database/|~that is a lot of infrastructure for what amounts to a nearest-neighbor query"),

"Hybrid retrieval</b>: dense + BM25": (
 "RAG Playbook Ch 8 &middot; Hybrid Search - why rank fusion beats score blending across incomparable scales|https://raw.githubusercontent.com/jxnl/systematically-improving-rag/main/docs/book/chapter8.md",
 "Build dense + BM25 + RRF with Qdrant Prefetch. Pass = nDCG@10 for each of the three on 50 queries, plus one SKU query only BM25 finds|https://qdrant.tech/documentation/tutorials-search-engineering/reranking-hybrid-search/",
 "https://www.reddit.com/r/Rag/comments/1pd7tao/i_rewrote_hybrid_search_four_times_heres_what/|I ended up going with Reciprocal Rank Fusion instead of normalizing raw scores ... With k=60 it has been rock solid in production"),

"Cross-encoder reranking": (
 "Sentence-Transformers &middot; Retrieve and Re-Rank - the Cross-Encoder section, where query and passage are scored jointly|https://www.sbert.net/examples/applications/retrieve_rerank/README.html",
 "Add a 50-in / 15-out reranker. Pass = the nDCG@10 delta AND the added p95 ms, both measured, so you can say what it bought and what it cost|https://www.sbert.net/examples/applications/retrieve_rerank/README.html",
 "https://www.reddit.com/r/Rag/comments/1oblymp/production_rag_what_we_learned_from_processing_5m/|Reranking: the highest value 5 lines of code you will add ... We found the ideal reranker set-up to be 50 chunk input to 15 output"),

"Lost in the Middle</b>": (
 "Liu et al, Lost in the Middle (TACL) - the multi-document QA section and its U-shaped accuracy-by-position curves|https://arxiv.org/abs/2307.03172",
 "Place the gold chunk at position 1, 5 and 10 of 10 for 50 questions. Pass = your own accuracy-by-position curve and the size of the sag|https://research.trychroma.com/context-rot",
 "https://arxiv.org/abs/2307.03172|performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades"),

"Contextual retrieval — prepending": (
 "Anthropic Engineering &middot; Contextual Retrieval - Performance improvements, then Implementation considerations|https://www.anthropic.com/engineering/contextual-retrieval",
 "Contextualise your own chunks and measure 1 minus recall@20 before and after. Pass = a named failure-rate drop plus $ per million chunks|https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb",
 "https://www.anthropic.com/engineering/contextual-retrieval|Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35% (5.7% to 3.7%)"),

"Citations and source attribution": (
 "Jason Liu &middot; There Are Only 6 RAG Evals - the Q, C, A conditional relationships, especially A given C (faithfulness)|https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/",
 "Add ~12% unanswerable and ~10% false-premise questions to your gold set. Pass = zero bluffs on the unanswerable ones, every claim carrying a chunk id|https://www.reddit.com/r/Rag/comments/1wfzp1a/fully_offline_rag_over_27_technical_books_11k/",
 "https://www.reddit.com/r/Rag/comments/1wfzp1a/fully_offline_rag_over_27_technical_books_11k/|Unanswerable questions in the gold set. Without them you never find out your answerer bluffs."),

"Index freshness": (
 "langchain_core.indexing reference - RecordManager, and the incremental / full / scoped_full cleanup modes|https://reference.langchain.com/python/langchain_core/indexing/",
 "Edit 100 source docs and re-run incremental indexing. Pass = zero duplicate chunks for the changed sources and a measured stale-answer window|https://reference.langchain.com/python/langchain_core/indexing/",
 "https://www.reddit.com/r/Rag/comments/1rqw1oo/i_had_to_reembed_5_million_documents_because_i/|~fine tuning embedding models should be the last thing you do"),

"Multi-tenant isolation": (
 "Qdrant &middot; Configure Multitenancy - partition by payload filter, the tenant payload index, why collection-per-tenant does not scale|https://qdrant.tech/documentation/guides/multiple-partitions/",
 "Run 200 tenant-B queries including injection attempts. Pass = zero tenant-A chunks, and recall@10 reported per permission cohort|https://www.reddit.com/r/Rag/comments/1w3q78p/our_rag_permissions_filter_is_safe_and_still/",
 "https://qdrant.tech/documentation/guides/multiple-partitions/|Each tenant's data must stay isolated: when a tenant searches, they should only see their own data."),

"The canonical debugging question": (
 "RAG Playbook Appendix D &middot; Debugging RAG Systems - the five-step process and the failure taxonomy|https://github.com/jxnl/systematically-improving-rag/blob/main/docs/book/appendix-debugging.md",
 "Seed 10 known failures (gold chunk deleted, ranked 30th, present but ignored). Pass = classify 10 of 10 from logs alone before fixing anything|https://github.com/jxnl/systematically-improving-rag/blob/main/docs/book/appendix-debugging.md",
 "https://github.com/jxnl/systematically-improving-rag/blob/main/docs/book/appendix-debugging.md|There are no stack traces when the model produces a wrong answer, no exceptions when retrieval returns irrelevant documents"),

"Scaling to 10M+ documents": (
 "turbopuffer &middot; fast search on object storage - take the cost-per-GB walk from in-memory to SSD to object storage|https://turbopuffer.com/blog/turbopuffer",
 "Freeze one gold set and run it against a 3.6k-chunk and a 32k-chunk index. Pass = quote the recall@8 and MRR delta at 9x distractors|https://www.reddit.com/r/Rag/comments/1wfzp1a/fully_offline_rag_over_27_technical_books_11k/",
 "https://www.reddit.com/r/Rag/comments/1wfzp1a/fully_offline_rag_over_27_technical_books_11k/|So vs. the 3.6k-chunk run: -1.9 pp recall, -0.026 MRR with 9x more distractors. Less than I expected."),

"Retrieval is too slow": (
 "Qdrant &middot; Optimize Performance - Balancing Latency and Throughput, and the four named profiles|https://qdrant.tech/documentation/ops-optimization/optimize/",
 "Instrument every stage: embed, ANN, filter, rerank, generate. Pass = cut p95 by 30% while losing at most 1 point of recall@10, both reported|https://www.reddit.com/r/Rag/comments/1p59v9t/we_cut_rag_latency_2_by_switching_embedding_model/",
 "https://qdrant.tech/documentation/ops-optimization/optimize/|Low Memory + High Speed: Use vector quantization. High Precision + Low Memory: Store vectors and HNSW index in the cold memory tier."),

"Semantic caching": (
 "RedisVL user guide &middot; Cache LLM Responses - the distance_threshold section and how to tune it|https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html",
 "Build 100 near-miss pairs that must NOT share an answer (negations, swapped dates, swapped ids) and sweep the threshold. Pass = hit rate at under 1% false hits|https://docs.redisvl.com/en/latest/user_guide/03_llmcache.html",
 "https://redis.io/blog/what-is-semantic-caching/|~When similarity exceeds a threshold (commonly 0.85-0.95), the system returns the cached response instead of calling the LLM"),

"Fine-tune vs RAG vs prompt engineering": (
 "RAG Playbook Ch 2 &middot; Training Data and Fine-Tuning - what it is for, and when a retriever or reranker is the cheaper lever|https://raw.githubusercontent.com/jxnl/systematically-improving-rag/main/docs/book/chapter2.md",
 "Fine-tune a reranker or embedding model on ~200 labelled pairs from your own traffic. Pass = recall@10 lift over the RAG-only baseline, or a measured null result|https://github.com/jxnl/systematically-improving-rag/tree/main/latest/week2",
 "https://www.reddit.com/r/Rag/comments/1rqw1oo/i_had_to_reembed_5_million_documents_because_i/|fine tuning embedding models should be the last thing you do. There are way better ways to improve retrieval"),

"Long context vs RAG</b>": (
 "Husain and Clavie &middot; Stop Saying RAG Is Dead (Jul 2025) - coverage and diversity over top-1, late interaction, multiple representations|https://hamel.dev/notes/llm/rag/not_dead.html",
 "Same 50 questions, three configs: top-5 RAG, top-50 plus rerank, whole-corpus long context. Pass = a table of accuracy, input tokens and $ per query|https://research.trychroma.com/context-rot",
 "https://hamel.dev/notes/llm/rag/not_dead.html|LLMs are frozen at training time. Million-token context windows do not change the economics of stuffing everything into every query."),

"NirDiamant/RAG_Techniques": (
 "all_rag_techniques, in order: simple_rag, choose_chunk_size, fusion_retrieval, reranking, HyDe, contextual_chunk_headers, raptor, self_rag, crag, graph_rag|https://github.com/NirDiamant/RAG_Techniques/tree/main/all_rag_techniques",
 "Point six notebooks at ONE shared corpus and one gold set. Pass = a ranked recall@10 table saying which techniques paid and which did not|https://github.com/NirDiamant/RAG_Techniques/tree/main/all_rag_techniques",
 "https://www.reddit.com/r/Rag/comments/1sfwq0v/i_maintain_the_rag_techniques_repo_27k_stars_i/|~I have spent the last 18 months maintaining the RAG Techniques repository on GitHub"),

"Jason Liu — Systematically Improving RAG": (
 "The playbook, now open-sourced &middot; Ch 1 Evaluation-First Development - synthetic eval data to break the cold start|https://raw.githubusercontent.com/jxnl/systematically-improving-rag/main/docs/book/chapter1.md",
 "Run week1 notebooks 01_synthetic_questions then 02_benchmark_retrieval on your corpus. Pass = recall@k and MRR on 50 synthetic questions|https://github.com/jxnl/systematically-improving-rag/tree/main/latest/week1",
 "https://jxnl.co/writing/2026/02/02/sunsetting-567-labs/|The courses close today, February 2, 2026. I am open sourcing the written content"),

"The original RAG paper": (
 "Lewis et al, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks - &sect;2 Methods and Figure 1 only|https://arxiv.org/abs/2005.11401",
 "Write the 10-line diff between RAG-Sequence/RAG-Token with a jointly trained DPR retriever and what you would actually ship in 2026, naming what replaced each piece",
 "https://arxiv.org/abs/2005.11401|~models which combine pre-trained parametric and non-parametric memory for language generation"),

"Anthropic — Contextual Retrieval": (
 "claude-cookbooks capabilities/contextual-embeddings/guide.ipynb - the situating prompt and the recall@20 evaluation cells|https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb",
 "Run the notebook on your own documents, then ablate: plain, contextual embeddings, plus contextual BM25, plus rerank. Pass = four 1-minus-recall@20 numbers|https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb",
 "https://www.anthropic.com/engineering/contextual-retrieval|Passing the top-20 chunks to the model is more effective than just the top-10 or top-5 ... All these benefits stack"),
}
