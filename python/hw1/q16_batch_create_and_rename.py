import random
import string
from pathlib import Path

SUFFIX = "-python"
ALPHABET = string.ascii_letters + string.digits


def read_positive(prompt, default):
    try:
        text = input(prompt).strip()
    except EOFError:
        text = ""
    if not text.isdigit() or int(text) == 0:
        print(f"没有输入有效数字，改用默认值 {default}")
        return default
    return int(text)


def random_text(length=8):
    return "".join(random.choice(ALPHABET) for _ in range(length))


def create_batch(directory, file_count, line_count):
    directory.mkdir(exist_ok=True)
    for index in range(1, file_count + 1):
        path = directory / f"note_{index:03d}.txt"
        content = "\n".join(random_text() for _ in range(line_count))
        path.write_text(content + "\n", encoding="utf-8")


def append_everywhere(directory):
    renamed = []
    for path in sorted(directory.iterdir()):
        if not path.is_file() or path.stem.endswith(SUFFIX):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        path.write_text("\n".join(line + SUFFIX for line in lines) + "\n", encoding="utf-8")
        new_path = path.with_name(path.stem + SUFFIX + path.suffix)
        path.rename(new_path)
        renamed.append(new_path.name)
    return renamed


def main():
    file_count = read_positive("请输入要创建的文件个数 i: ", 5)
    line_count = read_positive("请输入每个文件的行数 j: ", 3)

    directory = Path.cwd() / "test"
    create_batch(directory, file_count, line_count)
    print(f"已在 {directory} 创建 {file_count} 个文件，每个 {line_count} 行随机字符")

    first = sorted(directory.iterdir())[0]
    print(f"处理前示例 {first.name}:")
    for line in first.read_text(encoding="utf-8").splitlines():
        print(f"  {line}")

    renamed = append_everywhere(directory)
    print(f"已改名并追加后缀的文件: {len(renamed)} 个")
    print(f"文件名示例: {' '.join(renamed[:3])}")
    sample = directory / renamed[0]
    print(f"处理后示例 {sample.name}:")
    for line in sample.read_text(encoding="utf-8").splitlines():
        print(f"  {line}")


if __name__ == "__main__":
    main()
