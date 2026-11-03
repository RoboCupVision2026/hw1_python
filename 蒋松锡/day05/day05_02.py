import random
import string

n = int(input("输入行数："))
chars = string.ascii_letters + string.digits + string.punctuation + " "

with open("test.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        line = ""
        for j in range(20):
            line += random.choice(chars)
        f.write(line + "\n")

with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("copy_test.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("复制完成")
