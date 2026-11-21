"""
文件改名
题目： 在上一题的基础上，随机将50个文件改名为.jpg结尾。
"""

import pathlib as pl
import random as rd

img = pl.Path("img")
list = list(img.glob("*.png"))

rd.shuffle(list)

for i in range(50):
    old = list[i]
    new = old.with_suffix(".jpg")
    old.rename(new)