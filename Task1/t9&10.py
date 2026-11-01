from pathlib import Path
import random
import string
import shutil
img_dir=Path(__file__).resolve().parent/"img"
if img_dir.exists():
    shutil.rmtree(img_dir)
img_dir.mkdir()
#t9
i=0
while i!=100:
    filename="".join(random.choices(string.ascii_uppercase+string.digits,k=4))+".png"
    if not (img_dir/filename).exists():
        filepath=img_dir/filename
        filepath.touch()
        i+=1
#t10
files=list(img_dir.iterdir())
for i in random.sample(files,50):
    i.rename(i.with_suffix(".jpg"))

