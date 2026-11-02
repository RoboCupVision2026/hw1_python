#斐波那契数列
a = 0
b = 1
numbers_list = [a]
for i in range(19):
    a,b = b,a+b
    numbers_list.append(a)
print(numbers_list)