# 用四个数字1、2、3、4能组成多少个互不相同且无重复数字的三位数？各是多少？
result = []
cnt = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j & j != k & k != i:
                value = 100 * i + 10 * j + k
                result.append(value)
                cnt += 1
print(f"总共能组成{cnt}个互不相同的三位数")
print(result)