# 文件输入
import sys
from statistics import mean, median

sys.stdin = open("11.txt", "r")

a = list()
n = 10
for i in range(n):
    b = list(map(int, input().split(",")))
    print(*b)
    a.append(b[1])

print("max = " + str(max(a)))
print("min = " + str(min(a)))
print("mean = " + str(mean(a)))
print("median = " + str(median(a)))

