with open("test.txt","r") as f1:
    contents=f1.read()
new_contents="python\n"+contents+"python"
with open("test.txt","w") as f1:
    f1.write(new_contents)