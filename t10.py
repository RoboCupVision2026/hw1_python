# 第五题：文件改名
import random
from pathlib import Path

base_dir = Path(__file__).resolve().parent
img_dir = base_dir/"img"

files=list(img_dir.glob("*.png"))
selected_files=random.sample(files,50)

for selected_file in selected_files:
    new_file=selected_file.with_suffix(".jpg")
    selected_file.rename(new_file)