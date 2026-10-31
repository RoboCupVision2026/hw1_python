import random
import statistics

with open("data.txt", "w") as f:
    for i in range(10):
        nums = [random.randint(1, 100) for j in range(3)]
        f.write(",".join(map(str, nums)) + "\n")

data = []

with open("data.txt", "r") as f:
    for line in f:
        nums = line.strip().split(",")
        data.append(int(nums[1]))

print("最大值：", max(data))
print("最小值：", min(data))
print("平均值：", statistics.mean(data))
print("中位数：", statistics.median(data))