# 第七题：回文数
# 题目：任意位数的正整数，判断它是不是回文数。
#       例如 12321 是回文数，个位与万位相同，十位与千位相同。

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


if __name__ == "__main__":
    num = int(input("请输入一个正整数："))
    if is_palindrome(num):
        print("{} 是回文数".format(num))
    else:
        print("{} 不是回文数".format(num))
