a=int(input('请输入一个整数'))
a=str(a)
if a==a[::-1]:
    print('YES')
else:
    print('NO')