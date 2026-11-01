a=int(input())
s=list()
i=1
flag=0
while a!=0:
    s.append(a%10)
    a//=10
for x in s:
    if x==s[len(s)-i]:
        flag=1
        i+=1
    else:
        flag=0
        break
if flag:
    print('Yes')
else:
    print('No')
