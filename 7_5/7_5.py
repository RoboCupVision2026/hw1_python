import os
import random
cr_dir = os.path.dirname(os.path.abspath(__file__))
test_dir = os.path.join(cr_dir, "test")
if not os.path.exists(test_dir):
    os.makedirs(test_dir)
n = int(input("创建文件的数量："))
m = int(input("创建文件的行数："))
for i in range(n):
    with open(os.path.join(test_dir, f"test_{i+1}.txt"), "w") as f:
        for j in range(m):
            f.write("".join(random.choice([chr(k) for k in range(32, 126)]) for _ in range(random.randint(5, 10))) + "\n")

for i in range(n):
    old_file_path = os.path.join(test_dir, f"test_{i+1}.txt")
    new_file_path = os.path.join(test_dir, os.path.splitext(f"test_{i+1}.txt")[0] + "-python.txt")
    os.rename(old_file_path, new_file_path)
    with open(new_file_path, "r+") as f:
        old_lines = f.readlines()
        f.seek(0)
        for line in old_lines:
            f.write(line.strip() + "-python\n")