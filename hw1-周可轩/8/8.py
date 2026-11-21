"""
随机数文件
题目： 创建文件data.txt，文件共100000行，每行存放一个随机的1～100之间的整数。
程序分析： random库
"""

import random as rd

with (open("data.txt", "w") as f):
    for i in range (100000):
        f.write(str(rd.randint(1, 100)) + "\n")

