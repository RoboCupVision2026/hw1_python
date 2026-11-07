f=open("test.txt",mode="rt")
content=f.read()
f.close
newcontent="python"+content+"python"
f=open("test.txt",mode="wt")
f.write(newcontent)
f.close()
