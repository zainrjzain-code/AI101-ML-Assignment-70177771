# Dataset Guide: Task A1 (Breast Cancer Diagnosis)

## Dataset Overview
- **Name:** Breast Cancer Wisconsin (Diagnostic)
- **Source:** UCI Machine Learning Repository (Dataset ID: 17) / `sklearn.datasets.load_breast_cancer`
- **Reference:** W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction for breast tumor diagnosis. IS&T/SPIE 1993.
- **License:** Open Database License (ODbL) / Public Domain

## Dataset Dimensions & Target
- **Total Samples:** 569 instances
- **Input Features:** 30 continuous real-valued features computed from digitized images of Fine Needle Aspirate (FNA) of breast masses.
- **Target Variable:** Binary classification:
  - `0`: Malignant (212 samples, ~37.3%)
  - `1`: Benign (357 samples, ~62.7%)

## Feature Structure
Ten core morphological characteristics of cell nuclei are measured:
1. `radius` (mean of distances from center to points on the perimeter)
2. `texture` (standard deviation of gray-scale values)
3. `perimeter`
4. `area`
5. `smoothness` (local variation in radius lengths)
6. `compactness` (perimeter^2 / area - 1.0)
7. `concavity` (severity of concave portions of the contour)
8. `concave points` (number of concave portions of the contour)
9. `symmetry`
10. `fractal dimension` ("coastline approximation" - 1)

For each image, the **Mean**, **Standard Error (SE)**, and **"Worst" (mean of the three largest values)** are recorded, yielding $10 \times 3 = 30$ numeric features.

## How to Access & Load
The dataset is built directly into scikit-learn and can be fetched programmatically with zero manual download:

```python
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target
```

Alternatively, via `ucimlrepo`:
```python
from ucimlrepo import fetch_ucirepo
cancer = fetch_ucirepo(id=17)
X = cancer.data.features
y = cancer.data.targets
```

## Data Hygiene & Leakage Prevention
- **Splitting:** Stratified 80/20 train/test partition using a fixed random seed (`random_state=42`).
- **Pipeline Scaling:** Feature scaling (`StandardScaler`) is enclosed strictly inside `sklearn.pipeline.Pipeline` and fitted exclusively on training instances.
- **No Test Peeking:** The test set is evaluated once only for final metrics verification.
