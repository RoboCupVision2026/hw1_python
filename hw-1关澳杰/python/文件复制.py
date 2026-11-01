import random
import string
i = int(input("需要输入几行内容："))
with open("data/test.txt","w",encoding = "utf-8") as f:
    chars = string.ascii_letters + string.digits + string.punctuation
    for j in range(i):
        text = random.choices(chars, k=10)
        f.write("".join(text)+"\n")
with open("data/test.txt","r",encoding = "utf-8") as f:
    content = f.read()
with open("data/copy_test.txt","w",encoding = "utf-8") as f:
    f.write(content)