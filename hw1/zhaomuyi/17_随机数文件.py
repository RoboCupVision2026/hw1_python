# 第十七题：随机数文件
# 题目：创建文件 data.txt，文件共 100000 行，每行存放一个随机的 1~100 之间的整数。

import random


def make_data(path="data.txt", n=100000):
    with open(path, "w", encoding="utf-8") as f:
        for _ in range(n):
            f.write("{}\n".format(random.randint(1, 100)))
    print("已生成 {}，共 {} 行".format(path, n))


if __name__ == "__main__":
    make_data()
