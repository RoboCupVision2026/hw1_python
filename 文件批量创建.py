import random
import string
from pathlib import Path

folder = Path("test")
folder.mkdir(exist_ok=True)

n = int(input("请输入文件数量："))
m = int(input("请输入每个文件的随机字符数量："))

chars = string.ascii_letters + string.digits

for i in range(n):
    name = input("请输入第" + str(i + 1) + "个文件名：")

    file = folder / name

    content = "".join(random.choices(chars, k=m))

    with open(file, "w") as f:
        f.write(content + "\n")

for file in folder.iterdir():
    if file.is_file():
        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            for line in lines:
                f.write(line.rstrip("\r\n") + "-python\n")

print("所有文件处理完成")