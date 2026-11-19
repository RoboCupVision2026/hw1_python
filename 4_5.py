import random
import string
from pathlib import Path

current_dir = Path.cwd()
test_dir = current_dir / "test"

# 为了避免误修改旧文件，要求目录为空
# .iterdir()获取指定文件夹下的所有直接子项目
# any() 是 Python 内置函数，用于判断一个可迭代对象中是否至少存在一个为真的元素
if test_dir.exists() and any(test_dir.iterdir()):
    raise FileExistsError("test文件夹不为空，请先整理原有文件！") #raise是主动抛出异常

test_dir.mkdir(exist_ok=True)

# 2. 用户指定文件数量、每个文件的行数和每行长度
file_count = int(input("请输入创建的文件数量："))
line_count = int(input("请输入每个文件的行数："))
line_length = int(input("请输入每行随机字符的长度："))

if file_count <= 0 or line_count <= 0 or line_length <= 0:
    raise ValueError("输入必须为正整数！")

chars = string.ascii_letters + string.digits + string.punctuation + " "

for i in range(1, file_count + 1):

    file_path = test_dir / f"file_{i}.txt"

    with open(file_path, "w", encoding="ascii") as f:

        for j in range(line_count):
            content = ''.join(random.choices(chars, k=line_length))
            f.write(content + "\n")


# 4. 遍历目录下的所有文件
for file_path in list(test_dir.iterdir()):

    if file_path.is_file():

        # 读取所有行
        lines = file_path.read_text(encoding="ascii").splitlines()

        # 每一行末尾添加-python
        new_content = "\n".join(
            line + "-python" for line in lines
        )

        if lines:
            new_content += "\n"

        # 写回文件
        file_path.write_text(new_content, encoding="ascii")

        # 5. 修改文件名
        new_name = file_path.stem + "-python" + file_path.suffix

        new_path = file_path.with_name(new_name)

        file_path.rename(new_path)
