with open("data/test.txt","r+",encoding = "utf-8") as f:
    content = f.read()
    f.seek(0)
    f.write("python" + content + "python")