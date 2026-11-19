# 数字位数
num = input()
n = len(num)
print(n)
num = num[::-1]
p = -1
for i in range(n):
    if int(num[i]) != 0:
        p = i
        break
if p == -1:
    print(0)
else:
    print(num[p:n])
        
        