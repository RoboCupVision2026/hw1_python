n = int(input("请输入一个正整数："))
s = str(n)
print("它是", len(s), "位数")
rev = ""
for ch in s:
    rev = ch + rev
print("逆序：", rev)