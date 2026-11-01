with open("test.txt", "r", encoding="utf-8") as f1, open("copy_test.txt", "r", encoding="utf-8") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

max_len = max(len(lines1), len(lines2))
for i in range(max_len):
    l1 = lines1[i].strip() if i < len(lines1) else ""
    l2 = lines2[i].strip() if i < len(lines2) else ""
    if l1 != l2:
        print(f"第{i+1}行不相同")
