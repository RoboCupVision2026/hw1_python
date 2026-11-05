with open("test.txt", encoding="utf-8") as f1, open("copy.txt", encoding="utf-8") as f2:
    l1, l2 = f1.readlines(), f2.readlines()

for i, (a, b) in enumerate(zip(l1, l2), start=1):
    if a.strip() != b.strip():
        print(i)
if len(l1) != len(l2):
    for j in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
        print(j + 1)