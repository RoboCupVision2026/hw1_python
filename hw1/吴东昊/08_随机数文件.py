from pathlib import Path
from random import randint
p=Path(__file__).resolve().parent/"data.txt"
with p.open("w",encoding="utf-8") as f:
    for i in range(100000):
        f.write(str(randint(1,100))+"\n")
