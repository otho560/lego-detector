# LEGO Brick Color Detector

A YOLO model trained to detect LEGO bricks and count how many of each colour.

## For students: how to run it (no account, no sign-in, no install)

1. Click this button:

   [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/otho560/lego-detector/HEAD?filepath=Lego_Predict_Binder.ipynb)

2. Wait for it to load. **The first time, this can take several minutes** — it's building a full Python environment from scratch in the background (a progress log will scroll by). After the first launch, it's cached and loads much faster for everyone.

3. Once the notebook opens in your browser: menu bar → **Run → Run All Cells**.

4. An **"Upload photo" button** appears below the last cell. Click it, choose a photo of LEGO bricks from your computer.

5. The photo appears automatically with boxes drawn around each brick, plus the count per color printed underneath — right there in the browser, no download or extra steps.

> To try another photo, just click the upload button again and pick a new one.

**Nothing to sign in with, nothing to install** — this works on any computer with a web browser.

## Alternative: Google Colab (for anyone who has a Google account and wants faster startup)

1. Click the badge below (or open `Lego_Predict_1.ipynb` in GitHub and click "Open in Colab").

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/otho560/lego-detector/blob/main/Lego_Predict_1.ipynb)

2. In Colab: **Runtime → Run all**.
3. When the file picker pops up at the bottom, upload a photo of LEGO bricks.
4. You'll see the photo with bounding boxes drawn around each brick, plus a printed count per color.

## Repo contents

- `Lego_Predict_Binder.ipynb` — the notebook to run via Binder (no account needed, upload button instead of Colab's file picker).
- `Lego_Predict_1.ipynb` — the Colab version.
- `models/lego_model.pt` — the trained YOLO model (weights only, used for inference).
- `dataset/` — training images + labels, kept here for reproducibility/reference. Not needed to run predictions.
- `requirements.txt` — Python dependencies Binder uses to build the environment (`ultralytics`, `matplotlib`, `ipywidgets`).

## Instructor note

Before sharing with the class, launch the Binder link yourself once from a **private/incognito browser window** to (a) warm the build cache so students' launches are fast, and (b) confirm the upload → detect → display flow works end to end.
