import random
i=int(input("please enter the number of lines:"))
f=open("test.txt","w")
for j in range(i):
    line=""
    for k in range(20):
        c=chr(random.randint(32,126))
        line=line+c
    f.write(line+"\n")
f.close()

f1=open("test.txt","r")
a=f1.read()
f1.close()

f2=open("copy_test.txt","w")
f2.write(a)
f2.close()