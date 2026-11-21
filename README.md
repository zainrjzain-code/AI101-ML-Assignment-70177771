# Machine Learning Across Three Data Modalities (AI-101)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-orange.svg)](https://scikit-learn.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg)](https://pytorch.org/)
[![Course](https://img.shields.io/badge/AI--101-Introduction%20to%20AI-success.svg)](https://www.uol.edu.pk/)
[![IEEE Reports](https://img.shields.io/badge/Reports-IEEE%202--Column%20PDF-brightgreen.svg)](report/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Department of Intelligent Systems | The University of Lahore**  
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

Every task includes an executed Google Colab / Jupyter notebook, publication-grade figures, a 2-page double-column scientific report formatted to IEEE conference standards, and complete documentation.

---

## Portfolio Summary & Benchmark Results

| Task ID | Task Title | Modality & Setting | Benchmark Models | Primary Metric & Best Result | Deliverables |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **A1** | **Breast Cancer Diagnosis** | Numerical Tabular<br/>*(Binary Classification)* | Logistic Regression, RBF-SVM, Random Forest | **Recall (Malignant):** 92.86%<br/>**ROC-AUC:** 0.993 *(SVM)* | [Notebook](A1/A1/A1-Notebook.ipynb) • [Report](A1/report/70177771_A1_Report.pdf) |
| **A2** | **Concrete Compressive Strength** | Numerical Tabular<br/>*(Supervised Regression)* | Linear Regression, Poly + Ridge, Random Forest, **Gradient Boosting**, MLPRegressor | **Test R²:** 0.9277 (92.8%)<br/>**Test RMSE:** 4.31 MPa *(GB)* | [Notebook](A2/A2_notebook.ipynb) • [Report](A2/report/70177771_A2_Report.pdf) • [Roman Urdu Guide](A2/Task_A2_Complete_Project_Guide_Roman_Urdu.pdf) |
| **B3** | **Clothing Review Ratings** | Mixed Modality<br/>*(Tabular + TF-IDF NLP)* | Multinomial LR, Linear SVM, Random Forest, **LightGBM** *(Balanced)* | **Macro-F1 (3-Class):** 61.44%<br/>**Accuracy (3-Class):** 79.45% | [Notebook](B3/Task_B3_AI_Assignment.ipynb) • [Report](B3/70177771_B3_Report_3class_updated.pdf) |
| **C3** | **Image Captioning on Flickr8k** | Multimodal Seq2Seq<br/>*(Vision + LSTM NLP)* | ResNet50 + LSTM vs.<br/>**EfficientNet-B0 + LSTM** | **BLEU-1:** 60.81%<br/>**BLEU-4:** 18.79% *(Beam k=5)* | [Notebook](C3/Task_C3_AI_Assignment.ipynb) • [Report](C3/70177771-C3-Report.pdf.pdf) |

---

## Detailed Task Summaries

### Task A2: Predicting Concrete Compressive Strength (Pool A — Numerical)
- **Problem Statement:** Standard laboratory testing of concrete requires 28 days of water curing before destructive crushing tests. This project builds machine learning models to predict compressive strength directly from mixture components (cement, slag, fly ash, water, superplasticizer, coarse/fine aggregate) and curing age.
- **Key Engineering Insight:** Introducing domain-driven physical features—**Water-to-Cement Ratio ($w/c$, Abrams' Law)** and **$\log(	ext{Age})$ (logarithmic hydration kinetics)**—increased baseline Linear Regression explained variance from $R^2 = 0.6276$ to $0.8329$ (**+20.5% boost**).
- **Champion Architecture:** Gradient Boosting Regressor achieved $R^2 = 0.9277$, $	ext{RMSE} = 4.31	ext{ MPa}$, and $	ext{MAE} = 2.85	ext{ MPa}$ on the held-out test set, with 5-fold cross-validation RMSE of $4.69 \pm 0.37	ext{ MPa}$.
- **Diagnostic Visualizations:** Homoscedasticity residual analysis, predicted-vs-actual 45° calibration, and permutation feature importance.

### Task B3: Predicting Star Ratings of E-Commerce Clothing Reviews (Pool B — Mixed)
- **Problem Statement:** Predict customer star ratings (1–5) using review text combined with structured customer attributes (Age, Positive Feedback Count) and categorical metadata (Division, Department, Class).
- **Data Leakage Prevention:** `Recommended IND` was strictly omitted from input features as it is co-generated with the rating at checkout time.
- **Feature Ablation:** Evaluated structured-only vs. text-only vs. combined representations. The combined representation with class-weighted LightGBM achieved the highest validation Macro-F1.
- **Sentiment Reframing:** Reframed the 5-class problem into an actionable 3-class business sentiment system (Negative 1–2, Neutral 3, Positive 4–5), achieving 79.45% accuracy and 61.44% Macro-F1.

### Task C3: Image Captioning with CNN Encoders and LSTM Decoders (Pool C — Multimodal)
- **Problem Statement:** Generate descriptive, natural-language captions for input images using the Flickr8k benchmark (8,091 images, 40,455 captions).
- **Architectures Compared:** ResNet50 + LSTM vs. EfficientNet-B0 + LSTM using a merge-model architecture.
- **Decoding Strategies:** Compared Greedy Search against Beam Search ($k = 3$ and $k = 5$). Beam search ($k = 5$) with EfficientNet-B0 achieved superior linguistic fluency and corpus BLEU scores (BLEU-1: 60.81%, BLEU-4: 18.79%).

---

## Repository Architecture

```text
AI101-ML-Assignment-70177771/
├── A1/                                   # Task A1: Breast Cancer Diagnosis (Classification)
│   ├── A1/
│   │   ├── A1-Notebook.ipynb             # Executed notebook
│   │   └── figures/                      # ROC curves & confusion matrices
│   ├── report/
│   │   └── 70177771_A1_Report.pdf        # IEEE 2-page report
│   └── README.md
│
├── A2/                                   # Task A2: Concrete Strength Regression
│   ├── A2_notebook.ipynb                 # Fully executed notebook with embedded outputs
│   ├── Task_A2_Complete_Project_Guide_Roman_Urdu.pdf # Complete 4-page student & viva guide
│   ├── data/
│   │   └── README.md                     # Dataset source and download instructions
│   ├── figures/                          # Publication-ready diagnostic figures
│   │   ├── figure1_eda_distributions.png
│   │   ├── figure2_correlation_matrix.png
│   │   ├── figure3_scatter_relationships.png
│   │   ├── figure4_predicted_vs_actual.png
│   │   ├── figure5_residual_analysis.png
│   │   └── figure6_feature_importance.png
│   ├── report/
│   │   ├── 70177771_A2_Report.pdf        # 2-Page IEEE double-column PDF report
│   │   └── make_a2_report.py             # Reproducible report generator
│   └── README.md
│
├── B3/                                   # Task B3: E-Commerce Clothing Reviews (Mixed)
│   ├── Task_B3_AI_Assignment.ipynb       # Executed notebook
│   ├── 70177771_B3_Report_3class_updated.pdf # IEEE 2-page report
│   ├── data/README.md
│   ├── figures/
│   └── README.md
│
├── C3/                                   # Task C3: Flickr8k Image Captioning (Seq2Seq)
│   ├── Task_C3_AI_Assignment.ipynb       # Executed notebook
│   ├── 70177771-C3-Report.pdf.pdf        # IEEE 2-page report
│   ├── figures/
│   └── README.md
│
├── README.md                             # Global project documentation
├── requirements.txt                      # Environment dependencies
├── AI_DISCLOSURE.md                      # Transparent AI usage disclosure
└── .gitignore                            # Excludes large binaries and dataset dumps
```

---

## Rigorous Engineering Principles Followed

1. **Zero Data Leakage:**
   - All standardizers, polynomial transformers, and text vectorizers are fit exclusively on the training folds inside scikit-learn `Pipeline` or `ColumnTransformer` constructs. Test folds are evaluated strictly once for un-biased performance estimation.
2. **Full Reproducibility:**
   - Random seeds (`random_state=42`) are fixed across NumPy, Scikit-Learn, and PyTorch.
3. **No Large Files in Git:**
   - Large raw datasets (>50 MB) and heavyweight model weights are excluded via `.gitignore`. Download instructions and automated fetch scripts are provided inside each task's `data/README.md`.
4. **Transparent AI Disclosure:**
   - As per course policy, all generative AI assistance (debugging, formatting, and layout assistance) is fully disclosed in `AI_DISCLOSURE.md`.

---

## Installation & Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/zainrjzain-code/AI101-ML-Assignment-70177771.git
cd AI101-ML-Assignment-70177771
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run Notebooks
All notebooks are self-contained and pre-configured to automatically load dataset mirrors or standard UCI/Kaggle accessors. You can open any notebook directly in VS Code, Jupyter Lab, or upload to Google Colab.
