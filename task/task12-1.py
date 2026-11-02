#文件复制之创建初始文件
import random
import string
all_pool = string.ascii_letters + string.digits + string.punctuation
rows = int(input("输入你想要的行数"))
with open("test.txt","w",encoding="utf-8") as f:
    for i in range(rows):
        line="".join(random.choices(all_pool,k=20))+"\n"
        f.write(line)