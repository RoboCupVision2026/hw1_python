import random
import string
from pathlib import Path

folder = Path(__file__).resolve().parent / "img"
folder.mkdir(exist_ok=True)

while len(list(folder.glob("*.png"))) < 100:
    name = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=4
    ))

    file = folder / (name + ".png")

    if not file.exists():
        file.touch()

print("100个文件创建完成")