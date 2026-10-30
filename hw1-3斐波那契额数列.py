a = 0
b = 1

print(a, end='、 ')
for i in range(18):
    a, b = b, a + b
    print(a, end='、 ')
print(b)