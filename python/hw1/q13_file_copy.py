import random
import shutil
import string
from pathlib import Path


def read_count(default=10):
    try:
        text = input("请输入要生成的行数: ").strip()
    except EOFError:
        text = ""
    if not text.isdigit() or int(text) <= 0:
        print(f"没有输入有效行数，改用默认值 {default}")
        return default
    return int(text)


def create_test_file(path, rows):
    printable = "".join(ch for ch in string.printable if ch not in "\t\n\r\x0b\x0c")
    with path.open("w", encoding="utf-8") as file:
        for _ in range(rows):
            length = random.randint(5, 20)
            file.write("".join(random.choice(printable) for _ in range(length)) + "\n")


def main():
    rows = read_count()
    work_dir = Path.cwd()
    source = work_dir / "test.txt"
    target = work_dir / "copy_test.txt"

    create_test_file(source, rows)
    shutil.copyfile(source, target)

    print(f"已创建 {source}，共 {rows} 行随机 ASCII 可打印字符")
    print(f"已复制为 {target}")
    with source.open(encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            print(f"  {index}: {line.rstrip()}")
    print(f"两个文件大小: {source.stat().st_size} 字节 / {target.stat().st_size} 字节")
    print(f"内容完全相同: {source.read_bytes() == target.read_bytes()}")


if __name__ == "__main__":
    main()
