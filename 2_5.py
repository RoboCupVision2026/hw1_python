#创建顺序文件
import random
import string
from pathlib import Path

# 获取当前.py文件所在目录
current_dir = Path(__file__).resolve().parent
print(current_dir)

# 创建img文件夹
img_dir = current_dir / "img"
#mkdir() 是 Path 对象的方法，专门用于创建文件夹。
# 参数：如果文件夹已经存在，就不报错；如果不存在，就创建它。
img_dir.mkdir(exist_ok=True)

# 字符集合：大写字母和数字
chars = string.ascii_uppercase + string.digits

# 创建100个不同名称的文件
names = set()

while len(names) < 100:
    #random.choices(序列, k=数量)：从给定序列中随机选择（可重复）指定数量的元素
    #连接符.join(字符串列表)  连接字符串
    name = ''.join(random.choices(chars, k=4))

    file_path = img_dir / (name + ".png")

    #如果文件名不重复且img文件夹中不存在同名文件就创建文件
    if name not in names and not file_path.exists():
        file_path.touch()   #创建空文件夹
        names.add(name)
