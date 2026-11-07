num=int(input())
x=num
ans=0
while x:
    x//=10
    ans+=1
print(ans)
print(int(str(num)[::-1]))