with open("test.txt", "r", encoding="ascii") as f1, open("copy_test.txt", "r", encoding="ascii") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
diff = []
max_len = max(len(lines1), len(lines2))
for idx in range(max_len):
    l1 = lines1[idx].rstrip("\n") if idx < len(lines1) else ""
    l2 = lines2[idx].rstrip("\n") if idx < len(lines2) else ""
    if l1 != l2:
        diff.append(idx + 1)
if diff:
    print("內容不相同的行號：", diff)
else:
    print("兩個文件所有行都一致")