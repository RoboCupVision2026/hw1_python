from pathlib import Path
from itertools import zip_longest

# 文件路径
current_dir = Path.cwd()

file1 = current_dir / "test.txt"
file2 = current_dir / "copy_test.txt"

different_lines = []

# 同时打开两个文件,"\"表示续行
with open(file1, "r", encoding="ascii") as f1, \
     open(file2, "r", encoding="ascii") as f2:

    # 同时遍历两个文件
    # zip_longest将两个序列中相同位置的元素配对，即使两个序列长度不同，
    # 也会继续遍历较长的那个
    # 如果某个序列已经结束，就用 None 补充
    # enumerate可以在遍历元素时，同时获得元素的序号
    for row, (line1, line2) in enumerate(
        zip_longest(f1, f2, fillvalue=None), start=1
    ):

        if line1 is None or line2 is None:
            different_lines.append(row)

        #rstrip() 是字符串的方法，用于删除字符串末尾指定的字符,此处删去回车换行
        elif line1.rstrip("\r\n") != line2.rstrip("\r\n"):
            different_lines.append(row)

print("不同的行号：", different_lines)
