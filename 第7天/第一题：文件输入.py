# 先生成一个10*3的随机数矩阵，存到randomMatrix里面。
import random
import statistics
f = open("generatedFiles/randomMatrix", 'w', encoding='utf-8')
for i in range(10):
    f.write(f"{random.random()}, {random.random()}, {random.random()}\n")
f.close()

# 然后再输出第二列max, min, average, median
column2 = []
f = open("generatedFiles/randomMatrix", 'r', encoding='utf-8')
for line in f:
    line = line.strip().split(',')
    column2.append(float(line[1]))
f.close()

print(f"第二列的最大值是：{max(column2)}")
print(f"最小值是：{min(column2)}")
print(f"平均值是：{sum(column2) * 1.0 / len(column2) }")
print(f"中位数是：{statistics.median(column2)}")


