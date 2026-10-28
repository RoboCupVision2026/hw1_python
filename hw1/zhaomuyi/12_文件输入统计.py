# 第十二题：文件输入
# 题目：自行制作一个 10 行 3 列的文件，每列内容为随机数，逗号作为分割符。
#       写程序输出第二列的最大值、最小值、平均值、中位数。
# 思路：先用 random 生成 data_12.csv（10 行 3 列，逗号分隔），再读回来统计第二列。

import random
import statistics


def make_file(path="data_12.csv"):
    with open(path, "w", encoding="utf-8") as f:
        for _ in range(10):
            row = [str(random.randint(1, 100)) for _ in range(3)]
            f.write(",".join(row) + "\n")


def analyze_second_column(path="data_12.csv"):
    col2 = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cols = line.split(",")
            col2.append(float(cols[1]))   # 第二列（下标从 0 开始，所以是 cols[1]）
    print("第二列数据：", col2)
    print("最大值：", max(col2))
    print("最小值：", min(col2))
    print("平均值：", sum(col2) / len(col2))
    print("中位数：", statistics.median(col2))


if __name__ == "__main__":
    make_file()
    analyze_second_column()
