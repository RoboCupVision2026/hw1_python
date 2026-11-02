#创建顺序文件
import os
path = os.getcwd()
if not os.path.exists(os.path.join(path,"img")):
    os.mkdir(os.path.join(path,"img"))
for i in range(100):
    filename = str(i)+".png"
    with open(os.path.join(path,"img",filename),"w") as f:
        f.write(str(i))
