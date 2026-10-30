with open('test.txt', 'r', encoding='utf-8') as fa, \
     open('copy_test.txt', 'r', encoding='utf-8') as fb:
    la = fa.readlines()
    lb = fb.readlines()
diff_lines = []
max_len = max(len(la), len(lb))
for idx in range(max_len):
    s1 = la[idx] if idx < len(la) else None
    s2 = lb[idx] if idx < len(lb) else None
    if s1 != s2:
        diff_lines.append(idx + 1)
print("不同的行编号:", diff_lines)