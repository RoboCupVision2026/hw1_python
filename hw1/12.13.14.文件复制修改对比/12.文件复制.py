import random
from pathlib import Path
import string

#随机文件生成
i=int(input("请输入生成的文件的行数（正整数）："))
charPool=string.ascii_letters+string.punctuation+string.digits

def generateOneLine():
    while True:
        strs=[random.choice(charPool) for _ in range(random.randint(1,50))]
        yield "".join(strs)

filePath=Path(__file__).parent/"test.txt"
with open(filePath,"w",encoding="utf-8")as f:
    gen=generateOneLine()
    for k in range(i):
        f.write(next(gen))
        if k != i-1:
            f.write("\n")

newPath=Path(__file__).parent/"copy_test.txt"
newPath.write_bytes(filePath.read_bytes())