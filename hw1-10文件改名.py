import random
from pathlib import Path

img_dir = Path("img")

png_files = list(img_dir.glob("*.png"))

files_to_rename = random.sample(png_files, 50)

for file_path in files_to_rename:
    new_path = file_path.with_suffix(".jpg")
    file_path.rename(new_path)