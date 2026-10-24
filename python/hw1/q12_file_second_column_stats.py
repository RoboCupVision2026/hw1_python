import random
import statistics
from pathlib import Path


def create_matrix_file(path, rows=10, columns=3, low=1, high=100):
    with path.open("w", encoding="utf-8") as file:
        for _ in range(rows):
            values = [str(random.randint(low, high)) for _ in range(columns)]
            file.write(",".join(values) + "\n")


def read_matrix(path):
    with path.open(encoding="utf-8") as file:
        return [[int(item) for item in line.strip().split(",")] for line in file if line.strip()]


def main():
    path = Path.cwd() / "matrix.csv"
    create_matrix_file(path)
    matrix = read_matrix(path)

    print(f"已创建 {path}，{len(matrix)} 行 {len(matrix[0])} 列")
    for row in matrix:
        print("  " + ",".join(f"{value:>3}" for value in row))

    second = [row[1] for row in matrix]
    print(f"第二列: {second}")
    print(f"最大值: {max(second)}")
    print(f"最小值: {min(second)}")
    print(f"平均值: {statistics.mean(second):.2f}")
    print(f"中位数: {statistics.median(second)}")
    print(f"排序后: {sorted(second)}")


if __name__ == "__main__":
    main()
