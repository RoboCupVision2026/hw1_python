x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))
if x > y:
    t = x
    x = y
    y = t
if x > z:
    t = x
    x = z
    z = t
if y > z:
    t = y
    y = z
    z = t
print("从小到大是：", x, y, z)