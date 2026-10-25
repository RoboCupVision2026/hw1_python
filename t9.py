# 第四题：创建顺序文件
import os
import string
import random
from pathlib import Path

chars = string.ascii_letters+string.digits

fileDirPath = Path(__file__).resolve().parent / "img"
fileDirPath.mkdir(exist_ok=True)

filenames = set()
while (len(filenames) < 100):
    filename = "".join(random.choices(chars, k=4))
    filenames.add(filename)

for filename in filenames:
    file = fileDirPath/(filename+".png")
    file.touch()
