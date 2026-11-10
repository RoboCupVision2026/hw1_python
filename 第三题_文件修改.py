# 第三题：文件修改
#
# 题目：读取上述test.txt的文件内容，分别在文件的开头和结尾处追加字符串python。
from pathlib import Path
wenjian = Path(__file__).resolve().parent / "test.txt"
with open(wenjian, "r" ,encoding="utf-8")as file:
    content = file.read()
with open (wenjian, "w" ,encoding="utf-8")as file:
    content = "python" + content + "python"
    file.write(content)
