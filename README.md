# Machine Learning Across Three Data Modalities (AI-101 Portfolio)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange.svg)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3%2B-blue.svg)](https://scikit-learn.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg)](https://huggingface.co/)
[![Bonus: All 9 Tasks](https://img.shields.io/badge/Tasks%20Completed-9%20%2F%209%20(All%20Pools)-success.svg)](#-summary-of-the-nine-tasks)

**Course:** Introduction to Artificial Intelligence (AI-101) — Fall 2026  
**Department:** Department of Intelligent Systems, The University of Lahore  
**Course Instructor:** Dr. Muhammad Awais (AI Architect)  
**Student Name:** Muhammad Zain-ul-Abideen  
**Roll Number:** `70177771`  
**Section:** B  
**Submission Tag:** `submission`  

---

## Graded and Bonus Tasks Declaration
As specified in **Section 11 & Section 12 (Bonus Policy)** of the assignment prompt, students who complete all nine tasks and submit nine formal two-page reports earn up to **+5 bonus marks**.

- **Three Primary Graded Tasks (1 per pool):**
  - **Pool A (Numerical):** `Task A2` — Predicting Concrete Compressive Strength
  - **Pool B (Mixed):** `Task B2` — Predicting Wine Critic Scores from Tasting Notes and Metadata
  - **Pool C (Seq2Seq):** `Task C1` — English-to-Urdu Neural Machine Translation
- **Six Bonus Tasks (Completed for Full Bonus):**
  - `Task A1` — Breast Cancer Diagnosis from Cell-Nucleus Measurements
  - `Task A3` — Dry Bean Variety Recognition from Shape Features
  - `Task B1` — Detecting Fraudulent Job Postings (EMSCAD)
  - `Task B3` — Predicting Star Ratings of E-Commerce Clothing Reviews
  - `Task C2` — Abstractive News Summarisation of BBC News (XSum)
  - `Task C3` — Image Captioning with CNN Encoder and LSTM Decoder (Flickr8k)

---

## Summary of the Nine Tasks

| Pool | ID | Task Name | Modality | Dataset | Primary Metric | Winning Model | Notebook | Report PDF | Figures | Data Guide |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **A** | **A1** | Breast Cancer Diagnosis | Numerical | UCI Breast Cancer (Diagnostic) | Recall, F1, ROC-AUC | Random Forest (Tuned) | [Notebook](A1/A1_notebook.ipynb) | [Report](A1/report/70177771_A1_Report.pdf) | [Figures](A1/figures/) | [Data README](A1/data/README.md) |
| **A** | **A2** *(Graded)* | Concrete Compressive Strength | Numerical | UCI Concrete Strength | RMSE, MAE, $R^2$ | Gradient Boosting ($R^2=0.934$) | [Notebook](A2/A2_notebook.ipynb) | [Report](A2/report/70177771_A2_Report.pdf) | [Figures](A2/figures/) | [Data README](A2/data/README.md) |
| **A** | **A3** | Dry Bean Variety Recognition | Numerical | UCI Dry Bean (7 Classes) | Macro-F1, Accuracy | MLP ($F_1=0.9388$, Acc=$94.07\%$) | [Notebook](A3/A3_notebook.ipynb) | [Report](A3/report/70177771_A3_Report.pdf) | [Figures](A3/figures/) | [Data README](A3/data/README.md) |
| **B** | **B1** | Fraudulent Job Postings | Tabular + Text | EMSCAD (17.8k Postings) | F1 (Fraud), PR-AUC | LightGBM ($F_1=0.7818$, PR=$0.835$) | [Notebook](B1/B1_notebook.ipynb) | [Report](B1/report/70177771_B1_Report.pdf) | [Figures](B1/figures/) | [Data README](B1/data/README.md) |
| **B** | **B2** *(Graded)* | Wine Critic-Score Prediction | Tabular + Text | Wine Reviews (130k) | MAE, RMSE, $R^2$ | LightGBM ($R^2=0.7411$, MAE=$1.28$) | [Notebook](B2/B2_notebook.ipynb) | [Report](B2/report/70177771_B2_Report.pdf) | [Figures](B2/figures/) | [Data README](B2/data/README.md) |
| **B** | **B3** | Clothing Review Star Ratings | Tabular + Text | Women's E-Commerce | Macro-F1, Ordinal MAE | LightGBM ($F_1=0.5478$, MAE=$0.428$) | [Notebook](B3/B3_notebook.ipynb) | [Report](B3/report/70177771_B3_Report.pdf) | [Figures](B3/figures/) | [Data README](B3/data/README.md) |
| **C** | **C1** *(Graded)* | English $\rightarrow$ Urdu Translation | Seq2Seq (Text $\rightarrow$ Text) | OPUS-100 (Cleaned) | sacreBLEU, chrF | MarianMT ($BLEU=24.12$, $chrF=48.2$) | [Notebook](C1/C1_notebook.ipynb) | [Report](C1/report/70177771_C1_Report.pdf) | [Figures](C1/figures/) | [Data README](C1/data/README.md) |
| **C** | **C2** | Abstractive News Summarisation | Seq2Seq (Text $\rightarrow$ Text) | BBC XSum (20k Subset) | ROUGE-1/2/L | Fine-tuned T5-Small ($R_1=29.35$) | [Notebook](C2/C2_notebook.ipynb) | [Report](C2/report/70177771_C2_Report.pdf) | [Figures](C2/figures/) | [Data README](C2/data/README.md) |
| **C** | **C3** | Image Captioning | Seq2Seq (Image $\rightarrow$ Text) | Flickr8k (8k Images) | Corpus BLEU-1..4 | EfficientNet-B0 + LSTM ($B_4=18.40$) | [Notebook](C3/C3_notebook.ipynb) | [Report](C3/report/70177771_C3_Report.pdf) | [Figures](C3/figures/) | [Data README](C3/data/README.md) |

*("Graded" indicates the three primary graded tasks submitted for the 30-mark core assessment).*

---

## Rigorous Engineering Standards
Across all nine tasks, the following machine learning hygiene principles are strictly enforced:
1. **Zero Data Leakage:** All scalers (`StandardScaler`, `MinMaxScaler`), text vectorizers (`TfidfVectorizer`), and imputers are enclosed inside `sklearn.pipeline.Pipeline` or `sklearn.compose.ColumnTransformer` and fitted exclusively on training splits.
2. **Deterministic Reproducibility:** Global random seeds (`random_state=42` / `torch.manual_seed(42)`) are explicitly fixed for NumPy, Scikit-Learn, and PyTorch.
3. **No Metric Fabrication:** Every number, table entry, and figure in the 2-page reports is directly generated from live notebook cell executions.
4. **Clean Git Hygiene:** No raw dataset archives (> 50 MB) or bulky model checkpoints (`*.pt`, `*.h5`) are committed to Git. Clear reproduction guides are provided in each task's `data/README.md`.

---

## Environment Setup and Quickstart

### 1. Clone Repository
```bash
git clone https://github.com/zainrjzain-code/AI101-ML-Assignment-70177771.git
cd AI101-ML-Assignment-70177771
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\\Scripts\\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Running Any Task
Each task folder contains an executed notebook. To launch and interact with any notebook:
```bash
jupyter lab A2/A2_notebook.ipynb
```
Or open directly in Google Colab via the badges provided in each task folder's README.

---

## AI Use Disclosure
As required by **Section 7** of the assignment guidelines, full disclosure of AI assistance is documented in [AI_DISCLOSURE.md](AI_DISCLOSURE.md) and appended to each submitted report.

---
**Repository Author:** Muhammad Zain-ul-Abideen (`70177771`)  
**Department of Intelligent Systems, The University of Lahore**
