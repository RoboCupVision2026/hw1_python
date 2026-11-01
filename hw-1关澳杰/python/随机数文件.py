from encodings import utf_8
import random

with open("data/data.txt", "w", encoding="utf_8") as f:
    for i in range(0,100000):
        i= random.randint(1,100)
        f.write(f"{i}\n")
