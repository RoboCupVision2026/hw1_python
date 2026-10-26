# 第三题：文件修改
import os

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = "python"+content+"python"

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(content)
