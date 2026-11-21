# Task B2: Predicting Wine Critic Scores from Tasting Notes and Metadata

**Author:** Muhammad Zain-ul-Abideen  
**Roll Number:** 70177771  
**Section:** B  
**Course:** AI-101 (Introduction to Artificial Intelligence), The University of Lahore  
**Instructor:** Dr. Muhammad Awais  

---

## 1. Project Overview

This project implements mixed-modality regression models that integrate structured metadata (price, country, province, variety, winery, taster) and natural language processing of sommelier tasting notes to predict continuous critic ratings (points 80–100) from the Wine Enthusiast dataset.

- **Raw Reviews:** 129,971
- **Removed Duplicate Reviews:** 10,016 (7.71%)
- **Clean Unique Reviews:** 119,955
- **Target Points Range:** 80 to 100 (Mean: 88.44 ± 3.09 points)

---

## 2. Experimental Setup

- **Mandatory De-duplication:** All exact duplicate descriptions were eliminated prior to partitioning to prevent direct train-test leakage.
- **Dataset Split:** 80% Train (95,963 reviews), 10% Validation (11,996 reviews), and 10% Test (11,996 reviews).
- **Leakage Prevention:** Median price ($25.00), feature scalers, categorical encoders, and TF-IDF vocabulary (15,000 unigrams and bigrams) were fitted strictly on the training partition only.
- **Evaluation Metrics:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² (Coefficient of Determination).

---

## 3. Benchmark Results on Held-out Test Set (11,996 reviews)

| Model Architecture | Test MAE | Test RMSE | Test R² Score | Performance Summary |
|---|:---:|:---:|:---:|---|
| **Ridge Regression (α=5.0) [WINNER]** | **1.164** | **1.476** | **0.7689 (76.9%)** | Explains 76.9% of critic rating variance |
| SGDRegressor (Squared Error) | 1.255 | 1.596 | 0.7300 (73.0%) | Linear gradient descent regressor |
| Mean Baseline (Dummy Regressor) | 2.522 | 3.070 | -0.0000 | Predicts population training mean (88.44) |

---

## 4. Mandatory Modality Ablation Study

| Modality Setting | Test MAE | Test RMSE | Test R² Score | R² Improvement |
|---|:---:|:---:|:---:|:---:|
| **Metadata Only (Price + Origin + Length)** | 1.572 | 1.990 | 0.5800 | Baseline |
| **Text Only (TF-IDF Tasting Notes)** | 1.351 | 1.715 | 0.6879 | +10.79% over Metadata |
| **Combined (Metadata + Text)** | **1.164** | **1.476** | **0.7689** | **+18.89% over Metadata!** |

**Finding:** Tasting notes add **+18.89% explained variance** beyond price and origin metadata, reducing average prediction error by 0.408 points per bottle.

---

## 5. Performance per Points Band & Regression to the Mean

| Points Band | Test Reviews | Percentage | Test MAE (Points) | Trend Analysis |
|---|:---:|:---:|:---:|---|
| **80–84 (Lower Tier)** | 1,164 | 9.7% | 1.441 | Moderately high error |
| **85–89 (Median Band)** | 6,283 | 52.4% | **1.027** | **Best predicted band** (closest to population mean) |
| **90–94 (Excellent Tier)** | 4,301 | 35.9% | 1.239 | Low error |
| **95–100 (Classic Tier)** | 248 | 2.1% | **2.048** | **Highest error** (L2 shrinkage toward mean) |

---

## 6. Answers to Assignment Questions

### Question 1: How much does the tasting note add beyond price and origin?
Adding natural language tasting notes boosts explained variance from **58.00% to 76.89% (+18.89% absolute gain)** and lowers test MAE by 0.408 points per bottle. Sensory descriptors capture structural balance, oak integration, and palate concentration that price tags cannot convey.

### Question 2: Which words push predicted scores up or down (Ridge coefficients)?
- **Positive Descriptors (Pushing Scores UP):** `layered`, `seamless`, `cellar`, `long finish`, `opulent`, `velvety`, `complex`, `magnificent`.
- **Negative Descriptors (Pushing Scores DOWN):** `simple`, `sour`, `green`, `dilute`, `unripe`, `thin`, `harsh`, `watery`.

### Question 3: Why are the extremes (80–82 and 95+) predicted worst? Explain regression to the mean.
Ratings heavily cluster near 88.44 points. Ridge regression applies an L2 penalty ($\lambda \sum w_j^2$) that shrinks coefficients toward zero to minimize total squared error across the majority distribution. Consequently, extreme high ratings are underpredicted and extreme low ratings are overpredicted, pulling predictions toward the population mean.

### Question 4: What would have happened to your test score without de-duplication, and why?
The raw file contains **10,016 exact duplicate reviews**. Without de-duplication, identical reviews would be shared between training and test sets, causing direct data leakage. The model would memorize exact phrases, resulting in artificially inflated test R² and deflated test MAE that fail completely when deployed on unseen wine vintages.

---

## 7. Folder Contents

- `B2_notebook.ipynb`: Executed Google Colab / Jupyter notebook containing all code, tables, and embedded plots.
- `report/70177771_B2_Report.pdf`: 2-page double-column IEEE report.
- `Task_B2_Complete_Project_Guide_Roman_Urdu.pdf`: Complete step-by-step project guide and viva handbook in Roman Urdu and simple English.
- `figures/`: High-resolution figures generated during EDA, modeling, and ablation.
- `data/README.md`: Instructions for downloading and placing the dataset.
