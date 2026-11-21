"""
文件对比
题目： 读取“test.text”和“copy_test.txt”内容，检查他们的每一行内容是否相同，输出所有不同的行的编号。
"""

import pathlib as pl
import itertools as it

path1 = pl.Path(__file__).resolve().parent / "test.txt"
path2 = pl.Path(__file__).resolve().parent / "copy_test.txt"

with path1.open("r", encoding = "ascii") as f1:
    with path2.open("r", encoding = "ascii") as f2:
        for i, (line1, line2) in enumerate(it.zip_longest(f1, f2)):
            if line1 != line2:
                print(f"第{i + 1}行不同")