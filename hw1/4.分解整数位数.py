num=input("请输入一个正整数：")
print(f"该正整数为{len(num)}位数。\n数字逆序为：",end="")
for i in range(len(num)-1,-1,-1):
    print(num[i],end="")