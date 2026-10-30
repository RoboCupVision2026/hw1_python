import os, random
i = int(input("文件数 i: "))
j = int(input("每个文件行数 j: "))
os.makedirs('test', exist_ok=True)
filenames = []
for n in range(i):
    fname = os.path.join('test', f'file{n}.txt')
    filenames.append(fname)
    with open(fname, 'w', encoding='utf-8') as f:
        for _ in range(j):
            length = random.randint(3, 10)
            line = ''.join(chr(random.randint(33, 126)) for _ in range(length))
            f.write(line + '\n')
for old_path in filenames:
    with open(old_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for ln in lines:
        ln = ln.rstrip('\n')
        new_lines.append(ln + '-python\n')
    dir_name, base = os.path.split(old_path)
    name, ext = os.path.splitext(base)
    new_path = os.path.join(dir_name, name + '-python' + ext)
    with open(new_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    os.remove(old_path)
print("批量创建与重命名完成")