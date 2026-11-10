# # 第四题：文件对比
# 
# **题目：** 读取test.txt和copy_test.txt内容，检查它们的每一行内容是否相同，输出
# 所有不同的行的编号。
from pathlib import Path
text = Path("test.txt")
cop = Path("copy_test.txt")
count = 0
with open(text,"r",encoding="utf-8")as file:
    with open(cop,"r",encoding="utf-8")as file1:
        while True:
            i = file.readline()
            j = file1.readline()
            if i == "" and j == "":
                break
            count += 1
            if i != j:
                print(count)

                


