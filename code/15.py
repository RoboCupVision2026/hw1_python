# 文件批量创建
from pathlib import Path
import random
import string

folder = Path("test")
folder.mkdir(exist_ok = True)

n = int(input())
m = int(input())

for i in range(n):
    name = "test" + str(i + 1) + ".txt";
    path = folder / name
    with path.open("w") as f:
        for j in range(m):
            s = "".join(random.choices(string.ascii_letters, k = 10))
            print(s, file = f)

for path in folder.iterdir():
    if path.is_file():
        lines = path.read_text().splitlines()
        content = "\n".join(line + "-python" for line in lines)
        if lines:
            content += "\n"
        path.write_text(content)
        path.rename(path.with_name(path.name + "-python"))