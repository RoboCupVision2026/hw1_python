# 创建test目录，在该目录下创建i个以上的文件，项文件中随即输入j行随机字符。
# 然后遍历该目录下的文件，并在所有文件的文件名，和每一个文件的所有行后面都增加python
import os
import random
import string

i = int(input("请输入你想要的文件数量："))
j = int(input("你想要让每个文件中有多少行："))
chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
if not os.path.exists('test'):
    os.mkdir('test')

for k in range(i):
    with open(os.path.join('test', f"file{k}.txt"), 'w', encoding='utf-8') as f:
        for _ in range(j):
            randomLine = "".join(random.choice(chars) for u in range(10))
            f.write(randomLine)
            f.write('\n')

for file in os.listdir('test'):
    with open(os.path.join('test', file), 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(os.path.join('test', file), 'w', encoding='utf-8') as f:
        for line in lines:
            newLine = line.strip() + "-python\n"
            f.write(newLine)
    name, txt = os.path.splitext(file)
    newName = name + "-python" + txt
    os.rename(os.path.join('test', file), os.path.join('test', newName))