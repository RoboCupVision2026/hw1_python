import random
import shutil
import string
from pathlib import Path


def work_dir():
    return Path(__file__).resolve().parent


def ensure_files(directory, rows=10):
    source = directory / "test.txt"
    target = directory / "copy_test.txt"
    if source.exists() and target.exists():
        return source, target
    printable = "".join(ch for ch in string.printable if ch not in "\t\n\r\x0b\x0c")
    with source.open("w", encoding="utf-8") as file:
        for _ in range(rows):
            length = random.randint(5, 20)
            file.write("".join(random.choice(printable) for _ in range(length)) + "\n")
    shutil.copyfile(source, target)
    print("test.txt / copy_test.txt 不存在，已重新生成")
    return source, target


def read_lines(path):
    return path.read_text(encoding="utf-8").splitlines()


def diff_lines(left, right):
    left_lines = read_lines(left)
    right_lines = read_lines(right)
    total = max(len(left_lines), len(right_lines))
    different = []
    for index in range(total):
        first = left_lines[index] if index < len(left_lines) else "<该行缺失>"
        second = right_lines[index] if index < len(right_lines) else "<该行缺失>"
        if first != second:
            different.append((index + 1, first, second))
    return total, different


def main():
    directory = work_dir()
    source, target = ensure_files(directory)
    total, different = diff_lines(source, target)

    print(f"对比 {source.name} 与 {target.name}，共 {total} 行")
    if different:
        print(f"有 {len(different)} 行内容不同：")
        for number, first, second in different:
            print(f"  第 {number} 行: {first!r} != {second!r}")
    else:
        print("两个文件每一行内容都相同，没有不同的行")

    probe = directory / "copy_test_modified.txt"
    lines = read_lines(source)
    target_line = random.randrange(len(lines))
    lines[target_line] = lines[target_line] + "-changed"
    probe.write_text("\n".join(lines) + "\n", encoding="utf-8")
    total, different = diff_lines(source, probe)
    print(f"验证对比逻辑：故意改掉第 {target_line + 1} 行后再比，不同的行号: "
          f"{[number for number, _, _ in different]}")
    probe.unlink()


if __name__ == "__main__":
    main()
