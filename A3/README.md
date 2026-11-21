# Task A3: Multi-Class Variety Classification of Dry Beans

**Author:** Muhammad Zain-ul-Abideen  
**Roll Number:** 70177771  
**Section:** B  
**Course:** AI-101 (Introduction to Artificial Intelligence), The University of Lahore  
**Instructor:** Dr. Muhammad Awais  

---

## 1. Project Overview

This project implements machine learning models to automatically classify dry beans into seven registered commercial varieties using 16 computer vision morphological and shape features.

The seven varieties are:
- **Dermason** (3,546 samples, 26.05%)
- **Sira** (2,636 samples, 19.37%)
- **Seker** (2,027 samples, 14.89%)
- **Horoz** (1,928 samples, 14.16%)
- **Cali** (1,630 samples, 11.98%)
- **Barbunya** (1,322 samples, 9.71%)
- **Bombay** (522 samples, 3.84%)

Total dataset size is 13,611 samples.

---

## 2. Experimental Setup

- **Dataset Split:** Stratified 70% Train (9,527 samples), 15% Validation (2,042 samples), and 15% Test (2,042 samples).
- **Leakage Prevention:** `StandardScaler` was fitted strictly on the training partition only and used to transform the validation and test partitions.
- **Evaluation Metrics:** Accuracy, Macro-Averaged Precision, Macro-Averaged Recall, Macro-Averaged F1-Score, and Weighted F1-Score.

---

## 3. Benchmark Results on Held-out Test Set (2,042 samples)

| Model | Test Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 |
|---|:---:|:---:|:---:|:---:|:---:|
| **Support Vector Machine (RBF, C=10.0) [WINNER]** | **0.9256** | **0.9372** | **0.9355** | **0.9360** | **0.9252** |
| Multilayer Perceptron (MLP 128-64) | 0.9221 | 0.9351 | 0.9331 | 0.9338 | 0.9218 |
| Multinomial Logistic Regression | 0.9202 | 0.9329 | 0.9332 | 0.9327 | 0.9201 |
| Random Forest (200 trees) | 0.9197 | 0.9312 | 0.9317 | 0.9313 | 0.9196 |
| Gradient Boosting (150 trees) | 0.9163 | 0.9278 | 0.9303 | 0.9287 | 0.9163 |

---

## 4. Key Assignment Findings

### Question 1: Which bean varieties are confused most and why?
**Dermason and Sira** show the highest mutual confusion:
- 38 actual Sira beans were predicted as Dermason.
- 33 actual Dermason beans were predicted as Sira.

**Reason:** Both varieties are medium-sized elliptical beans with highly overlapping area, perimeter, and compactness distributions. In contrast, the **Bombay** variety achieved a flawless 100% precision and recall because its massive size (>170,000 pixel area) separates it completely from all other varieties.

### Question 2: Does class weighting improve minority variety recognition?
Yes. Applying `class_weight='balanced'` assigns higher penalties to minority class errors:
- Validation Macro-F1 improved from **0.9397 to 0.9409** (+0.12%) for SVM with zero drop in overall accuracy.
- Validation Macro-F1 improved from **0.9366 to 0.9372** for Logistic Regression.

### Question 3: How many PCA components are needed to retain 98% of peak Macro-F1?
The full model achieves a Macro-F1 of 0.9360. 98% of this value is 0.9173.
- $k = 4$ components retain 94.8% variance and achieve Macro-F1 = 0.8987 (96.0% of peak).
- $k = 8$ components retain 99.7% variance and achieve Macro-F1 = **0.9360 (100.0% of peak)**.

**Answer:** Exactly **8 principal components** are required. This reduces the feature dimensionality by 50% with zero loss in predictive fidelity.

---

## 5. Folder Contents

- `A3_notebook.ipynb`: Fully executed Google Colab / Jupyter notebook containing all code, tables, and embedded plots.
- `report/70177771_A3_Report.pdf`: 2-page double-column IEEE report.
- `Task_A3_Complete_Project_Guide_Roman_Urdu.pdf`: Complete step-by-step project guide and viva handbook in Roman Urdu and simple English.
- `figures/`: High-resolution figures generated during EDA, modeling, and dimensionality reduction.
- `data/README.md`: Instructions for downloading and placing the dataset.
