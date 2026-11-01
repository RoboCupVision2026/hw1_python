# 求出任意整数的位数，并逆序输出
s = input("请输入一个正整数：")
length = len(s)
result = s[::-1]
print(f"整数{s}有{length}位")
print(f"逆序输出的结果为：{result}")