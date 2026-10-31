num = int(input("请输入一个正整数："))

s = str(num)

if s == s[::-1]:
    print(num, "是回文数")
else:
    print(num, "不是回文数")