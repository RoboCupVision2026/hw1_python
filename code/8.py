# 随机数问题
import random

with open("data.txt", "w") as f:
    N = 100000
    a = [random.randint(1, 100) for _ in range(N)]
    for x in a:
        f.write(str(x) + "\n")
