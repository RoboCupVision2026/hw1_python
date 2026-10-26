# 第三题：斐波那契数列
array = [0, 1]
for i in range(2, 20):
    tmp = array[i-1]+array[i-2]
    array.append(tmp)
print(array)
