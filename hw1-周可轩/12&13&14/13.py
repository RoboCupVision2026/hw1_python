"""
文件修改
题目： 读取上述test.txt的文件内容，分别在文件的开头和结尾处追加字符串 python。
"""

import pathlib as pl

#path = pl.Path.cwd() / "test.txt"
path = pl.Path(__file__).resolve().parent / "test.txt"

with path.open("r", encoding = "ascii") as f:
    now = f.read()

with path.open("w", encoding = "ascii") as f:
    f.write("python" + now + "python")