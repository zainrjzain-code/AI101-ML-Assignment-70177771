# Task A1: Breast Cancer Diagnosis from Cell-Nucleus Measurements

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zainrjzain-code/AI101-ML-Assignment-70177771/blob/main/A1/A1_notebook.ipynb)
[![Report PDF](https://img.shields.io/badge/Report-70177771__A1__Report.pdf-red.svg)](report/70177771_A1_Report.pdf)
[![Primary Metric](https://img.shields.io/badge/Primary%20Metric-Recall%20%7C%20ROC--AUC-green.svg)](report/70177771_A1_Report.pdf)

---

## Executive Summary
This task addresses binary diagnostic classification on the **Breast Cancer Wisconsin (Diagnostic)** dataset (569 samples, 30 continuous morphological features). In clinical screening, missing a malignancy (False Negative) is substantially more dangerous than a false alarm (False Positive). Therefore, evaluation is strictly focused on **Malignant Recall**, **ROC-AUC**, and **Decision Threshold Optimization**.

---

## Key Experimental Results

| Model Pipeline | Accuracy | Precision (Malignant) | Recall (Malignant) | F1-Score (Malignant) | ROC-AUC | 5-Fold CV F1 (Mean ± Std) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Baseline)** | 0.9649 | 0.9524 | 0.9524 | 0.9524 | 0.9950 | $0.9643 \pm 0.0210$ |
| **Support Vector Machine (RBF)** | 0.9737 | 0.9756 | 0.9524 | 0.9639 | 0.9967 | $0.9688 \pm 0.0185$ |
| **Random Forest (Tuned)** | **0.9825** | **0.9762** | **0.9762** | **0.9762** | **0.9980** | **$0.9725 \pm 0.0152$** |

### Threshold Optimization Study
Moving the decision threshold on the winning Random Forest model to achieve **Malignant Recall $\ge 0.95$**:
- **Default Threshold (0.50):** Recall = 0.9762, Precision = 0.9762, False Negatives = 1.
- **Optimized Threshold (0.35):** Recall = 1.0000 (0 False Negatives), Precision = 0.9545 (cost of only 2.17% precision).

---

## Directory Contents
- `A1_notebook.ipynb` — Fully executed Google Colab notebook with all code, outputs, and findings.
- `report/70177771_A1_Report.pdf` — Formal IEEE 2-page double-column report.
- `figures/` — High-resolution visualization artifacts:
  - `figure1_class_distribution.png`: Class balance breakdown (357 benign vs 212 malignant).
  - `figure2_correlation_matrix.png`: Full $30 \times 30$ Spearman correlation heatmap.
  - `figure3_confusion_matrices.png`: Confusion matrices comparing all 3 classifiers.
  - `figure4_roc_curves.png`: Multi-model ROC comparison curves.
  - `figure5_adjusted_threshold_confusion_matrix.png`: Zero false negative decision boundary.
  - `figure6_feature_importances.png`: Top 10 permutation feature importances.
- `data/README.md` — Dataset description and programmatic access guide.
