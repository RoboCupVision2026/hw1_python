import random
import string
from pathlib import Path

TAG = "python"


def work_dir():
    return Path(__file__).resolve().parent


def ensure_test_file(path, rows=10):
    if path.exists():
        return
    printable = "".join(ch for ch in string.printable if ch not in "\t\n\r\x0b\x0c")
    with path.open("w", encoding="utf-8") as file:
        for _ in range(rows):
            length = random.randint(5, 20)
            file.write("".join(random.choice(printable) for _ in range(length)) + "\n")
    print(f"{path.name} 不存在，新建了 {rows} 行的示例文件")


def append_with_seek(path):
    with path.open("r+", encoding="utf-8") as file:
        start = file.tell()
        file.seek(0)
        content = file.read()
        file.seek(0)
        file.write(f"{TAG}\n{content}{TAG}\n")
        end = file.tell()
    return start, end


def append_with_rewrite(path):
    content = path.read_text(encoding="utf-8")
    path.write_text(f"{TAG}\n{content}{TAG}\n", encoding="utf-8")


def main():
    path = work_dir() / "test.txt"
    ensure_test_file(path)

    before = path.read_text(encoding="utf-8")
    print(f"修改前 {path.name} 共 {len(before.splitlines())} 行，前 3 行:")
    for line in before.splitlines()[:3]:
        print(f"  {line}")

    first, last = append_with_seek(path)
    print(f"用 seek/tell 定位：写入前指针在 {first}，写入后指针在 {last}")

    lines = path.read_text(encoding="utf-8").splitlines()
    print(f"修改后共 {len(lines)} 行，第一行: {lines[0]}，最后一行: {lines[-1]}")

    append_with_rewrite(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    print(f"再用重写方式追加一次，共 {len(lines)} 行，首行/末行: {lines[0]} / {lines[-1]}")


if __name__ == "__main__":
    main()
