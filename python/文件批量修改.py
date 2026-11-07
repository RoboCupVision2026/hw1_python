import os
import random
i = int(input("请输入创建的文件个数: "))
j = int(input("请输入每个文件的行数: "))
dir_name = "test"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
for file_idx in range(1, i + 1):
    file_name = f"{dir_name}/file_{file_idx}.txt"
    with open(file_name, "w") as f:
        for line_idx in range(j):
            f.write("随机内容\n")
all_files = os.listdir(dir_name)
for old_name in all_files:
    old_path = os.path.join(dir_name, old_name) 
    new_name = old_name.replace(".txt", "-python.txt")
    new_path = os.path.join(dir_name, new_name)
    os.rename(old_path, new_path) 
    with open(new_path, "r") as f:
        lines = f.readlines() 
    with open(new_path, "w") as f:
        for line in lines:
            line = line.strip() 
            f.write(line + "-python\n")
print("批量操作完成！")
