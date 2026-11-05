'''
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
'''

a=0
b=1
for _ in range(10):
    print(f"{a} {b}",end=" ")
    a+=b
    b+=a