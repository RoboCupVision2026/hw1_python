# 对比test.txt和copy_test.txt有哪几行不一样
with open("generatedFiles/test.txt", "r", encoding='utf-8') as f1, \
    open("generatedFiles/copy_test.txt", "r", encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    maxLen = max(len(lines1), len(lines2))
    for i in range(maxLen):
        if i < len(lines1):
            line1 = lines1[i].strip()
        else:
            line1 = ""

        if i < len(lines2):
            line2 = lines2[i].strip()
        else:
            line2 = ""

        if line1 != line2:
            print(f"第{i + 1}行内容不一样")
