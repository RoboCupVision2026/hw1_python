import random
import statistics


def main():
    with open("numbers.txt", "w", encoding="utf-8") as file:
        for _ in range(10):
            row = [random.randint(1, 100) for _ in range(3)]
            file.write(",".join(map(str, row)) + "\n")
    with open("numbers.txt", encoding="utf-8") as file:
        values = [int(line.strip().split(",")[1]) for line in file]
    print("最大值：", max(values))
    print("最小值：", min(values))
    print("平均值：", statistics.mean(values))
    print("中位数：", statistics.median(values))


if __name__ == "__main__":
    main()
