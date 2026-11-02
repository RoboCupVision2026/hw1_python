#文件改名
import os
import random
path=os.getcwd()
path_img=os.path.join(path,"img")
file_list=os.listdir(path_img)
random_files=random.sample(file_list,50)
for i in random_files:
    newname=i.replace(".png",".jpg")
    os.rename(os.path.join(path_img,i),os.path.join(path_img,newname))
