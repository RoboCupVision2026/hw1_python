a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
c=int(input("请输入第三个数："))
if a>b:
    j=b
    b=a
    a=j
if a>c:
    j=c
    c=a
    a=j
if b>c:
    j=b
    b=c
    c=j
print(a)
print(b)
print(c)
