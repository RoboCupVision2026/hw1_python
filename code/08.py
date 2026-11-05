# ## 第八题

import random

with open("data.txt","w",encoding="utf-8")as file:
    for _ in range(100000):
        number= random.randint(1,100)
        file.write(str(number) + "\n")
print("data.txt","已生成")

