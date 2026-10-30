x,y,z=map(int,input("请输入三个整数，用空格分隔：").split())
#法一
if x > y:x,y=y,x
if x>z:x,z=z,x
if y>z:y,z=z,y
print(x,y,z)
#法二
lst =sorted([x,y,z])
print("从小到大",lst) 
