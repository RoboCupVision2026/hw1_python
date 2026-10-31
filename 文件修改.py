with open("test.txt", "r+") as f:
    content = f.read()

    f.seek(0)

    f.write("python" + content + "python")

print("文件修改完成")