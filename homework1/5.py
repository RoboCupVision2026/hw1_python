n = input("请输入一个正整数：")
s = str(n)
rev = ""
for ch in s:
    rev = ch + rev
if rev == s:
    print(n, "是回文数")
else:
    print(n, "不是回文数")