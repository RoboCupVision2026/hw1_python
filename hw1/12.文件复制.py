from pathlib import Path
from random import randint

base=Path(__file__).resolve().parent
i=int(input())
with open(base/"test.txt","w") as p:
    for num in range(i):
        p.write(chr(randint(32,126))+"\n")
path=base/"copy_test.txt"
path.write_text((base/"test.txt").read_text())