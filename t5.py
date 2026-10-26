# 第四题：回文数
x = input("输入一个数字：\n")
ans = True
if x[::-1] == x:
    ans = True
else:
    ans = False
print(ans)
