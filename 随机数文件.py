import random

with open("data.txt", "w") as f:
    for i in range(100000):
        num = random.randint(1, 100)
        f.write(str(num) + "\n")

print("文件创建成功")