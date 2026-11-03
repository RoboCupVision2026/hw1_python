import os
import random
import string

n = int(input("文件数量："))
m = int(input("每个文件多少行："))

os.makedirs("test", exist_ok=True)
chars = string.ascii_letters + string.digits + string.punctuation + " "

for i in range(1, n + 1):
    with open("test/" + str(i) + ".txt", "w", encoding="utf-8") as f:
        for j in range(m):
            line = ""
            for k in range(20):
                line += random.choice(chars)
            f.write(line + "\n")

for name in os.listdir("test"):
    if not name.endswith(".txt") or name.endswith("-python.txt"):
        continue

    old = "test/" + name
    with open(old, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(old, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.rstrip("\n") + "-python\n")

    new = "test/" + name[:-4] + "-python.txt"
    os.rename(old, new)

print("完成")
