# Dataset Guide: OPUS-100 English-Urdu (en-ur)

## 1. Overview & Source
- **Dataset Name:** OPUS-100 Multilingual Corpus (English–Urdu)
- **Hugging Face Repository:** [`Helsinki-NLP/opus-100`](https://huggingface.co/datasets/Helsinki-NLP/opus-100) (config: `en-ur`)
- **Primary Source:** Tiedemann, J. (2012). *Parallel Data, Tools and Interfaces in OPUS.* Language Resources and Evaluation (LREC).
- **License:** Open Academic / Research (CC-BY-4.0)

## 2. Dataset Partition & Sizes
- **Raw Training Split:** 753,913 parallel sentence pairs
- **Validation Split:** 2,000 parallel sentence pairs
- **Test Split:** 2,000 parallel sentence pairs

## 3. How to Download and Access in Python
```python
from datasets import load_dataset

# Load the official English-Urdu split
dataset = load_dataset("Helsinki-NLP/opus-100", "en-ur")

print(dataset)
# Output:
# DatasetDict({
#     train: Dataset({features: ['translation'], num_rows: 753913}),
#     validation: Dataset({features: ['translation'], num_rows: 2000}),
#     test: Dataset({features: ['translation'], num_rows: 2000})
# })
```

## 4. Cleaning & Filtering Pipeline Applied
1. **Deduplication:** Remove exact duplicates and empty strings (retains 724,408 pairs).
2. **Length Ratio Filter:** Drop pairs where $\max(L_{en}, L_{ur}) / \min(L_{en}, L_{ur}) > 3.0$ (retains 719,690 pairs).
3. **Length Truncation:** Retain sentences $\le 30$ tokens (retains 432,566 pairs).
4. **Urdu Script Verification:** Ensure the target sentence contains Unicode characters in the Arabic/Urdu block `\u0600-\u06FF` (retains 431,215 clean pairs).
