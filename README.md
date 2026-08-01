# LEGO Brick Color Detector

A YOLO model trained to detect LEGO bricks and count how many of each colour.

## For students: how to run it in VS Code (no Colab account needed)

**Requirements:** Python 3.9+ and VS Code already installed on your computer.

1. Click this button — it opens VS Code and clones the repo for you automatically (VS Code will ask you to pick a folder to clone into, then open it):

   [![Open in VS Code](https://img.shields.io/badge/Open%20in-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)](vscode://vscode.git/clone?url=https://github.com/otho560/lego-detector.git)

   If the button doesn't do anything (some browsers block custom protocol links), clone it yourself instead:
   ```
   git clone https://github.com/otho560/lego-detector.git
   ```
   then open the `lego-detector` folder in VS Code (File → Open Folder).

2. VS Code will pop up a notification asking to install the recommended **Python extension** — click Install (only needed the first time).

3. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) → type **Run Task** → choose:
   **"1) Setup (install dependencies)"** — installs `ultralytics` and `matplotlib`. Only needed once.

4. Run the detector — either:
   - Press **F5**, or
   - Command Palette → **Run Task** → **"2) Run LEGO Detector"**

5. A file picker window pops up — choose a photo of LEGO bricks. A window will show the photo with bounding boxes drawn around each brick, and the counts per color are printed in the terminal.

> Every time you want to test a new photo, just run step 4 again.

## Alternative: Google Colab (no local install needed)

1. Click the badge below (or open `Lego_Predict_1.ipynb` in GitHub and click "Open in Colab").

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/otho560/lego-detector/blob/main/Lego_Predict_1.ipynb)

2. In Colab: **Runtime → Run all**.
3. When the file picker pops up at the bottom, upload a photo of LEGO bricks.
4. You'll see the photo with bounding boxes drawn around each brick, plus a printed count per color.

## Repo contents

- `predict.py` — run this in VS Code to detect bricks in a local photo (opens a file picker, shows the annotated image, prints counts).
- `Lego_Predict_1.ipynb` — the notebook version, for running in Colab.
- `.vscode/` — task/launch/extension config so VS Code setup and running is one click.
- `models/lego_model.pt` — the trained YOLO model (weights only, used for inference).
- `dataset/` — training images + labels, kept here for reproducibility/reference. Not needed to run predictions.
- `requirements.txt` — Python dependencies (`ultralytics`, `matplotlib`).
