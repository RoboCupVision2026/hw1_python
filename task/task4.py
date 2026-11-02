#数字位数
x = input("请输入一个任意位数的正整数")
y = str()
print("这个正整数有" + str(len(x)) + "位")
for i in range(len(x)):
    x,y = x[0:len(x)-1],y + x[len(x)-1]
print(y)