# 斐波那契数列

def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n-1) + f(n-2)

for i in range(0, 21):
    print(f(i), end = ' ')
    