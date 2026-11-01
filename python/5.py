a = int(input())
s1 = str(a)
s2 = ""
b = True

while a > 0:
    s2 += str(a%10)
    a //= 10

for i in range(len(s2)):
    if s1[i] != s2[i]:
        b = False
        break

print(b)