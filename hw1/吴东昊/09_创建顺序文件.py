from pathlib import Path
from random import choices
from string import ascii_uppercase,digits
p=Path(__file__).resolve().parent/"img"
p.mkdir(exist_ok=True)
a={f.stem for f in p.iterdir() if f.is_file()}
while len(a)<100:
    s="".join(choices(ascii_uppercase+digits,k=4))
    if s not in a:
        (p/(s+".png")).touch()
        a.add(s)
