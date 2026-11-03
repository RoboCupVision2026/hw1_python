with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("python" + text + "python")

print("修改完成")
