# Dataset Guide: Extreme Summarisation (XSum)

## 1. Overview & Source
- **Dataset Name:** Extreme Summarisation (XSum)
- **Hugging Face Repository:** [`EdinburghNLP/xsum`](https://huggingface.co/datasets/EdinburghNLP/xsum)
- **Primary Source:** Narayan, S., Cohen, S. B., & Lapata, M. (2018). *Don't Give Me the Details, Just the Summary! Topic-Aware Summarization of Newswire Articles.* Proceedings of EMNLP.
- **License:** Open Academic / Research (Edinburgh University / BBC)

## 2. Dataset Partitions & Sizes
- **Official Raw Train Split:** 204,045 BBC news articles
- **Official Raw Validation Split:** 11,332 BBC news articles
- **Official Raw Test Split:** 11,334 BBC news articles
- **Sampled Training Subset:** 20,000 articles (`seed=42`)
- **Sampled Validation Subset:** 1,000 articles (`seed=42`)
- **Sampled Test Subset:** 1,000 articles (`seed=42`)

## 3. How to Download and Access in Python
```python
from datasets import load_dataset

# Load official XSum dataset
dataset = load_dataset("EdinburghNLP/xsum")

print(dataset)
# Output:
# DatasetDict({
#     train: Dataset({features: ['document', 'summary', 'id'], num_rows: 204045}),
#     validation: Dataset({features: ['document', 'summary', 'id'], num_rows: 11332}),
#     test: Dataset({features: ['document', 'summary', 'id'], num_rows: 11334})
# })
```

## 4. Key Preprocessing Protocols
1. **Input Prefix:** For T5-Small models, articles are prefixed with `"summarize: "`.
2. **Input Truncation:** Articles are capped at 512 subwords for Transformer models (and 150-400 tokens for recurrent models).
3. **Target Truncation:** Summaries are capped at 40 tokens.
4. **Repetition Prevention:** Inference employs `no_repeat_ngram_size=3` and beam search ($k=4$).
