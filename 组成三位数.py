count = 0

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                num = i * 100 + j * 10 + k
                print(num)
                count += 1

print("共有", count, "个三位数")