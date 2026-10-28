# 第四题：九九乘法表
# 题目：输出 9*9 乘法口诀表。
# 思路：两层 for 循环，外层控制行 i（1~9），内层控制列 j（1~i）。

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, i * j), end="\t")
    print()  # 每打完一行换行
