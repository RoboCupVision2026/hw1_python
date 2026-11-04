f=open("test.txt","r")
data=f.read()
f.close()
newdata="python"+data+"python"
f=open("test.txt","w")
f.write(newdata)
f.close()