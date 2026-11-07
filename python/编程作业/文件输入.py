import random
with open("data.txt", "w") as f:
    for i in range(10): # 10行
        data = []
        for j in range(3): 
            data.append(str(random.randint(1, 100)))
        f.write(",".join(data) + "\n")
col2 = []
with open("data.txt", "r") as f:
    for line in f: 
        line = line.strip()
        if line == "":      
            continue
        parts = line.split(",") 
        col2.append(float(parts[1])) 
col2.sort()
max_ = col2[-1] 
min_ = col2[0]  
avg_ = sum(col2) / len(col2) 
mid_= len(col2) // 2
median_= (col2[mid_- 1] + col2[mid_]) / 2

print(f"最大值: {max_}, 最小值: {min_}, 平均值: {avg_:.2f}, 中位数: {median_}")
