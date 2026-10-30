import random
import string

ascii_chars = ''.join(c for c in string.printable if c not in '\t\n\r\x0b\x0c')
i = int(input())

with open('test.txt', 'w', encoding='utf-8') as f:
    for j in range(i):
        line = ''.join(random.choices(ascii_chars, k=15))
        f.write(line + '\n')

with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()

with open('copy_test.txt', 'w', encoding='utf-8') as f:
    f.write(content)