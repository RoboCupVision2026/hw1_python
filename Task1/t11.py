import random
import statistics
with open("data.csv","w") as f:
    for i in range(10):
        f.write(f"{random.randint(1,100)},{random.randint(1,100)},{random.randint(1,100)}\n")
with open("data.csv","r") as f:
    secondcolumn=[]
    for line in f:
        secondcolumn.append(int(line.split(",")[1]))
    print(f"最大值：{max(secondcolumn)}")
    print(f"最小值：{min(secondcolumn)}")
    print(f"平均值：{sum(secondcolumn)/len(secondcolumn)}")
    print(f"中位数：{statistics.median(secondcolumn)}")