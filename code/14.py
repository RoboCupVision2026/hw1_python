# 文件对比
with open("test.txt", "r") as f1:
    a = f1.readlines()

with open("copy_test.txt", "r") as f2:
    b = f2.readlines()

for i in range(max(len(a), len(b))):
    if i >= len(a) or i >= len(b) or a[i] != b[i]:
        print(i + 1)