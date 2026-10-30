# 求整数数位，并逆序输出
a = int(input())
b = str(a)
count = 0

while a != 0:
    a //= 10
    count += 1

print(count)
print(b[::-1])
