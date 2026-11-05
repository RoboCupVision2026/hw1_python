import random 
from pathlib import Path

def generateRandomLine():
    while True:
        nums=[str(random.randint(1,100)) for _ in range(3)]
        yield ",".join(nums)+"\n"

dataPath=Path(__file__).parent/"data.txt"

with open(dataPath,"w",encoding="utf-8") as f:
    gen=generateRandomLine()
    for _ in range(10):
        f.write(next(gen))

'''
方法一
with open(dataPath,"w",encoding="utf-8") as f:
    for _ in range(10):
        for i in range(3):
            f.write(str(random.randint(1,100)))
            if i != 2:
                f.write(",")
            else:
                f.write("\n")

'''