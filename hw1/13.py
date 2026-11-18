with open("test.txt") as f:
    s = f.read()
with open("test.txt", "w") as f:
    f.write("python" + s + "python")
