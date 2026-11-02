#排序
x = int(input("请输入整数x"))
y = int(input("请输入整数y"))
z = int(input("请输入整数z"))
if x>=y:
    x,y = y,x
if x>=z:
    x,z = z,x
if y>=z:
    y,z = z,y
print(x,y,z)

