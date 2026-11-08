import random

with open(r"D:\python learn\data2.txt","w")as f:
    for i in range(10):
        row=[]
        for j in range(3):
            num=random.randint(1,100)
            row.append(num)
        f.write(",".join(map(str,row))+"\n")

list2=[]
with open(r"D:\python learn\data2.txt","r")as f:
    for i in range(10):
        line=f.readline()
        parts=line.strip().split(",")
        list2.append(int(parts[1]))
for i in range(9):
    for j in range(9):
        if list2[j]>=list2[j+1]:
            temp=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=temp
Sum=0
for i in range(9):
    Sum=Sum+list2[i]
midnum=(list2[4]+list2[5])/2
maxnum=list2[9]
minnum=list2[0]
avrnum=Sum/10
print(f"最大的数字为{maxnum}")
print(f"最小的数字为{minnum}")
print(f"平均数为{midnum}")
print(f"中位数为{avrnum}")