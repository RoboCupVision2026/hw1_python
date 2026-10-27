# 回文数
a = input()
i = 0
j = len(a) - 1
flag = True
while i<j:
    if a[i] != a[j]:
        flag = False
        break
    else:
        i += 1
        j += 1

print(flag)