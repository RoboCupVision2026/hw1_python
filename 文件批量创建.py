import os
import random
import string
i = int(input("i="))
j = int(input("j="))
if not os.path.exists("test"):8
    os.mkdir("test")
file_list = []
for idx in range(i):
    filename = f"file_{idx+1}.txt"
    filepath = os.path.join("test", filename)
    file_list.append((filename, filepath))
    with open(filepath, "w", encoding="utf-8") as f:
        for _ in range(j):
            line_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            f.write(line_str + "\n")
for old_name, old_path in file_list:
    with open(old_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_content = [line.rstrip("\n") + "-python\n" for line in lines]
    with open(old_path, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    name_part, ext = os.path.splitext(old_name)
    new_name = f"{name_part}-python{ext}"
    new_path = os.path.join("test", new_name)
    os.rename(old_path, new_path)
