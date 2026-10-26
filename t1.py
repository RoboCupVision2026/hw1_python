# 第一题：组成三位数
sum = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k:
                sum += 1
print(sum)
