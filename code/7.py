# 最后剩下谁
n = 233
a = list(range(1, n + 1, 1))
cur = 0
while len(a) > 1:
    cur = (cur + 2) % len(a)
    a.pop(cur)
print(a[0]) 
