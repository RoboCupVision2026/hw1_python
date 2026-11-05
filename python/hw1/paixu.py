x=int(input("请输入x："))
y=int(input("请输入y："))
z=int(input("请输入z："))
t=[x,y,z]
for i in range(3):
    for j in range(0,3-i-1):
        if t[j]>t[j+1]:
            t[j],t[j+1]=t[j+1],t[j]
for i in range(3):    
    print(t[i])