from pathlib import Path
from random import randint
p=Path(__file__).resolve().parent/"nums.txt"
with p.open("w",encoding="utf-8") as f:
    for i in range(10):
        f.write(",".join(str(randint(1,100)) for j in range(3))+"\n")
with p.open(encoding="utf-8") as f:
    a=sorted(int(s.split(",")[1]) for s in f)
print("最大：",a[-1])
print("最小：",a[0])
print("平均：",sum(a)/len(a))
print("中位数：",(a[4]+a[5])/2)
