#文件复制之复制文件
with open("test.txt","r",encoding="utf-8") as f:
    content = f.readlines()
with open("copy_test.txt","w",encoding="utf-8") as f:
    f.write("".join(content))