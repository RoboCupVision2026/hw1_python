import os
import random
folder="./random image"
pnglist=[]
for name in os.listdir(folder):
    if name.endswith(".png"):
        pnglist.append(name)
select=random.sample(pnglist,k=50)
for name in select:
    path=os.path.join(folder,name)
    newname=name.replace(".png",".jpg")
    newpath=os.path.join(folder,newname)
    os.rename(path,newpath)