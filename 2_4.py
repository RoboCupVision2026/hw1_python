#随机数文件
import random

with open("data.txt", "w", encoding="utf-8") as f:
    for i  in range(1,100001):
        num = random.randint(1, 100)
        if i % 15 == 0 :
            f.write(str(num) + "\n")
        else :
            f.write(str(num) + "  ")
