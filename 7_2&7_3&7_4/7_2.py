import os
import random
import string
cr_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(cr_dir, "text.txt")
n = int(input("输入文件行数："))
with open(text_dir,"w") as f:
    for i in range(n):
        f.write("".join(random.choice([chr(k) for k in range(32, 126)]) for _ in range(random.randint(5, 10))) + "\n")
text_copy_dir = os.path.join(cr_dir, "text_copy.txt")
with open(text_dir,"r") as f:
    with open(text_copy_dir,"w") as f1:
        for line in f:
            f1.write(line)