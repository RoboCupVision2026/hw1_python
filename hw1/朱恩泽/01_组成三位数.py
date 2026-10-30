def main():
    numbers = []
    for hundreds in range(1, 5):
        for tens in range(1, 5):
            for units in range(1, 5):
                if len({hundreds, tens, units}) == 3:
                    numbers.append(hundreds * 100 + tens * 10 + units)
    print(len(numbers))
    print(*numbers)


if __name__ == "__main__":
    main()
