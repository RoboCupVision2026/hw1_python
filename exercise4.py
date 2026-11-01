a=int(input())
count=0
s=list()
while a!=0:
    s.append(a%10)
    count+=1
    a//=10
print(count)
print(s)