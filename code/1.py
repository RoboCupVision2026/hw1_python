# 组成三位数

ans = list()

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                ans.append(i * 100 + j * 10 + k);

print(len(ans))
print(*ans)