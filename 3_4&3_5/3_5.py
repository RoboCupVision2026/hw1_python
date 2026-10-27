import os
import random 
cr_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(cr_dir, "img")
all_img_nm = os.listdir(img_dir)
selected_img_nm = random.sample(all_img_nm, 50)
for name in selected_img_nm:
    old_path = os.path.join(img_dir,name)
    new_name = os.path.splitext(name)[0]+".jpg"
    os.rename(old_path, os.path.join(img_dir,new_name))