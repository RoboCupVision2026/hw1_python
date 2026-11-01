# 创建文件data.txt，输入100000行1到100的随机整数
import random

with open ("data.txt", 'w', encoding='utf-8') as f:
    for _ in range(100000):
        f.write(str(random.randint(1, 101)))
        f.write('\n')