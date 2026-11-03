import os
import random
os.chdir(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(base_dir,'test')
os.mkdir(file_path)
i=int(input("请输入文件个数："))
j=int(input("请输入每个文件的行数："))

for k in range(i):
    with open(os.path.join(file_path,f"{k}.txt"), "w",encoding="utf-8") as f:
        for l in range(j):
            f.write("".join(chr(random.randint(32, 126)) for s in range(10)) + "\n")

for m in range(i):
    os.rename(os.path.join(file_path,f"{m}.txt"), os.path.join(file_path,f"{m}-python.txt"))
    with open(os.path.join(file_path,f"{m}-python.txt"), "r+",encoding="utf-8") as f:
        content=f.readlines()
        for n in range(j):
            content[n]=content[n].rstrip("\n")+"-python\n"
        f.seek(0)
        f.writelines(content)

       
