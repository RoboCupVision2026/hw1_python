def swap(a,b):
    c=a
    a=b
    b=c
    return a,b
    
x = int(input())
y = int(input())
z = int(input())
if x>y:
    x,y=swap(x,y)
if y>z:
    y,z=swap(y,z)
if x>y:
    x,y=swap(x,y)
print(x,y,z)