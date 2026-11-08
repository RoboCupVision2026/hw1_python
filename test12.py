import random
import string

def random_ascii_line():
    return ''.join(random.choices(string.ascii_letters,k=10))
i=input()
with open("test.txt","w") as f:
    for _ in range(int(i)):
        f.write(random_ascii_line()+"\n")
with open("copy_test.txt","w") as f1,open("test.txt","r")as f2:
    for lines in range(int(i)):
        line=f2.readline()
        f1.write(line)

