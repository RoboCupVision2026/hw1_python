import random
import string
import shutil
print("请输入i的值：",end="")
n=int(input())
with open("test.txt","w") as f:
    for i in range(n):
        text="".join(random.choices(string.ascii_letters+string.digits+string.punctuation+" ",k=random.randint(1,50)))
        if i!=n-1:
            f.write(text+"\n")
        else:
            f.write(text)
shutil.copyfile("test.txt","copy_test.txt")
