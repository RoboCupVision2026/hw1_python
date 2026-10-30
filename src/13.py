import random

n = int(input("请输入行数："))
with open("test.txt", "w") as file:
    for i in range(n):
        file.write("".join(chr(random.randint(32, 126)) for j in range(100)) + "\n")

with open("test.txt", "r") as file:
    content = file.read()
with open("copy_test.txt", "w") as file:
    file.write(content)
