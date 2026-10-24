import random
import re
import string
from pathlib import Path

ALPHABET = string.ascii_uppercase + string.digits
NAME_PATTERN = re.compile(r"^[A-Z0-9]{4}\.(png|jpg)$")


def work_dir():
    return Path(__file__).resolve().parent


def generated_files(directory):
    return sorted(
        path for path in directory.iterdir() if path.is_file() and NAME_PATTERN.match(path.name)
    )


def create_files(directory, count):
    existing = {path.stem for path in generated_files(directory)}
    created = []
    while len(existing) < count:
        name = "".join(random.choice(ALPHABET) for _ in range(4))
        if name in existing:
            continue
        existing.add(name)
        path = directory / f"{name}.png"
        path.write_text(f"{name}\n", encoding="utf-8")
        created.append(path)
    return created


def main():
    directory = work_dir()
    created = create_files(directory, 100)
    files = generated_files(directory)
    print(f"生成目录: {directory.name}，与脚本在同一个文件夹")
    print(f"本次新建 {len(created)} 个文件，当前共 {len(files)} 个随机命名文件")
    print(f"文件名互不相同: {len({path.stem for path in files}) == len(files)}")
    print(f"文件名示例: {' '.join(path.name for path in files[:10])}")


if __name__ == "__main__":
    main()
