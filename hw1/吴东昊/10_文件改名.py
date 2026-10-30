from pathlib import Path
from random import sample
p=Path(__file__).resolve().parent/"img"
a=[f for f in p.glob("*.png") if not f.with_suffix(".jpg").exists()]
for f in sample(a,50):
    f.rename(f.with_suffix(".jpg"))
