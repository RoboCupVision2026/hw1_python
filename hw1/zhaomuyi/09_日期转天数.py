# 第九题：日期转天数
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 思路：把前面每个月的天数累加，再加上当前日。注意闰年 2 月是 29 天。

def day_of_year(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 闰年 2 月改为 29 天
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    # 累加前 month-1 个月的天数
    total = sum(days_in_month[:month - 1]) + day
    return total


if __name__ == "__main__":
    y = int(input("年："))
    m = int(input("月："))
    d = int(input("日："))
    print("这是 {} 年的第 {} 天".format(y, day_of_year(y, m, d)))
