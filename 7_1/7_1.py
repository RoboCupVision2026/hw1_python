import os
import random
cr_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(cr_dir, "text.txt")
with open(text_dir,"w") as f:
    for i in range(10):
        for j in range(2):
            f.write(str(random.randint(1,100))+",")
        f.write(str(random.randint(1,100))+"\n")

with open(text_dir,"r") as f:
    lines = f.readlines()
    num_2s =[]
    for line in lines:
        nums = line.strip().split(",")
        num_2s.append(int(nums[1]))
    print("最大值:",max(num_2s))
    print("最小值:",min(num_2s))
    print("平均值:",sum(num_2s)/len(num_2s))
    print("中位数:",sorted(num_2s)[len(num_2s)//2])