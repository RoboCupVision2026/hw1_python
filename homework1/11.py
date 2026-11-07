import random
f = open("num.txt", "w")
for i in range(10):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    f.write(str(a) + "," + str(b) + "," + str(c) + "\n")
f.close()
col = []
f = open("num.txt", "r")
for line in f:
    line = line.strip()
    parts = line.split(",")
    col.append(int(parts[1]))
f.close()
print("第二列的数据：", col)
print("最大值：", max(col))
print("最小值：", min(col))
print("平均值：", sum(col) / len(col))
col.sort()
if len(col) % 2 == 0:
    mid = (col[len(col) // 2 - 1] + col[len(col) // 2]) / 2
else:
    mid = col[len(col) // 2]
print("中位数：", mid)