import random
import statistics
with open('data_in.txt', 'w', encoding='utf-8') as f:
    for _ in range(10):
        row = [random.randint(1, 100) for _ in range(3)]
        f.write(','.join(map(str, row)) + '\n')
col2 = []
with open('data_in.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(',')
        col2.append(int(parts[1]))

print("第二列数据:", col2)
print("最大值:", max(col2))
print("最小值:", min(col2))
print("平均值:", sum(col2)/len(col2))
print("中位数:", statistics.median(col2))