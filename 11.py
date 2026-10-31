import random
import statistics
with open("table.txt", "w", encoding="utf-8") as f:
    for _ in range(10):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        n3 = random.randint(1, 100)
        f.write(f"{n1},{n2},{n3}\n")
col2 = []
with open("table.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        col2.append(int(parts[1]))

print("第二列最大值：", max(col2))
print("第二列最小值：", min(col2))
print("第二列平均值：", sum(col2)/len(col2))
print("第二列中位數：", statistics.median(col2))