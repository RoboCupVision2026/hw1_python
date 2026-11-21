"""
创建顺序文件
题目： 在当前.py文件目录新建目录img，里面包含100个文件，100个文件名各不相同。（X4G5.png）
程序分析： Python的pathlib库和Python的os库都提供了文件路径相关的函数和类。
"""

import pathlib as pl

img = pl.Path("img")
img.mkdir()

for i in range (100):
    file_name = f"{i + 1}X4G5.png"
    file_path = img / file_name
    file_path.touch()