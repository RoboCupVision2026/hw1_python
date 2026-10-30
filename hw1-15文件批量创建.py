import os
import random
import string

i = int(input("请输入要创建的文件数量: "))
j = int(input("请输入每个文件的行数: "))

dirname = "test"
os.makedirs(dirname, exist_ok=True)

for k in range(i):
    filename = f"file_{k + 1}.txt"
    filepath = os.path.join(dirname, filename)

    with open(filepath, "w") as f:
        for l in range(j):
            randomstring = ''.join(random.choices(string.ascii_letters, k=10))
            f.write(randomstring + "\n")

for filename in os.listdir(dirname):
    old_filepath = os.path.join(dirname, filename)

    if os.path.isfile(old_filepath):
        name, ext = os.path.splitext(filename)
        new_filepath = os.path.join(dirname, f"{name}-python{ext}")
        os.rename(old_filepath, new_filepath)

    with open(new_filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(new_filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + "-python\n")