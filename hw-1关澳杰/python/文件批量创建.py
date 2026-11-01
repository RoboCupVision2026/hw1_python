import os
import random
import string
os.makedirs("test",exist_ok=True)
i = int(input("创建文件的个数："))
j = int(input("输入的行数："))
chars = string.ascii_letters + string.digits
for k in range(i+10):
    name = "test." +str(k)+".txt"
    with open(f"test/{name}","w",encoding="utf-8") as f:
        for l in range(j):
            f.write("".join(random.choices(chars,k = 10))+"\n")
text_names = os.listdir("test")
for name in text_names:
    with open(f"test/{name}","r",encoding="utf-8") as f:
        content1 = f.read()
        content2 = content1.replace("\n","-python\n")
    with open(f"test/{name}","w",encoding="utf-8") as f:
        f.write(content2)
    name2 = name.replace(".txt","-python.txt")
    os.rename(f"test/{name}",f"test/{name2}")

