import random
import re
from pathlib import Path

NAME_PATTERN = re.compile(r"^[A-Z0-9]{4}\.(png|jpg)$")


def work_dir():
    return Path(__file__).resolve().parent


def generated_files(directory):
    return sorted(
        path for path in directory.iterdir() if path.is_file() and NAME_PATTERN.match(path.name)
    )


def main():
    directory = work_dir()
    png_files = [path for path in generated_files(directory) if path.suffix == ".png"]
    targets = random.sample(png_files, k=min(50, len(png_files)))
    renamed = []
    for path in targets:
        new_path = path.with_suffix(".jpg")
        path.rename(new_path)
        renamed.append((path.name, new_path.name))

    after = generated_files(directory)
    png_left = sum(1 for path in after if path.suffix == ".png")
    jpg_now = sum(1 for path in after if path.suffix == ".jpg")
    print(f"生成目录: {directory.name}，随机命名文件共 {len(after)} 个")
    print(f"本次把 {len(renamed)} 个 .png 随机改名为 .jpg")
    print(f"改名后: .png {png_left} 个，.jpg {jpg_now} 个")
    for old, new in renamed[:10]:
        print(f"  {old} -> {new}")


if __name__ == "__main__":
    main()
