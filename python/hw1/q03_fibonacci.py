def fibonacci(count):
    sequence = [0, 1]
    while len(sequence) < count:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:count]


def main():
    count = 20
    sequence = fibonacci(count)
    print(f"斐波那契数列前 {count} 项：")
    for start in range(0, count, 10):
        print("  ".join(f"{value:>5}" for value in sequence[start:start + 10]))
    print(f"第 {count} 项: {sequence[-1]}")


if __name__ == "__main__":
    main()
