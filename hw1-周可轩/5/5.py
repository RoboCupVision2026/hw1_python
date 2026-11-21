#回文数
#题目：任意位数的正整数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同

a = int(input())
a = str(a)

flg = 1
for i in range(len(a) // 2):
    if (a[i] != a[len(a) - 1 - i]):
        print("不是回文数")
        flg = 0
        break

if flg:
    print("是回文数")