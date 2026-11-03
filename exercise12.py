import os
import random
import shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path="test.txt"
i=int(input("请输入要生成的行数："))
lines=10
with open(file_path, "w", encoding="utf-8") as file:
    for r in range(i):
        line=""
        for l in range(lines):
            s=random.randint(32, 126)
            line+=chr(s)+" "
        file.write(line+"\n")
source_file = "test.txt"
copy_file = "copy_test.txt"
shutil.copy(source_file, copy_file)

