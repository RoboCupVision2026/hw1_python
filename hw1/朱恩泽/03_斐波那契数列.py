def main():
    numbers = []
    a, b = 0, 1
    for _ in range(20):
        numbers.append(a)
        a, b = b, a + b
    print(*numbers)


if __name__ == "__main__":
    main()
