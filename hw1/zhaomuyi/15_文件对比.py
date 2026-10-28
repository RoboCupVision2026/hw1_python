# 第十五题：文件对比
# 题目：读取 test.txt 和 copy_test.txt 内容，检查它们每一行内容是否相同，
#       输出所有不同的行号。
# 思路：两个文件按行读入列表，逐行比较（注意短的那个读完即止）。

def diff_lines(path_a="test.txt", path_b="copy_test.txt"):
    with open(path_a, "r", encoding="utf-8") as fa, \
         open(path_b, "r", encoding="utf-8") as fb:
        lines_a = fa.readlines()
        lines_b = fb.readlines()

    diff = []
    max_len = max(len(lines_a), len(lines_b))
    for i in range(max_len):
        a = lines_a[i] if i < len(lines_a) else "<无此行>"
        b = lines_b[i] if i < len(lines_b) else "<无此行>"
        if a != b:
            diff.append(i + 1)   # 行号从 1 开始
    return diff


if __name__ == "__main__":
    diff = diff_lines()
    if diff:
        print("两个文件不同的行号是：", diff)
    else:
        print("两个文件完全相同")
