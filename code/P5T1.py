import random
n=10
m=3
f=open("data1.txt","w")
for i in range(n):
    a=random.randint(1,100)
    b=random.randint(1,100)
    c=random.randint(1,100)
    line=str(a)+","+str(b)+","+str(c)+"\n"
    f.write(line)
f.close()

numlist=[]
f=open("data1.txt","r")
for line in f:
    row=line.split(",")
    b=int(row[1])
    numlist.append(b)
f.close()

big=max(numlist)
small=min(numlist)
total=sum(numlist)
avg=total/10
numlist.sort()
mid=(numlist[4]+numlist[5])/2

print("largest number:",big)
print("smallest number:",small)
print("average:",avg)
print("median:",mid)