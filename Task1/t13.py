txt=""
with open("test.txt","r") as f:
    txt="python\n"+f.read()+"\npython"
with open("test.txt","w") as f:
    f.write(txt)