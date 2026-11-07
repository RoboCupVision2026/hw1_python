from pathlib import Path
from random import sample

images=Path(__file__).resolve().parent/"img"
files=sorted(images.glob("*.png"))
chosen_files=sample(files,50)
for file in chosen_files:
    new_name=file.with_suffix(".jpg")
    file.rename(new_name)