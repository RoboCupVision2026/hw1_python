#随机数文件
from random import randint
with open("data.txt","w",encoding="utf-8") as f:
    for i in range(100000):
        f.write(str(randint(1,100))+"\n")
