#文件批量创建
import os
import random
import string

path = os.getcwd()
if not os.path.exists(os.path.join(path,"test")):
    os.mkdir(os.path.join(path,"test"))
path = os.path.join(path,"test")

all_pool = string.ascii_letters+string.digits+string.punctuation
files = int(input("请输入随机文件数量"))
lines = int(input("请输入随机行的数量"))
for i in range(files):
    with open(os.path.join(path,str(i)+".txt"),"w",encoding="utf-8") as f:
        for j in range(lines):
            f.write("".join(random.choices(all_pool,k=20))+"\n")

file_names_list = os.listdir(path)
for i in range(files):
    with open(os.path.join(path,str(i)+".txt"),"r",encoding="utf-8") as f:
        content = f.readlines()
        for j in range(len(content)):
            content[j] = content[j].replace("\n","-python\n")
    with open(os.path.join(path,str(i)+".txt"),"w",encoding="utf-8") as f:
        f.write("".join(content))
for file_name in file_names_list:
    if not file_name.endswith("-python.txt"):
        new_name = file_name.replace(".txt","-python.txt")
        os.rename(os.path.join(path,file_name),os.path.join(path,new_name))