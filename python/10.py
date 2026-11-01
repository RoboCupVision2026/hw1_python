from pathlib import Path
import random

if __name__ == "__main__":
    img_dir = Path("img")
    png_files = list(img_dir.glob("*.png"))
    selected = random.sample(png_files, k=50)

    for f in selected:
        new_path = f.with_suffix(".jpg")
        f.rename(new_path)
