x=int(input("please enter x:"))
y=int(input("please enter y:"))
z=int(input("please enter z:"))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(f"{x}<{y}<{z}")