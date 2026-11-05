s=str(input())
if s[0]=="0":
    print("请重新输入")
else:
    t=len(s)
    print(t,"位数字",sep="")
    for i in range(t-1,0,-1):
        print(s[i],end="")
    print(s[0])
