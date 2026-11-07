from random import randint
file=open("test.txt",mode="wt")
line1=""
line2=""
for n in range(10):
	char=chr(randint(33,126))
	line1=line1+char
for n in range(10):
        char=chr(randint(33,126))
        line2=line2+char 
line=line1+"\n"+line2
file.write(line)
file.close()
file=open("test.txt",mode="rt")
content=file.read()
file.close()
f=open("copy_test.txt",mode="wt")
f.write(content)
f.close()
