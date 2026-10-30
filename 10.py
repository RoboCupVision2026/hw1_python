import os
import random
folder = r"D:\robocup\week1\img"
files = [f for f in os.listdir(folder)
         if os.path.isfile(os.path.join(folder, f))]
choose = random.sample(files, min(50, len(files)))
for f in choose:
    old_path = os.path.join(folder, f)
    name, ext = os.path.splitext(f)
    if ext.lower() == '.jpg':
        continue
    new_path = os.path.join(folder, name + '.jpg')
    i = 1
    while os.path.exists(new_path):
        new_path = os.path.join(folder, f"{name}_{i}.jpg")
        i += 1
    os.rename(old_path, new_path)
    print(f"{f} -> {os.path.basename(new_path)}")
print("完成，共处理", len(choose), "个文件")