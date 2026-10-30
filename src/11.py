import random
from pathlib import Path

folder = Path(__file__).resolve().parent / "img"
files = list(folder.glob("*.png"))

for file in random.sample(files, 50):
    file.rename(file.with_suffix(".jpg"))
