import random
with open("data.txt","w") as f:
    for i in range(100000):
        f.write(str(random.randint(1,100))+"\n")
