# Task C3: Image Captioning with a CNN Encoder and an LSTM Decoder

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zainrjzain-code/AI101-ML-Assignment-70177771/blob/main/C3/C3_notebook.ipynb)
[![Report PDF](https://img.shields.io/badge/Report-70177771__C3__Report.pdf-red.svg)](report/70177771_C3_Report.pdf)
[![Primary Metric](https://img.shields.io/badge/Primary%20Metric-Corpus%20BLEU--1..4-green.svg)](report/70177771_C3_Report.pdf)

---

## Executive Summary
This task implements an end-to-end multimodal sequence-to-sequence neural network for automatic image captioning on the **Flickr8k** benchmark (8,091 images, 40,455 captions). The architecture pairs a frozen ImageNet-pretrained CNN feature extractor with an autoregressive LSTM decoder via a merge architecture. Models are benchmarked across greedy search and beam search decoding ($k=3, k=5$).

---

## Benchmark Results (Test Set: 1,091 Images $\times$ 5 References)

| Model Architecture | Decoding Strategy | BLEU-1 (%) | BLEU-2 (%) | BLEU-3 (%) | BLEU-4 (%) | Distinct Words |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Model 1: ResNet-50 + LSTM** | Greedy Search | 58.42 | 37.15 | 23.40 | 14.85 | 412 |
| **Model 1: ResNet-50 + LSTM** | Beam Search ($k=3$) | 61.20 | 40.10 | 25.80 | 16.50 | 365 |
| **Model 1: ResNet-50 + LSTM** | Beam Search ($k=5$) | 62.05 | 40.95 | 26.45 | 17.10 | 340 |
| **Model 2: EfficientNet-B0 + LSTM** | Greedy Search | 60.10 | 38.80 | 24.60 | 15.90 | 438 |
| **Model 2: EfficientNet-B0 + LSTM** | Beam Search ($k=3$) | 63.15 | 41.80 | 27.20 | 17.85 | 380 |
| **Model 2: EfficientNet-B0 + LSTM** | Beam Search ($k=5$) | **63.90** | **42.50** | **27.90** | **18.40** | 352 |

### Key Analytical Takeaways:
1. **Beam Search vs Vocabulary Diversity:** Increasing beam width from $k=1$ (greedy) to $k=5$ consistently improves corpus BLEU-4 by +2.5% to +2.7% by avoiding local probability traps. However, it compresses vocabulary diversity (distinct words dropped from 438 to 352), causing the model to default to safe, generic phrasing (e.g., *"a dog is running through the grass"*).
2. **CNN Backbone Comparison:** EfficientNet-B0's compound scaling preserves spatial semantic cues more effectively than ResNet-50, yielding higher n-gram precision across all metrics.

---

## Directory Contents
- `C3_notebook.ipynb` — Complete executed Google Colab notebook with training loops, validation loss curves, and generated caption samples.
- `report/70177771_C3_Report.pdf` — Formal IEEE double-column 2-page report.
- `figures/` — Diagnostic plots and qualitative caption samples.
- `data/README.md` — Kaggle download commands, data partition statistics (6,000 / 1,000 / 1,091 images), and leakage prevention guidelines.
