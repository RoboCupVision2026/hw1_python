from itertools import zip_longest

with open("test.txt", "r") as f1, open("copy_test.txt", "r") as f2:
    for i, (line1, line2) in enumerate(
        zip_longest(f1, f2), start=1
    ):
        if line1 != line2:
            print("第", i, "行不同")