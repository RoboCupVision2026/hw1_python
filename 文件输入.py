import random
with open("wenjianshuru.txt", "w", encoding="utf-8") as f:
    for _ in range(10):
        a = random.uniform(0, 100)
        b = random.uniform(0, 100)
        c = random.uniform(0, 100)
        f.write(f"{a:.2f},{b:.2f},{c:.2f}\n")
col2 = []
with open("wenjianshuru.txt", "r", encoding="utf-8") as f:
    for line in f:
        nums = line.strip().split(",")
        col2.append(float(nums[1]))
maxv = max(col2)
minv = min(col2)
avgv = sum(col2)/len(col2)
s = sorted(col2)
medv = (s[4] + s[5])/2

print(maxv, minv, avgv, medv)
