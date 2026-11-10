# 第四题：创建顺序文件
#
# 题目：在当前 .py 文件目录新建目录 img，里面包含 100 个文件，
#       100 个文件名各不相同（例如 X4G5.png）。
from pathlib import Path
p=Path(__file__).resolve().parent/"img"
p.mkdir(exist_ok=True)
for i in range(1,101):
    wen=p/f"{i:03d}.png"
    wen.touch()

