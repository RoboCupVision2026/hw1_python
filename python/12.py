import random
import string

i = int(input("行数："))
valid_chars = string.ascii_letters + string.digits + string.punctuation

with open("test.txt", "w", encoding="utf-8") as f:
    for _ in range(i):
        line = ''.join(random.choice(valid_chars) for _ in range(20))
        f.write(line + "\n")

with open("test.txt", "r", encoding="utf-8") as f1, open("copy_test.txt", "w", encoding="utf-8") as f2:
    f2.write(f1.read())
