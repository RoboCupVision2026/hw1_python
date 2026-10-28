# 第五题：打印菱形图案
# 题目：打印如下菱形（共 7 行，星号数分别为 1,3,5,7,5,3,1）
# 思路：用字符串的 center 方法居中，总宽度取最宽一行（7 个星）。

width = 7
stars = [1, 3, 5, 7, 5, 3, 1]
for n in stars:
    line = "*" * n
    print(line.center(width))
