# Dataset Guide: Task C3 (Image Captioning with Flickr8k)

## Dataset Overview
- **Name:** Flickr8k Image-Caption Benchmark Dataset
- **Source:** Kaggle (`adityajn105/flickr8k`) / Common Academic Benchmark (Hodosh et al., JAIR 2013)
- **License:** CC BY-NC-SA 4.0 / Academic Use
- **Size & Shape:** 8,091 real-world photographic images $\times$ 5 reference captions per image ($40,455$ captions total)

## Data Split Strategy (Zero-Leakage Splitting)
To avoid severe visual data leakage, **splits must be performed strictly by image identifier**, ensuring that all 5 captions describing a specific image reside within the same data split:

| Split | Number of Images | Number of Captions | Purpose |
| :--- | :--- | :--- | :--- |
| **Train** | 6,000 | 30,000 | Representation learning & teacher-forced training |
| **Validation** | 1,000 | 5,000 | Early stopping & hyperparameter tuning |
| **Test** | 1,091 | 5,455 | Final evaluation across corpus BLEU-1 to BLEU-4 |

## How to Download
To comply with the assignment policy against committing large binary media (> 50 MB) to GitHub:

### Option 1: Kaggle CLI
```bash
kaggle datasets download -d adityajn105/flickr8k -p data/ --unzip
```

### Option 2: Web Browser
1. Visit https://www.kaggle.com/datasets/adityajn105/flickr8k
2. Download the archive containing `Images/` and `captions.txt`.
3. Unzip into `C3/data/` or attach the dataset directly in Google Colab / Kaggle Notebooks via *Add Input*.

## Text Preprocessing & Vocabulary
1. **Cleaning:** Lowercasing, punctuation stripping, and whitespace normalization.
2. **Special Tokens:** Prefixing `<start>` and suffixing `<end>` to mark sentence boundaries.
3. **Vocabulary Thresholding:** Words occurring fewer than 5 times in the training partition are replaced with `<unk>` to reduce sparsity and control decoder dimension.

## Feature Extraction & CNN Backbone
Images are resized to $224 \times 224$ (or $299 \times 299$) and processed through frozen ImageNet-pretrained CNN backbones:
- **ResNet-50:** Features extracted prior to final classification layer (2,048-dimensional feature vector).
- **EfficientNet-B0 / InceptionV3:** 1,280-dimensional or 2,048-dimensional visual embeddings.
Extracted feature tensors are cached to disk to accelerate LSTM training cycles.
