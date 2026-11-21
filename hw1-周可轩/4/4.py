#数字位数
#题目：给一个任意位数的正整数，要求：一、求它是几位数。二、逆序打印出各位数字。
#程序分析：一、针对整数，分解出每一位数。二、整数转换为字符串，利用字符串的方法。

a = int(input())
b = a

#sol1
cnt = 0
while a > 0:
    print(a % 10, end="")
    a //= 10
    cnt += 1

print()
print(cnt)

#sol2
print(str(b)[::-1])
print(len(str(b)))