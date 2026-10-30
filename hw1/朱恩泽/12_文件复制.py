import random
import shutil


def main():
    line_count = int(input("请输入文件行数："))
    if line_count < 0:
        raise ValueError("行数不能为负数")
    alphabet = "".join(chr(code) for code in range(32, 127))
    with open("test.txt", "w", encoding="utf-8") as file:
        for _ in range(line_count):
            file.write("".join(random.choices(alphabet, k=50)) + "\n")
    shutil.copyfile("test.txt", "copy_test.txt")


if __name__ == "__main__":
    main()
