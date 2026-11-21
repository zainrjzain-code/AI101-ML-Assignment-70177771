# A2: Predicting Concrete Compressive Strength

**Student:** Muhammad Zain-ul-Abideen  
**Roll Number:** 70177771  
**Section:** B  
**Course:** Introduction to Artificial Intelligence (AI-101)  
**Task Pool:** Pool A (Numerical Modality)  

---

## Assignment Deliverables

- `A2_notebook.ipynb` — Complete, executed Google Colab / Jupyter notebook containing all EDA, feature engineering, cross-validation tuning, diagnostic plots, and markdown explanations.
- `report/70177771_A2_Report.pdf` — Two-page double-column scientific report formatted according to IEEE standards.
- `report/make_a2_report.py` — Python script used to compile the IEEE-style report PDF.
- `figures/` — High-resolution diagnostic figures (EDA distributions, Pearson correlation matrix, bivariate scatter plots, predicted vs. actual, residual diagnostics, and permutation feature importance).
- `data/README.md` — Dataset description, provenance, and download instructions.

---

## Task Summary

This task predicts concrete compressive strength (in MPa) from mixture component formulations and sample curing age.

- **Models Evaluated:** Linear Regression (baseline), Polynomial + Ridge Regression, Random Forest Regressor, Gradient Boosting Regressor, and Multi-Layer Perceptron (MLPRegressor).
- **Domain Feature Engineering:** Water-to-Cement Ratio ($w/c$, Abrams' Law) and $\log(\text{Age})$ (logarithmic curing curve).
- **Best Performing Model:** Gradient Boosting Regressor ($R^2 = 0.9277$, $\text{RMSE} = 4.31\text{ MPa}$, $\text{MAE} = 2.85\text{ MPa}$, 5-Fold CV $\text{RMSE} = 4.69 \pm 0.37\text{ MPa}$).
- **Feature Engineering Impact:** Improved baseline Linear Regression $R^2$ from $0.6276$ to $0.8329$ (+20.5% explained variance).
