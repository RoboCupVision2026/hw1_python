a=input()
b=a[::-1]
n=0
for i in range(len(b)):
    if a[i]!=b[i]:
        print("不是回文数")
        n=1
        break
if n==0:
    print("是回文数")