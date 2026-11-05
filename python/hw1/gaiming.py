from pathlib import Path
import random

files = list(Path("img").glob("*.png"))
for p in random.sample(files, 50):
    p.rename(p.with_suffix(".jpg"))