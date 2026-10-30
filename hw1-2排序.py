x, y, z = int(input()), int(input()), int(input())

if x > y:
    y, x = x, y
if x > z:
    z, x = x, z
if y > z:
    z, y = y, z
    
print(x, y, z)