import random
import string
from pathlib import Path

ALPHABET = string.ascii_uppercase + string.digits


def ensure_files(directory, count):
    directory.mkdir(exist_ok=True)
    used = {path.stem for path in directory.iterdir()}
    while len(used) < count:
        name = "".join(random.choice(ALPHABET) for _ in range(4))
        if name in used:
            continue
        used.add(name)
        (directory / f"{name}.png").write_text(f"{name}\n", encoding="utf-8")


def main():
    directory = Path.cwd() / "img"
    ensure_files(directory, 100)
    files = sorted(directory.iterdir())
    print(f"目录: {directory}，改名前的文件数: {len(files)}")

    targets = random.sample(files, 50)
    renamed = []
    for path in targets:
        new_path = path.with_suffix(".jpg")
        path.rename(new_path)
        renamed.append((path.name, new_path.name))

    after = sorted(directory.iterdir())
    png_left = sum(1 for path in after if path.suffix == ".png")
    jpg_now = sum(1 for path in after if path.suffix == ".jpg")
    print(f"随机改名的文件数: {len(renamed)}")
    print(f"改名后: .png 共 {png_left} 个，.jpg 共 {jpg_now} 个")
    for old, new in renamed[:10]:
        print(f"  {old} -> {new}")


if __name__ == "__main__":
    main()
