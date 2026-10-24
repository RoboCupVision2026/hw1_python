import random
import string
from pathlib import Path

ALPHABET = string.ascii_uppercase + string.digits


def random_name(length=4):
    return "".join(random.choice(ALPHABET) for _ in range(length))


def create_files(directory, count):
    directory.mkdir(exist_ok=True)
    used = set()
    created = []
    while len(created) < count:
        name = random_name()
        if name in used:
            continue
        used.add(name)
        path = directory / f"{name}.png"
        path.write_text(f"{name}\n", encoding="utf-8")
        created.append(path)
    return created


def main():
    directory = Path.cwd() / "img"
    created = create_files(directory, 100)
    names = [path.name for path in created]
    print(f"目录: {directory}")
    print(f"共创建 {len(created)} 个文件，文件名互不相同: {len(set(names)) == 100}")
    print(f"前 10 个: {' '.join(names[:10])}")


if __name__ == "__main__":
    main()
