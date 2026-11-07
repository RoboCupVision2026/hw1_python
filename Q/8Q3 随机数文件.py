import random

with open("data.txt","w",encoding="utf-8") as f:
    for _ in range(100000):
        f.write(f"{random.randint(1,100)}\n")