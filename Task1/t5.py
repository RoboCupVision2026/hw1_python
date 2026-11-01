print("请输入一个正整数：",end="")
a=input()
if a==a[::-1]:
    print("它是回文数")
else:
    print("它不是回文数")