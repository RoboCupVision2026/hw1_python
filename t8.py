# 第三题：随机数文件
import random

with open("data.txt", "w", encoding="utf-8") as f:
    for _ in range(100000):
        num = random.randint(1, 100)
        f.write(str(num) + '\n')
