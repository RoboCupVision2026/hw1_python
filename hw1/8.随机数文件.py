from pathlib import Path
from random import randint

path=Path(__file__).resolve().parent/"data.txt"
nums=[]
with open(path,"w") as p:
    for i in range(100000):
        a=randint(1,100)
        nums.append(str(a))
path.write_text("\n".join(nums))