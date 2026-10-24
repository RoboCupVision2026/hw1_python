import random
from pathlib import Path


def create_data_file(path, rows, low, high):
    with path.open("w", encoding="utf-8") as file:
        for _ in range(rows):
            file.write(f"{random.randint(low, high)}\n")


def main():
    path = Path.cwd() / "data.txt"
    create_data_file(path, rows=100000, low=1, high=100)
    with path.open(encoding="utf-8") as file:
        values = [int(line) for line in file]
    print(f"已创建 {path}")
    print(f"文件内容: {len(values)} 行，每行一个 1~100 的随机整数")
    print(f"前 5 行: {values[:5]}")
    print(f"最小值 {min(values)}，最大值 {max(values)}，平均值 {sum(values) / len(values):.2f}")
    print(f"文件大小: {path.stat().st_size} 字节")


if __name__ == "__main__":
    main()
