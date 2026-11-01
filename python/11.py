import random
import statistics

with open("number.txt", "w", encoding="utf-8") as f:
    for i in range(10):
        row = [random.randint(1, 100) for j in range(3)]
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

col2 = []
with open("number.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        nums = list(map(int, line.split(",")))
        col2.append(nums[1])

max_val = max(col2)
min_val = min(col2)
avg_val = sum(col2)/len(col2)
mid_val = statistics.median(col2)
print(f"最大值：{max_val}")
print(f"最小值：{min_val}")
print(f"平均值：{avg_val:.2f}")
print(f"中位数：{mid_val}")
