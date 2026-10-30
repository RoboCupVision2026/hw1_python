from itertools import zip_longest

with open("test.txt", "r") as file:
    lines1 = file.readlines()
with open("copy_test.txt", "r") as file:
    lines2 = file.readlines()

for i, (line1, line2) in enumerate(zip_longest(lines1, lines2), 1):
    if line1 != line2:
        print(i)
