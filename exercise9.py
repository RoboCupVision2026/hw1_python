import os
base_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base_dir, "img")
os.makedirs(img_dir, exist_ok=True) 
for i in range(1, 101):
    file_path = os.path.join(img_dir, str(i) + ".txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("这是第 " + str(i) + " 个文件")
