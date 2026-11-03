import os
import random
import numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
rows=10
lines=3
file_path="random_text.txt"
with open(file_path, "w", encoding="utf-8") as file:
    for r in range(rows):
        for l in range(lines-1):
            file.write(str(random.randint(1, 100)) + ',')
        file.write(str(random.randint(1, 100))+'\n')
with open(file_path, "r", encoding="utf-8") as f:
    lines=np.loadtxt(file_path, delimiter=',', dtype=int)
    data=lines[0:10,1]
    max_line = max(data)          
    min_line = min(data)         
    avg_line = sum(data) / len(data) 
    median_line = np.median(data)
    print("最大值：", max_line)
    print("最小值：", min_line)
    print("平均值：", avg_line)
    print("中位数：", median_line)
