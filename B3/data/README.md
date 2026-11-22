# Dataset Guide: Task B3 (Women's E-Commerce Clothing Reviews)

## Dataset Overview
- **Name:** Women's E-Commerce Clothing Reviews
- **Source:** Kaggle (`nicapotato/womens-ecommerce-clothing-reviews`)
- **License:** CC0 Public Domain
- **Size & Shape:** 23,486 customer reviews $\times$ 10 tabular columns

## Feature Schema
| Column Name | Data Type | Description | Role in Modeling |
| :--- | :--- | :--- | :--- |
| `Clothing ID` | Integer | Categorical product identifier | Dropped (high cardinality) |
| `Age` | Integer | Reviewer age in years | Numeric predictor |
| `Title` | String | Review headline | Text feature (concatenated) |
| `Review Text` | String | Detailed body of feedback | Text feature (TF-IDF) |
| `Rating` | Integer (1–5) | Customer satisfaction score | **Target Variable** |
| `Recommended IND` | Binary (0/1) | Whether reviewer recommends product | **LEAKAGE: MUST DROP** |
| `Positive Feedback Count` | Integer | Upvotes received by the review | Numeric feature: $\\log(1 + x)$ |
| `Division Name` | Categorical | High-level product division | One-Hot Encoded |
| `Department Name` | Categorical | Store department (e.g., Tops, Dresses) | One-Hot Encoded |
| `Class Name` | Categorical | Detailed garment category | One-Hot Encoded |

##  Critical Data Leakage Rule
As specified in the assignment prompt:
> **Leakage rule:** Do not use the column `Recommended IND` as an input. The same customer fills it in at the same moment as the rating, so it would not be available when you need the prediction.

This column is strictly dropped during data ingestion before any splitting or preprocessing.

## How to Download
To comply with the assignment policy against committing large data files to GitHub, download the dataset directly from Kaggle:

### Option 1: Kaggle CLI
```bash
kaggle datasets download -d nicapotato/womens-ecommerce-clothing-reviews -p data/ --unzip
```

### Option 2: Web Browser
1. Visit https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews
2. Download `Womens Clothing E-Commerce Reviews.csv`
3. Place the CSV file into `B3/data/` or reference it from your Colab runtime.

## Preprocessing & Data Splits
- **Rows without text:** Rows with empty review text are dropped (leaving 22,641 reviews).
- **Text merging:** `Title` and `Review Text` are concatenated into a single rich text representation.
- **Split Strategy:** Stratified 70/15/15 train/validation/test split using a fixed random seed (`random_state=42`).
- **Feature Pipeline:** `ColumnTransformer` with `TfidfVectorizer` (unigrams + bigrams), `StandardScaler` for numeric columns, and `OneHotEncoder` for categorical categories. Fitted strictly on training instances.
