# ##  十一

import random
with open("date.txt", "w", encoding="utf-8") as file:
    for _ in range(10):
        a= random.randint(1, 100)
        b= random.randint(1, 100)
        c= random.randint(1, 100)
        row= f"{a},{b},{c}\n"
        file.write(row)
print("date.txt 已生成")
nums= []
with open("date.txt", "r", encoding="utf-8") as file:
    for line in file:
        columns= line.split(",")
        value= int(columns[1])
        nums.append(value)
print("最大值", max(nums))
print("最小值",min(nums))
import statistics
print("平均数",  statistics.mean(nums))
print("中位数",  statistics.median(nums))

