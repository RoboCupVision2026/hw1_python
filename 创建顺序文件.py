import os
current_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(current_dir, "img")
os.makedirs(img_dir, exist_ok=True)
for i in range(1,101):
    filename = f"X4G5_{i}.png"
    filepath = os.path.join(img_dir, filename)

    with open(filepath, "wb") as f:
        pass
print("文件创建成功！")