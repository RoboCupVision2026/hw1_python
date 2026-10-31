with open("test.txt", "r+", encoding="ascii") as f:
    f.seek(0)
    content = f.read()
    new_content = "python" + content + "python"
    f.seek(0)
    f.write(new_content)
    f.truncate()

print("已在 test.txt 開頭和末尾加上 python")