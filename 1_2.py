#三个数排列
x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
z = int(input("请输入第三个整数："))

#法一
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print("（法一）从小到大：", x, y, z)

#法二
nums = [x, y, z]
nums.sort()
print("（法二）从小到大： ", nums)
