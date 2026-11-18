import os
import random
import string

i = int(input())
j = int(input())
os.makedirs("test", exist_ok=True)

for k in range(i):
    with open(f"test/{k}.txt", "w") as f:
        for m in range(j):
            f.write("".join(random.choices(string.ascii_letters, k=10)) + "\n")

for n in os.listdir("test"):
    p = "test/" + n
    with open(p) as f:
        a = f.read().splitlines()
    with open(p, "w") as f:
        for s in a:
            f.write(s + "-python\n")
    os.rename(p, p[:-4] + "-python.txt")
