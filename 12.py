import random
i = int(input("输入行数 i: "))
with open('test.txt', 'w', encoding='utf-8') as f:
    for _ in range(i):
        length = random.randint(5, 20)
        # ASCII 可打印字符 33~126
        line = ''.join(chr(random.randint(33, 126)) for _ in range(length))
        f.write(line + '\n')
with open('test.txt', 'r', encoding='utf-8') as src, \
     open('copy_test.txt', 'w', encoding='utf-8') as dst:
    dst.write(src.read())
print("复制完成")