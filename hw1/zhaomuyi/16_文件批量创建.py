# 第十六题：文件批量创建
# 题目：在当前目录下新建 test 目录，在 test 目录中自建 i（由用户指定）个文件，
#       向文件中随机输入 j（由用户指定）行随机字符。然后遍历该目录下的所有文件，
#       并在所有文件名称和每一个文件的所有行后面增加 "python"。
# 说明：
#   - "文件名后面增加 python"：理解为把文件名改成 xxx_python.txt
#   - "每一行后面增加 python"：每行末尾追加字符串 python

import os
import random
import string

PRINTABLE = [chr(c) for c in range(33, 127)]


def batch_create(i=3, j=4, folder="test_batch"):
    os.makedirs(folder, exist_ok=True)
    # 第一步：建 i 个文件，每个 j 行随机字符
    for k in range(i):
        path = os.path.join(folder, "file_{}.txt".format(k))
        with open(path, "w", encoding="utf-8") as f:
            for _ in range(j):
                line = "".join(random.choice(PRINTABLE) for _ in range(10))
                f.write(line + "\n")

    # 第二步：遍历目录，每个文件每行末尾加 python，并重命名为 xxx_python.txt
    for name in os.listdir(folder):
        old_path = os.path.join(folder, name)
        if not os.path.isfile(old_path):
            continue
        # 行内容加 python
        with open(old_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(old_path, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line.rstrip("\n") + "python\n")
        # 文件名加 python
        new_path = os.path.join(folder, name.replace(".txt", "_python.txt"))
        os.rename(old_path, new_path)

    print("已在 {} 目录下创建 {} 个文件，每个 {} 行，并追加完毕".format(folder, i, j))


if __name__ == "__main__":
    batch_create(i=3, j=4)
