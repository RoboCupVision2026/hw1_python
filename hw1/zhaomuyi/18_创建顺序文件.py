# 第十八题：创建顺序文件
# 题目：在当前 .py 文件目录下新建目录 img，里面包含 100 个文件，
#       100 个文件名各不相同（形如 X4G5.png，即 4 位随机大写字母/数字）。

import os
import random
import string


def random_name(length=4):
    chars = string.ascii_uppercase + string.digits   # 26 个大写字母 + 10 个数字
    return "".join(random.choice(chars) for _ in range(length))


def make_img_dir(folder="img", count=100):
    os.makedirs(folder, exist_ok=True)
    names = set()
    while len(names) < count:
        names.add(random_name() + ".png")
    for name in names:
        open(os.path.join(folder, name), "w").close()   # 创建空文件
    print("已在 {} 目录下创建 {} 个空文件，文件名形如 X4G5.png".format(folder, count))


if __name__ == "__main__":
    make_img_dir()
