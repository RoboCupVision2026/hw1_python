a = int(input())
s = ""

while a > 0:
    s = s + str(a%10)
    a = a // 10

print(len(s))
print(s)