# 文件修改
with open("test.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    print("python" + content + "python", file = f)
    