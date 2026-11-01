with open("test.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    print(f"读取全部内容后，文件指针位置：{f.tell()}")
    f.seek(0, 0)
    new_content = "python" + content + "python"
    f.write(new_content)
    print(f"写入完成后，文件指针位置：{f.tell()}")
