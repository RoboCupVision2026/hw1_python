from pathlib import Path
import random
import string

i = int(input("文件数量："))
j = int(input("行数："))
test_dir = Path("test")
test_dir.mkdir(exist_ok=True)
chars = string.ascii_letters + string.digits + string.punctuation

file_list = []
for n in range(i):
    raw_name = f"{n}.txt"
    file_path = test_dir / raw_name
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(j):
            line = ''.join(random.choice(chars) for _ in range(15))
            f.write(line + "\n")
    file_list.append(file_path)

for old_path in file_list:
    with open(old_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    new_lines = [line.rstrip("\n") + "-python\n" for line in lines]
    with open(old_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    stem = old_path.stem
    suffix = old_path.suffix
    new_name = f"{stem}-python{suffix}"
    new_path = old_path.parent / new_name
    old_path.rename(new_path)
