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
f = open("test.txt", "r")
s = f.read()
f.close()
s = "python" + s + "python"
f = open("test.txt", "w")
f.write(s)
f.close()
print("修改完成")
f1 = open("test.txt", "r")
lines1 = f1.readlines()
f1.close()
f2 = open("copy_test.txt", "r")
lines2 = f2.readlines()
f2.close()
if len(lines1) != len(lines2):
    print("两个文件的行数不一样")
# 两个文件行数可能不一样，取短的那个来比
n = len(lines1)
if len(lines2) < n:
    n = len(lines2)
for i in range(n):
    if lines1[i] != lines2[i]:
        print("第", i + 1, "行不一样")