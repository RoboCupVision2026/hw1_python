"""
文件输入
题目： 自行制作一个10行3列文件，每列内容为随机数，以逗号作为分割符，写程序输出第二列的最大值、最小值、平均值、中位数。
"""

import random as rd
import statistics as st
import pathlib as pl

file = pl.Path("num.csv")
with open(file, "w") as f:
    for i in range(10):
        f.write(f"{rd.randint(1, 100)}, {rd.randint(1, 100)}, {rd.randint(1, 100)}\n")

sec = []

with open(file, "r") as f:
    for i in f:
        col = i.split(",")
        sec.append(int(col[1]))

print(f"最大值: {max(sec)}")
print(f"最小值: {min(sec)}")
print(f"平均值: {st.mean(sec)}")
print(f"中位数: {st.median(sec)}")