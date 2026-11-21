"""
文件批量创建
题目： 在当前目录下新建test目录，在test目录中自建（由用户指定）个以上文件，向文件中随机输入（由用户指定）行随机字符，然后遍历该目录下的所有文件，并在所有文件名称和每一个文件的所有行后面增加-python。
"""

import random as rd
import pathlib as pl

path = pl.Path(__file__).resolve().parent / "test"
path.mkdir()

num = int(input("文件个数："))

for i in range(num):
    path1 = path / f"test{i + 1}.txt"
    rows = int(input(f"文件test{i + 1}.txt的行数："))
    with path1.open("w", encoding = "ascii") as f:
        for j in range(rows):
            line = ""
            len = rd.randint(10, 30)
            for k in range(len):
                line += chr(rd.randint(32, 126))
            f.write(line + "\n")

for file in path.iterdir():
    if file.is_file():
        with file.open("r", encoding = "ascii") as f:
            lines = f.readlines()

        with file.open("w", encoding = "ascii") as f:
            for now in lines:
                f.write(now.rstrip("\n") + "-python\n")

        new_name = f"{file.stem}-python{file.suffix}"
        file.rename(file.with_name(new_name))