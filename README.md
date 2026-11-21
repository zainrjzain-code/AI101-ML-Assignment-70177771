# AI101 - Machine Learning Assignment

This repository contains my AI101 machine learning assignment work. Each task has its own folder with its notebook, report, figures, and dataset instructions.

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

**Models:** Logistic Regression, Linear SVM, Random Forest, and LightGBM, compared with and without balanced class weights.

**Features:** TF-IDF review text, age, log positive-feedback count, review length, and product categories. `Recommended IND` was excluded to prevent data leakage.

**Selected model:** LightGBM with balanced class weights, selected using validation Macro-F1.

**Five-class test results:** Accuracy 60.55%, Macro-F1 43.90%, Weighted-F1 61.24%, Ordinal MAE 0.5013.

**Three-class test results:** Accuracy 79.45%, Macro-F1 61.44%, Weighted-F1 80.74%.

- [B3 notebook](B3/B3_notebook.ipynb)
- [B3 report](B3/report/70177771_B3_Report.pdf)
- [B3 dataset instructions](B3/data/README.md)

The B3 dataset CSV is not included in this repository. See the dataset instructions for how to obtain it.

### C3 - Image Captioning Using CNN and LSTM

This task develops an image captioning system that generates natural-language descriptions for images using the Flickr8k dataset.

**Dataset:** Flickr8k, containing 8,091 images with five human-written captions per image.

**Models:**
- ResNet50 + LSTM
- EfficientNet-B0 + LSTM

**Methodology:** Image feature extraction using frozen ImageNet-pretrained CNN encoders, feature caching, caption preprocessing, vocabulary construction, and an LSTM-based decoder.

**Evaluation:** Both models were evaluated using BLEU-1, BLEU-2, BLEU-3, and BLEU-4 with Greedy Search and Beam Search (k=3 and k=5).

**Best configuration:** EfficientNet-B0 with Beam Search (k=5).

**Best test BLEU scores:**
- BLEU-1: 60.81%
- BLEU-2: 41.89%
- BLEU-3: 28.05%
- BLEU-4: 18.79%

**Comparison:** EfficientNet-B0 achieved better BLEU scores than ResNet50 across the evaluated decoding configurations.

- [C3 notebook](C3/C3_Image_Captioning.ipynb)
- [C3 report](C3/report/70177771_C3_Report.pdf)
- [C3 dataset instructions](C3/data/README.md)
- [C3 figures](C3/figures/)

The Flickr8k dataset and large model files are not included in this repository. See the dataset instructions for how to obtain the dataset.

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
├── C3/
│   ├── data/
│   │   └── README.md
│   ├── figures/
│   ├── report/
│   │   └── 70177771_C3_Report.pdf
│   ├── C3_Image_Captioning.ipynb
│   └── README.md
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
- PyTorch
- Torchvision
- NLTK
- Pillow
- Jupyter Notebook

## General Notes

- Each task has a separate notebook and report.
- Dataset files and large model checkpoints are not included in the repository.
- Dataset download instructions are provided inside each task's `data/` folder.
- Required Python packages are listed in `requirements.txt`.
- AI assistance is documented in `AI_DISCLOSURE.md`.
