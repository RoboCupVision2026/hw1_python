import random
import os
if not os.path.exists("img"):
	os.mkdir("img")
else:
	print("该目录已存在")
names=set()
while len(names)<100:
	names_str=""
	for n in range(4):
		chars="QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
		names_str=names_str+random.choice(chars)
	names.add(names_str+".png")
for name in names:
	f_path=os.path.join("img",name)
	with open(f_path,mode="wt") as f:
		pass
