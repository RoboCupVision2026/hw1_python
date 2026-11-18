import random

n = int(input())
with open("test.txt", "w") as f:
    for i in range(n):
        f.write("".join(chr(random.randint(32, 126)) for j in range(20)) + "\n")

with open("test.txt") as f, open("copy_test.txt", "w") as g:
    g.write(f.read())
