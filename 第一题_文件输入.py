# # 第一题：文件输入
# 
# **题目：** 自行制作一个10行3列文件，每列内容为随机数，以逗号作为分割符。写程序输出第二列的最大值、最小值、平均值、中位数。

import random
from pathlib import Path
c2 = []
current = Path(__file__)
f = current.resolve().parent / "input_1.txt"
f.touch()
with open(f,"w",encoding = "utf-8")as file:
    for i in range(10):
        for j in range(3):
            number = random.uniform(3,100)
            file.write(str(number))
            if j<2:
                file.write(",")
            else:
                file.write("\n")
with open (f,"r",encoding = "utf-8")as file1:
    for line in file1:
        new1 = line.strip()
        new2 = new1.split(",")
        c2.append(float(new2[1]))
da = max(c2)
xiao = min(c2)
total = sum(c2)
average = total / len(c2)
sort = sorted(c2)
zhong = (sort[4]+sort[5])/2
print("最大值是：",da)
print("最小值是：",xiao)
print("平均值是：",average)
print("中位数是：",zhong)







