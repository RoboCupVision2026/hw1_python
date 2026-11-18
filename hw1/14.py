with open("test.txt") as f:
    a = f.readlines()
with open("copy_test.txt") as f:
    b = f.readlines()

for i in range(max(len(a), len(b))):
    if i >= len(a) or i >= len(b) or a[i] != b[i]:
        print(i + 1)
