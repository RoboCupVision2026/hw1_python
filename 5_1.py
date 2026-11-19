#正整数逆序
num = int(input("请输入一个正整数 ："))
count = 0
num_copy = num
while num > 0:
    count += 1
    num //= 10

num = num_copy

print(f"{num}是{count}位数")
print(f"{num}的逆序" + ''.join(reversed(str(num))))#reversed()返回反向迭代器
