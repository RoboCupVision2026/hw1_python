import os
import random
import string
cr_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(cr_dir, "img")
if not os.path.exists(img_dir):
    os.makedirs(img_dir)
img_nm=set()
while len(img_nm)<100:
    img_nm.add(''.join(random.choices(string.ascii_letters+string.digits,k=4))+".png" )
for name in img_nm:
    open(os.path.join(img_dir,name),"w")