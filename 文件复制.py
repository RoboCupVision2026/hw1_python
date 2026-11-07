import random
i = int(input())
with open("test.txt", "w", encoding="ascii") as f:
    for _ in range(i):
        line = ''.join(chr(random.randint(32, 126)) for _ in range(20))
        f.write(line + "\n")
with open("test.txt", "r", encoding="ascii") as fr, open("copy_test.txt", "w", encoding="ascii") as fw:
    fw.write(fr.read())
