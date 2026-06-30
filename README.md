# LEGO Brick Color Detector

A YOLO model trained to detect LEGO brick and count of each colour.

## For students: how to run it (no setup needed)

1. Click the badge below (or open `Lego_Predict_1.ipynb` in GitHub and click "Open in Colab").

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/otho560/lego-detector/blob/main/Lego_Predict_1.ipynb)

2. In Colab: **Runtime → Run all**.
3. When the file picker pops up at the bottom, upload a photo of LEGO bricks.
4. You'll see the photo with bounding boxes drawn around each brick, plus a printed count per color.


## Repo contents

- `Lego_Predict_1.ipynb` — the notebook to run.
- `models/lego_model.pt` — the trained YOLO model (weights only, used for inference).
- `dataset/` — training images + labels, kept here for reproducibility/reference. Not needed to run predictions.
- `requirements.txt` — Python dependencies (mainly `ultralytics`), for anyone running outside Colab.


