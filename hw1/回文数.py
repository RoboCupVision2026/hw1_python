s=input("输入一个数")
flag=True
for i in range(int(len(s)/2)):
    if s[i]!=s[-i-1]:
        flag=False
        break
if flag:
    print("是回文数")
else:
    print("不是回文数")
