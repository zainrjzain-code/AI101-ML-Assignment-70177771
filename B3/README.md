# Task B3: Predicting Star Ratings of E-Commerce Clothing Reviews

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zainrjzain-code/AI101-ML-Assignment-70177771/blob/main/B3/B3_notebook.ipynb)
[![Report PDF](https://img.shields.io/badge/Report-70177771__B3__Report.pdf-red.svg)](report/70177771_B3_Report.pdf)
[![Primary Metric](https://img.shields.io/badge/Primary%20Metric-Macro--F1-blue.svg)](report/70177771_B3_Report.pdf)

---

## Executive Summary
This task investigates multi-class ordinal classification of customer star ratings (1 to 5) on the **Women's E-Commerce Clothing Reviews** dataset (23,486 reviews). The target distribution is heavily skewed toward positive ratings (55% are 5-star ratings). The pipeline combines structured customer metadata (Age, Feedback Count, Department, Division) with unstructured review text using `ColumnTransformer` with TF-IDF and tree-based gradient boosting.

---

## Benchmark Model Performance

### 5-Class Ordinal Classification (Test Set)
| Model | Weighting | Accuracy | Macro-F1 | Weighted-F1 | Ordinal MAE |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Multinomial Logistic Regression** | None | 0.6120 | 0.4480 | 0.6010 | 0.485 |
| **Multinomial Logistic Regression** | Balanced | 0.5480 | 0.4810 | 0.5620 | 0.592 |
| **Linear Support Vector Machine** | None | 0.6210 | 0.4720 | 0.6140 | 0.471 |
| **Linear Support Vector Machine** | Balanced | 0.5640 | 0.4980 | 0.5790 | 0.570 |
| **LightGBM Classifier (Winner)** | Balanced | **0.6558** | **0.5478** | **0.6508** | **0.428** |

### Feature Modality Ablation (LightGBM)
| Feature Subset | Accuracy | Macro-F1 | Weighted-F1 | Finding |
| :--- | :---: | :---: | :---: | :--- |
| **(i) Structured Metadata Only** | 0.5542 | 0.2185 | 0.4320 | Barely beats majority-class baseline |
| **(ii) Text Features Only (TF-IDF)** | 0.6480 | 0.5310 | 0.6410 | Captures core sentiment signals |
| **(iii) Combined (Text + Structured)** | **0.6558** | **0.5478** | **0.6508** | Structured metadata yields +1.68% F1 boost |

### 3-Class Sentiment Re-Framing
Grouping ratings into Negative (1–2), Neutral (3), and Positive (4–5):
- **Accuracy:** **85.64%**
- **Macro-F1:** **0.7812**
- **Business Insight:** Eliminates ambiguous boundary friction between 4-star and 5-star reviews, providing an actionable triage system for customer support.

---

## Directory Contents
- `B3_notebook.ipynb` — Executed Google Colab notebook with complete markdown, outputs, and findings.
- `report/70177771_B3_Report.pdf` — Two-page IEEE double-column report.
- `figures/` — Visualization artifacts:
  - `figure1_rating_distribution.png`: Skewed class distribution across 1–5 stars.
  - `figure2_review_length_by_rating.png`: Average word length vs satisfaction rating.
  - `figure3_age_distribution.png`: Customer demographic density.
  - `figure4_ratings_by_department.png`: Satisfaction across retail departments.
  - `figure5_confusion_matrix_5class.png`: 5x5 confusion matrix highlighting adjacent rating confusion.
  - `figure6_feature_ablation_comparison.png`: Structured vs Text vs Combined ablation.
  - `figure7_confusion_matrix_3class.png`: 3-class sentiment matrix.
- `data/README.md` — Dataset documentation, Kaggle download instructions, and leakage rule explanation.
