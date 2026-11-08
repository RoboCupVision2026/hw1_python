from tempfile import tempdir

x=input()
y=input()
z=input()
temp1=x
temp2=y
if x>y:
    x=y
    y=temp1
if x>z:
    x=z
    z=temp1
if y>z:
    y=z
    z=temp2
print(x,y,z)

