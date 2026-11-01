# 在test.txt里随机生成i行ASCll字符
import string
import random

i = int(input("请输入你想要生成多少行数据："))
chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
with open("generatedFiles/test.txt", 'w', encoding='utf-8') as f:
    for j in range(i):
        randomLine = "".join(random.choice(chars) for _ in range(20))
        f.write(f"{randomLine}\n")

# 拷贝到copy_test.txt
with open("generatedFiles/test.txt", 'r', encoding='utf-8') as f:
    with open("generatedFiles/copy_test.txt", 'w', encoding='utf-8') as fw:
        for line in f:
            fw.write(line)