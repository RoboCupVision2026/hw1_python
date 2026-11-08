import os
import random
import string

currentdir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(currentdir,"test"),exist_ok=True)
i=int(input("创建文件的个数:"))
j=int(input("文件的行数:"))
for a in range(i):
    filepath=os.path.join(currentdir,'test',f"file{a}.txt")
    with open(filepath,'w') as f:
        for b in range(j):
            f.write(''.join(random.choices(string.ascii_uppercase+string.digits,k=10))+'\n')
for filename in os.listdir(os.path.join(currentdir,'test')):
    newfilename=filename.replace(".txt",".txt.python")
    oldpath=os.path.join(currentdir,'test',filename)
    newpath=os.path.join(currentdir,'test',newfilename)
    os.rename(oldpath,newpath)
    with open(os.path.join(currentdir,'test',newfilename),'r') as f:
        contents=[line.strip()+'python' for line in f.readlines()]
    with open(os.path.join(currentdir,'test',newfilename),'w') as f:
        f.write('\n'.join(contents))





