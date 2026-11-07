
line = input() 
str_list = line.split() 
x = int(str_list[0])
y = int(str_list[1])
z = int(str_list[2])

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x, y, z)
