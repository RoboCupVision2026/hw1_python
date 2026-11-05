with open("test.txt", encoding="utf-8") as f:
    content = f.read()

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("python" + content + "python")