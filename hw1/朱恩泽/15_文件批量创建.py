import random
from pathlib import Path


def main():
    file_count = int(input("请输入文件个数："))
    line_count = int(input("请输入每个文件的行数："))
    if file_count < 0 or line_count < 0:
        raise ValueError("文件个数和行数不能为负数")
    directory = Path("test")
    directory.mkdir(exist_ok=True)
    alphabet = "".join(chr(code) for code in range(32, 127))
    for index in range(1, file_count + 1):
        path = directory / f"file_{index}.txt"
        with path.open("w", encoding="utf-8") as file:
            for _ in range(line_count):
                file.write("".join(random.choices(alphabet, k=50)) + "\n")
    for path in sorted(directory.iterdir()):
        if path.is_file():
            target = path.with_name(path.stem + "_python" + path.suffix)
            if target.exists():
                raise FileExistsError(target)
            with path.open(encoding="utf-8") as file:
                lines = file.readlines()
            with path.open("w", encoding="utf-8") as file:
                for line in lines:
                    file.write(line.rstrip("\r\n") + "_python\n")
            path.rename(target)


if __name__ == "__main__":
    main()
