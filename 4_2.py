#文件复制
import random
import string
import shutil
from pathlib import Path

current_dir = Path.cwd()

test_file = current_dir / "test.txt"
copy_file = current_dir / "copy_test.txt"

n = int(input("请输入生成的行数："))
m = int(input("请输入每行字符数："))

#英文字母+数字+标点符号
chars = string.ascii_letters + string.digits + string.punctuation + " "

with open(test_file, "w", encoding="ascii") as f:
    for i in range(n):
        content = ''.join(random.choices(chars, k=m))
        f.write(content + "\n")

#shutil 是 Python 的高级文件操作模块
shutil.copy2(test_file, copy_file)
