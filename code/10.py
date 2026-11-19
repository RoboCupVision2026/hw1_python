# 文件改名
import random
from pathlib import Path

img = Path(__file__).resolve().parent / "img"

files = list(img.glob("*.png"))

selected = random.sample(files, 50)

for file in selected:
    file.rename(file.with_suffix(".jpg"))