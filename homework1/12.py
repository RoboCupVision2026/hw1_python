import random
n = int(input("请输入 test.txt 写多少行："))
f = open("test.txt", "w")
for i in range(n):
    line = ""
    for j in range(10):
        line = line + chr(random.randint(32, 126))
    f.write(line + "\n")
f.close()
# 复制
f1 = open("test.txt", "r")
f2 = open("copy_test.txt", "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()