import os
import random
current_dir = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(current_dir, "img")
files = [
    filename for filename in os.listdir(img_dir)
    if filename.endswith(".png")
]
selected_files = random.sample(files, 50)
for filename in selected_files:
    old_path = os.path.join(img_dir, filename)
    new_filename = filename[:-4] + ".jpg"
    new_path = os.path.join(img_dir, new_filename)

    os.rename(old_path, new_path)
print("随机改名完成！")