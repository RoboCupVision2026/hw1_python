# 第八题：判断闰年
# 题目：输入某年，判断这一年是不是闰年。
# 规则：
#   1. 普通闰年：公历年份是 4 的倍数，一般是闰年（如 2004 年）；
#   2. 世纪闰年：公历年份是整百数的，必须是 400 的倍数才是闰年
#      （如 1900 年不是世纪闰年，2000 年是世纪闰年）。

def is_leap_year(year):
    if year % 100 == 0:          # 世纪年
        return year % 400 == 0
    else:                        # 普通年
        return year % 4 == 0


if __name__ == "__main__":
    y = int(input("请输入年份："))
    if is_leap_year(y):
        print("{} 年是闰年".format(y))
    else:
        print("{} 年不是闰年".format(y))
