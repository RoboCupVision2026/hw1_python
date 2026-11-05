# ## 第十题

from pathlib import Path
folder= Path.cwd()/ "img"
paths= folder.glob("*.png")
files= list(paths)
import random
p= random.sample(files,50)
for old in p:
    new= old.with_suffix(".jpg")
    old.rename(new) 
print("已完成")

