# 第四题：文件对比
import os
from itertools import zip_longest

with open("test.txt", "r", encoding="utf-8") as f:
    lines1 = f.readlines()

with open("copy_test.txt", "r", encoding="utf-8") as f:
    lines2 = f.readlines()

for i, (line1, line2) in enumerate(zip_longest(lines1, lines2), start=1):
    if line1 != line2:
        print(f"第{i}行不同")
