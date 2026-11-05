a=str(input())
t=len(a)
i=0
while i<t//2:
    if a[i]!=a[t-i-1]:
        print("不是回文数")
        break
    else:
        i+=1
        continue
if i==t//2:
    print("是回文数")
