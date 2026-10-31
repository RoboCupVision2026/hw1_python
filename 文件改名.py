import random
from pathlib import Path

folder = Path(__file__).resolve().parent / "img"

files = list(folder.glob("*.png"))

selected = random.sample(files, 50)

for file in selected:
    new_file = file.with_suffix(".jpg")
    file.rename(new_file)

print("50个文件改名完成")