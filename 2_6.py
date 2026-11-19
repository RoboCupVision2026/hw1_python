#文件改名
import random
from pathlib import Path

# 获取img文件夹路径
current_dir = Path(__file__).resolve().parent
img_dir = current_dir / "img"

# 获取所有png文件
#glob() 是 Path 对象的方法，用于按照指定的模式查找文件
#glob返回的是可迭代的对象,list()把查找结果转换成列表

files = list(img_dir.glob("*.png"))

# 随机选择50个文件
#random.sample(序列, k)表示从一个序列中随机抽取 k 个不同的元素
selected_files = random.sample(files, 50)

# 修改文件扩展名
for file in selected_files:
    #with_suffix() 是 Path 对象的方法，用来生成一个扩展名不同的新路径
    new_file = file.with_suffix(".jpg")
    file.rename(new_file)
