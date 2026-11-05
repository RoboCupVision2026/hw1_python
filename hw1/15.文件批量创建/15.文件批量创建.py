from pathlib import Path 
import random 
import string

def createOneFile(rootDir,row):   #在rootDir\创建一个row行的文件   #已成功运行过
    namePool=string.ascii_letters+string.digits
    contentPool=string.ascii_letters+string.digits+string.punctuation
    randomName="".join([random.choice(namePool) for _ in range(4)])+".txt"  #名字为四个随机英文字母或数字
    with open(rootDir/randomName,"w",encoding="utf-8")as f:
        for l in range(row):
            f.write("".join([random.choice(contentPool) for _ in range(random.randint(1,20))])) #每行1~20个随机字符
            if l != row-1:
                f.write("\n")
#createOneFile(Path(__file__).parent,10)

#创建i个以上j行文件
i=int(input("请输入至少要创建的文件数:"))
j=int(input("请输入文件行数:"))
targetPath=Path(__file__).parent/"test"
targetPath.mkdir(exist_ok=True)
for _ in range(i+random.randint(0,10)): #比输入随机多0~10个
    createOneFile(targetPath,j)


#遍历所有文件，在文件名和文件里每行最后加-python
allFiles=list(targetPath.glob("*"))
#注：Path方法：name为全名，stem为去后缀名，suffix为后缀
'''for old in allFiles:
    newStem=old.stem+"-python"
    new=old.with_stem(newStem)
    old.rename(new)
#已将所有文件名后+"-python"     #已成功运行过'''

for oldFile in allFiles:
    newFile=oldFile.with_stem(oldFile.stem+"-python")
    with open(oldFile,"r",encoding="utf-8")as fOld:
        with open(newFile,"w",encoding="utf-8")as fNew:
            for line in fOld:
                fNew.write(line.strip()+"-python"+"\n")
    oldFile.unlink()