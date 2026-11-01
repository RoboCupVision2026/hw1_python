# 输入三个整数，升序输出
x = int(input("请输入x:"))
y = int(input("请输入y:"))
z = int(input("请输入z:"))

list = []
list.append(x)
list.append(y)
list.append(z)

list.sort()
print(list)