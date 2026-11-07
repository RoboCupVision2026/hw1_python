from pathlib import Path
from random import randint
from statistics import median

path=Path(__file__).resolve().parent/"rand_numbers.txt"
nums=[]
with open(path,"w") as p:
    for i in range(10):
        for j in range(3):
            if j==1:
                n=randint(1,1000000000)
                nums.append(n)
                p.write(str(n)+",")
            else:
                p.write(str(randint(1,1000000000))+",")
        p.write("\n")
print(max(nums),min(nums),sum(nums)/10,median(nums))