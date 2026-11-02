#回文数
x = input("输入一个正整数")
a = bool(1)
for i in range(len(x)):
    if x[i] != x[len(x)-i-1]:
        a = 0
    break
if a == 1:
    print("这是一个回文数")
else:
    print("这不是一个回文数")
