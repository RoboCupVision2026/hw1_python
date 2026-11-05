import random

nums = []
with open("shuru.txt","w", encoding="utf-8") as f:
    for row in range(10):
        cells = []
        for col in range(3):
            cells.append(str(random.randint(1, 100)))
        f.write(",".join(cells) + "\n")

with open("shuru.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        nums.append(int(line.split(",")[1]))

max_ = max(nums)
min_ = min(nums)
ave_ = sum(nums) / len(nums)
if len(nums) % 2 == 0:    
    m_ = float(sorted(nums)[len(nums) // 2]+sorted(nums)[len(nums) // 2 - 1]) / 2
else:
    m_ = sorted(nums)[len(nums) // 2]

print("最大值:", max_)
print("最小值:", min_)
print("平均值:", ave_)
print("中位数:", m_)