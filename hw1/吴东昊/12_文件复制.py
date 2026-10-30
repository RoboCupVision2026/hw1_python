from pathlib import Path
from random import randint
p=Path(__file__).resolve().parent
n=int(input("行数："))
with (p/"test.txt").open("w",encoding="utf-8") as f:
    for i in range(n):
        f.write("".join(chr(randint(32,126)) for j in range(20))+"\n")
with (p/"test.txt").open(encoding="utf-8") as f,(p/"copy_test.txt").open("w",encoding="utf-8") as g:
    g.write(f.read())
