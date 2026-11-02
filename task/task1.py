#组成三位数
numbers_list = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            i = 100*a+10*b+c
            if a!=b and b!=c and c!=a:
                numbers_list.append(i)
print("能组成" + str(len(numbers_list)) + "个这样的三位数" )
print("这些三位数分别是" + str(numbers_list))

