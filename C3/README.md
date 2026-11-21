# Task C3 — Image Captioning

This task implements an image captioning system using a CNN encoder and an LSTM decoder on the Flickr8k dataset.

## Contents

- `C3_Image_Captioning.ipynb` — Complete executed notebook
- `report/` — Final task report
- `figures/` — Generated plots and qualitative examples
- `data/` — Dataset download instructions

## Models

- ResNet50 + LSTM
- EfficientNet-B0 + LSTM

## Evaluation

Models are evaluated using BLEU-1, BLEU-2, BLEU-3 and BLEU-4 with greedy and beam search decoding.
