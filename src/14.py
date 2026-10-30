with open("test.txt", "r") as file:
    content = file.read()
with open("test.txt", "w") as file:
    file.write("python" + content + "python")
