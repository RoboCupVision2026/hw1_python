print("请在一行内输入三个整数，用空格隔开")
x,y,z=map(int,input().split())
if(x>y):x,y=y,x
if(x>z):x,z=z,x
if(y>z):y,z=z,y
print(x,y,z)