n = [3 for i in range(233)]
i, j = 0, 1

while sum(n):
    if n[i]:
        n[i] = j
        j = (j + 1) % 3
    i = (i + 1) % 233
print(i)