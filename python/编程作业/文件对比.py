with open("test.txt", "r") as f1:
    lines1 = f1.readlines()
with open("copy_test.txt", "r") as f2:
    lines2 = f2.readlines()
min_length = min(len(lines1), len(lines2))

for i in range(min_length):
    if lines1[i] != lines2[i]:
        print(f"第 {i + 1} 行不同")

if len(lines1) != len(lines2):
    print("文件总行数不一样！")
