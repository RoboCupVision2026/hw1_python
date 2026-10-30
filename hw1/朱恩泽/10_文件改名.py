import random
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent / "img"
    files = [
        path for path in sorted(directory.glob("*.png"))
        if path.is_file() and not path.with_suffix(".jpg").exists()
    ]
    if len(files) < 50:
        raise ValueError("需要至少 50 个可改名的 PNG 文件，请先运行第 9 题")
    for path in random.sample(files, 50):
        path.rename(path.with_suffix(".jpg"))


if __name__ == "__main__":
    main()
