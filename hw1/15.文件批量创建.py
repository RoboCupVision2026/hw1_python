from pathlib import Path
from os import makedirs
from random import randint

path=Path(__file__).resolve().parent/"test"
makedirs(path, exist_ok=True)
i=int(input())
num=randint(i+1,i+100)
j=int(input())
for k in range(num):
    with open(path/f"{k+1}.txt","w") as p:
        for l in range(j):
            p.write(chr(randint(32,126))+"\n")
files=list(path.iterdir())
for file in files:
    lines=file.read_text().splitlines()
    llines=[]
    for line in lines:
        llines.append(line+"-python")
    file.write_text("\n".join(llines))
    file.rename(file.with_name(file.stem+"-python"+file.suffix))