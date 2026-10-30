import random
from pathlib import Path

i = int(input("请输入文件数："))
j = int(input("请输入每个文件的行数："))
folder = Path("test")
folder.mkdir(exist_ok=True)

for n in range(i):
    with open(folder / f"{n + 1}.txt", "w") as file:
        for m in range(j):
            file.write("".join(chr(random.randint(32, 126)) for k in range(100)) + "\n")

for path in list(folder.iterdir()):
    if path.is_file():
        with open(path, "r") as file:
            lines = file.readlines()
        with open(path, "w") as file:
            for line in lines:
                file.write(line.rstrip("\n") + "-python\n")
        path.rename(path.with_name(path.name + "-python"))
