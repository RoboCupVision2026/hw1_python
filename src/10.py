# 创建顺序文件
import random
from pathlib import Path

folder = Path(__file__).resolve().parent / "img"
folder.mkdir(exist_ok=True)

for _ in range(100):
    while True:
        name = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
        file = folder / (name + ".png")
        if not file.exists():
            file.touch()
            break
