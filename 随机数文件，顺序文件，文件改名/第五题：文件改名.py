# 将随机的50个文件改为.jpg结尾
import random
import os

allFiles = os.listdir('img')
renameFiles = random.sample(allFiles, 50)

for file in renameFiles:
    oldPath = os.path.join('img', file)
    name, ext = os.path.splitext(file)
    newPath = os.path.join('img', name + '.jpg')
    os.rename(oldPath, newPath)