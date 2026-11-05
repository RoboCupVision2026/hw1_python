import random
from pathlib import Path
dataPath=Path(__file__).parent/"data.txt"
with open(dataPath,"w",encoding="utf-8") as f:
    for _ in range(100000):
        f.write(str(random.randint(1,100))+"\n")