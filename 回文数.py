n = int(input("请输入一个整数："))
num = 0
x = n
while n > 0:
    temp = n
    n = n % 10
    num = num * 10 + n
    n = (temp - n) // 10
if num == x:
    print("YES")
else:
    print("NO")

