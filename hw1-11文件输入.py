import random
import statistics

with open('data_10x3.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        row = [str(random.randint(1, 100)) for j in range(3)]
        f.write(','.join(row) + '\n')

second_column = []
with open('data_10x3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            second_column.append(int(parts[1]))

if second_column:
    print(f"最大值: {max(second_column)}")
    print(f"最小值: {min(second_column)}")
    print(f"平均值: {statistics.mean(second_column)}")
    print(f"中位数: {statistics.median(second_column)}")