num = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j:
                if i != k:
                    if j != k:
                        print(i * 100 + j * 10 + k)
                        num = num + 1
print("一共", num, "个")