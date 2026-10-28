# 第六题：数字位数
# 题目：给一个任意位数的正整数，要求：
#   一、求它是几位数；
#   二、逆序打印出各位数字。
# 思路：转成字符串最方便——长度就是位数，[::-1] 就是逆序。

def analyze_number(n):
    s = str(n)
    print("{} 是 {} 位数".format(n, len(s)))
    print("逆序打印各位数字：", s[::-1])


if __name__ == "__main__":
    num = int(input("请输入一个正整数："))
    analyze_number(num)
