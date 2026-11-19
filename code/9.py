# 创建顺序文件
import random
import string
from pathlib import Path

root = Path(__file__).resolve().parent

img = root / "img"
img.mkdir(exist_ok = True)
names = set()
N = 100

while len(names) < N:
    name = "".join(random.choices(
        string.ascii_uppercase + string.digits, k = 4
    )) + ".png"

    if name not in names and not (img / name).exists():
        names.add(name)
        (img / name).touch()