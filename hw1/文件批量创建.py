import os
from random import randint
if not os.path.exists("test"):
	os.mkdir("test")
else:
	print("该目录已存在")
for j in range(3):
	filename=f"test/{j+1}.txt"
	with open(filename,mode="wt") as f:
		for i in range(10):
			f.write(str(randint(1,100)))
f_list=os.listdir("test")
for f_name in f_list:
	old_path=os.path.join("test",f_name)
	new_name=f_name+"-python"
	new_path=os.path.join("test",new_name)
	os.rename(old_path,new_path)
with open(new_path,mode="rt") as f:
	lines=f.readlines()
modified_lines=[]
for line in lines:
	modified_lines.append(line+"-python")
with open(new_path,mode="wt") as f:
	f.writelines(modified_lines)
