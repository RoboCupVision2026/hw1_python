"""
文件复制
题目： 在工作目录下写程序创建一个文件（test.txt）并随机生成（由用户指定）行内容（包含ASCII标准的任意非控制字符）。写程序实现该文件的拷贝，拷贝文件文件名为copy_test.txt
"""

import random as rd
import pathlib as pl

rows = int(input("行数："))

path1 = pl.Path.cwd() / "test.txt"
path2 = pl.Path.cwd() / "copy_test.txt"

with path1.open("w", encoding = "ascii") as f:
    for i in range(rows):
        line = ""
        for j in range(20):
            line += chr(rd.randint(32, 126))
        f.write(line + "\n")

with path1.open("r", encoding="ascii") as f1:
    with path2.open("w", encoding="ascii") as f2:
        for line in f1:
            f2.write(line)