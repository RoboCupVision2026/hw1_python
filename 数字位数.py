n = int(input("请输入一个整数："))
count = 0
print("逆序表达为：",end="")
while n > 0:
    temp = n
    n = n % 10
    print(n,end="")
    n = (temp - n) // 10
    count += 1
print(" 数字位数为：",count)