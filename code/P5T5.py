import os
import random

def randline():
    s=""
    for k in range(10):
        num=random.randint(32, 126)
        s=s+chr(num)
    return s
i=int(input("number of files:"))
j=int(input("number of lines:"))

if not os.path.exists("test"):
    os.mkdir("test")

for n in range(1,i+1):
    path="test/"+str(n)+".txt"
    f=open(path,"w")
    for m in range(j):
        line = randline()
        f.write(line+"\n")
    f.close()

filelist=os.listdir("test")
for name in filelist:
    oldpath="test/"+name
    f=open(oldpath,"r")
    allline=f.readlines()
    f.close()
    newcontent=""
    for one in allline:
        one=one.strip("\n")
        newcontent=newcontent+one+"-python"+"\n"
    f=open(oldpath,"w")
    f.write(newcontent)
    f.close()

    dot=name.find(".")
    namefront=name[:dot]
    nameback=name[dot:]
    newname=namefront+"-python"+nameback
    newpath="test/"+newname
    os.rename(oldpath,newpath)