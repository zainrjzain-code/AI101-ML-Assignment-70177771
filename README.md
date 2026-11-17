# AI101 - Machine Learning Assignment

This repository contains my AI101 machine learning assignment work. Each task has its own folder with its notebook, report, figures, and data instructions.

## Student

- **Name:** Muhammad Zain-ul-Abideen
- **Roll Number:** 70177771
- **Section:** B

## Tasks Attempted

### A1 - Breast Cancer Diagnosis

This task classifies breast tumors as benign or malignant using machine learning.

**Models:** Logistic Regression, Support Vector Machine (SVM), and Random Forest.

**Techniques:** Exploratory Data Analysis, preprocessing and feature scaling, hyperparameter tuning, stratified 5-fold cross-validation, model evaluation, threshold analysis, and feature importance.

### B3 - Clothing Review Ratings

This task predicts clothing review ratings from review text and customer and product information. The five-class task predicts ratings from 1 to 5. The three-class task groups ratings as Negative (1-2), Neutral (3), and Positive (4-5).

**Models:** Logistic Regression, Linear SVM, Random Forest and LightGBM, compared with and without balanced class weights.

**Features:** TF-IDF review text, age, log positive-feedback count, review length, and product categories. `Recommended IND` was excluded to prevent data leakage.

**Selected model:** LightGBM with balanced class weights, selected using validation Macro-F1.

**Five-class test results:** Accuracy 60.55%, Macro-F1 43.90%, Weighted-F1 61.24%, Ordinal MAE 0.5013.

**Three-class test results:** Accuracy 79.45%, Macro-F1 61.44%, Weighted-F1 80.74%.

- [B3 notebook](B3/B3_notebook.ipynb)
- [B3 report](B3/report/70177771_B3_Report.pdf)
- [B3 dataset instructions](B3/data/README.md)

The B3 dataset CSV is not included in this repository. See the dataset instructions for how to obtain it.

## Repository Structure

```text
AI101-ML-Assignment-70177771/
│
├── A1/
│   ├── data/
│   ├── figures/
│   ├── report/
│   │   └── 70177771_A1_Report.pdf
│   └── A1_notebook.ipynb
│
├── B3/
│   ├── data/
│   │   └── README.md
│   ├── figures/
│   ├── report/
│   │   └── 70177771_B3_Report.pdf
│   └── B3_notebook.ipynb
│
├── README.md
├── requirements.txt
├── AI_DISCLOSURE.md
└── .gitignore
```

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- LightGBM
```

Commit summary:

```text
Update README with A1 and B3 details
```
