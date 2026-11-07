with open("test.txt", "r") as f:
    content = f.read()
new_content = "python\n" + content + "\npython"
with open("test.txt", "w") as f:
    f.write(new_content)
