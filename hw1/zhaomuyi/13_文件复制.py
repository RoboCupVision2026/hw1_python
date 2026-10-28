# 第十三题：文件复制
# 题目：在工作目录下写程序创建一个文件 test.txt，并随机生成 i 行内容
#       （包含 ASCII 标准的任意非控制字符）。写程序实现该文件的拷贝，
#       拷贝文件命名为 copy_test.txt。
# 思路：非控制字符的可打印 ASCII 范围是 chr(33)~chr(126)。

import random
import string

# 可打印的非控制字符（去掉空格 chr(32)）：33~126
PRINTABLE = [chr(c) for c in range(33, 127)]


def make_test_txt(i=5, path="test.txt"):
    with open(path, "w", encoding="utf-8") as f:
        for _ in range(i):
            line = "".join(random.choice(PRINTABLE) for _ in range(20))
            f.write(line + "\n")


def copy_file(src="test.txt", dst="copy_test.txt"):
    with open(src, "r", encoding="utf-8") as fin, \
         open(dst, "w", encoding="utf-8") as fout:
        fout.write(fin.read())


if __name__ == "__main__":
    make_test_txt(i=5)
    copy_file()
    print("已生成 test.txt 并复制为 copy_test.txt")
