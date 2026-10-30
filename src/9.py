# 随机数文件
import random

with open("data.txt", "w", encoding="utf-8") as file:
    for _ in range(100000):
        file.write(f"{random.randint(1, 100)}\n")
