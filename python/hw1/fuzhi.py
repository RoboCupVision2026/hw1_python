import random
import string

n = int(input())

ascii_chars = string.ascii_letters + string.digits + string.punctuation

with open("test.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        m = random.randint(10, 30)
        line = "".join(random.choice(ascii_chars) for i in range(m))
        f.write(line + "\n")

with open("test.txt", encoding="utf-8") as src, \
     open("copy.txt", "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line)