"""
LEGO Brick Color Detector — local / VS Code version

How to run:
  1. Open this folder in VS Code.
  2. Terminal -> Run Task -> "1) Setup (install dependencies)"   (only once)
  3. Press F5, or Terminal -> Run Task -> "2) Run LEGO Detector"
  4. A file picker window will pop up — choose a photo of LEGO bricks.
  5. A window shows the photo with boxes drawn, and counts are printed
     in the terminal.
"""

import os
from collections import Counter

from ultralytics import YOLO
import matplotlib.pyplot as plt

# Path to the trained model, relative to this file (works no matter
# which folder VS Code was launched from).
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "lego_model.pt")


def pick_image():
    """Open a native file picker so students can choose a photo (this
    replaces Colab's files.upload(), which only works inside Colab)."""
    from tkinter import Tk, filedialog

    root = Tk()
    root.withdraw()          # don't show the empty tkinter window
    root.attributes("-topmost", True)
    path = filedialog.askopenfilename(
        title="Choose a photo of LEGO bricks",
        filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")],
    )
    root.destroy()
    return path


def count_legos(model, image_path, conf=0.5):
    results = model(image_path, conf=conf, verbose=False)
    r = results[0]
    counts = Counter(r.names[int(c)] for c in r.boxes.cls.tolist())
    total = sum(counts.values())

    plt.figure(figsize=(10, 10))
    plt.imshow(r.plot()[..., ::-1])
    plt.axis("off")
    title = f"Total: {total}  |  " + "  ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
    plt.title(title, fontsize=12)
    plt.show()

    print("\n=== LEGO Count ===")
    print(f"Total bricks: {total}")
    for color, n in sorted(counts.items()):
        print(f"  {color:8s}: {n}")
    return dict(counts)


def main():
    print("Loading model...")
    model = YOLO(MODEL_PATH)
    print(f"Model loaded. Classes: {model.names}\n")

    image_path = pick_image()
    if not image_path:
        print("No image selected. Exiting.")
        return

    print(f"Running detection on: {image_path}")
    count_legos(model, image_path)


if __name__ == "__main__":
    main()
