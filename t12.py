# 第二题：文件复制
import random
from pathlib import Path
import string

chars = string.ascii_letters+string.digits+string.punctuation

# create file
work_dir = Path(__file__).resolve().parent
file = work_dir/"test.txt"

# fill the file with random ascii characters
i = int(input("input the lines that the txt files have:"))
txt_k = 10
with open(file, "w", encoding="utf-8") as f:
    for _ in range(i):
        text_per_line = random.choices(chars, k=txt_k)
        f.write("".join(text_per_line)+'\n')
# copy the file
file_copy = work_dir/"copy_test.txt"
with open(file, "r", encoding="utf-8") as fr:
    with open(file_copy, "w", encoding="utf-8") as fw:
        txt = fr.read()
        fw.write(txt)
