text=input("请输入三个整数,以空格分隔:")
x,y,z=text.split()
x=int(x)
y=int(y)
z=int(z)
if y<x:
    x,y=y,x #现在x<y
if z<x:
    x,y,z=z,x,y
elif z<y:
    y,z=z,y
print(x,y,z)