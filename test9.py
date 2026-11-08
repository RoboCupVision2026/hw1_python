import os
import string
import random

currentdir=os.path.dirname(os.path.abspath(__file__))
imgdir=os.path.join(currentdir,"img")
if not os.path.exists(imgdir):
    os.makedirs(imgdir)
files=set()
while len(files)<100:
    name="".join(random.choices(string.ascii_uppercase+string.digits,k=4))+".png"
    if name not in files:
        files.add(name)
        filepath=os.path.join(imgdir,name)
        open(filepath,'w').close