from pathlib import Path
from os import makedirs
from random import randint

images=Path(__file__).resolve().parent/"img"
makedirs(images, exist_ok=True)
names=set()
while len(names)<100:
    s=""
    for j in range(4):
        c=randint(0,35)
        if c>9:
            c=chr(ord('A')+c-10)
        s+=str(c)
    names.add(s)
for name in names:
    (images/f"{name}.png").write_text("")