# 在当前目录新建目录img，里面包含一百个文件名各不相同的png文件（X4G5.png）
import os
import random
import string

if not os.path.exists('img'):
    os.mkdir('img')

chars = list(string.ascii_uppercase + string.digits)
filesNames = set()

while len(filesNames) < 100:
    name = "".join(random.choices(chars, k=4))
    filesNames.add(name)

for name in filesNames:
    filePath = os.path.join('img', f"{name}.png")
    with open(filePath, 'w') as f:
        pass

