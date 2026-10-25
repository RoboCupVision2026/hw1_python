# 第一题：文件输入
import random
import os
from pathlib import Path
import statistics

with open("data.txt", "w", encoding="utf-8") as f:
    for _ in range(10):
        nums = [random.randint(1, 100) for _ in range(3)]
        f.write(",".join(map(str, nums))+'\n')

with open("data.txt", "r", encoding="utf-8") as f:
    second_nums = []
    for _ in range(10):
        nums = f.readline().strip().split(',')
        second_nums.append(int(nums[1]))
    print(second_nums)
    print(f"最大值为：{max(second_nums)}")
    print(f"最小值为：{min(second_nums)}")
    print(f"平均数为：{statistics.mean(second_nums)}")
    print(f"中位数为：{statistics.median(second_nums)}")
