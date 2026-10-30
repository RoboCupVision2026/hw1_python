from pathlib import Path
from random import randint
p=Path(__file__).resolve().parent/"test"
n=int(input("文件数："))
m=int(input("行数："))
p.mkdir(exist_ok=True)
for i in range(1,n+1):
    if (p/f"{i}-python.txt").exists():
        continue
    with (p/f"{i}.txt").open("w",encoding="utf-8") as f:
        for j in range(m):
            f.write("".join(chr(randint(32,126)) for k in range(20))+"\n")
for f in list(p.iterdir()):
    if f.is_file() and not f.stem.endswith("-python"):
        with f.open(encoding="utf-8") as g:
            a=g.readlines()
        with f.open("w",encoding="utf-8") as g:
            for s in a:
                g.write(s.rstrip("\n")+"-python\n")
        f.rename(f.with_name(f.stem+"-python"+f.suffix))
