import random
import csv
import statistics
from pathlib import Path

file_path = Path.cwd() / "data.csv"

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for i in range(10):
        #列表推导式[表达式 for 变量 in 可迭代对象]
        row = [random.randint(1, 100) for _ in range(3)]
        writer.writerow(row)

second_column = []

#newline=""	不进行换行符转换，由程序自行处理
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        second_column.append(int(row[1])) #字符要转int

print("第二列数据：", second_column)
#statistics模块：python内置统计模块
print("最大值：", max(second_column))
print("最小值：", min(second_column))
print("平均值：", statistics.mean(second_column))
print("中位数：", statistics.median(second_column))