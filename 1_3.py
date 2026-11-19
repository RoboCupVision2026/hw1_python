#斐波那契数列
a, b = 0, 1

print("斐波那契数列前20项：")

for i in range(20):
    print(a, end=" ")
    a, b = b, a + b
