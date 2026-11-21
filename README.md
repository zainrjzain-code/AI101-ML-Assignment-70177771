# Machine Learning Across Three Data Modalities (AI-101)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg)](https://scikit-learn.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg)](https://pytorch.org/)
[![Course](https://img.shields.io/badge/AI--101-Introduction%20to%20AI-success.svg)](https://www.uol.edu.pk/)
[![IEEE Reports](https://img.shields.io/badge/Reports-IEEE%202--Column%20PDF-brightgreen.svg)](report/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Department of Computer Science | The University of Lahore**  
> **Course:** Introduction to Artificial Intelligence (AI-101)  
> **Instructor:** Dr. Muhammad Awais  
> **Student:** Muhammad Zain-ul-Abideen  
> **Roll Number:** 70177771  
> **Section:** B  

---

## Executive Overview

This repository contains an end-to-end applied machine learning portfolio implementing rigorous data preprocessing, zero-leakage feature engineering, cross-validation tuning, ablation studies, and error analysis across three foundational data modalities:
1. **Numerical Tabular Modality** (Supervised Classification & Regression)
2. **Mixed Modality** (Structured Tabular + Unstructured Natural Language Text)
3. **Unstructured Sequence-to-Sequence Modality** (Multimodal Deep Learning: Image → Text)

Every task includes an executed Google Colab / Jupyter notebook, publication-grade figures, a 2-page double-column scientific report formatted to IEEE conference standards, a dedicated Roman Urdu project & viva handbook, and complete documentation.

---

## Portfolio Summary & Benchmark Results

| Task ID | Task Title | Modality & Setting | Benchmark Models | Primary Metric & Best Result | Deliverables |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **A1** | **Breast Cancer Diagnosis** | Numerical Tabular<br/>*(Binary Classification)* | Logistic Regression, RBF-SVM, Random Forest | **Recall (Malignant):** 92.86%<br/>**ROC-AUC:** 0.993 *(SVM)* | [Notebook](A1/A1/A1-Notebook.ipynb) • [Report](A1/report/70177771_A1_Report.pdf) |
| **A2** | **Concrete Compressive Strength** | Numerical Tabular<br/>*(Supervised Regression)* | Linear Regression, Poly + Ridge, Random Forest, **Gradient Boosting**, MLPRegressor | **Test R²:** 0.9277 (92.8%)<br/>**Test RMSE:** 4.31 MPa *(GB)* | [Notebook](A2/A2_notebook.ipynb) • [Report](A2/report/70177771_A2_Report.pdf) • [Roman Urdu Guide](A2/Task_A2_Complete_Project_Guide_Roman_Urdu.pdf) |
| **A3** | **Dry Bean Variety Classification** | Numerical Tabular<br/>*(7-Class Classification)* | Logistic Regression, **RBF-SVM**, Random Forest, Gradient Boosting, MLP | **Test Accuracy:** 92.56%<br/>**Macro-F1:** 0.9360 *(SVM)* | [Notebook](A3/A3_notebook.ipynb) • [Report](A3/report/70177771_A3_Report.pdf) • [Roman Urdu Guide](A3/Task_A3_Complete_Project_Guide_Roman_Urdu.pdf) |
| **B1** | **Fraudulent Job Postings** | Mixed Modality<br/>*(Tabular + TF-IDF NLP)* | **Logistic Regression**, Linear SVM, Random Forest | **Fraud F1:** 0.7958<br/>**PR-AUC:** 0.8770 • **Recall:** 86.92% | [Notebook](B1/B1_notebook.ipynb) • [Report](B1/report/70177771_B1_Report.pdf) • [Roman Urdu Guide](B1/Task_B1_Complete_Project_Guide_Roman_Urdu.pdf) |
| **B3** | **Clothing Review Ratings** | Mixed Modality<br/>*(Tabular + TF-IDF NLP)* | Multinomial LR, Linear SVM, Random Forest, **LightGBM** *(Balanced)* | **Macro-F1 (3-Class):** 61.44%<br/>**Accuracy (3-Class):** 79.45% | [Notebook](B3/Task_B3_AI_Assignment.ipynb) • [Report](B3/70177771_B3_Report_3class_updated.pdf) |
| **C3** | **Image Captioning on Flickr8k** | Multimodal Seq2Seq<br/>*(Vision + LSTM NLP)* | ResNet50 + LSTM vs.<br/>**EfficientNet-B0 + LSTM** | **BLEU-1:** 60.81%<br/>**BLEU-4:** 18.79% *(Beam k=5)* | [Notebook](C3/Task_C3_AI_Assignment.ipynb) • [Report](C3/70177771-C3-Report.pdf.pdf) |

---

## Detailed Task Summaries

### Task B1: Detecting Fraudulent Job Postings (Pool B — Mixed Modality)
- **Objective:** Detect deceptive online recruitment advertisements using 17,880 postings from the EMSCAD dataset (17,014 legitimate and 866 fraudulent; 4.84% scam prevalence).
- **Leakage Prevention:** Stratified 70/15/15 split. Preprocessors (15,000 TF-IDF features, standard scalers, one-hot encoders) strictly fitted on training split only.
- **Key Results:**
  - **Best Model:** L2-regularized Logistic Regression (Threshold 0.66) attained **Fraud F1 = 0.7958**, **PR-AUC = 0.8770**, and intercepted **86.92% of scams (113/130)** on the test set.
  - **Ablation Study:** Combining structured metadata with natural language text boosted fraud recall from **82.31% to 86.92% (+4.61% gain)**.
  - **Domain Signals:** Missing company profile (19.3% fraud rate vs 1.5% present) and absence of company logo (16.5% fraud rate vs 2.1% present) are the strongest structural predictors.
- **Deliverables:** [Executed Notebook](B1/B1_notebook.ipynb) | [IEEE 2-Page Report](B1/report/70177771_B1_Report.pdf) | [Roman Urdu Guide](B1/Task_B1_Complete_Project_Guide_Roman_Urdu.pdf)

---

### Task A3: Multi-Class Variety Classification of Dry Beans (Pool A — Numerical)
- **Objective:** Classify 13,611 dry bean specimens into 7 commercial varieties using 16 morphological and shape descriptors.
- **Key Results:** Support Vector Machine (RBF kernel, C=10.0) achieved **92.56% Test Accuracy** and **0.9360 Macro-F1**. PCA dimensionality reduction to 8 components retains 100% of peak Macro-F1.
- **Deliverables:** [Executed Notebook](A3/A3_notebook.ipynb) | [IEEE 2-Page Report](A3/report/70177771_A3_Report.pdf) | [Roman Urdu Guide](A3/Task_A3_Complete_Project_Guide_Roman_Urdu.pdf)

---

### Task A2: Predicting Concrete Compressive Strength (Pool A — Numerical)
- **Objective:** Predict 28-day concrete compressive strength (MPa) from 8 mixture component densities and curing age.
- **Key Results:** Gradient Boosting Regressor achieved **R² = 0.9277 (92.8%)** and **RMSE = 4.31 MPa**. Civil engineering feature engineering raised linear model fidelity by +20.5%.
- **Deliverables:** [Executed Notebook](A2/A2_notebook.ipynb) | [IEEE 2-Page Report](A2/report/70177771_A2_Report.pdf) | [Roman Urdu Guide](A2/Task_A2_Complete_Project_Guide_Roman_Urdu.pdf)

---

### Task A1: Breast Cancer Diagnosis (Pool A — Numerical)
- **Objective:** Diagnostic binary classification of breast mass biopsies (Malignant vs. Benign).
- **Key Results:** Support Vector Machine (RBF) achieved 92.86% Malignant Recall and 0.993 ROC-AUC.
- **Deliverables:** [Executed Notebook](A1/A1/A1-Notebook.ipynb) | [IEEE 2-Page Report](A1/report/70177771_A1_Report.pdf)

---

### Task B3: E-Commerce Clothing Review Rating Prediction (Pool B — Mixed Modality)
- **Objective:** Predict consumer satisfaction ratings from combined structured customer demographics and unstructured natural language reviews.
- **Key Results:** LightGBM with balanced class weights achieved 61.44% Macro-F1 and 79.45% Accuracy on the 3-class target setting.
- **Deliverables:** [Executed Notebook](B3/Task_B3_AI_Assignment.ipynb) | [IEEE 2-Page Report](B3/70177771_B3_Report_3class_updated.pdf)

---

### Task C3: Image Captioning on Flickr8k (Pool C — Multimodal Sequence-to-Sequence)
- **Objective:** End-to-end multimodal sequence-to-sequence generation mapping visual scene representations to natural language descriptions.
- **Key Results:** EfficientNet-B0 + LSTM with beam search (k=5) achieved BLEU-1 of 60.81% and BLEU-4 of 18.79%.
- **Deliverables:** [Executed Notebook](C3/Task_C3_AI_Assignment.ipynb) | [IEEE 2-Page Report](C3/70177771-C3-Report.pdf.pdf)

---

## Repository Structure

```
├── A1/                                   # Task A1: Breast Cancer Diagnosis
│   ├── A1/A1-Notebook.ipynb              # Executed notebook
│   └── report/70177771_A1_Report.pdf     # 2-page IEEE report
├── A2/                                   # Task A2: Concrete Strength Regression
│   ├── A2_notebook.ipynb                 # Executed Google Colab notebook
│   ├── figures/                          # 6 High-resolution publication plots
│   ├── report/70177771_A2_Report.pdf     # 2-page IEEE report
│   ├── Task_A2_Complete_Project_Guide_Roman_Urdu.pdf # Roman Urdu Project Guide
│   └── README.md                         # Task overview & engineering analysis
├── A3/                                   # Task A3: Dry Bean Variety Classification
│   ├── A3_notebook.ipynb                 # Executed Google Colab notebook
│   ├── figures/                          # 6 High-resolution publication plots
│   ├── report/70177771_A3_Report.pdf     # 2-page IEEE report
│   ├── Task_A3_Complete_Project_Guide_Roman_Urdu.pdf # Roman Urdu Project Guide
│   └── README.md                         # Task overview & engineering analysis
├── B1/                                   # Task B1: Fraudulent Job Postings Detection
│   ├── B1_notebook.ipynb                 # Executed Google Colab notebook
│   ├── figures/                          # 6 High-resolution publication plots
│   ├── report/70177771_B1_Report.pdf     # 2-page IEEE report
│   ├── Task_B1_Complete_Project_Guide_Roman_Urdu.pdf # Roman Urdu Project Guide
│   └── README.md                         # Task overview & ablation analysis
├── B3/                                   # Task B3: Clothing Reviews Mixed Modality
│   ├── Task_B3_AI_Assignment.ipynb       # Executed notebook
│   └── 70177771_B3_Report_3class_updated.pdf # 2-page IEEE report
├── C3/                                   # Task C3: Flickr8k Image Captioning
│   ├── Task_C3_AI_Assignment.ipynb       # Executed notebook
│   └── 70177771-C3-Report.pdf.pdf        # 2-page IEEE report
├── AI_DISCLOSURE.md                      # AI assistance compliance disclosure
├── requirements.txt                      # Environment dependencies
└── README.md                             # Root portfolio documentation
```

---

## AI Disclosure Statement

This project adheres to the course academic integrity and AI transparency policy. Generative AI tools (Antigravity) were utilized as coding and documentation assistants. Full methodology, experimental design, metric interpretation, and verification were conducted directly by the author. See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for full compliance details.
