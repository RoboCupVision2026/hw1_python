from pathlib import Path
import random
import string 

currentDir=Path(__file__).parent#获取当前文件的根目录
imgPath=currentDir/"img"
imgPath.mkdir(exist_ok=True)
#已创建/img
charsPool=string.ascii_letters+string.digits  #字符池
fileNames=set()#集合，不包括重复的元素
while len(fileNames)<=100:
    randomName="".join(random.choices(charsPool,k=4))+".png"#生成随机文件名
    if randomName in fileNames:#去重
        continue
    fileNames.add(randomName)#放入集合
    randomPath=imgPath/randomName#新文件的路径
    randomPath.touch()#创建新文件