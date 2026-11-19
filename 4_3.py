from pathlib import Path

file_path = Path.cwd() / "test.txt"

# r+: 以读写模式打开文件,不清空原文件
with open(file_path, "r+", encoding="ascii") as f:

    content = f.read()  #读取全部内容

    print("当前指针位置：", f.tell())  #tell()获取当前文件指针的位置标记

    f.seek(0)

    #write会覆盖当前文件指针的内容
    f.write("python" + content + "python")


