# ## 第二题：排序

x= input(": ")
x= int(x)
y= int(input("："))
z= int(input(":"))
if x > y:
    x,y= y,x
if x > z:
    x,z= z,x
if y > z:
    y,z= z,y
print("排好喽", x, y, z)
