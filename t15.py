# 第五题：文件批量创建
import os
from pathlib import Path
import random
import string

chars = string.ascii_letters+string.digits

base_dir = Path(__file__).resolve().parent
test_dir = base_dir/"test"
test_dir.mkdir(exist_ok=True)

i = int(input("新建文件数："))
j = int(input("新建文件的行数："))
txt_k = 10
# create files
for _i in range(i):
    file_dir = test_dir/f"file{_i+1}.txt"
    with open(file_dir, "w", encoding="utf-8") as f:
        for _ in range(j):
            content = "".join(random.choices(chars, k=txt_k))+'\n'
            f.write(content)

# modify files
for file in os.listdir(test_dir):
    file_dir = test_dir/file
    with open(file_dir, "r", encoding="utf-8") as f:
        content = "".join([line.rstrip()+"-python\n" for line in f.readlines()])
    
    with open(file_dir, "w", encoding="utf-8") as f:
        f.write(content)

    name,ext=os.path.splitext(file)
    new_path=name+"-python"+ext
    os.rename(file_dir,new_path)