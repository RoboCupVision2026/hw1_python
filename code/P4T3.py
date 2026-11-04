import random
f=open("data.txt","r")
for i in range(100000):
    num=random.randint(1,100)
    f.write(f"{num}\n")
f.close()