"""Learn / Practise / Evidence for track t04 (LLM & transformer foundations).

Format: see t03.

Researched Oct 2026. The headline finding is that three of this track's
original primaries were lectures that have not been taught yet - CME 295
Lecture 5 (Flash Attention) is dated 30 Oct 2026 and its page still reads
'Coming soon, stay tuned!', and MIT 6.5940 Lectures 13 and 14 are dated 27 and
29 Oct 2026, so the only recordings on YouTube are the Fall 2024 ones. Those
picks are replaced here with material that exists.

CME 295 is the right primary for breadth and currency (RoPE, GQA, MoE, scaling
laws, the model-family taxonomy) but it is deliberately light on maths, so the
two items that are maths items go to SLP3 and Karpathy instead.
"""

DATA = {
# ---- The core mechanism ---------------------------------------------------
"Self-attention, from scratch on paper": (
 "SLP3 Ch 7 &sect;7.1.1 'Attention more formally' - equations 7.11-7.13 and the sqrt(d_k) argument, pp. 6-8|https://web.stanford.edu/~jurafsky/slp3/7.pdf",
 "Hand-derive one head on 4 tokens, then code it in rasbt ch03. Pass = your output matches ch03.ipynb to 1e-6|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch03",
 "https://web.stanford.edu/~jurafsky/slp3/7.pdf|To avoid this, we scale the dot product by a factor related to the size of the embeddings, via dividing by the square root"),

"Causal masking, and why decoder-only won": (
 "CME 295 Lecture 1 at 1:22:16 for masking; the decoder-only half is Lecture 2 at 16:10, not Lecture 1|https://www.youtube.com/watch?v=114i2Kz-LZA&t=4936",
 "Implement the tril/-inf mask in rasbt ch03 CausalAttention. Pass = deleting the mask raises val loss and visibly leaks future tokens|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch03",
 "https://cme295.stanford.edu/slides/fall26-cme295-lecture1.pdf|Computational trick: masking &middot; 'Masked' also known as 'causal' self-attention"),

"Multi-head attention": (
 "Karpathy &middot; Let's build GPT at 1:21:59 - heads as parallel communication channels, three minutes on what they are for|https://www.youtube.com/watch?v=kCc8FmEb1nY&t=4919",
 "Run rasbt mha-implementations.ipynb. Pass = you can say why d_head = d/A keeps cost flat, and rank the variants by speed|https://github.com/rasbt/LLMs-from-scratch/blob/main/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb",
 "https://cme295.stanford.edu/slides/fall26-cme295-lecture1.pdf|~Multi-head attention &middot; Idea: Run multiple self-attention layers in parallel"),

"Positional encoding: sinusoidal": (
 "CME 295 Lecture 2, 45:36 Position embeddings through 1:01:58 Rotary position embeddings - about 24 minutes|https://www.youtube.com/watch?v=GaIeu3npx04&t=2736",
 "Code RoPE in rasbt ch05/11_qwen3 from a blank file. Pass = the rotated q.k depends only on (i-j), checked numerically|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/11_qwen3",
 "https://www.youtube.com/watch?v=GaIeu3npx04|~Position embeddings 45:36 &middot; Rotary position embeddings (RoPE) 1:01:58"),

"Encoder-only vs decoder-only vs encoder-decoder": (
 "CME 295 Lecture 2: 4:47 encoder-only, 13:47 decoder-only, 16:10 encoder-decoder versus decoder-only|https://www.youtube.com/watch?v=GaIeu3npx04&t=287",
 "Whiteboard all three with their mask patterns and one 2026 production use each, recorded. Pass = under 3 minutes, no notes|https://www.youtube.com/watch?v=GaIeu3npx04&t=970",
 "https://www.youtube.com/watch?v=GaIeu3npx04|~BERT and encoder-only models 4:47 &middot; GPT and decoder-only models 13:47 &middot; Encoder-decoder versus decoder-only 16:10"),

"The seven deltas from the 2017 paper": (
 "CME 295 Lecture 2: 1:09:28 SWA, 1:13:15 GQA, 1:18:13 Pre-Norm vs Post-Norm, 1:19:41 LayerNorm vs RMSNorm|https://www.youtube.com/watch?v=GaIeu3npx04&t=4168",
 "Build Qwen3 from scratch in rasbt ch05/11_qwen3. Pass = loading the official weights reproduces the reference generations|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/11_qwen3",
 "https://cme295.stanford.edu/slides/fall26-cme295-lecture2.pdf|Post-Norm + LayerNorm &middot; Pre-Norm + RMSNorm"),

"Mixture of Experts": (
 "CME 295 Lecture 2: 29:05 Mixture of experts, 33:11 MoE-based LLMs, 36:03 Load balancing loss - do not stop at 29:05|https://www.youtube.com/watch?v=GaIeu3npx04&t=1745",
 "Implement the router plus the auxiliary load-balancing loss in rasbt ch04/07_moe. Pass = expert usage comes out near-uniform|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/07_moe",
 "https://www.youtube.com/watch?v=GaIeu3npx04|~Mixture of experts (MoE) 29:05 &middot; MoE-based LLMs 33:11 &middot; Load balancing loss 36:03"),

"Attention is O(n²)": (
 "Gordic &middot; ELI5 FlashAttention - breaks the title apart: fast, memory-efficient, EXACT, IO-aware. 20 min|https://gordicaleksa.medium.com/eli5-flash-attention-5c44017022ad",
 "Benchmark naive MHA against torch SDPA in rasbt mha-implementations.ipynb. Pass = you explain the gap as HBM traffic, not FLOPs|https://github.com/rasbt/LLMs-from-scratch/blob/main/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb",
 "https://gordicaleksa.medium.com/eli5-flash-attention-5c44017022ad|Exact - meaning it is not an approximation of the attention mechanism (like e.g. sparse, or low-rank matrix approximation methods)"),

# ---- Tokens and context ---------------------------------------------------
"Tokenization: BPE vs WordPiece vs SentencePiece": (
 "HF LLM Course Ch 6: &sect;6.5 Byte-Pair Encoding, &sect;6.6 WordPiece, &sect;6.7 Unigram - all three, each fully implemented|https://huggingface.co/learn/llm-course/chapter6/5",
 "Write BPE from scratch (rasbt ch02/05), then take the HF Ch 6 quiz. Pass = full marks with no re-reading|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch02/05_bpe-from-scratch",
 "https://www.reddit.com/r/learnmachinelearning/comments/1wu3enx/how_id_learn_ml_in_2026_the_resources_id_use_at/|~Interested in NLP and LLMs? Stanford CS224n... Jurafsky and Martin... The Hugging Face LLM Course"),

"What the context window is": (
 "CME 295 Lecture 3 at 23:41 Long context training; pair it with Lecture 2 at 1:38:38 on context rot|https://www.youtube.com/watch?v=S3bCDcJhz4s&t=1421",
 "Extend a RoPE model past its trained length two ways, naive vs scaled theta, and plot perplexity. Pass = naive blows up, scaled does not|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch05/11_qwen3",
 "https://www.youtube.com/watch?v=S3bCDcJhz4s|~Long context training 23:41"),

"The <b>KV cache</b>": (
 "Raschka &middot; Understanding and Coding the KV Cache in LLMs from Scratch - the Advantages and Disadvantages section|https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms",
 "Code the cache in rasbt ch04/03, then size it for Llama 3.1 8B at 128K using SLP3 Fig 7.24. Pass = within 10% of measured|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache",
 "https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms|the cumulative work scales quadratically, O(n squared). With a cache, each key and value is computed once and then reused"),

"Sampling: temperature, top-k, top-p": (
 "SLP3 Ch 7 &sect;7.6.3 Temperature sampling and &sect;7.6.4 Top-k and top-p sampling, with Figures 7.20 and 7.21|https://web.stanford.edu/~jurafsky/slp3/7.pdf",
 "Reproduce SLP3 Fig 7.21 from one logit vector across five temperatures. Pass = you can say which of the three can emit a zero-probability token|https://web.stanford.edu/~jurafsky/slp3/7.pdf",
 "https://web.stanford.edu/~jurafsky/slp3/7.pdf|it is common to combine both top-k and top-p sampling, using top-k first as a kind of a hard filter to eliminate garbage"),

"Why hallucinations happen": (
 "Lilian Weng &middot; Extrinsic Hallucinations in LLMs - the in-context vs extrinsic split, then What Causes Hallucinations|https://lilianweng.github.io/posts/2024-07-07-hallucination/",
 "Build a 50-question closed-book eval with an abstain option. Pass = accuracy-only scoring ranks the guessing config ABOVE the honest one|https://openai.com/index/why-language-models-hallucinate/",
 "https://lilianweng.github.io/posts/2024-07-07-hallucination/|There are two types of hallucination: In-context hallucination... Extrinsic hallucination"),

# ---- Training, at decision depth ------------------------------------------
"The lifecycle: pretraining": (
 "CME 295 Lecture 3 (Oct 2026): 3:36 Pretraining, 31:47 SFT, 46:37 Preference tuning, 1:01:49 RLHF, 1:05:38 DPO|https://www.youtube.com/watch?v=S3bCDcJhz4s&t=1907",
 "Implement DPO in rasbt ch07/04 from the Bradley-Terry loss. Pass = the implicit reward margin separates chosen from rejected|https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb",
 "https://web.stanford.edu/~jurafsky/slp3/8.pdf|DPO does not require training an explicit reward model... DPO only incurs the cost of maintaining 2 LLMs during training"),

"LoRA: <code>ΔW = BA</code>": (
 "Raschka &middot; Practical Tips for Finetuning LLMs Using LoRA - the takeaways, plus Q3 on rank and Q4 on which layers|https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms",
 "Run a LoRA finetune via HF Ch 11 &sect;4, then merge and hot-swap two adapters. Pass = merged inference matches adapter inference|https://huggingface.co/learn/llm-course/chapter11/4",
 "https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms|ensure it is applied across all layers, not just to the Key and Value matrices... A good heuristic is setting alpha at twice the rank's value"),

"QLoRA and PEFT": (
 "Dettmers et al. &middot; QLoRA - the three mechanisms: 4-bit NormalFloat, double quantization, paged optimizers|https://arxiv.org/abs/2305.14314",
 "Run the rasbt appendix-E LoRA finetune, then redo it in 4-bit. Pass = you can state the memory saved and the runtime cost paid|https://github.com/rasbt/LLMs-from-scratch/blob/main/appendix-E/01_main-chapter-code/appendix-E.ipynb",
 "https://arxiv.org/abs/2305.14314|4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights"),

"Quantization: int8, int4, GPTQ/AWQ": (
 "MIT 6.5940 Lecture 13 (Fall 2024): 0:00 SmoothQuant, 16:11 AWQ and TinyChat - Song Han on his own methods|https://www.youtube.com/watch?v=sTz2tXG1T0c",
 "Quantize one model to int8 and to int4-AWQ, measuring perplexity and tokens/sec on all three. Pass = you explain why only some channels matter|https://www.youtube.com/watch?v=sTz2tXG1T0c&t=971",
 "https://www.youtube.com/watch?v=sTz2tXG1T0c|~SmoothQuant and quantization 0:00 &middot; AWQ and TinyChat deployment 16:11"),

"Catastrophic forgetting": (
 "Biderman et al. &middot; LoRA Learns Less and Forgets Less (TMLR 2024) - the abstract plus the best-practices section|https://arxiv.org/abs/2405.09673",
 "Finetune on one domain twice, full vs LoRA, and eval both out-of-domain. Pass = LoRA degrades measurably less|https://github.com/rasbt/LLMs-from-scratch/blob/main/appendix-E/01_main-chapter-code/appendix-E.ipynb",
 "https://arxiv.org/abs/2405.09673|LoRA better maintains the base model's performance on tasks outside the target domain... LoRA mitigates forgetting"),

"Scaling laws and the compute-vs-data tradeoff": (
 "CME 295 Lecture 2 at 19:23 Scaling laws - Kaplan et al. 2020, then the Chinchilla law. About 7 minutes|https://www.youtube.com/watch?v=GaIeu3npx04&t=1163",
 "From a fixed FLOP budget, derive the Chinchilla-optimal params/tokens split out loud. Pass = you land near 20 tokens per parameter unprompted|https://cme295.stanford.edu/slides/fall26-cme295-lecture2.pdf",
 "https://cme295.stanford.edu/slides/fall26-cme295-lecture2.pdf|Scaling Laws for Neural Language Models, Kaplan et al., 2020... Chinchilla law."),

# ---- Build these once -----------------------------------------------------
"Karpathy, <b>micrograd</b>": (
 "Karpathy &middot; The spelled-out intro to neural networks and backpropagation: building micrograd. 2h25m, watch it whole|https://youtu.be/VMj-3S1tku0",
 "Rewrite engine.py and nn.py from a blank file. Pass = test/test_engine.py agrees with PyTorch autograd to 1e-6. Do not self-grade|https://github.com/karpathy/micrograd/blob/master/test/test_engine.py",
 "https://www.reddit.com/r/learnmachinelearning/comments/1wu3enx/how_id_learn_ml_in_2026_the_resources_id_use_at/|Andrej Karpathy's Neural Networks: Zero to Hero. Fantastic if you learn by building. You build backprop from scratch"),

"Karpathy, <b>“Let's build GPT”</b>": (
 "Karpathy &middot; Let's build GPT, 1:02:00 'the crux of the video: self-attention' through 1:24:25 feedforward|https://www.youtube.com/watch?v=kCc8FmEb1nY&t=3720",
 "Train nanoGPT on Shakespeare end to end from your own file. Pass = val loss under 1.5 and coherent character-level output|https://github.com/karpathy/nanoGPT",
 "https://www.youtube.com/watch?v=kCc8FmEb1nY|~THE CRUX OF THE VIDEO: version 4: self-attention 1:02:00 &middot; multi-headed self-attention 1:21:59"),

"A 30-line MLP training loop": (
 "Karpathy &middot; makemore Part 2 at 37:56 'implementing the training loop, overfitting one batch' into 41:25 minibatches|https://www.youtube.com/watch?v=TCH_1BHY58I&t=2276",
 "Write it blind twice via Raschka's PyTorch in One Hour, then break it deliberately. Pass = you explain the failure when zero_grad() is removed|https://sebastianraschka.com/teaching/pytorch-1h/",
 "https://www.reddit.com/r/learnmachinelearning/comments/1wu3enx/how_id_learn_ml_in_2026_the_resources_id_use_at/|AI-written ML code can run and still be wrong... zero_grad() can be missing. If you understand the system, you can catch those mistakes"),

"Causal multi-head attention on a whiteboard": (
 "Karpathy &middot; Let's build GPT at 1:16:56, note 6 on why divide by sqrt(head_size), then 1:21:59 multi-head|https://www.youtube.com/watch?v=kCc8FmEb1nY&t=4616",
 "Record yourself drawing B,T,C through Q/K/V, mask, softmax, concat, W_O. Pass = under 4 min, no notes, every shape right. Grade the shapes|https://github.com/rasbt/LLMs-from-scratch/blob/main/ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb",
 "https://www.youtube.com/watch?v=kCc8FmEb1nY|~note 6: 'scaled' self-attention. why divide by sqrt(head_size) 1:16:56"),

"rasbt/LLMs-from-scratch": (
 "Raschka &middot; Build a LLM (From Scratch): Appendix A Intro to PyTorch FIRST, then Ch 2, then Ch 3|https://github.com/rasbt/LLMs-from-scratch/blob/main/appendix-A/01_main-chapter-code/code-part1.ipynb",
 "Type all three, then rebuild Ch 3 CausalAttention from blank. Pass = the repo's own tests and exercise-solutions agree with you|https://github.com/rasbt/LLMs-from-scratch/tree/main/ch03",
 "https://www.reddit.com/r/LLMDevs/comments/1wlh7j7/best_book_to_get_started_with_building_and/|Raschka's Build a Large Language Model (From Scratch) does what the title says. You type out a working GPT yourself"),
}
