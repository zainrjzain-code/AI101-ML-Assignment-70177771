# Task B1: Detecting Fraudulent Job Postings (EMSCAD Dataset)

**Author:** Muhammad Zain-ul-Abideen  
**Roll Number:** 70177771  
**Section:** B  
**Course:** AI-101 (Introduction to Artificial Intelligence), The University of Lahore  
**Instructor:** Dr. Muhammad Awais  

---

## 1. Project Overview

This project implements mixed-modality machine learning architectures combining structured tabular metadata and natural language processing to identify fraudulent employment advertisements from the Employment Scam Aegean Dataset (EMSCAD).

- **Total Postings:** 17,880
- **Real Postings:** 17,014 (95.16%)
- **Fraudulent Postings:** 866 (4.84%)
- **Severe Class Imbalance:** ~19.6:1 ratio

---

## 2. Experimental Setup

- **Dataset Split:** Stratified 70% Train (12,516 samples; 606 fraud), 15% Validation (2,682 samples; 130 fraud), and 15% Test (2,682 samples; 130 fraud).
- **Leakage Prevention:** TF-IDF vectorizer (15,000 unigrams and bigrams), standard scalers, and one-hot encoders are strictly fitted on the training partition only.
- **Decision Threshold Tuning:** Thresholds tuned on the validation set to maximize F1-score for the fraud class.
- **Evaluation Metrics:** Fraud Class F1, Precision, Recall, Precision-Recall AUC (PR-AUC), and ROC-AUC.

---

## 3. Benchmark Results on Held-out Test Set (2,682 samples)

| Model Architecture | Tuned Threshold | Fraud Class F1 | Precision | Recall | PR-AUC | ROC-AUC |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression [WINNER]** | **0.66** | **0.7958** | **0.7338** | **0.8692** | **0.8770** | **0.9884** |
| Linear SVM (SGD Calibrated) | 0.78 | 0.7757 | 0.7669 | 0.7846 | 0.8641 | 0.9872 |
| Random Forest (150 trees) | 0.70 | 0.7324 | 0.9398 | 0.6000 | 0.8435 | 0.9846 |

---

## 4. Mandatory Modality Ablation Study

| Modality Setting | Fraud Class F1 | Precision | Recall | PR-AUC |
|---|:---:|:---:|:---:|:---:|
| **Structured Features Only** | 0.3057 | 0.2111 | 0.5538 | 0.1954 |
| **Text Features Only** | **0.8699** | **0.9224** | 0.8231 | **0.9013** |
| **Combined (Structured + Text)** | 0.7958 | 0.7338 | **0.8692 (Catches 113/130)** | 0.8770 |

**Finding:** Combining structured corporate metadata (absent logo, missing profile) with natural language text lifts fraud recall from **82.31% to 86.92% (+4.61% boost)**, successfully discovering elusive scams that text alone failed to detect.

---

## 5. Answers to Assignment Questions

### Question 1: Why is accuracy a poor metric here? What accuracy does a model that always predicts 'real' achieve?
- Legitimate postings comprise 95.16% of the dataset.
- A dummy baseline that classifies every posting as "Real" achieves a deceptive **95.16% accuracy**, but has a fraud recall of **0.0%**, missing 100% of employment scams.
- F1-score (Fraud Class) and PR-AUC are required to properly penalize minority class errors.

### Question 2: Does combining text and structured features beat either alone? By how much?
- Yes, specifically in **fraud recall**.
- Combining modalities elevates test recall from 82.31% to **86.92% (+4.61% gain)**, catching 113 out of 130 scam postings. In scam prevention, catching additional fraudulent posts before job seekers lose funds is paramount.

### Question 3: Which words/n-grams and structured features are most indicative of fraud? Show false positives and explain them.
- **Indicative Words:** `administrative entry`, `clerical data`, `clerical administrative`, `wire transfer`, `data entry`, `payroll`.
- **Indicative Structured Features:** `missing_company_profile` (19.3% fraud rate vs 1.5% when present) and `has_company_logo=0` (16.5% fraud rate vs 2.1% when present).
- **False Positives:** 41 legitimate postings were flagged as fraud. These are primarily early-stage startups that lack a company logo, leave the company profile blank, and recruit remote data-entry personnel.

---

## 6. Folder Contents

- `B1_notebook.ipynb`: Executed Google Colab / Jupyter notebook containing all code, outputs, and embedded figures.
- `report/70177771_B1_Report.pdf`: 2-page double-column IEEE report.
- `Task_B1_Complete_Project_Guide_Roman_Urdu.pdf`: Complete step-by-step project guide and viva handbook in Roman Urdu and simple English.
- `figures/`: High-resolution figures generated during EDA, modeling, and ablation.
- `data/README.md`: Instructions for downloading and placing the dataset.
