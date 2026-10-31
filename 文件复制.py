import random
import string
import shutil

n = int(input("请输入文件行数："))

chars = string.ascii_letters + string.digits + string.punctuation + " "

with open("test.txt", "w") as f:
    for i in range(n):
        line = "".join(random.choices(chars, k=30))
        f.write(line + "\n")

shutil.copyfile("test.txt", "copy_test.txt")

print("文件复制完成")