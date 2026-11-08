import  os
import random

imgdir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"img")
allfiles=os.listdir(imgdir)
selectedfiles=random.sample(allfiles,50)
for file in selectedfiles:
    oldpath=os.path.join(imgdir,file)
    newname=os.path.splitext(file)[0]+".jpg"
    newpath=os.path.join(imgdir,newname)
    os.rename(oldpath,newpath)