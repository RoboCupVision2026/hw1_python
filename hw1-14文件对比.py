different_lines = []

with open('test.txt', 'r', encoding='utf-8') as f1, open('copy_test.txt', 'r', encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            different_lines.append(lines1.index(line1) + 1)

if different_lines:
    print(f"不同行的编号有：{different_lines}")
else:
    print("两个文件的内容完全相同。")