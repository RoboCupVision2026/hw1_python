import random
import os
f_names=os.listdir("img")
selected_files=random.sample(f_names,50)
for name in selected_files:
	old_path=os.path.join("img",name)
	new_name=name.replace(".png",".jpg")
	new_path=os.path.join("img",new_name)
	os.rename(old_path,new_path)
