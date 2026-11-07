from random import randint
f=open("data.txt",mode="wt")
for i in range(100000):
	n=randint(1,100)
	f.write(str(n)+"\n")
