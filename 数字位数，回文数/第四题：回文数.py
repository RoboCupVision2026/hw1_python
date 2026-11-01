# 输入一个整数，判断他是不是回文数
s = input("请输入一个正整数")
reversedS = s[::-1]
if s == reversedS:
    print(f"{s}是一个回文数")
else :
    print(f"{s}不是一个回文数")