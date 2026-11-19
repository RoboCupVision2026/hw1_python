#回文数判断
num = int(input("请输入一个正整数： "))
s = str(num)
s_r = reversed(s)
ans = True
for c0, c1 in zip(s, s_r):
    if(c0 != c1):
        ans = False
        break
print(f"{num}为回文数： {ans}")
