# 文件复制
import random
import string
import shutil

n = int(input())

with open("test.txt", "w", encoding = "ascii") as f:
    for i in range(n):
        length = random.randint(1, 80)
        line = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k = length))
        print(line, file = f)

shutil.copyfile("test.txt", "copy_test.txt")

