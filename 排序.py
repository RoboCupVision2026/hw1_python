x = int(input("第一个整数为："))
y = int(input("第二个整数为："))
z = int(input("第三个整数为："))
if x > y:
    temp = x
    x = y
    y = temp
if x > z:
    temp = x
    x = z
    z = temp
if y > z:
    temp = y
    y = z
    z = temp
print("从小到大排序：",x,y,z)