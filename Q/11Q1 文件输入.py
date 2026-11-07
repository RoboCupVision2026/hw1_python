import random as rd

with open("data2.txt","w",encoding="utf-8") as f:
    for _ in range(10):
        a,b,c = rd.uniform(0,100),rd.uniform(0,100),rd.uniform(0,100)
        f.write(f"{a:.2f},{b:.2f},{c:.2f}\n")

num=[]
with open("data2.txt","r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        lst = line.split(',')
        num.append(float(lst[1]))

order=sorted(num)

mx=max(num)
mn=min(num)
n=len(num)
sm=sum(num)
mid=(order[(n-1)//2]+order[n//2])/2

print(f"最大值为{mx}，最小值为{mn}，平均值为{sm/n:.2f}，中位数为{mid:.2f}")