import string
import os
import random

file_paths = []
os.makedirs("img", exist_ok=True)
chars = string.ascii_letters + string.digits
for i in range(0,100):
    name = "".join(random.choices(chars,k = 4))
    file_path = f"img/{name}.png"
    file_paths.append(file_path)
    with open(file_path, "w") as f:
        pass


#先选50个File——path出来
file_changes = random.sample(file_paths,50)
for file_change in file_changes:
    File_change = file_change.replace("png","jpg")
    print(File_change)



